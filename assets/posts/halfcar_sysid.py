"""
Half-car suspension system identification via differentiable simulation.

Companion script to "Differentiable Physics Engines: Warp and Newton"
(Physics-ML Monograph Series, Part II). Pure NumPy: the reverse pass is a
hand-written adjoint (a "tape" of 40 lines), the same mathematics NVIDIA
Warp generates automatically for kernel programs. Run time: ~1 minute CPU.

Model: pitch-plane half car, states [z, zd, th, thd]
  zf  = z - a*th - u_f(t)      front suspension deflection
  zr  = z + b*th - u_r(t)      rear suspension deflection
  Ff  = -kf*zf - cf*zfd
  Fr  = -kr*zr - cr*zrd
  m z'' = Ff + Fr,   I th'' = -a Ff + b Fr
Semi-implicit Euler, dt = 1 ms, horizon 4 s.
Identified parameters: theta = [kf, cf, kr, cr] (log-parameterized).
"""

import numpy as np
import time

rng = np.random.default_rng(7)

# ---------------- ground truth vehicle ----------------
M, I = 1400.0, 2100.0          # sprung mass [kg], pitch inertia [kg m^2]
A_, B_ = 1.2, 1.5              # CG to front / rear axle [m]
TRUE = dict(kf=32000.0, cf=1500.0, kr=28000.0, cr=1300.0)

DT, T = 1e-3, 4.0
N = int(T / DT)
V = 10.0                        # vehicle speed [m/s]
BUMP_H, BUMP_L = 0.05, 1.0      # half-sine bump: 5 cm high, 1 m long
T0F = 0.5                       # front axle hits bump at 0.5 s
T0R = T0F + (A_ + B_) / V       # rear delayed by wheelbase / speed

def road(t0):
    """Half-sine bump displacement and velocity time series."""
    t = np.arange(N) * DT
    dur = BUMP_L / V
    ph = (t - t0) / dur
    m = (ph >= 0) & (ph <= 1)
    u = np.zeros(N); ud = np.zeros(N)
    u[m] = BUMP_H * np.sin(np.pi * ph[m])
    ud[m] = BUMP_H * np.pi / dur * np.cos(np.pi * ph[m])
    return u, ud

UF, UFD = road(T0F)
UR, URD = road(T0R)

# ---------------- forward simulation ----------------
def simulate(kf, cf, kr, cr):
    z = np.zeros(N + 1); zd = np.zeros(N + 1)
    th = np.zeros(N + 1); thd = np.zeros(N + 1)
    for t in range(N):
        zf = z[t] - A_ * th[t] - UF[t]
        zfd = zd[t] - A_ * thd[t] - UFD[t]
        zr = z[t] + B_ * th[t] - UR[t]
        zrd = zd[t] + B_ * thd[t] - URD[t]
        Ff = -kf * zf - cf * zfd
        Fr = -kr * zr - cr * zrd
        zdd = (Ff + Fr) / M
        thdd = (-A_ * Ff + B_ * Fr) / I
        zd[t + 1] = zd[t] + DT * zdd
        z[t + 1] = z[t] + DT * zd[t + 1]
        thd[t + 1] = thd[t] + DT * thdd
        th[t + 1] = th[t] + DT * thd[t + 1]
    return z, zd, th, thd

# ---------------- loss + hand-written adjoint (the "tape") ----------------
SZ, STH = 1e-3, 5e-4  # loss weights ~ sensor scales: 1 mm, 0.5 mrad

def loss_and_grad(kf, cf, kr, cr, z_meas, th_meas):
    z, zd, th, thd = simulate(kf, cf, kr, cr)
    rz = (z[1:] - z_meas) / SZ
    rt = (th[1:] - th_meas) / STH
    L = (rz @ rz + rt @ rt) / N

    gz = gzd = gth = gthd = 0.0
    gkf = gcf = gkr = gcr = 0.0
    for t in range(N - 1, -1, -1):
        # loss injects adjoint at state t+1
        gz += 2.0 * rz[t] / (SZ * N)
        gth += 2.0 * rt[t] / (STH * N)
        # th_{t+1} = th_t + dt*thd_{t+1};  thd_{t+1} = thd_t + dt*thdd
        gthd += DT * gth
        gthdd = DT * gthd
        # z_{t+1} = z_t + dt*zd_{t+1};    zd_{t+1} = zd_t + dt*zdd
        gzd += DT * gz
        gzdd = DT * gzd
        # accelerations -> forces
        gFf = gzdd / M - A_ * gthdd / I
        gFr = gzdd / M + B_ * gthdd / I
        # recompute step-t deflections (checkpoint-free: state was stored)
        zf = z[t] - A_ * th[t] - UF[t]
        zfd = zd[t] - A_ * thd[t] - UFD[t]
        zr = z[t] + B_ * th[t] - UR[t]
        zrd = zd[t] + B_ * thd[t] - URD[t]
        # parameter gradients
        gkf += -zf * gFf;  gcf += -zfd * gFf
        gkr += -zr * gFr;  gcr += -zrd * gFr
        # forces -> deflections -> state at t
        gzf = -kf * gFf;  gzfd = -cf * gFf
        gzr = -kr * gFr;  gzrd = -cr * gFr
        gz += gzf + gzr
        gth += -A_ * gzf + B_ * gzr
        gzd += gzfd + gzrd
        gthd += -A_ * gzfd + B_ * gzrd
    return L, np.array([gkf, gcf, gkr, gcr]), (z, th)

# ---------------- adjoint verification vs central finite differences ----------------
def fd_grad(p, z_meas, th_meas, rel=1e-6):
    g = np.zeros(4)
    for i in range(4):
        e = np.zeros(4); e[i] = p[i] * rel
        Lp, _, _ = loss_and_grad(*(p + e), z_meas, th_meas)
        Lm, _, _ = loss_and_grad(*(p - e), z_meas, th_meas)
        g[i] = (Lp - Lm) / (2 * e[i])
    return g

# ---------------- Adam on log-parameters ----------------
def identify(p0, z_meas, th_meas, iters=500, lr=0.03, verbose_tag=""):
    lp = np.log(np.array(p0, float))
    m = np.zeros(4); v = np.zeros(4)
    for it in range(1, iters + 1):
        p = np.exp(lp)
        L, g, _ = loss_and_grad(*p, z_meas, th_meas)
        glp = g * p                       # chain rule through log-param
        m = 0.9 * m + 0.1 * glp
        v = 0.999 * v + 0.001 * glp * glp
        mh = m / (1 - 0.9 ** it); vh = v / (1 - 0.999 ** it)
        lp -= lr * mh / (np.sqrt(vh) + 1e-12)
    return np.exp(lp), L

def report(tag, p_hat, ref):
    names = ["kf", "cf", "kr", "cr"]
    errs = [(p_hat[i] / ref[n] - 1) * 100 for i, n in enumerate(names)]
    print(f"{tag}: " + "  ".join(f"{n}={p_hat[i]:8.1f} ({e:+5.2f}%)"
                                 for i, (n, e) in enumerate(zip(names, errs))))
    return errs

if __name__ == "__main__":
    p_true = np.array([TRUE["kf"], TRUE["cf"], TRUE["kr"], TRUE["cr"]])
    z_t, _, th_t, _ = simulate(*p_true)
    p0 = [18000.0, 800.0, 18000.0, 800.0]   # deliberately poor initial guess

    # --- 1. adjoint correctness ---
    zm = z_t[1:] + rng.normal(0, 1e-3, N)
    tm = th_t[1:] + rng.normal(0, 5e-4, N)
    _, g_adj, _ = loss_and_grad(*np.array(p0), zm, tm)
    g_fd = fd_grad(np.array(p0), zm, tm)
    rel = np.max(np.abs(g_adj - g_fd) / (np.abs(g_fd) + 1e-12))
    print(f"[1] adjoint vs central FD: max relative difference = {rel:.2e}")

    # --- 2. identification vs measurement noise ---
    results = {}
    for tag, (sz, st) in {"noise-free": (0, 0),
                          "1 mm / 0.5 mrad": (1e-3, 5e-4),
                          "5 mm / 2.5 mrad": (5e-3, 2.5e-3)}.items():
        zm = z_t[1:] + rng.normal(0, sz, N)
        tm = th_t[1:] + rng.normal(0, st, N)
        t0 = time.time()
        p_hat, L = identify(p0, zm, tm)
        dt_wall = time.time() - t0
        errs = report(f"[2] {tag:16s}", p_hat, TRUE)
        results[tag] = (p_hat, errs, dt_wall, L)
    print(f"    (each run: 500 Adam iters, {N}-step rollouts, "
          f"{results['noise-free'][2]:.1f}s wall on CPU)")

    # --- 3. drift detection: front damper degrades 25% ---
    WORN = dict(TRUE); WORN["cf"] = TRUE["cf"] * 0.75
    z_w, _, th_w, _ = simulate(WORN["kf"], WORN["cf"], WORN["kr"], WORN["cr"])
    zm = z_w[1:] + rng.normal(0, 1e-3, N)
    tm = th_w[1:] + rng.normal(0, 5e-4, N)
    p_hat_h, _ = identify(results["1 mm / 0.5 mrad"][0], zm, tm, iters=300)
    print("[3] worn-damper dataset (true cf reduced 25%):")
    report("    healthy-baseline re-fit", p_hat_h, TRUE)
    print(f"    fitted cf shift vs healthy estimate: "
          f"{(p_hat_h[1]/results['1 mm / 0.5 mrad'][0][1]-1)*100:+.1f}% "
          f"(injected: -25.0%)")
