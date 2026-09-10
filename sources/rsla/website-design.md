# rsla | website-design

RSL/A field measurements, newest first. Format in `pipeline/rubric.md` under "RSL/A field data". Every entry: the client site, the date measured, the tool, the numbers on both sides, plain meaning, factor id, evidence grade, lever. Routines never write here.

## 2026-09-06 | A GoHighLevel review widget costs 1.0 MB of JavaScript and fails contrast 10 times

- Source: RSL/A measurement, the GHL review widget frame on reputationhub.site as embedded for Select Landscape, measured 2026-09-06, Chrome DevTools network panel and axe DevTools
- Measured: 10 requests, 304 KB transferred on the wire, 1.0 MB of JavaScript decoded, one Cloudflare Insights beacon to a third party, and 10 axe contrast failures at ratios below 2.6 to 1 against the 4.5 to 1 floor in WCAG 2.2. The widget's AI Summary volunteered negative feedback and the 1-star review was shown in the default view.
- Means: The vendor widget carries a megabyte of script and ten real contrast failures onto a money page, and surfaces the worst review by default. Paste the Google reviews as text and link to the listing instead. This measures load cost, contrast and default content, not conversion, so `review-carousel-plugin` keeps its grade on the conversion lever.
- Factor: review-carousel-plugin | Evidence: C | Lever: trust | Scope: organic | Stage: both
