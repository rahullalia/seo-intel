# Rank Week 2026 - Resources

Everything Matt Diamante (HeyTony) shared during Rank Week 2026, pulled from the
authenticated member dashboard at `rankweektraining.com/dashboard` plus the session
transcripts. Collected 2026-06-19.

The dashboard is the master hub - it aggregates every prompt, spreadsheet, tool, and
download. Replays + transcripts live one level up in `../videos/` and `../transcripts/`.

## Downloaded locally

### AI Prompts (`prompts/`)
One per training day, copied verbatim from `/prompts`. `[BRACKETS]` are fill-in slots.

| File | Day | Purpose |
|---|---|---|
| [day1-blog-prompt.md](prompts/day1-blog-prompt.md) | 1 | Interviews you about a question, then writes a genuinely helpful/unique blog post with your experience |
| [day2-money-page-audit.md](prompts/day2-money-page-audit.md) | 2 | Formats raw page-audit output into 10 clean values for the audit spreadsheet |
| [day3-fix-money-page.md](prompts/day3-fix-money-page.md) | 3 | Takes your audit data + 3 competitor pages and rewrites your money page to outrank them |
| [day4-internal-linking.md](prompts/day4-internal-linking.md) | 4 | Finds the most natural spot to internal-link a post to your money page and rewrites that paragraph |

### Spreadsheet (`spreadsheets/`)
[auditSpreadsheet.xlsx](spreadsheets/auditSpreadsheet.xlsx) - 4 tabs:
- **Website Audit** - your page vs 2 competitors (URL, focus keyword, title, meta, H1/H2/H3, word count, keyword density)
- **Page Optimizations** - title (60 char), meta (156 char), keyword usage, mobile/desktop page speed
- **Optimization Rules** - the on-page rules (one H1, H1 has keyword, internal/external link counts, etc.)
- **Local SEO Audit + Checklist** - GMB/Google Business Profile optimization checklist

Live "make a copy" link: https://docs.google.com/spreadsheets/d/1qkz0xRMEct_eqkWl86II0rva8TcwdE573JL2_LJNezQ/copy

### Book (`downloads/`)
[getFoundBook.epub](downloads/getFoundBook.epub) - *"Get Found: The No-Fluff Guide to
Ranking Higher and Becoming Your Customers' First Choice"* by Matt Diamante (2025, ISBN
9781068826412).
Live link: https://drive.google.com/file/d/1zBry2M2OrxidtpGoReZ8zfpw03wE9lkc/view
Also [getFoundBookV2.pdf](downloads/getFoundBookV2.pdf) (v2, the version mined for Section 17
of `../rank-week-playbook.md`).

## Tools (links - interactive or external, nothing to download)

HeyTony's own (need member login):
- **Find Questions** - https://rankweektraining.com/tool/reddit-questions - mines r/SEO, r/TechSEO, r/DigitalMarketing, r/aeo, etc. for real questions to answer in posts. Public versions: findquestions.com / heykeywords.com
- **Site Audit** - https://rankweektraining.com/tool/site-audit - on-site SEO auditor

Third-party (the toolkit he recommends):
- **Page Audit Chrome extension** - https://chromewebstore.google.com/detail/page-audit/gmnbmbjdcjbbmdbjlmdkjddmjmpdciod (also pageaudit.com) - pulls the per-page values the audit prompt/spreadsheet need
- **PageSpeed Insights** - https://pagespeed.web.dev/ - mobile/desktop speed scores
- **Convertio** - https://convertio.co/jpg-webp/ - JPG→WebP for image speed (cited in the spreadsheet)

Also name-dropped in sessions (not part of the core toolkit, from a full transcript sweep):

- SEO research: SEMrush, Ahrefs, Google Search Console, Google Analytics, AnswerThePublic, AnswerSocrates, AlsoAsked
- AI assistants the prompts target: ChatGPT, Claude, Gemini
- Platforms referenced only as examples (not resources): WordPress, Shopify, MailChimp, ConvertKit (kit.com)

## Completeness

Verified 2026-06-19 by crawling every authenticated route (dashboard, `/prompts`, all
`/prompt/N`, all `/replay/N`, `/videos`, `/community` + its API, both `/tool/*`) and diffing
all external/file links. The whole site exposes exactly **one spreadsheet** and **one
download** (both pulled here) and **four prompts** (no prompt 2). Community has 2 engagement
posts and no shared files. Nothing else to collect.

## On the dashboard but not pulled

- **Setup videos** `/video/3`-`/video/7` - onboarding: Welcome, "Does Google Know About
  Your Website?" (sitemap), Registering With Google (Search Console), Setting Up Google
  Analytics. Short tutorials, watch on-site if needed.
- **Day replays** `/replay/1`-`/replay/5` - already downloaded + transcribed (see `../LOG.md`).
- **HeyTony Insiders** - https://heytony.ca/insiders/ - the paid continuity program he pitched on Day 5.

## How these were collected

Authenticated to `rankweektraining.com` by reusing the logged-in Chrome session
(`yt-dlp --cookies-from-browser chrome` → cookie jar → `curl`). The dashboard and
`/prompts` are server-rendered HTML, so prompts/links came straight out of the markup;
the Google Sheet was pulled via its `/export?format=xlsx` endpoint and the book via
Drive's `uc?export=download`.
