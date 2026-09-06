# Technical SEO with Elliot — 08.05.2026 (Call #047)

Format: live Q&A, raise-hand queue, live screen-share troubleshooting. Elliot Smith (technical SEO specialist, ~2 years at Hey Tony, works closely with Matt and Denroy; specializes in local SEO / Google Business Profile) subs for Denroy, who is out on paternity leave with a new baby (~1 week until his return). Question queue carries over unresolved issues from prior weeks — several attendees are called back specifically for follow-ups Elliot researched between calls. Duration 92m53s, ~16,723 words. Unanswered chat questions to be answered asynchronously in the Insiders group.

## Tactics & step-by-step how-to

- **Google Business Profile (GMB) post-linking chain:** every new post should carry three links: (1) the share-link of your immediately previous post, (2) a website link to a valuable service page, (3) your CID link. Chaining post→post links this way signals to Google that the profile is active and its posts are interconnected, which builds local-profile authority.
  - To get the previous post's link: click the three-dot menu on that post → **Share** → copy the link → paste into the new post.
  - Whatever new post you make next, link back to *that* one — continually roll the chain forward.
- **Getting your CID link (primary method):** copy your Business Profile's Share URL, paste it into a CID finder tool. Sometimes the tool fails to retrieve it.
  - **Fallback method when the tool fails:** right-click your profile link → **View Page Source** → search the page (Cmd+F on Mac) for "Ludo" (transcribed; the section is labeled "Ludo CID link") → the long number next to it is your CID.
  - Post format used: structure it as `maps.[cid link] = [long CID number]`.
  - Reuse the same CID link inside blog posts and service pages (not just GMB posts) wherever it fits naturally — this passes profile authority through the site and increases profile visibility. These links exist for the search engine, not for human visitors.
- **Diagnosing/fixing low-indexed pages (worked live on Katya's portfolio site, 12 indexed / 39 not indexed):**
  1. Identify which un-indexed pages are actually worth indexing — do they drive business (corporate/case-study pages aimed at your real target client) or are they filler?
  2. Keyword-check the page's topic with a real tool (SEMrush free trial, or the Hey Tony Insiders keyword tool / Reddit topic tool) to confirm search volume exists — the exact phrase you're describing the page with may not be a real searched term; look for the variant that actually gets traffic.
  3. Decide what value the page provides a visitor landing on it (showcase work vs. educate them) — this is literally what Google's crawl is evaluating: "what is this page about," then "what value will indexing it provide someone."
  4. Fix heading structure: one clear H1 (e.g., the event/project name), H2s for sub-elements (e.g., "event branding"), more depth added underneath each H2.
  5. Internally link the page from other related pages on the site (e.g., cross-link similar case-study/portfolio pages to each other) — once the page is optimized and the keyword has confirmed volume, internal linking is "the best, most tangible way" to get it to index.
  - Expect a multi-week lag: "Google does take a couple weeks to go over" changes.
  - Social-media links back to a page (e.g., LinkedIn posts) carry much lower link authority than a referring website or internal link — still worth doing, just don't expect it to move the needle much on its own.
- **Requesting indexing in GSC:** Indexing → Pages tab → find the not-indexed list and reasons → click into a page (or paste its URL in the top Inspect bar) → click **Request Indexing**. Two outcomes: "request submitted" or "indexing request rejected" (rejection usually means the page's been taken down or has another blocking issue). Not instant — expect delay.
- **Redirect conflict where redirects are already correctly in place (A.J.'s case):** don't re-undo/redo the redirect — instead do a sitemap resubmission in GSC (Indexing → Sitemaps → paste sitemap URL → Submit) so Google recrawls and catches up.
- **Reverting a slug/URL change (A.J.'s "-2" duplicate-page case):**
  1. Check GSC to see which URL (old vs. new) is actually getting traffic.
  2. Whichever version has the traffic is the one to keep; if the newer one has little/no traffic, revert.
  3. Delete the current redirect, then create a fresh redirect that points the new URL back to the old one.
  4. Don't delete any pages yet — test the revert first.
  5. Monitor for about a month; if the abandoned duplicate's metrics fully drop off, then remove that page.
- **Real-estate/listings indexing triage (Kai's site, sitemap 87 pages / GSC showing 24 indexed, 113–140+ not indexed depending on the report viewed):**
  1. Check GSC's "crawled — currently not indexed" list and cross-reference against any recent site rebuild/migration date (look for a drop-off/dead zone in the timeline around the switch).
  2. Rank un-indexed pages by importance before spending optimization time — are they money pages (bio/about, area-served) or lower-priority (blog, sold listings)?
  3. For real estate specifically: once a listing sells, **archive it** (keep it visible on the CMS backend but pulled from public/Google visibility) rather than leaving a "dead page" live — dead pages drag down overall site health and authority.
  4. To retain the marketing value of past sold work, build dedicated case-study/service pages (e.g., "how we stage homes in Muskoka," "the type of million-dollar homes we sell in Muskoka") instead of leaving individual sold-listing pages indexed.
  5. For thin pages like a bare Contact form: add even a short paragraph of real, keyword-relevant copy underneath the form (e.g., "Contact me — I'm your [location] realtor") — a page with nothing but a form is a common reason Google skips indexing it.
  - To explain sitemap-count vs. indexed-count mismatches: sitemaps still list redirected pages and 404 pages, so sitemap total ≠ true indexable page count. To verify what's really indexed, grab a clean (non-404) live URL and run it through URL Inspection in GSC.
- **Domain property vs. URL-prefix property confusion (Carolina, then Ariel — same question 2 weeks running):** always use the **Domain property** for your data/reporting — it's the umbrella that rolls up every URL variant (http/https, trailing-dash variants, etc.) underneath it. The separate URL-prefix ("https://…") property that shows up alongside it usually stems from a past protocol/URL change; don't bother trying to delete or merge it (Elliot looked into it — "a lot of hoops") — just ignore it and read the Domain property instead. Separately, confirm your actual live site URL is HTTPS.
- **Hand-coded FAQ schema drawing a bot swarm (Carolina):** if a hand-coded/third-party FAQ schema snippet is legitimately winning AI-search visibility but is also attracting a heavy AI/training-bot crawl, the fix is not to remove the schema — take the code snippet to **Claude**, explain that bots are combing the site, and ask it to add a snippet/rule that blocks the bad-bot crawling while preserving the FAQ schema itself.
- **Ecommerce dead pages / limited backlinks (Jorg):** once on-page optimization and internal linking are already done, the next lever is backlinks — either organic/free methods (from a prior call) or paid backlink buying (Matt supplied two resource links, pasted in chat, exact URLs not read aloud). When time is limited, prioritize pushing traffic/clicks to pages that are **already indexed** rather than spreading effort trying to get every dead page indexed at once; circle back to the unindexed backlog after.
- **CMS-limited platform (Ariel, on Showit) with a sitemap that won't fetch:**
  1. Verify the real sitemap URL directly by appending `/sitemap.xml` to the root domain and viewing it in-browser (Yoast-style sitemaps show 4 sub-sections: posts, pages, categories, authors).
  2. Copy that exact URL, paste into GSC → Sitemaps → Submit.
  3. If GSC still shows "couldn't fetch" after resubmitting the verified URL, suspect a platform/CMS-level limitation rather than a sitemap-content error.
  - Migrating CMS (e.g., Showit → WordPress) does **not** reset SEO from scratch as long as the domain stays the same — backlinks and authority persist, only the platform/design changes. Treat migration as a "longer down the line" move if the business is busy/thriving on the current limited platform now; hire an experienced person for the actual migration.
  - Interim strategy while stuck on a limited platform: proper heading structure, added content, internal linking, and dedicated location pages — "work within the confines of what you have."
- **Local-first keyword strategy for a new/low-authority site in a big-city market (Ariel, Chicago-suburb newborn/family photographer):** don't target the broad, maximally competitive city-wide term first. Build a small locational/neighborhood page (or a specific description page distinct from the homepage) targeting your immediate area, establish authority there, then broaden out toward the bigger city term over time.
  - Reference case: a past photography client in Chilliwack, BC — homepage targeted niche + "Chilliwack," while separate location pages targeted the surrounding Fraser Valley suburbs (Vancouver West, Abbotsford, etc.), chosen specifically because keyword research showed *more* traffic in the smaller local area than in the broad regional term.
  - Build sequence: optimize/build core service pages first, then progressively branch into additional location-targeted pages — framed as less overwhelming than trying to build everything at once.
  - Use a real keyword tool (Hey Tony Insiders' free tool, or SEMrush) to confirm actual search volume before committing to a keyword — don't rely on GSC's own built-in keyword-insight popup, which surfaced only a generic, low-value term ("photography") in this case.
- **Service-area page restructuring (Jessica, Long Island NY, Suffolk/Nassau counties):** original page was one long flat list (county → town → city, everything on one page, each city linking straight to the same generic service page). Matt's recommendation: restructure so clicking a Town surfaces/brings up the Cities within that town, rather than a flat list. Elliot's addition: use the restructure as the opportunity to build dedicated individual pages for the highest-opportunity cities (traction, underserved/easy-to-rank markets) — not all ~20 towns/cities at once.
- **Fixing a broken/non-working sitemap plugin (Bill):** use a standalone sitemap-generator tool as a fallback:
  1. Input your website URL, generate the sitemap.
  2. Tool crawls the site and lists pages as "added" or "skipped" (skipped = e.g. pages taken down or archived pages still technically discoverable) — don't worry about skips.
  3. Click Download to get the XML sitemap file.
  4. Go to GSC → Sitemaps → submit/upload that XML file. This becomes the fix when a plugin (e.g., broken Yoast setup) won't generate a working sitemap.

## Rules / dos & don'ts (keep every threshold, number, specific)

- GMB posts: link previous post + website link + CID link, every post, ongoing.
- CID/cross-post links are for the search engine, not for human visitors — don't expect them to drive click-throughs.
- One sitemap per site is the standard rule of thumb (especially new WordPress sites); some complex/legacy sites legitimately run 4–5 split by content type — that's the exception, not the norm.
- Changing a URL/slug — even on what feels like "the same page" — creates a brand-new page in Google's eyes. Expect (and verify) a redirect gets generated.
- Never re-redirect back and forth blindly — check GSC traffic on both URLs first to decide which to keep.
- Don't delete pages or redirects preemptively; test a revert first.
- Monitor ~1 month after any redirect flip before removing the abandoned duplicate page.
- Archive sold/closed real-estate listings once sold; don't leave them live and indexed as dead weight.
- A page with nothing but a bare contact form is a common non-indexing cause — always add real supporting copy.
- Sitemap totals are not the same as true indexable-page count — sitemaps still list redirected and 404'd URLs.
- Always read data from the GSC **Domain property**, never the URL-prefix property; don't bother trying to delete the URL-prefix duplicate.
- Site must be served over HTTPS.
- Social-media backlinks carry low link authority relative to referring websites or internal links.
- Paid backlinks: no guaranteed/known ROI — Elliot explicitly wouldn't vouch for it either way; framed purely as the owner's own budget/risk call.
- When time is limited, prioritize pushing traffic to already-indexed pages over chasing every unindexed page simultaneously.
- CMS/platform migration preserves backlinks/domain authority as long as the domain doesn't change — only the platform/design resets.
- Don't chase a maximally broad, high-competition city-wide keyword on a new/low-authority site — win neighborhood-level terms first, expand later.
- Build location/service pages for highest-opportunity areas first, not all at once.
- If a hand-coded schema snippet (e.g., FAQ) starts drawing heavy bot abuse, patch the bot-blocking, don't strip the schema that's earning AI-search visibility.
- Request Indexing is not instant — "Google does like to take its sweet time."
- "No referring sitemaps detected" in GSC may indicate a genuine sitemap-level issue, not just an internal-linking gap (flagged by Elliot as something to look into further, not resolved live).

## Tools, prompts & resources (exact prompt wording if quoted; tool names; settings)

- **Google Search Console (GSC)** — used throughout for: Indexing/Pages tab, Request Indexing, URL Inspection, Sitemaps submission, Domain property vs. URL-prefix property, and (per Ariel) its own built-in keyword-insight popup (called low-value/generic in this instance).
- **SEMrush** — free one-week trial mentioned for keyword-volume checks; also flagged as something beginners can "get lost in" compared to Hey Tony's own tool.
- **Hey Tony Insiders' keyword research tool** (free to members) and a **Reddit topic research tool** — recommended as a simpler starting point than SEMrush.
- **CID Link Finder tool** — paste in your Business Profile Share URL to auto-retrieve your CID link; documented failure mode (doesn't always work), with a manual view-source fallback (search "Ludo"/"Ludocid" in page source).
- **Claude** — explicitly recommended to patch a hand-coded FAQ schema snippet so it blocks abusive AI/training-bot crawling without removing the FAQ schema itself. Suggested framing: explain the bots are combing the site off the schema snippet and ask for a way to block that crawling.
- **Yoast SEO** — referenced for standard WordPress sitemap structure (4 sub-sitemaps: posts, pages, categories, authors) as the "what it should look like" reference when troubleshooting a broken sitemap.
- **Standalone sitemap-generator tool** (unnamed brand in transcript) — enter your site URL, it crawls and lists pages as added/skipped, download the resulting XML sitemap, submit that file to GSC. Used as Bill's fallback since his plugin-based sitemap wasn't working.
- **Cloudflare** — adopted by Carolina as a bot/DDoS-style mitigation layer; its SEO impact was explicitly left open/contested (see Tradeoffs).
- Two backlink-buying resource links (from Matt, relayed by Elliot to Jorg) — pasted in chat, not read aloud/named in the transcript.

## Case studies / examples / results (names, niches, numbers)

- **Niri** — asked (for the second time, after a lost recording) how to structure GMB post links; walked through live: previous-post share link, website link, CID link.
- **Katya** — graphic designer, ~3-year-old portfolio site, based in Quebec (French-language version exists). GSC: **12 pages indexed, 39 not indexed** (a separate view in the same session showed "22 pages" for a specific issue group). Zero real discoverability beyond direct/social links; hadn't started blogging yet ("I'm just trying to fix what I already have"). Target pages are corporate-client case studies (e.g., a symposium branding project) she needs surfaced for a specific target audience.
- **A.J.** — flagged 3 sitemap "conflicts" by an audit tool: 2 were redirects already correctly implemented; 1 was a slug he'd changed twice, creating a "-2" duplicate-page situation. Discovered WordPress (or an SEO plugin on it) auto-generates a redirect on slug change — surprised Elliot ("I've never heard of WordPress automatically doing a site redirect").
- **Kai** — realtor. Sitemap: **87 pages to discover**; GSC pages report: **24 indexed**, **113 not indexed** (also referenced ~140 total pages and, later in the call, "89" on the sitemap vs. "24" indexed — numbers were inconsistent as spoken, with Elliot's explanation being that sitemap totals include redirects/404s). Site was rebuilt by a new provider starting March, with an indexing dead-zone around March 21 before resubmission in early April (took 2 sitemap iterations to get right). Money pages = About/bio page and the "area I work in" page. Sold listings identified as dead-page drag; discussed archiving them and instead building case-study content (e.g., "how we stage homes in Muskoka," showcasing past luxury listings). Thin Contact page flagged as needing supporting copy.
- **Carolina** — asked the domain-property-vs-URL-prefix question (same question Ariel had asked the prior week). Hand-coded FAQ schema via a small third-party snippet tool (input questions → copy generated code → paste at page bottom) because her main SEO tool didn't natively support FAQ schema. Result: bot traffic spiked to **150,000 visits/day** on a site that normally gets **~40 visitors/day**; had to bring in a cybersecurity consultant, had her hosting IP fully reset, and adopted Cloudflare to survive it. Upside: "Google's AI is now recommending me because of those [FAQs]."
- **Jorg** — ecommerce site. Backlinks: **now ~4**, up from ~2 two weeks prior ("at least some more than two weeks ago"). Weighing paid backlink-buying against still-low site revenue; advised to prioritize internal linking and doubling down on already-indexed pages before spending on paid links or chasing every dead page.
- **Ariel** — photographer based in Chicago suburbs (studio ~3–10 minutes from the city border, not downtown), targeting "wealthy suburbs plus Chicagoland." Platform: **Showit** ("drag and drop," partly built by a hired freelancer). Sitemap showing effectively 0 pages / "couldn't fetch" in GSC despite a verified, correct `/sitemap.xml` URL — left as an open platform-level issue for Elliot to research further. Took a photographer-specific SEO course leaning on old-school keyword stuffing and long-tail keywords; historically ranked ~page 8 for "photographer near me" (not recently re-checked). Told domain/backlinks would carry over if she eventually migrates to WordPress. Reference case Elliot cited: a past Chilliwack, BC photography client — homepage targeted niche + Chilliwack, location pages targeted Vancouver West/Abbotsford/Fraser Valley suburbs based on keyword-volume research showing more local traffic than the broad regional term. GSC's own recommendation popup surfaced a generic "photography" keyword, called low-value.
- **Jessica** — Long Island, NY, service-area page covering Suffolk and Nassau counties. Original structure: one long page, counties → towns → cities all flat, cities linking straight to the same generic service page. Restructuring per Matt's guidance (discussed with him directly earlier that week) into a county → town → city click-through hierarchy, with dedicated pages to follow for the highest-opportunity cities.
- **Bill** — carried over from the prior week: sitemap.xml route wasn't working, no functioning plugin-based sitemap. Given a standalone sitemap-generator tool as the fix path (generate → download XML → submit to GSC).

## Notable verbatim quotes

- On the GMB post-chain: "The best thing you can do is get the link from the previous update you just had on the profile... and what that does is that gives like almost a backlink, referring to the previous post you just made."
- On the CID link's purpose: "Your CID link is basically a very specific code that Google gives you... it is really, it has a lot of value and juice or like authority behind that link."
- "It is more so for the search engine over anything than it is for... actual people to see."
- On what Google evaluates before indexing: "What it's doing is it's first looking through, okay, well like what is this page about?... And then the second thing is, okay, well if I'm going to index this page, what type of value is it going to serve by serving it to someone?"
- On internal linking as the fix: "As long as there's a healthy amount of internal links between your site, that's probably the best, most tangible way."
- On social-media links: "It's called link authority. And so sometimes... social media is a really well-known thing and it's great... However, the link authority with those is quite low. So it's not going to pass as much authority to it as let's say if you have a referring website."
- On slug changes: "If you change the URL at any capacity, that does make it a new page, even though you just changed the URL... Just as a rule of thumb."
- On dead real-estate listings: "Having a bunch of dead pages on your site will affect your SEO score."
- On sitemap totals: "The sitemap basically combinates everything. So redirects, 404 errors, like, everything. It sees everything."
- On the Domain property: "As a rule of thumb, use the domain property one, like, first and foremost — that's going to have the most accurate data."
- On the FAQ-schema bot storm (Carolina): "A good day for me is like 40 visitors"... "it reached the peak, reached 150,000 visits per day"... "They had to completely shut down my IP and give me a new one because it was just, it was a catnip for them."
- On the payoff despite the chaos: "The FAQs are helping. Like I'm being recommended on Google. Like Google's AI is now recommending me because of those."
- Elliot's fix recommendation: "I would recommend if you go to Claude and put it in... explain to it that... these chat bots are like trying to comb my site... can you please look at this and see if there's any way that you can make it so that it doesn't [crawl the site]."
- On CMS migration risk: "If you did a site migration longer down the line, that would include all of that... I think as long as you keep your domain the same and everything, you would still save your backlinks."
- On chasing a broad city keyword too early: "There is a lot of competition in Chicago going after wedding [photography]... you would have more success building at least a small locational aspect first and then broading out."
- On GSC's own keyword suggestions: "I would say the recommendations of Google Search Console aren't necessarily like the most helpful."
- On the Chilliwack case's targeting logic: "There was more traffic in her locational area than there was for the whole Vancouver Valley sort of thing."

## Tradeoffs & nuance

- Redirect flips cost real page authority (accumulated age, prior optimization, backlink history) even though backlinks nominally "pass through" the redirect — moving between URLs is never fully free.
- Archiving vs. deleting sold listings: Elliot prefers archiving (reversible, stays on the CMS backend) over deleting outright, but acknowledges the showcase value in past work — resolved by building separate dedicated case-study pages rather than leaving individual sold/transactional pages live and indexed.
- Paid backlinks: genuine cost/ROI uncertainty acknowledged rather than sold as a solution — "I don't know the effect... I cannot grab the effect" was the actual client's framing, and Elliot didn't push back with a confident guarantee either way.
- Domain property vs. URL-prefix property: the mismatch looks alarming but isn't actually a problem — the Domain property already aggregates everything, so it's not worth the technical effort to merge/delete the duplicate.
- FAQ schema is shown as a genuine double-edged tool: it's credited with getting Carolina recommended by "Google's AI," but the same implementation nearly took her site down via bot overload. The fix is to block the bad bots, not strip the schema that's delivering AI-search visibility.
- Cloudflare's SEO impact is left explicitly unresolved — Elliot cited conflicting Reddit opinions ("some say no effect... others say it can decimate your ranking in days if not configured by a professional") and declined to guess, deferring to Matt for a definitive answer next.
- CMS limitations (Showit) can be worked around with on-platform best practices even though a full migration would technically be "better" — migration is framed as a "longer down the line" move, not urgent, when the business is currently busy/profitable despite the platform's SEO limitations.
- Local-first keyword strategy is a function of current authority/competition, not a permanent rule — the same site can go after the broader city-wide term later, once smaller local wins build up authority.
- Some diagnoses were explicitly left open rather than force-fixed live: Ariel's non-fetching sitemap (suspected platform-level issue, no resolution given), the "no referring sitemaps detected" message (Elliot flagged it for further research), and Carolina's Cloudflare/SEO question — all pushed to follow-up in the Insiders group rather than guessed at on the call.
