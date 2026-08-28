# Roushan Gupta — Light Blogger Theme

A clean, minimal, white-and-blue personal blog theme for Blogger (Blogspot), hand-coded in
one XML file. Style merges **StartupTalky** (featured hero, card grids, category sections,
author boxes, social share, related posts) with **Skill India** (institutional clarity,
trustworthy typography, airy whitespace).

Brand: **Roushan Gupta** • Niche: **Startups • Business • Technology • AI • Marketing**

| | |
|---|---|
| File to upload | [`Roushan-Gupta-Blogger-Theme.xml`](Roushan-Gupta-Blogger-Theme.xml) |
| Size | ~121 KB — **zero** external JS/CSS libraries, one Google Fonts request |
| Layout | Blogger Layout v3, widget version 2, fully responsive (320→1440+) |
| Colors | White `#FFFFFF` bg, `#F7F8FA` alt sections, ink `#1A1A1A`, ONE accent `#2563EB` |
| Fonts | Inter (headings + body), preconnected, `display=swap` |
| SEO | Meta description, canonical, Open Graph, Twitter Card, JSON-LD (Person + WebSite + BlogPosting + BreadcrumbList) |

## What's inside

- **Sticky white header** — text logo, nav, search overlay, mobile drawer
- **Homepage** — hero featured card + card grid, alternating category sections (feed-driven), newsletter strip
- **Listing pages** (label / search / archive) — 3/2/1-column card grid + pagination, light breadcrumbs
- **Post page** — featured image, "Written by Roushan Gupta" byline + date + reading time, auto table of contents, share buttons (WhatsApp, Facebook, X, LinkedIn, Telegram, copy link), author bio box, related posts (label feed), native threaded comments
- **Sidebar** (posts/pages) — About + socials, Popular Posts, Recent Posts, Categories, Newsletter, 300×250 ad slot; 728×90 header ad slot on all pages
- **Footer** — 4 columns (About, Quick Links, Categories, Social), copyright, back-to-top
- **Custom 404**, no dark mode, no gradients, CLS-safe images (aspect-ratio + dimensions)

## Edit points (search these tags inside the XML)

| Tag | What to change |
|---|---|
| `[EDIT-1 LOGO]` | Header logo text or image |
| `[EDIT-2 MENU]` | Header + footer navigation links |
| `[EDIT-3 COLOR]` | Accent color (also via Theme Designer → Advanced → Colors) |
| `[EDIT-4 AUTHOR]` | Author photo + bio (post box and sidebar About widget) |
| `[EDIT-5 SOCIAL]` | Social profile URLs (schema `sameAs` + icons) |
| `[EDIT-6 SEARCH]` | Google Search Console verification meta tag |
| `[EDIT-7 ANALYTICS]` | Google Analytics 4 snippet |
| `[EDIT-8 CATEGORIES]` | Homepage category sections list |
| `[EDIT-9 ADS]` | AdSense ad slots |
| `[EDIT-10 NEWSLETTER]` | Newsletter form action URL |

## Upload (backup first!)

1. Blogger → **Theme** → ⋮ (top-right of the theme card) → **Backup** — download and save your current theme.
2. ⋮ → **Restore** → upload `Roushan-Gupta-Blogger-Theme.xml`.
3. Blog posts, pages and comments are untouched — only the presentation layer changes.
4. Open **Layout** to edit sidebar widgets (About, Newsletter, ad slots) without touching code.
5. Set your accent color in **Theme → Customize → Advanced → Colors**.

## Validation performed

- XML well-formed; single `b:skin`; unique section/widget IDs; every `b:include` resolves; every widget has a `main` includable; `widget-settings` precede includables
- Full template engine simulation of all 7 view types (home, post, page, label, search, archive, 404) + edge cases (no image / no labels / comments off / threading off / empty results): balanced HTML, no unresolved `data:` refs
- All JSON-LD blocks parse as valid JSON in every conditional branch
- Main JS + config JS pass `node --check` and a mock-DOM runtime smoke test (feed render paths included)
- CSS: 339/339 braces balanced, all 15 custom properties defined, 14 responsive breakpoints
