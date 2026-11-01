# google | programmatic

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2026-10-26 | Google names open comment forms and user generated content inputs as spam targets
- Source: Google Search Central, "Preventing user-generated spam", 2026-10-26 (Last updated), https://developers.google.com/search/docs/monitor-debug/prevent-abuse
- Source: Google Search Central, "Search Central documentation updates", 2026-10-26, https://developers.google.com/search/updates
- Quote: "Spammers often take advantage of open comment forms and other user generated content inputs."
- Means: The page, updated 2026-10-26, asks site owners to apply a noindex rule or a robots.txt block by default to pages built for sharing, collaboration or utility rather than search, and to verify the site in Search Console for email alerts on a manual action. A client site with open comments, user profiles or shared link pages carries a spam-policy exposure that moderation and a default noindex close off.
- Factor: user-generated-spam | Evidence: A | Lever: trust | Scope: organic | Stage: audit

## 2026-08-28 | Scaled content abuse targets mass page generation built to manipulate rankings
- Source: Google Search Central, "Spam policies for Google web search", 2026-08-28, https://developers.google.com/search/docs/essentials/spam-policies
- Quote: "Scaled content abuse is when many pages are generated for the primary purpose of manipulating search rankings and not helping users."
- Means: A programmatic template that spins out city or service pages with no real per-page difference matches this definition regardless of whether the text came from AI or a person. The policy applies to the practice, not the production method.
- Factor: scaled-content-abuse | Evidence: A | Lever: trust | Scope: organic ai | Stage: both

## 2026-08-28 | Doorway pages are query-bait pages that lead to a weaker final destination
- Source: Google Search Central, "Spam policies for Google web search", 2026-08-28, https://developers.google.com/search/docs/essentials/spam-policies
- Quote: "Doorway abuse is when sites or pages are created to rank for specific, similar search queries. They lead users to intermediate pages that aren't as useful as the final destination."
- Means: A location or service page matrix built only to catch search queries, then funnel visitors to one generic page, matches Google's own definition of a doorway rather than a legitimate location page.
- Factor: doorway-pages | Evidence: A | Lever: trust | Scope: organic ai | Stage: both

## 2026-08-28 | Site reputation abuse covers third-party content riding a host's earned authority
- Source: Google Search Central, "Spam policies for Google web search", 2026-08-28, https://developers.google.com/search/docs/essentials/spam-policies
- Quote: "The site reputation policy applies where third-party content is published on a host site mainly because of that host's already-established ranking signals, which it has earned primarily from its first-party content."
- Means: Renting space on a high-authority domain for unrelated third-party content, coupon pages, or white-label sections is a named policy violation, not just a weak page. Google can act on the section or the whole host.
- Factor: site-reputation-abuse | Evidence: A | Lever: trust | Scope: organic ai | Stage: both
