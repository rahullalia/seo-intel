# Rank Week Day 4 — Replay (Call 022)

Source: HeyTony Insiders Call Replay (hash: nNXZrjn02B) | 80m 41s | ~11,719 words

## Tactics & step-by-step how-to

- **Crawl depth model**: homepage = 0 clicks. Anything reachable from the nav (about, blog index, services/money page, product page) = 1 click. A specific blog post opened from the blog index = 2 clicks. A different post linked from that post = 3 clicks. 4+ clicks from the homepage = danger zone — Google deprioritizes pages that are hard for a human to stumble onto.
- **Live internal-linking exercise (4 minutes given)**:
  1. Open your money page (the one worked on the prior two days) in a browser tab.
  2. Open the blog post written on Monday — published link, or the Google Doc/Word doc if not yet posted.
  3. Open ChatGPT.
  4. Paste in the Day 4 prompt (from the "hey Tony CA prompts" page, shared in chat) and press enter.
  5. When it asks, paste in the blog post — link if it can read the site, otherwise paste the full text.
  6. When it asks for the money page, paste in the link plus a one-line description (e.g., "here's my money page, we do SEO for small businesses, prefer working with local businesses, not necessarily local to us").
  7. Output returned: recommended anchor text; destination page; rationale for why the link makes sense; the existing paragraph; a rewritten version of that paragraph with the link woven in (labeled e.g. "section 3"); an optional alternate CTA to add at the end of the post (not always needed).
  8. Action: copy the rewritten paragraph and swap it in for the original sentence/paragraph in the blog post.
- **Matt's internal-linking rule, part 1**: every blog post links out to 3–5 other blog posts + 1 money page. ~1,000-word post → aim for 5 other-post links; shorter post → aim for 3.
- **Matt's internal-linking rule, part 2**: every time you publish a new post, go back into 3 older posts and add a link from each of them into the new post — so the new post has inbound links immediately.
- **Auditing an old/messy blog back-catalog** (Justin Combs' 60+-post WordPress site): pull each page in Semrush or GSC, check if it's ranking page 2–3 (improvable) vs. buried; check impression volume — if it's ~2 impressions, don't bother with it; low-value pages get deleted/drafted to stop wasting crawl budget.
- **Tracking keyword coverage across many posts** to avoid future cannibalization: use a spreadsheet manually, or run the Insiders-exclusive tool that scans every page on a site and guesses the keyword it's targeting (Matt: nothing equivalent exists outside the Insiders — GSC can approximate it manually).
- **Testing a ranking page instead of overhauling it** (Ken's cheating-spouse page): make small edits — update or add a couple of paragraphs, add a couple of FAQs — then wait a couple of weeks and watch for ranking movement before doing anything bigger.
- **Diagnosing why the "wrong" page ranks** (Rocky's case: homepage stuck page 6–7, a blog post or even a competitor's Instagram outranking the intended page): look at what's sitting at #1, #2, #3 for that keyword — check word count, but more importantly check page *type* and *intent* (features page vs. a page that tells a story vs. one stacked with trust signals). Match your page type/optimization to what's actually ranking. If one of your own blog posts is cannibalizing your money page/homepage for that keyword, rewrite or remove the post.
- **Local SEO expansion into new markets** (Scott's roofing client, 3 steps): (1) set up a Google Business Profile in each new target city/area, fill out every service, add service descriptions, start collecting reviews; (2) build a dedicated location landing page on the site for each area served; (3) pursue local press/backlinks, partner with local businesses, join local associations (Chamber of Commerce, Rotary Club), consider sponsoring a local sports team.
- **Multi-language SEO** (Jasmine's English/Spanish site): don't just machine-translate the English keyword into Spanish — redo keyword research natively in the target language, since the real search phrase may differ from a literal translation.
- **Lead magnet on a money page** (Ken's case): add a short quiz/checklist (tick-box format) that gives away something of value (his own Amazon book) in exchange for contact info — this both captures leads and creates an on-page conversion signal.
- **Fixing a slow-loading homepage caused by embedded catalogs** (Yani's case): stop embedding the catalog directly; instead show an image of the catalog cover that links out to the catalog as its own page (open in the same tab, not embedded).
- **WordPress category hygiene**: keep it to 5–10 categories max, one category per blog post. If a post doesn't cleanly fit an existing category, ask whether it should be written at all, or whether two categories should be merged into a new one.
- Run the free `audit.heytony.ca` tool today (see Tools section) — its output feeds directly into tomorrow's (Day 5) 30-day SEO plan.

## Rules / dos & don'ts (keep every threshold, number, specific)

- 4+ clicks from the homepage = Google is much less likely to find/care about the page.
- Every blog post: 3–5 links to other blog posts + 1 link to a money page (scale down to 3 other-post links if the post is short).
- Every new post published: add a link to it from 3 older posts.
- WordPress: categories = yes (5–10 max, one per post). Tags = no — stated flatly three separate times across the call (to Justin, to Ken/Jasmine's tag question, and again explicitly: "The only thing I do on blog posts is I'll add category... but I'm not going to add any tags").
- Don't mass-optimize/rewrite an entire old back-catalog blindly — some posts may not even be indexed; check ranking position + impression volume first.
- Don't outright delete old posts — move to draft status first (so it can be restored), rather than permanent deletion.
- Give a drafted/dormant post 6 months to a year before deciding it's truly dead — internal linking can revive it.
- Crawl budget is finite per site, Google doesn't disclose the number, and it varies site to site — don't burn it on content that isn't performing.
- On link "rel" checkboxes (no opener / no referrer / no follow / sponsored) when creating a link/button: don't check any of them — just make a regular link.
- Domain TLD (e.g., a Swiss `.ch` domain targeting Florida leads) doesn't matter for geo-targeting as long as the content itself is in the target audience's language.
- Sales/checkout pages are fine hosted off-domain on a separate tool/platform — you don't have to take payment on your own website.
- "AI blocks" (content chunks some tools suggest adding specifically to game AI-search visibility): "we haven't found that that does anything, at least not yet" — don't do more than needed; write for humans first, Google/AI picks it up after.
- Ads vs. organic: don't kill a profitable ad campaign just to "go organic" — if it's producing positive ROI (a dollar in, a dollar-fifty out), keep running it.
- Low-search-volume keywords are good, not bad — pursue them deliberately; don't chase volume over intent.
- AI is an assistant, not a brain replacement: every AI output (blog draft, SEO recommendation) still needs human fact-checking and must not be "fluffing things up for the sake of fluffing things up."
- Keyword overlap across blog posts is fine as long as each targets a distinct question/specific angle (e.g., "how much does it cost to get my roof replaced" vs. "roof replacement timeline") — overlapping words are not the problem, overlapping intent is.
- The `audit.heytony.ca` free-month offer (code `June2026`) was stated as live-attendees-only — not extended to replay viewers.

## Tools, prompts & resources (exact prompt wording if quoted; tool names; settings)

- **Day 4 ChatGPT prompt** — sourced from the "hey Tony CA prompts" page (link shared in chat by Angela); too long to paste in chat, screenshot/copy recommended since the page comes down publicly after Sunday. Exact prompt text was not read aloud/quoted in the transcript — only its input/output behavior was described live (see Tactics section: takes blog post + money page as input, returns anchor text, destination, rationale, paragraph rewrite, optional CTA).
- **`audit.heytony.ca`** — technical SEO site audit tool (crawls the whole site: duplicate tags, missing tags, page speed, etc.). Paid tool, but code **`June2026`** = 100% off for the month (offer for live attendees only). Cancel by ~July 16–17 if not continuing. Crawl/audit takes several hours to complete (queued). Not yet included in the base Insiders membership. Does not do keyword research. Positioned explicitly against Ahrefs, Semrush, and Ubersuggest as being less bloated/overwhelming ("gives you so much crap and so much information that you don't need"); PageSpeed (web.dev) is not a substitute — different scope.
- **Hey Tony Insiders internal tool** — scans every page on a site and guesses which keyword each page is targeting; described as having no external equivalent.
- **Google Search Console** — manual per-page ranking/impression checks; also the fallback for manually tracking which keyword each page targets.
- **Semrush** — used for competitor ranking/impression checks; also called out as expensive.
- **Ahrefs, Ubersuggest** — named as tools Matt used previously and moved away from for audits.
- **ChatGPT vs. Claude** — Claude called out as producing meaningfully better writing output; explicit recommendation to move primary writing work from ChatGPT to Claude ("I recommend anybody get away from writing from Chat GPT, go to Claude").
- **Chrome extension** (introduced Day 2, used for competitor keyword lookups) — one attendee (Yani) couldn't get results from it; issue not resolved live, deferred to Insiders community/screen-share support.
- **hdinsiders.com/register** — registration link; annual discount available; this cohort's registration closes tomorrow (Day 5) at midnight.
- **support@heytony.ca** — email for platform-specific help requests (e.g., Duda-specific editing issues).
- **Insiders specialist calls**, all currently at **10am Eastern**: Denroy (local SEO + technical — "this guy's a machine"), Elliot (technical SEO), Leanne (website design as it relates to SEO), Matt (general work sessions/Q&A).
- **Duda** — website builder used by one attendee (Charlotte) via a hired developer; team's direct Duda expertise unconfirmed on the call, routed to support email.
- **Shopify** — ecommerce platform (Yvonne's case); third-party SEO-audit app + indexing app used to check product titles/descriptions/meta tags for compliance.

## Case studies / examples / results (names, niches, numbers)

- **Matt/heytony.ca (self case study)**: went through his own site and identified 70 old blog posts with no backlinks, no traffic, and/or not indexed — mass-deleted them, and traffic did not dip at all afterward.
- **Robert** (referenced from prior days): stuck at "metadata" on Day 2, by Day 3 reported his new Monday blog post finally got indexed; same person previously said he'd spent **$105,000 over 3 years** with an SEO group with nothing to show for it (≈$33–35K/year).
- **Diana**: on her third Rank Week; said Insiders + weekly calls "fill in the gap," calling her Friday call with Matt "sacred."
- **Lori**: joined Insiders in March; learned to issue a press release to dozens of media sites, and Gemini AI was already picking it up.
- **Ken** (private investigator): money page = catching a cheating spouse. Had ~150 blog posts, ~100 essentially dead. Incognito competitor search for his keyword turned up only 2 real competitors — a Reddit thread and an old "dad blog." ChatGPT produced a strong content-gap outline, but the resulting draft read as generic/"pseudo me" content; page currently ranks with only trickle clicks. Also has his own books on Amazon to use as a lead-magnet giveaway.
- **Scott**: launching his own agency, building case studies; client is a roofing company that owns its local market and services 19 states total, wants to expand into 2 secondary markets ~3 hours away and rank top-3 across the state's top 50 cities. Scott's own positioning: Google Business Profile optimization + AEO, deliberately not branding himself a full SEO agency. Attended this call from Cancun on vacation, hasn't missed a Rank Week day.
- **Yvonne** (Shopify, Canada, 5 years in business): sells knitting needles, crochet hooks, project bags/pouches — no yarn. Her real competitors for her money keyword turned out to be yarn stores (their pages rank for her keyword even though they don't specialize in her niche). Spent ~$5,000 last year with an SEO service (heard as "Golden Web SEO"/name unclear) that ran her site through an audit + gave her an SEO-compliance app and an indexing app; result: business up ~200% year over year. Also runs Google Ads — started at ~$500/month, now ~$1,000/month after 5 years, and wary of the ongoing dependency/upsell creep.
- **Yani** (certified balloon artist, near Atlantic City): homepage slowed by 4 embedded catalogs (winter gala, general, summer festival, +1 more). A recent post got rejected on posting despite being AI-written (two prior handwritten posts had gone through fine) — suspected cause was the attached image (file size) rather than AI authorship.
- **Rocky** (SaaS for the martial arts industry, Miami/East Coast): migrated from a static HTML site to WordPress specifically to start blogging. Traffic is up overall, but the target keyword/homepage sits page 6–7, with a competitor's Instagram profile even outranking his own homepage for that term. Repositioning blog content toward educational topics for martial-arts business owners (how to write a business plan, Instagram trends) rather than pure product content. Plans to compare ChatGPT vs. Claude output on the same task.
- **Jasmine** (startup in Lugano, Switzerland): sells remote sessions for inner-peace/burnout relief; target keyword shows low search volume. Runs a `.ch` domain but has real leads in Florida. Built English + Spanish content (targeting Spain) but got zero traffic on the Spanish version. Payment/checkout runs through a separate "lifetime deal" sales-page tool with a long non-branded URL, not her own domain.
- **Justin Combs**: works on a client WordPress site with 60+ blog posts, several years old, messy with keyword overlap/cannibalization; project is auditing and cleaning up the back-catalog.
- **Charlotte**: LPC counselor in Texas; noted Texas currently has no interstate counseling compact ("no pact"), making her practice state-specific and reinforcing the importance of local SEO. Site built by a hired developer on Duda; struggles editing things like image text herself. Said the blog requirement had previously felt "unattainable" (developer told her it was "crucial," she considered just hiding the blog page) — Rank Week made it feel doable.

## Notable verbatim quotes (only memorable/strategic ones)

- "If it takes four clicks or more to get to a page on your website, Google doesn't really care. The harder it is for a human to find your page, the less likely Google will actually care about it. And if Google doesn't care, you don't rank, you don't get customers, you don't make money and you can't pay your bills."
- "Every blog post should link to three to five other blog posts and one money page."
- "Every time you publish a new blog post, link to it from three older blog posts."
- "This is real SEO that you guys just did... This is something that experts even forget to do... They'll publish content, they'll get backlinks, but they won't do internal linking, which is massive."
- "Google will only crawl a certain number of pages on every site. It's different for every site. They don't tell you what it is... you don't want to be wasting your crawl budget on content that isn't doing anything for you."
- On overloaded audit tools: "It gives you so much crap and so much information that you don't need and that doesn't matter for your SEO... you get down this wormhole and you're like, I don't even know what the hell I just did."
- "I don't like spending money on ads if I can get it for free. But the caveat with that is if it's working for you and it's making you money, you're putting a dollar in, you're getting a dollar fifty out. Why would you stop that?"
- "I love keywords that not a lot of people use... people who are using that keyword are likely more likely to have a higher buying intent."
- "Claude, I will say, has a way better output... for writing, for everything, has elevated even more... I recommend anybody get away from writing from Chat GPT, go to Claude."
- On AI-optimized "blocks": "We haven't found that that does anything, at least not yet. So don't do more than you need to do. Write for humans first, and then Google and AI start picking that stuff up."
- On using AI properly: "We're using AI as a tool and not as a replacement for your brain... you still have to go through, fact check, make sure that everything's accurate."

## Tradeoffs & nuance

- Ads and organic aren't either/or: keep a profitable ad campaign running even while building organic traffic — "they're interlinked," per Matt, not a switch to flip.
- Deleting vs. drafting old content: the stated safe default is draft-and-wait 6 months to a year, but Matt's own aggressive move (mass-deleting 70 posts outright on his own site) had zero negative traffic impact — the "safe" rule and Matt's actual practice diverge.
- AI-drafted content can nail the content-gap/outline but still read as generic/inauthentic ("pseudo me") — needs human voice/editing, and replacing a live ranking page wholesale is riskier than incremental edits + a wait-and-watch period.
- National/international SEO vs. local SEO: "it's slightly different, but it's all the same concepts" — the diagnostic method (check top 3 ranking pages' type/intent) applies regardless of scope.
- When reverse-engineering competitors, word count is a secondary signal — matching page *type* and *intent* to what's actually ranking matters more.
- Insiders scaling concern (raised by multiple attendees): more members joining doesn't necessarily mean less individual attention, because people stop needing to ask once their question's been answered, and not everyone attends every call — only the ones relevant to that week's problem.
- The June2026 audit-tool discount was explicitly restricted to live attendees, not available to replay viewers after the fact.
