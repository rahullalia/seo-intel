# Rank Week 2026 Day 4 — Replay (Call 073)

Source: HeyTony Insiders Call Replay (hash: YDaAOv8ZDQ) | 100m 21s | ~16,182 words

## Tactics & step-by-step how-to

- **Crawl depth model** (how many clicks from homepage to any page): click 0 = homepage. Click 1 = anything linked directly from the homepage/nav (services, blog index button, a homepage "recent posts" or "services" module). Click 2 = e.g. clicking Blog (1) then a specific post from the archive (2), or clicking Services (1) then a specific service (2). Click 3 = a page linked from that post/service (e.g. clicking "next page" of the blog archive). Click 4 = e.g. posts sitting on page 2 of a paginated blog archive. Rule of thumb: **get every page you want ranked to 3 clicks or fewer from the homepage** — "if you can get to any page from your site in three clicks or less, that is going to make it more likely that Google will find that, because people can find that."
- **Live internal-linking exercise**:
  1. Open your money page and the blog post you wrote on Monday in two separate browser tabs (or the Google Doc if unpublished).
  2. Open ChatGPT, Claude, or Gemini — "doesn't matter" which model.
  3. Go to `https://heytony.ca/rank-week-crawl-prompt/` and copy the crawl prompt.
  4. Paste the prompt, scroll to "content to analyze," paste your blog post text (or Google Doc content) there, then paste your money page URL underneath it.
  5. Press enter.
  6. Output returns numbered sections: internal linking opportunity, recommended anchor text, why this link makes sense, where in the post to add it, the original paragraph, and a rewritten version of that paragraph with the link already woven in.
  7. Copy the rewritten paragraph back into the post (Google Doc, CMS editor, or directly on the live site) and update/save.
- **Rule 1**: every new blog post links out to **3–5 existing blog posts + 1 money page**.
- **Rule 2**: every time you publish a new post, go back and add a link to it from **3 older blog posts** (different ones than those the new post links out to). Together, "that's your entire internal linking strategy, done."
- Can be applied retroactively — go back into old posts, add the links, then re-crawl them.
- Claimed result of doing both rules consistently: "we've had pages index within an hour to two hours" of publishing.
- **Anchor-text technique**, demoed live: find a phrase in existing content that describes another page's topic (e.g. the words "content ideas for your blog"), highlight it, and link it directly to that other page — no separate "read more" link needed.
- **Advanced crawl-depth shortcut — category pages**: use blog "posts" (not static pages) because posts auto-populate a blog roll AND auto-sort into category archive pages. Clicking a category tag from the homepage (1 click) loads every post in that category (2 clicks total) — collapsing what would otherwise be a 3-click path (archive → next page → post) down to a 2–3 click path for an entire topic cluster.
- **Homepage modules that shorten crawl depth**: add a services bar/module and a "recent posts" module directly on the homepage (both become 1-click from homepage); link out to category pages from the homepage too.
- Local businesses: link to your Google Business Profile from the homepage or footer (Matt's own site does this via a map that loads the GBP with service area).
- **Quick nav fix**: if "Blog" isn't in your navigation menu, add it today — this helps both people and Google find content faster.
- **Multi-location expansion** (electrician case, LA/Orange/Riverside counties): don't blanket-generate a page for every city on a list from ChatGPT. Instead take each candidate city + service term, run it through a keyword tool (SEMrush) for volume and difficulty, and build location pages for the easiest-to-rank ones first. Use **subfolders** (`site.com/irvine`), never subdomains (`irvine.site.com`). Best option if physically present: a separate Google Business Profile per county/city.
- **Competitor-gap keyword mining when you have no obvious competitors**: ask ChatGPT to identify likely competitors, then plug those competitor domains into Ubersuggest or SEMrush and look at keywords they rank for but are **not well-optimized for** — "low-hanging fruit" / "gold keywords" you can outrank them on.
- **Handling AI-junk blog posts that are indexed but not ranking**: if you have a relevant replacement piece of content, 301-redirect the old URL to it; if not, just let it 404.
- **Keeping intentionally-hidden pages out of Google**: set the page to no-index (in Yoast/Rank Math, usually under an "Advanced" section) — don't rely on lack-of-internal-links alone (a hidden page can still surface, e.g. in a branded/ego search). Robots.txt can also block pages but Matt does not recommend most people edit it directly — easy to accidentally block the entire site.
- **Checking real ranking status**: use Google Search Console filtered by page, rather than eyeballing incognito searches.
- **Review rank movement monthly, not daily** — daily fluctuation is normal noise, not a signal to act on.
- Quizzes/interactive tools as top-of-funnel content: embed directly on your own site/page (not just a linked-out third-party tool) — anything that keeps visitors on-site longer and drives action is good for SEO signal.

## Rules / dos & don'ts (keep every threshold, number, specific)

- Every page you want ranked: **3 clicks or fewer** from the homepage.
- Every blog post: link to **3–5 other posts + 1 money page**.
- Every new post: get linked to from **3 older posts**.
- General max: **10–20 links per page**.
- For a small site (~5 pages), no need to stagger internal-link additions across multiple days — "do the whole thing" at once.
- Don't hide or bury money pages/blog links out of embarrassment — "if you hide things from the user, you're hiding them from Google."
- Don't put everything into dropdown/toggle menus. A dropdown item itself does **not** count as an extra click ("it's when you leave that page" that counts) — but overstuffed dropdowns hurt usability, especially since roughly **50–60% of all internet traffic is on mobile**.
- Orphan pages (zero internal links pointing in) are fine **only** when deliberate (lead-magnet quizzes, job postings, ad landing pages, internal-only pages) — pair with a real no-index tag; anything you want ranked must never be orphaned.
- Keep the "Blog" label in your nav — don't rename it (e.g. to "Learn Hub"). Doesn't hurt SEO directly, but hurts visitor clarity.
- Plurals (e.g. "broker" vs. "brokers") don't matter to Google — use naturally.
- Location pages: subfolders, never subdomains.
- Bad/AI-junk indexed posts: 301 if a relevant replacement exists, otherwise let 404.
- No evidence that AI-written content is penalized, and no evidence that specific "flagged" words in wellness/spiritual/alternative-health niches get filtered or suppressed — Matt has never heard this from any SEO expert he's talked to.
- Don't force a product gallery onto every blog post if you only carry a few products — link to the one relevant product instead.
- A blog CTA is fine (e.g. "get a free quote") but understand blog intent = research, money-page intent = ready to buy.
- A single business can and should have **multiple money pages** (one per service/offer), each pointing to the same lead-capture form if that's how the funnel works.
- Cancel any tool that pushes daily rank-change alerts — "that is just giving you anxiety"; check monthly averages instead.
- If a competitor holds #1 steadily, that's not always a fixable discrete problem — sometimes "Google thinks this is the number one website and nobody else has earned that spot yet."
- Discount code for the audit tool: **RANKWEEK2026** ("no spaces before or after").

## Tools, prompts & resources (exact prompt wording if quoted; tool names; settings)

- **Rank Week crawl prompt** — `https://heytony.ca/rank-week-crawl-prompt/`. Paste the prompt, then under "content to analyze" paste blog post text/doc content plus the money page URL, press enter. Works identically in ChatGPT, Claude, or Gemini.
- **audit.heytony.ca** — HeyTony's own technical site-audit tool. Code **RANKWEEK2026** = 1 month free (normally **$10/month**; auto-charges card after the free month unless canceled). Scans for: site health score, orphan pages, broken links, canonical-URL/sitemap mismatches, missing H1 tags, title tags too long or too short, meta descriptions too short, pages with low word counts. Every flagged error links to an embedded how-to-fix YouTube video. Supports up to **3 sites per account** (your own site plus up to 2 competitors). Turnaround "a couple hours up to a day" given high signup volume during the event. Does **not** do keyword research.
- **Google Search Console** — filter by page to see actual rankings/queries for that specific URL; foundational tracking tool recommended before any paid keyword tool.
- **Ubersuggest** — budget keyword research tool. Per Matt's own prior "shootout" vs. SEMrush/Ahrefs/SE Ranking: Ubersuggest's search-volume numbers run inflated (example cited: **3,600/month** on Ubersuggest vs. **750/month** on SEMrush for the same term), while the other tools clustered closer together. Still useful directionally ("points you in the right direction") if budget doesn't stretch to SEMrush/Ahrefs — treat it as relative, not literal, magnitude. Neil Patel was running a one-time lifetime-price offer (~$300–400) at time of call.
- **SEMrush** — used for keyword-volume/difficulty checks per city/term and for competitor keyword-gap analysis.
- **Yoast / Rank Math** — on-page SEO plugins. Have a no-index checkbox (usually under "Advanced"). Both are easy to "game" green by simply repeating the keyword more — doesn't mean it's actually well optimized. Neither tool does real keyword research, tells you ideal keyword frequency/page length relative to competitors, or evaluates internal-link quality or true readability.
- **robots.txt** — can block indexing but risky to hand-edit; not recommended for most people (easy to accidentally block the whole site).
- **HeyTony Insiders** — leveling system, 5 levels, auto-graduates on completion of each: Level 1 (get Google to find your site, register with Google Search Console, basic tracking setup — ~12 minutes of video total); Level 2 (what keywords are, how to find what customers search, writing your first blog post via ChatGPT); mid levels (auditing your site, light keyword research, fixing audit issues); Level 5 (tracking growth, "10x your traffic for free," increasing CTR, content calendar, bonus module "how to spawn your competition"). Qualifying questions at signup place you at the right starting level. Includes a community page for peer Q&A, and a full call-replay archive back through prior Rank Weeks. New: an e-commerce-focused SEO specialist is joining the team to run biweekly calls for members with online stores.
- **Insiders pricing** — roughly **$50–57/month** (referenced inconsistently in-call as "50 bucks or 57 bucks," and separately as "less than 60 bucks a month"). This cohort's registration closes "tomorrow at midnight." The $10 spent on the audit tool this week rolls into the Insiders cost if you convert.
- **Framer** — website builder used by one attendee (Samir), paired with an MCP connection from Framer to Claude to build out the site; mentioned as his own workflow, not a direct endorsement from Matt.
- **Canva** (as a website host) — Matt has no direct experience optimizing Canva sites, but says if standard fundamentals (sitemap, etc.) are in place it should be fine.

## Case studies / examples / results (names, niches, numbers)

- **Cliff**: Day 2 attendee who was "lost," "couldn't find the Chrome extension," said the pace was "too fast" — by Day 3 said "mind blown."
- **Amanda**: years struggling with SEO, hired multiple people/agencies previously — got more done in this one week than all of that prior effort combined.
- **Tori**: joined Insiders mid-week, posted one question in the community, got 27 responses — assumed they came from Matt's team; mostly other insiders answered.
- Denroy's Insiders call that same morning had **25 attendees** despite "hundreds" of new members just welcomed in — confirms not everyone attends every call.
- **Al**: corporate magician doing corporate magic shows in the San Francisco Bay Area; was targeting the keyword "corporate events" — Matt reviewed and redirected him toward better keyword opportunities.
- **Matt's own site (heytony.ca)** used as the live crawl-depth demo: homepage → Services (1 click) → specific service (2 clicks); homepage → Blog (1 click) → post (2 clicks) → "next page" arrow (3 clicks) → posts on page 2 (4 clicks, too deep). Category-tag shortcut collapses this: homepage → category (1) → full category archive (2) → post (3).
- Matt's own **"SEO lies"** blog post audited live on-call: found only **2** outbound internal links (below his own 3–5 target), linking to "what is a white hat backlink" and "creating tools to naturally gain backlinks" — flagged as needing more links added.
- Matt's own site audit shown live: **317 broken links** flagged, pending a recrawl after recent fixes.
- **Samir** — electrical company, building "AI-first," uses Framer + an MCP connection from Framer to Claude. Ranked #1 "most favorite business" on Nextdoor in 2024 and 2025, #1 on the Tesla Certified Installer Network, 50+ five-star Google reviews. Operates across LA County, Orange County, Riverside County (70+ jurisdictions/municipalities). Building an EV-charger comparison quiz as top-of-funnel content after finding via SEMrush that nobody bids on "best EV charger" despite it being a frequent search.
- **Peter Palmioto** — Medicare insurance broker, Maryland, runs sub-agents across multiple states, 20+ years doing SEO, says he's made "millions of dollars" from SEO over his career. Auto-generated a batch of AI blog posts that are indexed but not ranking (advised 301 or 404). Markets across the Mid-Atlantic (MD/DE/VA); asked about state-level money pages — deferred to a 1:1 look inside Insiders.
- **Kelsey** — solo business owner wearing many hats (does her own HR/payroll), can commit only ~1 hour/week, feels overwhelmed by the volume of Hey Tony content across platforms. Her "kitchen remodeling" content isn't ranking anywhere near page 1 ("not even on the sixth or seventh page"); guided to Google Search Console plus a keyword tool, and to introduce herself in the community for tailored direction.
- **Mike Eastman** — site built on Canva, only 5 pages total. Building an AI-literacy education business for kids/parents with no obvious local competitors; used ChatGPT to identify likely competitors, then advised to mine their keyword gaps via Ubersuggest/SEMrush.
- **Yehoshua** — mortgage broker. Asked pillar-page vs. long-tail-article strategy (Matt: don't force it, let cornerstone pages emerge naturally) and Ubersuggest-vs-SEMrush accuracy (source of the 3,600 vs. 750/month example).
- **Susan** — self-taught SEO, already ranking for multiple keywords but sees day-to-day rank "bouncing" between page 1 and 2; was paying for a daily rank-alert tool — told to cancel it and check monthly instead. Notes one specific competitor holds #1 consistently for her keyword.
- **Julia Dobkins** — works with an energy-healing/alternative-wellness client who deliberately hides certain pages (e.g. a quiz lead magnet), yet those pages still surfaced when the client searched her own name. Also relayed an unverified rumor that AI "filters" specific wellness/spiritual words and suppresses rankings — Matt has never heard this from any SEO expert he knows.
- **Leo Da Silva** — built a more advanced bank-lending comparison calculator for property investors than competitors' simple calculator tools; how to differentiate/target the same keyword deferred to a live 1:1 screen-share inside Insiders.
- **"Hey Tony" name origin**: coined around 2017–2018. Matt overheard two large construction workers swapping Toronto streetcar tracks; one said, "Hey Tony, you always know how to put a smile on my face." Matt wanted that warmth/authenticity association instead of a generic "[Name] Marketing/Digital" agency name.
- A copycat seller impersonated Matt/his book on Amazon at one point; reported and successfully removed.

## Notable verbatim quotes (only memorable/strategic ones)

- "The harder it is for a human to find your page, the less likely Google will care about it." (repeated twice, stated as the session's core thesis)
- "If you hide things from the user, you're hiding them from Google."
- "We want to get Google trapped on our website."
- On orphan pages: "This is a page that has been taken out back behind the barn and shot and forgot about."
- "Every blog post should link to three to five other posts and one money page... Every time you publish a new blog post, link to it from three older blog posts" — described as the entire internal linking strategy, done.
- "If it's useful to a person, it'll be useful to Google."
- To Susan, on daily rank-tracking anxiety: "Cancel that tool right away because that is just giving you anxiety."
- On budget objections: "Will money be tighter or less tight if you don't get new clients?"
- "Hey Tony, you always know how to put a smile on my face." (origin of the brand name)
- On gaming SEO plugins: "You're gaming Yoast essentially, which is not going to be good."

## Tradeoffs & nuance

- Orphan pages are bad practice by default, but deliberately useful for content you don't want found (lead-magnet quizzes, job postings, ad landing pages) — pair intentional exclusion with a real no-index tag, since a page can still surface (e.g. in an ego-search) even without internal links pointing to it.
- Dropdown/mega menus don't add crawl-depth clicks by themselves, but overloading them hurts usability — real tension is UX (especially mobile, ~50–60% of traffic) vs. cramming navigation.
- Sending blog readers to more blog content rather than hard-selling every time increases pages-per-session/dwell time — a positive signal — but don't force irrelevant CTAs or product galleries where they don't fit (e.g. a 3-product store shouldn't gallery-dump on every post; link the one relevant product).
- Pillar/cornerstone pages: don't plan content architecture around the concept upfront — "don't let that dictate what you should focus on first"; let them emerge naturally from keyword research and regular publishing.
- Keyword tool choice is a budget tradeoff: Ubersuggest is cheap and directionally correct but overstates absolute volume vs. SEMrush/Ahrefs — fine as a budget stopgap, not for literal magnitude.
- Lifetime/annual tool deals reward the vendor more than the buyer if usage isn't sustained (most people quit SEO after a month or two); Matt's own agency pays a premium to stay on monthly billing specifically to hedge this risk.
- Real vs. AI-generated/stock photography (raised in Q&A, general principle): authentic, imperfect real photos build more trust for local/trade businesses than polished AI or stock imagery, which viewers increasingly recognize as repeated across competitor sites in the same niche (e.g. dental sites reusing identical stock photos).
- Rank-position volatility day to day is expected noise, not a signal to act on; a competitor holding #1 steadily may simply mean Google hasn't found reason to promote anyone else yet, not always a discrete fixable problem.
- Renaming "blog" for branding polish (e.g. "Learn Hub") is a pure UX/clarity cost with no offsetting SEO upside.
- Small-site (~5 pages) internal-link cleanup can be done all at once — no indication a staged/incremental rollout is needed at that scale, though the general 10–20-links-per-page ceiling still applies.
- Insiders scaling concern (echoed from prior sessions): more total members doesn't mean less individual attention, since not everyone attends every call and people stop needing help once their specific question is answered.
