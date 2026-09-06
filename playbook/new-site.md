# New site: the build order

For a site being planned or built. It walks the `build` rows of `../factors/scorecard.md` in the order the decisions get made; a live site goes to `existing-site-audit.md`, and tools are in `tooling.md`.

## 1. Confirm it is truly from zero

1. Get the domain registration date, prior site and prior URLs before planning a page. An aged domain, rebuild or relaunch on new URLs is a migration, not a build. [ids: domain-change-risk, url-change-risk]
2. If history exists, list every URL with impressions in Search Console, which backfills about 16 months. Tool: `tooling.md`. [ids: indexable, url-change-risk]
3. A migration keeps URLs and headings identical, uses one-hop 301s, and leaves no URL with impressions on a 404. Change a URL only when the page has no ranking, no traffic and no backlinks. [ids: url-change-risk, ranking-page-freeze]

## 2. Measurement in week zero

4. Verify the GSC property, submit the XML sitemap once, and verify Bing Webmaster Tools, since 87 percent of ChatGPT citations match a page in the Bing top 20 (Zyppy, February 2026). Serve static HTML, not client-side JavaScript. [ids: sitemap-submitted, indexable, bing-indexing, static-html-rendering]
5. Create GA4 with conversion events, set event retention to 14 months off the 2-month default, split call tracking pools for organic and the profile, and write one canonical NAP string. [ids: ai-referral-conversion, citation-nap-consistency, nap-footer-crawlable]

## 3. Architecture that is expensive to change later

6. One keyword per page, always. Word-order and plural variants are the same keyword; a second keyword means a second page. [ids: one-keyword-per-page]
7. URLs stay hierarchical and plain (`/services/website-design`), keyword in every slug but the home page, no year, no "near me", every ranked page within three clicks of home. [ids: url-change-risk, crawl-depth]
8. The platform does not decide ranking ability, but Wix, Squarespace, Shopify and GoHighLevel each cap speed, headings or image formats. Run one SEO plugin, never two. [ids: static-html-rendering, mobile-usable, keyword-in-title-front]
9. Do not build the services times cities matrix. Home base plus satellites, one service each, smaller surrounding towns first. [ids: location-pages, one-keyword-per-page, topical-mismatch]
10. Templated pages at scale only where each carries data no other page has. A city page with the name swapped in is a doorway pattern. [ids: programmatic-templates-unique-data, programmatic-api-value-freshness, doorway-pages, scaled-content-abuse]

## 4. Google Business Profile in parallel from week one, when local

11. Claim and verify in week one: the only asset that can produce a lead inside 30 days, able to outrank fully built competitors in the map pack. [ids: gbp-verified, proximity]
12. Decide storefront, service-area or hybrid honestly and match the address config; faking the type is the second most common suspension cause. Use the exact real-world name, nothing appended. [ids: address-visible-storefront, sab-address-hidden, fake-address-listing, gbp-name-policy-risk, gbp-business-name-keywords]
13. Primary category is the most specific match to the money service, factor 1 of 187 (Whitespark 2026), read off the top 3 pack competitors. Add every predefined service plus custom ones under searched names; Sterling Sky measured movement in 24 to 72 hours. [ids: gbp-primary-category, gbp-predefined-services, gbp-services-keywords]
14. Review velocity starts week one: unfiltered link, replies inside 48 hours, no gating, no incentives. Google's April 2026 policy can strip every review, and FTC 16 CFR 465 runs to $53,088 per violation. [ids: review-velocity, review-recency, review-count, review-gating, review-incentives]
15. Load 8 to 12 real original photos, no stock and no EXIF geotags, then fill hours, attributes and the 750-character description, first 250 front-loaded, which Ask Maps reads live. Edit core fields one at a time after that. [ids: gbp-photos-original, photo-geotagging, gbp-hours-accuracy, ask-maps-completeness, rapid-core-field-edits]

## 5. Copy first, then design

16. Copy before layout: the layout carries the message, every H2 gets its own section, and the differentiator is first-person experience with real numbers and named sources. [ids: answer-first-structure, whitespace-section-rhythm, experience-first-person, information-gain, cite-sources-in-content, unedited-ai-output, eeat]
17. One H1 first in DOM order with the exact keyword, keyword at the front of a 50 to 60 character title, word count at the lowest of the top 3 plus 100 to 200 words, density at their count plus one or two. Tool: `tooling.md`. [ids: single-h1, keyword-in-title-front, word-count-competitor-relative, keyword-density-over-optimization]
18. Answer at the top in plain words, grade 6 to 8 reading level, FAQs capped at 3 or 4 as plain question and answer text. [ids: answer-first-structure, readability-grade-6-8, faq-block-plain-text, answer-passage-length]
19. Four design decisions damage ranking or extraction: a carousel hero, answer content behind an accordion, a duplicated desktop and mobile block, and a heading baked into an image. [ids: hero-carousel, hidden-accordion-content, single-h1, mobile-usable]
20. No ranking weight, still decisive: one primary CTA, tap-to-call in thumb reach, 16px body at 1.8 line height, soft dark gray on near white, real photos over stock, alt text of 5 or 6 words. [ids: single-primary-cta, tap-to-call, body-font-size, text-contrast, real-team-photos, alt-text, accessibility-baseline]

## 6. Money pages before blog posts

21. Home plus one page per service you sell, one keyword each, city level for local. No page, no ranking for that keyword. [ids: location-pages, one-keyword-per-page]
22. Then the launch batch: 5 to 6 posts at once, or 10 at launch dripping 2 per week. The exception expires at about 2 months old; 1 to 2 per week after. [ids: publishing-velocity-spike, content-freshness]
23. Every publish links out to 3 to 5 pages including one money page, then 3 older indexed pages link in, anchor text naming the destination keyword and varied across the three. [ids: internal-linking-inbound, internal-link-anchor-text, crawl-depth]

## 7. What waits

24. Backlinks, citations and directories wait until the pages exist. Then one owned citation build in order (core five, US aggregators, second tier, 5 to 10 niche), stopping at 25 to 40; never rented sync, since about 60 percent of listings degrade within 60 days of cancelling. [ids: referring-domains, press-release-links, chamber-sponsorship-links, core-five-citations, data-aggregators, niche-directories, citation-count-25-40, rented-citations]
25. Never audit a site still under construction, and fix speed after content and keywords match the top 3. Cap delivery at 2 posts per week plus 4 backlinks per month with link budget, or 1 post plus 2 location pages without. [ids: core-web-vitals, publishing-velocity-spike, location-pages]

## 8. The patience windows to tell the client

26. A brand-new site takes 2 to 3 weeks to about 2 months before the first crawl, and zero movement in that window is normal. After any edit leave the page alone about a month. [ids: indexable, ranking-page-freeze]
27. A new post gets a burst of impressions for 2 to 3 weeks, then halves in a day while position holds, so pre-empt it. Judge a title or H1 nudge at 2 weeks to 1 month, a rewrite at 2 to 3 months, first real movement at 3 to 6 months. [ids: content-freshness, internal-linking-inbound]
28. Local gates land at day 30, 60 and 90, detailed in `local/sop.md`. Seasonal businesses publish 3 to 4 months ahead, no forecast is quoted without a source, and no vendor has privileged algorithm access. [ids: gbp-verified, review-velocity, proximity, google-partner-algorithm-access]

Curated by hand. The evidence behind every id above lives in `../factors/scorecard.md`.
