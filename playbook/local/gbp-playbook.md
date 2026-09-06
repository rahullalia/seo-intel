# Google Business Profile Playbook

Verified 2026-08-31. Factor ranks and category weights are from Whitespark's Local Search Ranking Factors 2026 edition (published Nov 2025; 47 experts, 187 factors) unless noted. GBP churns fast: re-verify anything dated before quoting it to a client.

## How the local pack ranks (the model)

Three signals, same as always: **relevance** (does your profile match the query), **distance** (proximity of your verified address to the searcher, not the searcher's typed city), **prominence** (reviews, links, mentions). Category weights for the pack:

| Signal | Weight |
|---|---|
| GBP profile signals | 32% |
| On-page (your website) | 19% |
| Reviews | 16% |
| Links | 15% |
| Behavioral (clicks, calls, bookings) | 8% |
| Citations | 7% |
| Personalization | 3% |

Two field-tested truths that frame everything (RSL/A Bakersfield data, 2026-06):

1. **Reviews gate entry.** Every business in a pack has them; a profile with 3 does not enter a pack whose floor is 10.
2. **Proximity gates coverage.** High-review businesses far from the search point still lose. You rank strongest near your verified address and fade with distance. No GBP tactic beats this; only website pages, links, and LSAs reach past it (see `business-types.md`).

## Categories (factor #1)

**Do**
- Pick the single most specific primary category that matches the money service. This is the #1 ranked factor of all 187.
- Add 2-3 genuinely relevant secondary categories (up to 9 allowed; additional categories rank #8 but padding buys little).
- Audit quarterly: search your top keywords in incognito Maps, note the primary category of the top 3, compare. Change yours only on evidence, not vibes.

**Don't**
- Don't thrash the primary category reactively; each core-field edit can trigger re-review and rapid edits are the #1 suspension cause (see `donts.md`).
- Don't click "Apply All" on Google's recommended edits, ever. Review one by one.
- Don't let Google's auto-added services/categories sit: real cases had "telemarketing" and "magazine printing" auto-added. Delete irrelevant ones on the monthly recheck.

## Business name

Exact real-world name as it appears on signage and the website. Nothing else. No city, no service words, no taglines, no phone numbers. Keyword-stuffed names still correlate with rankings (keywords in title is factor #3) which is exactly why Google's AI now auto-flags them and competitors report them via the still-active redressal form. Suspension risk on a client profile is never worth it. If the legal/real name genuinely contains a service word, that is allowed and it helps. Renaming a GBP is safe (reverts if declined, keeps reviews), but expect possible re-verification.

## Hours, phone, website

- Hours accurate including holidays: "open at time of search" is factor #5, and Google now checks that stated hours match actual staffing.
- **Answer the phone.** Missed calls read as a bad outcome and hurt local rank (behavioral signal).
- One real, permanent phone number on GBP and every citation. Call tracking via dynamic number insertion on the website only, never in listings (see `citations.md`).
- Website link goes to your site (or the matching location page), never a Facebook page. UTM-tag it for GA4 attribution.

## Services (the fast lever)

**Do**
- Add every real service. Presence of predefined services is already factor #22 (new in 2026), and "keywords in GBP services" was the biggest mover in the report, #110 to #35 in one year.
- Use explicit, specific names matching real query language ("drain cleaning", "DUI defense", "vampire facial"). Sterling Sky measured ranking movement within 24-72 hours of adding keyword-named services (retested and confirmed Feb 2026).
- **Predefined services carry the most weight; custom services also move rankings, just less.** Sterling Sky's follow-up test (Jan 2024): custom services improved rankings even with no price and no description attached. So add every predefined service Google offers for the category first, then customs for real services Google doesn't list. Emojis in custom service names surface in search justifications.
- Fill the 300-character description per service (cut from 1,000 in 2024). Work the city/keyword in once, naturally. Descriptions remain untested in isolation for ranking (both Sterling Sky tests got their gains without them) but they are free Ask Maps source material.

**Don't**
- Don't repeat the city in every service entry, and no street addresses in service text.
- Don't list services the website doesn't document; the mismatch can read as padding. Mirror site and profile.

## Products

- Anyone can use them. Each product is an indexable mini-landing page with prominent mobile real estate, and Search Engine Land confirms the editor is "alive and well in 2026," more important after Google's 2025 e-commerce integrations.
- Service businesses: list flat-rate packages or plans as products ("Website in 30 Days - $4,500", "AC Tune-Up - $89"). Standard, accepted practice.
- Ranking impact is asserted, not measured (no Sterling Sky-grade test exists). Treat as visibility and conversion, not rank.

## Description

- 750 characters; only the first ~250 show before "More", so front-load: what you do, who for, city, differentiator.
- Ranking weight is effectively zero (#171 of 187). Write it for humans and for Ask Maps, which reads it live.
- No pricing, promos, or time-limited offers in it (against guidance; that is what Offer posts are for). No URLs.

## Photos and video

**Do**
- Real, original photos only: the team, jobs in progress, before/after, equipment, workspace, storefront, one recognizably-local shot. Photo/video quality (not stock) is factor #45.
- Specs: JPG/PNG, 10KB-5MB, minimum 250x250, recommended 720x720 or larger (1000x1000 square works well). Video: up to 30 seconds, 75MB, 720p+. Expect 24-48h before uploads go live.
- Cadence: batch 8-12 at launch to push completeness, then 2-4 fresh per month (each weekly post needs a photo anyway, so this is free).
- Ask customers to attach photos to reviews: "quantity of reviews with photos" is factor #43 and counts separately from owner uploads.
- Watch upload rejections: files over 5MB hard-fail, sideways iPhone shots are an EXIF orientation issue, and scraped thumbnails with third-party watermarks are a copyright problem.

**Don't**
- Don't use stock. Policy violation, and Google's AI flags generic/duplicate images as non-unique and buries them in the By Owner tab.
- **Don't geotag EXIF. Settled.** Google strips all EXIF on upload. Sterling Sky (Jan 2024, 5 locations): no measurable lasting change. Search Engine Land (Mar 2025, 27 lawn-care clients, 10 weeks, geotagged uploads 2x/week): 6 of 7 metrics flat or negative, and the single improved metric ("near me" in the tagged town) cannibalized "[service] + city" rankings elsewhere. HeyTony still calls it a cheap bet; the data says spend the minute on a real photo instead. The only photo metadata you control is the upload bucket: Logo, Cover, or plain "Add photos". Google sorts the rest into Interior, Exterior, At work and Team by image content once enough accumulate, and a photo cannot be retagged afterwards (Google Business Profile Help, "Manage your Business Profile photos & videos", read 2026-09-06). Photos that need a caption go on a Post or a Service.

## Google posts ("updates")

Honest framing first: posts frequency ranks #148 of 187 and posts quantity #168. Bottom quartile. The widely-quoted "weekly posters get 70% more discovery searches" has no traceable primary study; treat as folklore. What posts actually buy: an active-profile signal, fresh Ask Maps/AI source material, and a CTA surface (justifications like "mentioned in a post" still appear).

**Do**
- 1x/week floor, 2-3x/week when seriously pushing a map-pack market. A scheduler (GHL Social Planner) counts the same as manual.
- Every post: one original photo + one CTA (Book / Call now / Learn more) + the target keyword naturally in the opening line.
- HeyTony post formula, optional but cheap: keyword first, link the exact service page you want that keyword to rank, include your CID link, link the previous GBP post at the bottom (chain them).
- Rotate topics: result/win, educational, service spotlight, local angle, offer.
- Post types now: Updates (~1,500 chars, expire after 7 days), Offers (start/end dates), Events (persist for the event duration), Products via the product editor.

**Don't**
- Don't oversell posts to clients as a ranking lever, and never let posting cadence displace reviews or services work.
- Don't stuff links or keywords; one link, one keyword, written like a human.

## Reviews (the compounding lever)

Recency jumped from factor #20 (2023) to #11 (2026), the fastest-rising major factor. Sustained influx over time (not bursts) is #14, high rating #6, count-with-text #9.

**Do**
- Ask every customer, every time, with a direct unfiltered review link (`https://search.google.com/local/writereview?placeid=...`). Text/email it after the job, once they are home.
- Match or slightly beat competitor velocity: if the pack leaders get 2/month, get 3. Steady 1-2/week beats a burst of 10.
- Reply to every review within ~48h, working a service + city in naturally. AI-drafted replies are fine; review before posting (Google now pre-moderates owner responses).
- Ask happy customers to mention the specific service in their review; review text feeds relevance and Ask Maps.
- Put real review text (not screenshots) on money pages, linked to the source profile.

**Don't** (this section moved from "risky" to "banned with teeth", see `donts.md` for the full policy)
- No gating, no incentives of any kind, no staff quotas, no named-staff solicitation, no on-site kiosks/shared tablets, no review swaps or trains, no employee/family reviews.
- Never specify "5-star". Ask for "a review".

## Q&A is dead; Ask Maps replaced it

- Q&A API off 2025-11-03; public Q&A sections phased out from 2025-12-03. New profiles have none; legacy content is frozen.
- Replacement: **Ask Maps**, Gemini-powered, answers visitor questions live from your GBP fields (services, attributes, hours, categories, photos, description), your reviews, your website, and third-party sources.
- Consequence: profile completeness IS the new Q&A. Every field you fill is an answer Ask Maps can give; every gap is an answer it invents from third parties. Do not build anything that monitors or seeds Q&A.

## Also dead (do not budget for)

- **Messaging/chat and call history:** removed July 2024. Route "message us" intent to click-to-call or a form.
- **Google's website builder** (business.site): long gone.

## Attributes, booking, and the monthly recheck

- Fill every applicable attribute (identity attributes are trust/conversion signals, not ranking). Audit Google's AI-generated attributes for accuracy; it now invents them from reviews and your site.
- Booking links: a Reserve with Google partner gets the blue Book button; one case study attributed ~20% of listing clicks over 90 days to the appointment link.
- **Recheck the whole profile monthly.** Descriptions get silently declined, the public can suggest edits, services get auto-added, and Google now emails owners about pending edits. Profiles drift on their own.

## The CID link (HeyTony tactic, cheap)

Get the permanent CID URL (Maps share link through whatismycid.com, or View Source and find `ludocid`). Make the NAP in the site footer crawlable text with the address linked via the CID link, and reuse the CID link in blog posts and service pages. Unproven at Sterling Sky rigor, near-zero cost, plausible mechanism (explicit site-to-profile association).

## Cadence summary

| Item | Cadence |
|---|---|
| Review asks | Every customer; velocity 1-2/week steady |
| Review replies | Within 48h |
| Posts | 1x/week floor, 2-3x/week pushing |
| Photos | 8-12 at launch, then 2-4/month |
| Services/products refresh | Quarterly |
| Full profile recheck | Monthly |
| Description | Set once, revisit semi-annually |
| Citations | One build, then quarterly NAP scan |
| Heatmap scan | Weekly or monthly per client budget |
