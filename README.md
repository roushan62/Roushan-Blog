# RoushanTalky — StartupTalky Style Blogger Theme

**Ek hi complete XML file** — `Roushan-Blog-Theme.xml` — jise Blogger pe **Restore** karke aap
poori news-magazine website (StartupTalky jaisi) chala sakte ho.

Brand: **Roushan Gupta** • Niche: **Startups • Business • Technology • AI • Marketing**

| | |
|---|---|
| File to upload | [`Roushan-Blog-Theme.xml`](Roushan-Blog-Theme.xml) |
| Size | 119 KB (25 KB gzip) — **zero** external JS/CSS library |
| Layout | Blogger Layout v3, widget version 2, responsive |
| Colors | Red `#e5094b` + Dark navy `#0e1424` + clean white cards |
| Fonts | Sora (headings) + Inter (body), Google Fonts, `display=swap` |

---

## 1. Upload kaise kare (2 minute)

1. [Blogger.com](https://www.blogger.com) → apna blog kholo
2. Left menu → **Theme**
3. Theme card ke **⋮** (3 dots) → **Backup** (purana theme save kar lo)
4. **⋮** → **Restore** → `Roushan-Blog-Theme.xml` select → **Upload**
5. Blog kholo — done

> File ko hamesha **UTF-8** rakho. Word / Google Docs me copy-paste mat karo.

---

## 2. Upload ke turant baad (IMPORTANT)

### A) Blog title + description — **Settings → Basic**

| Field | Value |
|---|---|
| **Title** | `Roushan Gupta \| Startup, Business & AI Stories` |
| **Description** | `Roushan Gupta writes about startups, business models, technology, AI tools and digital marketing. Latest news, reviews, guides and success stories.` |

Ye title/description automatically homepage `<title>`, `og:site_name` aur **WebSite schema** me chala jata hai.

### B) Apna naam, photo, social links — **Theme → Customize → Advanced**

Sab kuch bina code ke edit hota hai (skin variables):

| Variable | Kya hai |
|---|---|
| `Author Name` / `Author Role` / `Author Short Bio` | Author box + sidebar card + footer |
| `Author Photo URL` | Author box, sidebar, **Person schema** ka image |
| `Logo Image URL` | Set karo → image logo; khaali chhodo → text logo (`Text Logo Short Name` = `RG`) |
| `Facebook / X / Instagram / LinkedIn / YouTube / WhatsApp URL` | Top bar + author box + footer + **Person schema `sameAs`** (khaali = icon hide) |
| `Newsletter Subscribe URL` | Sidebar newsletter form + header Subscribe button (khaali = WhatsApp/RSS CTA) |
| `Primary Color`, `Gradient Partner Color`, `Dark Color` | Poora theme recolour |
| `Default Meta Description` / `Default Share Image URL` | Fallback SEO + og:image |

### C) Pages banao — **Pages → New page** (Custom permalink me ye slug daalo)

`about`, `contact`, `privacy-policy`, `disclaimer`, `terms`
(Footer + menu inhi slugs pe linked hain: `/p/about.html` etc.)

### D) Menu edit karo — **Layout**

`Main Menu` (desktop) aur `Mobile Menu` (drawer) widgets me links badlo.
Default labels: **Startups, Business, Technology, AI, Marketing, Success Story**.

### E) Posts me labels lagao

Har post me label do — `Startups`, `Business`, `Technology`, `AI`, `Marketing`, `Success Story`.
Label se hi **category chip, breadcrumb, tags, related posts, schema `articleSection`** bante hain.

### F) AdSense

**Layout → Sidebar → Advertisement → Edit** → apna AdSense code paste karo.

---

## 3. Features

**Design / UX**
- Sticky nav + shrinking header, full-screen search overlay, mobile drawer menu
- Homepage: **Featured hero (1 big + 2 side)** → **Latest Stories grid**
- **Trending ticker** (auto, blog feed se), reading progress bar, back-to-top
- Scroll-reveal animations, card hover zoom, skeleton loaders, **dark mode** (localStorage + system preference, `prefers-reduced-motion` respected)
- Post page: breadcrumb, category chips, reading time, auto **Table of Contents**, share buttons (WhatsApp / X / Facebook / LinkedIn / Telegram / Copy), author box, prev-next pager, **related posts** (label feed se), inline comment form
- Custom **404** page, label/search/archive headers with `noindex`

**SEO**
- Per-page `<title>` logic (home / post / page / label / search / archive)
- Meta description (post → blog → theme fallback), canonical, robots (search & archive = `noindex, follow`)
- Open Graph + Twitter Cards, `theme-color`, favicon, viewport
- **JSON-LD**: `WebSite` + `SearchAction`, `Person` (Roushan Gupta, `sameAs` socials), `BlogPosting`, `BreadcrumbList` (post + label)
- Semantic HTML + `itemprop` microdata, lazy images, no render-blocking library

**Widgets included (Layout me editable)**
Header (logo) • Main Menu • Mobile Menu • Blog • About Roushan Gupta • Trending Now (Popular Posts) • Categories • Newsletter • Browse Topics • Advertisement • Footer About / Quick Links / Categories / Stay Connected • Attribution

---

## 4. Verification (jo tests is build pe chalaye gaye)

| Check | Result |
|---|---|
| XML well-formed (`xml.etree` parse) | ✅ pass |
| Skin: 1 skin, 28 variables, saare `$(var)` resolve | ✅ pass |
| Widgets: 15 widgets, sab me `main` includable, unique ids; 11 sections | ✅ pass |
| `<b:include>` → sab includables defined (missing = 0) | ✅ pass |
| HTML tags balance (6 view render) | ✅ 0 mismatch / 0 unclosed |
| JS: `node --check` + DOM-stub execution (drawer, search, dark mode, copy link, comment iframe, TOC, reading time, ticker, related) | ✅ no runtime error |
| JSONP feed renderers (real payload + empty/broken payload) | ✅ escaping + fallback OK |
| JSON-LD: 4 blocks × 2 scenarios (with/without labels, image, socials) | ✅ 8/8 valid JSON |
| Rendered views: home / post / page / label / search / 404 | ✅ titles, meta, robots, cards, comments nesting, pager sab sahi |

**Preview:** `preview/` folder (repo ke bahar) me isi theme ka rendered HTML + CSS + JS static server pe
chalaya gaya tha, design dekhne ke liye.

---

## 5. Chhoti si baat

- Theme me `b:css='false'` aur `b:js='false'` set hai — isse Blogger ka unused default CSS/JS bundle load
  nahi hota (fast PageSpeed). Iska matlab **JS-dependent Blogger gadgets** (Blog Archive, Contact Form,
  Followers) kaam nahi karenge. Agar aapko wo chahiye, to `<html ...>` tag me `b:js='false'` hata do.
- Blogger ka default blue **Navbar** gadget theme me maujood hai lekin render nahi hota (Layout me dikhega, blog pe nahi).

- Footer credit (`Designed with ♥ by Roushan Gupta`) aur `Powered by Blogger` link rakho — Blogger terms ke hisaab se attribution zaroori hai.
- Post ka **pehla image** automatically card/hero image banta hai (Blogger ka featured image). Image 16:9 ya 1200×630 rakho to sabse accha dikhega.
