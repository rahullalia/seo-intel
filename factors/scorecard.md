# Scorecard

One row per factor, 116 rows across nine categories, bootstrapped 2026-09-06 from 142 dated entries in `sources/` after the QA pass of the same date. Tier and evidence follow `pipeline/rubric.md`; evidence is the best grade an entry in `sources/` actually carries, never the grade the claim might deserve. Sources are entry anchors written `tier/category YYYY-MM-DD`, matching the entry heading in `sources/<tier>/<category>.md`; `seed: <doc>` means the row's only support is a seed document and no entry exists yet. Last verified is the newest entry date supporting the row, or the seed document's date when only a seed document supports it. Sorted by category in build order, then tier, then evidence grade.


| id | Factor | Category | Scope | Lever | Stage | Tier | Evidence | Last verified | Sources |
|---|---|---|---|---|---|---|---|---|---|
| https | HTTPS served sitewide | technical | organic local ai | ranking | both | Required | A | 2026-07 | google/technical 2014-08-07; creators/technical 2026-07 |
| mobile-usable | Page reflows and stays readable on a phone under mobile-first indexing | technical | organic local ai | ranking | both | Required | A | 2026-07 | google/technical 2025-12-10; creators/technical 2026-07 |
| indexable | Page indexed, not blocked, reachable by the crawler | technical | organic ai | ranking | both | Required | A | 2026-07 | google/technical 2025-12-18; creators/technical 2026-07 |
| sitemap-submitted | XML sitemap submitted once inside Search Console | technical | organic | ranking | both | Supporting | C | 2026-07 | creators/technical 2026-07 |
| domain-change-risk | Moving an established site to a new root domain | technical | organic | ranking | build | Supporting | C | 2026-07 | creators/technical 2026-07 |
| schema-markup | Structured data beyond the SEO plugin default | technical | organic ai | ranking | both | Minor | C | 2026-06 | experts/technical 2026-01-09; creators/technical 2026-06 |
| bing-indexing | Site verified and indexed in Bing Webmaster Tools | technical | ai | ranking | build | Minor | D | 2026-05 | seed: playbook/ai-search.md |
| faq-schema | FAQPage structured data on a page with question and answer pairs | technical | ai organic | ranking | build | Minor | D | 2026-05 | seed: playbook/ai-search.md |
| static-html-rendering | Static HTML or server rendering rather than client-side JavaScript | technical | ai | ranking | build | Minor | D | 2026-05 | seed: playbook/ai-search.md |
| canonical-self-reference | Canonical tag matching the live rendered URL exactly, trailing slash included | technical | organic | ranking | audit | Minor | D | 2026-06-11 | creators/technical 2026-06-11 |
| core-web-vitals | Core Web Vitals and load speed as a tiebreaker between equal pages | technical | organic | ranking | audit | Minor | D | 2026-07 | creators/technical 2026-07 |
| ai-crawler-allow | Retrieval agents allowed through robots.txt and the firewall | technical | ai | ranking | both | Minor | D | 2026-07 | experts/technical 2026-01-21; creators/technical 2026-07 |
| crawl-depth | Every page you want ranked within three clicks of the homepage | technical | organic | ranking | both | Minor | D | 2026-07 | creators/technical 2026-07 |
| url-change-risk | Changing the URL of a page that ranks, has traffic, or has backlinks | technical | organic | ranking | both | Minor | D | 2026-07 | creators/technical 2026-07 |
| llms-txt | An llms.txt file at the site root | technical | organic ai | ranking | build | Myth | B | 2026-07 | experts/technical 2026-06-15; creators/technical 2026-07 |
| meta-keywords | The meta keywords tag | technical | organic | ranking | audit | Myth | D | 2026-07 | creators/technical 2026-07 |
| content-freshness | Content updated within the last two months | content | organic ai | ranking | both | Core | B | 2025-12-15 | experts/content 2025-12-15 |
| cite-sources-in-content | Named, verifiable citations attached to the claims on the page | content | ai | ranking | build | Core | B | 2024-06-28 | experts/content 2024-06-28 |
| information-gain | Novel, non-redundant information relative to other pages on the query | content | organic | ranking | both | Supporting | A | 2025-12-10 | google/content 2025-12-10; google/content 2024-03-05; creators/content 2024-02-05 |
| readability-grade-6-8 | Reading level at Flesch-Kincaid grade 6 to 8 | content | organic ai | ranking | build | Supporting | B | 2026-07 | experts/content 2025-12-15; creators/content 2026-07 |
| faq-block-plain-text | FAQ answers as plain question and answer text, capped at three or four | content | organic ai | ranking | build | Supporting | B | 2026-07 | experts/content 2025-12-15; creators/content 2026-07 |
| one-keyword-per-page | One target keyword per page, no page sharing a keyword with another | content | organic | ranking | both | Supporting | C | 2026-01-15 | creators/content 2026-01-15 |
| ranking-page-freeze | Editing the content or structure of a page that already ranks | content | organic | ranking | both | Supporting | C | 2026-07 | creators/content 2026-07 |
| single-h1 | Exactly one H1, first heading in DOM order, carrying the exact keyword | content | organic | ranking | both | Supporting | C | 2026-07 | creators/content 2026-07; creators/content 2026-07-09 |
| word-count-competitor-relative | Word count matched to the top three results plus about ten percent | content | organic | ranking | both | Supporting | C | 2026-07-20 | creators/content 2026-07-20 |
| keyword-density-over-optimization | Keyword density meaningfully higher than the ranking competitors | content | organic | ranking | both | Supporting | C | 2026-07 | creators/content 2026-07 |
| unedited-ai-output | Publishing unreviewed AI output without expert oversight | content | organic | ranking | both | Supporting | C | 2026-07 | creators/content 2026-07 |
| experience-first-person | First-person accounts, real outcomes and practitioner authorship | content | organic | ranking | build | Minor | D | 2026-05 | seed: playbook/core-updates.md |
| multi-modal-content | Images, diagrams, tables and video alongside the text | content | ai | ranking | build | Minor | D | 2026-05 | seed: playbook/ai-search.md |
| answer-first-structure | The direct answer stated at the top of the page, before context | content | organic ai | ranking | both | Minor | D | 2026-07 | creators/content 2026-07 |
| eeat | Experience, Expertise, Authoritativeness and Trustworthiness signals | content | organic | trust | build | Minor | D | 2026-05 | seed: playbook/core-updates.md |
| answer-passage-length | Self-contained answer passages of 134 to 167 words | content | ai | ranking | build | Minor | D | 2026-05 | seed: playbook/ai-search.md |
| keyword-in-title-front | Focus keyword at or near the front of the title tag | content | organic | ranking | both | Minor | D | 2026-07 | creators/content 2026-07 |
| hidden-accordion-content | Important answer content hidden behind an accordion, toggle or dropdown | content | organic ai | ranking | both | Minor | D | 2026-06-25 | creators/content 2026-06-25; creators/content 2025-12-19 |
| alt-text | Descriptive alt text on every image, screen reader first | content | organic | trust | build | Minor | D | 2025-11 | creators/content 2025-11 |
| ai-generated-content | Content penalised for being produced with AI rather than for quality | content | organic | ranking | both | Myth | B | 2026-07 | experts/content 2025-07-08; creators/content 2026-07 |
| keyword-stuffing-ai | Repeating the target phrase to win generative engine citation | content | ai | ranking | build | Myth | B | 2024-06-28 | experts/content 2024-06-28 |
| hero-carousel | Auto-rotating hero slider or carousel | website-design | organic | conversion | build | Minor | D | 2026-07 | creators/website-design 2026-07 |
| single-primary-cta | One primary CTA per page, secondary actions receding | website-design | organic | conversion | build | Minor | D | 2026-07 | creators/website-design 2026-07 |
| tap-to-call | Clickable tap-to-call number within thumb reach on mobile | website-design | local organic | conversion | both | Minor | D | 2026-07 | creators/website-design 2026-07 |
| body-font-size | Body text 16px minimum, about 1.8 line height | website-design | organic | conversion | build | Minor | D | 2026-07-08 | creators/website-design 2026-07-08 |
| text-contrast | Soft dark gray on near white, never pure black on pure white | website-design | organic | conversion | build | Minor | D | 2026-05-13 | creators/website-design 2026-05-13 |
| whitespace-section-rhythm | Deliberate whitespace and alternating section rhythm | website-design | organic | conversion | build | Minor | D | 2026-04-15 | creators/website-design 2026-04-15 |
| real-team-photos | Real photos of the actual team rather than stock or AI images | website-design | organic | trust | build | Minor | D | 2026-07 | creators/website-design 2026-07 |
| review-carousel-plugin | Review carousel plugin on a money page | website-design | organic | conversion | both | Minor | D | 2026-07 | creators/website-design 2026-07 |
| accessibility-baseline | Real headings, live text, alt text and contrast for screen readers | website-design | organic | trust | both | Minor | D | 2026-07-16 | creators/website-design 2026-07-16 |
| gbp-verified | A verified Google Business Profile | local-gbp | local | ranking | both | Required | A | 2026-09-06 | google/local-gbp 2026-09-06 |
| gbp-name-policy-risk | Keyword-stuffed GBP name as a suspension and redressal risk | local-gbp | local | trust | both | Required | A | 2026-09-06 | google/local-gbp 2026-09-06 |
| review-gating | Sentiment pre-screening before the review ask | local-gbp | local | trust | both | Required | A | 2026-09-06 | google/local-gbp 2026-09-06; creators/local-gbp 2026-07 |
| review-incentives | Payment, discounts, freebies or contest entries offered for a review | local-gbp | local | trust | both | Required | A | 2026-09-06 | google/local-gbp 2026-09-06; creators/local-gbp 2026-07 |
| sab-address-hidden | Address hidden on a service-area business that does not serve customers on site | local-gbp | local | trust | both | Required | A | 2026-09-06 | google/local-gbp 2026-09-06 |
| gbp-hours-accuracy | Accurate hours including holidays, open at time of search | local-gbp | local | ranking | both | Core | A | 2026-09-06 | google/local-gbp 2026-09-06; experts/local-gbp 2025-11-06 |
| review-velocity | Sustained review influx over time rather than bursts | local-gbp | local | ranking | both | Core | A | 2026-07 | google/local-gbp 2026-04-16; experts/local-gbp 2025-11-06; creators/local-gbp 2026-07 |
| proximity | Distance from the searcher to the verified address | local-gbp | local | ranking | both | Core | A | 2026-09-06 | google/local-gbp 2026-09-06; experts/local-gbp 2025-11-06 |
| gbp-primary-category | The single most specific primary category matching the money service | local-gbp | local | ranking | both | Core | B | 2025-11-06 | experts/local-gbp 2025-11-06 |
| gbp-services-keywords | Keywords in the GBP services field | local-gbp | local | ranking | both | Core | B | 2026-02-27 | experts/local-gbp 2026-02-27; experts/local-gbp 2025-11-06; experts/local-gbp 2024-01-24 |
| gbp-predefined-services | Every predefined service Google offers for the category, added | local-gbp | local | ranking | both | Core | B | 2025-11-06 | experts/local-gbp 2025-11-06 |
| gbp-business-name-keywords | Service or city keywords in the GBP business name | local-gbp | local | ranking | both | Core | B | 2025-11-06 | experts/local-gbp 2025-11-06 |
| review-count | Count of reviews carrying text | local-gbp | local | ranking | both | Core | B | 2025-11-06 | experts/local-gbp 2025-11-06 |
| review-rating | High average star rating | local-gbp | local ai | ranking | audit | Core | B | 2026-07 | experts/local-gbp 2025-11-06; creators/local-gbp 2026-07 |
| review-recency | How recently the newest reviews arrived | local-gbp | local | ranking | both | Core | B | 2025-11-06 | experts/local-gbp 2025-11-06 |
| address-visible-storefront | A visible physical address in the searched city | local-gbp | local | ranking | both | Core | B | 2025-11-06 | experts/local-gbp 2025-11-06 |
| rapid-core-field-edits | Rapid edits to name, address, category or hours in quick succession | local-gbp | local | trust | both | Supporting | A | 2026-09-06 | google/local-gbp 2026-09-06; experts/local-gbp 2026-03-10 |
| gbp-photos-original | Real, original photos on the profile, never stock | local-gbp | local | ranking | both | Supporting | B | 2025-11-06 | experts/local-gbp 2025-11-06 |
| review-photos | Reviews that carry customer photos | local-gbp | local | ranking | audit | Supporting | B | 2025-11-06 | experts/local-gbp 2025-11-06 |
| gbp-posts | Google post frequency and quantity | local-gbp | local | conversion | both | Minor | B | 2026-07 | experts/local-gbp 2025-11-06; creators/local-gbp 2026-07 |
| fake-address-listing | A listing at a P.O. box, virtual office or unstaffed coworking desk | local-gbp | local | trust | both | Minor | D | 2026-08-31 | seed: playbook/local/donts.md |
| ask-maps-completeness | Profile field completeness as Ask Maps source material | local-gbp | local ai | conversion | both | Minor | D | 2026-07 | creators/local-gbp 2026-07 |
| nap-footer-crawlable | Crawlable NAP in the site footer linked to the profile | local-gbp | local | ranking | both | Minor | D | 2026-07 | creators/local-gbp 2026-07 |
| photo-geotagging | EXIF geotag injected into photos before upload | local-gbp | local | ranking | both | Myth | C | 2026-07 | experts/local-gbp 2025-03-25; experts/local-gbp 2024-01-15; creators/local-gbp 2026-07 |
| gbp-qa | Google Business Profile Q&A | local-gbp | local | conversion | audit | Dead | A | 2026-08-28 | google/local-gbp 2026-08-28 |
| gbp-messaging | GBP messaging, chat and call history | local-gbp | local | conversion | audit | Dead | D | 2026-08-31 | seed: playbook/local/gbp-playbook.md |
| unstructured-mentions | Mentions in articles, best-of roundups, local press and association pages | citations | local ai | ranking | audit | Core | B | 2026-06-26 | experts/citations 2026-06-26; experts/citations 2025-11-06 |
| citation-nap-consistency | Exact-match name, phone, city, ZIP and URL across every listing | citations | local | ranking | both | Supporting | B | 2026-07 | experts/citations 2025-11-06; creators/citations 2026-07 |
| niche-directories | Industry specific and topically relevant directories | citations | local ai | ranking | both | Supporting | B | 2026-07 | experts/citations 2018-09-07; creators/citations 2026-07 |
| rented-citations | Subscription sync listings that stop when the subscription stops | citations | local | ranking | both | Minor | C | 2026-07 | experts/citations 2024-10-28; creators/citations 2026-07 |
| citation-count-25-40 | Twenty five to forty city and industry relevant citations, then stop | citations | local | ranking | both | Minor | D | 2026-08-31 | seed: playbook/local/citations.md |
| core-five-citations | Google, Apple Business Connect, Bing Places, Facebook and Yelp claimed | citations | local | ranking | both | Minor | D | 2026-07 | creators/citations 2026-07 |
| data-aggregators | Data Axle, Foursquare and TransUnion Digital Business Profile | citations | local | ranking | build | Minor | D | 2026-08-31 | seed: playbook/local/citations.md |
| citation-blast | Mass identical-NAP submission to hundreds of junk directories | citations | local | ranking | both | Minor | D | 2026-08-31 | seed: playbook/local/citations.md |
| referring-domains | Count of unique referring domains rather than raw backlink count | backlinks | organic ai | ranking | both | Supporting | C | 2026-07 | creators/backlinks 2026-07 |
| backlink-anchor-relevance | Descriptive, geo-qualified anchor text on an earned external link | backlinks | organic | ranking | build | Supporting | C | 2026-07 | creators/backlinks 2026-07 |
| chamber-sponsorship-links | Chamber of commerce membership and local sponsorship links | backlinks | local organic | ranking | build | Supporting | C | 2026-07 | creators/backlinks 2026-07 |
| press-release-links | Paid press release distribution for links and AI answer citation | backlinks | organic ai | ranking | both | Supporting | C | 2026-07 | creators/backlinks 2026-07 |
| internal-linking-inbound | Three older indexed pages linking into each new page | backlinks | organic | ranking | both | Supporting | C | 2026-07 | creators/backlinks 2026-07 |
| internal-link-anchor-text | Internal anchor text naming the destination and its keyword | backlinks | organic | ranking | both | Supporting | C | 2026-07 | creators/backlinks 2026-07 |
| reciprocal-links | Direct reciprocal link swaps and friend-group link networks | backlinks | organic | ranking | both | Minor | D | 2026-07 | creators/backlinks 2026-07 |
| page-level-links | Links pointed at the exact page you want ranked | backlinks | organic | ranking | audit | Minor | D | 2026-07 | creators/backlinks 2026-07 |
| disavow-links | Disavowing backlinks flagged as toxic by an audit tool | backlinks | organic | ranking | audit | Minor | D | 2026-07 | creators/backlinks 2026-07 |
| aio-outside-top-10 | AI Overview citation for pages that do not rank in the organic top ten | ai-search | ai | ranking | audit | Core | B | 2026-07 | experts/ai-search 2026-03-02; creators/ai-search 2026-07 |
| ai-mode-domain-traffic | Site-level traffic volume as an AI Mode citation driver | ai-search | ai | ranking | audit | Core | B | 2025-12-15 | experts/ai-search 2025-12-15 |
| zero-click-rate | Share of Google searches that end without a click | ai-search | organic ai | conversion | audit | Core | B | 2026-06-09 | experts/ai-search 2026-06-09; experts/ai-search 2024-07-02 |
| ai-overview-claim-alignment | Stating the AI Overview's own claim first, then pivoting to your data | ai-search | ai | ranking | build | Supporting | C | 2026-07 | creators/ai-search 2026-07 |
| aio-citation-instability | Stability of AI Overview citation across repeated identical searches | ai-search | ai | ranking | audit | Supporting | C | 2026-07 | creators/ai-search 2026-07 |
| aio-cited-click-lift | Click lift for a site cited inside an AI Overview | ai-search | ai | conversion | audit | Minor | D | 2026-05 | seed: playbook/ai-search.md |
| aio-citation-answer-first | A semantically complete answer passage that earns an AI Overview citation | ai-search | ai | ranking | build | Minor | D | 2026-07 | creators/ai-search 2026-07 |
| perplexity-bluf | Bottom Line Up Front structure with clear heading hierarchy | ai-search | ai | ranking | build | Minor | D | 2026-05 | seed: playbook/ai-search.md |
| ai-referral-conversion | Conversion rate of visitors arriving from an AI generated answer | ai-search | ai | conversion | both | Minor | D | 2026-07-28 | experts/ai-search 2026-07-28; creators/ai-search 2026-07 |
| domain-authority-aio | Domain Authority as a predictor of AI Overview citation | ai-search | ai | ranking | audit | Myth | D | 2026-05 | seed: playbook/ai-search.md |
| position-one-ctr | Position one organic click-through rate on queries carrying AI features | signals | organic ai | conversion | audit | Core | B | 2025-12-15 | experts/signals 2025-12-15 |
| reddit-mentions | Reddit mentions and an active subreddit presence | signals | ai | ranking | build | Supporting | C | 2026-07 | creators/signals 2026-07 |
| social-posts-ai-citation | Social posts as an input AI answer engines weigh | signals | ai | ranking | build | Supporting | C | 2026-07 | creators/signals 2026-07 |
| ugc-platform-presence | Presence on Reddit, YouTube, Quora and Medium | signals | ai | ranking | build | Minor | D | 2026-05 | seed: playbook/ai-search.md |
| mentions-breadth-mediums | Breadth of different mediums carrying a mention over any one source's authority | signals | ai | ranking | build | Minor | D | 2026-07 | creators/signals 2026-07 |
| social-posts-ranking | Social media posts as a direct organic ranking signal | signals | organic | ranking | both | Minor | D | 2026-07 | creators/signals 2026-07 |
| brand-longevity | Business longevity and established authority in the local pack | signals | local | ranking | audit | Minor | D | 2026-07 | creators/local-gbp 2026-07 |
| google-partner-algorithm-access | Vendors claiming privileged access to Google's ranking algorithm | signals | organic local | trust | both | Myth | A | 2026-07 | google/signals 2026-06-05; creators/signals 2026-07 |
| scaled-content-abuse | Many pages generated mainly to manipulate rankings rather than help readers | programmatic | organic ai | trust | both | Required | A | 2026-08-28 | google/programmatic 2026-08-28 |
| doorway-pages | Near-identical pages built to catch queries and funnel to one weaker destination | programmatic | organic ai | trust | both | Required | A | 2026-08-28 | google/programmatic 2026-08-28 |
| site-reputation-abuse | Third-party content published on a host site to ride its earned ranking signals | programmatic | organic ai | trust | both | Required | A | 2026-08-28 | google/programmatic 2026-08-28 |
| topical-mismatch | Publishing outside the site's established topical area to chase traffic | programmatic | organic | ranking | both | Supporting | A | 2026-08-28 | google/content 2026-08-28 |
| location-pages | City level landing pages on the website | programmatic | local organic | ranking | both | Minor | D | 2026-07 | creators/programmatic 2026-07; experts/programmatic 2026-01-20; experts/programmatic 2025-11-27 |
| programmatic-templates-unique-data | A page template carrying data or assets no competing page already publishes | programmatic | organic | ranking | build | Minor | D | 2026-01-20 | experts/programmatic 2026-01-20; experts/programmatic 2025-11-27; creators/programmatic 2023-04-11 |
| thin-page-ratio | Share of a templated page set that carries little or no value per page | programmatic | organic | ranking | both | Minor | D | 2026-09-02 | experts/programmatic 2026-09-02; experts/programmatic 2025-05-05 |
| publishing-velocity-spike | A sudden jump in publishing volume on an established site | programmatic | organic | ranking | both | Minor | D | 2026-07 | creators/content 2026-07 |
| programmatic-api-value-freshness | Numeric values inside a programmatic template refreshed from an API call | programmatic | organic | ranking | build | Minor | D | 2023-03-13 | creators/programmatic 2023-03-13 |

## Rows resting on opinion

Fifty one rows whose only support is grade D or no entry at all. QA on 2026-09-06 moved every one of them to Minor, the lowest tier the scorecard carries, because `pipeline/rubric.md` gives Supporting and Minor a floor of grade B or C and gives grade D no tier. Thirty five rest on grade D entries in `sources/`; the sixteen marked `seed only` have no entry and rest on a seed document with no primary link. Each is a research target in `pipeline/backlog.md`, and none of them should carry a playbook edit until a grade B study or a grade C test lands.

- technical: bing-indexing (seed only), faq-schema (seed only), static-html-rendering (seed only), canonical-self-reference, core-web-vitals, ai-crawler-allow, crawl-depth, url-change-risk, meta-keywords
- content: experience-first-person (seed only), multi-modal-content (seed only), eeat (seed only), answer-passage-length (seed only), answer-first-structure, keyword-in-title-front, hidden-accordion-content, alt-text
- website-design: all nine rows, hero-carousel, single-primary-cta, tap-to-call, body-font-size, text-contrast, whitespace-section-rhythm, real-team-photos, review-carousel-plugin, accessibility-baseline
- local-gbp: fake-address-listing (seed only), gbp-messaging (seed only), ask-maps-completeness, nap-footer-crawlable
- citations: citation-count-25-40 (seed only), data-aggregators (seed only), citation-blast (seed only), core-five-citations
- backlinks: reciprocal-links, page-level-links, disavow-links
- ai-search: aio-cited-click-lift (seed only), perplexity-bluf (seed only), domain-authority-aio (seed only), aio-citation-answer-first, ai-referral-conversion
- signals: ugc-platform-presence (seed only), mentions-breadth-mediums, social-posts-ranking, brand-longevity
- programmatic: location-pages, programmatic-templates-unique-data, thin-page-ratio, publishing-velocity-spike, programmatic-api-value-freshness

Two rows keep a tier the evidence does not reach, because demoting them would assert the opposite claim rather than a weaker one: `gbp-messaging` stays Dead and `domain-authority-aio` stays Myth, both on a seed document with no entry. `meta-keywords` stays Myth on a single grade D entry and is already an open dispute in `factors/disputes.md`. All three are backlog lines.
