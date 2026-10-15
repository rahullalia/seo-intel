# google | signals

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2026-10-08 | Google documents a separate ingestion pipeline for trending user generated content, open to approved platforms only
- Source: Google Search Central, "About the UGC Fresh Data Program", 2026-10-08, https://developers.google.com/search/docs/appearance/ugc-fresh-data-program
- Quote: "The UGC Fresh Data Program is a specialized pipeline designed exclusively for trending UGC content."
- Means: The page was added on 2026-10-08 per Google's documentation updates log, and it limits participation to "platforms that meet specific content quality and volume guidelines" while stating that the program "doesn't guarantee that content will appear in Search". A client who posts on a forum is not a participant in this program, so the page confirms the pipeline exists and claims no ranking benefit for a business present on those platforms.
- Factor: ugc-platform-presence | Evidence: A | Lever: ranking | Scope: organic ai | Stage: build

## 2026-10-08 | The September 2026 spam update finished its rollout in 13 days, 16 hours
- Source: Google Search Status Dashboard, "September 2026 spam update", 2026-10-08, https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu
- Source: Google Search Status Dashboard, "Ranking updates", 2026-10-15 (no page date), https://status.search.google.com/summary
- Quote: "The rollout was complete as of October 8, 2026."
- Means: The incident page records the rollout as beginning 2026-09-24 09:15 and ending 2026-10-08 01:00 US/Pacific, so ranking movement on a client site after that time is not this update. The dashboard prints the duration as 13 days, 16 hours, against 2 days, 16 hours for the August 2026 spam update and 2 days, 1 hour for the June 2026 spam update.
- Factor: scaled-content-abuse | Evidence: A | Lever: trust | Scope: organic | Stage: audit

## 2026-09-24 | Google released a September 2026 spam update, global and all languages
- Source: Google Search Status Dashboard, "September 2026 spam update", 2026-09-24, https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu
- Quote: "Released the September 2026 spam update, which applies globally and to all languages. The rollout may take up to two weeks to complete."
- Means: Ranking movement on a client site between 2026-09-24 and roughly 2026-10-08 can be attributed to a confirmed Google update rather than an unconfirmed one. A spam update enforces the spam policies, so pages generated at scale are the first thing to check.
- Factor: scaled-content-abuse | Evidence: A | Lever: trust | Scope: organic | Stage: audit

## 2026-06-05 | Google says no one can guarantee a number one ranking
- Source: Google Search Central, "Do You Need an SEO? Tips for Hiring an SEO", 2026-06-05, https://developers.google.com/search/docs/fundamentals/do-i-need-seo
- Quote: "No one can guarantee a #1 ranking on Google."
- Means: Any vendor claiming special access to the ranking algorithm is contradicted by Google's own guidance. The only partner program Google runs is for Ads, not organic ranking.
- Factor: google-partner-algorithm-access | Evidence: A | Lever: trust | Scope: organic local | Stage: both
