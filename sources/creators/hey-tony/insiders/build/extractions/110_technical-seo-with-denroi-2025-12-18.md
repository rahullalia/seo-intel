# Technical SEO with Denroy — 18.12.2025 (Call #110)

Format: live Q&A, raise-hand queue, live screen-share audits/walkthroughs, no set lesson plan. Denroy = technical SEO team lead at Hey Tony, ~5.5 years working with Matt (since before Matt's Instagram/social media even started); has worked across SEO, web design, Google Ads, and web dev. Calls run every two weeks; replays post within ~2 days. Attendance climbed to ~40 during this call — Denroy says it's the largest he's ever run (normally 5–10 people).

## Tactics & step-by-step how-to

- **Domain/rebrand migration:** 301-redirect every old URL to its exact new-URL equivalent — not just homepage-to-homepage (e.g. `/seo-services` on the old domain → `/seo-services` on the new one). Keep a list of every previous URL first. Anything that doesn't map 1:1 to a new page, redirect to the new homepage instead. Immediately after cutover, confirm Search Console and Analytics tracking are set up on the new domain.
- **Diagnosing a canonical-page error flagged by an audit tool (WordPress + Yoast + Elementor):** open the flagged URL and check for a "?" or "=" near the end instead of a clean "/" — that marks it as a dynamic URL (e.g. an inventory/search-results page), which is the real cause of the canonical mismatch, not a genuine site defect.
- **Elementor template pages:** if "Edit with Elementor" opens a shared template rather than a unique per-page layout, you can't fix the canonical tag on just one URL — editing the template changes behavior for every page built on it.
- **Fixing a dynamic search/inventory page's canonical issue:** build a static page (URL without the "?"/"=" parameters), shortcode in the same search-results field/content, and separately exclude the dynamic URL pattern in robots.txt so crawlers/audit tools stop flagging it.
- **Checking if a URL is indexed:** paste the exact URL into the Google Search Console top search bar. Green = indexed. Gray = not indexed. Red = there's a problem.
- **"Crawled – currently not indexed" (GSC):** if it's a page you actually want ranking, add more on-page content and build more internal links to it (more internal links = Google reads the page as more important). If it's a page you don't care about (e.g. leftover default/sample blog posts), just delete it.
- **"Alternate page with proper canonical tag" (GSC):** check if the flagged URLs are dynamic (contain "?"/"="). If so, safe to ignore — canonical is correctly pointing at the clean URL ending at the last "/".
- **Priority order for a site/multiple sites with no SEO work done yet:** (1) get tracking installed and verified first — Google Site Kit / Search Console / Analytics — so there's data to optimize against; (2) then do keyword research inside Search Console: what's ranking, what's trending, what opportunities exist; (3) if a page is trending up but has few internal links pointing to it, write more blog content and add internal links to it.
- **One keyword per page** you're deliberately trying to rank for — don't spread a single target keyword's intent across multiple pages.
- **Small brand/property sites that don't need every subpage to rank** (e.g. a single vacation-rental listing with 5 pages): consolidate ranking effort onto the homepage; build extra blog/content pages to earn long-tail keyword authority feeding the homepage, rather than trying to rank each subpage individually.
- **Merging near-duplicate blog posts targeting the same intent:** pull Search Console data for each post. If one clearly and meaningfully outperforms the others, migrate the useful content from the underperformers into the winner, then 301-redirect the losers to it. If all posts perform similarly (or all perform poorly, even if one technically ranks), combine all the content into one post and re-optimize for a single keyword.
- **Tag pages:** treat as effectively unsalvageable — don't use them at all; rely on categories instead.
- **URLs:** strip out any embedded year (e.g. `/2025/`) — it becomes stale/less relevant as time passes.
- **Diagnosing "Page with redirect" in GSC:** Indexing tab → Pages → click the gray ("why pages aren't indexed") segment → find "Page with redirect" → click through to see the actual list of flagged URLs.
- **Confirming a "Page with redirect" flag is a non-issue:** if the flagged URL variants (e.g. non-SSL version, `www` version, `www` + non-SSL version) are all correctly redirecting to the one canonical secure non-`www` URL, there's nothing to fix — GSC is just reporting that it saw those URL variants somewhere (sitemap, robots.txt, an llm.txt-style file, or CMS config), not flagging a real defect.
- **CMS auto-generated `/home` slug** (site builders that force the homepage's page title to "home," e.g. Coach D's platform): 301-redirect `/home` to the root domain, and additionally set the original `/home` page to draft/not-public inside the CMS to further minimize the chance a crawler indexes it as a duplicate.
- **Diagnosing conflicting H1 reports** (a page-audit Chrome extension says fine/has an H1, but the full site audit tool says missing/multiple H1s): treat as a caching problem, not a real conflict. Expect **at least a 12-hour delay** before the audit tool re-crawls a page and reflects a fix, even after manually hitting "new crawl" — caching can also sit on the extension side or the site's own cache.
- **Fixing empty/duplicate H1s on Shopify:** Online Store → Customize (or Open Theme Editor) → locate the `theme.liquid` file → Ctrl+F / Cmd+F → search `page.title` (or "H1") → look for an empty `<h1></h1>`, an H1 wrapping the logo, or extra H1s injected by popups/plugins (e.g. a promo banner). If empty, insert the actual target keyword/title text as the H1.
- **Rule of thumb applied to nearly all sites:** exactly one H1 per page, and it should be the very first heading element on the page.
- **H2 usage / how many to use:** pull up the page currently ranking #1 for your target keyword, count its H2s, and use a similar number — a little more is fine (example given: if the top page has 5 H2s, go for 7–8). Don't wildly overshoot the top-ranker's count (example: top page has ~50 H2s, going to 200 would be over-optimizing). In practice, 5–10 H2s on a normal article is "totally fine."
- **Locale-duplicate content** (e.g. Shopify `EN-CA` vs. default English pages mirrored across the whole catalog): pull Search Console to see which locale variant is actually ranking. For blog content, redirect the lower-performing duplicate to the higher-ranking one. For product pages, don't force a redirect without a prompt/switcher — let the visitor confirm. Check installed Shopify apps for a geolocation/geo-redirect app (Shopify doesn't fork locale URLs like this by default) and review its settings; treatment is case-by-case.
- **Keyword-to-content workflow:** find the keyword (via "what are people asking"–style research plus a keyword-volume tool), put the primary keyword in the H1, then check what currently ranks #1 for it and mirror/slightly exceed their H2 depth.
- **Submitting a sitemap in GSC:** Search Console → Indexing (left nav) → Sitemaps. If nothing appears under "Submitted sitemaps," none has been submitted yet. In 99% of cases the path is just `sitemap.xml` (occasionally `sitemap_index.xml` or a platform-specific variant). Test it first by pasting `yourhomepage.com/sitemap.xml` directly into a browser to confirm it loads; only then paste that same URL into GSC's "Add sitemap" field. If the status shows "Error" immediately after submitting, refresh the page — it can flip to "Success" without changing anything.
- **Sitemap is a hard crawl dependency:** if the audit tool (or Google, somewhat more resilient) can't find the sitemap, it can't crawl the site — always confirm the sitemap is present, linked/submitted in Search Console, and hasn't been accidentally deleted.

## Rules / dos & don'ts (keep every threshold, number, specific)

- Redirect every old URL to its exact new-URL equivalent on a rebrand/domain change — never just homepage-to-homepage.
- Anything without a clean 1:1 mapping on migration: redirect to the new homepage.
- A URL ending in "?" or "=" instead of "/" = dynamic URL; treat differently from static pages for canonical/indexing purposes.
- Dynamic/search-result pages with no static content (no paragraphs, text blocks, FAQs) are inherently harder to rank — the content keeps changing.
- Editing a shared Elementor template changes canonical/heading behavior for every page built on that template, not just one.
- GSC URL-inspection colors: green = indexed, gray = not indexed, red = a real problem.
- Delete pages you don't want ranking (e.g. leftover default/sample blog posts) rather than trying to fix a "crawled, not indexed" status on them.
- "Alternate page with proper canonical tag" on dynamic (?/=) URLs: safe to ignore.
- Tracking setup (Site Kit / GSC / Analytics) is the #1 priority before any other optimization work — you need data to optimize against.
- One keyword per page.
- Google does **not** penalize redirecting many old blog posts into one consolidated post.
- Google **does** penalize redirect loops (a chain that bounces and never resolves to a live page).
- Avoid putting a year in a URL.
- Never use tag pages — use categories instead ("they tend to be dead pages," largely duplicate content, no unique value).
- Don't auto-redirect visitors on locale/geo duplicates without a prompt, at least for product/transactional pages.
- Exactly one H1 tag per page, and it must be the first heading on the page — a general rule applied to pretty much all sites.
- H2 count: no fixed number, but don't drastically overshoot the current top-ranking competitor's heading count (example ratio: ~50 vs. 200 = "way over optimizing"); 5–10 H2s is "totally fine" for a typical post.
- A missing/deleted sitemap can crater traffic — cited case: a client's traffic dropped from "hundreds of thousands" to zero after their sitemap was deleted.
- Google Search Console and a Google Business Profile are "completely" different products — don't conflate them.
- Sitemap URL convention: try `/sitemap.xml` first (works in 99% of cases).
- Audit-tool re-crawl caching: allow **at least 12 hours** before trusting new results after a fix.

## Tools, prompts & resources (exact prompt wording if quoted; tool names; settings)

- **Hey Tony Site Audit Tool** — the group's proprietary crawler/checker referenced throughout; known caching lag (12+ hours before re-crawl reflects a fix, even after manually triggering a new crawl).
- **Google Search Console** — used constantly: URL Inspection bar (paste URL → green/gray/red status); Indexing → Pages report (errors like "Crawled – currently not indexed," "Alternate page with proper canonical tag," "Page with redirect"); Indexing → Sitemaps (submit/check sitemap status).
- **Yoast SEO** (WordPress plugin) — the tool surfacing the canonical page error MJ was troubleshooting.
- **Elementor** — page builder on MJ's site; "Edit with Elementor" button; template vs. per-page editing distinction is what determines whether a canonical fix is possible.
- **robots.txt** — recommended location to exclude dynamic/search-parameter URLs from crawling.
- **Google Site Kit** (WordPress plugin) — bundles Search Console + Analytics; sends automated canonical-error emails (referenced by Marlo).
- **Shopify theme editor** — Online Store → Customize / Open Theme Editor → `theme.liquid` file; search via Ctrl+F/Cmd+F for `page.title` or "H1."
- **Simvali** (per transcript — likely the "Simvoly" site builder) — the non-WordPress CMS Coach D used; auto-names the homepage's page title "home," producing a `/home` URL that needs a 301 redirect plus draft/unpublish of the original.
- **Go High Level (GHL)** — Dr. Karen's site builder; sitemap isn't automatically surfaced/visible and has to be located and exposed for crawling.
- **AnswerThePublic** ("ask the public") — for finding what people are searching/asking, to shape blog topics and headings.
- **SEMrush** — mentioned by Dr. Karen as out of her price range.
- **Ubersuggest** — the keyword tool Dr. Karen uses instead of SEMrush.
- **ChatGPT** — Dr. Karen mentioned consulting it to try to find where her GHL sitemap lives (didn't fully resolve it on the call).
- Sitemap URL pattern to test/submit: `yourdomain.com/sitemap.xml` (fallback `sitemap_index.xml` or a CMS-specific variant).

## Case studies / examples / results (names, niches, numbers)

- **MJ** — auto-finance/ATV dealer site ("Autoby Finance CA"); dynamic inventory-search pages (template-driven via Elementor) triggering canonical errors. After fixing other audit-tool errors: site audit score went from **63 to 86**; reports rising impressions, clicks, and visitor traffic.
- **Marlo** — runs multiple websites, including a vacation-rental listing site for a property called **"Casaluna Azul"** in Isla Mujeres, Mexico (5 pages on that site). Decision: focus ranking effort on the homepage rather than every page, build long-tail-keyword content around it — long-tail keyword floated: **"four bedroom beachfront vacation rental"** (contingent on her own keyword research confirming demand). Also asked about "crawled, not indexed" pages (turned out to be irrelevant leftover sample blog posts — recommended deletion) and an "alternate page with proper canonical tag" error (confirmed as dynamic-URL noise, safe to ignore).
- **Thomas** (Albania) — SEO agency site in a non-English language; had 3 overlapping posts plus a tag page all clustered around "what is SEO"-type intent, including one with "2025" in the URL that was a translated duplicate of another. Best of the three ranks at **position #9** but isn't capturing much traffic relative to the other two. Since none clearly dominates, recommendation was to combine all three into one post and re-optimize for a single keyword, drop the year from the URL, and eliminate the tag page — while keeping a separate "AI and SEO" post as its own topic since it targets a different keyword intent.
- **Coach D** — new to SEO/Search Console; site **ladyjunkcarbuyer.com** (junk-car-buying business). GSC "Page with redirect" report showed 3 URL variants (no-SSL, `www`, `www` + no-SSL) all correctly redirecting to the canonical `https://` non-`www` URL — confirmed as a non-issue, nothing to fix. Also confirmed her `/home` → root 301 redirect was done correctly (CMS auto-named the homepage "home").
- **Monique** — Shopify store selling bee venom skincare (copy referenced: "The Best Bee Venom Distilled in Nature's Lab," "Best Bee Venom Skincare," a "25% off your first order" popup). Site audit score rose from **42% to 92%** after fixes, but organic performance then dipped — diagnosed as an audit-tool/extension caching lag rather than a real regression. Live diagnosis found a genuinely empty H1 on the homepage plus multiple stray H1s from theme/popup elements, to be fixed inside `theme.liquid`.
- **Andrea** — Shopify store with `EN-CA` vs. default-English locale-duplicated URLs across every page/product; most likely caused by a geolocation app rather than native Shopify behavior (Shopify doesn't do this by default). Resolution deferred to reviewing her actual plugin screenshots — flagged as case-by-case.
- **Dr. Karen** — new to SEO via Rank Week; GHL-built site where the original developer had marked every heading as an H1 (called "very common with developers") — she'd already gone through and corrected it herself. Confirmed her instinct of 5–10 H2s per page as "totally fine." Also working through exposing her sitemap in GHL so it can be crawled.
- **General cited pattern** (unnamed client): a site whose sitemap was deleted saw traffic "drop from hundreds of thousands to zero."
- **Call scale:** attendance climbed from ~30 to 37 to ~40 people during the session — Denroy's largest call ever (normally 5–10 people). Cadence: every two weeks. Replays post within ~2 days.

## Notable verbatim quotes

- "Anytime you see a question mark or an equal sign at the end of a URL instead of that slash, this is more of a dynamic URL."
- "Dynamic pages like this typically have a harder time ranking because the content is constantly changing depending on what is there."
- "The more internal links you build to a page, the more Google will understand this page is important."
- "Basically you want to go one keyword per page that you want to optimize for."
- On redirects: "Google will penalize if you... make a redirect loop that just bounces things back and never loads a page... But just redirecting traffic to a more important page will not [penalize you]."
- On tag pages: "They tend to be dead pages. A lot of the time it's duplicate content from the blog post that it's referring to or the blog post it's linking to, and there's no unique content on tag pages... most times we opt to never even use tag pages. Instead just use categories."
- "Some errors you will see in the page indexing tab in Search Console are not actual errors. It's just Google saying this cannot rank because XYZ reason."
- "There will always be some issues in Search Console that aren't really issues. It's just things Google picks up on their end."
- "If the audit tool can't find your site map, it can't crawl your site... we've had cases where we've had clients deleting sitemaps in the past that we've created and all of a sudden their traffic just drops from hundreds of thousands to zero."
- "One heading, one tag per page. And that should be the very first heading."
- On H2 over-optimization: "If the current rank one has 50 [heading twos] and then you're going for 200, that'd be way over optimizing."
- "Whoever created my website made every heading an H1 tag. Very common with developers."
- "This is the biggest call I've ever had... I've never had 40 people on any of my calls before. I run these calls every two weeks."

## Tradeoffs & nuance

- A canonical/indexing "error" flagged by an audit tool isn't automatically a real problem — dynamic search-parameter URLs, correctly-redirecting protocol/subdomain variants, etc. routinely show up as "errors" that need no action. The skill is distinguishing genuine defects from Search Console/audit-tool noise.
- Fixing a template-level canonical issue on a dynamic page isn't always possible without affecting every other page on that template — sometimes the practical fix is a net-new static page rather than patching the dynamic one directly.
- Consolidating overlapping blog content is intent-dependent, not purely traffic-dependent: two posts can both be "about SEO" and legitimately stay separate if they serve different keyword intents (e.g. "AI and SEO" vs. "are SEO services worth it"). Only true near-duplicates targeting the same intent should be merged/redirected — and even then, the decision branches on whether one post is clearly winning (migrate + redirect) vs. all performing similarly/poorly (combine into one and re-optimize).
- Locale/geo URL duplication has no one-size-fits-all fix — Shopify itself doesn't create `EN-CA`-style duplicates by default, so the real fix lives in whatever third-party geolocation app is installed, and the right behavior differs for blog content (safe to hard-redirect to the winner) vs. product pages (should prompt rather than silently redirect).
- Apparent ranking/traffic regressions right after implementing fixes may not reflect the fixes at all — both the audit tool and browser extensions cache aggressively (12+ hour lag cited), so "did this fix work" often can't be judged same-day.
- H1/H2 guidance is deliberately a heuristic, not a hard rule: match roughly what the current top-ranking page for your keyword is doing (a little more, not drastically more), rather than applying a universal fixed count.
- Redirecting is the same underlying tool used both safely (consolidating old blog content, once-per-migration URL mapping) and harmfully (redirect loops) — the risk is in implementation/sequencing, not in the tactic of redirecting itself.
