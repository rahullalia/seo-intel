# New-Client Local SEO SOP (90 days)

The runnable version of the playbook. One client, top to bottom. Rules and evidence live in the other files; this is just the order of operations. Written 2026-08-31.

## Phase 0: Intake (before touching anything)

- [ ] Decide the business type honestly: storefront / SAB / hybrid (`business-types.md`). This decision gates everything and faking it is the #2 suspension cause.
- [ ] Create the client's canonical NAP record (the `nap-canonical.md` pattern): exact name string, one permanent phone, address or hidden-address policy, website URL, hours, categories, service list, service areas. Every listing gets built from this file and only this file.
- [ ] Access: GBP owner or manager invite (audit existing managers, remove stale/unknown ones: a spam-flagged manager account can kill the profile), website edit access, GA4 + GSC.
- [ ] Baselines before any change: heatmap scan (LeadSnap), GSC snapshot if the site has history, review count + rating vs the top 3 pack competitors, screenshot the current profile.
- [ ] Competitor read: primary categories of the top 3 in the pack, their review counts and velocity, their services. This sets the category choice and the review target.

## Phase 1: Day 1 (profile foundation)

- [ ] Verification if new: video rules in `business-types.md` (live in-app, 30s+ single take, signage + operations proof). Prep the shots before starting.
- [ ] Name: exact real-world name, nothing appended.
- [ ] Primary category: most specific match to the money service, informed by the competitor read.
- [ ] 2-3 secondary categories, genuinely relevant only.
- [ ] Hours including holidays; phone (the one permanent number); website link with UTMs.
- [ ] Address config per business type: shown (storefront), hidden + up to 20 honest service areas (SAB), shown + areas (hybrid).
- [ ] **Then stop editing core fields.** One core change at a time from here, never batched, never right after verification (rapid edits = #1 suspension cause).

## Phase 2: Week 1 (the high-leverage fields)

- [ ] Services: every predefined service Google offers for the category, then custom services for the rest, explicit keyword names. This is the fastest measured lever (24-72h). 300-char descriptions, city/keyword once each.
- [ ] Description: 750 chars, front-load the first 250.
- [ ] Attributes: everything applicable; audit any AI-generated ones for accuracy.
- [ ] Products: flat-rate packages for service businesses, real inventory otherwise.
- [ ] Photos: batch 8-12 real ones (team, jobs, workspace, one local shot; specs and rejection traps in `gbp-playbook.md`). No stock, no geotagging.
- [ ] Booking link if the business takes appointments.
- [ ] Build the direct review link and send the first 3-5 asks (`review-templates.md`), prioritizing recent wins.
- [ ] Website: crawlable NAP in the footer, address linked via the CID link; LocalBusiness schema if the stack supports it.

## Phase 3: Weeks 2-4 (velocity + citations + site)

- [ ] Review velocity running: 1-2 asks/week, every reply within 48h.
- [ ] Posts cadence starts: 1x/week (2-3x if pushing), photo + CTA + keyword, scheduled via GHL.
- [ ] Citations: one-time build, `citations.md` order (core five, aggregators, second tier, 5-10 niche from a competitor gap analysis). 25-40 total, all from the canonical NAP record. Fix duplicates first if any exist.
- [ ] Site: the primary city/service landing page live; SAB satellite pages queued at 1-2/week thereafter, smaller towns first.
- [ ] One local link action: chamber membership, sponsorship, or local press.

## Phase 4: Gates at 30 / 60 / 90 days

Run the heatmap weekly or monthly (budget-dependent) and judge at gates, not daily.

- **Day 30:** profile 100%, review gap closing, posts + photos on cadence, citations submitted, landing page live. Expect first appearances on low-competition terms near the pin. If reviews stalled below target: escalate the ask channel (calls over texts, ask at the moment of a delivered win).
- **Day 60:** review floor for the pack reached (competitor read sets the number), first top-10 grid points near the pin on wedge terms. If a wedge term is flat: check the matching service is on the profile, the landing page is live and indexed, and the GBP description leads with it.
- **Day 90:** top-3 near the pin on the least-contested wedge term, visible mid-grid on mid-tier terms. **If near-pin is strong but metro is flat, that is proximity physics, not failure**: shift budget to location pages, links, and LSAs, and stop spending GBP effort on far grid points.

Client reporting per gate: what was built + what moved underneath (reviews, coverage, impressions), never a rank promise. Month 1 reports activity, month 3 reports movement, month 6 reports leads.

## Recurring (steady state)

| Cadence | Task |
|---|---|
| Weekly | 1 post, 1-2 review asks, reply to new reviews, heatmap delta glance |
| Monthly | Full profile recheck (silent declines, auto-added services, public edits), 2-4 fresh photos, one local link action, GSC 28-day compare |
| Quarterly | Services/products refresh, NAP scan across citations, duplicate recheck, competitor category re-read |

## Before ANY edit, always

1. Is the page/profile already ranking top-3 for the term? Then don't touch the thing that ranks.
2. Is this a core field (name, address, category)? One at a time, log it, expect possible re-review.
3. Never "Apply All" on Google recommendations.
4. Does the change match the canonical NAP record? If the record is wrong, fix the record first, then propagate.
