# Roushan Pro v1.1 — Complete Blogger Theme (100% Apna)

**Roushan Gupta / Roushan Kumar** ke personal brand blog ke liye — **Business • Tech • AI**.
Same modern look (teal + navy), lekin puri tarah **clean rebuild**:

- ❌ SoraTemplates / Gooyaabi credit links — **removed**
- ❌ Encrypted credit-lock JavaScript (`_0x...`) — **removed**
- ❌ Font Awesome / Remixicon / jQuery CDN — **removed** (sirf inline SVG icons)
- ✅ 100% vanilla code — koi third-party template code nahi, blog **poora aapka**
- ✅ Full SEO + fast + dark mode + live search + related posts

**Blogger pe upload karne wali file:** [`Roushan-Blog-Theme.xml`](Roushan-Blog-Theme.xml)

Design pehle dekhna ho to `preview/index.html` kholo (ya repo me preview folder).

---

## 1. Blogger pe upload kaise kare (2 minute)

1. [Blogger.com](https://www.blogger.com) → apna blog kholo
2. Left menu → **Theme**
3. Theme card pe **⋮** (three dots) → pehle **Backup** (apna purana theme save kar lo)
4. Phir **⋮** → **Restore** → `Roushan-Blog-Theme.xml` select karo → **Upload**
5. Blog kholo — done! 🎉

> **Note:** File ko hamesha UTF-8 hi rakho — Word/Google Docs me copy-paste mat karo.

---

## 2. Upload ke turant baad ye karo (important)

### A) Pages banao
**Pages → New page** — ye 5 pages banao (menu/footer me already linked hain):

| Page title | Permalink (URL) |
|---|---|
| About | `about` |
| Contact | `contact` |
| Privacy Policy | `privacy-policy` |
| Terms & Conditions | `terms` |
| Disclaimer | `disclaimer` |

(Page banate waqt right side **Page settings → Custom permalink** me upar wala slug daalo.)

### B) Posts me Labels lagao
Har post me label add karo: `Business`, `Technology`, `AI`, `Startups`, `AI Tools`, `Marketing`…
- Homepage ke **topic cards** aur **menu** inhi labels se linked hain
- **Related posts** bhi label se automatic aate hain
- Card image = post ki **pehli image** (ya featured image)

### C) Social links apne daalo
3 jagah placeholder `#` links hain — apne profile URLs se replace karo:
- **Layout → Sidebar → "About Me" widget → Edit** (pencil icon)
- **Layout → Footer Columns → "About" widget → Edit**
- Search karke bhi mil jayega: Theme → Edit HTML → `href="#"`

### D) Apni photo lagani ho to
- **Layout → Header (Logo) → Edit** → image upload karo (placement: *Instead of title and description*) — text logo ki jagah image logo lag jayega
- Sidebar "About Me" me avatar chahiye to widget me `<div class="about-ava">R</div>` ki jagah `<img src="photo-URL" class="about-ava" style="object-fit:cover"/>` likho

---

## 3. Blogger me kya-kya handle ho sakta hai (Layout se, bina code chhue)

| Kya badalna hai | Kahan |
|---|---|
| Menu (Home/Business/Tech/AI/About/Contact) | **Layout → Main Menu** |
| Hero section ka text + buttons | **Layout → Hero Section → Edit** |
| 3 Topic cards (Business/Tech/AI) | **Layout → Topics Section → Edit** |
| Featured slider / Trending ticker | Homepage sections (feed se automatic) |
| AdSense header + sidebar slots | **Layout → AdSense — Header / AdSense — Sidebar → Edit** (AdSense code paste) |
| Newsletter | **Layout → Sidebar → Newsletter** |
| Stats numbers (100+, 50000+…) | **Layout → Stats Section → Edit** |
| Sidebar (About / Popular / Categories) | **Layout → Sidebar Widgets** |
| Footer (About / Quick Links / Topics) | **Layout → Footer Columns** |
| Copyright text | **Layout → Copyright** |
| Colors + fonts | **Theme → Customize → Theme Designer** |
| Naye widgets (Ad slot, HTML…) | Layout me "Add a Gadget" — sidebar/footer me allowed hai |

**Colors badalne ke liye code ki zaroorat nahi:** Theme → Customize → Advanced → Theme Colors → Accent Color badlo — pura theme (buttons, links, chips) update ho jayega.

---

## 4. SEO Setup (Roushan Gupta / Roushan Kumar rank karne ke liye)

### A) Blogger Settings
1. **Settings → Title** → `Roushan Gupta — Business, Tech & AI` (ya apna pasand ka)
2. **Settings → Meta tags → Description** ON karo aur likho:
   > `Roushan Gupta (Roushan Kumar) blogs about business, technology and artificial intelligence — practical guides, AI tools and growth ideas in simple language.`
3. **Settings → HTTPS** → ON + **HTTPS Redirect** ON
4. **Settings → Crawlers and indexing** → Custom robots.txt allow karo (agar pata hai), `noindex` search pages already theme handle karta hai

### B) Har post me (ye adat bana lo)
- **Search Description** likho (post editor → right sidebar → Search Description)
- **1 label minimum** + **achi featured image**
- Title me main keyword (jaise "10 AI Tools…")

### C) Google Search Console (ranking ke liye MUST)
1. [search.google.com/search-console](https://search.google.com/search-console) → property add karo (apna blogspot URL ya custom domain)
2. **Sitemaps** → `sitemap.xml` submit karo (Blogger ka automatic sitemap)
3. Har naye post ka URL **URL Inspection → Request Indexing** karo
4. 2–4 hafte me `Roushan Gupta`, `Roushan Kumar`, `Roushan blog` jaise searches me aana shuru hoga

### D) Theme me already built-in SEO
- Dynamic `<title>` + meta description + canonical
- **JSON-LD schemas:** `Person` (alternateName: *Roushan, Roushan Kumar*), `WebSite` + SearchAction, `BlogPosting`, `BreadcrumbList`
- Open Graph + Twitter Cards (WhatsApp/Telegram/X share me achi preview)
- Semantic HTML5, ek hi H1 per page, lazy images, fast CSS (no render-blocking libs)
- Search/archive pages pe `noindex` (duplicate content se bachav)

### E) Personal branding boost (name se gugl karne pe aana)
- **Google Business Profile / LinkedIn / X** pe apne blog ka link daalo (sameAs)
- About page me poora naam + photo + achievements likho
- Har post ke end me author box already "Roushan Gupta" dikhata hai

---

## 5. Features (sab built-in, zero plugins)

**Design**
- Teal `#30bd9b` + navy `#0a0f1e` brand system (Theme Designer se changeable)
- Sticky glass header, mobile drawer, 404 page, dark navy footer
- Hero section with animated chips + glass card
- 3 topic cards, featured first post, count-up stats
- **Dark mode** (toggle + memory), fully responsive

**Blog**
- Post grid cards (label chip, author, date, snippet)
- Single post: breadcrumb, labels, reading time, **auto Table of Contents**
- Share: Facebook, X, LinkedIn, WhatsApp, Telegram, Copy link
- **Related posts** (label-based, automatic)
- Author box, prev/next navigation, Blogger threaded comments (styled)
- Popular posts (ranked), categories, topics cloud
- **Live search overlay** (`Ctrl/Cmd + K`) — type karte hi results
- Back to top, reading progress bar, image lightbox, copy-code buttons
- Reveal-on-scroll animations (prefers-reduced-motion respected)

**v1.1 additions**
- **Featured slider** — homepage carousel of latest posts (feed-powered, autoplay + arrows + dots)
- **Trending ticker** — scrolling headlines bar under the header
- **Topics mega menu** — Business / Technology / AI dropdown with sub-labels
- **Newsletter widget** — sidebar email signup (Layout se Feedburner/Mailchimp form laga sakte ho)
- **AdSense ad slots** — header/in-content (728×90) + sidebar (300×250); Layout → Edit widget me apna AdSense code paste karo
- **Cookie notice** — one-tap Accept, `localStorage` memory
- **Sticky sidebar** — desktop pe scroll ke saath chipka rehta hai

**Performance**
- No jQuery, no icon fonts, no animation libraries — sirf ~15KB vanilla JS
- Async Google Fonts (Poppins + Noto Sans — Hindi bhi support)
- Inline SVG icons, native lazy-loading
- Ek hi request-safe CSS (sab theme me inline)

---

## 6. Advanced customization (Edit HTML)

| Kya | Kahan dhoondo |
|---|---|
| Author box bio | Edit HTML → `author-bio` |
| Person schema (name/alternateName) | Edit HTML → `"@type": "Person"` |
| Dark mode colors | Edit HTML → `html[data-theme='dark']` |
| Related posts count | Edit HTML → `shown >= 3` |
| Font | Edit HTML → `fonts.googleapis.com` (poora link hata bhi sakte ho — system font fallback hai) |

CSS/JS source alag se edit karke rebuild karna ho to:
```
build/p1_head.xml  +  p2  +  p3  +  p4  →  Roushan-Blog-Theme.xml
```
(cat se jod do, phir Blogger pe restore)

---

## 7. File map

```
Roushan-Blog-Theme.xml   ← YE BLOGGER PE UPLOAD KARO
Sian Free Version 1.0.xml ← purani file (reference, upload mat karo)
preview/                  ← design demo (browser me kholo, Blogger se related nahi)
build/                    ← theme ke 4 source parts
README.md                 ← ye guide
```

## 8. Error-free notes

- Valid XML, Blogger **layoutsVersion 3**, widgets **version 2**
- Required widgets included: Blog, Header, Attribution, PopularPosts, Labels, LinkLists
- Saare `b:include` references defined, widget/section IDs unique, CDATA balanced
- Tested well-formed with an XML parser
- Koi external JS/CSS library nahi — sirf Google Fonts (optional, remove bhi kar sakte ho)

Agar Blogger "Unable to parse" de: file UTF-8 me upload karo, aur restore se pehle pura theme backup le lo.
