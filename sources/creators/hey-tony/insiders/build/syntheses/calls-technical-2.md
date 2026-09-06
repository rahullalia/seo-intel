# Technical SEO — Consolidated Synthesis

**Source calls (chronological order):**
- Call #121 — "Technical Replay with Denroy," 2025-12-04 (small call: Brett, Monica via written Qs, James; 51m25s)
- Call #110 — "Technical SEO with Denroy," 2025-12-18 (largest call ever run, ~40 attendees, normally 5–10; runs every two weeks, replays post within ~2 days)
- Call #097 — "Technical SEO with Denroy," 2026-01-15 (second-biggest call ever)
- Call #086 — "Technical SEO with Denroy," 2026-02-12 (smaller call; Denroy covering Matt's writing-call slot the following two Mondays)

**Host:** Denroy, technical SEO team lead at Hey Tony, ~5–5.5 years working with Matt as of these calls (one call cites "6 years" from an earlier session, since corrected to 5). Background spans SEO, web design/dev, WordPress, Shopify, Wix, Squarespace, HubSpot, Storyblok, Google Ads, GMB/GBP, and some YouTube/Reddit/Pinterest SEO. Format throughout: live Q&A, raised-hand queue, live screen-share audits, no fixed lesson plan. DM response commitment: within 48 hours.

---

## 1. Keyword Strategy: One Keyword Per Page

- **Baseline rule, restated every call, no exceptions:** one keyword per page, site-wide. *"You want to rank for one keyword per page. You want to focus on that singular keyword per page."* / *"Basically you want to go one keyword per page that you want to optimize for."* / *"This goes back to every page having one keyword to optimize around."*
- **Selecting which keyword:** pull candidate variants into a keyword tool, compare search volume vs. competition/difficulty, and pick the **easiest to rank for — not the highest-volume one**. Example candidate set for a print-on-demand store: "funny T-shirts," "funny apparel," "funny memorabilia," "gag gift."
- **Homepage vs. interior-page split:** if collection/product pages already own product keywords, make the homepage a branded page instead (H1 = brand name, title tag = brand name + what the store sells, meta description spells out the offering).
- **Before changing an existing page's target keyword (e.g., a homepage rebrand):**
  1. Run the candidate keyword through a keyword tool to confirm it has real search volume — never assume a desired phrase has volume just because you want to rank for it (case: assuming "Waste Solutions" had volume without checking).
  2. Check Google Search Console for what the page currently ranks for.
  3. If it already ranks well for the existing keyword, leave that page/keyword alone — build or optimize a **separate page** for the new target instead of overwriting.
  4. If research supports the new keyword, update the title tag (target keyword + business name), match the meta description to the exact keyword, and sprinkle the keyword through H2s.
  5. Also update the old page's copy/keywords so the two pages don't compete for the same term (cannibalization).
- **Local-intent keyword targeting:** rewrite broad/regional titles to name the specific state/city (e.g. "Northwest Lien" → "Mechanics Lien in California"); narrow to a specific city where possible for lower competition. Same fix applies to meta description.
- **When a head term is extremely high-difficulty and the site has weak internal linking/backlinks:** stop pushing it; go narrower/lower-difficulty, including adding a location modifier (e.g. "Texas website hosting" if most clients are in Texas) to get traction faster. **~90% keyword difficulty is a flagged red line for a low-authority site** (cited for "web hosting," "VPS hosting," "shared hosting") — these need heavy internal linking + backlinks + content investment first; not a realistic first target.
- **Realtor/local-business keyword research workflow** (generic "Realtor" searches surface industry/practitioner content, not buyer/seller intent):
  - Break location pages down by **neighborhood**, not just city (east/west, named communities, "by the beach," etc.) — lower volume but far easier to rank, especially for a lower-authority site.
  - Structure content around buy vs. sell intent per neighborhood (e.g. "buy a beach home in Miami").
  - Mine actual past-client questions as keyword seeds ("what is the average house cost in Miami," "can I get approved for a mortgage on minimum wage") — type verbatim into SEMrush/Google to see real volume/variations.
  - Cross-reference SEMrush and Google's own autosuggest until landing on a term with real (even low, e.g. **10–20/mo**) volume at low difficulty.

## 2. Title Tags & Meta Descriptions

- **Title tag structure:** homepage = company name + that page's one focus keyword. Every other page = focus keyword first, then a line break, then the brand name at the end.
- Google frequently strips the trailing brand name from a title tag **in the SERP display only** — this is Google's display behavior, not a defect in your HTML. Verified live via the Detailed SEO extension (searched "does color affect SEO," compared SERP snippet to the live page's actual tag — brand name still present in the HTML).
- **Title tag keyword ordering:** if the primary keyword is buried after a modifier (e.g. "Colorful and Cute Combat Boots"), move the primary keyword to the front — provided keyword research confirms it's the higher-value term. Similarly, replace generic branded intros ("Welcome to Teton Excursions... Teton Excursions") with the actual money keyword up front ("Yellowstone Tours"), then extend with researched modifiers ("multi-day Yellowstone tours," "national park tours").
- **Meta description rules:**
  - Every page needs a **manually-written, unique** meta description — never rely on an auto-pulled excerpt of on-page content. Shopify in particular may auto-pull an arbitrary visible text block if no custom description exists — in one case this pulled EU-mandated product-safety/warning copy, a clear tell the field was never set.
  - Target length: roughly **140–145 characters** so it doesn't get cut off in search results.
  - When changing a page's target keyword, match the meta description to the exact new keyword.
  - Example meta description given live: *"Laulu Design is a boutique online store that offers funny T-shirts, apparel and drinkware."*
- **Shopify: where to set title tag/meta description:**
  - Homepage: Shopify Settings (site name/SEO fields) directly.
  - Individual product/collection pages: open the page in the dashboard, scroll toward the bottom of the editor for **SEO settings / search engine snippet** (sometimes hidden behind a pencil icon) — opens 2–3 fields: title tag, URL slug, meta description.
  - When unsure where a setting lives, ask **Shopify's own AI ("Sidekick")** — it can crawl the store directly. Exact prompt given: *"How can I edit individual page meta descriptions in Shopify?"* Denroy called it "quite good."
- **WordPress:** Yoast SEO plugin — SEO title and meta description fields live just above the URL slug in the page editor.
- **CTA/button copy** can use the exact target keyword directly — no need to invent a "natural" variation specifically for buttons.
- **Trimming AI-sounding/keyword-stuffed copy:** e.g., rewrote "Why Rainbow City Colorful Cute Combat Boots Are Different" down to "Cute combat boots are different."
- **Blog hygiene (Shopify):** make sure every blog post has a featured image, not just some of them.
- **Shopify blog pagination:** default is often set to show only 6 posts/page (splitting even 2 real posts across 2 pages) — set to **~30** so all current posts show on one page with headroom for growth, without adding click/crawl depth. As the blog grows past that, raise again to **60, then 100** — don't over-set upfront, since more posts per page = slower page load.

## 3. Heading Hierarchy (H1–H4)

- **Core rule, restated every call:** exactly **one H1 per page**, and it must be the **literal first heading** to appear in the page's rendered/DOM order. Headings otherwise run in strict order (H1→H2→H3→H4) with no skipped levels. *"You should only have one H1 and you shouldn't jump from H1 to heading to H4."* / *"For semantic HTML, you want to follow the rules of one heading one per page."* Confirmed directly that hierarchy matters for SEO: *"Does hierarchy matter when you're doing header tags? Yes."*
- **Never use the company/brand name as an H1** (or any header tag) — it's assumed knowledge. Put it in a normal paragraph or H2 if needed at all. *"That should never be a title tag. I mean a header tag."* Don't put the brand name in H2s on non-homepage pages either (service/product pages) — brand-name ranking happens automatically if everything else is done right: *"You will rank for your brand name no matter what you do. As long as you're doing everything else right, your brand name will rank no matter what."* More acceptable on the homepage itself, especially for a brand-new business establishing recognition.
- **If a heading jumps straight to H4** (skipping H2/H3, common in carousel/slider captions): ask whether that content needs to be a heading at all. If not, change the tag to a paragraph or div.
- **If nav/menu elements render as H2/H3 above the true H1** in page order (breaking "H1 must be first"): convert those to div or plain paragraph tags, recheck visually, patch with CSS if the tag swap breaks formatting. A designer objecting to an ugly default heading element is valid — resolve by demoting/hiding the tag visually via CSS rather than skipping the SEO fix.
- **Platform-specific fix paths:**
  - **WordPress/Elementor (theme-generated carousel/slider heading):** Appearance → Theme File Editor → confirm active theme/child theme → locate the file rendering the slider (varies by theme) → change the H4 tag to div/`<p>` → retest visually; if styling breaks, wrap in inline CSS (e.g. `<span style="...">`) matching the original heading's look. Alternative: edit the Elementor widget directly as plain HTML (availability depends on Elementor version) to see/change the heading tag in place.
  - **Shopify Dawn theme:** open `theme.liquid`, find the existing (often generic/ugly) H1 tag, change to div/paragraph, verify formatting.
  - **Shopify, general (empty/duplicate H1 fix):** Online Store → Customize (or Open Theme Editor) → locate `theme.liquid` → Ctrl+F/Cmd+F → search `page.title` (or "H1") → look for an empty `<h1></h1>`, an H1 wrapping the logo, or extra H1s injected by popups/plugins (e.g. a promo banner). If empty, insert the actual target keyword/title text as the H1.
  - Developers commonly mark **every** heading as H1 by default — *"Very common with developers"* (case: Dr. Karen's GHL-built site; she'd already corrected it herself before the call).
- **H2 count heuristic (no fixed universal number):** pull up the page currently ranking #1 for your target keyword, count its H2s, and use a similar number — a little more is fine (example: top page has 5 H2s → go for 7–8). Don't drastically overshoot (example: top page has ~50 H2s, going to 200 would be "way over optimizing"). In practice, **5–10 H2s is "totally fine"** for a normal article.
- **Keyword-to-content workflow:** find the keyword (via "what are people asking"-style research plus a keyword-volume tool) → primary keyword goes in the H1 → check what currently ranks #1 for it → mirror/slightly exceed their H2 depth.
- **Caching gotcha — conflicting H1 reports:** if a page-audit Chrome extension says the H1 is fine but a full site-audit tool says missing/multiple H1s (or vice versa), treat it as a **caching problem, not a real conflict**. Expect **at least a 12-hour delay** before the audit tool re-crawls and reflects a fix, even after manually hitting "new crawl" — caching can also sit on the extension side or the site's own cache. Apparent ranking/traffic regressions right after a fix may just be this lag, not a real regression (case: Monique's site audit score rose 42%→92% but organic performance dipped immediately after — diagnosed as caching lag, not a fix failure).

## 4. Internal Linking — The Core Growth Lever

- **Hey Tony's own SEO service page** is the flagship proof case, told twice with slightly different elapsed-time estimates (Denroy himself uncertain both times, prefacing with "I think"):
  - Call #086: content unchanged for **~4 years**; climbed from **position 13 to position 1** using only accumulating internal links (every new blog post links to this one page). *"We have not changed this page, I think, four years now, and over time it went from position 13 to number one with only internal links."*
  - Call #097: left un-optimized for roughly **3 years**, reached #1 purely from cumulative internal linking out of "dozens of blog posts." *"We didn't optimize it for I think three years and over time from just internal linking to it from dozens of blog posts, it eventually got to that number one spot."*
- **Separate internal-linking speed case (Matt, cited in call #121):** Matt got a page to rank #1 in **3 hours** using internal linking alone — Denroy says he personally witnessed it happen live. *"Matt got a page to rank one in three hours. Just internal linking."* / *"I was there when you did that blog... that blog made me double check. Like wait, how'd mine do?"*
- **Core mechanism:** *"The more internal links you build to a page, the more Google will understand this page is important."* Google's crawl bots read internal-link volume as an importance signal.
- **Volume guidance — effectively no ceiling:** *"If you go, go crazy with internal links... 4, 5, 6, just go insane with it. And that has historically given us some of the best results."* Called one of Hey Tony's historically best-performing tactics.
- **Click depth (crawl depth) — clicks from homepage to reach a page — has recently mattered more** for getting service/product pages to rank, per Hey Tony's own internal testing. Minimize unnecessary extra clicks (e.g. a hover-menu turned into a click-to-open menu costs an extra click and should be flagged as both a UX and click-depth problem).
- **Workflow: fixing an under-indexed or low-authority site via internal links:** go through every blog post, find mentions of relevant terms (e.g. VPS, dedicated hosting, domain registrar, domain transfer), and add internal links from those mentions to the matching service pages — across the **entire blog back-catalog**, not just new posts.
- **Workflow: improving location pages live 1+ year with low visibility:** scan existing blog posts for mentions of that neighborhood/area and link back to the location page from there.
- **Priority order for a site/multiple sites with no SEO work done yet:** (1) get tracking installed and verified first (Site Kit/GSC/Analytics) so there's data to optimize against; (2) do keyword research inside Search Console — what's ranking, what's trending, what opportunities exist; (3) if a page is trending up but under-linked, write more content and add internal links to it.
- **International-expansion sequence for a small local business:** (1) publish lots of blog content to build domain authority and answer as many questions as possible; (2) once there's a real content base, build heavy internal linking from that content into true focus/priority pages (best sellers, top-converting collection, best-performing blog page); (3) use Search Console + sales data to identify which products/pages already earn traffic and prioritize linking to those specifically. Denroy declined to name a priority category without seeing that data: *"Without the data, I can't really suggest anything."*
- **Anchor format rule:** in-content/blog links should **always** be anchor text (should exactly describe the destination page); buttons are for hyper-specific homepage/CTA links (contact, get a quote, read more reviews) since buttons can be styled/animated to stand out.
- **Auditing internal links — don't trust a visual scan alone:** unstyled/white link text can hide that a link exists; hover/inspect to confirm rather than just looking for color (case: Thomas's web-hosting site had near-zero effective internal linking partly because existing links were white/unstyled and easy to miss).

## 5. External Linking Rules

- **Number one linking rule, stated every call it comes up: never external-link to a direct competitor, for any reason.** Naming them, praising them, or listing them is fine — just never hyperlink to them. *"The number one rule with linking is never link to a competitor."* / *"You're never external linking to a competitor. You can mention them however many times you want to... Just don't external link to them."*
- **"Best-of-industry" list-post technique** (from Matt's book — Marcus Sheraton / pool-installation case study, city likely Hamilton): write a listicle naming every competitor in your market (e.g. "best pool installation companies in [city]"), say genuinely positive things about them if warranted, but never hyperlink to any of them; internally link the page hard toward your own converting pages. You don't have to include your own company in the list at all. Tested both including and excluding his own company — *"didn't really make too much of a difference for conversions or clicks or impressions"* either way, but the page ranked and drove traffic both times. Result: ranked #1 for "best pool installation company [city]"-type searches, converting visitors via internal links on that same page. *"You will start ranking for those searches. Who is the best blank? Should I hire blank? Who is the best in blank?"*
- **A site still needs at least a few outbound external links to non-competitor sites/resources.** Zero outbound links reads to Google's crawler as a dead end and hurts authority for the site's important pages: *"If your entire site doesn't have a single external link, it doesn't go anywhere. When Google's crawl bots go from another site to yours, it stops there... it can't move on."* This is a two-sided requirement — sites need both plenty of inbound/internal links AND a handful of genuine outbound links; an all-inbound, zero-outbound site is a crawl dead end.
- **Testimonials/reviews:** always external-link each testimonial/review to its actual source (Google, Yelp, a specific review page). Connect displayed customer reviews back to the actual Google Business Profile review (link the review text or the surrounding div) plus add a "Read more reviews" button linking to the full Google profile.
- **Reddit backlinks are no-follow** — *"Google doesn't really seem to care about follow versus no-follow"* in this context; still treated as a genuine positive signal (see Section 12).
- **Citation directories** (Brownbook, Yellow Book/Yellow Pages) function as backlinks/authority builders for local businesses.

## 6. Canonical Tags, Dynamic URLs & GSC Error Triage

- **Identifying a dynamic URL:** check for a "?" or "=" near the end instead of a clean "/" — this marks it as a dynamic URL (e.g. an inventory/search-results page). *"Anytime you see a question mark or an equal sign at the end of a URL instead of that slash, this is more of a dynamic URL."* Dynamic/search-result pages with no static content are inherently harder to rank — the content keeps changing: *"Dynamic pages like this typically have a harder time ranking because the content is constantly changing depending on what is there."*
- **Diagnosing a canonical-page error (WordPress + Yoast + Elementor):** open the flagged URL and check for that "?"/"=" pattern — usually the real cause of the mismatch, not a genuine site defect.
- **Elementor template constraint:** if "Edit with Elementor" opens a shared template rather than a unique per-page layout, you can't fix the canonical tag (or heading behavior) on just one URL — editing the template changes behavior for every page built on it.
- **Fixing a dynamic search/inventory page's canonical issue:** build a static page (URL without "?"/"=" parameters), shortcode in the same search-results field/content, and separately exclude the dynamic URL pattern in **robots.txt** so crawlers/audit tools stop flagging it.
- **Checking if a URL is indexed:** paste the exact URL into the Google Search Console top search bar. **Green = indexed. Gray = not indexed. Red = there's a problem.**
- **"Crawled – currently not indexed" (GSC):** if it's a page you want ranking, add more on-page content and build more internal links to it. If it's a page you don't care about (e.g. leftover default/sample blog posts), just delete it.
- **"Alternate page with proper canonical tag" (GSC):** check if the flagged URLs are dynamic (contain "?"/"="). If so, safe to ignore — canonical is correctly pointing at the clean URL ending at the last "/".
- **"Page with redirect" (GSC):** Indexing tab → Pages → click the gray ("why pages aren't indexed") segment → find "Page with redirect" → click through to see the actual flagged URLs. Confirm it's a non-issue if all flagged variants (e.g. non-SSL version, `www` version, `www` + non-SSL version) correctly redirect to the one canonical secure non-`www` URL — GSC is just reporting that it saw those variants somewhere (sitemap, robots.txt, an llm.txt-style file, or CMS config), not flagging a real defect.
- **CMS auto-generated `/home` slug** (site builders that force the homepage's page title to "home," e.g. a Simvoly/"Simvali"-style builder): 301-redirect `/home` to the root domain, and additionally set the original `/home` page to draft/not-public inside the CMS to further minimize the chance a crawler indexes it as a duplicate.
- **General framing:** *"Some errors you will see in the page indexing tab in Search Console are not actual errors. It's just Google saying this cannot rank because XYZ reason."* / *"There will always be some issues in Search Console that aren't really issues. It's just things Google picks up on their end."* The skill is distinguishing genuine defects from Search Console/audit-tool noise.
- **Priority order for a site with no SEO work done yet:** (1) tracking installed/verified (Site Kit/GSC/Analytics); (2) keyword research inside Search Console; (3) content + internal links for trending-but-under-linked pages.
- **Google Search Console and a Google Business Profile are "completely" different products** — don't conflate them.
- **Case — MJ (auto-finance/ATV dealer, "Autoby Finance CA"):** dynamic inventory-search pages (Elementor template-driven) triggered canonical errors. After fixing other audit-tool errors, site audit score rose from **63 to 86**, with rising impressions, clicks, and visitor traffic.
- **Case — Coach D (ladyjunkcarbuyer.com):** GSC "Page with redirect" showed 3 URL variants (no-SSL, `www`, `www`+no-SSL) all correctly redirecting to the canonical `https://` non-`www` URL — confirmed non-issue. Her `/home` → root 301 redirect (from the CMS auto-naming the homepage "home") was confirmed done correctly.

## 7. Sitemaps

- **Submitting a sitemap in GSC:** Search Console → Indexing (left nav) → Sitemaps. If nothing appears under "Submitted sitemaps," none has been submitted yet. In **99% of cases** the path is just `sitemap.xml` (occasionally `sitemap_index.xml` or a platform-specific variant). Test it first by pasting `yourhomepage.com/sitemap.xml` directly into a browser to confirm it loads; only then paste that same URL into GSC's "Add sitemap" field. If status shows "Error" immediately after submitting, refresh the page — it can flip to "Success" without changing anything.
- **Sitemap is a hard crawl dependency:** if the audit tool (or Google, somewhat more resilient) can't find the sitemap, it can't crawl the site. *"If the audit tool can't find your site map, it can't crawl your site."*
- **Catastrophic case (unnamed client):** a deleted sitemap caused traffic to **drop from hundreds of thousands to zero**. *"We've had cases where we've had clients deleting sitemaps in the past that we've created and all of a sudden their traffic just drops from hundreds of thousands to zero."*
- **Permalink/URL structure changes:** always 301-redirect old→new for every changed slug, AND manually force an XML sitemap refresh/recrawl inside the SEO plugin — Yoast/All in One SEO usually auto-update but can lag, so don't rely on the auto-timing alone.
- **Platform gaps:** Go High Level (GHL) doesn't automatically surface/expose a sitemap for crawling — has to be manually located and exposed (case: Dr. Karen, still working through this at call's end; had consulted ChatGPT to try to find where her GHL sitemap lives, unresolved on the call).

## 8. Site Migrations, Rebrands & Redirects

- **Full domain/rebrand migration checklist:**
  1. Keep a list of every previous URL first.
  2. 301-redirect every old URL to its **exact new-URL equivalent** — not just homepage-to-homepage (e.g. `/seo-services` on the old domain → `/seo-services` on the new one).
  3. Anything without a clean 1:1 mapping: redirect to the new homepage instead.
  4. Immediately after cutover, confirm Search Console and Analytics tracking are set up on the new domain.
- **Domain rebrand for expansion (e.g. "Northwest Lien" → "NW Lien Service" ahead of nationwide expansion):** set up a 301 redirect to transfer domain authority.
- **Expanding into multiple states/cities:** add a "Locations" or "Service Areas" nav item, build a dedicated page per location.
- **Redirect priority order** (used when retiring low-value pages, e.g. tag pages): similar already-ranking page → similar category page → similar blog post → homepage (last resort only).
- **Redirect penalty rules:** Google does **not** penalize redirecting many old blog posts into one consolidated post. Google **does** penalize redirect loops — a chain that bounces and never resolves to a live page. *"Google will penalize if you... make a redirect loop that just bounces things back and never loads a page... But just redirecting traffic to a more important page will not [penalize you]."* The risk is in implementation/sequencing, not in the tactic of redirecting itself.
- **Any permalink/slug change:** always 301-redirect, and manually force a sitemap refresh (see Section 7).

## 9. Tag Pages & Content Consolidation

- **Tag pages: treat as effectively unsalvageable — don't use them at all; rely on categories instead.** *"They tend to be dead pages. A lot of the time it's duplicate content from the blog post that it's referring to... and there's no unique content on tag pages... most times we opt to never even use tag pages. Instead just use categories."*
- **Tag-page audit/cleanup workflow (case: Brett, realtor site):**
  1. Run `site:yourdomain.com` in Google to see everything indexed.
  2. In GSC: Performance → Search Results → Add Filter → Page filter → "URL containing" → paste the path up to `/tag/`. Surfaces every indexed tag page regardless of ending slug.
  3. Click "Pages" to see per-page impressions/clicks.
  4. If traffic is insignificant, delete the tag pages in WordPress and 301-redirect them (priority order per Section 8).
  5. **Threshold:** keep tag pages live if they're bringing in **more than 5% of total site traffic** — otherwise cut them. If they DO carry meaningful traffic, first publish better content to outrank them for the same keywords; once the new content ranks, delete the tag pages and redirect. Deleting first is riskier once a page has real traffic.
  - **Live numbers (Brett):** impressions of 29, 10, 3, 12, 2, 7 across tag pages over 3 months, with only **3 total clicks** combined — confirmed insignificant, cleared for deletion + redirect.
- **Merging near-duplicate blog posts targeting the same intent:**
  1. Pull Search Console data for each post.
  2. If one clearly and meaningfully outperforms the others, migrate the useful content from the underperformers into the winner, then 301-redirect the losers to it.
  3. If all posts perform similarly (or all perform poorly, even if one technically ranks), combine all the content into one post and re-optimize for a single keyword.
  - Consolidation is **intent-dependent, not purely traffic-dependent**: two posts can both be "about SEO" and legitimately stay separate if they serve different keyword intents (e.g. "AI and SEO" vs. "are SEO services worth it"). Only true near-duplicates targeting the same intent should be merged.
  - **Case — Thomas (Albania, SEO agency site, non-English language):** 3 overlapping posts plus a tag page clustered around "what is SEO"-type intent, including one with "2025" in the URL that was a translated duplicate of another. Best of the three ranked **position #9** but wasn't capturing much traffic relative to the others. Since none clearly dominated: recommendation was to combine all three into one post, re-optimize for a single keyword, drop the year from the URL, and eliminate the tag page — while keeping a separate "AI and SEO" post as its own topic (different keyword intent).
- **URLs: strip out any embedded year** (e.g. `/2025/`) — becomes stale/less relevant as time passes.

## 10. Site Speed

- **Diagnosing mobile site speed:** run the URL through **pagespeed.web.dev**, check the **Mobile tab separately from Desktop** — desktop often scores fine while mobile doesn't. Look for flagged issues like high LCP and heavy JavaScript.
- **Previewing mobile rendering/animations:** Chrome right-click → Inspect → click "toggle device toolbar" (top-right of DevTools) → pick a device (e.g. iPhone 12) to see what's actually loading/animating on mobile.
- **Fixing slow template-based sites (Wix/Shopify/WordPress purchased templates):** have a developer audit for leftover unnecessary code/scripts from the template; disable non-essential animations, especially on mobile; defer scripts into a CDN (e.g. Cloudflare). *"Very often with templates, not just on Wix, Shopify, WordPress, there is some unnecessary code in there that can... slow things down."*
- **Wix-specific constraint:** users can't access hosting-level settings (no cPanel/host manager) — must contact **Wix support** directly to adjust those settings.
- **Case — Katie (Wix site):** mobile PageSpeed issues traced to a purchased template with heavy scripts/animations; fix path = developer script cleanup + Wix support ticket + disabling non-essential mobile animations.
- **Blog pagination as a speed lever (Shopify):** don't over-set posts-per-page upfront (see Section 2) — more posts per page loading = slower page load; scale the number up only as the blog actually grows.

## 11. Local SEO

- **Geographic expansion sequence:** rank in one small area first, win it, then branch outward. *"When you're trying to rank locally, one thing you always want to do is start in a much smaller area, and then once you win that area, start branching outwards."* Hey Tony's own model: start in Hamilton (Matt's home base), then expand to Toronto or Windsor.
- **Local-intent title/meta fix:** name the specific state/city being targeted rather than a broad regional term; narrow to a specific city if possible for lower competition.
- **Neighborhood-level location pages** (vs. city-wide): trade search volume for winnability — lower monthly volume than a city-wide "Realtor [city]" term, but much more realistic to rank, especially on a lower-authority site. Structure by buy vs. sell intent per neighborhood.
- **Improving underperforming location pages (live 1+ year, low visibility):**
  - Add the location-page link into **Google Business Profile posts**, with descriptive copy naming the service + location.
  - Build more internal links to those pages by scanning existing blog posts for mentions of that neighborhood/area.
- **Physical/local presence as an SEO lever:** a verified physical location + properly set-up Google Business Profile can produce a fast #1 local rank; also unlocks Google Maps visibility to nearby people who don't already know the brand; also unlocks citation-building (directory listings functioning as backlinks), raising domain authority. Named citation directories: **Brownbook, Yellow Book/Yellow Pages**. Framed as a genuine SEO lever but ultimately a **business-model decision**, not just an SEO checkbox — going physical/storefront remains separate from the SEO upside.

## 12. Reddit Keyword Research (Insiders Proprietary Tool)

- **Location:** Insiders homepage, scroll down to a bright-orange "Reddit keywords" box, or under the **Tools** section at the bottom of the homepage. Built "99%" by Matt.
- **Core workflow:** type a seed keyword in → it crawls multiple subreddits and returns the actual questions people are asking about that term (plus keywords, pain points, and content ideas) → lists the source subreddits at the bottom of the results → search each question individually → check what's currently ranking / what angle competitors are actually targeting → if no one is directly answering that exact question, write a blog post that answers it head-on. *"You give it a keyword and it will crawl through multiple different subreddits looking for that keyword, looking for that mention, and let you know where those conversations are taking place."* / *"The entire purpose of this tool is to find the questions people are asking, search those questions, see what the competitors are already doing."*
- **Treat the four output types independently, not as one funnel:**
  - Questions → answer directly in-thread or via a dedicated blog post.
  - Keywords → run through Ubersuggest/SEMrush/Ahrefs.
  - Pain points → use as a blog subheading.
  - Content ideas → spin into a wholly separate blog, or into a local-service page (e.g. a "web designer and SEO services" page).
- **Niche single-product application:** type the exact product into the tool (example: "gymnastics rings") to surface every question people ask about it — *"What are gymnastic rings made out of?", "How thick should they be?", "What makes gymnastics rings good?"* — answer each in its own separate blog post; each becomes a bottom-of-funnel, high-intent, low-competition page.
- **Reddit engagement — three interchangeable modes:** (1) simple question → answer directly in-thread, optionally adding "if you want to know more about X, here's an example from [company]" with a link; (2) broader question → write the full blog post, reply on Reddit answering the question and linking to it; (3) do both on the same thread.
- **Demand-signal nuance:** even when SEMrush/Ubersuggest/Ahrefs show **zero search volume** for a Reddit-sourced question, if the source subreddit conversation is still active, treat it as real (if unmeasured) demand. Google's "People Also Ask" boxes are independent confirmation a keyword/question is being searched even when standard tools show no volume. *"Even if [research tools] say zero, there is still some traffic to those keywords or related keywords."*
- **Especially effective for LLM/AI rankings, not primarily classic Google rankings:** *"Many companies, many online brands that don't have a local business, don't have a specific local area, are getting a lot of mentions on Reddit... they're gaining traffic, they're outranking competitors, especially in LLM rankings. So ChatGPT, Gemini, things like that. Not so much with Google rankings, but a lot to do with AI rankings."* A business optimizing purely for classic SERP position shouldn't expect the same lift as one chasing AI-tool visibility.
- **Origin case study — Denroy's own "does color affect SEO" blog:** searched "SEO colors," found via the tool that people were asking a specific question competitors weren't directly answering (they targeted hierarchy/usage/conversion angles instead); wrote a blog answering that exact question, which ranked **#1, #2, or #3 within days**. General result cited across many Reddit-sourced posts: *"We've gotten plenty of high impression keywords at low difficulty. We've gotten plenty of featured snippets off of this. And this has won several AI references just because we're answering a very specific question that no one else has talked about."*
- **A second, unreleased tool** — Denroy personally built the majority of it, "coming soon," not currently pushed to the Insiders group, no further details given.

## 13. Diagnosing Traffic/Ranking Drops

- **Full workflow (case: Monica's site — Ahrefs DR dropped 36→4, homepage visits fell from "hundreds" to fewer than 100/month):**
  1. Go into Search Console, run a period comparison (a few months ago vs. now).
  2. Filter the dropped pages by clicks — identify whether it's a specific page or a specific search query losing clicks.
  3. Manually search the losing query in Google — check for a new competitor going heavy on that keyword, or new competing content that's displaced you.
  4. Check Search Console → **Security & Manual Actions** (left sidebar) — a manual action signals a backlink problem; may require disavowing low-quality/spammy backlinks.
  5. Get the full scope from Search Console before doing anything drastic (e.g. before disavowing).
  6. Separately, **treat a huge Ahrefs DR swing with suspicion** — it can be a false flag if their crawler hasn't fully refreshed; run a secondary Ahrefs crawl to confirm before acting on it.
  - In Monica's case, the only recent site changes were heading-tag corrections and title/meta description improvements — Denroy's read: more likely backlink-related (spam/quality) than the on-page edits, but the DR number itself was also flagged as a possible stale-crawl artifact needing re-verification.
- **Two distinct causes require two distinct responses:** a real backlink-quality problem (→ disavow candidate) vs. third-party tool crawl staleness (→ just re-crawl and re-check). Jumping straight to disavowing without confirming which is discouraged.

## 14. Locale/Geo Duplicate Content

- **Case pattern (Shopify `EN-CA` vs. default English pages mirrored across the whole catalog):** pull Search Console to see which locale variant is actually ranking.
  - For **blog content:** redirect the lower-performing duplicate to the higher-ranking one.
  - For **product pages:** don't force a redirect without a prompt/switcher — let the visitor confirm.
  - Check installed Shopify apps for a geolocation/geo-redirect app — Shopify doesn't fork locale URLs like this by default; review the app's settings. Treatment is case-by-case.
  - **Case — Andrea:** `EN-CA` vs. default-English locale-duplicated URLs across every page/product, most likely caused by a geolocation app rather than native Shopify behavior; resolution deferred to reviewing her actual plugin screenshots.
- No one-size-fits-all fix — the real fix lives in whatever third-party geolocation app is installed, and correct behavior differs for blog vs. transactional pages.

## 15. Looker Studio Analytics & AI/LLM Referral Tracking

- **Tracking trending pages/posts in Looker Studio (case: Monica's Q4 review), step by step:**
  1. Open the landing-page chart, edit its filter (or add one).
  2. New filter → Include → field = landing page → condition "contains" (or "equals to" if using UTM/tracking codes) → paste the page URL → save.
  3. To track multiple pages on one chart: edit the filter again, use the "OR" option, add another "landing page contains [url]" line, repeat per page/post.
  4. Output: individual growth per page plus a combined growth total across everything included.
  5. To isolate one page again, delete the extra OR conditions.
  - **No dynamic way (yet)** to pull GSC/GA4's native "Trending"/Insights tab into Looker Studio — fully manual, copy-paste each URL. Team is watching for Google to add a trending dimension to Looker Studio; doesn't exist yet.
- **Blending Google Analytics into the same Looker Studio report:** Add Data Source → Google Analytics → select the GA account (must share the same signed-in email) → Accept. Once added, GA and Search Console data combine in the same report.
- **Tracking AI/LLM referral traffic via GA4 in Looker Studio:** create a filter on dimension **"session source,"** condition **"contains,"** value = the AI platform name (e.g. "chatgpt" for ChatGPT traffic, or the model name for Perplexity). Surfaces every session where that AI referenced/cited the site. Same pattern for any additional LLM — just swap the string. Demoed live on the Hey Tony profile itself.

## 16. YouTube ↔ Blog Cross-Promotion

*(Case: James's son, cleaning-content YouTube/TikTok channel building a blog backwards, site letscleanthatup.com — built a large following during COVID, "already an authority," already surfacing in ChatGPT search results for his video topics; team backfilling SEO/website infrastructure after audience-first growth.)*

- **Link the matching blog post in the YouTube video description** whenever topics are the same.
- **Reword the anchor phrase to include the actual target keyword** next to the link — e.g. *"Read our blog on the best way to clean your oven"* instead of generic "Read the blog here." Creates pseudo-anchor-text so Google associates the keyword with that URL even without a literal hyperlinked keyword. *"Google's not dumb. It can still tell... this was meant to go with this."*
- **Put that blog link above the fold** in the description (visible before "show more"/"view more") — links higher up carry more weight than links buried lower.
- **Embed the matching YouTube video directly inside the corresponding blog post.**
- **Image alt text must contain the target keyword** (or a variation) for that page while still accurately describing what's actually in the image — never keyword-stuff for its own sake. *"Don't just keyword stuff for the sake of keyword stuffing. That doesn't help anyone."*
- **Internal linking: "go crazy"** — 4, 5, 6+ internal links per post; called one of the historically best-performing tactics, no stated ceiling.
- **Live audit findings on the oven-cleaning post/video:** blog link found buried below the fold in the YouTube description with generic "read the blog here" phrasing; images missing alt text; heading structure otherwise good (clean single H1) but one empty H2 found; good use of timestamps; heavy use of Amazon affiliate links assessed as fine as-is; internal linking gap flagged as the top priority to fix going forward.

## 17. Social Bio-Links & Email/Newsletter Strategy

- **Bio-link strategy (Instagram/TikTok → website):** avoid Linktree/aggregators — link directly to the destination site/page wherever the platform allows it. *"I always say link directly to the website or the page you want. You don't want to link to the middleman."* / *"I am very against this link tree link, if possible."* Reasoning covers both SEO (link equity passes to the middleman domain first, only the remainder reaches your site) and UX (extra redirect hop can fail if the aggregator is slow, or if the visitor's ad-blocker/anti-spam extension blocks the redirect). Not banned outright — acceptable when a creator deliberately spreads attention across many platforms with no single preferred destination; works against you when the actual goal is funneling one platform's audience toward one specific destination.
- **Email/newsletter — core technique: behavioral list segmentation.** Automate moving a subscriber to a different list/segment based on which email(s) they open (open one → move to list A; open another → move to list B, etc.). *"Email is one of the best platforms for conversion optimization. It beats almost everything when you manage your email list properly."*
- **Platform notes:**
  - **Beehiiv** — James's son's platform, founded by the team behind Morning Brew (built after they sold it); described as "high level" on features/segmentation; already supports full open-based segmentation/automation, so no urgency to migrate off it. Case: ~**7,000 subscribers**, entirely organic, "no push," no active list-building lift; paused during a family caregiving period, now being relaunched as a priority.
  - **Mailchimp** — Denroy's suggested simpler fallback if advanced automation isn't required.
  - **GoHighLevel (GHL)** — Matt's own preferred email platform; Denroy explicitly said he's "not too experienced" with it and deferred detailed GHL questions to Matt.

## 18. CRO-Adjacent Fixes Flagged During Audits

*(Explicitly called out as beyond pure SEO but worth doing anyway since it affects whether ranking traffic actually converts.)*

- **Sticky-nav workaround:** if the header nav isn't sticky, replicate the same links (or at least main collections/categories) in the footer — a footer with zero links/buttons is a dead end for the visitor.
- Make scroll-arrow buttons bigger/bolder if easy to miss.
- Add padding to balance an off-center carousel start.
- Fix low-contrast text (thin light-gray-on-white).
- Place a CTA button near end-of-page content (e.g. beside a sizing chart) so the page doesn't dead-end with nothing left to click.
- **Accordion/toggle content with thin copy:** expand the content behind each toggle to include the target keyword/variations rather than one short line; if there's nothing substantial to say, skip the toggle entirely and list the content directly instead. *"Otherwise why are these in dropdowns? They could just be listed as is."*
- **Generic section headers → keyword-specific:** "What our customers say" → "What our customers say about our Yellowstone tours"; repeat per-product on individual tour/product pages (reviews heading made specific to that exact tour, not a reused generic block).
- **Finding where uneditable on-page text lives:** check if it's a plugin/shortcode-generated block (e.g. something like `[testimonials]`); if so, the copy must be changed in the plugin's settings, not the page content editor.

---

## 19. Tools & Platforms Quick Reference

| Tool / Platform | Use |
|---|---|
| **pagespeed.web.dev (PageSpeed Insights)** | Free Google tool; per-page speed/technical/accessibility scoring; separate Mobile/Desktop tabs; flags LCP, heavy JS |
| **Chrome DevTools** | Inspect → toggle device toolbar for mobile emulation/preview (e.g. iPhone 12) |
| **Hey Tony Page Audit tool** | Free Chrome extension built by Hey Tony; input a target keyword, returns keyword occurrences/density for that page; functionally similar to Detailed SEO |
| **Detailed SEO** | Chrome extension; Denroy's personal daily-driver ("a much older tool," habit not superiority); used to verify actual title-tag HTML vs. SERP display |
| **Hey Tony Site Audit Tool** | Proprietary crawler/checker; known ~12+ hour caching lag before re-crawl reflects a fix |
| **Hey Tony Reddit keyword research tool** | Proprietary, built ~99% by Matt; seed keyword → subreddit-sourced questions/keywords/pain points/content ideas (see Section 12) |
| **Second unreleased Hey Tony tool** | Denroy-built, "coming soon," not yet in Insiders group |
| **SEMrush / Ahrefs / Ubersuggest** | Search volume + keyword difficulty checks; cross-reference against Google's own autosuggest; Ahrefs Domain Rating can show stale-crawl false flags on big swings |
| **Serpstat** | Brett's former keyword tool — described by him as "not highly effective" |
| **Answer the Public** | Free-tier question/long-tail keyword ideas |
| **Google Search Console (GSC)** | URL Inspection (green/gray/red); Indexing → Pages (Crawled-not-indexed, Alternate page w/ canonical, Page with redirect); Indexing → Sitemaps; Performance → Search Results filters; Security & Manual Actions; period comparison |
| **Google Site Kit** (WP plugin) | Bundles GSC + Analytics; sends automated canonical-error emails |
| **Yoast SEO** (WP plugin) | SEO title/meta fields above URL slug; sitemap auto-update (can lag, force manual refresh) |
| **All in One SEO** | Alternative to Yoast, same sitemap-lag caveat |
| **Elementor** | WP page builder; template vs. per-page editing distinction determines whether canonical/heading fixes are page-specific or template-wide |
| **Avada** | Denroy's personal favorite WP builder, paired with WooCommerce — "we've used Avada the most of any WordPress website builder" |
| **Divi** | Named WP builder |
| **WooCommerce** | Page-builder stack (with Elementor); gives more creative freedom per Denroy vs. Shopify |
| **Shopify Dawn theme** | Default H1 lives in `theme.liquid` |
| **Shopify Sidekick (AI)** | In-dashboard "how do I" assistant; can crawl the store directly; example prompt: *"How can I edit individual page meta descriptions in Shopify?"* |
| **Cloudflare** | Example CDN for deferring scripts to improve page speed |
| **robots.txt** | Exclude dynamic/search-parameter URLs from crawling |
| **Google Business Profile (GBP)** | Posting location-page links with descriptive copy; fast local ranking off a verified physical address; distinct product from GSC |
| **Looker Studio** | Custom dashboards; landing-page "contains"/OR filters; blend GA4 + GSC; AI/LLM referral tracking via "session source contains [name]" |
| **Wix support** | Required for hosting-level speed settings (no user-level access) |
| **GoHighLevel (GHL)** | Matt's preferred email platform; also a client site-builder whose sitemap isn't auto-surfaced (must be manually exposed) |
| **Simvoly** (transcribed "Simvali") | Non-WordPress CMS; auto-names homepage page title "home" |
| **Citation directories** | Brownbook, Yellow Book/Yellow Pages — function as backlinks/authority builders |
| **Linktree** | Bio-link tool explicitly de-prioritized/avoided |
| **Beehiiv** | Newsletter platform, Morning Brew team; full open-based segmentation already built in |
| **Mailchimp** | Simpler newsletter fallback if no heavy automation needed |
| **WordPress Theme File Editor** | Appearance → Theme File Editor, for locating/hand-editing theme files (carousels, headings) |
| **WordPress redirect plugin** (unnamed) | For 301s after deleting tag pages |

## 20. Case Studies Index

| Client / Site | Call | Issue | Outcome / Numbers |
|---|---|---|---|
| **Laulu Design** (aka "Lalu Design") | #086 | POD store, Etsy+Shopify, live since October; title tag/meta unset; only 2 blog posts on 2 paginated pages (setting=6); collection pages missing custom meta (one auto-pulled EU product-safety text) | 322 impressions, 4 clicks over 14 days |
| **Goshopia** (Araceli, aka "Garopia") | #086 | Dubai sustainable/slow-fashion shop since 2019; second H1 further down homepage; multiple H4s used for carousel captions; WooCommerce + Elementor | Already had strong "sustainable fashion" language site-wide (rare even among new clients); goal: expand from small home market to US/Canada/Australia/UK |
| **Margaret** | #086 | Asked whether title tag should include company name + location vs. just keywords | Answered via homepage-vs-interior-page title rule |
| **Marcus Sheraton** (pool installation, from Matt's book) | #086 | Published "best pool installation companies in [city]" naming every competitor, zero external links to any | Ranked #1 for "best pool installation company [city]"-type searches; in/out of own-company-in-list tested, negligible difference in conversions/clicks |
| **Hey Tony's own SEO service page** | #086, #097 | Unchanged content, internal-links-only growth | #086: ~4 yrs unchanged, position 13→1. #097: ~3 yrs unoptimized, "dozens of blog posts," reached #1 |
| **Katie** | #097 | Wix site, mobile PageSpeed issues from purchased template with heavy scripts/animations | Fix = dev script cleanup + Wix support ticket + disable non-essential mobile animation |
| **Anthony** (NJ Dumpster Rentals → "Jersey Specialized Hauling") | #097 | Homepage ranks well for "NJ Dumpster Rentals"; wants broader "Waste Solutions" positioning | Plan: keep existing page/keyword, build separate Waste-Solutions-targeted homepage, consolidate dumpster keyword strength on dedicated service page. (Separately asked about GBP category change risk — not directly answered on call.) |
| **Lux** (mechanics-lien co., "Northwest Lien" → planned "NW Lien Service") | #097 | High CA traffic, poor conversion; WooCommerce site with hidden/extra-click nav (click-depth issue); developer called build "unnecessarily complex" | Considering rename + 301 + switch to Avada theme, for nationwide expansion |
| **Thomas** (web hosting company, site ~2 yrs old) | #097 | Only homepage indexed in GSC; targeting "web hosting"/"VPS hosting"/"shared hosting" (~90% difficulty); near-zero internal linking blog→service; thin About page competing with homepage for brand-name ranking; existing internal links were unstyled/white text | Already requested indexing + removed spam backlinks; recommendation: build internal links, go narrower/local first |
| **Heather** (clothing brand, "cute combat boots" line) | #097 | Shopify Dawn theme had stray H1 ahead of true H1; otherwise good fundamentals (canonical present, all images alt-tagged, single true H1) | Building dedicated money page for "Cute combat boots" (confirmed high volume/low difficulty via her own research) |
| **Aaron** (Teton Excursions, Yellowstone tour operator, WP + Avada) | #097 | Homepage title led with "Welcome to Teton Excursions... Teton Excursions" instead of money keyword; generic "What our customers say" headers on homepage + product pages | Fix: title → "Yellowstone Tours" + modifiers; keyword-specific review headings per page. (Site-speed concern raised but call ran out of time.) |
| **MJ** (auto-finance/ATV dealer, "Autoby Finance CA") | #110 | Dynamic inventory-search pages (Elementor template) triggering canonical errors | Site audit score 63 → 86; rising impressions/clicks/traffic |
| **Marlo** (vacation rental, "Casaluna Azul," Isla Mujeres, Mexico — 5 pages) | #110 | Whether to rank every subpage vs. consolidate; "crawled not indexed" pages (irrelevant sample posts); "alternate page w/ canonical" flag | Decision: focus on homepage, build long-tail content (e.g. "four bedroom beachfront vacation rental"); sample posts → delete; canonical flag → confirmed dynamic-URL noise |
| **Thomas** (Albania, SEO agency, non-English site) | #110 | 3 overlapping "what is SEO" posts + a tag page, one with "2025" in URL (translated duplicate) | Best ranked #9 but low relative traffic; recommendation: combine 3 into 1, drop year from URL, kill tag page; keep separate "AI and SEO" post (different intent) |
| **Coach D** (ladyjunkcarbuyer.com) | #110 | New to SEO/GSC; "Page with redirect" flag (3 URL variants); `/home` slug from CMS auto-naming | Both confirmed correctly handled / non-issues |
| **Monique** (Shopify, bee venom skincare) | #110 | Empty H1 on homepage + multiple stray H1s from theme/popup elements | Site audit score 42% → 92%; organic dip right after = caching-lag artifact, not a real regression |
| **Andrea** | #110 | Shopify `EN-CA` vs. default-English locale duplication across every page/product | Likely a geolocation app, not native Shopify; resolution deferred to reviewing her plugin screenshots |
| **Dr. Karen** | #110 | New to SEO via Rank Week; GHL site where developer had marked every heading H1 (already self-corrected); sitemap not surfaced in GHL | Confirmed 5–10 H2s/page fine; still working through exposing GHL sitemap (consulted ChatGPT, unresolved) |
| **Brett** (realtor, "Brett Sells Miami" → "Advanced Realty Miami") | #121 | Many low-value tag pages ranking (found via `site:` search); generic "Realtor" keyword research surfacing wrong-intent content | Impressions 29/10/3/12/2/7 across tag pages over 3 months, only 3 total clicks — cleared for deletion+redirect; pivoted to neighborhood-level buy/sell pages |
| **Monica** | #121 | Drastic ranking/authority drop: Ahrefs DR 36→4, homepage visits hundreds→<100/month; only recent changes were heading + title/meta fixes | Diagnosis pointed more toward backlink issue than on-page changes; DR swing itself flagged as possibly stale-crawl |
| **Matt (Hey Tony, internal case)** | #121 | Demonstration of internal-linking speed | Got a page to rank #1 in 3 hours using internal linking alone (Denroy witnessed live) |
| **James's son** (YouTube/TikTok cleaning creator, letscleanthatup.com) | #121 | Built large following during COVID (audience-first, "already an authority," already surfacing in ChatGPT results); backfilling SEO infrastructure | Fixes: reposition blog link above the fold w/ keyword anchor phrasing, add alt text, embed video in blog post, ramp internal linking (flagged as top priority) |
| **James's son's newsletter (Beehiiv)** | #121 | Organic list, paused during family caregiving (mother passed; father had Alzheimer's, also passed) | ~7,000 subscribers, entirely organic, "no push"; relaunch now a priority |
| **Unnamed client** | #110 | Sitemap deleted | Traffic dropped from "hundreds of thousands" to zero |

## 21. Cross-Cutting Tradeoffs & Nuance

- **Display behavior ≠ tag content:** Google visibly stripping a brand name from a title tag's SERP display doesn't mean the tag itself is wrong — the underlying HTML and Google's rendering choice are two different things.
- **Reddit-mentions strategy is asymmetric by channel:** explicitly framed as working "especially" for LLM/AI rankings rather than traditional Google rankings — don't expect the same lift chasing classic SERP position.
- **Zero-volume ≠ zero-demand:** standard keyword tools frequently show zero volume for Reddit-sourced long-tail questions — a tooling blind spot, not proof of no demand, provided the source subreddit thread is still active.
- **The Reddit tool's four output types are independently usable**, not a single sequential funnel — don't assume they build on each other.
- **Best-of list inclusion (own company or not) tested both ways** — negligible difference in conversions/clicks/impressions, though the page ranked and drove traffic either way; closing preference is still to keep the traffic for yourself.
- **External linking is two-sided:** sites need both inbound/internal links AND a handful of outbound links to non-competitors — all-inbound/zero-outbound reads as a crawl dead end.
- **Platform constraints change what's fixable directly:** Wix limits user-level access to hosting/speed settings (must go through Wix support); WordPress/Shopify issues (theme.liquid, plugin shortcodes, Elementor templates) are usually fixable by a developer with code access — but even then, the exact file/theme location "depends on theme" and "depends also on Elementor version," so troubleshooting sometimes yields a general path, not a guaranteed fix.
- **International/small-business expansion has no shortcut:** content volume and internal-link-building come first; broader geographic/competitive rank only after that authority is built.
- **Promotional vs. informative content isn't either/or:** promotional homepage copy is "fine," but informative content answering real user questions is "the main strategy" for traffic, domain authority, and AI-tool citations.
- **Keeping an existing ranking vs. rebranding a page's keyword:** don't force a rewrite where a page already ranks well — build a second page for the new target and let the two divide the keywords, provided their content doesn't overlap/compete.
- **Aggressive keyword targets vs. site authority:** chasing a ~90%-difficulty head term is possible in theory but impractical without heavy internal linking/backlinks first — go narrower/lower-difficulty (including local) for faster wins instead.
- **Design vs. SEO tension:** a designer not wanting an ugly default H1 visible is valid — resolved by demoting/hiding the tag visually via CSS rather than skipping the fix.
- **CRO advice is explicitly adjacent to, not part of, core SEO** — offered because it affects conversion of ranking traffic, but called out as a separate concern from ranking work itself.
- **Brand name in headings:** acceptable on the homepage (especially for a new business establishing name recognition), explicitly unnecessary on inner service/product pages.
- **A canonical/indexing "error" flagged by an audit tool isn't automatically real** — dynamic search-parameter URLs, correctly-redirecting protocol/subdomain variants, etc. routinely show up as "errors" needing no action; the skill is distinguishing genuine defects from noise.
- **Template-level canonical/heading issues on dynamic pages aren't always fixable directly** — sometimes the practical fix is a net-new static page rather than patching the dynamic one.
- **Content consolidation is intent-dependent, not purely traffic-dependent** — see Section 9.
- **Locale/geo URL duplication has no one-size-fits-all fix** — differs for blog content (safe to hard-redirect to the winner) vs. product pages (should prompt rather than silently redirect).
- **Apparent regressions right after a fix may just be caching** — both the Hey Tony audit tool and browser extensions cache aggressively (12+ hour lag cited); same-day "did this work?" judgments are often premature.
- **H1/H2 guidance is a heuristic, not a hard rule** — match roughly what the current top-ranking competitor page is doing (a little more, not drastically more), rather than a universal fixed count.
- **Redirecting is the same tool used both safely and harmfully** — consolidating old content or migrating URLs (safe) vs. redirect loops (penalized); the risk is in implementation/sequencing, not the tactic itself.
- **Tag-page deletion is conditional, not automatic:** a tag page already carrying meaningful traffic (>5% of site total) should be out-ranked with better content first, not deleted outright.
- **A domain-rating collapse has two very different causes needing different responses:** real backlink-quality problem (→ disavow) vs. third-party tool crawl staleness (→ re-crawl and re-check) — don't jump straight to disavowing.
- **Linktree-style aggregators aren't banned outright:** fine when a creator deliberately spreads attention across many platforms with no single preferred destination; work against you when funneling one platform's audience toward one destination.
- **Physical/local presence is a real SEO lever but remains a business-model decision**, not just an SEO checkbox.
- **Email platform choice is genuinely "it depends":** Beehiiv already covers advanced segmentation (no urgency to migrate); Mailchimp is only a fallback absent heavy-automation needs; GHL is Matt's preference but outside Denroy's stated expertise.
- **Tool choice (Detailed SEO vs. Hey Tony Page Audit tool, SEMrush vs. Ahrefs vs. Ubersuggest)** is repeatedly flagged as personal habit/familiarity, not one tool being objectively superior — described as functionally equivalent options.

## 22. Highest-Value Verbatim Quotes (not already inlined above)

- "Sometimes, actually most times, Google will even remove... the brand name from the end of your title tag when your pages appear in search results."
- "As the website loads in more blog posts, it will take longer to load. So hard-setting at 30. Make sure that if you publish more blogs in the future, go up to 60, 100 blog posts."
- "When Google send its crawl bots to scrape a site, one thing you always want to look out for is click depth, sometimes considered crawl depth... click depth seems to matter a lot more for getting service pages, product pages ranking higher."
- "Whoever created my website made every heading an H1 tag. Very common with developers."
- "This is the biggest call I've ever had... I've never had 40 people on any of my calls before. I run these calls every two weeks."
- "If the current rank one has 50 [heading twos] and then you're going for 200, that'd be way over optimizing."
- "Google Search Console and a Google Business Profile are completely different products" (paraphrase of a direct clarification made on-call).
- "People also ask sections in Google search results, so we know people are searching them even if the tools say otherwise."
