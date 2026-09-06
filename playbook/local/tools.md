# Tools: LeadSnap Verdict and the Stack

Verified 2026-08-31, including live pulls from the agency's own LeadSnap account (8 locations) via its API.

## Verdict: keep LeadSnap, but only for what it's uniquely good at

**Keep:** GBP management + geogrid heatmap tracking (GBP+Heatmap Pro, $99/mo, 25 locations, 20K credits). White-label reports free on every tier; open REST API (locations, citations, heatmaps/schedules, GSC data) that only Local Falcon matches.

**Drop:** the Citations add-on ($20/mo per location). It is a subscription sync (same push architecture as Yext) to ~50-53 directories. Replace with one-time owned builds.

**Consolidate into GHL (already paid for):** review-request automation, review replies/inbox, GBP post scheduling via Social Planner. LeadSnap's CRM tiers ($99-299/mo) duplicate GHL entirely; never buy them. GHL confirmed does NOT do citations or geogrid tracking (both are open feature requests), which is exactly why LeadSnap stays.

## Facts from the live account (corrects our own docs)

- Actual synced directory count is **~50-53 per location, not the 65+** in `../rsla/local-seo/CLAUDE.md`. LeadSnap's own pages disagree with each other (42/46/53); the account data settles it.
- MCP access exists but is read-only since the OAuth move (writes 403); posts/photos are UI-only. Heatmap schedules run natively in LeadSnap (see memory `reference_leadsnapHeatmapMcp`).

## The citation add-on, tested (2026-08-31)

LeadSnap markets "listings you own forever, never deleted if you cancel." We tested it against our own locations:

- **Lapsed location** (Casagrande Salon, citations lapsed ~9 months, last synced 2025-11-27, full public NYC address): zero Google-indexed listings across YellowPages plus 20 major citation directories (Brownbook, Hotfrog, Cylex, ShowMeLocal, EZlocal, MerchantCircle, Foursquare, ChamberofCommerce.com, etc.). A direct YellowPages site search also returns nothing. Its only live footprint is Yelp, Facebook, and Fresha, none of which came from LeadSnap.
- **Active control** (RSL/A, subscribed, synced 4 days before the test): same result. Zero indexed listings on the same directory set, including YellowPages, one of only four publishers LeadSnap names by logo.
- The public API exposes no per-directory listing URLs at all (only a master `citation-profile` record), so "listings still populated after cancelling" means LeadSnap's internal record survives, nothing more.
- Schema fingerprint (`imprint`, `auto_sync_publisher`, per-platform tracking-number fields) looks like a white-labeled Uberall-style feed network. Inference, unconfirmed publicly.

**Conclusion:** the add-on behaves like data-feed distribution (apps, nav, voice), not crawlable citation building. Caveats: Google's index isn't exhaustive, and some directories suppress hidden-address SABs, but Casagrande has a full public address and shows nothing either, and a citation Google cannot see is worth approximately nothing for local SEO. This upgrades "drop the add-on" from a cost argument to a delivery argument: one-time BrightLocal/Whitespark builds create real, indexed profile pages; this does not appear to.

## Citation builds (the replacement)

| Tool | Cost | Notes |
|---|---|---|
| BrightLocal Citation Builder | ~$3.20/listing, $2 bulk credits, one-time | Owned forever; also does GBP post scheduling + rank tracking if ever consolidating |
| Whitespark | Packages $20-999; $399/location Yext Replacement Service | Manual, human-verified; their Local Citation Finder is the gap-analysis tool |

Math for 8-10 locations: ~$1,000-1,600 one-time vs $1,900-2,400/year forever on the add-on. Breaks even in 6-8 months, then pure savings, and the listings are owned.

## The rest of the field (evaluated, not adopted)

| Tool | Price | Why not |
|---|---|---|
| Local Falcon | $25-200/mo credits | Geogrid leader (21x21 grids) + AI-answer visibility tracking ("Share of AI Voice", ChatGPT/Gemini/AI Overviews) + MCP connector. Roughly a wash vs LeadSnap's bundled credits at our cadence. Add ONLY if AI-visibility tracking becomes a sold client deliverable |
| Yext | $199-999/location/yr | Rented: 60% of listings degrade within ~60 days of cancelling (Whitespark study). Never |
| Uberall / Moz Local | Quote-only, 25-location minimum | Same rented architecture; minimum prices us out anyway |
| Local Viking | $39-200/mo | GBP management only, no citations; "Attribute Sentry" edit alerts are its one nice trick |
| GMB Everywhere | $0-50/mo | Chrome-extension audit tool, different category; fine as a free competitor-category spy |
| Places Scout | ~$299/mo | Citation auditing only (not building), thin documentation, priced above every LeadSnap tier |
| BrightLocal platform | Track/Manage/Grow tiers, now price-on-request (confirmed 2026-08-31; 14-day trial, no card; Citation Builder stays standalone pay-as-you-go) | The fallback if LeadSnap ever dies: citations + grid tracking + GBP posting in one |

## The recommended stack (5-10 client profiles)

| Job | Tool | Cost |
|---|---|---|
| GBP management + heatmaps | LeadSnap GBP+Heatmap Pro | $99/mo |
| Citations | BrightLocal or Whitespark one-time per client | ~$100-160/client once |
| Review requests + GBP posting + CRM | GHL | $0 incremental |
| Rank truth beyond the grid | GSC (free) + `gsc` MCP | $0 |
| AI-visibility tracking (optional deliverable) | Local Falcon Starter | +$25-100/mo |

Decision rule for new tools in this category: does it (a) build owned assets, (b) measure something GSC can't, or (c) automate something GHL can't? If none, skip it.
