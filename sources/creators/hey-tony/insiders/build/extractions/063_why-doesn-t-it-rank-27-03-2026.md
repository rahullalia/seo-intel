# 063 — Why Doesn't It Rank (27.03.2026)

## Tactics & step-by-step how-to

- **Blog vs "resources" naming (Maria's general-contractor site)**: keep the literal word "blog" in the nav — don't rename it to "resources" or "news" thinking it'll read better to an AI crawler; humans need to recognize it as a blog, and renaming doesn't change how AI scans the site.
- Blog/guide pages should stay **general** (not city-specific), even on a site serving 20+ cities. Only mention a specific city contextually within the body copy (e.g., "if you're looking for a complete home renovation in Scottsdale...") and link out to that city's dedicated location page from there.
- Optional structure: keep one general guide (e.g., "Kitchen Guide") plus a button/CTA on it that filters to a city+service-specific version of that same guide for whichever location page the user came from.
- **Location/service page building (Kenneth's tactic behind his grid-map win)**: go in and create detailed, individual location pages and service pages per neighborhood/area rather than one generic area page — this is what moved him to #1–#3 across a 2.5-mile grid map.
- Testing (result not yet back): embedding GPS coordinates in image metadata for photos used on location pages, as a possible ranking signal for map/grid rankings.
- When a competitor is beating you on map rankings, check their **Google review count** and **local citations** (e.g., chamber of commerce, local business directories) as likely causes before assuming it's something technical.
- **One keyword/topic per page.** If multiple pages are all optimized for the exact same keyword, fix it by making each page's keyword a distinct variant: "[keyword] + location," "[keyword] + best practices," etc. — never the identical bare keyword repeated across pages.
- **Blog post titles as full questions**: don't force a short 2-4 word "keyword" into a question-style title — the entire question IS the keyword. Website-builder SEO tools will choke on a full sentence as a "keyword field," but that's fine; ignore the tool, follow how people (and LLMs) actually search now — longer, more specific queries.
- **Overwhelm fix**: set a realistic, small recurring goal — e.g. one hour a week fixing keywords/titles, or "fix 2 pages a week" / "fix 10 pages a week," whatever is sustainable. SEO is a marathon, not a sprint.
- Attend the **Monday work sessions** — live, guided blog-post writing during the call — as a forcing function for weekly progress; if you can't attend live, watch the replay and pause it at the point writing starts, then do the exercise yourself with a dedicated hour.
- **Migrating platforms (Kartra → WordPress, Emily's case)**: don't do extra SEO work on the soon-to-be-replaced site. Instead, write blog posts now but hold publishing until the new site is live. Build a backlog; once live, publish at whatever cadence (1–2/week) to keep a steady drip without needing to write in real time.
- **Blog page critique (Matt Paro's "iPad magic tricks" post)**: don't restate the H1 in a giant hero image directly below it — redundant and pushes the answer below the fold. Don't make the user scroll to start getting the answer. State the direct answer/list immediately near the top (e.g., H2 = "Here are five magic tricks you can see on an iPad," followed immediately by the first trick).
- Putting the exact keyword very early (per tools like Rank Math) doesn't have to mean literally repeating it as an H2 identical to the H1 — better to just have the keyword naturally appear within the first couple of sentences of body copy instead.
- **Competing on word count**: match or slightly exceed competitors' word count, but the real lever is what content is actually attracting users to their page — study that, don't just pad length.
- **Homepage CTA cleanup**: identify the ONE action you actually want a visitor to take (e.g., "send an inquiry"), then strip out every competing CTA (Call Now, Email Now, WhatsApp Now, Book Now, Inquire Now all stacked together). Keep the phone number/email visible in the header, but reduce the action buttons to one clear, bigger CTA.
- **Contact/booking page**: don't add filler copy like "complete the form below" — just show the form itself (left or right column) plus the alternate contact channels (call / email / WhatsApp) without redundant labels.
- **Diagnosing non-indexed pages**: Google Search Console → **Indexing** (left sidebar) → **Pages** → scroll down — GSC will state the specific reason a page isn't indexed.
- **Diagnosing a ranking drop**: use GSC's **Insights tab**, which shows which queries/pages are trending up vs. down. If something you changed is trending down, either give it time to recover or revert that specific change and watch for it to come back.
- **Iframe-embedded tools (Joshua's mortgage calculator)**: if a calculator/tool is pulled in via iframe from a separate platform, Google sees it as belonging to that other site, not yours — rebuild or integrate it so it's native/embedded directly on your own site's code.
- Put functional tools (calculators, etc.) at the very top of the page — Joshua's required 3 scrolls to reach his; that's a fix, not just a nice-to-have.
- Build more **internal links using descriptive anchor text** pointing at your money/tool page — identified as the likely gap versus competitors who outrank you for the same tool/page.
- Ignore "AI-generated content" detector flags entirely — don't hunt for a tool/platform that gives a "unique" checkmark; it doesn't matter for ranking.

## Rules / dos & don'ts (keep every threshold, number, specific)

- Never reuse the identical exact keyword across multiple pages — it risks being flagged as duplicate content.
- Local/city-based targeting is **not required** for affiliate-marketing sites unless the business genuinely serves a local area.
- Always compare **28 days vs. previous 28 days** in GSC — never 7-day vs. 7-day; short windows are too noisy and search-term usage shifts across a month.
- Check rankings **monthly only**, not daily — "if you look at things daily, you're going to drive yourself crazy," make too many changes, and not give Google time to properly index/settle where a site belongs.
- Don't obsess over maxing out SEO scoring tools (builder's on-page checker, Rank Math, Rank Report Card) to 100%/A-plus — "sometimes you need that D to help you rank"; SEO isn't about perfect scores everywhere.
- When two sites (old vs. new) are both ranking and competing against each other: don't do 301 redirects reflexively. Leave both live, pick the one with more traffic/better rankings for target keywords to actively work on, and just stop updating the other — don't abandon or delete either yet.
- Changing a ranking page's URL is risky — the old URL may carry backlink authority/"juice" the new one starts from zero on ("new kid at school, nobody knows who they are"). Confirmed cost: a client's re-optimized-URL money page still wasn't indexed 2–3 weeks after the change despite internal links, external links, a 301 from the old URL, and sitemap inclusion.
- On a non-WordPress website builder, a missing "SEO section" on individual blog posts is fine as long as each post still auto-gets a title tag and a meta/OG description.
- Rank Report Card checks roughly **50 ranking factors**, including: H1 tag present, GSC connected, mobile-friendliness, page speed, accessibility score, mobile tap targets, mobile font size, and content length flagged if under **300 words**.
- No free tool exists for daily/automatic keyword rank tracking — "everything is paid."

## Tools, prompts & resources

- **Link Gap Analyzer** (linkgap.io / "Backlink Gap analyzer") — lead magnet built with **Claude Code**; enter a site/competitor URL, get backlink gaps and opportunities (where competitors are cited and you're not); email required for the full report. Already cached data behind it, so it works instantly. Not branded to Matt beyond a small "brought to you by Hey Tony" footer line — driving organic shares from people who don't know Matt built it (referenced: someone in India cited it in a non-English video).
- **Topic Cluster Analyzer** — lead magnet tool, also built with Claude Code.
- **Rank Report Card** — lead magnet tool; ~50 ranking-factor check (see above), emails a full report of warnings/fixes after email opt-in.
- All three tools + the site hosting them were built with **Claude Code**: "it made this entire site... it did all the functionality for me."
- **Google Search Console** — Indexing → Pages (why a page isn't indexed); Insights tab (trending up/down queries); Performance tab set to 28-day comparison windows.
- **SEMrush** — Matt's pick for keyword rank tracking ("I use Semrush to see everything").
- **Ubersuggest** — alternate paid tool that also does keyword rank tracking.
- **Looker Studio** — existing report template (currently used in the main Hey Tony program) still functions; Matt is building an upgraded version for Insiders, blocked on Google's approval to let members connect their own GSC to it. Planning a dedicated troubleshooting call (pending calendar check) since multiple members hit issues setting it up.
- **Rank Math** (WordPress SEO plugin) — referenced by Matt Paro as the source of the "keyword near the start of content" guidance that led him to duplicate the H1 as an H2 plus a giant restating hero image.
- Website-builder on-page SEO tool (Jillian's, non-WordPress) — pick 1 primary keyword + 2 backup keywords; must appear in meta title, meta description, and URL; gives a completion "score."
- **Instagram**: Kush Desai (@realkushdesai) cited one of Matt's pages/tools in a Reel as one of "three pages to use for SEO" (per Diana, who spotted and forwarded it to Matt).

## Case studies / examples / results

- **Victor** (movers, Washington D.C.): overall visibility +37%; new DC-movers page +300% views, impressions +20%, clicks +32%. Average position: 23.6 (3-month) → 16.3 (last 7 days) → 13.4 (last 24 hours). Also landed 3 organic sales in one day, zero paid ads involved.
- **AJ** (med spa, Scottsdale, AZ): "facials" keyword moved from page 4 to page 3 in 5 days, in a highly competitive niche.
- **Kenneth** (Tampa/St. Petersburg/Clearwater, FL client): 2.5-mile pin-to-pin grid map now shows #1, #2, or #3 rankings in every area he built detailed location/service pages for. Two competitor spots in the upper-right of the grid traced (not fully confirmed) to a competitor's stronger Google-review volume and consistency; testing GPS-in-image-metadata next, results pending.
- **Rodrigo**: client site impressions went from 1,020 to ~2,400–3,000 over a 28-day comparison (nearly tripled); clicks also nearly tripled; conversion rate identified as the next thing to fix.
- **Matt's lead magnets**: Link Gap tool signups went from ~6,000 to **7,600 within the prior week alone**.
- **Matt Paro** (event musician/magician, mattpyro.com): "iPad magician" page ranking on page 2; a separate "magic tricks you can see on an iPad" page already ranking #1 for that exact query. Homepage previously had 5 competing CTAs (Book Now, Call Now, Email Now, WhatsApp Now, Inquire Now) — trimmed down to one primary CTA ("send an inquiry").
- **Lori**: changed her money-page URL 2–3 weeks prior (during Rank Week) specifically to fit a target keyword; new URL still not indexed despite internal links, external links, a redirect from the old page, and sitemap presence.
- **Joshua**: mortgage-calculator tool page live over a year, retooled a couple weeks ago; getting impressions but not ranking or clicking. Calculator embedded via iframe from a separate web platform (looked to Google like content belonging to that other site). No dedicated blog section on the site. Copied a higher-ranking competitor's page layout closely (per Matt, possibly too closely) via incognito searches.
- **Sita**: photography business; moved Mauritius → Atlanta (5 yrs) → back to Mauritius (~1.5 yrs ago); kept an old Squarespace site and later built a new site on a new URL/template, and now both rank (positions ~10–15) and compete against each other. Old site pulls more overall traffic; new site ranks better specifically for "family photographer [location]." Advised: keep both live, work only the higher-traffic (old) site, leave the new one untouched and monitor — no redirects.
- **Jillian**: hypnotherapy site on a non-WordPress builder; post-Rank-Week meta title/description cleanup left "hypnotherapy" (bare, undifferentiated) as the primary keyword on nearly every page — flagged as a duplicate-content risk needing rework into location- or topic-specific variants.

## Notable verbatim quotes

- "SEO is a marathon, not a sprint."
- "Google doesn't care if it's AI generated. AI doesn't care if it's AI generated as long as it's helpful."
- "Sometimes you need that D to help you rank."
- "Don't make people scroll down to start getting the answer."
- On daily rank-checking: "You have permission not to [check daily]." / "Okay, I'll get that in writing."
- On a changed URL losing its old page's authority: "out with the old, in with the new, and the new is... brand new, new kid at school, nobody knows who they are."
- On the Link Gap tool being shared unbranded: "other people are just like, wow, this is a cool thing, I'm going to share this. And then they don't know that they are feeding my machine."
- "SEO is not about getting a hundred percent perfect scores everywhere."

## Tradeoffs & nuance

- Matching competitor word count is only a secondary signal — Matt explicitly redirects attention to *what* is attracting users on the competitor page rather than treating length as the lever.
- Old-vs-new competing site problem (Sita) has no clean single fix: Matt's answer is to keep both live rather than pick a winner outright, defer the redirect/deletion decision, and let the current traffic/ranking data guide effort allocation — explicitly framed as reversible ("you can always go in later and remove... or move content over").
- URL-change recovery (Lori) is presented as genuinely ambiguous causality — could be lost backlink authority, a content-similarity flag, or ordinary indexing lag. Matt's process is to check GSC's own stated reason first rather than guess, then choose between patience (keep blogging, wait) or reversal (restore the old link) — framed as "are you going backwards or forwards?"
- Repeating a keyword as both H1 and a restating H2 is called out as "a test that we do ongoing" — presented as unresolved/experimental, not settled guidance, despite tools like Rank Math recommending early keyword placement.
- SEO on-page scoring tools (builder checkers, Rank Math, Rank Report Card) are described as tools that "gamify SEO, to be like, yeah, you're doing a good job, even though you might not be" — passing the tool's checklist is explicitly decoupled from being correctly optimized, and can actively produce the duplicate-keyword-across-pages problem.
- Local-relevance advice is conditional, not universal: applies to local-service businesses; explicitly does not apply to affiliate/non-local business models unless there's a genuine local footprint.
