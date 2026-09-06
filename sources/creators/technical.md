# creators | technical

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2026-07 | Every site needs HTTPS

- Source: HeyTony master playbook, Part IV HTTPS, 2026-07 (skills/skills/heyTony/reference/part-4-technical-and-internal-linking.md), local file
- Quote: "Every site needs HTTPS (the encrypted "S"); modern browsers expect it, and it is required to accept payments."
- Means: Install an SSL certificate through the registrar or host, then bulk-swap any hardcoded http links after a rebuild.
- Factor: https | Evidence: D | Lever: ranking | Scope: organic local ai | Stage: build

## 2026-07 | Mobile-first indexing means a cut-off phone layout is a direct negative

- Source: HeyTony master playbook, Part IV Mobile and responsive design, 2026-07 (skills/skills/heyTony/reference/part-4-technical-and-internal-linking.md), local file
- Quote: "Google has done mobile-first indexing since ~2016; visually cut-off or non-reflowing mobile content is a direct negative regardless of desktop quality."
- Means: Test reflow separately from heading structure; a clean heading audit does not prove the page is responsive.
- Factor: mobile-usable | Evidence: D | Lever: ranking | Scope: organic local ai | Stage: both

## 2026-07 | A deleted sitemap took client traffic to zero

- Source: HeyTony master playbook, Part IV Sitemaps, 2026-07 (skills/skills/heyTony/reference/part-4-technical-and-internal-linking.md), local file
- Quote: "documented client case where a deleted sitemap dropped traffic "from hundreds of thousands to zero.""
- Means: Submit the sitemap once in Search Console and never hand-build or delete it; a dead reference left in robots.txt silently blocks discovery.
- Factor: sitemap-submitted | Evidence: C | Lever: ranking | Scope: organic | Stage: both

## 2026-07 | Speed is fixed after content and keywords, never before

- Source: HeyTony master playbook, Part IV Site Speed and Core Web Vitals, 2026-07 (skills/skills/heyTony/reference/part-4-technical-and-internal-linking.md), local file
- Quote: "You gotta fix your pages first and then you can look at page speed after that."
- Means: Speed is a tiebreaker between otherwise equal pages, so it comes after content and keyword targeting already match the competition.
- Factor: core-web-vitals | Evidence: D | Lever: ranking | Scope: organic | Stage: audit

## 2026-07 | Never block AI crawlers, fix crawl load with hosting and a firewall

- Source: HeyTony master playbook, Part V 7.4, 2026-07 (skills/skills/heyTony/reference/part-5-offpage-and-ai-search.md), local file
- Quote: "I firmly believe we should not be blocking AI from crawling our sites - how else are they going to recommend it?"
- Means: When bot volume crashes hosting, move to cloud or VPS hosting and add a web application firewall rather than blocking the agents that cite you.
- Factor: ai-crawler-allow | Evidence: D | Lever: ranking | Scope: ai | Stage: audit

## 2026-07 | A page more than three clicks from the homepage does not get indexed

- Source: HeyTony master playbook, Part IV Crawl Depth, Orphan Pages and Broken Links, 2026-07 (skills/skills/heyTony/reference/part-4-technical-and-internal-linking.md), local file
- Quote: "If I can't get to it from your homepage, Google's not going to index it."
- Means: Every page you want ranked sits within three clicks of the homepage; four or more is the danger zone because a human cannot find it either.
- Factor: crawl-depth | Evidence: D | Lever: ranking | Scope: organic | Stage: both

## 2026-07 | Change a URL only when it has no ranking, no traffic and no backlinks

- Source: HeyTony master playbook, Part IV Site Migrations, Redirects and URL Changes, 2026-07 (skills/skills/heyTony/reference/part-4-technical-and-internal-linking.md), local file
- Quote: "we do everything right and the traffic still just doesn't carry over the way it's supposed to"
- Means: A changed URL is a new page to Google. Check all three conditions first, and if you change it, 301 it and update every internal link.
- Factor: url-change-risk | Evidence: D | Lever: ranking | Scope: organic | Stage: audit

## 2026-07 | A domain change collapsed six years of rankings

- Source: HeyTony master playbook, Part IV Site Migrations, Redirects and URL Changes, 2026-07 (skills/skills/heyTony/reference/part-4-technical-and-internal-linking.md), local file
- Quote: "a January domain change collapsed six years of rankings"
- Means: Expect to lose rankings and link equity on a root domain change even after notifying Google. Domain forwarding homepage to homepage is the safe version.
- Factor: domain-change-risk | Evidence: C | Lever: ranking | Scope: organic | Stage: build

## 2026-07 | The meta keywords field is dead

- Source: HeyTony master playbook, Part IV Title Tags, Meta Descriptions and Open Graph, 2026-07 (skills/skills/heyTony/reference/part-4-technical-and-internal-linking.md), local file
- Quote: "Meta keywords field (flagged "missing" by some plugins): ignore completely, dead since the 90s."
- Means: Ignore any audit tool that flags a missing meta keywords tag. The field still exists in plugins, which is why the flag keeps appearing.
- Factor: meta-keywords | Evidence: D | Lever: ranking | Scope: organic | Stage: audit

## 2026-07 | llms.txt is auto-generated and has no confirmed ranking impact

- Source: HeyTony master playbook, Part V 7.8, 2026-07 (skills/skills/heyTony/reference/part-5-offpage-and-ai-search.md), local file
- Quote: "Not mandatory, no confirmed ranking impact yet, but low-effort and expected to matter more as agentic crawling grows."
- Means: Check whether the SEO plugin already generates one, then spend no further effort on it for Google Search specifically.
- Factor: llms-txt | Evidence: D | Lever: ranking | Scope: organic ai | Stage: build

## 2026-07 | Internal linking, not manual submission, is what gets a page indexed

- Source: HeyTony master playbook, Part IV Indexing and Google Search Console, 2026-07 (skills/skills/heyTony/reference/part-4-technical-and-internal-linking.md), local file
- Quote: "A page does not need a manual "request indexing" click for every edit; solid internal linking is what actually gets it crawled."
- Means: A properly internally linked page has indexed in about two hours; a brand-new site can take two to three weeks before Google crawls at all.
- Factor: indexable | Evidence: D | Lever: ranking | Scope: organic ai | Stage: both

## 2026-06 | Schema showed no measured lift, and non-ranking pages carried more of it

- Source: HeyTony Insiders, call 020, 2026-06 (insiders/transcripts/020_rank-week-day-5-replay.txt), local file. Filename carries no date; 2026-06 inferred from transcript order, call 019 is 2026-06-22
- Quote: "Doesn't matter... not worth the time."
- Means: Turn on the SEO plugin's automatic schema and skip a custom build; schema is only penalised when the data is wrong.
- Factor: schema-markup | Evidence: D | Lever: ranking | Scope: organic ai | Stage: both

## 2026-06-17 | 99 percent of 10,937 analysed pages were missing at least one schema type their competitors carry

- Source: Kyle Roof, PageOptimizer Pro, "Why Isn't My Content Ranking in Google and AI? We Analysed 10,937 SEO'd Pages", 2026-06-17, https://www.pageoptimizer.pro/blog/why-isnt-my-content-ranking-in-google-and-ai
- Quote: "Schema isn't advanced SEO anymore. It's table stakes - and 99% of pages in our study aren't at the table."
- Means: 45 percent of the 10,937 pages carried no schema at all and the average page was missing 10.4 recommended types, measured between 10 and 30 April 2026. Roof writes on the same page that schema is not a direct ranking factor, which agrees with the HeyTony no-lift entry; the value he claims is indexing, rich results and AI citation.
- Factor: schema-markup | Evidence: C | Lever: ranking | Scope: organic ai | Stage: both

## 2026-06-11 | The canonical must match the live URL exactly, trailing slash included

- Source: HeyTony Insiders, call 030, 2026-06 (insiders/page-types/00-rules-for-every-page.md, citing transcripts/030_techinical-seo-with-denroi-11-06-2026.txt), local file
- Quote: "The canonical tag must match the live, rendered URL exactly, including the trailing slash."
- Means: A "canonical not self-referencing" flag is very often only a trailing-slash mismatch, not a real defect.
- Factor: canonical-self-reference | Evidence: D | Lever: ranking | Scope: organic | Stage: audit
