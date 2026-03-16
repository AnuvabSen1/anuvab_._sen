<div align="center">

# 🌐 Anuvab Sen — Academic Website

**[anuvabsen.me](https://anuvabsen.me)**

A personal academic website built with **Jekyll** and hosted on **GitHub Pages**. Designed for researchers, PhD students, and academics who want a clean, professional, and customizable web presence.

[![GitHub Pages](https://img.shields.io/badge/Hosted%20on-GitHub%20Pages-blue?logo=github)](https://anuvabsen.me)
[![Jekyll](https://img.shields.io/badge/Built%20with-Jekyll-CC0000?logo=jekyll)](https://jekyllrb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## ✨ Features

- **Dark Mode** — Toggle between light and dark themes with localStorage persistence
- **Responsive Design** — Fully mobile-friendly with hamburger navigation
- **SEO Optimized** — JSON-LD structured data, Open Graph, Twitter Cards, sitemap, and robots.txt
- **Publication Management** — YAML-driven publication list with venue badges, PDF/Code/BibTeX links
- **Selected Publications** — Highlight your top papers on the homepage
- **News Timeline** — Chronological news feed with collapsible "Show more" for older items
- **Talks & Presentations** — Cards with oral/invited/upcoming badges and venue details
- **Academic Services** — Conference and journal reviewer grid
- **Custom Favicon** — Personalized navy/gold "AS" favicon
- **Google Scholar Stats** — Auto-updating citation count via GitHub Actions (optional)

---

## 🚀 Quick Start

### Prerequisites

- [Ruby](https://www.ruby-lang.org/) (>= 2.7)
- [Bundler](https://bundler.io/) (`gem install bundler`)
- [Jekyll](https://jekyllrb.com/) (`gem install jekyll`)
- A GitHub account

### 1. Fork or Clone

```bash
# Fork this repo on GitHub, then clone your fork:
git clone https://github.com/YOUR_USERNAME/anuvab_._sen.git
cd anuvab_._sen
```

### 2. Install Dependencies

```bash
bundle install
```

### 3. Run Locally

```bash
bundle exec jekyll serve
```

Open [http://localhost:4000](http://localhost:4000) in your browser.

### 4. Deploy to GitHub Pages

1. Go to your repo's **Settings → Pages**
2. Set **Source** to `main` branch, root `/`
3. Your site will be live at `https://YOUR_USERNAME.github.io/REPO_NAME/`

### 5. Custom Domain (Optional)

1. Add a `CNAME` file with your domain (e.g., `anuvabsen.me`)
2. Configure DNS:
   - `A` records pointing to GitHub's IPs (`185.199.108.153`, etc.)
   - Or a `CNAME` record pointing to `YOUR_USERNAME.github.io`
3. Enable HTTPS in repo Settings → Pages

---

## 📁 Project Structure

```
├── _config.yml              # Site configuration (name, SEO, links)
├── index.md                 # Homepage content
├── favicon.ico              # Browser favicon
├── robots.txt               # Search engine crawling rules
├── sitemap.xml              # Sitemap for Google indexing
├── CNAME                    # Custom domain
│
├── _layouts/
│   ├── homepage.html        # Homepage layout (sidebar + main)
│   └── default.html         # Sub-page layout (publications, talks, etc.)
│
├── _includes/
│   ├── navigation.md        # Nav bar links
│   ├── news.md              # News timeline
│   ├── selected_pubs.md     # Homepage selected publications
│   ├── talks.md             # Talks & presentations page
│   ├── services.md          # Academic services (reviewer roles)
│   ├── contact.md           # Contact section
│   └── footer.html          # Footer
│
├── _data/
│   ├── publications.yml     # Full publication list
│   └── selected_pubs.yml    # Publications featured on homepage
│
├── _sass/
│   └── minimal-light.scss   # Main stylesheet (light + dark mode)
│
├── assets/
│   ├── css/
│   │   ├── style.css        # Compiled CSS
│   │   ├── pub.css          # Publication page styles
│   │   └── nav.css          # Navigation styles
│   ├── img/                 # Images (avatar, thumbnails, favicons)
│   └── js/                  # JavaScript files
│
├── publications/
│   └── index.html           # Full publications page
├── talks/
│   └── index.html           # Talks page
├── services/
│   └── index.html           # Academic services page
└── teaching/
    └── index.html           # Teaching page
```

---

## 🔧 Customization Guide

### Step 1: Update `_config.yml`

Replace all personal information:

```yaml
title: Your Name
position: PhD Candidate
affiliation: Your University
email: you (at) university.edu
canonical: https://yoursite.com

# Social links
google_scholar: https://scholar.google.com/citations?user=YOUR_ID
github_link: https://github.com/YOUR_USERNAME
linkedin: https://www.linkedin.com/in/YOUR_HANDLE
twitter: https://twitter.com/YOUR_HANDLE

# SEO
keywords: your name, your research areas, your university
description: A brief description of your research for search engines.
```

### Step 2: Update Your Photo

Replace `assets/img/Anuvab_Sen1.jpeg` with your own photo. Recommended:
- **Square crop** (1:1 aspect ratio)
- **800×800px** minimum
- **JPEG format** for smaller file size

### Step 3: Edit Homepage (`index.md`)

The homepage has these sections in order:
1. **About Me** — Two `<div class="justify-text">` paragraphs
2. **Looking Ahead** — Bold red text for research vision
3. **Callout Box** — Collaboration / job market statement
4. **News** — Included from `_includes/news.md`
5. **Selected Publications** — Included from `_includes/selected_pubs.md`
6. **Contact** — Included from `_includes/contact.md`

### Step 4: Add Publications

Edit `_data/publications.yml`. Each entry:

```yaml
- title: "Your Paper Title"
  authors: <strong>Your Name</strong>, Coauthor One, Coauthor Two
  conference_short: CVPR
  conference: IEEE/CVF Conference on Computer Vision and Pattern Recognition <strong>(CVPR)</strong>, 2026.
  pdf: https://arxiv.org/abs/XXXX.XXXXX
  code: https://github.com/your-repo
  bibtex: https://your-bibtex-link
  image: "your_thumbnail.jpg"        # Place in assets/img/
  notes: Accepted                    # Rendered as a red badge
```

For homepage highlights, add entries to `_data/selected_pubs.yml`:

```yaml
main:
  - title: "Your Paper Title"
    authors: <strong>Your Name</strong>, Coauthor
    conference_short: CVPR
    badge_class: cvpr          # CSS class: cvpr (red), wacv (blue), trs (green)
    conference: Full venue name, year.
    notes: Oral                # Optional badge
```

### Step 5: Update News (`_includes/news.md`)

Add news items to the visible section (PhD-era) or the collapsible `#newsmore` div (older items):

```html
<div class="ni">
  <span class="d">Mar 2026</span>
  <div class="c">🎤 <strong>Oral Presentation</strong> of <em>Paper Name</em>
  at <a href="#">Venue</a>, City.</div>
</div>
```

### Step 6: Update Talks (`_includes/talks.md`)

Each talk is a card with a type badge. Supported types:
- `oral` — Red badge and header
- `invited` — Purple badge and header

### Step 7: Update Services (`_includes/services.md`)

Edit the conference and journal reviewer lists in the two-column card grid.

---

## 🎨 Theming

### Colors

The site uses **Georgia Tech** colors. To change them, search and replace in `_sass/minimal-light.scss`:

| Variable | Value | Usage |
|----------|-------|-------|
| Navy | `#13294B` | Headers, text, nav background |
| Gold | `#B3A369` | Accents, borders, badges, links on hover |
| Dark BG | `#0d1117` | Dark mode background |
| Dark Card | `#161b22` | Dark mode cards |

### Dark Mode

Dark mode is toggled via the 🌙/☀️ button in the navbar. It:
- Adds `body.dark-mode` (or `body.dm` in the preview) class
- Persists via `localStorage`
- All dark mode CSS is in `_sass/minimal-light.scss` under `body.dark-mode` selectors

### Custom Favicon

Replace the favicon files in `assets/img/`:
- `favicon-16x16.png`, `favicon-32x32.png`, `favicon-48x48.png`, `favicon-96x96.png`
- `favicon-180x180.png`, `favicon-192x192.png`, `favicon-512x512.png`
- `apple-touch-icon.png`
- `favicon.ico` (root directory)

Use [favicon.io](https://favicon.io/) or [realfavicongenerator.net](https://realfavicongenerator.net/) to generate all sizes from a single image.

---

## 🔍 SEO Checklist

This site is pre-configured for strong search engine visibility:

- [x] **JSON-LD Person schema** — Name, photo, job title, employer, social links
- [x] **JSON-LD WebSite schema** — Site name, URL, description
- [x] **Open Graph meta tags** — og:title, og:description, og:image (absolute URL)
- [x] **Twitter Cards** — summary_large_image with photo
- [x] **Canonical URL** — Prevents duplicate content
- [x] **Meta description** — Full research description, not just your name
- [x] **Expanded keywords** — Name variants, venue names, paper names
- [x] **robots.txt** — `Allow: /` for full crawling
- [x] **sitemap.xml** — All pages with current dates

### After Deploying

1. **Submit sitemap** to [Google Search Console](https://search.google.com/search-console):
   - Add property → URL prefix → `https://yoursite.com`
   - Go to Sitemaps → Submit `https://yoursite.com/sitemap.xml`

2. **Verify ownership** via HTML tag or DNS record

3. **Request indexing** for your homepage URL

4. **Link your site** from Google Scholar profile, LinkedIn, Twitter, and GitHub

---

## 📊 Google Scholar Stats (Optional)

The `google_scholar_crawler/` directory contains a GitHub Action that can auto-update your citation count. To enable:

1. Edit `.github/workflows/google_scholar_crawler.yml`
2. Set your Google Scholar ID
3. The action runs on a schedule and updates `gs_data_shieldsio.json`

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

Feel free to use this template for your own academic website. If you do, a link back is appreciated but not required.

---

<div align="center">

**Built with ❤️ by [Anuvab Sen](https://anuvabsen.me)**

*If you found this useful, consider giving it a ⭐ on GitHub!*

</div>
