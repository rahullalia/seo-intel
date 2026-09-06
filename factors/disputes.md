# Disputes

Where Google's statements and measured field results disagree, or where two credible sources conflict. Recorded, not resolved by fiat. A dispute closes only when new evidence settles it, and the closing entry says which evidence. Bootstrapped 2026-09-06 from the seed's 19 disputes plus 1 opened by the programmatic research, then 1 opened by the research run of 2026-09-06: 16 open, 5 closed.

## Open

### Core Web Vitals as a measured ranking effect
- Google says "Core Web Vitals are used by our ranking systems" on its page experience documentation, page last updated 2025-12-10, google/technical 2025-12-10
- Ahrefs measured 5.21 million pages and reported no conclusive ranking method behind Core Web Vitals, 2022-01-31, experts/technical 2022-01-31
- Grade A statement against a grade B measurement, so `pipeline/rubric.md` rule 6 holds the row at Minor and records the conflict. Google confirms the signal is used and attaches no weight to it; Ahrefs looked for the weight in field data and did not find it. The Ahrefs study is from 2022 and predates the March 2024 page experience documentation rewrite, so a current large-scale measurement would settle this. Opened 2026-09-06

### GBP posts as a ranking lever
- Whitespark says post frequency ranks 148th and post quantity 168th of 187 local pack factors, both bottom quartile, 2025-11-06, experts/local-gbp 2025-11-06
- Matt Diamante says post at least twice a week for a serious map pack push, once a week as the floor, 2026-07, creators/local-gbp 2026-07
- The creators entry records the conflict itself and does not resolve it. The local playbook also flags the widely quoted "weekly posters get 70% more discovery searches" figure as having no traceable primary study, 2026-08-31, seed: playbook/local/gbp-playbook.md

### Schema markup and AI citation
- Schema App says its own site gained 19.72 percent AI Overview visibility after adding entity linking, and one Fortune 500 customer gained 8.5 percent, 2026-01-09, experts/technical 2026-01-09
- Matt Diamante says schema showed no measured lift in his testing and non-ranking pages on one site carried more schema than ranking pages, 2026-06, creators/technical 2026-06
- The seed's 3.2x FAQ schema figure is not on Schema App's page, so the larger claim is unverified, 2026-09-06, pipeline/backlog.md
- Cyrus Shepard scored 23 AI citation factors across 54 sources and reports a small but consistent positive relationship between schema and citation, 2026-05-07, experts/technical 2026-05-07
- Kyle Roof measured 10,937 pages and writes that schema is not a direct ranking factor, claiming value for indexing, rich results and AI citation instead, 2026-06-17, creators/technical 2026-06-17. Shepard at grade B and Roof at grade C agree the effect is small and indirect, which narrows the dispute to the size of Schema App's 19.72 percent figure rather than the direction. The row moved to evidence B and stayed at Minor, the tier `pipeline/rubric.md` gives a measurable but small effect, 2026-09-06

### FAQ schema against FAQ content
- SE Ranking says pages with plain text FAQ sections in the body average 4.9 AI Mode citations against 4.4 without, 2025-12-15, experts/content 2025-12-15
- playbook/ai-search.md says FAQ schema gives a 3.2x AI Overview citation advantage in one section and negligible AI Mode impact, about 3x weaker than FAQ content blocks, in another, 2026-05, seed: playbook/ai-search.md
- No entry reproduces the 3.2x figure, so the FAQPage row still rests on the seed document alone

### AI crawler policy
- Cubitrek says block GPTBot, CCBot and ClaudeBot as training scrapers and allow OAI-SearchBot, ChatGPT-User and Claude-SearchBot as retrieval agents, 2026-01-21, experts/technical 2026-01-21
- Matt Diamante says never block any AI crawler and fix crawl load with cloud hosting plus a firewall, 2026-07, creators/technical 2026-07
- Both sides are grade D practitioner recommendations with no before and after test attached
- Google says robots.txt directives for Googlebot are the control site owners have over how their sites are crawled for Search, and that AI is built into Search, page last updated 2025-12-10, google/ai-search 2025-12-10. This settles the Google half at grade A: blocking Googlebot removes a site from AI Overviews and AI Mode along with classic results. It says nothing about OpenAI, Anthropic or Perplexity user agents, so the dispute stays open on the non-Google crawlers, 2026-09-06

### Collapsed and accordion content
- HeyTony call 015 says accordions and toggles are safe to index and agentic crawlers interact with menus and forms, 2026-06-25, creators/content 2026-06-25
- HeyTony call 109 says hidden or collapsed text counts against you, naming dropdown FAQs, 2025-12-19, creators/content 2025-12-19
- Same corpus, two calls, six months apart. Displayed open is the safer default until a test settles it

### Core Web Vitals priority
- playbook/core-updates.md says pages with LCP over 3 seconds lost 23 percent more traffic in the December 2025 core update, 2026-05, seed: playbook/core-updates.md
- Matt Diamante says fix pages first and look at page speed after that, putting speed last in the fix order, 2026-07, creators/technical 2026-07
- No primary URL was found for the Semrush Sensor or Glenn Gabe figures behind the 23 percent claim, 2026-09-06, pipeline/backlog.md

### Word count target
- Matt Diamante says length is set by the top three competitors for the keyword, plus a little, 2026-07-20, creators/content 2026-07-20
- The same corpus carries four other unreconciled numbers: 750 to 1,500 words, 1,000 minimum, 2,000 or more on a homepage, and no fixed number, 2026-07, seed: sources/creators/hey-tony/insiders/page-types/00-rules-for-every-page.md
- playbook/ai-search.md adds a fifth, competitor-independent figure: articles over 2,300 words earn 5.1 AI Mode citations against 4.1 for articles under 500, 2026-05, seed: playbook/ai-search.md

### Duplicate H1s
- Matt Diamante says his own "website design in Hamilton" page fell from first to seventh with the mobile and desktop dual H1 named as a contributing cause, 2026-07, creators/content 2026-07
- The same corpus records Ellen Mitchell ranking first with two duplicate H1s, hidden overlay text and the keyword used 122 times, and tolerates two H1s carrying identical text from separate desktop and mobile blocks, 2026-07, seed: heyTony part-3 1.2 and part-4 Heading Structure

### GBP business name keywords
- Whitespark says keywords in the GBP business title rank third of 187 local pack factors, 2025-11-06, experts/local-gbp 2025-11-06
- Google says including unnecessary information in a business name is not permitted and could result in suspension, 2026-09-06, google/local-gbp 2026-09-06
- Grade A policy against grade B measured ranking benefit on the same field. Per `pipeline/rubric.md` rule 5 both rows keep their tier and this stays open

### Google Business Profile as an AI lever
- Matt Diamante says in his own repeated testing the profile shows little to no pull in AI recommendation results, 2026-07, creators/local-gbp 2026-07
- Whitespark ranks a citation type factor first in its new AI Search Visibility category, with unstructured citation quality fourth and quantity seventh, 2025-11-06, experts/citations 2025-11-06
- playbook/local/gbp-playbook.md says Ask Maps answers visitor questions live from profile fields, so profile completeness is the new Q&A, 2026-08-31, seed: playbook/local/gbp-playbook.md

### Backlinks and AI Mode citation
- SE Ranking says sites over 1.16 million visitors earn about 6.4 AI Mode citations against 2.4 for sites under 2,700 visitors, 2025-12-15, experts/ai-search 2025-12-15
- SE Ranking's referring-domain figure was carried by a second entry whose quote did not match the page, deleted by QA on 2026-09-06, so the link half of this dispute now has no verified entry
- Matt Diamante says LinkGap.io ranks second for "backlink gap" on a single 35-word page with one backlink, and members rank 1 to 3 on long-tail keywords with zero backlinks, 2026-07, creators/backlinks 2026-07

### Stock against AI imagery
- Matt Diamante ranks image sourcing as real photography first, then AI generated, then stock, 2026-07, creators/website-design 2026-07
- The same corpus says stock is roughly equivalent to AI generated after real photography, and call 079 calls AI images uncertain, 2026-07, seed: sources/creators/hey-tony/insiders/page-types/00-rules-for-every-page.md
- Only real original photography is undisputed. No external source has been found for either ordering

### External links on money pages
- HeyTony part-3 2.12 sets at least one external link per page including money pages as the rule, 2026-07, seed: heyTony part-3 2.12
- The same source records that his own flagship SEO service page has zero external links and ranks first, 2026-07, seed: heyTony part-3 2.12
- `00-rules-for-every-page.md` resolves it as a default the ranking page need not retrofit. No scorecard row carries this factor yet

### Meta keywords, Myth or Dead
- `pipeline/rubric.md` lists meta keywords among its Dead examples, alongside GBP Q&A and GBP messaging, 2026-09-06, pipeline/rubric.md
- Matt Diamante says the field is dead since the 90s and still flagged as missing by some SEO plugins, which is a Myth pattern rather than a removed feature, 2026-07, creators/technical 2026-07
- Seeded and kept as Myth. The rubric's example list needs a decision from the human supervisor

### Templated location pages
- Matt Diamante says a location page needs 100 percent original content, one page per city per service anchored in real local hooks, rolled out one to two a week, against a services times cities matrix, 2026-07, creators/programmatic 2026-07
- Backlinko says swapping "[City] plumbers" across 500 locations with identical generic text is spam rather than programmatic SEO, 2026-01-20, experts/programmatic 2026-01-20
- Search Engine Land says each template should target a specific searcher need, and the strongest programmatic pages carry research data, calculators, interviews or original graphics competitors cannot copy, 2025-11-27, experts/programmatic 2025-11-27
- Ahrefs says a company publishing a huge number of very similar pages risks creating thin content that offers little to no value, 2026-09-02, experts/programmatic 2026-09-02
- The split is on method, not on outcome: the practitioner guides endorse templated pages carrying unique data, Diamante rejects the matrix pattern outright. Every side is grade D after QA regraded the Eli Schwartz podcast entry, which carries an opinion and no measured result

## Closed

### Zero-click rate
- SparkToro says 360 of every 1,000 US Google searches in 2024 sent a click to a non-Google property, that is 36 percent, 2024-07-02, experts/ai-search 2024-07-02
- SparkToro says 68.01 percent of US Google searches from January through April 2026 ended without a click, up from 60.45 percent in 2024, 2026-06-09, experts/ai-search 2026-06-09
- Closed by the two SparkToro primaries. The seed carried 69 percent from playbook/ai-search.md and 60 percent from playbook/core-updates.md, both attributed to SparkToro and Datos and neither matching the published figures. The scorecard row now reads 68.01 percent for January to April 2026, verified 2026-06-09

### Photo geotagging
- Sterling Sky says it tracked 5 listings with geotagged photos over several weeks and saw no measurable increase in organic or local pack ranking, 2024-01-15, experts/local-gbp 2024-01-15
- Search Engine Land says Jake Hundley tested 27 lawn care clients over 10 weeks, one improved, six saw no impact and four of those six ranked worse, 2025-03-25, experts/local-gbp 2025-03-25
- Matt Diamante says Google is confirmed to strip EXIF on ingestion yet clients using it still show correlated ranking movement, 2026-07, creators/local-gbp 2026-07
- Closed by two independent grade C tests, different authors, different years, different sample sizes, both showing no benefit. `pipeline/rubric.md` rule 1 says opinion never moves a tier, so the grade D counter-claim does not reopen it. Tier stays Myth

### Review incentives
- Google says offering incentives such as payment, discounts or free goods in exchange for a review is prohibited content, 2026-09-06, google/local-gbp 2026-09-06
- Matt Diamante says a small incentive, for example 10 percent off the next service, is fine, 2026-07, creators/local-gbp 2026-07
- Closed by Google's own policy at grade A against a grade D practitioner position that predates the April 2026 review policy rewrite. The row is Required, and FTC 16 CFR 465 runs a separate federal exposure recorded in `pipeline/backlog.md` as unverified

### AI content and ranking
- Ahrefs says a check of 600,000 webpages found no clear relationship between how much AI generated content a page has and how highly it ranks, 2025-07-08, experts/content 2025-07-08
- Google's own statement on the same point sat in a 2023-02-08 entry whose quote dropped a word from the page, deleted by QA on 2026-09-06, so no grade A entry backs this side now
- Matt Diamante says a roughly 99 percent AI written post took about 30 minutes and ranked first with zero backlinks, 2026-07, creators/content 2026-07
- Closed by the grade B study across 600,000 pages, with a grade C field case agreeing. The seed's opposing figure, Surfer SEO finding human-written content 8x more likely to rank first, has no verified entry. Tier stays Myth, evidence moves from A to B

### llms.txt
- Ahrefs says it checked 137,000 sites, about 28 percent publish an llms.txt file, AI citation bots account for 1.1 percent of the requests those files receive, and 97 percent get no traffic at all, 2026-06-15, experts/technical 2026-06-15
- Matt Diamante says the file is auto-generated by Yoast with no confirmed ranking impact yet, 2026-07, creators/technical 2026-07
- Closed by the Ahrefs study at grade B. The seed's split was between playbook/ai-search.md recommending it anyway as a business-to-agent signal and HeyTony calling it unproven; the 137,000-site read settles the factual half. Tier stays Myth, evidence moves from A to B because no Google entry was reached
