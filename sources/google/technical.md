# google | technical

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2025-12-18 | Search Essentials sets three technical requirements for indexing
- Source: Google Search Central, "Search Essentials, technical requirements", 2025-12-18, https://developers.google.com/search/docs/essentials/technical
- Quote: "The page works, meaning that Google receives an HTTP 200 (success) status code."
- Means: A page must return a 200 status, stay unblocked for Googlebot, and hold supported text content that does not violate spam policies before Google will consider indexing it. Meeting these does not guarantee indexing.
- Factor: indexable | Evidence: A | Lever: ranking | Scope: organic ai | Stage: both

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
