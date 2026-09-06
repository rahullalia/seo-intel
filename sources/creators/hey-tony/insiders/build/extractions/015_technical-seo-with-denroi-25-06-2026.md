# Technical SEO with Denroi — 25.06.2026 (HeyTony Insiders Call #015)

Speakers: Denroy (technical SEO team lead, hey Tony, ~6 years) and Elliot (tech team, ~2 years, specializes in local business profile optimization). Live Q&A / site-audit call format.

## Tactics & step-by-step how-to

- **Fix "crawled but not indexed" / "discovered not indexed" GSC errors:**
  - Identify if site uses a front-end builder (Bakery, Elementor, Astra) — these generate their own dynamic/template page files that will never rank.
  - Confirm those dynamic/template pages are NOT listed in the sitemap.
  - Confirm sitemap is actually submitted in Google Search Console.
  - In GSC error lists, any URL with a `?` or `=` is a dynamic URL — ignore it, it wouldn't rank anyway ("pretend those aren't there").
  - To check true indexing status, search only the clean URL (strip trailing numbers/params) into the GSC search bar.
  - If not indexed, request indexing directly from GSC.
  - For blog posts stuck un-indexed: add internal links to them and make sure each is optimized around one singular keyword.

- **Content/blog strategy for a coaching/service business:**
  - Do NOT create a blog post for every YouTube video — redundant. Instead embed or link to the YouTube video from within blog posts.
  - Build blog content around answering audience questions (e.g., "how to deal with separation anxiety," "how to deal with relationship problems").
  - Use keyword/question-research tools to find those questions (see Tools section).
  - Always internally link blog answers to other site pages, and especially to service/conversion pages.
  - Create one category per core service/offering; each category becomes a "hub" page that lists/links every blog under that topic.
  - When topics overlap and categorization feels ambiguous, resolve it by the keyword that's literally in the blog post's title — that decides the category.
  - Build a hub page linking out to every service page; you don't have to build/launch all service pages at once — build them out over time.

- **Orphan pages:**
  - If an orphan-page warning applies to a page you want to rank, add internal links to it from elsewhere on the site.
  - If the page is only meant for conversions and is linked from outside the site (e.g., a YouTube video), it's fine to leave it as an intentional orphan — do nothing.

- **Cleaning up mass low-quality/AI blog content:**
  - Start by identifying what's most relevant to the business among indexed pages, and check performance.
  - Pages that are indexed AND relevant AND getting traffic → re-optimize or consolidate (e.g., merge content into a service page or a single blog page) rather than delete.
  - Pages that are indexed but low-traffic (including keyword-swapped duplicate/competitor pages) → draft/remove immediately, no need to preserve.
  - Recommended look-back window for this audit: 3 months (can extend to 6 months; use whatever represents "the most recent quarter").
  - Threshold for "low traffic" worth cutting: **less than 1% of the site's total impressions** in that look-back window (calibrate against your own site's typical per-page average, not an absolute number).
  - Rationale: irrelevant blog sprawl signals Google an unclear topical direction and "diminishes the authority you have in the specific field."

- **Service page vs. blog page (how to decide what to build):**
  - Service pages = the specific things the business sells/offers; where visitors find info and convert (example given: MRI scans, retina scans, lip injections).
  - Blog pages = supporting context/value content that answers a question about the service topic (example: "are lip injections safe for X").
  - Small business doesn't need many service pages (3–4 is fine) — just keep linking blogs to those few pages; blogs can also link to other blogs.

- **Site audit warning triage (hey Tony Site Audit Tool):**
  - Fix everything flagged **red/severe** first.
  - Yellow/warning-level items can be pushed to later — but treat these as must-fix soon: duplicate H1s, multiple H1 tags, missing meta description, missing title tag, title too short, duplicate meta descriptions.
  - Rule: every page you want ranked needs a title tag + a meta description + exactly one H1 (two H1s allowed only if you have separate mobile/desktop layouts).
  - Leaving title/meta blank tells Google to auto-generate an excerpt and signals the page isn't focused around a keyword — "don't push it as high."
  - Fix missing Open Graph (OG) metadata by installing an SEO plugin and enabling "OG data" in its settings (OG governs Facebook/social share previews).
  - On GoHighLevel: the platform auto-creates two blog pages by default; if you've only optimized one, remove the unused one (ask Matt or GHL support for exact steps — Denroy flagged GHL as the platform he's used least in 6 years).

- **Fixing GSC "Not Found (404)" report entries:**
  - After making redirects/fixes, click the **"Validate Changes"** button in GSC for that specific issue.
  - Typically resolves within about 3 months, but Google's removal from the issues list is not guaranteed on a fixed schedule.
  - For genuinely non-existent pages showing 404, just redirect them straight to the homepage.
  - A persisting GSC report entry after the real-world fix is not a penalty signal — it's a slow report, not a live problem.

- **Multilingual (EN/FR) SEO setup:**
  - It's fine if the French page's URL literally keeps the English slug text with "fr" inserted in the middle — Google treats it as a distinct French page as long as the on-page content is actually in French.
  - To optimize further: check GSC to see how the French URLs are currently ranking/how much traffic they get.
  - If a French URL is new/low-traffic, you can change it to be built around the French keyword — but ALWAYS create a redirect from the old URL to the new one when you do (Shopify has a checkbox for this at the bottom of the URL edit screen).
  - Before touching any French URL, check GSC first to confirm you're not changing one that's already ranking.

- **Meta descriptions at e-commerce/product-catalog scale:**
  - Every page/product needs a unique meta description — never duplicate one across the site.
  - Each product page should be optimized around one specific long-tail keyword (e.g., "18 karat gold engagement ring" vs. "14 karat gold engagement ring" vs. "24 karat engagement ring" — each karat variant is its own long-tail keyword).
  - At scale (e.g., 100 product designs), track keyword-to-page assignments in a spreadsheet so you don't lose track and accidentally duplicate.
  - Achieve variation by reordering emphasis (materials first vs. design name first, etc.) as long as no two are identical.

- **YouTube-to-blog content duplication:**
  - Never paste the YouTube transcript directly as the blog post.
  - You can reuse the same topic and even the same chapter/heading structure from a YouTube video, but the actual written content under those headings must differ.
  - Blog headings should still be chosen to optimize around one target keyword — what worked as a YouTube chapter heading may not be the right on-page heading.

- **Crawl depth on blog archives:**
  - Blog archive pagination (page 2, page 3, etc.) DOES count as a click away from the main menu — it adds to crawl depth.
  - Don't dump hundreds of blog posts onto a single archive/homepage.
  - Instead, expose blog **categories** (footer or a dedicated section) as hub pages — e.g., a "marketing" category page shows all 100 marketing posts directly, avoiding deep pagination.
  - A mega menu is also a good tool to surface pages that would otherwise sit 2–3 clicks deep.

- **Accordion/toggle content:** confirmed fine for indexing — no special handling needed.

- **Editing an auto-generated Yoast sitemap:**
  - With Yoast Premium: edit directly in the plugin's settings.
  - Without Premium: go into your web host's file manager → `public_html` → `wp-content` → `plugins` → the Yoast folder → find `sitemap.xml` → edit manually.
  - If it's not under the Yoast plugin folder, check the root of the server instead.

- **AI-era content format:** consider adding a ~100-word TL;DR summary at the top of blog posts for AI-crawler/LLM consumption.

## Rules / dos & don'ts

- Ignore any GSC URL containing `?` or `=` — these are dynamic/template URLs and will never rank.
- Sitemap must be submitted in GSC, and must exclude builder-generated dynamic/template pages.
- Every page meant to rank needs: title tag + meta description + exactly one H1 (two H1s allowed only for separate mobile/desktop layouts).
- Meta descriptions must be unique per page, no exceptions, even across near-identical product variants.
- Never have duplicate content anywhere on a site — this is called out explicitly as "the number one thing" to avoid.
- Fix red/severe audit issues before yellow/warning-level ones.
- Low-traffic cutoff for pruning AI/duplicate content: **under 1% of total site impressions** over a 3-month (up to 6-month) look-back.
- Indexing timeline: "three months is a safe bet in most cases" — varies with keyword difficulty, search volume, internal link count, and backlinks to that page.
- 404/redirect validation timeline: usually resolves in ~3 months after clicking Validate Changes, but not guaranteed on a fixed schedule.
- Don't create a blog post per YouTube video — embed/link instead of duplicating.
- Orphan pages: only fix (internally link) if you want the page to rank; leave orphaned if it's a conversion-only page fed by external traffic (e.g., YouTube) and not meant to rank.
- Generic/non-existent 404 pages should redirect straight to the homepage.
- Don't overbuild service pages — some businesses have 25 service offerings, but that's not the goal; 3–4 solid pages plus incremental buildout is fine.

## Tools, prompts & resources

- **hey Tony Site Audit Tool** — flags warnings/errors by severity (red = severe, yellow = warning): title tags, meta descriptions, duplicate H1s, missing OG metadata, etc.
- **Google Search Console** — URL Inspection for indexing status + "Request Indexing"; **Validate Changes** button to confirm fixes/redirects; per-page Impressions/Clicks data for the low-traffic threshold calc.
- **Keyword/question research tools recommended:** Semrush, Ahrefs, Matt's **"Quest Question Finder"** tool, Answer the Public.
  - Note: hey Tony is "trying to find ways to go around without needing" Semrush since it was bought out by Adobe — for people without a paid tool, Matt's tools + Answer the Public are the recommended fallback.
- **Link Juicer** (WordPress plugin) — used by a client's hired SEO freelancer to auto-interlink ~3000 pages to one another; flagged as part of a problematic setup.
- **SEO plugin (generic/Yoast-type)** — install, go to settings, enable OG data to auto-generate Open Graph metadata across all pages.
- **Yoast SEO** — sitemap.xml generation and (Premium) in-plugin editing; free-tier requires manual file edit via host file manager.
- **GoHighLevel** — auto-creates two blog pages by default; extra one should be removed once you've settled on the one you're optimizing.
- **Google Analytics** — used alongside GSC to establish site-wide traffic context for judging what counts as "low traffic" on a given page.
- **Shopify** — built-in checkbox on the URL-edit screen to auto-create a redirect when a page URL is changed.

## Case studies / examples / results

- **Carolina:** GSC showed 55 indexed pages vs. 300+ discovered/crawled-not-indexed; site built on Bakery Builder; 27 blog posts not being picked up despite being optimized (each around a different keyword); started proper SEO ~4 months ago post-Rank Week. Advised 3 months is a safe-bet resolution window.
- **Cali:** Master's in psychology; runs 1:1 sessions plus a "Relationship Clarity Program" (6-month hybrid group coaching); YouTube channel focused on toxic relationships; site on Kajabi. Matt had already told her not to duplicate YouTube content into blog posts. Advised to build category hub pages (e.g., relationship therapy, anxiety therapy, ADHD) with blogs feeding each, plus example service-page ideas like "narcissistic abuse recovery" and "help people get out of cults and recover from that." Also has intentional orphaned landing pages fed by YouTube traffic only, correctly left un-linked internally.
- **Sam:** owns an escape-room business (targeting keyword "escape room nyc"); a hired SEO freelancer produced roughly **3000 AI-generated blog posts**, of which at least **~1000 got indexed** (not ranked); duplicated one blog post ~5 times, swapping the focus keyword to competitor names each time; used the Link Juicer plugin to interlink all pages together. Original data pulled with a 12-month look-back showed a minimum of 6 clicks and roughly 800–2,000 impressions per page — reassessed against the recommended 3-month look-back + <1%-of-impressions rule. Site overall gets ~20,000 visits/month (mostly paid ads), with ~5,000 of those landing on money pages.
- **Michael:** healthcare business, brand new post-Rank Week, only has 3–4 core service pages so far. (Elliot's illustrative examples for service pages: MRI scans, retina scans, lip injections.)
- **Doug:** first blog just uploaded; ran the hey Tony Site Audit and cleared all red/severe issues, left with 44 warnings — missing OG metadata (11, corrected to 17), duplicate H1s, missing meta description, missing/short title tags, duplicate meta descriptions. Site built on GoHighLevel, which auto-created two blog pages (only one optimized).
- **Jorg:** 62 pages showing 404 in GSC despite being redirected roughly 1–2 months prior; had not clicked Validate Changes for that specific issue.
- **Kate (Montreal):** jewelry/engagement-ring e-commerce on Shopify; AI auto-translation created French pages whose URLs still contain the English slug text with "fr" inserted mid-URL, which looked like duplicate-content flags in the audit but isn't actually a problem since content is in French. Site is under 1 year old; French section live since Christmas (~6 months); currently ~300 hits/month, very low visibility, largely untouched since initial setup. Long-tail keyword examples used: 18-karat / 14-karat / 24-karat gold engagement rings.
- **Martin:** newbie post-Rank Week; asked about crawl depth on paginated blog archives, mega menus, accordion/toggle indexing, editing a Yoast sitemap manually, and 100-word AI TL;DR summaries. Denroy confirmed accordion/toggle menus have been used "on over 100 sites" and "they all rank." TL;DR summaries have been tested on some clients and "some of the hey Tony blogs" with mixed-but-leaning-positive results.

## Notable verbatim quotes

- "Those pages would never rank anyways." — on builder-generated dynamic/template pages.
- "Anything with those numbers at the end wouldn't rank. So pretend those aren't there." — on dynamic URL parameters in GSC.
- "Three months is a safe bet in most cases." — on indexing timelines.
- "Don't make blogs going over the same content as your YouTube content. That's redundant."
- "It kind of diminishes the authority you have in the specific field that you have." (Elliot) — on irrelevant blog sprawl.
- "It would really just be less than 1% of total impressions. Would be the best rule of thumb to go to, to remove those." (Elliot)
- Missing title/meta description "just tells Google that page its content isn't as important. It's not focused around a keyword. Don't push it as high."
- "You have to do an Excel sheet... Otherwise you're going to get screwed because you will not remember all the keywords." — Jorg, advising Kate on tracking per-product meta descriptions.
- "You just want to make sure that you never have duplicate content on your site. That's the number one thing."
- "I've used accordion toggle menus on over 100 sites now. They all rank."
- "It seems to be a bit of a mixed bag, leaning more towards good than bad. And even in the case of neutral, it's still better to do if it's something that your competitors are not doing." — on TL;DR summaries.

## Tradeoffs & nuance

- Indexing timelines have no universal number — keyword difficulty, search volume, internal link count, and backlinks to the specific page all move the estimate; ~3 months is a rough safe floor, not a guarantee.
- GSC issue-list entries (e.g., 404s) can visually persist long after the underlying problem is actually fixed; Google's report-refresh cadence is slow and not fully controllable — a lingering entry is not itself evidence of an unresolved problem or a penalty.
- Large-scale low-quality content cleanup isn't one-size-fits-all: indexed + traffic-getting pages deserve re-optimization/consolidation, while indexed-but-low-traffic pages (even if relevant) are safe to cut immediately. Don't blanket-delete without checking traffic first.
- Bilingual URL structure is "good enough, not ideal": Google can correctly treat an English-slug-plus-"fr" URL as a distinct French page based on on-page language, so it's not urgent to fix — but if a page isn't ranking well, changing the URL to the French keyword (with a redirect) can help. Never touch the URL of an already-ranking translated page casually.
- Accordion/toggle content is fine today, but the caution in older SEO advice wasn't baseless — it reflected an earlier Google visual-crawl-only behavior; Google now also does raw HTML crawls and agentic AI crawling (bots clicking menus, filling mock forms, interacting with page elements), which is why the old guidance is now outdated.
- Blog pagination isn't forbidden outright, but for large archives (hundreds of posts) routing through category hub pages is better than raising crawl depth via numbered pagination.
- TL;DR summaries for AI consumption: explicitly "mixed" results — sometimes good, sometimes neutral, rarely bad — so it's a low-risk, not-guaranteed-upside tactic; more compelling specifically as a competitive differentiator when rivals aren't doing it.
- Service page count is a "just enough" game, not a maximization game — some businesses run 25 service pages, but going that broad isn't a stated goal; better to nail 3–4 and expand deliberately over time so the site doesn't overwhelm visitors.
- Team is actively moving away from Semrush post-Adobe-acquisition but hasn't found a full replacement yet — recommends Matt's internal tools + Answer the Public as accessible substitutes when a paid tool isn't available.
