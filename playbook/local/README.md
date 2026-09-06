# Local SEO Playbook

Agency-wide playbook for Google Business Profile optimization, citations, and local rankings. Research layer for a future `/localSeo` skill. All claims verified against 2025-2026 sources on 2026-08-31 (Whitespark Local Search Ranking Factors Nov 2025, Sterling Sky, Near Media, Search Engine Land, Google's own docs) plus the HeyTony method and RSL/A's own Bakersfield field data.

RSL/A's own GBP operations (NAP canonical, Bakersfield strategy) live in `my-business/rsla/local-seo/`. Nothing client-specific belongs here.

## The files

| File | What it covers |
|---|---|
| `gbp-playbook.md` | The core: how the local pack ranks, field-by-field do/don't (categories, name, services, products, description, photos, posts, reviews), cadences, dead features |
| `business-types.md` | Storefront vs service-area (SAB) vs hybrid: setup, verification, ranking realities, how a SAB expands reach |
| `citations.md` | Which citations to claim (ranked), data aggregators, industry lists, NAP rules, build methods and costs, the AI-mentions angle |
| `donts.md` | The master what-NOT-to-do: suspension causes, name stuffing, review policy (April 2026 rewrite + FTC rule), myths, gray-hat |
| `tools.md` | LeadSnap verdict and the recommended stack (BrightLocal/Whitespark one-time builds, GHL overlap, Local Falcon), plus the 2026-08-31 citation add-on test |
| `sop.md` | The runnable 90-day new-client SOP: intake, day 1, week 1, gates at 30/60/90, recurring cadence |
| `review-templates.md` | Compliant review ask + reply templates (Apr 2026 policy + FTC rule) and the GHL automation spec |

## Quick answers (the questions this playbook exists for)

- **How often to post Google updates:** 1x/week floor, 2-3x/week when pushing a market. Honest framing: posts rank #148 and #168 of 187 local ranking factors (Whitespark 2026), so they are an engagement/freshness/conversion layer and Ask Maps source material, not a ranking lever. Never let posting displace review or services work.
- **Geotag photos?** No. Settled, not disputed. Google strips EXIF on upload; Sterling Sky's 5-location test showed no effect; a 27-client 10-week study (Search Engine Land, Mar 2025) showed no effect or negative on 6 of 7 metrics. Real photos shot on-site, nothing injected.
- **Photos:** real and original only, never stock (Google's AI flags stock as non-unique and buries it, and it is a policy violation). Batch 8-12 at launch, then 2-4 fresh per month. Specs: 10KB-5MB, 720x720+ recommended, video up to 30s/75MB/720p+.
- **How important are services:** very. The fastest profile lever measured: Sterling Sky saw ranking movement within 24-72 hours of adding explicit keyword-named services, and "keywords in GBP services" jumped from factor #110 to #35 year-over-year. Add every real service with the exact name customers search.
- **Products:** worth adding for anyone. Each product is an indexable mini-landing page with big mobile real estate. Service businesses list flat-rate packages ("AC Tune-Up - $89"). Ranking impact unproven (unlike services); treat as free visibility and conversion.
- **Description:** 750 chars, only the first ~250 show before "More". Effectively zero ranking weight (#171 of 187). Write it anyway: it is conversion copy and Ask Maps reads it live.
- **Which citations to claim:** core five (Google, Apple Business Connect, Bing Places, Facebook, Yelp), then BBB, Nextdoor, Foursquare, Yellow Pages, chamber of commerce, the three US aggregators (Data Axle, Foursquare, TransUnion Digital Business Profile, formerly Localeze), plus 5-10 industry directories. Stop at 25-40 total; diminishing returns after.
- **How to get citations:** one-time owned builds (BrightLocal ~$3/listing or Whitespark packages), competitor citation-gap analysis to find the niche ones, chamber membership, local sponsorships, local press. Never subscription-rented sync (Yext model: ~60% of listings degrade within ~60 days of cancelling).
- **Reviews (the real lever):** velocity and recency are the fastest-rising ranking factors. Reviews gate pack entry; proximity gates coverage. Ask every customer, unfiltered direct link, reply within 48h. April 2026 policy + FTC rule make gating, incentives, kiosks, and quotas genuinely dangerous now.
- **LeadSnap:** keep it for GBP management + heatmap tracking. Drop the $20/mo/location citations add-on in favor of one-time owned builds, and route review requests + GBP posting through GHL (already paid for). Full math in `tools.md`.

## Order of leverage (spend effort top-down)

1. Primary category (factor #1 of 187; audit what the top 3 competitors use)
2. Reviews: velocity, recency, text, owner replies
3. Services with explicit keyword names (fast, measured lever)
4. Address reality and proximity (cannot be faked; sets expectations, see `business-types.md`)
5. Website: local landing pages + links (on-page 19% + links 15% of the pack model)
6. Profile completeness: hours, attributes, description, real photos (Ask Maps reads all of it)
7. Citations: one 25-40 build, then maintenance only
8. Posts + photo cadence (engagement layer)
9. Behavioral: answer every call, booking links (missed calls hurt)
