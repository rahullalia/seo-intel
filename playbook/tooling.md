# Tooling: which tool answers which question

Tools produce the numbers this playbook acts on. They are not evidence of what ranks; that lives in `../factors/scorecard.md`, the only file here that grades a claim. A position is a measurement, not a cause. Free is preferred: the only paid lines are DataForSEO (pay as you go), the NoxTools SEMrush login, and LeadSnap at $99/mo. Local map-pack and citation tooling was decided 2026-08-31 in `local/tools.md`.

## Question to tool

| Question | Tool | Cost | How (MCP tool or export path) | Trap to avoid |
|---|---|---|---|---|
| What is actually happening on this site | Google Search Console | Free | `gsc` MCP `get_advanced_search_analytics`, query and page | Average position blends every query; split by query first |
| Did traffic move, and when | GSC | Free | `compare_search_periods`, 28 days vs prior 28 | Say the window with every number, never two |
| Transactional query on a blog URL | GSC | Free | `get_search_by_page_query` | Do not redirect the blog post; it ranks |
| Keyword search volume | DataForSEO | $0.012/task plus $0.00012/item | `dataforseo` MCP, KEYWORDS_DATA and DATAFORSEO_LABS | Batch about 10 keywords per call or pass `noAiMode: true` |
| Live SERP composition | DataForSEO SERP, or a plain search | $0.0006 queued, $0.002 live | `dataforseo` MCP SERP module | Match the top 3 for depth; no fixed word count exists |
| Competitor keywords, KD%, intent, backlinks | SEMrush through NoxTools | Group-buy login, no API | `noxtools.com/secure/login`, Keyword Overview bulk 100, Export CSV | Backlinks are observed and quotable; traffic is modeled. Rahul exports |
| Your own backlink profile | Ahrefs Webmaster Tools | Free, verified sites | Verify, then Site Explorer | Verified sites only, so no competitor audit |
| Question mining for blog topics | Answer the Public | Free tier | Seed the topic, read the question wheel | Volumes are unlabeled; confirm in DataForSEO first |
| Map pack rank by location | LeadSnap heatmaps | $99/mo, 25 locations | See `local/tools.md` | `local_pack` search_type is an artifact, rank about 20 at 0%; use `google_maps` |
| GBP Insights | LeadSnap reads | Included | `/locations/{id}/performance/*`: appearances, actions, queries, 6-month trend | Monthly-report material, not a ranking diagnosis |
| AI citation visibility | Bing Webmaster Tools | Free | Grounding-queries export, plus GA4 sessions by AI source | Citations are roughly 30% unstable run to run; test 2-3 at a time |
| Page speed | PageSpeed Insights | Free | Paste the URL | Lab score is one throttled run; 28-day CrUX field data is measured |
| Structured data validity | Rich Results Test | Free | Paste the URL or markup | Valid markup makes a rich result possible, not earned |
| Indexing status, one URL or the whole report | GSC | Free | `inspect_url_enhanced`, `batch_url_inspection`: about 2000/day, 10 per batch. Bucket lists: Indexing, Pages, reason, Export | Inspection lags a fresh deploy by days to 2 weeks. A 410 reports as "Not found (404)" |
| Crawl and technical audit of a whole site | Screaming Frog free tier | Free to 500 URLs, then DataForSEO ONPAGE | Crawl, export the issue tabs | Do not chase 100%: 80% per page, 90% site health is fine |
| Seasonality | Google Trends | Free | Compare terms across 5 years | Relative 0 to 100, not volume. Publish 3-4 months ahead |
| Traffic value and conversion | Google Analytics 4 | Free | `google-analytics` MCP `run_report`, `run_conversions_report` | Event retention defaults to 2 months; set 14 first |

## In an audit of an existing site, consult in this order

1. **The client's folder.** `brain.md`, `seo/`, `ls audits/`: the export may already be on disk.
2. **`gsc` MCP.** `list_properties`, `get_advanced_search_analytics` by query and page, `compare_search_periods` 28 vs prior 28.
3. **The live SERP.** Read the top 3 for the exact keyword.
4. **`dataforseo` MCP** for real search volume when the keyword choice is open.
5. **`google-analytics` MCP** when the question is value or conversion, not position.
6. **Bing WMT grounding-query export** for any AI-citation question.

## When building a new site, set up before launch

1. **GA4 property, conversion events defined, retention moved to 14 months** off the 2-month default.
2. **GSC property verified.** It backfills about 16 months, so verifying late loses no baseline. GA4 does not.
3. **Bing WMT verified, sitemap submitted.** 87% of ChatGPT citations match a page in the Bing top 20 (Zyppy, February 2026).
4. **Call tracking with separate pools for organic and GBP**, separable in month six.
5. **One canonical NAP string used everywhere.**
6. **GBP claimed in week one** if local: the only asset that can produce a lead in 30 days.

## Known limits

- **SEMrush traffic is modeled and overstates.** One RSL/A client page, 2026-07: SEMrush called it the top traffic driver at 42 visits/mo; GSC showed 0 clicks and 261 impressions in 90 days. Label it "estimate"; quote GSC or GA4 for actuals.
- **DataForSEO.** About 10 keywords per call or `noAiMode: true`. SERP $0.0006 queued, $0.0012 priority, $0.002 live; Labs $0.012/task plus $0.00012/item. `AI_OPTIMIZATION` is off on purpose at about $1.09 per check.
- **The GSC Page Indexing report is UI only**, as are Request Indexing and Validate Fix. Reconstruct with URL Inspection or ask for an Export. The `gsc` MCP is a local server, so cloud routines cannot call it.
- **GA4 event data retention defaults to 2 months.** Standard report aggregates survive; Explorations and event-level queries do not. Set 14 months on day one.
- **LeadSnap has no GBP write endpoints.** Spec dump 2026-09-04: 53 paths, every write heatmap-related. Posts, photos, hours, services and categories stay manual.
- **Bing WMT grounding queries are the only AI visibility data that exists.** Otherwise: ask the AI tools directly and record whether the client is retrieved, named, linked.
