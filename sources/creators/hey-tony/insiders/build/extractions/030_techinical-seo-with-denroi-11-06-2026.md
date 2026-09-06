# Technical SEO with Denroi — 11.06.2026 (HeyTony Insiders Call #030)

Speakers: Denroy (technical SEO lead, hey Tony, ~6 years, started with Matt in 2020 "before any of the social media stuff") — first call back after ~2 months of paternity leave (became a dad in April), smaller/casual live Q&A format this session. Attendees who asked questions: Varuna, Catherine, Mary, David, Neri (site referenced live as "Clement.com" but branded "Clevant" in Denroy's own phrasing — remote bookkeeping business, St. Petersburg, FL), Jorg.

## Tactics & step-by-step how-to

- **Diagnosing a WordPress site that keeps breaking on edits (Varuna, ~15-year-old WordPress site):**
  1. Check PHP version first — ask the host to confirm; want the newest (8.2), not an outdated version (6.2 named as the "old" example). Varuna's was already on 8.2, so ruled out.
  2. Next check hosting bandwidth/memory limits — specifically the "memory time limit" / "memory execution limit" (name varies by host). Most hosts default this to 30 seconds; if plugins/scripts need more, triple it to 90 seconds and re-test.
  3. Identify the failure mode: full 503/temporary downtime vs. partial breakage (menu messed up, some assets/images not loading).
  4. If it's a caching/speed plugin (Varuna uses WP Rocket): go to **File Optimization** and check "Minify JavaScript files," "Load JavaScript deferred," and the JS execution-delay setting — these very commonly cause assets/images to stop loading properly.
  5. Also check **Media > Lazy Loading** settings — combined with JS minify, lazy loading can stop background-image assets from loading, especially ones with effects/animations attached.
  6. If unsure how to safely edit these, hand it to a dev team to test/roll back rather than guessing.
  7. Denroy screen-shared hey Tony's own WP Rocket dashboard as a live reference (File Optimization tab has a custom post type exclusion showing "HT load post"; plugins like Ninja Forms need individual investigation per-site; hey Tony's own Media settings currently have **no lazy loading enabled at all**).

- **Handling seasonal/out-of-stock e-commerce product URLs (Catherine, apparel retailer):**
  1. Don't just disable/404 a product page the moment it's out of stock or out of season.
  2. Instead, hide the "Add to Cart"/"Buy Now" button or set inventory/stock to zero, and leave the page itself live.
  3. To fix nav-menu clutter (Catherine gets 5-6 new collections per season for one brand), remove the item from the navigation menu only — the underlying page/URL stays live and indexed.
  4. Ask: will this product ever restock? If yes → always keep the page live (stock = 0) rather than removing it, because taking it down (404 + redirect) causes Google to devalue the page, and bringing it back later means lost traffic history plus Google having to recrawl/rediscover it from scratch.
  5. If a product is genuinely "one and done" (never restocking) → okay to fully remove: set stock to zero, then create a 301 redirect to a relevant page. 301s (specifically) pass on link authority to the destination page.

- **Benchmarking blog word count and keyword density against competitors (recurring theme, Mary + David):**
  1. Manually Google-search the target keyword and note word counts of the top 3 ranking pages.
  2. Target roughly 10% more words than whichever of the top 3 has the highest count (e.g., competitor at 1,000 words → write ~1,100). Don't blow past that (e.g., jump to 2,000-3,000) — over-shooting risks "over-optimizing" the page even though you're still ahead of the top ranker.
  3. For keyword frequency: check how many times the top-ranking competitor(s) use the exact keyword, then use it once or twice more than the top count (they say it 10x → you say it 11x; they say it 5x → you say it 6x).
  4. For low-difficulty keywords, the gap can be small — if competitors mention it 2x, mention it 3-4x.
  5. One target keyword per blog post is enough — place it in: the title, the URL slug, and early in the body copy (second sentence, per the hey Tony example below). No need to run the whole title/content through Semrush or a keyword tool.
  6. When a benchmarked page significantly overshoots competitors on keyword count (David's case, see below), don't look at the aggregate — break it down **per individual keyword variation** (e.g., "auto repair" vs. "automotive repair" as separate metrics) and trim/add per-variation rather than uniformly.
  7. After word count and density are dialed in, benchmark **internal links** and **backlinks** the same way: if a competing page has 5 backlinks, aim to build 6; if it has 3 internal links, aim to build 4 (via a tool like Semrush to see competitor backlink/internal-link counts).
  8. Audit anchor text on those links: generic anchor text ("click here," "learn more") is unhelpful; rewrite to descriptive, keyword + location-included anchor text (e.g., "learn more about auto repair in [city]").

- **Structuring a homepage Q&A/FAQ section on a small site (Neri, Clevant — bookkeeping, St. Petersburg FL, live audit on call):**
  1. Since the site is still small (not hundreds of pages / dozens of service-location pages yet), keep the FAQ section short.
  2. Write each question around the focus keyword + location together (e.g., "Why should you hire a bookkeeper in St. Petersburg?", "What are the benefits of hiring Clevant as your bookkeeper in Florida/St. Petersburg?").
  3. As more service/location pages get built later, go back and update the FAQ answer toggles to internally link out to that new content.

- **Fixing a "canonical URL not self-referencing" flag (Neri, live audit):**
  1. Compare the actual live page URL (check if it has a trailing slash) against what the audit tool reads as the canonical tag.
  2. Common mismatch: the real URL has a trailing slash but the canonical tag doesn't (or vice versa) — tool flags this as "not self-referencing" even though the page is fine.
  3. Fix by locating the canonical URL field in the CMS (in Squarespace: inside page/site settings) and adding the missing slash so it exactly matches the live URL.

- **Structuring a "brand sale" collection page when reselling another company's products at a discount (Catherine, apparel retailer competing on a European lingerie brand):**
  1. Create one separate collection per brand being discounted, named "[Collection] Brand Name Sale."
  2. List all discounted products from that brand on the page.
  3. Add at least 1-2 paragraphs of unique content: state what the brand is, that the products are on sale, and something that differentiates your store from the brand's own site — don't just list products with zero copy.
  4. Accept going in that the brand itself will always rank #1 for its own brand name — target the "sale"/discount modifier instead, aiming to rank directly under the brand's own site.
  5. Build internal links to the sale page; get a press release mentioning the sale if possible, to help it rank.
  6. Go all-in on whichever discount-adjacent keyword (sale, cheap, discounted) has the highest search volume.

- **Adapting content strategy for Google AI Overviews / zero-click search (from Matt's internal test, cited by Denroy in response to David's core-update question):**
  1. Broaden mentions across as many different mediums as possible (press releases, social posts, etc.) rather than chasing fewer, "higher quality" mentions — presence/volume outweighs mention quality for AI Overview citation.
  2. Broaden geographic scope in written content: instead of writing city-specific (e.g., Hamilton, Houston), write around the full state/province (Ontario, Texas) to maximize AI Overview surface area.
  3. Bake in time-relevance: add the current year (e.g., "2026") into content, matching how AI models append the year to their own background searches (example given: Gemini silently appending "2026" to a query like "demolition cost" before answering).
  4. Don't prioritize high-domain-authority sources for these mentions — volume of mentions matters more than the authority of where they appear.
  5. Specifically build a Reddit presence: create your own subreddit and get brand mentions there — links back to your site aren't even required, mentions alone reportedly move AI Overview visibility.

- **Deciding city-specific vs. broad-region targeting for a remote/nationwide-capable service business writing a press release (Neri, bookkeeping, based in St. Petersburg FL but able to serve nationwide):**
  1. Optimize the actual ranking target around the single city you can realistically win (St. Petersburg) — chasing a whole state/country ranking is described as "extremely difficult" and multi-year/costly.
  2. Within that same content, explicitly mention that you also serve the wider state (Florida) and can service the whole country, without optimizing around ranking for that scope.
  3. This dual approach (narrow keyword target + broad service-area mention) is what wins both traditional local rankings and broader AI citations simultaneously.

- **Print-on-demand / broad product-term visibility in AI search (Jorg's question; Denroy's own side-testing of print-on-demand WordPress stores):**
  1. Ranking for broad generic product terms (e.g., "beautiful t-shirts") inside Gemini/ChatGPT/Anthropic-style answers is very difficult based on direct testing — no reliable playbook yet.
  2. What did help: sourcing backlinks from other sites — even very low domain authority ones — that specifically **describe the product**: what it's made of, how it was printed, what's printed on it, its print quality, rather than generic brand mentions.

## Rules / dos & don'ts

- PHP version: run 8.2, not an outdated version (6.2 given as the "old" example) — mismatched PHP + plugins/theme/JS is one of the most common causes of a site breaking after edits.
- Hosting memory/execution time limit: default is usually 30 seconds; hey Tony's own fix pattern is to triple it to 90 seconds when scripts/plugins are timing out.
- WP Rocket File Optimization (minified JS, deferred JS load, delayed JS execution) and Media > Lazy Loading are the most common causes of broken assets/images after a speed-optimization pass — test and be ready to roll back.
- Never straight-404 a seasonal/out-of-stock product page if there's any chance of restocking — hide the buy button or zero the stock, keep the page live.
- Only fully remove (zero stock + 301 redirect) products that are permanently discontinued ("one and done").
- Redirects must be 301s specifically to pass link authority to the destination.
- Content length: benchmark against the top 3 Google results for the target keyword; aim ~10% longer than whichever of the three has the most words — don't overshoot into 2-3x territory (over-optimization risk).
- Keyword frequency: match top competitors' usage count +1 (roughly); for low-difficulty keywords, competitors' count of 2 → use 3-4.
- One target keyword per blog post is sufficient — must appear in title, URL slug, and early body copy; no need to run full content through a keyword tool.
- Local keyword variations often need only 2-3 mentions to rank top 3 — don't force 10-12 insertions (David's "mechanic" example: 3 mentions beat competitors at 0 mentions, ranking top 3).
- When benchmarking backlinks/internal links against competitor pages, aim for competitor count + 1 (5 backlinks → build 6; 3 internal links → build 4).
- Anchor text must be descriptive and include keyword + location context — "click here"/"learn more" is flagged as generic and unhelpful.
- Canonical URLs must exactly self-reference, including trailing slash — a slash mismatch between the live URL and the canonical tag will get flagged as an error by audit tools even though it has no real ranking impact.
- A missing period after an abbreviation in title/meta (e.g., "St" vs. "St.", caused here by an AI-generated meta description running out of characters) does **not** affect actual Google search results — treat both forms as the same keyword for your own work, but note that some tools (Semrush named specifically) will treat them as different strings for keyword-density reporting, so you may need to run two separate reports in that tool.
- When reselling another brand's products, do not try to outrank the brand for its own brand name — that's not winnable; target the sale/discount modifier keyword instead.
- Brand-sale collection pages need real differentiating copy (1-2 paragraphs minimum), not just a bare product listing.
- Location strategy: optimize/rank for the specific winnable city; separately state (don't optimize for) the broader state/nationwide service area in the same content.
- For AI Overview citation: presence/frequency of mentions across many mediums matters far more than the domain authority of the site mentioning you.
- For AI Overview citation: broaden location references to state/region level, not just city, in content meant to build AI visibility.
- For AI Overview citation: include the current year in content since AI models append the current year to their own background queries.
- Image format: prefer WebP or AVIF; fall back to compressed JPEG only where the platform doesn't support the newer formats.
- Photo resolution: keep uploads under 2K; downsize large raw/DSLR captures (example: 5000×2000 shrunk to ~1000×1500) before upload rather than letting the platform serve the full-size file.
- Squarespace does not accept AVIF at all; WebP support depends on which Squarespace builder/version you're on (older builders may reject it) — fall back to compressed JPEG on older builds.
- Wix accepts WebP without issue.

## Tools, prompts & resources

- **WP Rocket** — caching/speed plugin; relevant settings are File Optimization (Minify JavaScript files, Load JavaScript deferred, delay-JS-execution) and Media (Lazy Loading). Hey Tony's live dashboard shown as reference; their own site currently runs with lazy loading fully disabled.
- **Easy Table of Contents** — WordPress plugin Denroy pasted into the call chat; historically used on the hey Tony site and "to this day on dozens of client sites" to generate the in-article table of contents; CSS is fully customizable (text size/color, toggle style, restrict to H2-only vs. including H3/H4).
- **Hey Tony's "X minute read" estimator** — not a named plugin; it's custom code built into the theme by their developer, scanning total word count to estimate read time. Denroy had no off-hand plugin recommendation for this but said he'd find one and post it in the Insiders community afterward.
- **Semrush** — used here for: pulling competitor backlink counts, competitor internal-link counts and anchor-text data, and keyword-density/audit reporting (noted as treating punctuation like "St" vs. "St." as literally different strings).
- **Matt's backlink tool** — a separate, proprietary tool (distinct from Semrush) that surfaces whether other sites recommend you as a backlink source; David used it to write a piece for a Texas-based automotive-industry site and discovered his own site is now recommended as a good backlink even without many backlinks of his own.
- **A "Page Audit"-type Chrome extension** (referenced by Neri as "not Page Audit... with that Chrome extension," matching the "Page Audit" tool named in other hey Tony calls) — used live to check title/description character counts, keyword density, and canonical URL self-referencing status.
- **Squarespace Assistant** — recommended as the go-to for platform-specific "where do I find X" questions (e.g., locating the canonical URL field, which lives in site/page settings).
- **WebP / AVIF** — recommended image formats for compression and load-time; compressed JPEG as the fallback where unsupported.
- **Matt Diamante's AI Overview citation test/article** — an internal test analyzing hundreds of keywords for what drives AI Overview citation; Denroy posted the article link into the call chat live and separately pointed Neri to it for worked examples of when specific-city vs. broad-region keyword targeting wins AI citations.
- **Reddit** (as a channel, not a research tool here) — creating a brand's own subreddit and accumulating mentions (no backlink required) was named as one of the most effective levers found for AI Overview visibility.

## Case studies / examples / results

- **Hey Tony's own site** — used live as the WP Rocket reference dashboard (File Optimization tab shows a custom-post-type exclusion for "HT load post"; Media tab currently has zero lazy-loading enabled). Also the source of the blog keyword-placement example: target keyword "cheapest keyword research tool" placed in the title ("What is the cheapest keyword research tool"), URL slug ("cheapest-keyword-research-tool"), and second sentence of body copy ("The cheapest keyword research tool worth using in 2026").
- **Varuna** — ~15-year-old WordPress site that breaks frequently on edits, requiring hosting-company calls and backup restores; already on PHP 8.2; uses WP Rocket; walked through File Optimization and Media/lazy-loading settings live. Separately has a new client on Webflow and asked if Denroy could help troubleshoot it (Denroy: "I know webflow a bit below the basic level, but... webflow still gives me some headaches").
- **Catherine** — apparel/lingerie retailer based on "an island in the English Channel," selling primarily to the UK. Two separate questions: (1) seasonal/out-of-stock product URL handling amid getting 5-6 new collections per season for one brand; (2) building sale collection pages for discounted resold brands, using a brand referred to inconsistently in-call as "Marion Melhorn"/"Prima Donna"/"Mary Jo"/"Marie Jo" as the worked example — since that brand also ships direct-to-UK from Europe, the identified differentiator for Catherine specifically was absorbing more of a pricing/margin hit than the brand does, not a shipping-origin advantage.
- **Mary** — asked a cluster of blog-writing questions off the live hey Tony blog: the "X minute read" custom feature, the "In This Article" table of contents (built with Easy Table of Contents historically, now custom), word-count/keyword-frequency benchmarking method, and image format/resolution rules; confirmed she publishes on Squarespace and separately asked about Wix — landed on: Squarespace = no AVIF, WebP support version-dependent; Wix = WebP fine.
- **David** — auto repair shop, live keyword-density benchmarking walkthrough: top 3 competitors ran 1,500-2,000 words; David started at 1,300, raised to 2,010 words (closest competitor below him sat at 2,002 — confirmed as a fine, non-excessive gap). Keyword counts: "auto repair" ×26, "automotive repair" ×17 — combined total beat competitors' combined total by 12 instances, which David felt was overshooting; advised to break down and trim per keyword variation rather than in aggregate. Also ranks top 3 for "mechanic" using only 3 mentions vs. 0 for all three competitors. Used "the backlink tool from Matt" after writing an article for a Texas-based automotive-industry site and is now surfaced as a recommended backlink source himself; visibility score reportedly rose from 17 to 22. Separately runs a sister towing company site that was unaffected by the recent Google update, while his auto-repair site was hit hard — businesses with fewer reviews and, per David, "no website" now outranking him — used as a live example of how a single core-update rollout can hit one niche/site in a portfolio while leaving another untouched.
- **Neri** — Clevant (live-audited site referenced verbally as "Clement.com"), a remote bookkeeping business physically based in St. Petersburg, FL but serving clients nationwide. Live homepage FAQ/Q&A structuring walkthrough; live canonical-URL trailing-slash fix; live title/meta-description period discrepancy resolved as a non-issue; final question on how to phrase a press release (recommended: target St. Petersburg specifically, mention Florida/nationwide service secondarily).
- **Jorg** — runs a print-on-demand store; asked how single-answer AI shopping results could ever work for visually-driven purchases like t-shirts. Denroy disclosed he has personally built and run multiple print-on-demand WordPress sites specifically to test AI Overview/LLM visibility (Gemini, ChatGPT, Anthropic models) and found ranking for broad product terms very difficult, with descriptive low-DA backlinks being the one lever that helped.

## Notable verbatim quotes

- "There's a few reasons that a site could be breaking. Actually, there are hundreds of reasons a site could be breaking."
- On seasonal product pages: "Google sees that and then lowers the importance of that page. And by the time it comes back up... it had traffic lost, it all became a 404. And then Google needs to recrawl it and refind it."
- On content length: "If we don't, the reason we don't want to go to 2000, 3000, is because we want to avoid over optimizing that page... we're not over optimizing and we're still beating them on that metric."
- On keyword insertion generally: "You just want to be slightly a bit ahead of whatever the top people are doing."
- On local keyword density: "Very common with, especially with local keywords, you don't need 10, 11, 12 keyword insertions. Sometimes just two or three is more than enough to get you to that top spot."
- On generic anchor text: "If the anchor text is just 'learn more,' 'click here.' That's generic anchor text. That's not helpful."
- On reselling brand products: "That brand is going to rank number one for their brand name. There is no way around that. You will never beat them, never gonna win."
- On zero-click / AI Overviews: "Google is prioritizing zero click search results, meaning they want to start moving people away from just showing you all the websites, all of the possible results and allowing you to make your own decision... instead they just want to tell you what the result is, what the best thing is, and just do the judgment themselves and just tell you the answer. That's what zero click essentially is."
- On what drives AI Overview citation: "Google really prefers high amount of presence across all different mediums and the quality of those mentions doesn't matter nearly as much."
- On Reddit as a citation lever: "Making your own subreddit and then having mentions of your brand — or you don't even need links to your site, you just need the mentions. And that has done wonders for every single case that we've seen of getting into AI overviews, getting more visibility."
- On chasing a nationwide ranking: "That's extremely difficult and would take years and thousands of dollars."
- On the pace of AI-search change: "Things are constantly changing almost by the day when it comes to this."
- On AI shopping's future: "The entire tech behind it is still so new, so many things are changing every single day with it."
- Closing note on the moment in SEO/AI search: "I think it's very, very adventurous time."

## Tradeoffs & nuance

- WP Rocket's speed settings (JS minify, deferred JS, lazy load) are a direct reliability/speed tradeoff — there's no universal safe configuration; hey Tony's own production site runs with lazy loading off entirely, and the recommendation is to test changes and involve a dev rather than apply a fixed rule.
- Word count and keyword density targets are explicitly relative to the current SERP, not fixed numbers — "it depends" is the repeated answer; the same keyword can need 2 mentions or 11 depending on what's currently ranking.
- Beating competitors by a wide keyword-density margin (David's case) isn't automatically better — closely matching/slightly exceeding is the goal; large overshoots read as over-optimized risk even without a stated formal penalty threshold.
- Tool-flagged issues aren't always real ranking problems: the canonical trailing-slash mismatch is a genuine fix, but the "St" vs. "St." period gap is explicitly framed as a non-issue for actual search results — only mattering for certain tools' (Semrush's) literal-string keyword-density counting.
- Conceding you'll never outrank a resold brand for its own name is presented as sound strategy, not failure — the win condition shifts to the discount/sale modifier instead.
- Broad-region content for AI visibility and narrow-city content for traditional local ranking are pursued **simultaneously**, not as either/or choices — go broad in mentions/press for AI citation while still concentrating the actual on-page optimization on the winnable specific city.
- AI Overview citation weighting (presence/volume over source domain authority) is a real departure from classic backlink-quality thinking, and Denroy frames it as something they're actively testing/"playing around with," not settled doctrine.
- Print-on-demand/broad e-commerce visibility in AI search is an open, unsolved problem by Denroy's own admission — his testing found it "very difficult," and his answer about future personalized single-answer results is explicit speculation, not a confirmed mechanism.
- A single Google core-update rollout can devastate one site in an operator's portfolio (David's auto-repair site) while leaving a closely related sister site (his towing company) untouched — impact is niche/vertical-specific, not a uniform global effect.
