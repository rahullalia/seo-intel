# Foundations Course — HeyTony Insiders (Levels 1–5 Curriculum)

Synthesis of 21 short lesson videos across the `curriculum` folder: `startHere` (membership tour) + Level 1 **starter** (4) + Level 2 **newbie** (3) + Level 3 **intermediate** (4) + Level 4 **advanced** (4) + Level 5 **expert** (5 + 1 bonus). This is the sequential "get moving" track — heavy repetition of the same core loop (keyword research → write with ChatGPT → publish → internal link) at increasing depth each level. Duplicated material below is merged into its single strongest version.

---

## Platform Orientation

- Signup places you at a level (1–5) based on a short questionnaire; level ≠ skill judgment, just "how much foundational help you need." All levels are visible/unlocked to everyone — skip ahead or go back anytime.
- **Level 0** (not shown on the homepage, only reachable via the Video Training tab) = "Understanding SEO," the full intro course for someone who knows nothing about SEO yet.
- **Live coaching calls**: Monday and Friday, joined via a Zoom link under the Live Calls tab.
- **Community tab**: reciprocity norm — "the more you put into this, the more you will get out." Introduce yourself on joining; post wins; every workflow below ends with an instruction to post progress here.
- **Blog Post Writer Bot**: a guided Q&A tool (separate from the manual ChatGPT process taught in the lessons) that prompts you with questions and drafts a blog-post starting point.
- **"Wisdom" AI search**: ask it a specific question (e.g. "how long should a title tag be?") and it searches only Matt's own content/community for an answer, with a link back to the source video — use for spot-checks against your own site's issues.
- Free bundled tools: **Page Audit** Chrome extension, **Content Analyzer**. Paid add-ons: **Site Audit Tool** ($10/mo) and **Watchdog** ($10/mo) — both covered in depth below.

---

## 1. Technical Foundations (Level 1 — is your site even visible?)

### 1.1 Check Google indexing
- Search `site:yourdomain.com` in Google.
- Listings appear → Google already knows about the site, move on.
- Nothing appears → not indexed yet; proceed through 1.2–1.3 below.

### 1.2 Sitemap
- Definition: a machine-readable list of every page on the site, built for search engines, not people.
- Check: visit `yourdomain.com/sitemap.xml` (some platforms use `sitemap_index.xml`). A **valid sitemap can render as a formatted page OR raw unformatted code** — either counts, as long as the page loads.
- WordPress, Wix, Squarespace, Shopify: auto-generated, no action needed.
- Custom-built site: contact your host/developer to get one generated automatically.
- **Rule: never hand-build a sitemap yourself.** Use a plugin — **Yoast SEO** (recommended) or **Rank Math** on WordPress — or the platform's built-in generator, so it updates automatically every time a page is added.

### 1.3 Google Search Console (GSC)
1. Sign up at Google Search Console with a Google/Gmail account.
2. **Add Property → Domain** (not the URL-prefix option) → enter the bare domain, no trailing spaces (a stray space causes an error).
3. **Verify via DNS**: copy the TXT verification code GSC gives you → log into your registrar (e.g. Namecheap) → Advanced DNS → Add New Record → **TXT Record**, Host = `@`, paste the value → Save.
4. Return to GSC → click **Verify**. First attempt commonly fails ("couldn't find the verification") — DNS propagation can take a few minutes; keep retrying Verify until it passes.
5. Once verified: go to **Sitemaps** → submit `yourdomain.com/sitemap.xml`. Expect possible errors on a brand-new/unconnected domain — that's normal; the goal is that the sitemap is readable and recognized as a real sitemap.
6. Net effect: tells Google "here are all my pages, index me, rank me."

### 1.4 Google Analytics (GA4)
- Not required for core SEO, but it surfaces two things GSC cannot: **traffic referred from LLMs** (ChatGPT, Perplexity, etc.) and traffic from social/paid ads/email.
- Setup: same Google account used for GSC → business/property name → timezone → currency → industry category → business size → objectives (check all relevant: view user engagement, understand traffic, drive sales/leads) → accept → Create.
- Add a **Web** data stream with the site's URL — confirm it's `https://` (HTTPS covered as a separate, later topic).
- Install the **Google tag** manually in the site's `<head>`, or via the CMS's native integration (look up "install Google Analytics on [WordPress/Shopify/Squarespace]") → Test Installation.

---

## 2. Keyword Research (Levels 2–4, all methods merged)

### 2.1 What a keyword actually is
- Plain definition: **exactly what people type into Google.**
- Keywords are **not** random words stuffed onto a page. They are the *questions and problems* your customers are already searching for solutions to (e.g. "how much does SEO cost," "best coffee shop near me," "how do I fix a leaky faucet").
- Length classes:
  - **Short-tail** (1–3 words): broad, high search volume, high competition, hard to rank. Avoid as a primary target for a smaller site. Example: "photographer" — too broad, you're competing worldwide.
  - **Long-tail** (4+ words): specific, lower volume, easier to rank, faster traffic. Example: "wedding photographer Hamilton," or more specific still, "elopement wedding photographer Hamilton."
- Action step (Level 2): write down your core industry/service in one phrase — you'll feed this into every tool below.

### 2.2 The keyword opportunity matrix
| Traffic | Competition | Verdict |
|---|---|---|
| High | High | **Avoid.** Everyone's chasing these; you'll struggle to rank and it's discouraging. |
| Low | Low | **Default starting point.** Easiest realistic wins. |
| High | Low | **Unicorns / gold.** Rare — lots of searches, nobody's contesting them. Always prioritize when found. |
| — | — | **High-intent keywords**: fewer searches but far higher conversion (bottom-of-funnel, near a buying decision). |

### 2.3 Free, tool-less discovery: AnswerThePublic
- URL: **answerthepublic.com**. Free account = 3 searches/day; no account at all = 1 search/day.
- Type in your core industry/service term (e.g. "hot sauce," "plumber").
- Switch from **Wheel view** (visually interesting but unreadable/not useful) to **List view** — organized alphabetically by question-starter (who/what/how/can, etc.). Ignore the Volume and CPC columns at this stage; that comes later.
- Output: pick **3 questions** you already know the answer to (or can research) — these become your first blog topics.

### 2.4 Tool-based competitor keyword research
Any keyword tool works — demos use **Semrush**; **Ubersuggest** is a cheaper alternative; **Ahrefs** also works. Two distinct methods:

**Method A — Organic Research on a single competitor**
1. Google your industry + your location (or your core product if e-commerce) → open the #1 (or top 2–3) ranking site.
2. Paste that domain into your keyword tool → **Organic Research** → view every keyword it ranks for.
3. Sort/scan the **Volume** and **KD** (Keyword Difficulty) columns for the *competitor's* easy keywords — these become your own target list.
4. Illustrative thresholds called "good": KD 5/100 at 140 searches/mo; KD 6/100 at 880 searches/mo (the high-volume/low-difficulty sweet spot); KD ~25/100 at 1,000 searches/mo is borderline-acceptable.
5. **Never bake "near me" literally into a keyword or page copy** — reads as spammy. You'll still rank locally from other local signals Google already uses (e.g. a dentist example: "sedation dentistry," not "sedation dentistry near me").
6. Contrast a citywide head term (e.g. "dentist St. Catharines" — 1,000 searches, very high KD, hard) against an easier adjacent term (e.g. "wisdom teeth removal" — 880 searches, much easier KD) — prefer the easier one until you have authority. A term like "dentist near me" can show ~90,000 searches at the national-tool level but is effectively unrankable for a new/small site — don't chase raw volume over winnability.

**Method B — Keyword Gap (aka Content Gap) tool, two-domain comparison**
1. Enter your domain + a competitor's domain. The "competitor" doesn't need to be a direct business rival — pick someone with deep topical content in your space (example used: Neil Patel for marketing/SEO topics). **The bigger/more authoritative the comparison site, the more opportunities surface** — a small local competitor yields far fewer usable gaps.
2. Click **Compare**. The visualization shows two circles (your keyword universe vs. theirs) — overlap is shared keywords; the non-overlapping majority is opportunity.
3. Filter by custom **KD range: 0–30** as the standard easy band. For newer/lower-traffic sites, tighten to **0–15 (or under 14)** for the safest wins.
4. Focus on the column showing keywords **they rank for that you don't** — ignore how well they personally rank; you're mining topic ideas, not judging their SEO.
5. Once you pick a target keyword, open its **Keyword Variations / Ideas / Related Keywords** panel and harvest secondary keywords. **Cap secondary keywords at 5–10 per piece** — don't overstuff.
6. Export the list as CSV; keep only **Keyword + Volume + KD** columns, drop the rest.

### 2.5 Judging real rankability via the SERP's backlink profile
- For any keyword you're considering, check who currently holds positions 1–5 and their **referring domains** (unique linking sites) vs. **backlinks** (total link count — many-to-one is possible).
- Example: a #1 result with 5,600 referring domains / 2.4M backlinks is not realistically outrankable soon.
- Green flag: a page ranking on page 1 with **0–2 referring domains** — genuinely winnable.
- When benchmarking competitor content, skip Amazon-type results (they rank on raw domain authority, not content quality — beatable with better content but not a useful structural benchmark) and YouTube results (not a fair blog-content comparison).

### 2.6 Mapping keywords to specific pages
- Do keyword research **per page**, not once for the whole site.
- A keyword showing **zero monthly search volume is not automatically a bad target**: if it precisely matches what the page is actually about (e.g. "3D dental imaging" / "CBCT scans") and carries zero difficulty, it's a free, uncontested ranking opportunity worth taking anyway.
- Put the finalized keyword directly into that page's **H1 tag** (and title tag).

---

## 3. Site Audits & Fixing Issues (Level 3)

### 3.1 Tool options
| Tool | Price | Note |
|---|---|---|
| Semrush | $139/mo | Audit access requires the full suite subscription |
| Ahrefs | $129/mo | Bundles unused extras; audit judged "not 100% comprehensive," less beginner-friendly |
| Screaming Frog | Free tier limited / $245/yr paid | Cheapest full paid option |
| **HeyTony Site Audit Tool** | **$10/mo, up to 3 sites** | Built to be clearer/more actionable than the above; a full site crawl takes **roughly an hour** |
| **Page Audit Chrome extension** (pageaudit.com) | **Free** | No data collection; instantly shows a live page's title tag, meta description, and full heading-tag breakdown — used throughout Sections 3, 6, 10 below |

### 3.2 Reading the report
- Overall **site health %** = a weighted mix of warning count, site speed, and issue severity.
- Issues bucket by severity: **red = serious** (actively blocks/hurts ranking — fix first), **orange/yellow = warning** (won't necessarily block ranking, fix eventually), **grey/info = low priority**.
- **Anti-overwhelm rule**: don't try to clear the whole report at once. Start with red issues that have the **lowest count** first, to build momentum — fix one, post the win in the community, move to the next.

### 3.3 Common issues & fixes
- **Missing H1 tag**: the single most important on-page tag — tells Google (and readers) what the page is about. H2 tags exist to *support* the H1; a page with H2s but no H1 is "supporting a topic that doesn't exist." Fix: do the page-specific keyword research from §2.6, then write an H1 containing the target keyword (+ locality if relevant) — e.g. "3D Imaging and CBCT Dental Scans in St. Catharines, Ontario."
- **Missing meta description**: flagged repeatedly across examples; also the main lever for CTR (see §11).
- **Broken links**: three fix options — remove the link, replace it with a working external link, or replace it with an internal link to another page on your own site.
- **Orphan pages**: pages with zero internal links pointing to them. Google can technically discover them but has no reason to prioritize/rank a page nothing else links to (commonly hits old/hidden blog archives). Fix: add internal links to them from relevant existing pages.

---

## 4. Every Page = One Main Topic (Level 3)

- Every page — and every blog post — must map to exactly **one** main topic/keyword. Treat each page as its own silo.
- Violation symptom: a homepage or service page that name-drops multiple unrelated cities/services/topics on one page (e.g. mixing "St. Catharines" content with "Niagara" content) — this dilutes what the page is "about" in Google's eyes, even if everything on it is nominally related to the business.
- Good pattern: single-topic dedicated pages — one page about dental implants only, a separate page about white fillings only, no cross-contamination. Check by keyword-scanning the whole page for stray off-topic mentions.
- **Keyword cannibalization**: when 2+ pages compete for the same topic/keyword, Google can't determine which is canonical and may fail to properly index/rank *either* one — this actively hurts your own rankings. Applies to blog posts too: don't publish two posts chasing the same core keyword.
- A neglected blog is a common silent violator too — e.g. a business with a blog last updated years ago, where individual old posts have weak/no keyword targeting (e.g. a post titled around a vague non-searched topic) — each post still needs the same one-topic discipline as a service page.

---

## 5. Writing Your First Post with ChatGPT (Level 2)

**Core principle**: content must be genuinely unique — your expertise, direct experience, opinions, case studies. Generic/regurgitated AI output that reads like "we've heard this one before" won't be taken seriously by Google or readers.

**Exact starter prompt:**
> "I'm writing a blog post about [one of your three researched questions from §2.3]. Ask me questions you'd need to know to write the most complete blog post about this topic. Make sure you ask questions about my expertise, experience, opinions, case studies, etc. so that the blog post is truly unique to me."

1. Answer the resulting question list by typing, or by voice dictation (works from the ChatGPT mobile app in the same conversation).
2. Once answered, either accept the follow-up prompt ("Do you want me to turn them into a structured blog draft now?" → "Yes, please") or explicitly ask: "Write me a blog outline with basic details filled in."
3. **Always get an outline first — never a full draft in one shot.** One-shot full drafts tend to fabricate specifics (example given: an invented hourly-rate range that didn't match reality).
4. Paste the outline into a separate blank document. Delete or correct anything factually wrong or off-brand; leave inline notes for what needs to change. Re-submit with: **"I updated the draft. Here's the draft. Please write a blog post using this draft."**
5. For tone/content fixes, edit **section by section**, not the whole document at once — ChatGPT struggles to apply nuanced notes consistently across an entire long piece. Paste just the problem section back with a direct instruction, e.g.: **"This doesn't sound like me. It should be more jokey and sarcastic."** Splice the corrected section back in manually.
6. **Funnel awareness**: the specific question/keyword driving a post signals funnel position. Bottom-of-funnel informational queries (e.g. "how much does SEO cost") mean the reader is close to a buying decision; top-of-funnel queries (e.g. "when was hot sauce invented") mean early discovery — use the content itself to guide the reader down-funnel with a contextual internal link/CTA (e.g. answer the history question, then: "check out our hot sauces →").
7. Paste the final cleaned copy into your site as a blog post; **the post title = the exact question people are googling.**
8. Ship **one** post, not a batch — post "I just wrote my first blog post" + the link in the community (the reciprocity norm from Platform Orientation).

---

## 6. Why Blog Posts Work: Case Studies & Compounding Effects (Level 4)

### 6.1 Case study — $120K/month from blog-only SEO
- Client onboarded ~2.5 years before filming, starting from near-zero organic traffic.
- Strategy = blog content, nothing else.
- A **typical** (not best) month now nets **$120,000/month**, with SEO as the *only* marketing channel running.
- Takeaway: this is a long game — expect roughly a 2–2.5 year horizon for full compounding payoff, not overnight results.

### 6.2 Case study — ranked #1 purely from internal linking
- Speaker personally ranked a page #1 for a competitive keyword using internal linking alone, with no other active optimization, after roughly a year of the page sitting dormant with zero movement.
- The rule that produced it: **every time you publish a blog post, link at least once to a relevant service/product page, using the target keyword itself as the anchor text.** This tells Google what the destination page is about — "doing half of Google's work for them."

### 6.3 Case study — $30,000 sale from one blog post + one internal link
- Speaker searched "can you start a community on Slack," found a pros/cons blog post that internally linked to a paid community-platform product, signed up for a demo, and ended up buying a custom implementation for $30,000.
- Implication: internal links pointed at sub-$100 products/services convert far more casually/impulsively — but the mechanism (educational content → contextual internal link → conversion) scales to any price point.

### 6.4 The seven reasons blog posts work (deduplicated across both advanced-level videos)
1. **Increased traffic + trust** — easier long-tail keywords rank faster, bringing real visitors whose engagement (time on site, clicks, form fills) signals quality to Google.
2. **Internal-linking equity** — every new post is a fresh chance to pass keyword-anchored links to money/service pages.
3. **Unlocks harder keywords over time** — accumulated traffic + trust eventually lets you compete for terms you couldn't touch on day one.
4. **Organic backlinks** — genuinely unique content earns natural external links; each linking domain is a "vote of confidence" that compounds trust further.
5. **The "avalanche method"** — rankings → traffic → backlinks → more rankings → more traffic, an explicitly named self-reinforcing snowball.
6. **Consumer trust/recognition** — answering the exact questions prospects already have, early in their journey, builds expert positioning that pays off at the purchase decision.
7. **Topical authority** — modern Google favors sites that stay tightly focused on one field over sites scattered across unrelated topics; consistent single-vertical blogging signals genuine expertise.

---

## 7. Building a Blog Outline From Competitor Structure (Level 4)

Deeper version of §5, run after full keyword-gap research (§2.4 Method B):

1. Put your primary keyword + its harvested secondary keywords (5–10 max, §2.4) into a spreadsheet — columns: Primary Keyword / Secondary Keywords.
2. Back in your keyword tool, open the primary keyword's SERP view, filter to your target country, and identify the current top 3–5 ranking pages.
3. Check each top result's **backlink profile** (§2.5) to gauge real outrank feasibility. Skip Amazon/YouTube-type results as non-representative benchmarks — but genuinely authoritative competitor content (even if you likely can't outrank it yet) is still useful purely as a *structure* source.
4. Install the free **Page Audit** extension (pageaudit.com → Browser Extension) if you haven't. Open each top-ranking page and extract its full heading-tag list (H1–H4).
5. Paste all extracted headings from every top page into **one** blank outline document.
6. Edit down: delete anything irrelevant/boilerplate (cookie-consent banners, unrelated nav items); keep anything genuinely on-topic; restructure into a logical H2/H3/H4 hierarchy (intro → core sections → FAQ/summary).
7. Append the primary keyword and full secondary-keyword list to the bottom of the document, explicitly labeled ("this is the primary keyword," "these are secondary keywords") — this block becomes part of the eventual ChatGPT prompt telling it exactly which terms to weave in.
8. Framing goal: write the single best, most complete piece on this topic that exists. You may not outrank the term's originator (their inherent authority advantage) — but you can still out-write lower-authority competitors already ranking with thin content (example: a page ranking on page 1 that was only a few short paragraphs).

---

## 8. Publishing & On-Page Optimization Checklist (Level 4)

Full pass, in order, once ChatGPT content is drafted from the §7 outline:

1. **Strip AI "tells"**: remove random/needless bolding, horizontal-rule dividers, emoji (emoji reportedly hurt on-page/Google reception), decorative arrows, and other GPT-house formatting quirks.
2. **Title**: paste the H1/working title into the CMS title field.
3. **URL slug**: manually shorten to **just the core target keyword** — not the full auto-generated long slug, not filler words like "introduction." CMS auto-lowercases and hyphenates.
4. **Heading hierarchy check**: confirm true H2s are marked H2 (not bolded text styled to *look* like a heading) and true H3s are marked H3.
5. **Trust-building intro rewrite** — prompt:
   > "Rewrite the intro to include a statistic that I can externally link to." + "Provide me the link."
   Manually verify the statistic and its source actually say what's claimed before publishing.
6. **External links**: minimum 1 per page, ideally at or very near the top (within the first few paragraphs) — shows Google/readers the content wasn't fabricated from nothing.
7. **Save the draft frequently** — treat this as a real workflow step (sites go down; interns/staff have deleted client content by accident before — keep a backup copy of the finished piece outside the CMS too).
8. **Internal links OUT**: search `site:yourdomain.com [topic keyword]` to find your own older related posts. Add **3–5** internal links from the new post to old posts, using descriptive (not "click here") anchor text.
9. **Categories**: assign to the single most relevant existing category; a genuinely cross-cutting post can take 2. **Max ~10 categories site-wide.** Never leave a post as "Uncategorized" — reads as a neglect signal.
10. **Featured image via AI, style-referenced**:
    > "Generate a featured image for this blog post, without any words, using the attached image as a style reference."
    Upload an existing on-brand image from your own site as the reference — for a more reliable style match, upload **2–4** reference images rather than one. For a variant: "Make it different than the other photo, but the same illustration style."
11. **Rename the image file** before upload (AI-generated filenames are unusable).
12. **Alt text**: include the target keyword plus a plain description (e.g. "[keyword] illustration featured image").
13. **Set as featured image.**
14. **Media enrichment**: add supporting images/graphics/screenshots/embedded video through the body — breaks up "wall of text," builds trust, and serves different learning preferences (visual/video/text).
15. **Preview before publishing, always** — check for spacing/formatting breakage (code snippets or lists rendering as unstyled plain paragraphs) and fix before going live.
16. **Publish.**
17. **Internal links IN (easy to skip, actually matters most)**: immediately after publishing, run `site:yourdomain.com [keyword]` again to find **2–3 older** existing posts, edit them, and add inbound links pointing to the brand-new post. This is what actually gives the new page a fast shot at getting crawled/indexed — it's now referenced from pages Google has already indexed.

---

## 9. Tracking Growth & Reporting (Level 5)

- **Timeline expectation**: SEO realistically takes **3–6 months, sometimes a full year**, to show results. Reporting is deliberately taught *last* in the curriculum so beginners build momentum first instead of getting discouraged watching flat early metrics.
- **Looker Studio + GSC dashboard**: Looker Studio is a free Google tool that connects directly to a GSC property and is far easier to navigate than native GSC. Setup: click **Make a copy** on the provided template → click into any chart → **Add Data Source** → search "Search Console" → connect/authorize → data populates. Same process for a GA4 data source.
- Report sections in the template:
  - High-level overview: top pages, clicks, device breakdown.
  - **"Favorite slide"**: clicks + impressions trend line — the single best at-a-glance "is this site healthy" indicator; used with every client.
  - **LLM/AI-referral traffic slide** (GA4 only — not available in GSC at all): tracks referral traffic attributed to ChatGPT/Perplexity/other LLM surfaces. Example cited: a **375% year-over-year increase** despite zero deliberate "LLM SEO/GEO" optimization work.
  - **Keyword-cluster slide**: filter to any single word (a service name, a city name) to see every query containing it and its individual performance.
  - **Content-performance-over-time slide**: log which posts/pages were published/updated in a given month and track their trend month-over-month/year-over-year. If a previously-strong page starts declining, that's the trigger to go re-optimize it.
  - **Content optimization ideas quadrant**: four buckets — Why / What / How / Can — seeded from queries with real impression volume but no matching content yet (example: "why can't I post on Instagram" showing 1,500 monthly searches with nothing on-site addressing it = a content gap to fill).
- **Date-range gotcha**: the default/auto range can default to a stale or too-short window (e.g. last 28 days, or an old cached range) — explicitly set a full year-over-year range and sanity-check the numbers before drawing conclusions.
- A traffic decline in the dashboard isn't automatically a crisis — check whether you're still ranking for your core "money keywords" before reacting.

---

## 10. Growing Rankings You Already Have — "10x Traffic for Free" (Level 5)

Prerequisite: at least 3–6 months of live GSC data (a brand-new site won't have enough history).

1. In GSC → Search Results, enable the **Average position** column and expand rows shown (500–1,000). Scan into the **11+** range: **page 2 ≈ positions 11–20; page 3 ≈ 21–30.**
2. Look for keywords with meaningful **Impressions** but landing at position 11+ — "showing up, just not getting clicked," i.e. free upside sitting on page 2/3. Worked examples: a keyword at ~12.4 average position with 456 impressions; another with 406 impressions; another with ~800 impressions at the tail of page 2; another with ~1,100 impressions in page-3 territory.
3. Click into the keyword to find which URL ranks for it, open that **live URL directly**, and use the Page Audit extension or Ctrl/Cmd+F to literally count how many times the exact keyword phrase appears on the page.
4. Common finding on old/neglected content: **missing meta description entirely**, the keyword appearing only ~2–3 times total across title/H1/body, sometimes garbage leftover schema markup/shortcode visibly broken on the page (delete it).
5. **Do NOT change the URL** if the page already gets any traffic/ranking — changing the URL makes Google treat it as a brand-new page, forcing a full recrawl/reindex that destroys existing equity.
6. Fix list, purely additive: ensure the keyword is in the title tag (add if missing), rewrite the meta description to include it, ensure it's in the H1, add it to at least one H2, and work it in a couple more times naturally in body copy. Don't rewrite the whole page — just nudge density.
7. **Wait roughly 2 weeks to 1 month** before judging results.
8. **Rollback rule**: if performance drops after the change, revert to the prior version and try a smaller, more conservative edit next time.
9. Framed explicitly as "the secret, the trick to SEO" — small, patient, additive on-page nudges to content that's already halfway there, not large rewrites.

---

## 11. Increasing Click-Through Rate (CTR) (Level 5)

- Symptom: ranking well (even #1) with real impressions but near-zero clicks.
- Root cause almost always: **missing or weak meta description and/or an uncompelling title tag** — described as "the billboard for your site" in the SERP.
- If no meta description is set, Google either shows nothing useful or auto-generates one from page content — neither compels a click as reliably as one deliberately written.
- Fix: write (or have ChatGPT write) a meta description that includes the target keyword **and** gives a clear, specific preview of the payoff (example: for "size of Facebook cover photo," promise the exact dimensions plus a call to click for full details).
- **Exact prompt**: "Write me a compelling title tag" or "five compelling title tag options for this, make sure it includes [keyword]" — pick the best of the five.
- **Guardrail**: if you're already ranking well (or #1) for a keyword, do **not** strip that exact keyword out of the title tag while "improving" it — removing the ranking keyword risks losing the ranking/traffic entirely. Edit around it, never delete it.
- First diagnostic before any of this: confirm impressions are current/ongoing, not a stale spike from months ago that's since died off (if nobody's searching it anymore, optimizing has no payoff).

---

## 12. Content Calendar — Deliberately Minimal (Level 5)

- Explicit rejection of heavy multi-month editorial calendars for most people — framed as overkill/a time sink most won't sustain, since opinions/strategy/ideas shift.
- The entire system: pick **one fixed day per week**, block **one hour**. During that hour: find one keyword/question (any method above) → draft with ChatGPT using the full process from §5–8 → publish → remember to internal link.
- Two sessions/week is fine if sustainable; the floor is once/week. Goal is consistency, not volume.
- Closing maxim: **"SEO only works if you don't give up."** Consistency over time is positioned as the actual ranking hack.

---

## 13. Competitive Intelligence Tools (Level 5 bonus)

### 13.1 HeyTony Watchdog — competitor change-monitoring
- **$10/month, up to 3 tracked sites.** URL: watchdog.heytony.ca.
- Differentiator vs. standard keyword tools (Semrush/Ubersuggest): those only show what competitors *already* rank for, meaning you're already months behind by the time you see it. Watchdog instead detects real-time **changes** on competitor sites as they happen — title tag edits, meta description edits, word-count shifts, pricing changes, new pages added, pages removed, links added/removed, internal-linking strategy shifts.
- Shows a before/after diff per tracked page/change, with original publish date and update date.
- Can surface unlisted/unlinked pages a competitor thinks are hidden (example: an internal keyword-tracking page not meant for public discovery still got picked up because it was reachable by direct link).
- Use pattern: spot a brand-new competitor page → infer their internal-linking strategy from which existing pages started linking to it → anticipate their next SEO moves in near-real-time instead of 3–6 months later via lagging rank-tracking data.

### 13.2 Linkgap.io — backlink gap analysis
- Free entry, email-gated full report. Enter your domain + one competitor domain → **Analyze Backlink Gap** (~30 seconds) → free preview shows 3 sample gaps; full list requires your email (check spam — delivery reportedly lands there).
- Report contents: domain + specific URL of every site linking to the competitor but not to you. Example run surfaced **112 total backlink gaps.**
- Core heuristic: "if somebody is willing to link to your competitor, you can probably get them to link to you too."
- Most gap sources in practice are **directories and press-release/news-aggregator sites** (examples referenced: general business directories, a "submit your site" directory, Yellow Pages). Action: visit each, find their submission/contact/press-release path, and request or self-submit a listing.
- Suggested cadence: **1–2 outreach/submissions per week.**

---

## 14. Tool & Pricing Quick Reference

| Tool | Price | Use |
|---|---|---|
| HeyTony Site Audit Tool | $10/mo (3 sites) | Full site crawl/audit, ~1 hr to run |
| HeyTony Watchdog | $10/mo (3 sites) | Real-time competitor change monitoring |
| Page Audit (Chrome ext., pageaudit.com) | Free | Per-page title/meta/heading-tag inspector |
| Content Analyzer | Free | Bundled content tool |
| Linkgap.io | Free (email-gated full report) | Backlink gap analysis |
| Semrush | $139/mo | Full suite; used for Organic Research + Keyword Gap |
| Ahrefs | $129/mo | Alternative keyword/audit suite |
| Screaming Frog | Free (limited) / $245/yr | Crawl/audit alternative |
| Ubersuggest | Cheaper than Semrush | Keyword research alternative |
| AnswerThePublic | Free: 1 search/day; free account: 3/day | Question-based topic discovery |
| Google Search Console | Free | Indexing, sitemap submission, ranking data |
| Google Analytics (GA4) | Free | Traffic source detail, incl. LLM referrals |
| Looker Studio | Free | GSC/GA4 dashboarding |
| ChatGPT | External subscription | Drafting, outlining, image generation, title/meta rewrites |
