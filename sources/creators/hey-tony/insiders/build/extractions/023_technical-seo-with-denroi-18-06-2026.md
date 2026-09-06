# Technical SEO with Denroi — 18.06.2026 (HeyTony Insiders Call #023)

Speakers: Denroy (technical SEO team lead, hey Tony, ~6 years, "six years in August") and Elliot (technical specialist, hey Tony, 2 years, specializes in local business profile / local SEO). Live Q&A call format.

## Tactics & step-by-step how-to

- **Migrating citations off Yext onto BrightLocal (David's situation: Yext citations dropped from ~4-5 pages down to 8 after a year):**
  1. Pull the full list of citations Yext currently manages/previously built.
  2. Compare that list against BrightLocal's citation list — find duplicates (e.g., both list BrownBook.com).
  3. For duplicates: let BrightLocal own/manage that citation, remove it from Yext.
  4. For citations only on Yext: check BrightLocal's Citation Builder / Citation Campaign Builder to see if that specific directory is buildable there.
     - If yes → build it through BrightLocal, let BrightLocal fully manage it.
     - If no → leave it on Yext to manage, OR check if BrightLocal lets you add it as a custom/manual citation to monitor.
  5. Once BrightLocal covers everything it can, go back to Yext and check for remaining outliers — see if those can also be added to BrightLocal as custom citations.
  6. If a citation truly can't move: either leave it on Yext, or cancel Yext entirely and manage that handful yourself directly.
  7. **On the Yext account:** find the sync toggle for business info/citations. Turn sync OFF for anything BrightLocal also manages — if sync stays ON, Yext will compete with/overwrite BrightLocal's data.

- **URL slug structure for a single-location local service business (example used: armed security/security guards in Toronto):**
  - Use `/service-type/location/` — e.g. security-guard/toronto — and drop a "services" parent segment entirely; it's redundant since people search "security guard [city]" not "services security guard [city]."
  - Hyphen vs. slash between service and location scales with site size: hyphen is fine for a small page count; once you're building dozens/hundreds of location pages (servicing an entire country), use the slash — it's easier to categorize and tag pages by location at that scale.

- **Multi-location page-building process (Benjamin: WordPress web design agency, HQ in UK, second office in Wyoming, USA, majority traffic from UK):**
  1. Check Search Console first for what keywords people already use to reach the site.
  2. Since majority traffic is UK: optimize the homepage and main service pages around UK keywords; don't touch US optimization yet.
  3. Build one entirely separate page per US location/state targeted, each around one location keyword — e.g., title tag + H1 = "Web Developer in Wyoming."
  4. Fill the rest of that page with subheadings that answer questions: "Why should you hire a web developer in Wyoming?", "Why your Wyoming business needs professional web development", "How a web developer can help businesses in Wyoming."
  5. Repeat that exact page structure for every state/area targeted.
  6. Build blog posts or a main hub page linking to every one of those location pages.
  7. Make sure anyone landing on the hub page can immediately tell those pages are for the US market (not the UK).

- **Switching a Google Business Profile to a new address (Pavitra: closing Florida location, moving to Dubai, keeping online services from the Florida market):**
  - You can change the existing GBP's address directly to the new location — profile will likely need re-verification after the address change, but functions identically once reverified, and **keeps existing reviews**.
  - Decision fork: if Florida traffic doesn't matter anymore, convert the existing profile to Dubai and close it out. If Florida traffic is still significant and a priority alongside Dubai, instead create a brand-new separate profile for the other location (after converting the first one) — but note a new profile starts with zero reviews.
  - Location pages don't need to be in the main nav, but the most important location pages should be placed somewhere in navigation (header or footer).
  - Squarespace blog location-metadata field: set it to the specific location only if that blog's content is actually about/targets that location (e.g., a Dubai service blog → set Dubai). Generic blog content (e.g., "What is a web developer?") → leave location blank.

- **Debugging a broken `site:` search (Cynthia, raisingyourbar.com):** the error was caused by typing `site.raisingyourbar.com` (period) instead of `site:raisingyourbar.com` (colon) — a period turns it into a subdomain-style URL lookup, not the search operator. Live-checked via `site:raisingyourbar.com` and confirmed the whole site was indexed and ranking fine.

- **Content/ranking strategy for a non-location, fully virtual business (Laura's e-card platform, "Wrap Gifts"):**
  1. Use **Answer the Public** (or Matt's own question-finder tool, linked from his Instagram profile) to surface real questions people ask about the product/service — e.g., "how to send e-cards," "what is an e-card," "benefits of e-cards vs. personal mail" — then build content that answers them.
  2. Mine Reddit directly: type your short-tail target keyword into Reddit search, read the actual conversations/post titles (e.g., "how long does it take for e-cards to be delivered?"), check whether that exact phrase has low competition in Google, then write content that specifically answers that exact question — you already know real search demand exists for it.
  3. Set up Google Search Console (indexing/ranking side) and connect Google Analytics (on-site behavior side); use the actual queries GSC shows people are using to find the site (e.g., "gift cards near me," "how do I buy e-gift cards") to build new blog posts or service pages answering those specific terms directly.

- **Legitimate link-building process (vs. buying spam links):** find companies that advertise as press-release distributors / connectors to large publications, ask if they also do guest blogging/guest posts, then write and pitch a full blog post optimized around one keyword with a link back to your site inside the content, and give them the post for free — they get free optimized content, you get a natural backlink.

- **Generating FAQ schema markup (Mark's Squarespace site):** ask Claude, ChatGPT, or Gemini to analyze your on-page question + answer text and generate the schema markup, then copy/paste that markup into the page's backend code-injection block. (Mark had already done exactly this across every page — confirmed as the right method.)

- **Diagnosing schema errors flagged by Google's Rich Results Test:** open the site in the tool, check each flagged item against what's actually rendered in the schema block (not just the error label) — several "critical" flags can be non-issues if the actual data (name, image, etc.) is present elsewhere in the schema; often a Squarespace rendering artifact, not a real gap.

## Rules / dos & don'ts

- Yext: you never own citations built through it — it's an API overlay, and if you stop paying the subscription, those citations disappear.
- If you manage 3, 4, or fewer than 10 citations through Yext, just take direct control of those yourself instead of paying the monthly subscription — cheaper and easier long-term.
- BrightLocal is now hey Tony's preferred citation/local tool; when they see a client on Yext, they'll almost always recommend swapping to BrightLocal.
- Don't add a "services" parent path segment to single-service local URLs — it's redundant and unnecessarily lengthens the slug.
- Semrush is no longer an officially recommended partner/platform (per Matt) since its acquisition by Adobe — but still usable daily since there's no clean alternative; look into Ahrefs or similar as options.
- All keyword-research/traffic tools (Semrush, Ahrefs, etc.) return **estimates only** — the only concrete, real traffic data comes from Google Search Console and Google Analytics, which requires being an admin on the site.
- Focus on the **trend** in these tools over time, not the absolute numbers.
- GBP post-core-update priorities, in order: (1) fully complete profile — every listed service has a description, all info matches the website exactly; (2) consistent updates/posts, daily or every-other-day, to signal active monitoring; (3) reviews, especially for service-based businesses — Google reads reviews as a relevancy/experience signal.
- Posting to GBP via a secondary scheduling tool (e.g., social scheduler cross-posting, or BrightLocal's own scheduler) counts the same to Google as manually posting directly.
- Not hitting 100% GBP profile completeness even after following every prompt can be a Google glitch, or the recommendations themselves aren't always relevant/applicable — as long as all services have full descriptions with keywords and no other core info is missing, you're fine regardless of the percentage shown.
- Any major WordPress SEO plugin (Yoast, All in One SEO, etc.) does the same core job — check for these 5 non-negotiable capabilities: (1) editable title tag, (2) editable meta description, (3) automatic sitemap creation, (4) sitemap update frequency, (5) automatic schema markup generation. Robots.txt/LLM.txt support are secondary, nice-to-haves.
- Managing two separate GBP listings under one business: use BrightLocal, or manage directly inside GBP — either works, comes down to preference.
- GSC and Bing Webmaster Tools report completely separate data (different search engines, different clicks/impressions/CTR/rankings) — but the underlying ranking *process* on both is essentially the same.
- Importing a property from GSC into Bing Webmaster Tools is a one-click process.
- Always use the Index Now feature, especially right after publishing a new page or updating an existing one — faster indexing means faster traffic and faster natural backlink accumulation.
- Roughly 90% of paid link-selling services are low-quality spam and bad for your site; only the remaining ~10% (legit blogger/publication partners) are worth pursuing.
- Schema is only a real risk when the data is **wrong or misleading** — that's a genuine Google penalty. Missing/incomplete (but accurate) schema fields are not penalized.
  - Example: wrong business hours listed → "slight penalty."
  - Example: schema claims "restaurant" when the business is actually digital marketing/PR → "major penalty."
- FAQ schema specifically: skipping it carries no penalty; only worth the manual dev effort for high-competition keywords, otherwise it's optional extra credit.
- Don't publicly list a home address in schema/GBP if you're a service-based business working remotely — safety reason (see Matt anecdote below).

## Tools, prompts & resources

- **BrightLocal** — hey Tony's preferred tool for citation management, GBP post scheduling, and local rank/position tracking. Used "for six years"; tried switching away, came back. Praised customer support: responds to issues "within a day usually."
- **Yext** — API-overlay citation builder; citations disappear if subscription lapses; has a sync toggle for business info/citations that must be turned off wherever BrightLocal owns the same data.
- **Semrush** — no longer an official hey Tony recommendation post-Adobe acquisition (accuracy, timing, credit limits described as "slightly different" since the buyout) but still used daily internally.
- **Ahrefs** — mentioned as a comparable third-party alternative to Semrush.
- **Google Search Console** — source of truth for real traffic/ranking data; required for indexing checks, `site:` operator verification, and Index Now-related workflows.
- **Google Analytics** — source of truth for on-site consumer behavior; pairs with GSC (GSC = how people find you, GA = what they do once there).
- **Bing Webmaster Tools** — separate index/ranking data from Google; import a property from GSC in one click; supports Index Now.
- **Yoast SEO** — Denroy's personal preference for WordPress SEO plugin, cited reason: "more frequent updates."
- **All in One SEO** — confirmed as "totally fine," functionally equivalent to Yoast for the 5 core needs.
- **Answer the Public** — recommended tool for surfacing real user questions to build content around.
- **Matt's question-finder tool** — referred to as "Find Questions"; linked from Matt's Instagram profile ("there's a proper link to the tool on his Instagram account").
- **Reddit (used as a research tool)** — search short-tail target keywords directly on Reddit to find real questions/conversations and gauge content-gap opportunities.
- **Page Audit** — free hey Tony Chrome extension; shows metadata, heading tags, alt text — "the basic things that you would need for SEO on any site," does "almost everything that you need to check on any website."
- **Google Rich Results Test** (referred to also as "Google Rich Data Tester") — Google's own tool for validating schema markup; used live on-call to walk through Mark's flagged errors.
- **Claude / ChatGPT / Gemini** — recommended prompt use: "Ask Claude at ChatGPT Gemini to analyze your question, your answer, and create the schema markup for you" — then paste the output into the page's code-injection/backend block.
- **Hey Orca** — social media scheduling tool mentioned by Rachel; cross-posting through it to GBP counts the same as a native manual GBP post.

## Case studies / examples / results

- **David** — signed up for Yext ~last August (annual plan, ends this August), got "4-5 pages" of citations built; a year later, down to only 8 individual citations (mostly social/direct, not Yext-built) after the sync/overlay issue; now running BrightLocal alongside Yext and needs to reconcile/migrate.
- **Gabriel** — armed security/security guard business in Toronto; used as the worked example for `/security-guard/toronto/`-style URL structure and the slash-vs-hyphen decision.
- **Rachel** — agency-side, multiple clients; reported GBP performance fluctuation across clients despite following best practices, tied to recent Google core updates (Elliot dates the relevant update to March for the completeness/reviews guidance, and separately references a May update as "the most substantial milestone" for lessening the no-location penalty).
- **Benjamin** — WordPress web design agency; HQ in the UK, second office in Wyoming, USA; majority of current search traffic is UK-based with only "a few" US searches; building out state-by-state US location pages; runs two separate GBP listings for the two offices; uses All in One SEO plugin.
- **Pavitra** — service business physically closing its Florida location and relocating to Dubai while still serving Florida-origin clients online; has two location pages (Florida ranking, Dubai not yet); working through the GBP-conversion-vs-new-profile decision and reviews retention.
- **Cynthia** — site raisingyourbar.com; live on-call debug of a `site:` search typo (period vs. colon) that had her believing something was broken; confirmed on screen-share that the whole site was properly indexed and ranking.
- **Laura ("Wrap Gifts" / "Rap Gifts", spelled out as W-R-A-P G-I-F-T-S)** — fully virtual e-card platform with no physical location, also both a "product" and "service" (they send the e-cards for you); had previously added then removed a GBP location because a virtual business doesn't fit GBP's model, describing the workaround as needing to "almost add the location page and then eliminate it in order to get Google to notice us"; also asked about distinguishing legitimate vs. spam paid-link services.
- **Mark** — Squarespace site (schema name: "Involves Strategies Inc."), added FAQ schema to every page using Claude, then hit multiple flags in Google's Rich Results Test; live walkthrough showed the flagged local-business and organization schema issues were Squarespace rendering artifacts with a real-world "net impact of zero," not actual problems — his FAQ schema approach (Claude-generated, pasted into the code injector) was confirmed correct.
- **Matt (hey Tony founder), anecdote** — used to have his real home address listed publicly and received unwanted packages/scares after people started sending him things directly, which is why hey Tony's own GBP/schema doesn't show an address today.

## Notable verbatim quotes

- "BrightLocal is now our preferred tool. Whenever I see a website or a client is using Yext, I will almost always recommend swapping over to Bright Local."
- "If you only have three, four or less than 10 citations managed through Yext, take control of all of those profiles, manage them yourself and you'll have an easier time and you'll save a lot of money than spending the monthly subscription with yext."
- "What you're looking for is the trend because all of these tools are still estimates... The only concrete traffic data you will get is from Google Search Console and Google Analytics."
- "We've used them [BrightLocal] for six years. We swapped away for them for a little bit and then tried a bunch of different other platforms and then just came right back."
- "Google Search Console is all Google... Bing Webmaster Tools uses the Microsoft Bing search engine. So that's why you're getting completely separate info."
- "90% of them are not worth doing. They are low quality spam, very bad links to have pointed at your website. However, that last 10%... those are usually partners with blogging sites or verified bloggers, news publications."
- "You already have guaranteed search traffic to that keyword. And that's... a really easy way to rank within the top three very fast." — on the Reddit-question content tactic.
- "The only time schema is an issue that needs immediate attention is if your schema information is wrong or misleading. That is a major penalty to Google."
- "Ask Claude at ChatGPT Gemini to analyze your question, your answer, and create the schema markup for you."
- "Matt used to have his and he got some packages... he got scared a few times when people saying they've sent him stuff." — on why hey Tony's profile shows no address.
- "I love it. Thank you for walking me off the cliff. I was about to jump off." — Mark, after the schema errors turned out to be non-issues.

## Tradeoffs & nuance

- Yext isn't necessarily "all bad" — keep it for the small residual set of citations BrightLocal genuinely can't build/manage, or when the count is too small to bother migrating; the real fix is just turning off the sync toggle so it stops competing with BrightLocal's data.
- Semrush: still usable and still used internally daily despite no longer being an official recommendation — the acquisition changed accuracy/timing/credit-limit behavior, but no alternative tool is categorically better, so the call is to diversify (Ahrefs, etc.) rather than drop it outright.
- URL slash-vs-hyphen for location pages is scale-dependent, not a universal rule — hyphens are fine at small scale; slashes only earn their keep once you're building dozens-to-hundreds of location pages.
- GBP profile conversion vs. new profile (Florida → Dubai case) is a real tradeoff: converting keeps reviews but sacrifices dedicated Florida presence; creating a new profile preserves both markets' visibility but the new one starts with zero reviews.
- Location pages don't strictly need main-nav placement, but burying the *most important* ones entirely (no header or footer link) is discouraged.
- Blog location metadata should be applied conditionally, not blanket — only tag geography when the content actually targets that geography, otherwise leave it off.
- Non-location businesses used to be flatly penalized for lacking an address; the more recent core update loosened that penalty, but only as a substitute for real signals — full profile completeness, regular updates, and reviews still have to compensate for not having a location.
- FAQ/schema markup investment should be need-based: worth the manual dev work for high-competition keywords, skippable elsewhere since there's no penalty for omission — effort should track competitiveness, not be applied uniformly.
- Squarespace's known schema-rendering quirks have reportedly gone unfixed for "five, six years"; Denroy's read is that this persists precisely because the real-world SEO impact nets to zero, which argues against over-investing time chasing every Rich-Results-Test flag on that platform.
- Paid link-building is mostly a trap (90% low-quality/harmful) — the viable 10% requires relationship-building (press-release/guest-post partners) and a value exchange (free optimized content for a natural link), not a straightforward purchase.
