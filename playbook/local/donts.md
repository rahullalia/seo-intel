# What NOT To Do

Verified 2026-08-31. This half of the playbook matters as much as the other half: enforcement stepped up sharply in 2025-2026 (Google's 2025 Trust & Safety report: 292M policy-violating reviews removed (~22% of all submitted), 13M fake profiles removed, 782K+ accounts restricted, Gemini-powered detection, proactive owner alerts). The operating rule, from HeyTony, applies to everything below: **if it feels sneaky, don't do it.**

## Suspension causes, ranked (Sterling Sky, Mar 2026)

1. **Excessive/rapid edits to core fields** (name, address, category, hours in quick succession). Change one thing, wait, verify, then the next. Never batch core-field edits, never right after verification.
2. **No genuine physical presence at the address:** P.O. boxes, virtual offices, unstaffed coworking.
3. **A spam-flagged manager/owner account** takes down every profile it manages. Vet who has access; remove stale managers; never accept manager invites from unknown "SEO vendors."
4. **Duplicate listings** (same business, or overlapping service territory between two profiles).
5. **High-spam verticals** (locksmiths, garage doors, movers, towing) get flagged more aggressively even when compliant; extra caution there.

**Hard vs soft:** soft = profile shows "unverified"/"Claim this business", rankings mostly intact. Hard = gone from Search and Maps entirely.

**Reinstatement:** appeals tool only (sole channel since Feb 2024). Prepare business registration, licenses, tax certificate, utility bill, photo/video of the location; remove suspended manager accounts first. 1-6 weeks, no case ID. Document everything as you go so the evidence exists before you need it.

## Business name

- Never keyword-stuff the name (city, service words, taglines, phone numbers). It works, which is why competitors report it: the redressal form is active, takes bulk reports, and gets manual review. Enforcement is complaint-triggered, not automatic, so do not tell a client "Google will fix the competitor's name on its own" and do not assume yours won't be reported.
- Name on GBP = name on signage = name on the website, one string.

## Reviews (banned with teeth now)

Google rewrote the review policy April 16-17, 2026. Now explicitly banned, with the penalty escalated to potentially losing **all** reviews on the profile, not just the bad ones:

- Review gating (routing happy vs unhappy customers differently, including CRM sentiment pre-screens)
- Incentives of any kind: payment, discounts, freebies, contest entries, regardless of sentiment
- Staff review quotas, and directing staff to solicit reviews naming themselves
- On-premises kiosks, shared tablets, or watched/pressured asks
- Reviews from anyone with a conflict of interest: employees, vendors, family
- Review swaps/trains (caught under the Fake Engagement policy)

Also live: the **FTC rule** (16 CFR 465, effective Oct 21 2024, first enforcement letters Dec 2025): fake/incentivized reviews and gating are now US federal violations at **$53,088 per violation** (raised from $51,744 on 2025-01-17; frozen at that level through 2026 because the Oct 2025 shutdown blocked the CPI adjustment; re-check in Jan 2027).

Behavioral flags that get real reviews filtered: sudden velocity spikes vs the profile's history, identical phrasing/length across reviews, non-local or low-trust accounts, many reviews from one IP/device. Steady drip, real customers, unfiltered link. Never specify "5-star."

## Photos

- No stock, no AI-generated "office" shots, no scraped images with third-party watermarks. Flagged as non-unique, buried, and a policy violation.
- No EXIF geotag injection. It is a no-op (Google strips EXIF) at best and measured-negative at worst (SEL 27-client study, Mar 2025). RSL/A position: never do it, never bill for it. The rebuttal for anyone selling it: Sterling Sky tested it, Search Engine Land tested it, Google states EXIF is not a local ranking factor.

## Listings and addresses

- No fake listings in cities you want to rank in: virtual offices, a friend's address, a subleased desk with no staff. This is the fraud-adjacent category Google now litigates (it sued a network running ~10K fake/hijacked listings in 2025).
- No lead-gen listings (profiles that exist to harvest and resell calls).
- No second profile at the same address without a genuinely separate business or the practitioner exception (see `business-types.md`).
- Never show the address on a SAB that customers don't visit, and never verify with a P.O. box.
- Don't max out 20 service areas across a whole state because you "would drive there." Overlapping/implausible territories trigger verification failures.

## Profile management

- Never click "Apply All" on Google's recommended edits (GBP or Ads).
- Don't thrash the primary category or rename reactively; each core edit risks re-review.
- Don't let auto-added services/attributes sit unreviewed (monthly recheck).
- Don't put tracking numbers in citations, and don't scatter NAP variants.
- Don't buy citation blasts (hundreds of junk directories, manual-action risk) or rented-citation subscriptions without an exit plan (`citations.md`).
- Don't build workflows around dead features: Q&A (gone), messaging/chat (gone July 2024).

## Myths and dead tactics (don't spend on these)

| Myth | Reality |
|---|---|
| Geotagging photos | Settled no. EXIF stripped; tested twice; flat-to-negative |
| "Near me" as a keyword | Google resolves proximity; targeting it marks you as amateur |
| Posts as a ranking lever | #148/#168 of 187; engagement layer only |
| Description keyword stuffing | #171 of 187; write it for humans and Ask Maps |
| Service-area selection = ranking | No effect; proximity runs off the hidden verified address |
| 500-directory citation packages | Junk, possible manual action |
| Chasing 100% on audit tools | 80-90% is enough; the last 10% is busywork |
| "Google partner" vendors with algorithm access | Only Ads partners exist; nobody has ranking access |

## Gray-hat: known, named, not used

For awareness (competitors do these); RSL/A does not, per the sneaky rule and client-risk math: keyword-stuffing the GBP name, a second GBP via a subleased office, review micro-sites built to manipulate brand SERPs, buying reviews. All of these now sit in the highest-enforcement categories above. The clean version of each exists in this playbook: real name + services field, real second location or LSAs, real review velocity.
