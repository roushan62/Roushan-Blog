# 10 Ready-to-Publish Blogs — Roushan Gupta

Ten original, SEO long-form articles written for the `Roushan-Gupta-Blogger-Theme.xml`
theme. English, Indian context, evergreen guides and comparisons.

| | |
|---|---|
| Total | **17,861 words** across 10 posts |
| Per post | 1,542 – 2,013 words (7–9 min read) |
| Originality | **0.000%** 5-word and 8-word shingle overlap against the reference article analysed |
| Markup | Only `h2 h3 p ul ol table thead tbody tr th td blockquote strong em code h1` — every one already styled by the theme |
| Inline CSS / JS / classes | None. Nothing can conflict with the theme |

## Files

```
blogs/
├── blogpage.html          ← OPEN THIS. Index of all 10 + one-click copy + instructions
├── 01-zoho-vs-freshworks.html          Blogger-paste HTML for post 01
├── 02-validate-startup-idea-30-days.html
├── 03-free-ai-tools-small-business-india.html
├── 04-first-100-customers-india.html
├── 05-how-upi-makes-money.html
├── 06-ai-digital-marketing-2026.html
├── 07-business-plan-guide-2026.html
├── 08-franchise-business-india.html
├── 09-personal-brand-founders-linkedin.html
├── 10-unit-economics-cac-ltv.html
├── _preview/              ← the same posts rendered inside your theme (read-only previews)
└── .gitignore
```

`_build/` (the `theme.css` extracted from the theme XML, `preview.css`, `posts.json` and the
originality-check reference) is generated, so it is git-ignored. To reproduce it: extract the
`<b:skin>` block from `Roushan-Gupta-Blogger-Theme.xml` and substitute the ten `Variable`
defaults — `#2563EB`, `#1D4ED8`, `#EFF4FF`, `#FFFFFF`, `#F7F8FA`, `#1A1A1A`, `#5F6B7A`,
`#E5E8EE`, the body font and the heading font.

## The 10 posts

| # | Title | Labels | Words |
|---|---|---|---|
| 01 | Zoho vs Freshworks: Which Indian SaaS Company Is the Better Bet in 2026? | Business, Technology | 1,999 |
| 02 | How to Validate a Startup Idea in 30 Days Without Spending Money | Startup, Business | 2,013 |
| 03 | 10 Free AI Tools Every Small Business in India Should Use in 2026 | AI, Technology | 1,918 |
| 04 | How to Get Your First 100 Customers in India With Almost Zero Budget | Startup, Marketing | 1,708 |
| 05 | How UPI Actually Makes Money: The Economics Behind India's Free Payments | Fintech, Business | 1,752 |
| 06 | AI for Digital Marketing in 2026: What Actually Works and What Is Just Noise | Marketing, AI | 1,665 |
| 07 | How to Write a Business Plan in 2026 That Investors and Banks Will Actually Read | Business, Startup | 1,764 |
| 08 | How to Start a Franchise Business in India: Costs, Profit Margins and the Questions Nobody Tells You to Ask | Business, Startup | 1,773 |
| 09 | Personal Branding for Founders in 2026: A Practical LinkedIn and Content Playbook | Marketing, Startup | 1,542 |
| 10 | Unit Economics Explained: CAC, LTV and Payback Period With Real Indian Examples | Startup, Business | 1,727 |

## Publishing (2 minutes per post)

1. Open `blogpage.html` in a browser (or run `python3 -m http.server 8080` inside `blogs/`).
2. Click **Copy for Blogger** on a card.
3. Blogger → **New post** → click the `</>` **HTML view** icon → **paste**.
4. Switch back to **Compose**.
5. **Title** = the headline. (The copied HTML deliberately excludes the `<h1>`, because Blogger
   renders the post title as the page H1 — this avoids two H1 tags.)
6. **Labels** = the two shown on the card. The theme's homepage category sections and related
   posts are label-driven, so use them consistently.
7. **Search description** = the one-line summary on the card.
8. Add your own featured image.
9. Publish.

Fallback if the clipboard is blocked (browsers block it on `file://`): open **Source HTML**,
select everything between the `COPY-FROM-HERE` and `COPY-TO-HERE` comments, copy that.

## Why these are copyright-safe

- **No copied expression.** All prose was written from scratch. Topic choice and article
  structure are not protected by copyright; copied sentences are, and there are none.
  Verified by shingle comparison — see `_build/reference_startuptalky.txt`.
- **Facts are attributed in-text.** NPCI UPI data, Zoho's FY25 RoC filings, DPIIT startup
  counts, GST thresholds, market-size estimates. Facts are not copyrightable, but the
  attribution stays in every post.
- **Brand names are nominative use.** Naming Zoho, Freshworks, Swiggy or Razorpay in a
  comparison is legal. Do not use their logos as featured images.
- **Images remain your responsibility.** Use your own photos, original Canva/Figma graphics,
  or free-licence stock (Pexels, Unsplash, Pixabay). Never an image lifted from a news site.
- **Each post carries an Editor's Note** flagging that the figures are date-stamped and
  should be re-verified.

## One-time Blogger settings

- **Settings → Meta tags → Description**: enable it. The theme only emits `<meta description>`
  when this is on.
- **Theme → Customize → Advanced → Colors**: accent is `#2563EB`.
- **Publish 2–3 posts a week**, not all ten at once.
- After 4–5 posts are live, add 2–3 internal links between related articles.

## Verification performed

| Check | Result |
|---|---|
| HTML well-formedness (all 21 files) | Balanced, no stray or unclosed tags |
| Word count per post | 1,542–2,013 — inside the 1,500–2,200 target |
| Headings per post (theme needs ≥3 for auto-TOC) | 21–28 each |
| Tables per post | 1–8; 35 total |
| Copy-extraction logic in `blogpage.html` | Runs on all 10 files; H1 correctly stripped |
| Originality vs reference article | 0.000% overlap at 5-word and 8-word shingle level |
| HTTP serve test | `blogpage.html` 200, previews 200, source files 200 |
