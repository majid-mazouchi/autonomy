# Autonomy

Personal engineering blog by Majid Mazouchi — notes on control and machine learning. Covers control systems, motor control, machine learning, neural networks, and reinforcement learning. Jekyll-based, designed to be hosted on GitHub Pages with zero build configuration.

Features: light/dark mode (auto), inline LaTeX math (MathJax), syntax-highlighted code blocks, reading-progress bar, related-posts suggestions, client-side search, SEO/OpenGraph tags, RSS, sitemap, custom 404.

---

## Quick start — get it online in 10 minutes

### Option A: User site (cleanest URL)

Your site will live at `https://<your-username>.github.io`.

1. Create a new repository on GitHub named exactly **`<your-username>.github.io`** (use your actual username). Make it **public**.
2. Open a terminal in this folder:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-username>.github.io.git
   git push -u origin main
   ```
3. In the repo on GitHub, go to **Settings → Pages**. Under "Build and deployment", set source to **Deploy from a branch**, branch **main**, folder **/ (root)**. Save.
4. Wait 1–2 minutes. Your site is live at `https://<your-username>.github.io`.
5. Open `_config.yml` and set:
   ```yaml
   url: "https://<your-username>.github.io"
   baseurl: ""
   ```

### Option B: Project site (any repo name)

Your site will live at `https://<your-username>.github.io/<repo-name>`.

1. Create any public repo (e.g. `autonomy`).
2. Same git commands as above.
3. Settings → Pages → same.
4. In `_config.yml`:
   ```yaml
   url: "https://<your-username>.github.io"
   baseurl: "/<repo-name>"
   ```
   Leading slash matters; no trailing slash.

---

## Running locally (optional)

Install Ruby 3.x (macOS has it; on Ubuntu `sudo apt install ruby-full build-essential`). Then:

```bash
gem install bundler
bundle install
bundle exec jekyll serve
```

Open <http://localhost:4000>. Every save rebuilds automatically.

---

## Writing a new post

1. Create a file in `_posts/` named `YYYY-MM-DD-slug.md`. The date prefix is required.
2. Use this front-matter:
   ```yaml
   ---
   title: "Your post title"
   subtitle: "A one-line deck shown under the title"
   date: 2026-04-16
   category: "Control Systems"
   slug: your-post-slug
   excerpt: "One or two sentences shown on list pages."
   reading_time: 8
   ---
   ```
3. Write the body in Markdown. Code fences, math, quotes, images, all standard:

   ````markdown
   Inline math: $y = Kp \cdot e + Ki \int e\,dt$

   Display math:
   $$ u(t) = K_p e + K_i \int e\,dt + K_d \dot e $$

   ```python
   def pid_step(err, dt):
       ...
   ```

   > A blockquote.

   ![caption](/assets/img/my-diagram.png)
   ````

4. `category` must match **exactly one** of:
   - `"Control Systems"`
   - `"Motor Control"`
   - `"Machine Learning"`
   - `"Neural Networks"`
   - `"Reinforcement Learning"`

   Related posts and category pages filter on this field — spelling matters.

---

## What's included

### Inline LaTeX math

MathJax loads automatically on post pages. Use `$...$` for inline, `$$...$$` for display. No configuration needed.

### Syntax highlighting

Fenced code blocks are highlighted by Rouge (Jekyll's built-in highlighter). Specify a language for best results:

````
```python
def hello(): print("world")
```
````

The color palette matches the warm editorial theme and adapts to dark mode.

### Light / dark mode

Switches automatically based on the visitor's OS preference (`prefers-color-scheme`). No toggle needed — but you can add one if you want. All colors are CSS variables so adding more themes is easy.

### Reading progress bar

A thin accent-colored bar at the top of post pages fills as you scroll. Post-only (not on home or archive).

### Related posts

The post layout automatically shows up to 3 other posts from the same category at the bottom.

### Client-side search

`/posts/` has a live filter box. Type to narrow. Press `/` anywhere on that page to focus it.

### SEO, RSS, sitemap

Open Graph + Twitter card tags built in. `jekyll-seo-tag`, `jekyll-feed`, and `jekyll-sitemap` plugins generate `<meta>`, `/feed.xml`, and `/sitemap.xml`. You don't need to do anything.

### 404

Custom 404 at `/404.html` matches the site style. GitHub Pages serves it automatically.

---

## Customizing

**Site identity** — `_config.yml`:
- `title`, `tagline`, `description`
- `author`, `email`
- `social.github`, `social.linkedin`

**Colors, fonts, spacing** — `assets/css/main.scss`. CSS variables at the top (`--paper`, `--ink`, `--accent`, fonts) drive everything. Change `--accent` once and it propagates through links, hover states, progress bar, OG image references, etc. Dark-mode variables live in the `@media (prefers-color-scheme: dark)` block right below.

**Navigation** — `_includes/masthead.html`.

**Favicon / social image** — `assets/img/favicon.svg` and `assets/img/og-default.svg`. Both are SVG so they scale cleanly. Replace either with your own if you like.

**Topic names or blurbs** — `categories_list` in `_config.yml`. Renaming a category requires updating the matching `permalink` in `categories/*.html` and the `category:` field in existing posts.

**Adding a new topic**:
1. Add an entry to `categories_list` in `_config.yml`.
2. Copy a file in `categories/` (e.g. `control-systems.html`), change `permalink`, `title`, and the slug it filters on.
3. Use the new category name in post front-matter.

---

## Directory map

```
.
├── _config.yml              # site settings, topics, social links
├── Gemfile                  # Ruby deps (github-pages gem)
├── README.md
├── 404.html                 # custom not-found page
├── search.json              # auto-generated search index
│
├── _layouts/
│   ├── default.html         # base shell: <head>, masthead, footer, MathJax, progress bar
│   ├── post.html            # article template with related-posts section
│   └── page.html            # static pages (About, etc.)
│
├── _includes/
│   ├── masthead.html        # sticky header with nav
│   └── footer.html          # bottom bar
│
├── _posts/                  # one .md file per post
│   └── 2026-04-19-gaussian-processes-interactive-explainer.md
│
├── assets/
│   ├── css/main.scss        # all styles (dark mode, syntax theme, everything)
│   └── img/
│       ├── favicon.svg
│       └── og-default.svg
│
├── index.html               # home page
├── about/index.md           # About page
├── posts/index.html         # archive + search
└── categories/              # topic index + one page per topic
    ├── index.html
    ├── control-systems.html
    ├── motor-control.html
    ├── machine-learning.html
    ├── neural-networks.html
    └── reinforcement-learning.html
```

---

## Things worth knowing

- **Custom domain**: add a `CNAME` file at the repo root containing just your domain (e.g. `blog.example.com`). Point a DNS CNAME at `<your-username>.github.io`. GitHub's docs cover DNS specifics.
- **Images in posts**: drop them in `assets/img/`, reference as `![alt](/assets/img/filename.png)`.
- **Drafts**: create a `_drafts/` folder. Files there aren't published. `bundle exec jekyll serve --drafts` previews them locally.
- **MathJax load cost**: MathJax is loaded only on post pages, and only when the user actually hits a post — the home and archive pages don't pay the cost.

---

## License

Content is yours. The Jekyll scaffolding is MIT-licensed; do what you want.
