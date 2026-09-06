# Foundations: Site Audit Fixes + HeyKeywords Tool — Synthesis

Source: HeyTony Insiders curriculum, `auditFixes` (13 lessons) + `heyKeywordsTutorials` (5 lessons). Covers how to resolve every flagged issue in the site-audit tool and how to run the HeyKeywords keyword/competitor research suite.

---

## Cross-Cutting Rules (apply across multiple issues below)

- **Platform baseline**: Squarespace, Wix, Shopify auto-generate robots.txt, sitemap.xml, SSL/HTTPS, and auto-exclude admin/private pages from the sitemap. On these platforms most of the "infrastructure" audit issues below should never occur — if they do, it's a platform bug, not something you configure. **WordPress is where these issues actually surface**, because of custom builds, custom themes, and plugin conflicts.
- **Never run 2+ SEO plugins at once on WordPress.** Yoast SEO, Rank Math, and All in One SEO (AIOSEO) each inject their own title tag and meta description into the page. Running more than one simultaneously is the direct cause of "multiple title tags defined" AND "multiple meta descriptions defined" — same root cause, two different flagged issues. Fix: disable/uninstall all but one. Custom-coded sites can get the same issue if a dev hardcoded the tag twice.
- **Diagnostic tool: "Detailed SEO" Chrome extension** — instantly shows a live page's title tag, meta description, H1 tag(s)/count, and Open Graph/schema markup (under its "Social" tab) without needing to view source. Used repeatedly across the H1, title, and Open Graph fixes.
- **Diagnostic fallback: View Page Source + Ctrl/Cmd-F search for the tag** (e.g. search `h1`) when the extension isn't enough to find *where* a duplicate/hidden tag is being injected from in the template.
- **Not every flagged issue needs fixing.** Before fixing anything, ask: *do I actually want this page found/indexed/ranking?* Thank-you pages, ad-only landing pages, contact pages, category/archive pages, and funnel/sales pages routinely trigger "orphan page," "low word count," or similar flags and that's often fine/intentional — see individual sections below for which flags are safe to ignore and why.
- **Always re-run the crawl/audit after a fix** to confirm the flagged issue clears.
- **Internal linking is the unifying fix** behind three separate issues (orphan pages, dead-end pages, broken links): target **3–5 internal links per page of content**, on every page type — homepage, service pages, blog posts, product pages (e.g. "related products"). This keeps Google's crawler moving deeper into the site and keeps human visitors finding what they need faster instead of bouncing.

---

## Part 1 — Site Audit: Fixing Flagged Issues

### Infrastructure / Crawlability

#### Robots.txt Not Accessible
- Verify by visiting `yourdomain.com/robots.txt` directly — you should see a simple directives file (a minimal one just says "allow everybody and anybody to access my website").
- Auto-generated on Squarespace, Wix, Shopify, WordPress — you never need to set this up manually.
- If flagged: contact your developer or platform's support (GoDaddy builder, etc.) and ask specifically why `robots.txt` isn't accessible/doesn't exist.

#### Sitemap Not Available
- Verify by visiting `yourdomain.com/sitemap.xml` — should load a list of every URL on the site.
- Two reasons this matters: (1) the audit tool itself can't crawl your site without one; (2) it's the fastest way to submit your site to Google's index, especially for a new site.
- Auto-generated on Squarespace, Wix, Shopify, WordPress. If missing on any of these — or on Webflow, a GoDaddy builder, etc. — contact your developer/platform support; you should essentially never see this flag on a major platform.

#### Site Uses HTTP Instead of HTTPS
- HTTPS = encrypted connection (the "S" = secure); modern browsers expect every site to have it. Needed before you can safely accept payments or run an online store.
- Fix = get an SSL certificate, typically through your domain registrar (GoDaddy, Namecheap, etc.) or your host.
- Squarespace, Wix, Shopify: effectively impossible to *not* have HTTPS — handled automatically.
- WordPress: more custom, so this can genuinely happen. A *managed* WordPress host (e.g. GoDaddy-managed WordPress, not a custom server) usually still handles it for you. Self-hosted/custom-server WordPress may require you to purchase and install the SSL certificate yourself — contact the platform's support/help center or open a ticket if unsure how.

#### Page Not Accessible
- Cause: the page is password-protected, or it's an admin/editing page that shouldn't be public.
- Website builders (WordPress, Squarespace, Shopify, Wix) should automatically keep non-public/admin pages out of the sitemap — if this flag fires, something is misconfigured.
- Fix workflow: visit each flagged page and decide — should the public see this?
  - If it's a real page that should be public: remove the password / make it publicly viewable.
  - If it's an admin/system page that shouldn't be indexed: it needs to be removed from the sitemap — since most sitemaps are auto-generated, contact the platform (e.g. Wix/Squarespace support) and ask why these pages are appearing in your sitemap and whether they can be excluded.

### Content Issues

#### Page Has No Content
- Meaning: a URL/page exists but is completely blank — content was started or a URL was set up and then abandoned.
- Two valid fixes:
  1. **Delete the page and 301-redirect** that URL to another existing, relevant page on the site.
  2. **Finish building the page** if it's meant to serve a purpose for the brand.
- If a page is actively under construction: keep it **private/unpublished** while building. Otherwise it can get added to the sitemap and partially indexed by search engines before it's ready, letting people find an unfinished page.

#### Low Word Count
- Tool's built-in default recommendation: minimum **100 words** per page (author flags this as outdated / "I need to talk to my developer" — considers it too low).
- Author's real recommended minimum: **500+ words per page.**
- Agency's actual internal practice/target for pages they optimize for clients: **1,000–1,500 words per page.**
- Word count should be measured from the actual body content — **excludes footer text, nav/menu text, and sidebar boilerplate.**
- Fix for a genuinely thin/abandoned page: delete it if it serves no purpose.
- Fix for a real content page that should rank: add more substantive, on-topic words to the content area.
- **Pages where low word count is fine and not worth "fixing":**
  - **Contact pages** — expected to be sparse; keep in the nav menu so people/Google can find it; can optionally pad with an FAQ section if you want more content.
  - **Category/archive pages** that just aggregate other content (e.g. a "Facebook Ads case studies" category listing) — not meant to be indexed/ranked; word count naturally grows as more items get added to the category; can also add explanatory copy above the listing (e.g. "here's our strategy for Facebook Ads...").
  - **Funnel/landing/sales pages** used for external traffic (e.g. an Instagram bio link to a course offer) — deliberately excluded from the nav menu and not meant to rank publicly.

### Internal Linking Issues

#### Orphaned Page (No Internal Links Point to It)
- Definition: a page that cannot be reached by clicking around the website — it isn't linked from anywhere else on the site, even though it exists and Google may already know about the URL.
- Common legitimate reasons a page is orphaned (not automatically a problem):
  - **Thank-you pages** — reachable only after a form submission, never by clicking.
  - **Ad landing pages** — traffic sent from Google/Facebook/Instagram ads to a page deliberately not linked from the public site (e.g. a heavier discount than the public offer, or a follow-up/upsell page).
- Fix workflow:
  1. First decide: should this page actually exist/be findable? If it serves no purpose (e.g. an abandoned draft with a random URL and no idea what form it was for) — **just delete it.**
  2. If it should be kept and be findable: go into any other relevant page/post, **highlight anchor text** relevant to the orphan page's topic, use the editor's **link/insert-link button**, paste in the orphan page's URL, apply, save, publish.
  3. Re-run the report — the page should no longer show as orphaned.
- Key insight on why this matters for ranking: Google can technically know a page exists, but if **real humans** can't reach it by clicking around your site, Google treats that as a signal the page "isn't important to these people" and deprioritizes it in search — being crawlable is not the same as being link-equity-connected.

#### Dead-End Page (Has No Outgoing Links)
- Definition: a page with **zero outgoing links** — no internal links, no external links, no nav menu, no footer, no share buttons, no "related articles" widget. Essentially a page that traps a visitor with nowhere else to go.
- Fix: edit the page, highlight relevant text/keyword phrase in the content, click the **insert-link button**, and link out to another relevant page on your own site. Process is functionally the same across website builders.
- Ties directly into the internal-linking-density rule above: **3–5 outgoing links per page** (homepage, service pages, product pages included) is the target — keeps Google crawling deeper into the site and keeps visitors engaged/finding information faster.

#### Broken Link (How to Fix)
- Definition: clicking a link (internal or external) leads somewhere that no longer exists or errors out.
- Why it matters: broken links signal to Google "we're not on top of our site's user experience" — fix these as soon as they're flagged.
- Fix workflow:
  1. Open the flagged post/page and identify the exact anchor text / link instance flagged as broken.
  2. Manually test the destination URL in a new tab.
  3. **False positive case**: some external sites block crawler bots, which can make a perfectly working link get flagged as broken. If you've manually confirmed the link works, click **"manually validate"** — the tool will discount/exclude it on the next crawl.
  4. **Real redirect case**: the destination site restructured its URL (e.g. `shopify.com/enterprise` now redirects to a new URL that added the word "blog" into the path). The destination's redirect is legitimate/appropriate — but you should still **update your own link to point directly at the new URL** rather than relying on their redirect chain. Edit the post, locate the linked text, replace the href with the corrected URL, save/update.
  5. **No good replacement exists**: just remove the link entirely (unlink the text) — it's no longer flagged as broken because it no longer links anywhere.
  6. After fixing/validating, the next crawl/audit will reflect the corrected status.

### On-Page Tag Issues

#### Title Tag Issues — missing / multiple defined / too long / too short
- Title tag = the blue clickable headline in Google search results; also shown in the browser tab.
- **Target length: 50–60 characters.** Longer gets truncated with "..." in the SERP.
- **Multiple titles defined**: caused by running 2+ SEO plugins simultaneously (see cross-cutting rule above), or a custom site with the tag hardcoded twice. Fix: keep only one SEO plugin active.
- **Missing title**: genuinely hard to trigger — nearly every builder/CMS auto-populates a default title tag from the page name, even with zero SEO plugin installed. Demonstrated live: the author deleted both the SEO-plugin title field and the on-page title, and the system auto-refilled a default (page name + site name) title anyway — had to restore an old **page revision/history** to recover the original custom title.
- **Too long / too short**: edit directly in the SEO plugin's "SEO Title" field (Yoast/Rank Math-style snippet editor), available at the bottom of every page/post editor — this field can differ from the visible on-page headline. Optional: remove the auto-appended "| YourSiteName" suffix/separator if you don't want the brand name in the tag.
- **Highest-value tactic (stated as "really important")**: put your target keyword **as close to the front/beginning** of the title tag as possible.
- Good examples cited directly: *"How long should a URL be for SEO?"* (exact long-tail question match), *"Custom WordPress Development,"* *"Fixing 404 Errors,"* *"Disadvantages of Market Mapping: A Comprehensive Guide,"* *"How to Edit Captions in Facebook Reels"* (covers the "FB reels" phrasing variant too).
- Explicit **bad example** (author's own): *"10 Simple Ways to Improve Your Google Search Ranking"* — flagged by the author himself as "not a well optimized title at all" because the keyword isn't framed as the exact phrase/question being searched.

#### Meta Description Issues — missing / multiple defined / too long / too short
- Meta description = the descriptive snippet under the blue title link in Google's results ("Google Preview").
- **Length: Google displays roughly 120–150 characters** (varies by character width); commonly the practical cutoff is **~156–160 characters** before truncation with "...".
- Doesn't directly move rankings much, but it's your pitch copy to win the click over competing results — directly impacts **click-through rate (CTR).**
- **Multiple meta descriptions defined**: same root cause as multiple titles — 2+ SEO plugins active simultaneously, or hardcoded twice on a custom build. Fix: disable all but one plugin. Squarespace/Wix/Shopify users essentially never see this.
- **Missing**: nothing shows in the snippet at all — you should always have one set.
- **Too long/short**: fix directly in the SEO plugin's snippet editor (Yoast SEO / Rank Math / All in One SEO — Yoast also available for Shopify) at the bottom of the page/post editor. Use a character counter (example tool named: **wordcounter.net**) to check length before saving — worked example landed at **124 characters**, described as "kind of where we want it to be."
- **Best practice**: include your target keyword directly in the meta description.

#### No H1 Heading / Multiple H1 Headings Defined
- H1 = the largest heading tag, usually the biggest text near the top of the page; represents the page's main topic.
- **Rule: exactly one H1 tag per page.**
- H1 content should equal the page's exact topic (e.g. blog post title "How long should a URL be for SEO?" = the H1 verbatim).
- **Fix for missing H1**: in the page editor, convert a text block to "Heading 1" / "H1" / "Header 1" style (label varies by builder) and place it at the top of the page's content.
- **Fix for multiple H1s** — root cause is frequently a **theme/template module silently auto-injecting a hidden or duplicate H1** (case study: the **Avada WordPress theme** — described as "the most popular WordPress theme" — has a **Page Title Bar / Layout** module that was auto-generating an empty duplicate H1 on a page). Troubleshooting sequence:
  1. Use the **Detailed SEO Chrome extension** to see the current H1 tag(s)/count instantly.
  2. Use **View Page Source + Ctrl/Cmd-F search "h1"** to locate where in the raw HTML the duplicate lives.
  3. If still unclear, isolate by testing: delete page-builder sections one at a time (or insert a marker word like "test" into a suspected module) and re-check which setting is injecting the tag.
  4. Check theme-level page settings (e.g. Avada's Page Title Bar toggle, set per-page or globally) — disable it or edit the duplicate down to an H2/paragraph.
- **Explicit exception/test case** shared by the instructor: he intentionally runs 2 H1 tags on one specific service page (separate desktop-version and mobile-version designs, identical content) as a deliberate SEO experiment to see how Google's algorithm handles it — currently ranking #1 despite the duplicate. He's explicit this is a one-off test, **not standard practice** — the default rule remains one H1 per page.

#### Open Graph Issues
- Open Graph (OG) tags control how a page looks when shared on Facebook/social platforms: title, description, image, URL, and type.
- **OG Title missing**: should mirror the page's actual title tag exactly; same length/missing rules as title tags apply.
- **OG Image missing**: this is the page's **featured image**. Always set one on pages you'd actually want shared/seen socially (main homepage-adjacent pages, main portfolio/work page, main services page — flagged directly as gaps the instructor found on his own site and needs to fix). Category pages, testimonial pages, and other never-indexed/never-shared pages don't need one.
- **OG URL missing**: normally auto-populated by the SEO plugin.
- **"OG URL does not match canonical URL"**: called out as an issue you'll essentially never actually get.
- **OG Description too long — plugin bug case study**: the instructor's SEO plugin (Yoast) was **not pulling the actual meta description** he'd set for the OG description — instead it auto-grabbed the first chunk of body text from the page, producing mismatched/oversized OG descriptions. He flags this explicitly as a bug worth reporting to Yoast ("their social tags aren't pulling the correct descriptions, it's just pulling the first thing they see on the page").
- **OG Type ("metadata type")**: e.g. "article" vs. a service/product page type. SEO plugins auto-set this and typically expose **no manual UI control** (checked Yoast's "Cornerstone Content" and "Advanced" tabs — no option found). A wrongly-typed page (e.g. a service page tagged as "article") requires hand-coding the schema/OG type tag directly rather than through the plugin UI.
- **Diagnostic tool**: Detailed SEO Chrome extension → "Social" tab shows live OG/Facebook schema (type, title, description, etc.) for any page.
- **Rule of thumb**: if ALL Open Graph issues are flagged across most pages of a site simultaneously, it almost always means there's **no SEO plugin installed at all** (or it's badly misconfigured) — check that first before fixing tags one at a time.

---

## Part 2 — HeyKeywords Tool Workflows

> **Set the country filter correctly in every one of these tools before trusting any number.** Keyword/traffic data is described as "very different" between countries for the identical search term — wrong country setting silently skews every result (volume, difficulty, traffic estimates).

### Tool Pipeline (how the 5 tools connect)
1. **Keyword Research** — go deep on one keyword/topic idea.
2. **Domain Overview** — zoom out to a whole domain's (yours or a competitor's) authority, traffic, and ranking footprint.
3. **Keyword Gap** — compare two domains to find content-topic opportunities.
4. **Backlinks Gap** — compare two domains to find link-building opportunities (same UI pattern as Keyword Gap, applied to links instead of content).
5. **Find Questions** — surface real audience language/long-tail question content ideas, independent of competitor comparison.

### Keyword Research
- Workflow: enter a seed term describing what you sell — include your **city/location** if you're a local business (example used throughout: "plumber Hamilton") — hit search.
- Output per keyword: **Keyword Difficulty (KD)** score (example: "plumber Hamilton" = KD 60 = harder to rank), **search intent** classification (commercial / informational / navigational / transactional), and a **12-month search trend graph.**
- List controls: sort by min/max **volume**, sort/filter by max **KD** (e.g. filter to KD ≤30 to surface easier targets).
- **Known display bug** (flagged by instructor, expected to be fixed): the keyword *list* view can show a different — and wrong — KD number than clicking into that exact keyword's own detail page shows (example: list showed 17, detail page showed the correct 60 for "plumber Hamilton"). **Trust the number on the keyword's own detail page.**
- **KD sanity-check method beyond the raw score**: click into the current top-ranking result for a keyword and check whether those ranking pages actually have backlinks. If the top-ranking competitors have zero/few backlinks, that's a strong secondary signal the keyword is genuinely easier than its KD suggests (example: "24 hour plumber Hamilton" showed KD 45, but the author estimates real-world difficulty closer to ~20% because the ranking pages had no backlinks).
- **Content-modeling workflow**: scroll down to see the current **Top 10 (sometimes 9, if Google is showing AI Overviews)** ranking pages for the keyword — click through and study what content/structure/keyword placement they use, then build your own page to match/improve on what's already proven to rank ("this is what Google likes").
- **Primary + secondary keyword strategy**: pick a primary target keyword (pursue it even at higher difficulty if it's the right term), then search that same base term to surface close variations (e.g. "plumber Hamilton," "plumbers Hamilton Ontario," "emergency plumber," "plumber Stoney Creek," "best plumbers in Hamilton Ontario") and weave the relevant variants into the same page as **secondary keywords.**
- **Separate-page rule**: if a variant represents a meaningfully distinct location or intent (e.g. "Stoney Creek" is a different physical location than "Hamilton"; "emergency plumber" is a distinct urgent-intent search), give it **its own dedicated page** rather than folding it into the main page as a secondary keyword.

### Domain Overview
- Input: any domain — yours or a competitor's (root domain, or a specific page URL — see below).
- Metrics returned: **Authority Score**, estimated organic traffic, estimated cost to buy equivalent traffic via ads, number of organic keywords ranked, total **backlinks**, **referring domains**, dofollow vs. nofollow link counts, 12-month traffic trend chart, **Keywords by Position** breakdown, the full paginated list of organic keywords ranked, and **Top Referring Domains.**
- Instructor's explicit take on dofollow/nofollow: *"don't pay attention to these too much — people get really wrapped up in it — they both count, they both matter."*
- **Case study / cautionary example**: instructor's own site had **85 keywords ranking in the top 3 positions in January 2026**, which dropped to **just 9** after making changes to the site — flagged as "quite concerning," with a separate video promised to explain the cause.
- **Use case 1**: browse a domain's full ranked-keyword list just to harvest blog/content ideas, without running a formal Keyword Gap.
- **Use case 2 — page-level backlink scoping**: paste a **specific page/post URL** (not just the root domain) into Domain Overview to see backlink data scoped to that one piece of content. Worked example: a specific blog post showed low Authority Score, ~0 estimated traffic, **4 backlinks, 4 referring domains, 4 dofollow links** — used to estimate "I probably only need ~4 links to this exact page to compete."

### Keyword Gap
- Input: your domain + a specific competitor's domain (country filter still applies).
- Output categories: **Opportunities** (keywords the competitor ranks for that you don't — case study: **735 opportunities** found between two example sites), **My Exclusive Keywords**, **Shared Keywords**, and **Position Battle** (head-to-head on shared keywords — example: winning 20 of the shared set).
- Each opportunity row shows search intent (informational / commercial / navigational / transactional).
- **Filter box**: type a theme word (e.g. "SEO" or "how to") to narrow a huge opportunity list down to a specific content angle.
- **Guidance on difficulty**: *"it doesn't really matter what the difficulty is, it just [has to] make sense for your website"* — sanity-check relevance to your business before filtering by KD.
- **Caution for newer/lower-authority sites**: avoid chasing the hardest-looking keywords at the top of these opportunity lists — prioritize realistic, winnable targets.
- **Simpler alternative** that skips the two-domain comparison entirely: just run Domain Overview on a single competitor and browse their ranked-keyword list directly for ideas.

### Backlinks Gap
- Input: your domain + competitor's domain — same two-domain UI mechanic as Keyword Gap, but for links instead of content. Instructor's framing: *"very, very similar, but different."*
- Output: **Exclusive Backlinks** (yours only), **Shared Backlinks** (both of you have — often generic directories you both already submitted to), and the priority section, **Opportunities** — domains linking to your competitor but not to you.
- **Actionable workflow**: click through each opportunity domain to categorize it — free/self-submit business directories (examples encountered: **Silex Canada**, "Flyers Online," "OpenDi"-type sites), dead/unreachable sites ("this site can't be reached"), paid-listing directories ("this one has pricing"), or guest-post-style sites requiring direct outreach.
- Framed as *"the quickest and easiest way to find backlinks for your business and potentially take some away from your competitor."*

### Find Questions
- Instructor calls this feature **"my favorite."**
- Input: a seed term describing what you sell (examples used: "manicures," "nail salon").
- Mechanism: scans real people's actual questions from sources including **Reddit, Quora, and "People Also Ask"**-style results, then AI reads and clusters them into labeled **topic clusters.**
- **Case study output ("manicures")**: **25 questions found**, **9 threads analyzed**, **7 topic clusters** — example cluster "Salon Quality and Standards" containing questions like *"Why do some nail salons charge more for manicures?"*, *"What should I look for in a clean, high-quality nail salon?"*, *"How can I tell if a nail salon is trustworthy and sanitary?"*
- **Second example ("nail salon")**: surfaced clusters like "Nail Salon Amenities" (*"Where can I get a pedicure with a massage included?"*) and "Nail Salon Experience" (*"How long do I typically wait at a good nail salon?"*, *"What should I expect from a nail salon experience?"*) — not every surfaced question is a great content target; requires human judgment to filter signal from noise.
- **Strategic framing**: these are long-tail keywords most competitors ignore, and the instructor states most are "really easy to rank for" — aim to be the literal answer/result for that exact question.
- **Critical filtering rule (repeated explicitly)**: **avoid using location/city names surfaced in sample questions unless it's literally your own location.** Example locations the tool surfaced that should be skipped/ignored unless locally relevant: San Francisco, Rochester, Portland, San Diego, Memphis. A generic question-answering blog post does **not** need your city in the title or content — this directly contrasts with the local-page strategy in Keyword Research, where a distinct location variant (e.g. "Stoney Creek") *does* deserve its own dedicated page. **Rule of thumb: use location keywords for local service pages; do not use them for generic informational/question-based blog content.**
- Results take a few seconds to generate — the tool has to crawl sources first, then have AI read/cluster everything before displaying.
- **Workflow suggestion**: run multiple seed terms/synonyms for the same business (not just one core term) to surface more distinct question sets.
