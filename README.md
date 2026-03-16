<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:B3A369,100:003057&height=180&section=header&text=anuvabsen.me&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Academic%20Personal%20Website%20•%20Built%20with%20Jekyll&descAlignY=58&descSize=16&descColor=ffffff" width="100%" />

<a href="https://anuvabsen.me"><img src="https://img.shields.io/badge/🌐_Live_Site-anuvabsen.me-003057?style=for-the-badge" /></a>
<a href="https://github.com/AnuvabSen1/anuvab_._sen/fork"><img src="https://img.shields.io/badge/Fork_This_Template-B3A369?style=for-the-badge&logo=github&logoColor=white" /></a>
<img src="https://img.shields.io/github/stars/AnuvabSen1/anuvab_._sen?style=for-the-badge&color=B3A369" />
<img src="https://img.shields.io/github/forks/AnuvabSen1/anuvab_._sen?style=for-the-badge&color=003057" />

</div>

---

## About

This is the source code for [**anuvabsen.me**](https://anuvabsen.me) — the personal academic website of **Anuvab Sen**, a Ph.D. Candidate at the Georgia Institute of Technology. The site is built with [Jekyll](https://jekyllrb.com/) and hosted on [GitHub Pages](https://pages.github.com/).

**Features:**

- Clean, responsive academic layout with a fixed sidebar and sticky navigation
- Publication list powered by a YAML data file — no manual HTML editing needed
- News timeline with collapsible "Show more" for older entries
- Separate pages for Publications, Teaching, Academic Services, and Talks
- Google Scholar auto-crawler for citation stats
- Georgia Tech gold & navy color scheme with smooth hover interactions
- Mobile-friendly responsive design
- ClustrMaps visitor tracking widget

---

## 🚀 Use This as a Template

Want to build your own academic website? Fork this repo and customize it in a few steps.

### Step 1 — Fork & Rename

Click the **Fork** button at the top of this page. Then rename the repository to `your-github-username.github.io` for a free GitHub Pages site, or to any name if you plan to use a custom domain.

### Step 2 — Edit `_config.yml`

Update your personal info:

```yaml
title: Your Name
position: PhD Student  # or Professor, Postdoc, etc.
affiliation: Your University
affiliation_link: https://your-university.edu
email: you (at) university.edu

google_scholar: https://scholar.google.com/citations?user=YOUR_ID
github_link: https://github.com/your-username
linkedin: https://www.linkedin.com/in/your-profile/
twitter: https://twitter.com/your-handle

avatar: /assets/img/your-photo.jpeg
```

### Step 3 — Add Your Photo

Replace `assets/img/Anuvab_Sen1.jpeg` with your own photo. A square image (e.g., 800×800) works best.

### Step 4 — Update Content

| File | What to edit |
|:-----|:-------------|
| `index.md` | Your About Me bio and research description |
| `_includes/news.md` | News and announcements timeline |
| `_includes/contact.md` | Mailing address, office, phone |
| `_includes/services.md` | Conference/journal reviewing services |
| `_includes/talks.md` | Invited talks and presentations |
| `_data/publications.yml` | Your publication list (see format below) |
| `_data/preprints.yml` | Preprints and under-review papers |
| `teaching.md` | Courses taught or TA'd |

### Step 5 — Adding Publications

Publications are defined in `_data/publications.yml`. Each entry follows this format:

```yaml
- title: "Your Paper Title"
  authors: <strong>Your Name</strong>, Coauthor One, Coauthor Two
  conference_short: CVPR
  conference: IEEE/CVF Conference on Computer Vision <strong>(CVPR)</strong>, 2026.
  pdf: https://link-to-paper.pdf
  code: https://github.com/your-repo
  bibtex: https://link-to-bibtex
  image: "your-paper-thumbnail.png"  # place in assets/publications/
  notes: Oral Presentation  # optional badge
```

### Step 6 — Deploy

**Option A — GitHub Pages (free):**

Push to your repo. Go to **Settings → Pages → Source** and select the `main` branch. Your site will be live at `https://your-username.github.io/repo-name/`.

**Option B — Custom domain:**

Update the `CNAME` file with your domain (e.g., `yourname.me`). In your domain registrar, point it to GitHub Pages:
- A record: `185.199.108.153`
- CNAME record: `your-username.github.io`

**Option C — Local development:**

```bash
gem install bundler jekyll
bundle install
bundle exec jekyll serve
# Open http://localhost:4000
```

---

## 📁 Project Structure

```
├── _config.yml            # Site-wide settings
├── _data/
│   ├── publications.yml   # Publication entries
│   ├── preprints.yml      # Preprint entries
│   └── navigation.yml     # Navbar links
├── _includes/
│   ├── news.md            # News timeline
│   ├── contact.md         # Contact info
│   ├── publications.md    # Publication template
│   ├── services.md        # Academic services
│   └── talks.md           # Talks list
├── _layouts/
│   ├── homepage.html      # Main page layout
│   ├── default.html       # Inner page layout
│   └── simple.html        # Minimal layout
├── _sass/
│   └── minimal-light.scss # Main stylesheet
├── assets/
│   ├── css/               # Additional CSS (pub, nav)
│   ├── img/               # Avatar, logos, favicons
│   ├── js/                # JavaScript utilities
│   └── publications/      # Paper thumbnail images
├── index.md               # Homepage content
├── publications.md        # Publications page
├── services.md            # Academic services page
├── teaching.md            # Teaching page
└── talks.md               # Talks page
```

---

## 🎨 Customization Tips

**Change the color scheme** — Edit the CSS variables in `assets/css/pub.css`:
```css
:root {
  --global-theme-color: #13294B;  /* primary navy */
  --global-hover-color: #B3A369;  /* gold accent */
}
```
And update the navbar gradient in `assets/css/nav.css`.

**Change fonts** — Edit the `@import` lines at the top of `_sass/minimal-light.scss`.

**Add new pages** — Create a new `.md` file with a YAML front matter header:
```yaml
---
layout: default
title: Your Page Title
permalink: /your-page/
---
```
Then add a link in `_data/navigation.yml`.

---

## 📄 License

This project is licensed under the MIT License. Feel free to use this as a template for your own academic website. If you do, a link back to this repo or a star would be appreciated!

---

<div align="center">

**Built by [Anuvab Sen](https://anuvabsen.me)** · PhD Candidate · Georgia Institute of Technology

<a href="https://www.linkedin.com/in/anuvabsen/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" /></a>
<a href="https://scholar.google.com/citations?user=aQkZOqQAAAAJ&hl=en"><img src="https://img.shields.io/badge/Scholar-4285F4?style=flat-square&logo=googlescholar&logoColor=white" /></a>
<a href="https://anuvabsen.me"><img src="https://img.shields.io/badge/Website-003057?style=flat-square&logo=googlechrome&logoColor=white" /></a>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:B3A369,100:003057&height=100&section=footer" width="100%" />
