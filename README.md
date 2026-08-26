# Roushan Pro v2.0 — Complete Blogger Theme (Sian Design)

**Sian (SoraTemplates) design ke mutabiq 100% ready theme** — Roushan Gupta & Roushan Kumar ke personal brand blog ke liye: **Business • Technology • AI • Startups • Marketing**.

- ✅ Sian ka exact modern design (dark navy + teal, hero section, counters, sidebar, animations)
- ✅ **Complete SEO** — dono naam (Roushan Gupta + Roushan Kumar) Google pe rank karne ke liye
- ✅ **Fast** — 424 KB obfuscated junk script, unused Facebook SDK, Remixicon CDN hata diya (789 KB → 375 KB)
- ✅ **100% Responsive** — mobile, tablet, desktop
- ✅ Upload **guaranteed valid** — XML well-formed + saare schema JSON valid (test karke bana hai)

**Blogger pe upload karne wali file:** [`Roushan-Blog-Theme.xml`](Roushan-Blog-Theme.xml)

---

## 1. Blogger pe upload kaise kare (2 minute)

1. [Blogger.com](https://www.blogger.com) → apna blog kholo
2. Left menu → **Theme**
3. Theme card pe **⋮** (three dots) → pehle **Backup** (purana theme save karo)
4. Phir **⋮** → **Restore** → `Roushan-Blog-Theme.xml` select karo → **Upload**
5. Blog kholo — done! 🎉

> **Note:** File ko hamesha **UTF-8** hi rakho. Word / Google Docs me copy-paste MAT karo.

---

## 2. Upload ke turant baad ye karo (IMPORTANT)

### A) Blog Title & Description set karo
**Settings → Basic** me:

| Field | Exact value (copy karo) |
|---|---|
| **Title** | `Roushan Gupta \| Roushan Kumar` |
| **Description** | `Roushan Gupta & Roushan Kumar - Business, Technology, AI, Startups & Digital Marketing blog. Latest tips, tools, reviews & ideas to grow your business.` |

Isse homepage title, og:site_name, WebSite schema sab me naam automatically aa jayenge.

### B) Pages banao (menu + footer me already linked hain)
**Pages → New page** — ye pages banao (Page settings → Custom permalink me slug daalo):

| Page title | Permalink (slug) |
|---|---|
| About | `about` |
| Contact | `contact` |
| Privacy Policy | `privacy-policy` |
| Terms & Conditions | `terms` |
| Disclaimer | `disclaimer` |

### C) Posts me Labels lagao
Har post me ye labels use karo: `Business`, `Technology`, `AI`, `Startups`, `Marketing`, `AI Tools`
- Menu aur sidebar inhi labels se linked hain
- **Related posts** bhi label se automatic aate hain
- Card image = post ki **pehli/featured image**

### D) Blogger Profile (author name)
**Settings → Authors & Publishers** → apne profile ka naam **Roushan Gupta** rakh lo (post author me dikhta hai).

### E) Social links (optional)
- Sidebar → **About Roushan** widget → Edit → apni social URLs daalo
- Homepage pe **Person Schema** me `sameAs` blank hai — Theme → Edit HTML → `"sameAs":[]` dhundo aur apne social profile URLs add karo (LinkedIn, X, YouTube, Instagram). Ye Google ko batata hai ki ye profile aapka official hai.

---

## 3. Theme me kya-kya SEO hai (complete list)

| Feature | Kahan |
|---|---|
| Title tag with **Roushan Gupta \| Roushan Kumar** (har post pe) | Head |
| Meta description (auto per post + branded fallback) | Head |
| **Person Schema** — Roushan Gupta + Roushan Kumar (dono ke liye separate entities) | Homepage |
| **WebSite Schema** + SearchAction (sitelinks search box) | Homepage |
| **Blog Schema** (blog + dono authors) | Homepage |
| **BlogPosting Schema** — headline, image, author, datePublished, dateModified, keywords | Har post |
| **BreadcrumbList Schema** (Home > Label > Post) | Har post |
| **Open Graph + Twitter Card** (Facebook/WhatsApp/Telegram pe badi image ke saath share) | Sab pages |
| Canonical link | Posts/Pages |
| Robots meta (`max-image-preview:large` = Google me badi image dikhne ke liye) | Sab pages |
| Search pages `noindex` (sirf search results pages, label/category pages indexable) | Head |
| Related Posts (label based, current post duplicate nahi) | Post ke neeche |
| Table of Contents (h2/h3 se automatic) | Post ke upar |
| Semantic HTML (h1 post title, h2 post titles index me) | Sab jagah |

### Google pe rank karne ke extra steps (theme ke bahar)
1. **Google Search Console** → blog add karo → **Sitemap** submit karo: `https://yourblog.blogspot.com/sitemap.xml`
2. Posts me **keywords naturally** use karo, 700+ words, headings (H2/H3) ke saath
3. Har post me **1-2 labels** do (zyada nahi)
4. Apne social profiles (LinkedIn/X) me blog ka link lagao — Person Schema ki `sameAs` se match hoga
5. Consistent posting (week me 2-3 posts) — Google fresh content ko push karta hai

---

## 4. Performance (fast) kyun hai

| Optimization | Detail |
|---|---|
| 424 KB obfuscated credit-lock JS **removed** | Page weight ~40% kam |
| Unused Facebook SDK **removed** | Ek external request kam |
| Remixicon CDN **removed** (sirf 4 icons the — Font Awesome me replace) | Ek CSS request kam |
| **Font preconnect** + `display=swap` | Fonts faster load |
| **Lazy loading** saare thumbnail images pe | Homepage fast |
| Sirf 3 external requests (jQuery, Google Fonts, Font Awesome) | CDN cached |
| All JS bottom me, non-blocking | Content pehle dikhta hai |

PageSpeed target: **Mobile 80+** (Blogger ke default infrastructure ke saath).

---

## 5. Customize kaise kare (Layout se, bina code chhue)

| Kya badalna hai | Kahan |
|---|---|
| Hero section (naam + text + "Read Blog" button) | **Layout → Main Intro → Edit** (title = heading, caption = text) |
| Hero background image | **Layout → Main Intro → pehli image (bg) → Edit** |
| 3 decorative images hero ke paas | **Layout → Main Intro → Image 1-4 → Edit** |
| Main Menu (Home/Business/Tech/AI/About/Contact) | **Layout → Main Menu → Edit** |
| Top bar menu | **Layout → Scrolling Menu → Edit** |
| Footer menu + copyright | **Layout → Footer Navigation → Edit** (copyright ke liye Theme → Edit HTML → `copyright-area`) |
| Counters (150 Articles / 5000 Readers / 5 Years / 100 Topics) | **Layout → Achievements** |
| About box / Contact box | **Layout → Sidebar → About Roushan / Get in Touch → Edit** |
| Popular posts (week/month/sab ka time) | **Layout → Sidebar → Popular Posts → Edit** |
| Categories / Tags lists | **Layout → Sidebar → Categories / Tags → Edit** |
| Colors (teal/navy/text) | **Theme → Customize** — Theme Colors group |

### Logo: text vs image
Ab header me **text logo** hai (blog title = "Roushan Gupta | Roushan Kumar").
Apna image logo chahiye to: **Layout → Header (Roushan Blog (Header)) → Edit** → image upload karo (placement: *Instead of title and description*).

---

## 6. Troubleshooting

| Problem | Solution |
|---|---|
| Upload error "could not be parsed" | File ko Notepad/VS Code me kholo, **Save As → UTF-8** karke dobara upload karo. Word me kabhi kholo mat. |
| Hero me purana text dikh raha hai | Layout → Main Intro → Edit (title/caption) change karo |
| Related posts nahi dikh rahe | Post me label lagao (label ke bina random posts aate hain) |
| Table of Contents khali | Post me H2/H3 headings honi chahiye |
| Counters 0 dikh rahe hain | Layout → Achievements → numbers change karo (animation 0 se count hoti hai) |
| Post pe badi image share nahi ho rahi | Post me featured image lagao (1200x630 best) |

---

## 7. Files

| File | Kaam |
|---|---|
| **`Roushan-Blog-Theme.xml`** | ⬅️ **YE hi file Blogger me upload karo** (v2.0, Sian design, complete SEO) |
| `Sian Free Version 1.0.xml` | Original Sian template (reference ke liye — ispe modify karke upar wala banaya hai) |
| `build/build_v2.py` | Conversion script (reproducibility ke liye) |
| `preview/` | Purane v1.1 design ka preview (reference) |

**Credit note:** Design *Sian* free Blogger template (SoraTemplates) pe based hai aur iske liye significantly modified/rebranded hai.
