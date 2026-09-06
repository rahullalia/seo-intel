# Existing site: the audit order

For a live site that needs diagnosing, walking the `audit` rows of `../factors/scorecard.md`. A site being planned or built goes to `new-site.md`; tools are in `tooling.md`.

## 1. Step 0: pull the data before diagnosing

1. Treat the stated premise as unverified. "Stuck at 12 to 16" bundles four claims: the page exists, it targets that keyword, the market is right, the position is real. Three can be wrong at once. [ids: indexable, one-keyword-per-page, position-one-ctr]
2. List the client folder before reading it, `brain.md`, `seo/` and `audits/`, because the export you are about to pull may already be on disk. [ids: indexable, ranking-page-freeze]
3. Pull GSC by query and by page, then compare the last 28 days against the prior 28. Tool: `tooling.md`, the audit order. [ids: indexable, position-one-ctr, zero-click-rate]
4. Average position blends every query the page appears for: one homepage reading 13.8 was almost entirely the founder's surname, 134 impressions at 14.5 with zero clicks. Split by query first. [ids: position-one-ctr]
5. Impressions falling while position holds means the query set narrowed, not that you dropped. A new post's raised impressions settle to baseline after 2 to 3 weeks, which is decay, not a penalty. Position 25 with 400 impressions and no clicks is a depth problem, not a title problem. [ids: content-freshness, position-one-ctr, keyword-in-title-front]
6. Query rows are sampled, so page totals exceed the listed queries. Never mix time windows in one claim, strip bot query series, then read the live top 3 for the exact keyword. [ids: zero-click-rate, word-count-competitor-relative]

## 2. Find work already done but not shipped

7. Before recommending a build, look for it already existing: unmerged branches, drafts, staged pages, planned URLs returning 404, sitemap entries on old paths. Finished work behind a merge is invisible from the live site and the cheapest win available. [ids: indexable, sitemap-submitted, url-change-risk]

## 3. The diagnosis order

8. Too early? A site under about a month does not rank, a page changed last week cannot be judged, and a content change needs 2 to 3 months. If it is too early, stop here. [ids: ranking-page-freeze, content-freshness]
9. Does a page for that exact keyword exist and is it indexed? If no page exists, that is the whole answer: build it. [ids: indexable, sitemap-submitted, crawl-depth]
10. Cannibalization: two pages on the same or near-same intent get consolidated to one, because Google ranks neither. [ids: one-keyword-per-page]
11. Competitive match: compare word count, depth, angle and page type against the top 3, matching the lowest-ranked of them plus 100 to 200 words. [ids: word-count-competitor-relative, keyword-density-over-optimization, single-h1, keyword-in-title-front]
12. Intent and page type, both directions: does the ranked set want a post, a service page or a collection page, and do you own the wrong type? [ids: one-keyword-per-page, location-pages]
13. Internal links, the fastest lever: does anything point at the page with relevant anchor text? Pages have reached number one on internal links alone. [ids: internal-linking-inbound, internal-link-anchor-text, crawl-depth]

## 4. The missing money page

14. Read the query-by-page report for transactional queries landing on blog URLs: demand already earned, pointed at a page that cannot convert it, with the impression count sizing the build. [ids: one-keyword-per-page, location-pages]
15. Do not delete or redirect the blog post that surfaced the gap, because it ranks. Link it into the new money page with anchor text naming the destination keyword. [ids: ranking-page-freeze, url-change-risk, internal-link-anchor-text]

## 5. What not to touch

16. Never edit a page ranking 1 to 3, or ranking at all, past a UX or CTA tweak, even at 122 keyword uses or duplicate H1s. The trigger to re-audit is the day it drops. [ids: ranking-page-freeze, keyword-density-over-optimization, single-h1]
17. Redesign scope follows ranking status: strong rankings mean preserve wording, keywords and URLs and restructure visually only; weak or no rankings mean free to rewrite. [ids: ranking-page-freeze, url-change-risk, keyword-in-title-front]
18. A page that does not rank waits 3 months, then 6, taking internal links and small additions meanwhile, not surgery. [ids: internal-linking-inbound, ranking-page-freeze]

## 6. Technical and speed last

19. Fix order: broken links and missing or duplicate H1s, titles and metas first, heading structure next, speed and schema last. [ids: single-h1, keyword-in-title-front, schema-markup, core-web-vitals]
20. 80 percent on a page audit and 90 percent site health are fine; chasing the last flags wastes time and can create cannibalization. Fix 5 to 10 issues per week, never the whole report at once, changing one variable per page. [ids: core-web-vitals, one-keyword-per-page, schema-markup]
21. Confirm the canonical matches the rendered URL exactly including the trailing slash, the sitemap was submitted once, and no AI crawler is blanket-blocked. [ids: canonical-self-reference, sitemap-submitted, ai-crawler-allow]
22. Spend nothing on llms.txt, the meta keywords tag, or a disavow file built from a toxic-link tool. [ids: llms-txt, meta-keywords, disavow-links]

## 7. Local branch: the GBP field audit

23. Work the order of leverage in `local/README.md`, top down. Primary category first, read against the top 3 pack competitors: factor 1 of 187 (Whitespark 2026). [ids: gbp-primary-category]
24. Reviews second: velocity, recency, count of reviews carrying text, rating and owner replies inside 48 hours, measured against the pack competitors. [ids: review-velocity, review-recency, review-count, review-rating, review-photos]
25. Services third and fastest to move: every predefined service plus custom keyword names, which went from factor 110 to 35 year over year. [ids: gbp-services-keywords, gbp-predefined-services]
26. Then address reality and proximity, then location pages and a crawlable NAP footer, on-page 19 percent and links 15 percent of the pack model, then hours, attributes and real photos, which Ask Maps reads live. [ids: proximity, address-visible-storefront, sab-address-hidden, location-pages, nap-footer-crawlable, gbp-hours-accuracy, gbp-photos-original, ask-maps-completeness]
27. Then one 25 to 40 citation build on exact-match NAP, then posts and photos as the engagement layer at factors 148 and 168 of 187. [ids: citation-count-25-40, citation-nap-consistency, core-five-citations, niche-directories, gbp-posts]
28. Flag the suspension risks before anything else moves: a keyword-stuffed name, rapid core-field edits, a P.O. box or virtual office address, review gating and review incentives. [ids: gbp-name-policy-risk, gbp-business-name-keywords, rapid-core-field-edits, fake-address-listing, review-gating, review-incentives]
29. Rebuild nothing dead and geotag nothing: GBP Q&A went off the API on 2025-11-03, messaging ended July 2024, and Google strips EXIF on upload. [ids: gbp-qa, gbp-messaging, photo-geotagging]

## 8. Programmatic and thin-page audit

30. Count indexed URLs against the pages that actually earn impressions. Index bloat is templated pages Google crawls and nobody searches. [ids: programmatic, pending]
31. Flag templated pages carrying no data unique to that page, and any services times cities matrix, as doorway patterns. [ids: programmatic, pending]
32. Separately, check the publishing record for a volume spike on an established site and for posts outside the site's established topic. [ids: publishing-velocity-spike, topical-mismatch]

## 9. How to report month 1, 3, 6

33. Month 1: indexed pages and impressions, never rankings, which teach the client to watch the wrong number for a year. [ids: indexable, sitemap-submitted]
34. Month 3: impressions trend, query-set growth, first position movement, still not leads. Month 6 and after: clicks, then leads, against the promise made at kickoff. [ids: position-one-ctr, content-freshness, zero-click-rate, ai-referral-conversion]
35. On a flat quarter lead with what was built and what is moving underneath, and pre-empt fresh-content decay. AI citations are not clicks, so give both numbers in one sentence. [ids: content-freshness, aio-cited-click-lift, ai-referral-conversion]
36. Local reporting runs to the day 30, 60 and 90 gates in `local/sop.md`. No forecast is quoted without a source, and no vendor has privileged algorithm access. [ids: proximity, review-velocity, google-partner-algorithm-access]

Curated by hand. The evidence behind every id above lives in `../factors/scorecard.md`.
