# google | technical

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2025-12-18 | Search Essentials sets three technical requirements for indexing
- Source: Google Search Central, "Search Essentials, technical requirements", 2025-12-18, https://developers.google.com/search/docs/essentials/technical
- Quote: "The page works, meaning that Google receives an HTTP 200 (success) status code."
- Means: A page must return a 200 status, stay unblocked for Googlebot, and hold supported text content that does not violate spam policies before Google will consider indexing it. Meeting these does not guarantee indexing.
- Factor: indexable | Evidence: A | Lever: ranking | Scope: organic ai | Stage: both

## 2025-12-10 | Core Web Vitals are named as an input to Google's ranking systems
- Source: Google Search Central, "Understanding page experience in Google Search results", 2025-12-10 (page last updated), https://developers.google.com/search/docs/appearance/page-experience
- Quote: "Core Web Vitals are used by our ranking systems."
- Means: Core Web Vitals carry ranking weight in Google's own words. The same page adds that a good score does not guarantee a top position, so a slow page is a fix on the list rather than the reason a page does not rank.
- Factor: core-web-vitals | Evidence: A | Lever: ranking | Scope: organic | Stage: audit

## 2025-12-10 | Page experience aspects other than Core Web Vitals do not directly raise rankings
- Source: Google Search Central, "Understanding page experience in Google Search results", 2025-12-10 (page last updated), https://developers.google.com/search/docs/appearance/page-experience
- Quote: "Beyond Core Web Vitals, other page experience aspects don't directly help your website rank higher in search results."
- Means: Interstitials, ad load and layout clarity are user experience work with no direct ranking effect, by Google's own statement. Google says they can make a site more satisfying to use, which is the argument for them, not a ranking argument.
- Factor: core-web-vitals | Evidence: A | Lever: ranking | Scope: organic | Stage: audit

## 2025-12-10 | Mobile-first indexing ranks a page on its phone version, not its desktop one
- Source: Google Search Central, "Mobile-first indexing best practices", 2025-12-10, https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing
- Quote: "Google uses the mobile version of a site's content, crawled with the smartphone agent, for indexing and ranking. This is called mobile-first indexing."
- Means: If a page hides content, links, or structured data on its mobile version, Google ranks it on that reduced mobile version, not the fuller desktop one. A page has to reflow and stay complete on a phone to keep its ranking signals.
- Factor: mobile-usable | Evidence: A | Lever: ranking | Scope: organic local ai | Stage: both

## 2014-08-07 | HTTPS became a lightweight ranking signal
- Source: Google Search Central Blog, "HTTPS as a ranking signal", 2014-08-07, https://developers.google.com/search/blog/2014/08/https-as-ranking-signal
- Quote: "For now it's only a very lightweight signal, affecting fewer than 1% of global queries, and carrying less weight than other signals such as high-quality content, while we give webmasters time to switch to HTTPS."
- Means: HTTPS started in 2014 as a minor tiebreaker, not a hard requirement. Google said it might strengthen the signal over time, so a site still on HTTP is running against a signal Google has kept and reinforced since. The page renders the quoted sentence with dashes, replaced here with commas under the repo dash rule.
- Factor: https | Evidence: A | Lever: ranking | Scope: organic local ai | Stage: both
