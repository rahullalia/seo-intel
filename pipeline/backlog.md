# Backlog

Research targets carried out of the 2026-09-06 bootstrap. The research routine reads this file on the 1st and 15th and works the list top down. A line clears when a dated entry lands in `sources/` and the scorecard row cites it.

## Unresolved citations

Twenty seven lines. Each names a scorecard factor, the source a seed document credited, and why the bootstrap could not reach it. Format: `factor-id | source | why`. The last two were added by the manual fold-in of 2026-10-05.

location-pages | Whitespark | the on-page share figure lives only in a chart image
sab-address-hidden | Sterling Sky | overlapping territory claim not found verbatim in three articles
citation-count-target | closed 2026-09-10 | no source measures a stopping point. Darren Shaw's 30 to 50 recommendation is on file at grade D and the row now states that. Nothing further to chase unless someone runs a test
citation-blast | BrightLocal | manual action claim not found in four pages
information-gain | US Patent 11,769,017 | patents.google.com not fetched
eeat | Search Quality Evaluator Guidelines v13.0 | not reached
llms-txt | Google AI optimization guidance | no confident URL
aio-cited-click-lift and ai-mode-domain-traffic | Google blog I/O 2026 | not attempted
photo-geotagging | Google EXIF statement | no live Google page found
review-incentives | FTC 16 CFR 465 | ftc.gov not fetched, registry entry added
ask-maps-completeness | Google Ask Maps | only press coverage found
gbp-messaging | Google messaging removal July 2024 | no removal notice found
fake-address-listing | Google litigation | only third-party press
domain-authority-aio | Moz | no primary page for the 0.18 figure
perplexity-bluf | Perplexity docs | not reached
faq-schema | Schema App | the 3.2x figure is not on Schema App's page
reddit-mentions | SE Ranking | figure not confirmed verbatim
core-web-vitals | Semrush Sensor Dec 2025, Glenn Gabe | no primary URL
unedited-ai-output | Semrush Sensor, Ahrefs, Clearscope, SEJ | not located
experience-first-person | Semrush Sensor, Roundtable | not reached
publishing-velocity-spike and topical-mismatch | Lily Ray, Amsive | amsive.com DNS failure
ugc-platform-presence | The Slide Factory | no URL
bing-indexing, static-html-rendering, answer-first-structure | Zyppy ChatGPT citation analysis Feb 2026 | article not located
press-release-links | Edward Sturm | private Instagram video only
cite-sources-in-content | Kira, HeyTony call 076 | private guest, no public page
purchase-intent-page-type | no grade B or C source on file | a conversion rate by query intent study with its method disclosed, or a before and after on rsla.io once the 13 money pages on branch brand-visual-system ship
purchase-intent-page-type | Edward Sturm, two YouTube videos | captions returned HTTP 429 on 2026-10-05: watch?v=ucBewL5kP9Q, watch?v=hFR1QFaOI5M

## Rows resting on opinion

Fifty one scorecard rows rest on grade D or on no entry at all and are listed by category under `## Rows resting on opinion` in `factors/scorecard.md`. QA moved all of them to Minor on 2026-09-06, since `pipeline/rubric.md` gives Supporting and Minor a floor of grade B or C. Each needs a grade B study or a grade C test before its tier can be trusted in a playbook edit. Sixteen of the fifty one have no entry at all and rest on a seed document.

## Tiers corrected by QA 2026-09-06

Thirty five rows lost a tier because their cited entries did not reach the rubric minimum. Each line names what would restore it. Format: `factor-id | old tier -> new tier | evidence needed`.

fake-address-listing | Required -> Minor | a grade A Google page or a court or regulator record on P.O. box and virtual office listings
bing-indexing | Core -> Minor | a grade B study tying Bing Webmaster Tools verification to AI answer citation
experience-first-person | Core -> Minor | a grade B study on first-person authorship and core update outcomes
multi-modal-content | Core -> Minor | a grade B study on images, tables or video and AI citation rate
aio-cited-click-lift | Core -> Minor | the Google I/O 2026 blog post carrying the click-lift figure
answer-first-structure | Core -> Minor | a grade B or C test on answer-first placement and ranking
aio-citation-answer-first | Core -> Minor | a grade B or C test on answer passages and AI Overview citation
location-pages | Core -> Minor | the Whitespark on-page share figure, currently only in a chart image
information-gain | Core -> Supporting | a grade B study or a second independent grade C test; the two Google pages are grade A and rule 2 says A alone does not set Core
referring-domains | Core -> Supporting | a grade B study on referring domain count; the SE Ranking entry was deleted for a quote that did not match the page
faq-schema | Supporting -> Minor | the Schema App 3.2x FAQ figure or another grade B source
static-html-rendering | Supporting -> Minor | the Zyppy ChatGPT citation analysis of February 2026
eeat | Supporting -> Minor | Search Quality Evaluator Guidelines v13.0
answer-passage-length | Supporting -> Minor | the study behind the 134 to 167 word passage figure
citation-count-target | Supporting -> Minor | a measured test of a citation count ceiling; the row was renamed on 2026-09-10 because no source states a range as a measurement
data-aggregators | Supporting -> Minor | a grade B or C source on Data Axle, Foursquare and TransUnion coverage
perplexity-bluf | Supporting -> Minor | Perplexity documentation on answer structure
ugc-platform-presence | Supporting -> Minor | The Slide Factory analysis or another grade B source
canonical-self-reference | Supporting -> Minor | a grade C test on trailing slash canonical mismatches
core-web-vitals | Supporting -> Minor | the Semrush Sensor December 2025 or Glenn Gabe LCP figures
ai-crawler-allow | Supporting -> Minor | a before and after test on blocking or allowing retrieval agents
crawl-depth | Supporting -> Minor | a grade B or C test on click depth and indexing
url-change-risk | Supporting -> Minor | a grade B or C study on URL changes and traffic loss
keyword-in-title-front | Supporting -> Minor | a grade B or C test on keyword position inside the title tag
hidden-accordion-content | Supporting -> Minor | a test settling the accordion dispute recorded in `factors/disputes.md`
alt-text | Supporting -> Minor | a grade B or C source on alt text and image or page ranking
ask-maps-completeness | Supporting -> Minor | a Google page on Ask Maps and profile field completeness
nap-footer-crawlable | Supporting -> Minor | a grade B or C test on footer NAP markup
core-five-citations | Supporting -> Minor | a grade B or C source on the Google, Apple, Bing, Facebook and Yelp set
reciprocal-links | Supporting -> Minor | a grade B or C study on reciprocal link patterns
mentions-breadth-mediums | Supporting -> Minor | a grade B study comparing breadth of mediums against source authority
thin-page-ratio | Supporting -> Minor | a grade B or C measurement of the thin page share that triggers a drop
publishing-velocity-spike | Supporting -> Minor | the Lily Ray or Amsive analysis, amsive.com previously failed DNS
ai-referral-conversion | Supporting -> Minor | the Similarweb 2025 ecommerce report itself; the HubSpot post only relays it and is grade D
programmatic-templates-unique-data | Supporting -> Minor | a grade B or C test on unique data inside a page template

Three rows kept a tier the evidence does not reach, because demoting them would assert the opposite claim rather than a weaker one. Each still needs evidence.

gbp-messaging | Dead, no entry | Google's July 2024 messaging removal notice
domain-authority-aio | Myth, no entry | the Moz page behind the 0.18 correlation figure
meta-keywords | Myth, one grade D entry | a grade A Google statement or a no-effect test; also an open dispute in `factors/disputes.md`

## Website design has no external evidence yet

All nine website-design rows rest on the HeyTony corpus and nothing else: hero-carousel, single-primary-cta, tap-to-call, body-font-size, text-contrast, whitespace-section-rhythm, real-team-photos, review-carousel-plugin, accessibility-baseline. `sources/google/website-design.md` and `sources/experts/website-design.md` are both empty as of 2026-09-06, so every one of the nine is grade D and tiered Minor. These are conversion and trust levers, not ranking levers, which is why the gap did not block the bootstrap. The targets are Baymard Institute, Nielsen Norman Group and Google's page experience documentation for carousel, CTA, tap target, font size and contrast claims, plus WCAG 2.2 for the accessibility row.
