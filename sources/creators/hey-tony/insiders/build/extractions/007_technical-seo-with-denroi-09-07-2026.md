# Technical SEO with Denroy — 09.07.2026 (Call #007)

Format: live Q&A, raise-hand queue, live screen-share audits. Denroy = technical SEO team lead at Hey Tony, ~6 years working with Matt. Calls run every 2 weeks; other weeks covered by other Hey Tony team members. ~45 attendees on this call (unusually high, credited to recent Rank Week).

## Tactics & step-by-step how-to

- **WebP conversion cleanup (Squarespace/any site):** after converting images to WebP and re-uploading, the old PNG/JPEG files stay on the server and keep dragging speed down. Manually delete the old PNG/JPEG originals after confirming the WebP replacements are live — don't just "replace" via a tool, physically remove the legacy files.
- **Diagnosing a bloated image:** inspect any image element in dev tools, check its file extension (PNG vs WebP) and hover to see file size. A 5.4MB PNG converted to WebP was estimated to drop to ~300KB (under 10% of original size).
- **PHP + server-level speed fixes (WordPress, cPanel access):**
  1. Update PHP version to 8.2 or higher.
  2. Before upgrading, verify all plugins are compatible with that PHP version (so you know what to roll back to if something breaks).
  3. In cPanel's PHP section, enable OPcache, Redis, and Memcached.
  4. Re-test site speed after each change.
- **Shopify speed checklist — check these four before doing anything else:**
  1. CDN set up.
  2. Images served as WebP.
  3. Image lazy loading enabled.
  4. CSS/JS deferred (non-critical).
  If all four are in place, "site speed overall should be very, very good."
- **Audit tool showing stale results after a fix:** re-crawls can take 5–12 hours to reflect changes (or may still be finishing in the background). Wait that window before assuming a fix failed; cross-check with the Detailed SEO extension or the Hey Tony Chrome extension if still wrong after that.
- **Yoast overriding page-builder meta descriptions:** if Yoast is set to pull an excerpt from page content, it silently overrides whatever meta description you set in Elementor (or any builder). Fix: open Yoast's own meta description box on that page and set it there directly — this is what search engines/crawlers actually read, separate from the front-end content the user sees. Must be repeated per page (no bulk fix shown).
- **Squarespace title auto-appending business name:** if a page title looks correct in Squarespace's SEO settings (e.g. 41 characters) but the business name still gets appended in previews/audit tools, look for a "dynamic text" option inside the title tag's HTML/theme code and remove the auto-population there. Framed as optional — Google typically strips the appended name in actual search results anyway, so it's just an audit-tool warning, not a real ranking issue.
- **FAQ vs. blog post decision rule:** ask — can the question be answered in one paragraph, or does it need more information/visuals/longer-form treatment that the user would benefit from? Yes → turn it into a blog post. No (simple answer) → keep it as an FAQ on the homepage, service page, or contact page.
- **Adding hand-coded/React pages to a hybrid site's sitemap:** take the full URL of every React (or otherwise hand-coded) page, manually add each to the site's `sitemap.xml` (append `/sitemap.xml` to the root domain to view it), confirm every publicly-indexable page is listed, then submit the sitemap to Google (Search Console).
- **Diagnosing "discovered — currently not indexed" pages (GSC):** in order —
  1. Check internal links to those pages — confirm they aren't orphaned.
  2. Check keyword competition level the page targets — high competition can stall indexing/ranking priority.
  3. In GSC, paste the URL into the top search/inspect bar to see if Google has it indexed; if the gray "not indexed" box appears, click Request Indexing.
  4. Check the XML sitemap itself — confirm the specific pages are actually listed; sitemap updates can lag behind publish or skip new posts depending on the plugin/generation method.
- **Keyword density / "how many times should I use my keyword":** no fixed number. Check what top-ranking competitors do — if they use it once, use it twice; if they use it 20 times, use it 21ish. Don't go far beyond competitors (e.g., 20 extra uses) — that reads as over-optimization to Google rather than genuine helpfulness.
- **Duplicate H1 tags on one page (e.g., Shopify + page-builder auto-generating a second H1):**
  1. Check Search Console to see which of the two headings' keyword variant is already ranking higher.
  2. Keep that one as the true H1 (usually the shorter/more abbreviated version).
  3. Do NOT delete the other text/content — instead demote its tag. In Shopify, edit the theme's `product.liquid` file and change the second `<h1>` to `<h2>` or plain text. (Low-volume alternative: manually edit each product page if the catalog is small.)
- **Canonical/permalink mismatch (renamed WP taxonomy, e.g. "Portfolio" renamed to "Work"):**
  1. Symptom: some pages resolve under the new slug, others under the old one; canonical tag points to a URL that 404s.
  2. Confirm via an SEO inspector (Detailed SEO / Hey Tony extension) that "canonical tag does not match sitemap."
  3. Fix per page: WordPress → Yoast → scroll to the **Advanced** tab → **Canonical URL** field → paste the correct URL → publish.
  4. If the issue persists on one specific page after that (others fixed fine), suspect caching, a theme setting silently overriding it (e.g. a theme's own "rename Portfolio" option), or duplicate logic. Next step: Appearance → Theme File Editor → open `functions.php` (or whatever the theme calls its equivalent) and find/edit whatever code is generating the canonical tag directly. Don't attempt this fix through permalink structure settings.
- **Ranking for an ultra-competitive head keyword with a new/low-authority site (e.g. "Toronto wedding photographer"):**
  1. Fix heading hierarchy first if headings appear out of order (H2s before H1).
  2. Do NOT chase the broad city-wide term. Narrow to specific neighborhoods/sub-areas (example given: Richmond, Mississauga, Hamilton, or "Toronto and GTA").
  3. Use a keyword tool (SEMrush, Ahrefs) to find modifiers with low competition but sufficient search volume.
  4. Build out content and blog posts targeting those narrower local terms first.
  5. Build backlinks/authority over time; only go after the harder, broader keyword once that authority exists.
- **New/thin site with no confirmed target keyword (e.g. niche product using unfamiliar terminology):** do keyword research to find the best modifier/variant with real search volume before committing a homepage H1 to it. When you can't use the exact "made up"/branded term in a heading, still ensure the surrounding body copy includes the actual keyword variant you want to rank for.
- **Turning jargon into rankable content:** if your product/service relies on terms customers don't search for by name (e.g. a proprietary process name), write blog content that explains what the related, more-searched terms mean (e.g. clean living, Ayurveda) rather than forcing the jargon term into headings.
- **New-site content cadence:** publish at least 2 blog posts per month to build backlinks, topical authority, and traffic.
- **Multi-service site architecture:** the single service that makes the most revenue becomes the homepage's target keyword/topic. Every other service gets its own dedicated page. Rule of thumb: **one keyword per page**, applied site-wide.
- **Video hosting:** never self-host video files on your own web server — always embed via YouTube, Vimeo, or similar. Applies even to a low-traffic dev/pre-launch site.
- **Booking/CTA flow:** it's fine for a call-to-action button to leave the current site/domain entirely and land on a separate booking or landing page — no SEO penalty for that.

## Rules / dos & don'ts (keep every threshold, number, specific)

- Delete old PNG/JPEG files after converting to WebP — don't leave them on the server "just in case."
- PHP version target: **8.2 or higher**. Confirm plugin compatibility first.
- Enable in cPanel: **OPcache, Redis, Memcached**.
- Recommended image-conversion plugin: **WebP Converter for Media** (preferred over **Imagify**, which Denroy called "a little bit too heavy").
- Audit-tool re-crawl caching: allow **5 to 12 hours** before trusting new results.
- H1 rule: only **one H1 per page**. H2 can be used **as many times as needed**, including back-to-back with no text between.
- Heading styling doesn't matter for SEO — **not** required that H1 be the visually largest text. Only two things matter: (1) the text must be visible/readable, not hidden, and (2) headings must appear in the correct sequential order (H1 first, then H2s, etc.).
- Keywords are weighted **heavier in heading tags** than in regular paragraph copy — always work the target keyword (or a variation, or a local modifier) into headings; avoid generic non-descriptive headings like "Learn More."
- Keyword prominence rule: the **sooner** a keyword appears in the title tag, meta description, and body content, the more weight Google/crawlers assign it.
- Keyword repetition: match competitors' usage count, don't wildly exceed it — over-optimizing (e.g., stuffing 20 extra instances beyond top competitors) reads to Google as manipulation, not helpfulness.
- "You may also like"/related-product blocks **do count** as internal links.
- Never self-host your own videos — no exceptions worth taking, "even" with a strong dedicated server "YouTube is just better."
- Never external-link to a direct competitor, for any reason (e.g., don't link out to a rival local business in your own market). Linking to a separate, non-competitor landing page (e.g. your own booking page) is fine.
- One keyword per page, site-wide, as the general architecture guideline.
- Squarespace/theme quirks aside, if Google already strips an auto-appended business name from titles in actual SERPs, treat the audit-tool warning as informational, not a hard fix requirement.
- Google has been penalizing pages with excessive white space/blank content sections in the last year or so — noted as a recent enforcement shift ("as recently as last year").
- Medical/health-niche sites: Google treats this vertical "a little bit differently" from other site types — reinforces the need for explicit keyword+location matching in headings.

## Tools, prompts & resources (exact prompt wording if quoted; tool names; settings)

- **Hey Tony Site Audit Tool** (aka "Rank Report Card" inside Insiders, dark-mode page) — the main crawler/audit tool referenced throughout; has a known caching bug on recent recrawls.
- **Detailed SEO** — Chrome extension used repeatedly on-screen to inspect live meta tags, canonical tags, and headings.
- **Hey Tony Chrome extension** — secondary verification tool for meta/canonical checks.
- **GTmetrix** and **PageSpeed Insights** — mentioned as speed-testing tools attendees had already tried.
- **WP Rocket** — caching plugin already in use on Anthony's Divi site.
- **WebP Converter for Media** — Denroy's recommended WebP conversion plugin.
- **Imagify** — alternative WebP plugin, called serviceable but "too heavy."
- **Yoast SEO** — used for meta description overrides and canonical URL field (Advanced tab).
- **Google Search Console** — used for: checking indexing status via URL inspection ("paste your URL in there, hit search"), Request Indexing action, and comparing which heading/keyword variant is ranking higher when two exist on one page.
- **SEMrush** and **Ahrefs** — recommended for keyword research to find low-competition, sufficient-volume modifiers.
- **WordPress Theme File Editor** (Appearance → Theme File Editor → `functions.php` or theme equivalent) — used to locate and edit code generating an incorrect canonical tag.
- **Shopify `product.liquid` file** — edited directly to demote a duplicate H1 to H2/plain text at the theme-code level.
- Sitemap check technique: append `/sitemap.xml` to any root domain to view the full indexed-page list.

## Case studies / examples / results (names, niches, numbers)

- **Mary** — Squarespace site, converted every image to WebP; speed still bad. Live test result: **54 mobile / 81 desktop**. Root cause: old PNG/JPEG files still sitting on the server.
- **Anthony** — WordPress + Divi, CDN + WP Rocket already active. Found a **5.4MB PNG** still being served (not yet converted); estimated post-WebP size **~300KB** (under 10% of original).
- **David** — archangelcommunications.com (PR firm). Meta title/description appeared missing/wrong due to (a) audit caching and (b) Yoast silently overriding Elementor's meta description via excerpt pull.
- **Steph** — Squarespace mental-health/therapy site. Title tag 41 characters in settings but business name auto-appended in preview. Heading audit: **1 H1, 8 H2, 5 H3, 7 H4** — confirmed as correct hierarchy ("what you've done is perfect"). Discussed reworking a generic H2 ("often") into something more keyword-supportive; also discussed FAQ vs. blog decision for an anxiety-therapy FAQ section.
- **Todd** — voicedragons.com. Hybrid site: Squarespace front end + hand-coded/React back end (e.g. "Find a Voice" page). React pages were entirely missing from the Squarespace sitemap.
- **Cynthia** — Rank Week alum, site health score **95–96**. GSC: **33 pages indexed, 17 not indexed**, of which **7 are "discovered — currently not indexed"** (6 of those are blog posts, not particularly new). Confirmed strong internal linking already in place; competition level of target keywords flagged as the likely next thing to check.
- **Joanne (Joan)** — Shopify store. Asked whether "keyword cluster six times in product description" is still the right density rule (answer: no fixed number, match/slightly beat competitors). Also confirmed heading-order/styling rules.
- **Kate** — Shopify + GemPages, goldsmith/jewelry business (example product: "vintage engagement ring, 18 karat"). ~50 products. Duplicate H1 issue on product pages caused by GemPages injecting the collection-page product title as an H1 alongside a separately authored H1 in the product description.
- **Emphasize** — WordPress site on the Calium theme, graphic-design portfolio. Site health **98**, score **~97**. Renamed built-in "Portfolio" section to "Work"; canonical tag on the main `/work` page still pointed to the now-404ing `/portfolio`, while sub-pages under `/work` were fine. Also has a front-loaded video causing a first-content-download bottleneck.
- **Fredo / Prito** — Showit website, Toronto wedding photographer, site ~1 year old (published end of prior year), effectively zero backlinks. Target keyword "Toronto wedding photographer" not appearing in results checked through 40 pages / incognito; getting impressions but zero clicks per GSC. Diagnosed: heading order wrong (H2s before H1), plus keyword far too competitive for site's age/authority. Blog examples cited as also too competitive: "Golden Hour," "Wedding photography." Images served as `.jpg`, loaded in background — recommended WebP conversion.
- **Ellie** — "Healing Textiles" (UK), Ayurveda-infused organic-cotton yoga rugs ("Ayavastra"/"Aya Vastra"), Shopify, site ~3 months old. Did Rank Week, then went dormant. Empty H1 tag found on homepage. Keyword indecision among "yoga rugs," "yoga mats" (rejected, inaccurate), and "Ayavastra" (rejected, unsearched term). Denroy floated "outdoor yoga rugs" as an off-the-cuff (caveat: no formal keyword research done) example H1. Specific heading rewrites discussed: "the healing power of Ayavastra" → possibly "the healing power of Ayurveda"; "Natural botanical dyes" → work in "naturally and botanically dyed yoga rugs"; "Our best sellers" → "Our best selling yoga rugs."
- **Yvonne** — executive assistant to "Dr. S," medical weight-loss clinic in Chandler, Arizona. Old site ranked **#1 for "weight loss Chandler" / "weight loss in Chandler, Arizona."** New dev site (not yet live) homepage headline ("Lose weight, keep it off, tighten tone contour") and secondary heading ("Three pillars of health") both omit the keyword and location entirely. Services offered: weight loss, hormone, medical aesthetics. Some site videos correctly YouTube-embedded, others not.

## Notable verbatim quotes

- "So you've already uploaded the new versions. Just go ahead and remove the old versions, the PNG JPEG from your server and that should speed things back up."
- "The styling does not matter. The H1 does not have to be the largest text."
- "Google search engines overall will prioritize keywords in heading tags higher than keywords in regular paragraph content."
- "You always want your headings to have a purpose other than just learn more. You don't want your headings to be generic."
- "Can the question be answered in one paragraph? ... If the answer is yes, turn it into a blog. If the answer is something simple, well, you can keep it as an FAQ on your homepage, service or contact page."
- "It depends. So take a look at what the competitors are doing. How many times have they mentioned it? If they only mentioned it once, you likely will only need to do it twice. If they mention it 20 times, you'll likely have to do it 21."
- "The only [time] styling matters is if the text is invisible or not. Otherwise the size does not matter... And it appears first. The headings appear in order. That's what matters."
- "The sooner that keyword appears in your title, in your meta description, in the content as a whole, the more important Google and crawl bots will view that keyword."
- "Only heading one is limited to just one per page. Heading two, you can have as many as you [want]."
- "This canonical tag does not match sitemap... What this tells Google in crawl bots is that the correct URL to have this content is on slash portfolio. However, if we take that URL and paste it in, we get a 404."
- "You are going for one of the most competitive keywords you possibly can go for."
- "Going for overall Toronto is going to be one of the longest SEO journeys you can possibly have... It is very, very expensive, multimillion dollars to rank for this keyword."
- "As recently as last year, Google has started punishing sites that have too much white space in their content... You're losing points with Google for how high your page can rank."
- "Get very narrow to the locations, to the point of neighborhoods even that you want to rank for."
- "You just want to have your keyword as many times as possible to get the ball rolling. Especially since you are such a new site."
- "Never ever host your own videos. Always upload them to a player like YouTube, Vimeo Daily anything... Unless you have your own super strong dedicated server. And even then YouTube is just better."
- "If you offer multiple services, your primary service, the one that makes you the most money will be your homepage... One keyword per page is the general guideline you will always follow on any site."
- "You never want to external link to a competitor for any reason."

## Tradeoffs & nuance

- Squarespace's auto-appended business name in titles is technically flaggable by audit tools but often a non-issue in practice because Google frequently strips it in real SERPs — worth distinguishing "audit tool warning" from "actual ranking problem."
- Keyword density has no universal number — it's always relative to what's currently ranking, meaning the "right" amount changes per SERP and must be re-checked, not treated as a fixed formula.
- When a page has two competing H1-like headings, the fix isn't to delete either — content should be preserved and only demoted (H1→H2 or plain text) to avoid losing on-page copy/value while still resolving the duplicate-H1 technical issue.
- Aggressive keyword repetition ("as many times as possible") was advised specifically because the site was brand-new with no authority yet — implying this tactic is a bootstrapping move, not a permanent best practice once authority is established.
- For the Toronto wedding photographer case, the tradeoff is explicit: chasing the broad, high-value keyword immediately is slower and far more expensive than winning narrower local/neighborhood terms first and building authority up to the bigger term over time.
- Denroy repeatedly deferred exact keyword/heading choices to formal keyword research (SEMrush/Ahrefs) rather than prescribing a term outright, even when brainstorming examples on the call (e.g. "outdoor yoga rugs" offered explicitly as an unresearched guess, not a recommendation).
- Some diagnoses were left open/unresolved live (e.g. Emphasize's persistent single-page canonical issue) with a next-step investigation path given rather than a guaranteed fix, since the exact cause (caching vs. theme override vs. other conflict) couldn't be confirmed on the call.
