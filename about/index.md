---
layout: page
title: "About"
kicker: "Colophon"
blurb: "Who writes here, and why."
permalink: /about/
---

Hi — I'm **{{ site.author }}**. This is my working notebook on control and machine learning — the engineering stack that sits under autonomous systems. My professional page is at [majid-mazouchi.github.io](https://majid-mazouchi.github.io).

I started this because the internet has great resources on each of these topics in isolation, but surprisingly little that sits at the intersection. A PID tutorial won't tell you how reinforcement learning relates to it. A deep learning course won't tell you why the stability arguments you see in an LQR derivation matter when you're training a controller with PPO.

Everything here is written in the spirit of a good lab notebook: show the math, show the code, show what actually happened when you ran it.

## What you'll find

- **Control Systems** — classical and modern control theory, worked through with examples.
- **Motor Control** — driving DC, BLDC, and stepper motors, plus the sensors and electronics around them.
- **Machine Learning** — the classical ML toolkit, with a bias toward problems in signal processing and dynamics.
- **Neural Networks** — architectures and training, especially where they overlap with system identification and control.
- **Reinforcement Learning** — policy optimization, actor-critic methods, and how they connect to adaptive and optimal control.

## Contact

Drop me a line at [{{ site.email }}](mailto:{{ site.email }}){% if site.social.github and site.social.github != "" %} or open an issue on [the GitHub repo](https://github.com/{{ site.social.github }}){% endif %}.

## Colophon

Built with [Jekyll](https://jekyllrb.com), typeset in Fraunces and Newsreader with DM Mono for labels and code, hosted on GitHub Pages.{% if site.social.github and site.social.github != "" %} Source is on [GitHub](https://github.com/{{ site.social.github }}).{% endif %}
