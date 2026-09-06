# Rank Week Day 2 Replay (Call 118)

Source: HeyTony Insiders — Call Replay (hash: lDdkx9972y) | 92m 3s | ~15,284 words

## Tactics & step-by-step how-to

- **Money Page Audit exercise** (the entire session, done live, step by step):
  1. Make a copy of the "Money Page Audit" Google Sheet Matt shares (link posted in chat/email; also downloadable as CSV if you don't have a Google/G Suite login).
  2. Choose one money page from your site — a product or service page you want people to buy from or contact you through (realtor example: the buy-a-house or sell-a-house page). If you don't have one yet, use any page you want to eventually rank, or pick a landing page for one specific service (e.g., personal injury vs. car accidents as separate law-firm pages; male vs. female haircuts as separate salon pages).
  3. Paste that page's URL into pageaudit.com → Page Audit → leave target keyword blank for the first pass → click Analyze.
  4. Go to the tool's **Metadata** tab, copy the meta title (title tag) and meta description into the spreadsheet.
  5. Go to **Content** tab, copy the H1 tag(s), all H2 tags, all H3 tags, and the word count into the spreadsheet. (Shortcut: the PageAudit Chrome extension → Headings → Copy all headings, then manually strip out non-H2 lines.)
  6. Decide your main keyword (guess it if you don't have a keyword tool, using the "what do I do + where am I based" formula for local/service businesses; use a real keyword tool like SEMrush/Ubersuggest if you have one — type in a candidate keyword, check monthly volume and difficulty).
  7. Back in the audit tool, enter that keyword, re-run the scan, and record: keyword usage (raw count of times the keyword appears on page) and keyword density (%).
  8. Check the tool's **Overview** tab traffic-light indicators — is the keyword present in the title tag, the meta description, and the H1 tag (yes/no/green-red per field).
  9. Google the exact keyword, skip sponsored results and the map pack, open the #1 and #2 organic results.
  10. Run each competitor URL through pageaudit.com the same way; paste their title tag, meta description, H1, H2s, word count, keyword usage, and keyword density into the same spreadsheet, side by side with your own page.
  11. Compare: word count vs. competitors, keyword count vs. competitors, keyword density vs. competitors, and which of title/meta/H1 you're missing that they have.
  12. Stop — do not rewrite the page yet. This audit is prep for "tomorrow" (Day 3), where the group uses ChatGPT plus a spreadsheet tab of "optimization rules" to actually rewrite the page copy.
- **Diagnosing why a competitor with worse on-page signals still outranks you**: check whether they're using a *keyword variation* instead of your exact term (Matt's own case: he targeted "website design" but the two competitors beating him both use "web design" — check their title/meta/H1 for the literal words they're using, not just the phrase you assumed was "the" keyword).
- **If your keyword tool shows nothing/zero volume for a candidate term**: broaden to the core generic keyword first (e.g., typed "20 bedroom [island]" → nothing; typed the island name alone → real volume), then use the tool's "include keywords" / keyword-variation filter (e.g., filter for "rent" or "group") to narrow into buyer-intent long-tail terms, sorted by color-coded difficulty (darker green = easier to rank).
- **Backdoor ranking play for a business up against big platforms** (junk removal vs. TaskRabbit/Thumbtack): don't try to outrank the big platforms directly; instead target very specific how-to/informational questions competitors aren't covering (example given live: "how to dispose of a fridge," "can you put a fridge in a junk removal bin") as blog posts, then internally link those posts to your money page.
- **Choosing what counts as your "money page" for non-standard site structures**:
  - Marketplace/multi-brand sustainable-fashion site: use category/collection pages (by brand or by clothing type) as money pages rather than individual product pages, because collections are stable while individual products rotate/discontinue.
  - Etsy-style handmade seller: same logic — money pages should be the stable groupings (e.g., a "little black dress" collection page), not SKUs that churn.
  - Pure informational/news site (no product): skip money-page optimization entirely; focus on ranking articles instead.
- **Own-brand keyword cannibalization fix** (Alex Hopcraft's podcast site vs. his separate digital-marketing services site): if one of your own properties already ranks #1 for a term, do not target the same or similar keyword/content on your other property — Google (and ChatGPT) will connect the two as the same person/entity and it can undermine the #1 ranking.
- **International expansion approach** (asked by a UAE-based marketplace): do keyword research within the target country/market (e.g., UK, US) and build content around those localized keywords/queries — but Matt was explicit this is a weak, generic answer without actually auditing the site.
- **JS-heavy sites (React etc.) not being read by Google**: verify with `site:yourdomain.com` in Google search — if pages don't show up despite Search Console + sitemap submission, the fix is pre-rendering the site (server-side/rendered snapshot for crawlers).

## Rules / dos & don'ts

- **Never touch a page that's already ranking #1** — for any page, not just the one you're auditing today.
- Every blog post should link to **one** money page (repeated from Day 1); every page should be built around **one keyword or one small keyword cluster** — never stuff the same keyword repeatedly across every page ("Google's gonna be like, well, this person's spamming things").
- One H1 tag per page, period. Multiple H1s = a web designer using H1 for visual styling, not semantic structure — signals to Google the page is about "a whole bunch of different topics." Minimum 2–3 H2 tags recommended; H3 tags optional/only worth digging into if you've already optimized everything else and still aren't ranking.
- Body/paragraph text does not need special heading treatment — plain paragraph styling is fine as long as it's readable and appropriately sized.
- **No universal "optimal" word count, keyword count, or keyword density** — the only real benchmark is what's currently ranking #1–#2 for that specific keyword. Match your competitors' ballpark, don't guess a fixed number.
- Rule of thumb on density: if your keyword density is several percentage points higher than your competitors', you are almost certainly over-optimized (Matt's own case: 5.04% density vs. competitors' 1.76% and 0.9% — nearly 5x higher — while he'd dropped from #1 to #9).
- Any density reading of "600%+" or similarly absurd in the tool means a formatting error (stray space, keyword field left blank) — fix the input, don't trust the number.
- A density reading of exactly 0% or "0.something" means the keyword isn't actually present on the page at all.
- **Do not use sneaky/gray-hat tricks** — explicitly flagged as the reason Matt's own page dropped rankings:
  - Duplicating the same H1 text once for mobile display and once for desktop display (hidden via responsive CSS) — Google caught onto this.
  - Keyword text that only becomes visible on hover/mouse-over (technically not hidden, but functionally keyword stuffing) — "Google does not like this."
  - Consequence isn't necessarily de-indexing/banning, but you "won't get results."
- Match competitors' *exact* keyword phrasing, not just a close synonym — Matt lost visibility for "website design" while both top competitors use "web design"; that literal variance is what Google was rewarding.
- Do not copy competitors' actual title tags/meta descriptions/tag content verbatim — study the keyword and pattern, write your own.
- Don't name products/services after your own invented brand language if nobody searches that term — name the product what people actually type into Google (moisturizing-lotion example; the "beaver fur hat" custom-hatmaker example: renamed around "beaver fur hat/beaver fur top hat" because that's the searched term, not his invented product name).
- For local/service-area page networks (e.g., "plumbing Austin," "plumbing Houston"): expanding to many area pages is fine and can work, but you must write genuinely distinct content per area — do not duplicate content across those pages ("dangerous territory" if you're not diligent).
- Evergreen content over timely/news content, for anyone not already a recognized news authority in their niche: news-cycle content gets scooped by publications with existing authority even if you published first: real complaint from a boxing-news-site owner — he published something first, a competitor republished 3 hours later and outranked him despite his having "decent domain authority." Evergreen ("relevant forever") content is the reliable lane for everyone else.
- Avoid benchmarking/competing against big generalist platforms (TaskRabbit, Thumbtack, Home Depot, Amazon) — "they don't have good SEO on the page... analyzing their SEO and being like I need to do this bare minimum shit isn't going to help you." Benchmark against local competitors instead, regardless of whether those locals rank #1 or #6.
- Google (or the platform's own crawler) sometimes overrides your chosen title tag/meta description with its own — you can suggest one, but it isn't guaranteed to be used as-is.
- If a JS/React site doesn't appear in `site:domain.com` after Search Console + sitemap have been done properly, pre-rendering is described as the only remaining option.

## Tools, prompts & resources

- **Money Page Audit spreadsheet** (Google Sheet, "make a copy," downloadable as CSV) — columns for: your page's meta title, meta description, H1, H2s, H3s, word count, keyword usage count, keyword density; identical columns for competitor #1 and competitor #2; a separate tab for "optimization rules"; a separate tab that will be used Day 3 with ChatGPT to rewrite copy; a checklist tab specifically for Google Business Profile (GMB) optimization steps for local businesses.
- **pageaudit.com** — Matt's own tool (built by a developer, "I paid for it to be built... free for you guys to use"), load-tested to ~20,000 concurrent users. Two ways to use it:
  - Full site audit at pageaudit.com → paste URL (+ optional target keyword) → Analyze → tabs for Metadata, Content, Overview (traffic-light presence of keyword in title/meta/H1).
  - Chrome extension (7,000+ existing users) — quick on-page glance (title tag, meta description, all heading tags with one-click copy) without running a full audit; extension can sometimes see JS-rendered content that the full audit tool cannot (reported live by an attendee with a React site).
- **SEMrush** — Matt's preferred keyword research tool; used live to check "website design Hamilton" (260 searches/month Canada, keyword difficulty 14) and to demo Organic Research → "View all keywords" → include-keyword filtering (e.g., filter for "rent" or "group") with color-coded difficulty (darker green = easier).
- **Ubersuggest** — named as the cheaper/budget alternative to SEMrush when asked about cost.
- **"Keywords That Rank" mini-course** — bonus for anyone joining HeyTony Insiders same-day as either Rank Week Day 1 or Day 2; described as leveling per user (levels 1–5, tailored to where you are), covering: does Google know about your site, sitemap registration, Google Analytics setup ("Starter" tier ≈ 12 minutes total video), up through 10x traffic tactics, CTR improvement, content calendars, competitor-spying for advanced users.
- **Insiders program access terms**: joining gets you replay access to all Rank Week calls "indefinitely" while you're an active insider; non-insiders who attend live only get replay access until **December 17**.
- **Sign-up-today bonus tease**: hinted (not confirmed) advance ebook copy of Matt's upcoming book, guaranteed only for people who sign up same-day (still received even if you miss Day 3).
- **support@heytony.ca** (transcribed as "supportheytony ca" / "supportetoni CA") — email for missing recap/call emails or account access issues (often a typo'd email or a full inbox).
- **HARO-style "help a reporter" backlink tactic** and other resources referenced only in passing were not covered in this call (that's from a different session) — not present here.

## Case studies / examples / results

- **Matt's own page — "website design in Hamilton"**: ranked #1 for ~2 years at 600–695 words; now ranking #9 on page one/bottom. Used keyword "website design" 35 times at 5.04% density (vs. competitor densities of 1.76% and 0.9%). Root causes identified live: keyword variance (competitors use "web design," he uses "website design"), far higher word count on competitor pages (2,500 and 2,300 words vs. his 695), and his own past gray-hat tactics (duplicate hidden H1 for mobile/desktop, hover-reveal keyword text) that got the page penalized after the initial #1 run.
- **Beaver-fur custom hat maker**: client insisted on a unique/trendy invented product name; keyword research showed "beaver fur hat" gets 260 searches/month in Canada and 880/month in the US, and is an easy keyword to rank for — reframed his product naming around the literal searched term.
- **Junk-removal/bin-rental business (Matt's book's opening story)**: Matt, while still in school, designed their website with zero backlink work and minimal technical knowledge (didn't even do heading tags properly) — grew them from ~11 rental bins to 120+ in a small town purely through basic on-page SEO. Cited as proof of how much impact on-page fundamentals alone can have.
- **Local service-area page client**: has ~40 separate service-area pages; "some of them do really well for her, and some of them don't do anything" — outcome is unpredictable per-area until built and tested.
- **Etsy jewelry seller (Chloe/Nicole)**: strong reviews and long, detailed listings, but products intermittently disappear from Etsy search/cart with no explanation from Etsy support; parallel case cited — a similar client built their own website after an Etsy decline and started getting found on Google instead. Also cited: a separate jewelry maker generating $20–30K/month primarily from Instagram (only ~10,000 followers) despite (Matt's words) "shit" SEO, a "shit" website, and a bad checkout process — offered as proof there's no single required marketing channel.
- **Sustainable-fashion marketplace (Dubai-based)**: PageAudit showed only 6 words and 0 images on their homepage (likely due to Elementor/JS rendering not being visible to the audit tool, though `site:domain.com` confirmed Google does index them). Discussed restructuring their "money page" concept around category/brand collection pages instead of individual products, since products get discontinued/rotate frequently.
- **Vacation-rental / Airbnb site targeting a 5-mile island (Isla Mujeres, Mexico)**: live keyword-research demo — initial guess ("20 bedroom Isla Mujeres") returned zero volume; broadening to the island name alone surfaced real search volume; filtering for "rent"/"group" surfaced usable long-tail terms like "homes for rent" (140/month, easy) vs. harder terms, illustrating the broad-to-narrow keyword research method live.
- **Boxing news site**: owner published a story first but a competitor republished ~3 hours later and outranked him despite his "decent domain authority" — used to illustrate the evergreen-vs-news distinction.
- **Attendee poll mid-call**: multiple attendees reported completing the entire audit spreadsheet live during the session; Matt had them "give yourselves a round of applause" for finishing a full competitive analysis in one sitting.

## Notable verbatim quotes

- "If it's already ranking number one, do not touch that page. And I mean that for every single page on your website."
- "I want to make sure to be clear, this page that we're optimizing today is not — it should not be ranking. If it's already ranking number one, do not touch that page."
- "What is good is what is ranking number one. What is good is what's ranking number two."
- "This is why I tell you, do not do sneaky shit."
- "I wouldn't say it's black hat. It's more gray hat... I'm lucky my site didn't get de-indexed."
- "SEO is this simple, this basic."
- "SEO is not a quick thing. It's going to take time."
- "Every single page on your website should be focused on one keyword or one small group of keywords."
- On the Instagram jewelry seller making $20–30K/month with bad SEO: "There's no right way to do marketing or to advertise your business... that just proves that there's no right way to do anything."
- To the Etsy seller, on building her own site: "I would start a website because then you control that ecosystem."
- "The whole point of the insiders and the whole point of Rank Week is to get you actually moving forward and not wasting time watching all these courses, watching all these videos and then not taking action."
- "Most business owners will never do this kind of work — and you just did it live." (from the written AI summary framing the session)

## Tradeoffs & nuance

- There is no fixed "ideal" word count, keyword frequency, or keyword density — the right target is whatever the specific page's current #1–#2 competitors are doing, which varies keyword by keyword and niche by niche. A number that worked for Matt's own page for two years (600–700 words) later lost to competitors running 2,300–2,500 words on the same term — the target moves as the competitive set changes.
- Being far above competitors' keyword density isn't automatically "more optimized" — past a certain point (Matt's 5x-competitor density) it reads as over-optimization/keyword stuffing and appears correlated with ranking loss, not gain.
- Choosing between targeting your literal head keyword vs. a close variant (web design vs. website design) requires checking what phrasing the actual ranking pages use — assuming your own phrasing is "the" keyword can be the whole problem.
- Blog/article ranking vs. money-page ranking isn't either/or: go after easy, low-competition keywords for blog posts specifically to build overall site trust/traffic, which in turn makes the harder money-page keyword easier to win — but every post should still funnel a link to a money page.
- Building many local/service-area pages is a legitimate scale play (a client runs ~40), but the risk of duplicate/thin content across near-identical area pages rises with volume — described as "dangerous territory" that punishes anyone not being genuinely diligent about unique content per page.
- Running multiple owned properties around the same person/brand (podcast site + services site) creates a cannibalization/entity-confusion risk with Google and LLMs alike ("Google and ChatGPT will put pieces together") — sometimes the right call is to deliberately not compete with yourself on a term, even at the cost of one property not ranking for it.
- For sites with fast-rotating inventory (marketplace, Etsy, made-to-order goods), individual product pages may be the wrong optimization target entirely; stable category/collection pages capture the SEO value that individual SKUs can't hold onto.
- Advice given without seeing the actual site (international expansion question, "will this rank" questions) was explicitly caveated by Matt as potentially wrong — generic keyword-research-by-country guidance stands in for a real technical/content audit he didn't have time to do live.
- A tool's inability to "see" content (JS rendering, Elementor page reporting 6 words/0 images) doesn't necessarily mean Google can't see it either — cross-check with `site:domain.com` before assuming a rendering problem is actually hurting rankings.
