# 031 — Work Session: Press Releases (08.06.2026)

## Tactics & step-by-step how-to

- **AI Overviews citation-alignment tactic (core research finding of the call):**
  1. Matt built a custom AI agent to analyze ~100 search queries, comparing (a) who's cited in Google's AI Overviews, (b) who ranks page 1 organically, (c) the overlap between the two.
  2. Finding: ranking #1 organically does **not** make you more likely to be cited in AI Overviews — no reliable correlation.
  3. He then manually inspected the actual source content behind each AI Overview citation.
  4. Core insight: citation isn't about heading tags or formatting. Google's AI generates a claim/statistic first, then looks for content that **supports** that claim.
  5. Worked example (kitchen renovation): if Google's AI Overview states "average kitchen renovation costs $50-75K" and your real price is $25-35K, writing "we do it for $25-35K" won't get you cited — you're contradicting the claim. Instead: state their claim first ("the average kitchen renovation costs $50-75K in [state/area]"), **then** pivot ("however, we can do it for $25,000"). This supports Google's claim (increasing citation odds) while still giving the reader genuinely new/differentiated info.
  6. How to find "Google's claim" for your topic: Google the exact query/question you want to rank for, read the AI Overview, and see what it's asserting and who it's citing.
  7. Origin story: Matt wrote a "how long does it take to rank on Google" Q&A-style post; 5 days later a competitor copied his exact title/idea but wrote it to align with Google's stated claims, and got cited in AI Overviews despite publishing after Matt did.

- **Full press-release production + distribution workflow (ABNewswire):**
  1. Gather 5-6 reviews max (site won't use more anyway) from Google Business Profile or any other source — screenshots are fine, and non-Google reviews (DMs, texts) are acceptable too.
  2. No reviews yet (brand-new business)? Angle the release as a launch/new-in-market announcement instead (e.g., "[Business] launches as [City]'s newest [service]").
  3. Paste Matt's Claude prompt (posted in Insiders community as "press release prompt") into a new Claude chat. If too long to paste in one go, split into two paste actions.
  4. Drop the review screenshots directly into the same chat.
  5. Claude outputs: "For Immediate Release" line + dateline + city, a headline, a body opening with an aggregate-rating claim (e.g., "holds a 5-star average across 111 Google reviews"), a placeholder owner quote to swap for a real one, quotes pulled from the actual reviews, and an "About [Company]" boilerplate + contact info.
  6. (Optional, Matt's own habit for the demo) Paste the output into a Google Doc/Word doc to edit — swap in a real owner quote, fix any placeholder/location mismatches.
  7. Create a free ABNewswire.com account.
  8. Pick a pricing tier (see Rules) and click "Add Press Release."
  9. Title field = headline only (leave out "For Immediate Release").
  10. Paste the full body into the press release content box.
  11. Write/paste a 500-character-or-less summary (have Claude/ChatGPT draft this too).
  12. Upload an image: a real Google Business Profile or review screenshot, or an AI-generated composite (Matt used ChatGPT image gen to build a headshot + 5-star rating graphic + an actual review quote overlaid). Skip the optional image-description/quote field.
  13. Add links (platform allows up to 5, Matt recommends using 2-3): e.g., a Google Reviews link and a website/service-page link, using a real keyword phrase as anchor text (e.g., "SEO Agency based in Hamilton").
  14. Get your CID link (see Tools) and use it instead of a generic Google Maps/place link for any link pointing at your Google Business Profile; used as anchor text on one link (e.g., anchor "111 Google Reviews").
  15. Select ~3 relevant categories.
  16. Fill in company details: contact email, address (unverified by the platform).
  17. Set PR Type to "web only."
  18. Select all syndication outlets available to you.
  19. Skip the meta tags section entirely.
  20. Set publishing schedule to same-day; preview to check links render; submit.
  21. Expect ~1 day turnaround; email confirmation arrives once live, with links to where it was picked up (e.g., USA Today, syndication/aggregator partners).
  22. If rejected for formatting (line breaks/page breaks/paragraph length), paste the rejection notice back into Claude/ChatGPT along with the release text, ask it to fix per that feedback, then resubmit.

- **Post-publish distribution/follow-up tactic:**
  - Do not add a press-release link/section on your own website — it's a self-referential link with no real value.
  - Post about the release (with a real link) on LinkedIn, X, and Facebook.
  - On Instagram, skip the link — post a screenshot instead.
  - Proactively contact local newspapers/publications after the release goes live: "hey, we were featured here — want to do a write-up or an exclusive interview?"
  - Sister companies/multiple locations: run a separate release per company/location, don't combine — same discipline as not double-targeting keywords on one page.
  - New company/location: wait until it's actually open before publishing that specific release.
  - Verification: no dedicated tracking tool — manually Google your exact target query and see if you show up. GSC's AI Overview reporting is still an incomplete rollout (only 1 of Matt's clients has it), so don't rely on GSC for this yet.
  - CID link extraction: go to Google Maps, find your business listing, copy its link, paste into whatismycid.com, get back the CID link.

## Rules / dos & don'ts

- Reviews: 5-6 max per release (platform won't use more anyway).
- No reviews yet: use a "new business/just launched" angle instead of a reviews angle.
- One release = one topic/business/location/keyword. Never combine two businesses, two locations, or multiple service keywords into a single release — same rule as one keyword target per webpage.
- New company/location: don't publish the "we're open" release until it's actually open.
- DBA/rename in progress (not yet reflected on Google): fine to publish now; note "also doing business as [new name]" in the copy.
- Relocating to a new area: fine to publish an arriving-in-market release now.
- Multiple services: fine to eventually do one release per service, but space them out.
- Frequency: **1-2 press releases per month max**. (Contrast: directory listings are a separate, previously-taught cadence at **8-10/month** — don't confuse the two numbers.)
- This session's exercise: do exactly ONE release, then observe impact (check back "Friday").
- If doing several releases, wait **at least ~2 weeks** between them.
- Image: always a real screenshot (Google Business Profile, a review, a composited headshot+rating) — never a stock image.
- ABNewswire title field = headline only; "For Immediate Release" stays in the body/content box, not the title.
- Links: up to 5 allowed, use only 2-3.
- Use your CID link, not the generic Google Maps/place link, for anything pointing at your Google Business Profile — Matt's claim: the CID link "passes authority," the generic place link doesn't.
- Meta tags field: leave blank.
- Categories: pick about 3 relevant ones (categories seen on the platform: Media and Communications, Website and Blog, Manufacturing, Personal Finance, Marketing and Sales, Books and Literature, plus regional UK/US options but no Canada option). Matt selected Media and Communications, Website and Blog, and (evidently) Marketing and Sales for his demo; noted Books and Literature is the right pick for a book-related release.
- Company/contact details: address is not verified by the platform (any address works); use a real contact email. The "Verify Site" button in the form did nothing when tested live.
- PR Type: "web only" is sufficient.
- Syndication outlets: select all available to you.
- Own website: never add a press-release section/link there — provides no SEO value.
- Pricing: **$80** = web distribution only. **+$30 USA Today add-on = $110 total** (Matt's recommended tier if budget allows). **~$500 bulk-credit tier** ("the 501" in the transcript) = cheaper per unit, more credits, meant for people running lots of tests — don't buy this upfront; try one $80/$110 release first unless you already know you'll test repeatedly.
- Full/"legit" human-reviewed press release service (manual submission, human review) costs **~$1,500-$2,000** — this AI+ABNewswire DIY approach is explicitly the cheaper "B tier / C tier" alternative by comparison.
- Formatting compliance: if bounced for line breaks/page breaks/paragraph length, feed the rejection notice + your release back to the AI, fix, resubmit.
- Press-release copy does **not** need a de-AI-ification/humanizing rewrite the way blog posts do — Matt leaves Claude's output mostly as-is for this format.
- Ethics guardrail: fine to headline "[Business] named best choice for X" when sourced from genuine reviews saying so — normal PR practice, not deceptive, as long as something real (reviews, an award, a study) backs the claim.
- Contest/award mentions: legitimate to include even a pay-to-enter competition win — nobody outside the judges knows the entry mechanics.
- Nothing to announce? Fall back to reviews, or use a milestone/anniversary angle (e.g., "[Business] celebrates 20 years in business").
- This is explicitly **not** "buying backlinks" in the penalized sense — framed as standard PR practice (new business, new client, award, great reviews), not manipulative.

## Tools, prompts & resources

- **ABNewswire** (abnewswire.com) — press release distribution/syndication service used for the whole exercise. Pricing: $80 web-distribution-only; +$30 USA Today add-on ($110 total); ~$500 bulk-credit tier with volume discounts.
- **Claude** — Matt's preferred model for press-release drafting ("does a much, much better job" than ChatGPT for this); ran on a higher/"high" reasoning setting during the live demo (visibly slower — Matt attributes the delay to this setting).
- **Press-release prompt** — Matt: "I had Claude come up with a prompt for me for this specifically based on what I normally do." Posted the full prompt text in the Insiders community under the label "press release prompt." The exact wording was pasted on-screen during the call, not read aloud, so it is **not verbatim-quotable from this transcript** — retrieve it from the Insiders community post directly.
- **ChatGPT** — usable as an alternative to Claude; one member's ChatGPT-drafted headline ("Breeze Air Conditioning earns a perfect five-star rating from Austin Homeowners") was approved by Matt as fine.
- **Matt's multi-model workflow habit** (general, not PR-specific): keeps Claude, Gemini, and ChatGPT all open simultaneously for other tasks, runs the same prompt through all three, and either picks the best output or mixes between them — says quality varies day to day between models.
- **whatismycid.com** — converts a Google Maps place link into your business's true CID link.
- **Google Maps** — source of the business listing/link used for CID extraction.
- **Google Doc/Word** — optional intermediate drafting/editing surface between Claude's output and pasting into ABNewswire.
- **Google Business Profile** — source of reviews/screenshots for both the press-release image and body quotes.
- **SamCart** — Matt's own checkout tool for his book sales funnel (money page on his site → SamCart checkout), positioned as functionally equivalent to Gumroad's own checkout page.
- **Gumroad** — mentioned as a comparable checkout platform (used by a member selling a book) with weaker on-platform SEO than a dedicated money page on your own site.

## Case studies / examples / results

- **Jackie** — published a new "capstone" money page covering all core services; indexed quickly after submission; already ranking around #3 on Google (win shared at the top of the call).
- **Matt's ~100-query AI Overview research** — custom AI agent compared AI-Overview citations vs. page-1 rankings across ~100 queries; found no reliable correlation; manually inspected source content behind citations to find the "supports Google's claim" pattern.
- **Matt's "how long does it take to rank on Google" post** — Q&A-style; a competitor copied the title/idea 5 days later, wrote it to align with Google's AI claims, and got cited in AI Overviews despite publishing after Matt.
- **HeyTony (Matt's own agency) demo press release** — Hamilton, Ontario-based digital marketing/SEO agency; body claim "holds a 5-star average across 111 Google reviews"; discloses (Matt says he normally never reveals client names) that Royal Caribbean left a Google review with an uploaded results screenshot; owner quote attributed to "Matt Diamante"; contact hello@heytony.ca; used the CID link as anchor text on "111 Google Reviews."
- **HeyTony's ABNewswire outlet access** — two outlets, including "Globe and Mail," showed as "temporarily unavailable" on his account; Matt's guess is this followed an Instagram video he and "Edward" posted that got millions of views (causal link unconfirmed, presented as a guess).
- **Matt's book** — hit #1 bestseller in the SEO category; ran a dedicated separate press release specifically for that milestone (not folded into a general reviews release). Sold via Gumroad; his own site money page (with testimonials + buyer photos) funnels to SamCart for checkout rather than Gumroad's own page. Parallel: "Rank Week" ranks #1 organically for its own name search and uses the same page → Reserve Your Spot → SamCart funnel.
- **Tatiana** — a prior ABNewswire release was bounced with feedback to "correctly format the content section," "remove all line breaks and page breaks," "divide content into short paragraphs to enhance readability"; fixed by pasting that feedback + the release text back into AI, then resubmitted successfully.
- **"Natalie" (per transcript speaker label; likely the bookkeeping-business member also called "Nary")** — reported all new clients recently coming through AI chat referrals (e.g., ChatGPT), including for niche/local terms like "dysfunctional medicine in Boston" and "skincare" — an anecdotal win, no further diagnostic detail given.
- **Nary / Naringa** (bookkeeping business, mid-DBA change from "Klavan Solutions" to "Clevan/Clavam Bookkeeping," not yet updated on Google) — asked whether to wait for the DBA to finalize before publishing; Matt: no, publish now, can note "also doing business as [new name]" in the copy.
- **Jason Bush** (architectural photography, Atlanta) — raised an ethics question about the headline "Jason Bush Photography named best choice for architectural photography in Atlanta" sourced only from his own reviews; Matt confirmed this is fine since it's grounded in real client language. Jason contrasted this with an unnamed competitor ("Christine [...] Photography," per his own vague description) whose site claims "premier photographer in Atlanta"/"best photographer" with, per Jason, little actual work behind it — Matt's take: Google likely won't demote for the unsupported superlative, but she also won't get the citation/credibility lift without evidence (reviews, awards) to back it.
- **David** (Bill's Towing / Chuck's Garage, sister companies) — asked about combining both businesses into one release for efficiency; told no, keep separate, same logic as not stacking two keyword targets on one page. Also opening a new facility "the first of the year" — advised to wait until it's actually open before doing that release.
- **Mariana** — 20-year-old existing business (not new); asked whether the tactic still applies without new news; Matt: yes, an anniversary itself is valid press-release material (e.g., "our business celebrates 20 years in business"); confirmed she already surfaces across Claude/Gemini/ChatGPT for her business, and this is just additive on top of that.
- **Bruna** — asked about press-release cadence, referencing Matt's earlier-taught 8-10/month figure for directory listings; Matt clarified PR cadence is different: 1-2/month.

## Notable verbatim quotes

- "It's not necessarily about heading tags, it's not about formatting. It's about Google's AI is coming up with... a claim... then they're going to look for content that supports their claim."
- "Rather than saying, hey, we can do it for 25 to 35,000, you'd say the average kitchen renovation costs between 50 and $75,000 in whatever state or whatever area you're in. And then you would say, however, we can do it for $25,000. So you're backing up their claim. Google's more likely to show it in the AI overviews."
- "You literally go to Google and you type in whatever that question is or whatever that thing that you want to rank for is, and you look at who's being cited there."
- "When you shoot a shotgun, you might hit something, but if you shoot like a rifle and you're aiming at something, you're more likely to hit it." — on picking one target market instead of several.
- "We're not purchasing backlinks in this way because a lot of these won't actually get you a backlink... this is a very common thing in PR."
- "It's going to cost you like 1500 bucks or two grand" [for a fully human-reviewed press release] — "this is kind of like a B tier, if you will, or a C tier" [describing the AI + ABNewswire DIY approach by comparison].
- "I don't think this is like an ethic thing." — on using real reviews to justify a "named best choice" headline.
- "It's not the best use of anchor text, but I'm just doing it just to see." — Matt, on using a descriptive keyword phrase as CID-link anchor text.
- "I want to see you guys getting cited in the AI overviews. I want to see Google making more associations with your businesses in your area for top rated for just even organic results as well." — Matt's stated goal for the exercise.
- "This stuff actually works, guys. It's crazy. If you put in the time and you just make the pages..." — Jason, reacting to Jackie's #3-ranking win.

## Tradeoffs & nuance

- CID link vs. generic Google Maps/place link: Matt asserts the CID link "passes authority" while the generic place link doesn't, but this is presented as his own working practice/theory, not independently verified against a confirmed Google mechanism.
- Anchor text choice: Matt used a full descriptive phrase ("111 Google Reviews") as anchor text on the CID link and explicitly flags this as suboptimal ("not the best use of anchor text") — he did it anyway in the demo just to observe results, knowingly trading anchor-text purity for expedience.
- Owner-quote/location edits aren't always "fix toward literal truth": when Claude generated "South Florida" for a client actually focused on Boca, Matt first suggested changing it to the accurate area — then reversed to "keep it South Florida" once she mentioned her actual clients say they found her searching "South Florida," not "Boca." Lesson: defer to real customer search behavior over strict geographic accuracy.
- Budget tradeoff: bulk-credit tiers (~$500) are cheaper per release and suit heavy testers (like Matt), but risk sitting unused if the tactic doesn't pan out for a given business — most members are steered toward a single $80/$110 release first.
- Legal/competitive exposure: it's "technically all right" for a competitor to run your original content through AI and reword/paraphrase it to compete for the same citation. The one carve-out: if you can claim a genuinely original study/proprietary data set, a competitor can't legitimately claim it as their own.
- Anti-scraping habit (a copyright line at the bottom of posts) is something Matt does but is explicitly unsure helps ("I don't know that it matters") — a low-confidence, low-cost precaution, not a proven deterrent.
- Verification limits: no reliable automated way yet to confirm AI-Overview citation impact — manual Google searching is the only check available now, and GSC's AI Overview reporting is an incomplete rollout (visible for only 1 of Matt's clients) — so any "did this work" read in the near term is necessarily informal, not data-verified.
- Superlative claims without backing (e.g., a competitor's unsubstantiated "premier photographer") may not get demoted by Google per Matt's belief, but also won't earn citation/credibility the way a reviews-backed claim will — the risk isn't punishment, it's simply no lift.
- National/non-local businesses: the tactic still works via essentially random small-market syndication placements (e.g., "Alaska News Desk," "Atlanta Chronicle") even with no logical geographic tie to the business — the value framed as "getting cited elsewhere" generally, not location-matched relevance.
