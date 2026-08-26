# SkillBlog Pro — Complete Blogger Theme

SkillCourse.in inspired, **responsive**, **SEO-ready**, **error-free** Blogger XML theme.

**Restore this file on Blogger:** [`myblog.xml`](myblog.xml)

---

## Blogger pe restore kaise kare (2 minute)

1. [Blogger.com](https://www.blogger.com) pe apna blog kholo
2. Left menu → **Theme**
3. Theme card pe **⋮** (three dots) → **Restore** / **Backup**
4. **Upload** → `myblog.xml` select karo → **Upload**
5. Preview check karo, phir **Apply to Blog**

> Pehle apna current theme backup zaroor lo (same ⋮ menu → Backup).

### Alternate method
Theme → **Customize** → **Edit HTML** → saara code hatao → `myblog.xml` ka content paste → **Save**.

---

## Restore ke baad ye pages banao

Pages → New page (ye URLs theme footer/header me already linked hain):

| Page title | Permalink / URL |
|---|---|
| About | `/p/about.html` |
| Courses | `/p/courses.html` |
| Privacy | `/p/privacy.html` |
| Disclaimer | `/p/disclaimer.html` |
| Contact | `/p/contact.html` |
| Terms | `/p/terms.html` |

Phir **Layout → Main Menu (Pages gadget)** me in pages ko add karo.

Posts me labels use karo: `Excel`, `Power BI`, `SQL`, `Python`, `AI` — cards aur related posts isi se chalte hain.

---

## Features

### Design (SkillCourse UI)
- Gold / peach / navy brand system (`#E5B549`, `#FECDA5`, `#1B2431`)
- Homepage hero, mastery-style post cards, Why-us, stats, newsletter
- Sticky glass header, mobile drawer, 404 page, dark footer
- Fully responsive (desktop / tablet / phone)

### SEO
- Dynamic title, description, canonical, robots
- Open Graph + Twitter Card
- JSON-LD: WebSite + SearchAction, BlogPosting, BreadcrumbList
- Semantic HTML5, heading hierarchy, RSS/Atom, lazy images
- Hindi + English font stack (Plus Jakarta Sans + Noto Sans Devanagari)

### Blog features
- Grid cards on home / labels / search
- Single post: breadcrumb, featured image, TOC, reading time
- Social share (Facebook, X, WhatsApp, LinkedIn, Telegram, copy link)
- Related posts (label-based JSON feed)
- Author box, tags, comments (Blogger iframe)
- Popular posts, labels cloud, archive, profile, follow-by-email
- Search overlay (`Ctrl/Cmd + K`)
- Dark mode, reading progress, back-to-top
- Image lightbox, copy-code buttons
- Cookie notice, WhatsApp float, ad slot
- Theme Designer color + font variables

---

## Customize

| Kya badalna hai | Kahan |
|---|---|
| Colors / fonts | Theme → Customize → Theme Designer |
| Menu pages | Layout → Main Menu |
| WhatsApp number | Theme → Edit HTML → search `wa.me/` |
| Email | Edit HTML → `hello@yourblog.com` |
| Hero text | Edit HTML → `sb-hero` section |
| Stats numbers | Edit HTML → `sb-stats` |
| Sidebar ad | Layout → Sidebar Ad HTML gadget |
| Social links | Footer icons in Edit HTML |

WhatsApp example:

```html
href='https://wa.me/91XXXXXXXXXX'
```

---

## Settings (recommended)

Blogger → Settings:

- **Meta description** add karo (SEO)
- **Custom robots** → `index, follow`
- **HTTPS** enable
- **Search preferences** → custom description
- Posts: always add **title, label, featured image** (first image = card image)

---

## File map

```
myblog.xml          ← upload / restore this on Blogger
README.md           ← this guide
src/skin.css        ← theme CSS source
src/app.js          ← theme JS source
src/build_theme.py  ← rebuilds myblog.xml
preview/            ← visual demo only (not uploaded to Blogger)
```

Rebuild after CSS/JS edits:

```bash
python3 src/build_theme.py
```

---

## Error-free notes

- Valid XML, Blogger layoutsVersion **3**, widget version **2**
- Required gadgets included: Blog, Header, Attribution, PageList
- Sidebar gadgets use official default markup (no fragile custom loops)
- Ampersands escaped, CSS/JS inside CDATA
- Tested well-formed with an XML parser

Agar kabhi Blogger “Unable to parse” dikhaye: file ko **UTF-8** me hi upload karo, Word/Google Docs se mat copy karo.
