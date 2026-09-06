# Why Doesn't It Rank — 12.12.2025 (Call 113)

Source: HeyTony Insiders Call Replay (hash: lDdkx0Mm2y) | 61m 32s | ~9254 words

## Tactics & step-by-step how-to

- **Diagnostic order for "why doesn't this rank?"**: 1) does a sitemap exist and is it submitted? 2) does Google even know the page exists (check via Search Console coverage / the page showing up in the tool at all)? 3) is the page targeting the right keyword for the actual location/service/intent? 4) backlinks/local authority signals. 5) only then look at page speed.
- Format of this recurring exercise: someone shares a link to a page they optimized **months ago** (never brand new), Matt live-audits it on screen using Semrush + the Hey Tony site-audit tool + PageSpeed Insights + the live site itself.
- **Local-business copy fix (Michelle)**: replace vague professional description ("experienced psychotherapist for individual and family therapy") with the exact neighborhood + service, e.g. "couples therapy, Midtown Manhattan," placed prominently — not buried at the bottom of the page.
- **Interactive map replacement**: instead of embedding a live Google Maps widget, take a screenshot of the map, upload it as a static web image (smaller file size), and hyperlink that image directly to the Google Business Profile / Maps listing — keeps the "we're local" trust signal without the page-speed cost.
- **Keyword iteration method**: plug candidate phrases into Semrush and compare Volume vs Keyword Difficulty; cycle through synonyms and geographic variants (e.g. "couples counseling" vs "couples therapy"; "Times Square" vs "Midtown Manhattan" vs "Midtown NYC") until finding a low-KD, decent-volume match.
- **Homepage swap test (Jessa)**: when a page is already ranking for a term it isn't truly optimized for (often a residual signal from internal-link anchor text), consider promoting the properly-optimized page to be the new homepage. In WordPress: Settings → Reading → set the homepage to the target page. Don't delete the old homepage content — just monitor rankings for days/weeks and revert the setting if performance drops. The site's "Home" nav button will simply point to the new page; no menu restructuring needed.
- **Recovering lost local rankings (Trevor)**: after losing signal (a developer change + leaving the local Chamber of Commerce), rejoin a relevant Chamber of Commerce — even a nearby major-city one instead of your literal small suburb — purely for the backlink and hyper-local relevance signal.
- **Finding local link opportunities (Ash)**: Google "[city] business directory" style searches, then pay the listing fee (even a cheap one, e.g. $29/year found live) to get a citation/backlink — worth it even if the link is no-follow.
- **Blog-to-video repurposing (Ash)**: take an existing blog post (e.g. "how much does residential cleaning cost in Cincinnati"), feed it to ChatGPT to get a video script, then film and post that as a video instead of another static photo post — starts indexing on Google and reaches more people even without likes.
- **Multi-domain consolidation (Marla)**: compare Authority Score of each domain in Semrush, keep the strongest as the single hub, and stop cross-linking to/routing bookings through the weaker satellite domains.
- **Collapsing a fragmented booking journey**: if a user has to bounce across 3 separate domains to complete one action (book villa → "things to do" site → cruise page → back), consolidate into one continuous flow on the strongest-authority domain so both users and Google's crawlers stay on one site.
- **Navigation design for many sub-offerings**: don't list every sub-page in the nav — feature the top ~5 most popular items, then add a lower "other experiences" section for people who scroll further.
- **Homepage/landing-page headline formula**: state location + what you do + one clear CTA button placed above the fold (not a small side "get quote" box) — Matt's example: "We are a dentist. We will fix your teeth. We are plumbers. We will fix your leaks."
- **Header decluttering**: don't show your own logo/brand name twice (once as an image, once as text) in the header — that's "wasted real estate"; use the second slot for a value proposition or CTA instead.
- **Insecure-link fix**: audit for `http://` (non-secure) targets in outbound/internal links, even ones that technically redirect, and change them to explicit `https://`.
- **Dead-site cleanup**: check page builders (e.g. Elementor) for stale references to domains you've already deleted (Marla still had an old link to a deleted "refocusretreats.com" causing a broken/insecure outbound link).
- **Accountability mechanic**: after each session, post publicly in the community "one thing you learned this week that you're going to fix" — saying/writing it out increases follow-through odds.

## Rules / dos & don'ts (keep every threshold, number, specific)

- Only bring a page that's been live/optimized for **months** — never a brand-new page — to this exercise.
- If a local business, the copy must state the exact service area (specific neighborhood, not just a landmark/transit hub nobody actually searches, e.g. "Times Square" vs. the real keyword "Midtown").
- Don't use interactive/embedded Google Maps widgets: nobody in the live poll used that feature on any site, it adds page weight, and it was directly flagged by PageSpeed as a slowdown source (Google Maps API + related JS).
- Use WebP images instead of other formats; reduce unused JavaScript — standard PageSpeed fixes, but tackle these only **after** content/keyword targeting is fixed.
- **One keyword/topic per page** — don't let a single homepage try to rank for two distinct services (Trevor's homepage diluted between "live streaming" and "video production").
- If the top-ranking results for a keyword are all "platform" types (e.g. Vimeo-style results) and you're a local service/agency, that keyword's intent doesn't match your business — deprioritize it even if keyword difficulty is 0.
- If top results are blog posts, ranking a hard sales/service page for that same term will be difficult, and vice versa — match content format to the dominant search intent.
- Priority order for technical work: **content/keyword correctness → backlinks/authority → page speed**. Trevor was told explicitly not to worry about his "abysmal" page speed until his pages are properly focused.
- A "suspicious" backlink flag in Semrush isn't worth chasing down — don't disavow; just keep earning more legitimate links and the suspicious ratio dilutes naturally.
- A no-follow backlink still counts as valuable — Matt: he doesn't care about follow vs. no-follow, it's still "another online mention" and "another place people can find you."
- **Instagram rule**: never put a link inside a Reel or a regular post caption — it isn't clickable on desktop or mobile; only the bio link is clickable.
- Instagram allows up to 3 hashtags, but use only **1–2**, and pick ones your actual customers would follow — not industry-insider tags (critiqued "Cincy Ma[i]d" as a hashtag mostly followed by other maids/cleaners, not customers).
- Don't strip site navigation to force a single "buy" action on a landing/sales page — it kills trust and blocks people from verifying legitimacy or finding more info; add nav back even on a single-offer cruise/sales page.
- Don't lump unrelated items under one taxonomy/page (Marla's "Things To Do" page mixed in pesos/currency info, trip insurance, airport services, golf cart rentals, and restaurant/snack info) — it confuses Google about the page's actual topic; keep categories semantically clean.
- Don't try to rank for/serve every possible keyword and page — "pigs get fat and hogs get slaughtered" (Matt says he's repeated this all week); breadth-grabbing backfires.
- Terminology doesn't matter (funnel page, lead page, landing page) — "it's a website and people are looking for information"; design for the visitor's task, not the label.

## Tools, prompts & resources (exact prompt wording if quoted; tool names; settings)

- **Semrush** — used throughout for: Domain Overview, Organic Research (exact-URL vs. root-domain toggle), Keyword Overview (Volume + Keyword Difficulty, filterable by country: US/Canada/Mexico), Backlink Analytics (referring domains, follow vs. no-follow, Authority Score, "suspicious" link flags), and competitor SERP/backlink comparisons.
- **Google PageSpeed Insights** — run against Michelle's site; flagged Google Maps API as a slowdown source, image delivery (recommend WebP), and unused JavaScript.
- **Google Search Console** — referenced for sitemap submission status and whether a page is indexed; Jessa and Ash both confirmed sign-up.
- **GoDaddy** site builder — Michelle's site; sitemap wasn't auto-generating despite the platform's claim that it would — action: contact GoDaddy support directly.
- **WordPress admin → Settings → Reading** — used to change the homepage assignment (Jessa's course-page swap).
- **Yoast SEO** plugin — generates Ash's sitemap.xml correctly (contrasted with Michelle's broken GoDaddy sitemap).
- **ChatGPT** — (1) Trevor asked it whether to renew his Chamber of Commerce membership; (2) recommended workflow for Ash: feed an existing blog post into ChatGPT to get a video script, then film/post it.
- **GoHighLevel (HighLevel)** — the platform Marla is testing for one of her sites, as an alternative to her usual WordPress builds.
- **Elementor** — page builder referenced while tracing a stale link to Marla's deleted "refocusretreats.com."
- Local directories cited live during Ash's audit: **Cincy Directory**, **Visit Cincy**, a local **Chamber of Commerce** listing, **Business Directory News** — one listing found priced at **$29/year**.
- The in-house Hey Tony **site-audit tool** flagged Michelle's missing sitemap and gave Jessa a false "sitemap unavailable" error despite a valid WordPress sitemap; workaround = email a screenshot to **matt@heytony.ca** so it can be forwarded to their developer ("it's like 99% of websites are fine, but it's always... that 0.1% that doesn't work").
- **Norton Antivirus** flagged an insecure-link warning on Marla's site (spotted by a participant, Eric, in chat); Matt is skeptical of Norton's general value ("I don't really think it does what it's supposed to do... I think it just bloats things") but confirmed the underlying HTTP-vs-HTTPS issue was real.

## Case studies / examples / results

- **Michelle — "Safe Space for Couples," Manhattan couples therapy.** No sitemap at all (GoDaddy). Google's index/coverage showed awareness of only the homepage, nothing else. Copy referenced "Times Square" (not a real search term) instead of the actual neighborhood. Semrush data: "couples counseling nyc" = 590 searches/month but harder to rank; "Midtown Manhattan" = keyword difficulty ~0 (called "nothing"), volume 40/month; "Midtown NYC" = volume 20/month, KD 0. Recommended target: "couples therapy, Midtown Manhattan/NYC."
- **Jessa — "Intimacy with Ease," online intimacy course for couples.** Homepage already ranks #2 in the US for "online intimacy course for couples," while the dedicated course page (which uses the word "course" only 6 times) doesn't rank on page 1 for anything. Competing top results: a Reddit thread, "roadmap to intimacy" course, "The Lovers Play" course, "Enhancing Sexual Intimacy" course — all course-branded. Recommendation: promote the course page to be the new homepage.
- **Trevor — "We Film Events," Vancouver live streaming/videography.** Currently ranks for nothing in Semrush's Canada view; used to rank before (a) a new developer made site changes and (b) he left his local Chamber of Commerce. Logo is an image (Google can't read the text in it). Target keyword "event live streaming services" = 40 searches/month in Canada, keyword difficulty 0. Top SERP results for a related term were dominated by platform-type sites (e.g., Vimeo-style), signaling an intent mismatch for a local videography service. He is based in a suburb (Burnaby/Surrey), an hour outside Vancouver proper.
- **Ash — Ash House Cleaning, Cincinnati.** Strong homepage copy already ("Cincinnati's trusted house cleaning for busy families," booking flow described as "book in 60 seconds"). Rankings had started climbing over a 2-year Semrush view. Has a working Yoast sitemap and Google Search Console set up. Authority Score flagged as low; Semrush showed 87 referring domains, mostly no-follow/directory-type links (told not to worry about them) plus some flagged "suspicious" links. Local Chamber of Commerce membership quoted around $800/year (Ash initially thought monthly; Matt corrected to yearly) — still called "pretty expensive," but Matt cited a cleaner in his own Chamber who won real business through it. A local directory listing was found at $29/year. Instagram bio link present and correct; flagged for an ineffective "#CincyMa[i]d"-style hashtag (mostly followed by other maids, not customers) and for posting a link inside an Instagram post/Reel (non-functional).
- **Marla — Isla/Mexico vacation rentals + tours ("the Joint Sunset Cruise").** Business spans multiple domains: a HighLevel test site, "onisla.com," her main "East ___ Vacation Rentals" site (referred to inconsistently in the transcript, ~15 years old), and a deleted "refocusretreats.com" with a lingering dead link. Domain Authority Scores compared in Semrush: onisla.com = 5, East Vacation Rentals = 18. Keyword checks: a branded cruise-name + "Isla" variant showed ~20 searches/month (Canada/US view), with one pass showing 0 volume but 22% keyword difficulty; the broader generic term "Sunset Cruise" = 50 searches/month, keyword difficulty 0 — and the #1 and #2 ranking competitors for it have only 1 backlink and 0 backlinks respectively, proving it's winnable on content alone. Target keyword phrase used only twice on the page. Page used a stock Unsplash photo Matt says he's "seen a billion times." Navigation had been intentionally removed to force a single "buy" action. Booking journey required bouncing across 3 separate domains with inconsistent fonts/design to complete one purchase. Traffic currently comes from Facebook organic posting/commenting plus direct outreach to guests already booked on the island, not paid ads.

## Notable verbatim quotes

- "I signed up for the monthly audit. My website is bad. It's okay. That just means you have a lot of room for improvement."
- "Does anybody use these interactive maps on a website? Show of hands... No, right. So what these maps do is it just clutters your site."
- "Google can't see the photo, right? They can't see the words in the photo."
- "It's like 99% of websites are fine, but it's always, you know, that .01% that doesn't work. Of course. That's who's using it."
- "SEO is all about testing, trying different things out, seeing what works."
- "You gotta fix your pages first and then you can look at page speed after that."
- "If your content is equal or better than everybody else's content and you're still not ranking, then I would say, okay, look at your page speed after that."
- "Everybody pay attention to what the top results are... if the top results are a service and you're trying to get a blog post, like, you're probably not going to rank for that."
- "We are a dentist. We will fix your teeth. We are plumbers. We will fix your leaks."
- "Even if it's a no follow link is totally fine... it's another online mention. It's another place people can find you."
- "Never put a link in your reel or in your post. That won't do anything."
- "Make it one cohesive experience."
- "Pigs get fat and hogs get slaughtered."
- "It's a website and people are looking for information."
- "It's like the window, the glass manufacturer who goes around smashing people's windows so that they buy more windows." — Matt, agreeing with a participant's "antivirus makes viruses to sell" joke about the Norton warning.
- "I'm here to serve you. I'm here to guide you on your journey and facilitate you going from not ranking to ranking."
- "If you type it out, if you say it out loud, you're more likely to do it, you're more likely to remember it, you're more likely to fix it."

## Tradeoffs & nuance

- Swapping a homepage for an already-ranking sub-page (Jessa) is explicitly framed as risky ("this is a little bit risky") — the mitigation is monitor-and-revert, not avoiding the test.
- Google Maps embeds signal local presence but cost real page speed for a feature Matt says essentially no one uses; a static screenshot linked to Maps preserves the trust signal without the performance hit.
- No-follow vs. follow backlinks: conventional SEO wisdom prizes follow links, but Matt explicitly downweights the distinction — for him the citation/mention value outweighs the technical link attribute.
- Suspicious/spammy backlinks are treated as a dilution problem (get more good links) rather than a removal/disavow problem.
- Removing navigation to funnel toward one purchase (Marla) has an internal logic — minimize distraction from "buy" — but conflicts with trust-building and crawlability; Matt weighs rankability/trust above narrow conversion-funnel purity.
- Consolidating multiple branded domains under one authority hub is a clear SEO win, but Marla's underlying business reasons for a separate "things to do" identity show real tension between brand/operational separation and SEO consolidation — Matt's resolution: keep the businesses operationally distinct but stop the cross-linking/traffic dilution between the sites.
- The content → backlinks → speed sequencing is a deliberate prioritization, not a claim that speed doesn't matter — it's deferred only until the bigger keyword/content problems are fixed.
- Chamber of Commerce value is presented as inconsistent/anecdotal rather than guaranteed — works well for local-service referrals per Ash's and Matt's own experience, but Trevor's specific complaint (his chamber focuses on "growing members, not nurturing current members") is left unresolved even while Matt still recommends joining for the backlink/relevance signal.
