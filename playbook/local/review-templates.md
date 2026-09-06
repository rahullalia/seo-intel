# Review Ask + Reply Templates (Apr 2026 policy compliant)

Written 2026-08-31. Every template here survives Google's April 2026 review policy and the FTC rule (16 CFR 465, $53,088 per violation). The compliance box is the law; the templates are the voice.

## The compliance box (non-negotiable, all clients)

- Ask **every** customer, not just happy ones. No sentiment pre-screen anywhere, including inside a GHL workflow. Gating can now cost a profile ALL its reviews.
- No incentives of any kind: no discounts, freebies, contest entries, tips. Federal violation + Google violation.
- Never specify a rating. "A review", never "a 5-star review".
- No on-premises kiosks, shared tablets, or watched asks. Send the link after, once they are gone. A card handed over post-service is fine; standing there while they type is not.
- No staff quotas, no "mention my name" solicitation, no employee/vendor/family reviews, no swaps.
- Always the direct unfiltered link: `https://search.google.com/local/writereview?placeid=<PLACE_ID>`
- Velocity: 1-2/week steady. Never batch a backlog of past customers into one week.

## Ask templates

**SMS, right after a delivered job (the default):**
> Hey [name], thanks again for letting us handle [the thing you did]. Quick favor: reviews on Google are how people find us. Would you mind leaving one? Takes two minutes: [link]. If you can, mention what we actually did for you. It genuinely helps.

**Email version:**
> Subject: quick favor
>
> Hi [name],
>
> Glad we could get [project/job] done for you. One small ask: a Google review helps us more than any ad we could run. Here's the direct link: [link]
>
> A sentence or two about what we did for you is perfect. Thank you!
>
> [signature]

**Personal-relationship ask (past clients, people you know):**
> Hey [name], quick favor. Reviews are the thing that gets [business] found on Google. You saw the work we did on [the website / the automations / the rankings]. Would you mind leaving a quick one? Two minutes, direct link: [link]. If you can, mention what we actually built for you. Thank you!

**The one follow-up (5-7 days later, then stop):**
> Hey [name], no pressure at all, just floating this back up in case it got buried: [link]. Two minutes and it makes a real difference for us.

**QR card copy (handed after service, never watched):**
> Enjoyed working with us? A Google review helps more than you'd think. Scan to leave one. [QR to the direct link]

**Timing rules:** ask at the moment of a delivered win (site shipped, job passed inspection, problem fixed), not weeks later. Ask the person who thanked you first. Nudge customers to mention the specific service and attach a photo (reviews with photos are ranking factor #43, and service keywords in review text feed relevance and Ask Maps). Nudging content is fine; scripting their words is not.

## Reply templates (every review, within 48h)

**Positive:**
> Thank you, [name]! Glad the [service] [outcome, e.g. "is already saving you time"]. Enjoyed working on this one. See you next time you need [service] in [city].

Work one service + city in naturally, vary the phrasing every time, never paste the same reply twice. AI-drafted is fine; a human reads it before it posts (Google pre-moderates owner replies now).

**Negative (real customer, real problem):**
> [Name], thank you for the honest feedback, and I'm sorry we missed the mark on [the specific thing]. That's not the standard we run at. I'd like to make it right: call me directly at [number] or reply to [email] and I'll handle it personally.

Rules: reply once, calmly, take it offline. Never argue, never litigate details publicly, never reveal customer/job information (medical clients: HIPAA applies, confirm nothing, not even that they were a customer). After it's resolved, you may ask (without conditions) if they'd consider updating the review; never require it.

**Suspected fake or wrong-business review:**
> We have no record of working with anyone by this name. If you're a real customer, contact us at [number] and we'll sort it out immediately.

Then flag it: profile > review > Report, and track it via the Reviews Management Tool. Removal takes days to weeks and only works on policy violations (conflict of interest, off-topic, fake). A real negative review is not removable; it's answerable.

## GHL automation setup (per client)

- Trigger: job completed / invoice paid.
- Action: SMS (email fallback) with the direct link, template above.
- Explicitly OFF: any sentiment filter, rating pre-ask, or "how was your experience" branch before the link. That branch IS review gating.
- One follow-up max, 5-7 days, then the workflow ends.
- New review webhook: draft reply for approval, 48h SLA.
