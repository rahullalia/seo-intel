# Tools, Prompts, Local SEO, Ecommerce, Don'ts & Mindset

Matt Diamante's operating layer: the exact tools and prompts that run the method, how local and ecommerce sites are structured differently from everything else, the hard "don't" rules that override every tactic, and the business/mindset frame that decides whether any of it gets done at all.

---

## PART 1 — TOOLS & PROMPTS

### 1.1 The governing tool philosophy

- **Google Search Console is the single most important tool, ranked above every keyword tool and even above Google Analytics.** It is the only concrete, real (non-estimated) ranking/traffic data source, straight from Google. Set it up *before* making any keyword-targeting decision: "without Search Console, you really are just shooting in the dark." Use GSC as the definitive source of truth whenever third-party tools disagree.
- **Every keyword/backlink tool disagrees with every other tool, and with GSC, by wide margins for the identical domain.** One live example on one domain, checked back to back: GSC showed **325** referring domains, HeyKeywords showed **~1,100** referring domains / **2,700** backlinks, SEMrush showed **~1,300** referring domains. Ubersuggest routinely overstates volume (one term: **3,600/mo** on Ubersuggest vs. **750/mo** SEMrush vs. **600/mo** SE Ranking). Treat any single tool's absolute numbers as directional only; the "who is actually ranking for what" data is the part that's reliable across tools.
- **Set the country filter correctly in every tool, every time.** Data is "very different" per country for the identical term; a wrong country setting silently skews volume, difficulty, and traffic. Set to the country you want to rank in, not necessarily where you live.
- **Refresh cached data before trusting it.** SEMrush/Ubersuggest/Ahrefs show cached data (sometimes weeks or years stale); a keyword showing "N/A" difficulty just needs a metrics refresh (one term went N/A → 38% after refreshing). Click "update"/refresh to force current numbers.
- **A tool blind spot to know:** around Aug/Sept, Google restricted third-party/LLM tool access to roughly page-1-only SERP data ("Google basically spanked every AI LLM"). A genuine position-24 ranking confirmed in GSC simply won't appear in SEMrush/Mangools-style tools. The disagreement is a structural tool limit, not a ranking failure.
- **AI is a tool, never the decision-maker on strategy.** Claude/ChatGPT are fine for orientation, drafting, sanity-checks, and implementation tasks (writing missing code, generating schema). They are not the final call on keyword targeting, location-page expansion, or architecture: "make the decision not necessarily based on what Claude's saying, but on just what the actual data points are." ChatGPT specifically "will bullshit you," tends to agree with whatever you propose, and has produced keyword-stuffed headings when asked to architect content directly. "You are the expert, you're doing the research."
- **Don't chase 100% on any tool's health score.** 80%+ on a page audit is fine; a 90% site-health score is "fantastic." 100% does not correlate with a #1 ranking, and members with near-perfect scores rank no better than members who don't chase the score. "Sometimes you need that D to help you rank." (Exception: a paid SEO provider's *own* site faces a higher credibility bar because prospects scrutinize it.)

### 1.2 Keyword & competitor research tools

| Tool | Price | Notes |
|---|---|---|
| **SEMrush** | ~$130–150/mo; 7-day (sometimes cited 2-week) free trial | Matt's most-cited paid tool, called "most accurate" for volume/difficulty in most sessions. Genuinely contradictory stance: in one Jun-2026 session Matt says he's "stopped using/recommending it," calling it "way too expensive" post-Adobe-acquisition with reported billing/cancellation horror stories. Trust **Keyword Difficulty**; don't over-weight "Competitive Density." Free-trial trap: cancel immediately, they charge and reportedly don't refund. |
| **Ahrefs** | $129/mo; **Ahrefs Lite $29/mo, 100 searches/mo cap** | Comparable accuracy to SEMrush. **Trust Ahrefs over Ubersuggest on difficulty disagreements 100% of the time.** |
| **Ubersuggest** | ~$29–40/mo; lifetime $290 (individual) / $490 (multi-site) | Cheapest, least accurate, overstates absolute volume. Runs on a lifetime-deal model that's profitable because most buyers quit SEO within a month or two. Good for cheap bulk discovery, then verify the shortlist in a pricier tool. |
| **KeySearch** | ~$24/mo billed annually (~$20/mo), 200 searches/day | Named alternative. |
| **Mangools** | Limited free searches/day | Named alternative. |
| **HeyKeywords** (heykeywords.com) | ~$29–31/mo base (50 keyword + 10 domain analyses); upper ~$31–51/mo (150 + 30) | Matt's own tool, built via Claude Code over a weekend; pulls volume live from Google Ads (the source every other tool re-estimates). Discount code **HTKEYWORDS** = 50% off first month. Known gap: per-page backlink lookup returns 0 on pages that do have links. |
| **Google Keyword Planner** | Free | Directional only. **Don't use Google Trends to judge search volume** ("no, don't use that") — use a real keyword tool. |

- **Read the SERP's backlink profile, not just KD.** Referring domains, not raw backlink count, is the metric that matters ("backlinks are expensive... if I can avoid it, I will avoid it at all costs"). If the actual #1 page for your target has 0–2 referring domains, the keyword is winnable with zero link-building regardless of the tool's KD number.
- **KD ideal range: 0–15/20%; up to 25% "still possible"; 31% is "a little more difficult than I'd like"; ~90–100% is unwinnable for a low-authority site.** KD reads roughly as the domain authority you'd need to rank page 1. National KD can badly mislead local intent (a term can show KD 88 nationally with no single city accounting for that volume).

### 1.3 Question / topic discovery tools

| Tool | Notes |
|---|---|
| **answerthepublic.com** | Free: 1 search/day no account, **3/day with a free account.** Type the broadest version of what you sell → **Search Engines → Questions** → List view (skip the wheel). **Skip page 1; use page 2–4** (competitors rarely click past page 1). Scroll further for a **hidden Bing question set** most people miss (Bing = ~4% of global search; ChatGPT pulls from both Google and Bing). Set region to United States for volume. Crashes under heavy live load. |
| **Google "People Also Ask"** | Fully equivalent substitute — same method, same quality. Also check "People also search for." |
| **findquestions.com, alsoasked.com, answersocrates.com** | Interchangeable question-finders; type in what you sell. |
| **HeyTony Blog Idea Finder / Reddit Keywords tool** | In-platform. Reddit tool crawls subreddits for a seed term → returns questions + keywords + pain points + content ideas + source subreddits. Especially strong for LLM/AI-answer visibility, less so for classic Google rank. **Even when tools show zero volume, an active subreddit thread or a PAA box is proof of real demand.** |
| **rankweektraining.com, app.rwideas.com** | Matt's own question portals. |

### 1.4 Site & page audit tools

| Tool | Price | Use |
|---|---|---|
| **pageaudit.com** (+ "PA" Chrome extension) | Free forever | Cost Matt $30–40K to build, given away to lower the barrier; load-tested to ~20,000 concurrent. Content tab (word count, keyword occurrences, density), Metadata tab (title/meta), Overview tab (keyword presence in title/meta/H1). Extension has "Copy All Headings" and can sometimes see JS-rendered content the crawler misses. **Always ignore the overall score/percentage.** |
| **audit.heytony.ca** (Site Audit Tool / Rank Report Card) | **$10/mo or $99.99/yr, up to 3 sites** | Full-site crawler (~1 hr per crawl, 24-hr recrawl cycle): duplicate/missing tags, page speed, orphan pages, broken links, canonical/sitemap mismatches, missing H1s, low word count. Buckets: **Serious / Warnings / Info**, each with an embedded how-to-fix video. **"Manually validate"** clears false positives (e.g. a live link a bot couldn't reach). Does NOT do keyword research. Rotating discount codes each cohort (all mechanically identical, 1 month free, card required, cancel before renewal): RANKWEEK10, rankweek2026/RANKWEEK2026, June2026. |
| **HeyTony Watchdog** (watchdog.heytony.ca) | **$10/mo, 3 sites** | Real-time competitor *change* monitoring (title/meta edits, word-count shifts, pricing changes, pages added/removed, link changes) with a before/after diff. Catches you up in near-real-time instead of 3–6 months later via lagging rank trackers; surfaces unlinked "hidden" competitor pages. |
| **Money Page Doctor / Analyzer** | In-platform, **capped 20 audits/mo** | Paste a money-page URL → ~10-sec competitor-gap read (infers keyword, IDs competitors, flags word-count/density/keyword-mismatch/"blog detected but competitors are service pages"). **Always check where you actually rank before acting** — if already ranking well, don't touch the page just because it flags a gap. Reported competitor word counts can be flatly wrong (2,200–3,400 that couldn't be found on the page). |
| **Keyword Conflict Detector / Cannibalized Keywords Scanner** (+ keywordconflict.com) | In-platform | Auto-pulls sitemap, flags 2+ pages targeting the same keyword. Scan capped ~50 pages/run (bump toward 500). Not 100% accurate — cross-check flagged URLs against sitemap.xml/robots.txt; if absent from both, they're redirect artifacts, not real pages. |
| **Detailed SEO** (Chrome ext.) | Free | Non-caching; instantly shows live title tag, meta description, H1 count, OG/schema. Use to verify actual HTML vs. what Google displays. |
| **wordcounter.net / characterCounter.net** | Free | Verify real word count/keyword density on any AI draft — never trust the AI's self-reported numbers (one demo targeted 2,200 words, delivered ~1,700; targeted 20–45 keyword uses, delivered 13). |
| **whatcms.org / BuiltWith** | Free | Identify an unknown site's CMS / which CDN it runs. |

### 1.5 Other HeyTony Insiders tools (app.htinsiders.com)

Separate login from the community; sign up with the **exact same email attached to your Stripe subscription** (case-sensitive — a mismatched capital or typo silently fails to match). Add your site + set search country first. Full suite: **Blog Post Writer bot** (Claude-powered, interviews you ~7–10 questions, follows Matt's rules — **hard cap 10 generations/account**, and a *failed* generation still burns a slot), **Blog Idea Finder**, **Reddit Keywords**, **Topic Cluster Analyzer** (what Google thinks the site is about vs. what you wrote), **Link Gap Analyzer** (linkgap.io — backlink gaps vs. a competitor, email-gated full report), **Money Page Doctor**, **Keyword Conflict Detector**, a sitewide per-page target-keyword guesser. Built-in **AI help / "Wisdom" search** answers natural-language questions from the full call/transcript archive with source links. Coming: "Matt Bot 3000." Support: **support@heytony.ca** (Angela), not Matt's DMs.

### 1.6 The AI model stack

- **The dominant split: ChatGPT for the voice/interview capture, Claude for the actual writing.** ChatGPT's Whisper voice-to-text is "the best of the best." Claude "writes like a person," follows word-count/format instructions far more precisely, makes conservative edits on rewrites (vs. ChatGPT's over-rewriting), and is markedly better at spreadsheets/data (one member burned 5+ hours in ChatGPT on an Excel task Claude did almost instantly). Matt's recommendation shifted over time: "for writing, for everything... I recommend anybody get away from writing from ChatGPT, go to Claude." ChatGPT is still preferred for image generation and brainstorming.
- **Any LLM works for the interview/draft loop** — ChatGPT, Claude, Gemini, Grok, Copilot, Perplexity are interchangeable for that step. Gemini (free tier) is notably strong at meta-description length compliance and GBP-aligned copy, and at image generation from reference photos.
- **ChatGPT reasoning setting:** use "Instant" for the fast Q&A stage, "High" for the actual writing stage. ChatGPT degrading to one-line answers after ~10 posts in one thread is fixed by switching effort level or moving to Claude.
- **Cost:** Matt runs Claude, Claude Code, ChatGPT, Manus, Gemini — "a fortune in AI subscription fees," ~a couple hundred dollars/month. Claude's annual plan is cheaper than monthly. ChatGPT's ~$20/mo tier roughly doubled his output over the free tier.
- **Claude Code builds tools and on-domain pages, not the whole website.** Matt (a non-coder) built the entire htinsiders.com suite, HeyKeywords, and Money Page Doctor with it: "I don't know how to code, guys. I'm literally working with AI to do this for me." Use it to build a page *in your existing CMS/theme* so the code pastes into your native editor and stays on your own domain — don't run a website *on* Claude Code as the platform. Back up before letting any AI touch theme/functions files. (Its capacity estimates aren't reliable — it promised ~200 concurrent users on a tool that queued badly on the live call.)
- **Reviews micro-site build (see Don'ts §4 for the caveat):** dump review screenshots into Claude/Claude Code, describe the business, "here's what I like, build this out," host on Railway (~$5/mo) or Netlify. Transcribe reviews as real text, never post them as image/JPEG.

### 1.7 The exact prompt library

**Interview / clarifying-questions prompt** (the spine of the whole method; question count varies 5–10 by version). Cohort C / current canonical:
> "I'm writing a blog post answering this question. [paste in the question you found] Ask me five questions you need to know the answer to in order to write a truly unique and helpful blog post. It should include my expertise, experience, case studies, opinions, etc. Ask me the questions one at a time and wait for my answer before asking me the next question."

Fuller 10-question variant:
> "I'm writing a blog post answering this question: [question]. Ask me anything you need to know the answer to in order to write a blog post that is truly helpful and unique. It should include my experience, expertise, case studies, examples, opinions, etc. Keep it limited to 10 questions. Ask me them one at a time. I'll be using voice mode to answer them. Give me time to breathe as well before going to the next question."

- Answer via **voice mode** one question at a time (2–3 sentences each; rambling is fine, it "trains" the AI to your voice). If it defaults to ~30 questions, cap it: "ask me only 10 questions."
- Repurpose a transcript/podcast/video by appending: *"Here's a transcript from a conversation I had. Use that information when you can and where you can to pull my expertise, experience, all that kind of stuff."* Never hand over a raw transcript and ask for "a blog post."

**Write-the-post prompt** (current canonical, strips AI formatting clutter):
> "Write this as a clean WordPress ready blog post using my expertise, experience, opinions, stories, etc. Use H2 and H3 headings only. No horizontal rules, section dividers, tables, callout boxes or other formatting elements. Just headings, paragraphs and bullet points where appropriate."

**Meta description prompt:**
> "Write me a killer, compelling, click-worthy meta description for this page." (Generate ~5, pick the best.) Title tag: *"Write me a title tag for this page under 60 characters. The focus keyword is [X]."*

**Cover/featured image prompt** (attach 2–4 on-brand reference images):
> "Using the style of the images attached, create me a featured image for this blog post. Here is [topic] — you don't need any text on the image. Make sure not to include any of the exact images that are in these; make new ones in that style."

**Internal-linking prompt** (sitemap-based, Cohort C verbatim):
> "I'm looking for 3 incoming internal linking opportunities to this service/product page: [LINK TO PAGE]. Find me 3 relevant opportunities from my sitemap pasted below. [PASTE SITEMAP]"

**Money-page SEO-tags update prompt** (Cohort C verbatim):
> "Here are my current tags and my focus keyword. Update them so the keyword appears naturally, is front-loaded where possible, and matches the style and brand of my business. Also make sure each one is better than my two competitors': [PASTE YOUR AUDIT] Competitor 1 (Same Order As Mine) [PASTE] Competitor 2 (Same Order As Mine) [PASTE]"

**Money-page full rewrite prompt** (Cohort C verbatim):
> "Here is the content from my product/service page: [PASTE]. Here are the top 2 competitor pages that rank for my keyword: Competitor 1: [paste] Competitor 2: [paste]. My focus keyword: [keyword]. Rewrite my page so that: it is clearer, more helpful, and more persuasive; word count is between [comp low]–[comp high] words; keyword density is similar to the competitors; includes the keyword in natural positions; adds missing topics my competitors include; improves structure, readability, and expertise; keeps my brand voice; uses headings where appropriate; does NOT keyword-stuff. Produce the final optimized version I should publish."

**Section refinement prompts** (same thread): "You forgot these heading two tags, write a couple paragraphs each and expand on the ideas." / "Can you rewrite this section to be more funny and personable?" / "Ask me five questions to write a better unique piece of content using my expertise, experience, etc."

**Money-page identification:** "I am a realtor, what would be my money page?"

**Platform-mechanics (get unstuck on any CMS):** "How do I add a link to a blog post or to another page on my site from highlighted words?" then name your platform. General pattern: screenshot the screen/error, upload it, "Where do I click? What do I do?" + "Talk to me like I'm an idiot."

**Bot-blocking diagnostic:** paste the page URL into ChatGPT, Claude, and Google with "How many words are on this page?" Re-run once. If it consistently returns far fewer words than the real page (and title/meta come back "server not verified"), the host is blocking bots.

**Knowledge-base seeding (carry context between AIs):** "I want to make a .md file that has everything you know about me and everything that another AI would need to know in order to operate the same way that you do with me." Paste the result into Claude as standing context. Also: "Make me a document that will teach any AI everything you know about my business." Keep a client's knowledge doc to ~25–30 pages, not 50 — context overload dilutes output.

**Mining client-call transcripts:** "What are all the questions and answers that happened in these calls?" — "a gold mine for content."

**E-A-T self-audit:** after editing content, paste it to Claude/ChatGPT and ask for a grade on each E-A-T category plus specific improvements.

### 1.8 PR, backlink & local tools

- **AB Newswire** — press-release distribution: **$80** web-only, **+$30 USA Today add-on = $110** (recommended tier), **~$500 bulk credit** ("the 501") for repeat testers, or a ~$400 premium tier for ~20 placements (AP News, USA Today, Benzinga, Globe and Mail, Barchart). **EIN Presswire** — $149/release, a June promo bundled 7 for ~$500.
- **featured.com** (HARO successor) — journalist queries; batch 20 min/day. **HARO** — free, ~3 emails/day.
- **thehoth.com** — paid backlinks, $175/link tier (DR/DA 20–30+). **GetMeLinks.com** — $500/mo = 3 guest posts on DR 30 sites (~$166/link). **HOTH.com** — "good, but not cheap."
- **BrightLocal** — HeyTony's preferred local/citation tool (~6 years): **$2/citation, ~$180–200/round or ~$200 flat, one-time.** Also GBP post scheduling and local rank tracking.
- **Geo Imgr / "Geo Imager"** — image geotagging (5 free/day or ~1,000/mo paid). **whatismycid.com / Plerdy** — retrieve a GBP CID link.
- **Google Analytics (GA4)** — the only place to see AI-referral traffic (session source contains "chatgpt"/"claude"/"perplexity") and non-organic channels. **Looker Studio** — free GSC+GA4 dashboarding. **PageSpeed Insights** (pagespeed.web.dev). **Bing Webmaster Tools** — one-click GSC import, supports IndexNow.

---

## PART 2 — LOCAL SEO

### 2.1 The page-vs-post dividing line

- **"We offer this service in this town" = a dedicated page. "X vs. Y" / comparison / informational / local-color content = a blog post.** A brand-new business location gets a page, not a post. Static/evergreen info meant to rank for a money keyword = page; a specific one-off question = post.
- **One keyword = one page = one service = one location, always.** Never build one page for the same city targeting two services ("you're not even getting a slice"). Never combine multiple cities in one post — cycle city by city.
- **Adding a location makes it a whole new keyword.** "We buy junk cars Dallas" and "...Houston" are not cannibalization no matter how similar the template, *provided* the location-specific body copy is genuinely substantive.
- **"Near me" is never a target keyword.** Google connects searcher + business location automatically. Targeting "near me" literally in copy or URLs is "the sign of somebody who doesn't know how to do SEO" / "amateur SEO." Support proximity with real local signals instead (explicit service-area names, a visible address).

### 2.2 Location-page architecture

- **Homepage = your true home-base/flagship market** on the single service that makes the most revenue. Home base can carry one page per service ("Chicago Newborn Photographer" AND "Chicago Family Photographer"); every *satellite* location gets only ONE service page (the one easiest to rank there), mentioning other services in passing.
- **City-size sizing rule:** a ~500,000-population city (Hamilton ≈ **15,000 small businesses**) justifies targeting the whole city as the geo-modifier. A 3–4 million metro (Toronto) is too big — go **neighborhood-level** instead (people won't cross a huge city for a local service). Neighborhood pages work the same for named sub-areas ("junk removal Leslieville," "landscape lighting Montreal").
- **Prioritize smaller towns/suburbs over the big nearby city** — almost nobody targets them, and a location page usually cannot outrank a real local competitor's homepage (their de-facto money page, most-backlinked page) without dedicated backlinks. A Toronto-area photographer was told to drop "GTA wedding photography" entirely for "Toronto wedding photographer," then build individual pages for Hamilton, Stouffville, Mississauga, Oakville, King City.
- **Too small/new to rank at city level → target state-level keywords first, then build pages for the top 10–20 highest-population cities.** A brief mention + link at the bottom of an otherwise-generic post ("if you're looking for website design in West Virginia →") is enough; a full hub/pillar structure isn't required.
- **Service-area hierarchy, not a flat link dump:** top page lists sub-regions/counties → each links to a county page listing its towns → each town gets its own page (which can list neighborhoods). One case replaced a flat list with ~10–20 pages.
- **Avoid the combinatorial explosion.** Don't build every location × service (one case would have been 66 pages: 25 cities × 6 event types). Build one page per location with sections per service, and only build a dedicated combo page where keyword research confirms real volume (~5 of 66 in one case). A ~200-page HVAC service×city matrix was flagged as overreach.
- **Location pages must be genuinely unique per location** — real landmarks, venues, funeral homes/hospitals/high schools (for a florist), delivery-time specifics, seasonal color. **"You need 100 original, my friend."** Copy-paste-with-city-swapped at scale risks demotion. For non-delivery/remote services, anchor each city page in genuinely local hooks (nearest hospitals, local grocery stores carrying your product, local gyms/trails).
- **Rollout: ~1–2 unique pages/week.** A 12-location build finishes in ~3 months without burnout; even a huge client is paced at ~2/week ("sniper rifle" over "shotgun"). **Stop once a subset is already ranking/converting** — you don't have to finish the whole list. **Expect 3–6 months (up to a year) for a new location page to move.**
- **Nav:** a "Locations" hub in header/footer → hub lists every location → each links to its page. Link new local pages directly from the homepage ("areas we serve") to index faster; footer-only links index slower. Nest location pages under a standalone Locations hub, never inside one service page.
- **Layer local into broad content:** even a broad how-to post should carry a local CTA with an anchor link ("If you're looking for a hairstylist in Denver, [link] give us a call") plus NAP in the footer and a link to your GBP.

### 2.3 Google Business Profile (the full playbook)

- **GBP post formula:** target keyword at the very top (optionally in quotes) → link to the specific service page you want that keyword to rank for → your CID link → a link to your *previous* GBP post at the bottom (chain posts together). Roll the chain forward with each new post. Signals an active, interconnected profile.
- **Getting your CID link:** Google Maps → your business → Share → copy → paste into whatismycid.com (or the Plerdy plugin, or View Source + find "ludocid"). A GBP gets a permanent CID ~2 weeks after creation that stays valid "for life." Matt's claim: the CID link passes authority where a generic Maps place link doesn't. Reuse it in blog posts, service pages, and as the linked business address on your site.
- **Posting cadence: at least 2×/week (Mon/Wed/Fri is the working minimum); 1×/week is the floor.** One aggressive test case ran 6×/day. Purpose is primarily to signal Google the profile is actively maintained; a scheduling tool counts the same as posting manually. Posts don't need to be promotional — a tweet-length weekly summary works; start every post with the exact keyword you want the profile to rank for.
- **Service description: 300-character limit.** Work the city/keyword in **once** per listing in natural copy; never repeat it across every service entry; never put a street address in the description text. Fill out **every** listed/suggested service with a brief keyword-rich description. Caution: listing *more* services than your website documents can read as padding — audit for a services/website mismatch.
- **Photos:** batch ~10, then wait a week to a month before the next ~10 (steady, not one dump). Recommended **1,000 × 1,000 (square)**. Geotag to the service location.
- **Recheck the description and full profile monthly** — descriptions get silently declined or publicly edited "through no fault of your own." Regularly delete irrelevant auto-added services (real case had "telemarketing" and "magazine printing" auto-added).
- **Profile must be set to public** (a silent "not public due to missing information" error can block visibility for months). Profile strength can drop 100% → 80% on its own; clicking "complete" routes to Google's paid ~$27/mo bundle and doesn't restore 100% free.
- **Verification:** fully online-only/no-service-area businesses get rejected; multi-location now often requires **video verification** (recording yourself entering each building). A **service-area business** (no public address) is allowed and can upgrade to a physical address later without restarting. A second GBP at the same street address generally needs proof of a physically separate entrance (a window sticker sufficed once). Don't publicly list a home address in schema/GBP for a remote business (safety).
- **Never click "Apply All" on Google's recommended edits** (GBP services or Google Ads recommended changes) — a client did both and rankings + ad spend went sideways.
- **A GBP with zero website can outrank fully-built competitors** in local results — for a business with no web presence, get a real GBP live before anything else. Missed/unanswered calls hurt local rankings (Google reads poor call responsiveness as a bad outcome). The GBP pin must sit at the actual physical address (a Mexico rental targeting US bookers still pins in Mexico).
- **Rename a GBP freely** (e.g. add "Bookkeeping") if every local competitor has the service word in their name and you don't — Google may delay it, but it should go through, and it keeps existing reviews. A name change tied to a DBA/press release is safe to run in parallel (if declined, it reverts, no suspension).
- **GBP appears to have little pull on AI-answer results** in Matt's own repeated testing — treat it as a discovery/local-pack asset, not an AI-visibility lever.

### 2.4 Citations

- **Do local directories with a real physical presence/service area** — chamber of commerce, local newspaper, local business directory (they send local-relevance signals). National/global generic directories are lower-value but not harmful. **Never sign up for directories in a country you don't operate in.** Skip local directories entirely for a nationally-shipped ecommerce brand with no storefront.
- **BrightLocal builds citations at ~$2 each** (~$180–200/round, one-time, no ongoing management). **brightlocal.com** also auto-submits to a batch of directories. Also import to **Bing Places** (from GBP, ~2 min) and **Apple Business Connect** (needs a DNS TXT record; include "www" if your site uses it). Pull a dominant competitor's backlink/citation profile and get listed on the same ones — "they've already done the work for you."
- **Yext is an API overlay — you never own the citations.** Stop paying and they disappear (one case: an annual plan built "4–5 pages," a year later only 8 citations remained). If you manage fewer than ~10 citations through Yext, take them over yourself. If migrating to BrightLocal, turn OFF Yext's sync toggle for anything BrightLocal manages or Yext will overwrite it.
- **Never say the word "backlink" to a non-SEO person/org.** Ask: "Can I include a link to my business on your site/directory/profile?"

### 2.5 Reviews, reputation & the map pack

- **Never review-gate.** No NPS/1–5 pre-screen before sending a review link; that includes a CRM automation that pre-screens sentiment. Google can **ban the entire Business Profile.** Always send a direct, unfiltered link straight to the GBP.
- **Never ask for a "5-star" review — just ask for "a review."** A QR-code business card + a small incentive (e.g. 10% off next service) is fine; specifying the rating is not.
- **Avoid in-person QR-code review asks** (a customer or competitor can report it and get the whole account shut down); text/email the link later once the customer is home — the Google-approved, more-honest pattern.
- **Review pace beats volume, especially for professions that can't ask clients directly** (therapists/counselors → colleague character-testimony reviews). ~1 new review/week; ~6 months of 1/week can outpace a stagnant competitor with more total reviews.
- **Sudden review clusters are a red flag** (5 within 20 minutes), especially if reviewers aren't local — Google sees reviewer IP/location. **Stop "review trains"** (groups trading review requests) — reads as gaming, gets reviews taken down, and drags down other legitimate reviews as collateral. General rule: **"if it feels sneaky, don't do it."**
- **Never use a review-carousel plugin** (adds ~1,000 words of markup, hurts load, users scroll past). Hand-paste 2–3 real reviews as plain text on each money page, rotating which appear where. **A review screenshot is fine for human trust but Google can't read text inside an image** — embed the review's actual text if you want it to carry SEO weight. AI-drafted review replies are fine (review before publishing, don't auto-post).
- **Map-pack playbook (the recurring winning pattern):** post to GBP ≥2×/week; geotag every photo with the target keyword in the file/metadata; CTA/click-to-call + website link on every post; chain posts via previous-post share links; build service-area pages linked to matching GBP service categories; ask for reviews continuously. One case sustained this ~1 year across two locations for a "very consistent lead generator" — but a decades-old, completely inactive competitor can still outrank it "by a mile" on longevity/authority alone.
- **Diagnosing a dropped map-pack position:** check whether you changed anything; compare review count AND **velocity** vs. competitors (velocity can beat higher total count); confirm citations; confirm crawlable NAP in the footer linking to the GBP via CID; check GBP services match/exceed the website; factor in that Google updates its map-pack algorithm independently.
- **Geotagging is genuinely disputed** — ChatGPT calls it "one of the most overrated tactics," Google strips EXIF on ingestion, yet Matt's agency reports correlated results. Test on 1–2 clients, keep it if it correlates; the cost is low enough to run regardless. Fundamentals (more reviews, complete GBP, regular photos, a good connected website) come first.

### 2.6 The local + broad-content tradeoff

Out-of-area traffic that can never convert locally is still worth it — it costs nothing extra and builds engagement/authority signals (time on site, page visits, form fills, newsletter opens) that indirectly help your local/transactional rankings. "If I'm getting traffic from five towns over, somebody's not going to hire me. That's totally fine. That is helping my website show up higher in my local area." Do **not** jam your target city into general how-to posts to force geo-relevance — one member's edit inserting a town name into broad-ranking posts (on ChatGPT's advice) dropped traffic; reverting all affected posts at once is fine, give it 1–2 months.

---

## PART 3 — ECOMMERCE

### 3.1 Homepage / collection / product keyword split

- **Stop trying to rank the ecommerce homepage for one keyword.** Give each featured product a clean homepage section with descriptive text; push actual ranking onto **collection and product pages.** The homepage just needs to make a visitor understand what the site is once they land from an entry page.
- **Collection page = the broad, competitive keyword** (repeated in the collection title, every product title in it, and body copy). **Product page = specific/attribute-based** ("polyester paddle shirt," "18-karat gold engagement ring"). Reinforce a collection by repeating its exact keyword phrase in every product title inside it.
- **Shopify collection pages CAN and do rank** (unlike blog category/tag pages, which basically never do) — optimize them like money pages.
- **You cannot rank for a keyword without a page built around it.** "Everybody's trying to get through the front door... I want to go through the back door where nobody else is going." Put high-intent/transactional terms ("Scorpio candle," "buy ghost peppers hot sauce") on collection or product pages, not blog posts.
- **Rough volume floors for a low-authority site:** product pages ≥ ~30 monthly volume, collection pages ≥ ~50 (can go lower for a brand-new site). Singular vs. plural can carry very different difficulty — check both ("tennis t-shirts" KD ~16 vs. "tennis t-shirt" KD 8 at higher volume; the singular won).

### 3.2 Shopify collection-page structure

**"The biggest missed opportunity when I look at a Shopify store":** intro sentence(s) → product grid → long blog-length paragraphs with images underneath, covering the collection in depth. Put marketing/info copy **below** the grid, never above it (someone on a collection page is ready to buy, not read; especially on mobile). Add real product photography (a person using/wearing the item) with descriptive alt text.

- **FAQs on collection pages first** (broadest reach, far less labor than per-product), built as Shopify's native collapsible-row component. Write them as plain H2 questions (not labeled "FAQ") answered in natural human language that reincorporates the keyword a few more times ("How long does the temporary tattoo last?"). Two payoffs: preempt purchase-blocking questions (conversion) and feed long-tail/AI search, since people now type full sentences. For near-identical SKUs (jewelry, collectibles), write product-specific FAQs (carat, metal, care) — **never duplicate the same FAQ block across every page.**
- **Use the native blog, skip third-party blogging apps.** Shopify blog pagination often defaults to 6 posts/page — set to ~30 (then 60, 100 as it grows). Ensure every post has a featured image.

### 3.3 Product naming, keywords & duplicate SKUs

- **Name products what real searchers type, not invented brand language.** Type the plain physical/functional description into a keyword tool, find the phrase with real volume + low competition, and rename the actual product title (not just alt text) to that phrase; append the cute/brand name at the end, never the reverse. Cases: a "cream beaver fur hat" under a made-up name → "beaver fur top hat" (260/mo Canada, 880/mo US); Irish-named candles → "Vanilla Soy Candle" (~30/mo) with the Irish name appended; a product filed under generic "novelty bongs" → "octopus bong." Get explicit client sign-off before overriding a preferred name.
- **Novel product with no search demand:** don't force the keyword nobody Googles — identify the underlying problem the user searches ("nobody buys my book, what do I do") and build content around that. Or write an "[established competitor product] alternative" page.
- **Portfolio strategy when no single head term has enough volume:** build many small transactional variants (per zodiac sign, per birth month, "funny tennis shirts") plus one hub/master post linking to each. "Cosmos Within" candle brand: "horoscope candles" ~19 KD/~110 mo, "Scorpio candle" zero difficulty.
- **Duplicate content across near-identical SKUs/locations:** for low-stakes near-duplicates (an escape-room booking page for Anaheim vs. Connecticut), differentiating only the title tag + meta description ("Booking — Anaheim") can be enough. A page meant to independently rank for its own local keyword still needs genuinely unique body copy.
- **Multi-niche stores** (tennis + padel + horseback apparel) create real per-niche research friction — each niche needs its own research and doesn't share an audience — but can work under a unifying "sports" frame.

### 3.4 Seasonal, reviews & pipeline

- **Publish supporting content BEFORE the thing is ready** so it's indexed and ranking when demand hits. A florist should optimize for major gifting holidays ~6 months out, not a month before; a Super-Bowl-driven location page starts ~6 months ahead. Write "gifts for a May birthday" months before that demand spike.
- **Seasonal/annual pages:** keep ONE evergreen URL with no year in it; update the title/meta/H1 to the new year each year (2026 → 2027) rather than making a new page — preserves accumulated equity. Never put the year in an evergreen URL.
- **Seasonal money pages:** build a dedicated page per key season (Black Friday, Christmas, Valentine's); keep the URL live year-round but pull the nav link out of season (Google still knows the URL exists).
- **Reviews are a direct ranking factor for ecommerce product listings** — a product with ~5,000 five-star reviews gets surfaced above comparable products with fewer/weaker reviews.
- **Blog-to-paid-product pipeline:** publish the free/shorter version as a blog post, then sell a longer detailed version as a standalone paid guide (Jackie's curly-hair guide sold to people who never come in). **Turn a recurring support question into a reusable asset** — write the how-to once, send that link to every new customer (Matt's team's "how to add/remove users from Meta Business Manager" post replaced a 30–60 min onboarding call for every new client and later earned organic traffic).
- **Directory/aggregator SERP:** if directories outrank you, get listed on them (free) rather than out-content them — it sends a legitimacy signal. **GBP for ecommerce** is only for a real storefront/service area — a nationally-shipped brand skips it.

---

## PART 4 — TRADEOFFS & DON'TS

### 4.1 The cardinal rule: never touch a page that's already ranking

The single most-repeated rule in the entire body of teaching, stated independently and forcefully in nearly every call: **if a page is ranking for anything — even a keyword other than the one you intended — leave its content and URL alone.**

- It applies **even when the page violates every other rule**: duplicate H1s, keyword stuffed 122×, hidden overlay text, thin content, zero backlinks. "I don't give a shit if you have 31 heading one tags when you should only have one. If you have 31 of them and you're ranking number one, I'm not touching that page." / "If it's ranking, don't touch the text. I don't care if it doesn't match your brand guidelines."
- **You can't rank higher than #1 — touching it is pure downside risk.** Proof: Matt's own "SEO in Hamilton" page hit #1 after ~1 year on internal links + anchor text alone, never edited ("did anybody touch this page? All we did was internal link to it"); his web-design page held #1 for ~2 years on 600–800 words. The trigger to re-audit is *after* rankings actually drop, never before.
- **If it's #1 but converting poorly:** tiny incremental edits only (one sentence, one button, a CTA). UX/CTA polish is the one still-safe category — never a full content rewrite.
- **If it's ranking but flat-traffic:** don't rewrite it; keep publishing easier-keyword blog posts and internally link them to it.
- **If it's NOT ranking:** wait 3 months, then 6 months (internally linking with descriptive anchor text meanwhile) before touching content. Only rewrite from scratch once you're sure it isn't ranking. "Most of the time, if you're not ranking, you're either doing too little or too much" — resolve by comparing against the actual top 3, never a fixed rule.
- **Freshness-gaming caveat:** Google sometimes deliberately suppresses a newly-published/updated page, then waits to see if you panic-edit (which itself reads as a spam signal). Give a page ~1 month after publishing/editing before touching it again.

### 4.2 The consolidated Don'ts

**Don't**
- **Don't chase 100% / perfect scores** on any audit tool (Page Audit, Yoast, Rank Math, accessibility). 80%+/90% is enough.
- **Don't disavow backlinks. Full stop.** "In all the years I've been doing SEO, we have never disavowed links... never." Some clients who disavowed after a scary flag saw rankings drop — a "toxic" link may be secretly helping and there's no way to know which. Dilute (build more good links) instead. Only consider disavowing if the domain has no real traffic/rankings to lose.
- **Don't act on "toxic"/"suspicious" backlink flags by default.** Verify a flagged link is even real (View Source + Ctrl-F your domain; cross-check GSC Links vs. the tool). Spam-score benchmark: stay under ~11%, ideally ~1% (you can't hit 0%).
- **Don't buy cheap backlinks from Fiverr** or reply to unsolicited backlink-selling emails. Ignore bulk-link spam ("100 links"). ~90% of paid link-selling is low-quality spam. The only real "Google partner" status is a Google Ads partner — nobody has special algorithm access.
- **Don't reciprocal-link.** "As soon as you link back to the person, you're destroying the link equity you're building." Getting 10–20 sites to link to you while you link to none is fine. Use **ABC linking** (A→B→C→A) not direct A↔B swaps. Stop friend-group "private blog networks" and "review trains" immediately.
- **Don't use "near me" / zip codes / "near you"** as target keywords or in copy/URLs.
- **Don't keyword-stuff.** Match the actual #1 competitor's exact-phrase count "plus one," never wildly exceed it. Higher density does not equal better rankings — Google increasingly reads heavy repetition as over-optimization (Matt's own page dropped #1→#9 at 5.04% density / 35 uses vs. competitors' 1.76% and 0.9%). Even when a competitor ranks *with* stuffing, don't copy it — they only got away with it because the keyword had near-zero competition; copying it risks a penalty for no benefit.
- **Don't use hidden text** (font matching background), a duplicate desktop/mobile H1 hack, or hover-hidden keyword text — Google reads it as cloaking/gaming ("Google does not like this"). Matt cites his own mobile/desktop dual-H1 hack as the cause of one page's drop.
- **Don't change a URL that has any ranking, traffic, OR backlinks.** All three must be "no" before it's safe. A changed URL is a brand-new page to Google that starts from zero, and even a textbook 301 doesn't always preserve traffic. "Update this with extreme caution."
- **Don't fully automate content creation/publishing.** "It's a slippery slope if you just let AI do whatever." Platforms increasingly detect and label automated content. Spend ~1 hour/day being intentional; use AI to brainstorm/rewrite/generate images, not to publish unsupervised.
- **Don't "humanize" content or run an AI-detector on your own writing** — philosophically backwards. "We don't want to humanize our content. We want to write human content and have AI just frame it." Every piece should come from your real expertise, not "AI slop."
- **Don't block AI crawlers**, even when they overwhelm your server ("how else are they going to recommend it?"). Fix crawl floods with better hosting + a WAF, not by throttling bots.
- **Don't publish a "coming soon" placeholder**, allow blog comments (spam), use tags (thin archive pages), or mass-dump a batch of posts on a live site (Google reads high velocity as spam-like instability).
- **Don't over-check.** "You can look at it every day, but don't make actions on it every day — that's how you lose money, lose credit, lose sanity." Cancel any tool pushing daily rank-change alerts. Check monthly averages.

### 4.3 Gray-hat: acknowledged but not endorsed

Matt names several tactics people run that he explicitly does not recommend and calls out as manipulation: the **reviews micro-site** ("not a white-hat strategy... it is to manipulate the search results"), stuffing the keyword into the **GBP business-name field** ("I'm not recommending you do this"), a **second GBP via a subleased office** in a target city, and the **press-release → AI Overview** play (which sometimes only lasts about a week, and which publicizing can burn — the Edward Sturm/Globe and Mail case had the AI-cited link taken down after a viral video called it "manipulating AI"). The through-line: **"if it seems like you're trying to game the system, don't do it. If it feels bad, if it feels sneaky, don't do it."**

### 4.4 Key tradeoffs (the genuinely unsettled calls)

- **Word count / keyword count / heading count are competition-relative, and cut in both directions.** The same "match the top 3" rule means sometimes trim excess, sometimes add depth — benchmark the *lowest*-ranked of the top 3, not the highest (if #3 ranks with 500 words, aim ~600, not 3,000 because #1 has 3,000). There is no universal "more is better."
- **SEMrush stance is genuinely unresolved** — "most accurate" in most sessions, "stopped recommending it, way too expensive" post-Adobe in another. Both are Matt's real view at different points.
- **Blog cadence 1–2/week is a ceiling for newer sites, not a hard cap for established operators** — experienced batch-writers (CJ) run well above it without being flagged. The ceiling protects sustainable onboarding.
- **Deleting vs. drafting old content:** the safe rule is draft-and-wait 6 months to a year, but Matt's own aggressive mass-delete of 70 posts (no backlinks/traffic/indexing) had zero negative impact. He doesn't reconcile this.
- **Geotagging, custom schema, FAQ schema, and the reviews-microsite are all low-cost, outcome-based bets, not proven mechanisms.** Matt's position on each: "the cost is low enough to test regardless of whether we can prove why it works." Schema and most "AI SEO" tactics haven't moved the needle in his own testing; FAQ schema (after a year of testing) showed no measurable difference and can draw a bot storm.
- **AI citation and organic rank are decoupled** — you can rank #1 and not be cited; AI-Overview citation was only ~30% consistent across repeated identical searches in one test. Don't over-read a single "why did a competitor beat me in the AI Overview" snapshot.
- **Whether to invest in SEO at all is conditional on where a business already converts.** Matt told an attendee thriving via Instagram/events/referrals it was legitimate *not* to prioritize organic SEO; for a novel marketplace, he was openly for partnerships/influencers/community distribution over SEO. "Everybody runs a business in a different way."
- **Aged/used domains carry real but unquantifiable risk** — a clean-looking backlink profile doesn't guarantee no past-owner penalty. Matt now defaults to registering new domains (a client's ~$500 marketplace domain did "all the right things" for a year with zero movement; a fresh domain with the same content ranked within a month).
- **Reverse-engineering a competitor's odd on-page pattern** (duplicate H1s, etc.) is a reasonable experiment only when you have nothing to lose (not ranking anyway) — and keep the actual copy unique.

---

## PART 5 — BUSINESS & MINDSET

### 5.1 The agency model & pricing

- **Flat monthly retainer, never hourly.** Benchmark package (the answer to "what should we charge"): **$3,000 USD/month or more; 8 pieces of content/month** (8 blog posts, OR 8 page updates, OR 8 new pages such as location pages); **4 backlinks/month; ongoing technical fixes; monthly reporting; a dedicated point of contact.** "If they're not charging at least $1,500/month, they can't do enough work for you." Matt's own agency charges **$2,500/month** per client.
- **Two proven client cadences, contrasted:**
  - *With backlink work:* **2 blog posts/week + 4 backlinks/month, nothing else** — the model behind a 3-year anonymized client now at **$1.3M/year**, ranking for ~9,600 keywords, grown from ~$20K/month to $100K+/month (seasonal spikes to ~$200K).
  - *Without any backlink work:* **1 blog post/week + 2 city/location pages/month** — a 3-month engagement that ended with the client "at capacity" and hiring more staff. Delivered via a pre-mapped, client-signed-off content plan (12 blog topics + 6 city pages) and a ~4-general-questions-per-topic interview shortcut.
- **HeyTony's own disclosed cadence: two deliverables/week per client** (one new blog post + one existing service/product-page rewrite), i.e. **4–8 pieces every 28 days**, and **4 backlinks/month** ("that's all we do" and it gets "crazy results" — not 4–10/*week*, "that's too many").
- **Map the full content plan up front** — topics, which pages link to which, which topics tie to which money pages — and get client sign-off before the interview-and-write cycle.
- **Revenue is capped by fulfillment capacity, not lead volume.** More SEO traffic doesn't move the bottom line once a team can't absorb the work; past that point, conversion-rate work and pricing are the growth levers (Matt's own agency: 2.5% lead-to-client conversion, inbound already exceeding fulfillment, now in sales training / considering price increases rather than chasing more leads).
- **List pricing/cost ranges on your own site** even as a premium provider — "if you don't have any prices, you're getting left out entirely" from price-shoppers who will shop regardless. (Nuance: a luxury provider whose buyer decides through an in-person/call experience can validly hide prices — the test is your buyer's actual decision process.)
- **Client auto-publish:** default is pre-approval; ask around month 3–4 whether they'll allow auto-publish. Clients who allow it "typically get the best results."

### 5.2 Cadence, patience & the compounding game

- **Cadence: 1–2 posts/week, max.** One/week is "fantastic," two is "great," 1/week is a genuine baseline (not an inferior fallback), and **never both on the same day.** Daily/365-a-year is "too much" (reads as AI-spam churn). New-site launch can batch ~5–6 (or ~10, then drip 2/week) — the exception, not live-site practice.
- **SEO is a marathon: 3–6 months minimum before a real win, sometimes month 12–14 even when monthly gains looked flat.** Ranking within 2 weeks is "magic," not the norm. Insiders following the method report movement in ~1–1.5 months, faster than the typical agency's 2–3 months. New location pages: 3–6 months, up to a year.
- **Check performance ~once a month, not daily.** "Don't look at your credit score every day. Do the right thing every day, and 30 days later, without you looking, it's changed and you can buy a house." Day-to-day rank bouncing is normal noise. "Page 3 is very different from position 3" — don't panic-react to page-level movement.
- **The avalanche / snowball method:** deliberately target small, low-competition, near-zero-volume question keywords first (even 10–20 searches/month), all interlinked. Each barely moves traffic alone, but the accumulated topical authority is what eventually unlocks the harder head keywords the site couldn't touch on day one — and feeds LLM-recommendation visibility. "A KD of 21 is still easy." Google/ChatGPT "start picking us up" as trust compounds.
- **~15% of Google's daily searches are brand new**, never searched before, invisible to every keyword tool (SEMrush/Ahrefs/Moz only show what they've already detected) — and rising. Zero historical volume is not proof of zero future demand; "I guarantee there's nothing too niche that people aren't searching." This cuts both ways: a niche invisible to competitor tools is also harder to forecast/prove ROI on before publishing. "Keyword research is becoming less important than it was."

### 5.3 The mindset that actually decides outcomes

- **The #1 failure mode is quitting too early, not doing it wrong.** "Google does that on purpose because spammers come in... but then they give up, they go away. The people who get results aren't the ones who learn the most in a day. They're the ones who keep going." **Overwhelm is explicitly named as the top cause of quitting** — the whole method is engineered against it.
- **~1 hour a week is enough.** "I'm trying to make SEO so simple that anybody could do it in an hour a week." The 30-day plan is deliberately capped low (fix 5 issues not all of them, 4 posts not more) specifically to prevent the burnout-driven quitting that happens by week two. **Fix 5–10 site-health issues per week, not everything at once** ("you'll be astounded how much progress you make and how not stressed you are"). Fixing a systemic mistake at one or two per day/week, not retroactively all at once.
- **Focus on the 20% that drives 80%; explicitly skip the rest** — schema, FAQ schema, messy HTML, "AI blocks," chasing an audit percentage, running AI-detectors. "That only gets you 20% of the results and takes 80% of the time. I don't want to do that."
- **"Pigs get fat and hogs get slaughtered."** Never grab a whole market/region/keyword set at once. Take a slice, win it, expand. "Do you want to shoot a shotgun and maybe miss, or a sniper rifle and hit the target?"
- **Every page is "a door into your business"** — build one solid door at a time, not a million thin ones that "collapse when somebody walks through."
- **The core litmus test for any content: "Would my customers actually need this? And read this? If yes, publish it."** And after an AI draft: "Am I proud of this?"
- **The real objective isn't the algorithm.** "We don't care about SEO, we care about getting clients — SEO is the way we're doing that." / "The objective is not to game the algorithm, it's to write a piece of content so unique it talks to somebody with that specific problem." / "If the way you're thinking is 'I want to rank because I want people to pay me money' — that's the opposite of how we should think." Write to genuinely help; ranking and revenue follow.
- **AI-written content is NOT penalized** — Google and AI penalize *regurgitated, generic* content, not AI assistance. "Google and AI hate AI written posts. They do not. They hate regurgitated information that's the same everybody else is saying." What avoids the penalty is your own real expertise injected via the interview method.
- **Ranking position obsession is outdated.** #1, #2, #3, anywhere on page 1 all get traffic; "the new SEO" is aggregate traffic from many sources plus being recommended inside LLM answers. Rank in AI tools by ranking on Google first — "if you rank on Google, you will get recommended by AI."
- **Reciprocity is the community norm and the growth flywheel.** "What you put into this is what you get out of it... these are your results, not my results." "All ships rise with the tide."

### 5.4 Proof it works (case-study evidence)

- **Marcus** (pool installation, near bankruptcy 2008, zero SEO knowledge): answered real customer questions nightly → **#1 pool website in the world within 2 years.** The founding story of the entire method.
- **The $1.3M/year anonymized client:** 2 posts/week + 4 backlinks/month, no other marketing, ~$20K→$100K+/month over 3 years.
- **$120K/month blog-only client:** blog content as the *only* channel, ~2–2.5 years to full compounding.
- **The Hamilton therapist:** "write one blog post a week and answer your customers' questions," ~1.5–2 years → 3-month waitlist, fully booked, hiring, no ads, cancelled his Psychology Today listing — while every keyword tool shows **zero ranking** for "male therapist Hamilton," yet he ranks live on Google and ChatGPT for it. Grossing "probably a quarter million a year" off waitlist demand alone.
- **The bin-rental client** (Matt's book's opening): built in school, zero backlinks, heading tags not even done right → ~11 rental bins to **120+** on on-page fundamentals alone.
- **Marvin** (age 76): after 10 months of self-driven SEO with no movement, 4 days of Rank Week took his site from the bottom of page 1 into the map pack; landed a **$799/month recurring** client from a prior Rank Week.
- **Todd** ("Cosmos Within"): search-driven sales up **60% month-over-month.** **David** (Chuck's Garage): broad "common issues" posts drove traffic from <1,000 to 40,000; GSC average position ~13–15 → 5.7. **Peter** (Bulgaria): #1 in six cities for GBP after ~1.5 weeks; site scored 96% vs. a named competitor's 64% after ~3 months on the program.

---

*Cardinal takeaways: pick tools for the job and treat their numbers as directional (GSC is truth); structure local and ecommerce around one-keyword-one-page and the money-page hierarchy; never touch a ranking page and never do anything that "feels sneaky"; and win by outlasting competitors at one hour a week, not by chasing perfection.*
