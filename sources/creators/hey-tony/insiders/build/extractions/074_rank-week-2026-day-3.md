# 074 — Rank Week 2026: Day 3 (Why They Rank, and You Don't)

## Tactics & step-by-step how-to

- **Competitor Gap Analysis process** (the core exercise of the day):
  1. Open ChatGPT (or Claude, Gemini, Grok — any LLM).
  2. Open your Day 2 audit spreadsheet.
  3. Go to heytony.ca/rank-week-prompts/ and copy the full prompt.
  4. Paste the prompt into the LLM — **don't press Enter yet**.
  5. Copy your entire spreadsheet and paste it where the prompt says `[PASTE YOUR DATA TABLE HERE]`.
  6. Press Enter.
- The prompt analyzes **8 dimensions**: title tag, meta description, H1, H2/H3 structure, word count, keyword density, page speed, trust signals. For each dimension with a meaningful gap it gives the exact fix, written out, with a priority flag: 🔴 do this first / 🟡 do this week / 🟢 nice to have. It ends with a **3-bullet Quick Wins summary**.
- **Today's one task**: fix your money page based on the gap analysis — title tag, meta description, H1 first; "most of this takes 5–10 minutes."
- Core theory to internalize (works even without the prompt, "you can do this manually"): whatever your #1 competitor is doing on their page, Google likes — mirror it, then slightly outdo it. Don't just add more (words, keyword repeats) — over-optimizing relative to the competitor who outranks you can suppress rankings.
- **Money Page Doctor** (new bonus tool, Insiders-exclusive this week): paste in your homepage/money-page URL; it crawls the page, infers the correct target keyword (double-checks it against on-page content), identifies competitors, checks their title/H1/density usage of that keyword, and flags gaps — e.g. "keyword mismatch: not found on competitor pages, but competitors appear to target [X] instead," "content is thin, consider adding more words," "keyword density too low/high," "blog post detected — competitors ranking are dedicated service pages, consider building one." Shows a "congratulations, you're already ranking #1" banner where applicable. Runs in ~10 seconds per site.
- **Page speed fixes** if your page is slow: talk to your web developer/designer; use next-gen image formats; shrink image file size (same on-screen dimensions, smaller file); compress images; remove unused scripts; lazy-load images. For deeper how-to, ask the same LLM conversation "how do I do this?"
- **Finding your real competitors** (don't trust an LLM's guess): go to Google, type the exact keyword/question you want to rank for — whoever shows up in results are your actual competitors for that keyword. Repeat per keyword; different keywords will surface different competitor sets.
- **Blog posts that don't read as a "humble brag"** (pricing/informational topics especially): don't write "I'm the best, cheapest, fastest" — go in-depth instead: show a too-long-didn't-read summary up top, price ranges/tiers (e.g., $1,000 / $3,000 / $10,000 / $50,000), a cost breakdown by phase, screenshots of what people are saying elsewhere (e.g. Reddit) about the topic. Can also tell the LLM: "analyze this content and ask me questions so I can make a unique piece."
- **Evergreen pricing-style posts**: don't put the year in the URL. Keep the URL static (e.g. "how much does SEO cost") and update the on-page pricing/content each year in place — changing the URL forces Google to re-index from scratch.
- **Site redesign / URL cleanup rule**: identify pages that are ranking, getting traffic, or have backlinks — leave those exact URLs alone. Everything else can be changed/removed, but must get a 301 redirect to the right page, and internal links must be updated to stop pointing at the old URLs.
- **Expanding to a new/distant city** (different market, ~3 hrs away): recommended to start a separate website (with its own Google Business Profile) rather than folding it into the existing brand — "if I'm opening a business three hours away, I'm going to have another website for it that's all about that location." Same-vs-new brand name is genuine preference (e.g., append the city to the existing name) unless you already have name recognition in the new market.
- **Adjacent-keyword traffic** (e.g., a wedding photographer ranking for "wedding venue" searches): don't fight it — capture it, since the audiences overlap even though the service doesn't match. Tactic: add a sidebar/popup/downloadable guide ("wedding planning guide — step one, hire a photographer") on the pages ranking for the adjacent term.
- **Ranking outside your home city** when Google Business Profile can't help (no physical presence there): build location pages on your own site as the primary fix. (A second GBP tied to a subleased office in that city is mentioned as something people do, but flagged as against the rules — see Rules section.)
- **Non-English / foreign-language sites**: the same framework still applies without reading the language — check where the keyword appears (title, H1, meta, content), whether there's a clear call to action, and whether there's too much/too little info. Running both a native-language and an English version of a page can rank for the same keyword twice and pick up incidental foreign/traveler search traffic.
- **Differentiated/niche keyword naming** (told via a secondhand example): rename the specific product/page to the exact term real searchers use rather than a generic category label (e.g., naming a specific product "octopus bong" instead of filing it only under "novelty bongs") after confirming via research that people search the specific term.
- **Explaining a confusing/novel product or service**: ask actual customers/prospects what wording *they* use to describe it (e.g., "ask them what verbiage they use — what does Jim on the construction site say"), then use that language on the site. Rule of thumb: grade 7–8 reading level — "if you can't explain it to a kid, you can't explain it."
- **Blog cadence**: pick a frequency (minimum 1/week) and hold it consistently; scale to 2–3/week only if you have the time/energy/resources to sustain it — inconsistency (e.g., 4-month gaps between posts) is worse than a lower steady cadence.
- **Multi-line-of-business site structure** (same craft/niche, different product types: finished goods, raw materials, a how-to course): fine to keep on one website as long as the navigation makes the visitor's path unambiguous (e.g., separate "shop," "build your own," "materials" sections).
- **Double-folder / duplicate-path URLs** from an old migration: treat as a form of keyword stuffing in the URL — clean up on any page that isn't already ranking; leave ranking pages' URLs untouched.
- **Refreshing a #1-ranking page that isn't converting**: don't overhaul it all at once. Make small changes only — update a couple of words or a sentence, add a button — because you can't rank higher than #1, so the only real risk is losing the position.
- **Real (non-Chrome) heading structure with JS-rendered pages** (e.g. React + Tailwind not emitting semantic H1/H2 by default): get the framework/AI coding tool to output real H1/H2 elements, then restyle them with CSS to match the desired visual size/shape/color — don't fake headings with styled divs.
- **Suspect/underperforming purchased domain** that won't rank despite a year of legitimate work and no visible red flags in the backlink profile: register a brand-new domain, move the same content over. (See case study — started ranking within a month.)
- **Recommended baseline WordPress stack**: WordPress + the Avada theme ("the number one WordPress theme I think of all time"); add plugins one at a time, searched for as the specific need arises — no fixed a-priori plugin list.

## Rules / dos & don'ts (keep every threshold, number, specific)

- More keywords/repetitions does **not** equal better rankings; using the keyword more times than the competitor outranking you can be interpreted by Google as keyword stuffing/over-optimization and can suppress rankings.
- Whatever your #1 competitor is doing is what Google likes — mirror it and slightly outdo it; don't try to "do more."
- **Never edit a page currently ranking #1, #2, or #3** — "don't edit any pages that are ranking, for the love of God" — even if the information on it is slightly wrong. Wait until rankings actually drop.
- If #1 but not converting: small incremental edits only (a sentence, a button), never a full rewrite at once.
- During a redesign: any URL with rankings, real traffic, or backlinks stays exactly as-is; everything else can change, but must 301-redirect and get internal links updated.
- Don't put a year in an evergreen page's URL — a URL change forces re-indexing.
- Don't trust an LLM's guess at "who are my competitors" — verify by Googling the actual target keyword.
- Money page = the service/info page a visitor clicks through *from* to reach a contact form or intake form. The **contact form/intake form itself is not the money page** — the page that sends them there is.
- Video is **not** required to rank ("Do I need video to rank? No.").
- Hero/background autoplay video: weigh visual appeal against page speed and mobile experience — ask "is that video appealing to you, or is it appealing to a person looking to hire you?"
- FAQ schema: Matt's own stance after "redoing our site for a year" without them — "I haven't found that they're any more or less useful than using them or not using them." Deliberately deprioritized.
- Messy/inconsistent HTML markup (div IDs, data-start/data-end leftovers) doesn't meaningfully matter for rankings — "most websites, the source code, it's just a disaster in the back."
- No platform (Wix, Squarespace, Shopify, WordPress) is inherently closed to Google or better/worse for ranking, provided you have unique URLs, a sitemap, and good content. WordPress just has more SEO features built in by default — but many people don't use them (e.g., overusing default tags creates bloated, non-indexable pages that waste crawl budget).
- Google Business Profile requires a physical location — fully virtual/online-only businesses cannot register one.
- Ranking for an "adjacent" keyword (photographer ranking on venue terms) is not a problem as long as your actual service is clearly stated elsewhere on the site (homepage, service pages).
- A second Google Business Profile via a subleased office in a target city is explicitly flagged as against the rules ("not saying to do this... technically you shouldn't do that"), even though Matt names it as something people do.
- Insiders pricing: **$57/month**, month-to-month, cancel any time — no lock-in commitment. New registrations close **Friday** (end of Rank Week), no exceptions stated.
- The Blog Topic Finder tool (referenced from Monday) stops being public after Friday and moves Insiders-only.
- The Chrome extension itself (pageaudit.com) stays **free forever** for everyone, Rank Week or not.

## Tools, prompts & resources

- **heytony.ca/rank-week-prompts/** — hosts the full Competitor Gap Analysis prompt; available during Rank Week only (screenshot/save it — "keep that prompt, it's yours to use forever").
- LLMs used interchangeably for the prompt: **ChatGPT, Claude, Gemini, Grok**; Matt also referenced testing **Menace AI** (a new AI product by Meta) as something he's currently digging into.
- **pageaudit.com** — the Chrome-extension audit tool from Day 2; free forever, no browser lock-in for using the site directly.
- **Money Page Doctor** — new Insiders-exclusive tool this week; put in your site/URL, get an automated competitor gap read on your money page in ~10 seconds. Not run live for everyone because of processing cost.
- **SEMrush** — Matt's personal daily keyword tool; put a competitor's domain in to see what keywords they rank for and their traffic; **~$150/month**; has a **7-day free trial**.
- **Ubersuggest** — budget keyword-research alternative, **~$30–40/month**; same competitor-domain lookup workflow as SEMrush.
- **Google Search Console** — recommended first check for a struggling blog: confirm posts are actually indexed before assuming content quality is the problem.
- **WordPress + Avada theme** — Matt's own go-to stack.
- **Claude Code** — Matt uses it daily ("I love Claude Code and I'm using it every single day"); built the Money Page Doctor tool with it the night before this call; also uses it to run a weekly independent user-count script for his own analytics.
- **NotebookLM** — one attendee (Josh) discovered Matt via a "how to make an infographic using NotebookLM" post; Matt is planning more videos on free Google AI tools after finding a related Reddit thread the night before.
- **"Ugly baby"** — a tool one attendee (Laura) uses to get real human users to flag confusion/UX friction on her site.
- **Support: SupportTony.ca** — for locked Insiders accounts.
- **Insiders** — $57/month, month-to-month, cancel any time; closes to new signups Friday.

## Case studies / examples / results

- **"Stack Electric"** — hypothetical example site (ranking 5th, page 2) used to walk through the gap-analysis theory against competitors 1–4.
- **Bong shop** (secondhand story, "a friend of mine" did the SEO): a specific product was filed only under a generic "novelty bongs" category; after research showed people searching the specific term, it was renamed "octopus bong" (repeated for other products) — implied lift from matching real search language.
- **Purchased/marketplace domain client** (Matt's own case): client bought a domain for **~$500** on a marketplace; built backlinks and posted blogs "doing literally all the right things" for a full year with zero ranking movement, while comparable clients climbed monthly; backlink profile showed no visible red flags. Fix: registered a brand-new domain, moved the same content over — started ranking within a month.
- **Andy** (UK, "a skeptical old geek," 50 years in software, previously hit and recovered from a **Google Penguin** penalty) — signed up for Insiders within 20 minutes of the call starting. Asked about swapping his 20-year-old domain because a UK competitor's exact-match domain ("trout flies" + fishing gear) keeps them at #1. Matt's counter-example: he personally outranks a competitor called "Hamilton SEO" for the term "Hamilton SEO," showing exact-match domains aren't required to win.
- **Jeff** — did Matt's **December 2025** Rank Week, didn't act for months; during this call revealed he'd just published his first blog post, tied to finally setting up his money pages. Matt: "if you're not in the insiders on my calls on Monday, I'm gonna be pissed because you need a huge kick in the ass."
- **Josh** (auto detailer/ceramic coating) — ran the Chrome extension (had trouble on Microsoft Edge, got it working); discovered his own money page had **5 H1 tags** from careless Squarespace template/font choices.
- **Debbie** — a site migration left doubled folder segments in URLs (double slash / repeated subfolder); treated as URL keyword-stuffing; told to leave ranking pages alone, fix and 301-redirect the rest.
- **Scott** — NYC-based service business expanding to a market **~3 hours away** (Albany area); advised to start a separate site + new Google Business Profile for the new city; also asked about "Durable" (an AI website builder marketed on SEO) — Matt hadn't used it, gave a neutral "try it, share results if it works" answer. States he's currently ranking **#2** in his niche after **2 years** in business.
- **~1,000 people** on the live Rank Week call vs. **~20–30 (up to ~50)** on a typical Insiders call — cited repeatedly as why individualized answers are only possible on Insiders calls.
- **~300 people** shared their money page link in the previous day's chat, feeding the Money Page Doctor demo.
- **Felix** (Montreal) — posted a bilingual SEO question overnight in the Insiders community; got an in-depth reply (with a screenshot) from Matt — cited as proof of async community support.
- **Tori (Newbie)** — joined partway through Rank Week, posted a question that drew **27 comments** of community help.
- **Andy Kitchener** framed himself as "software for 50 years... spammed Google, done all those things, got banned in Penguin, recovered it, sorted it" — direct lived-experience data point on penalty recovery being possible.

## Notable verbatim quotes

- "Whatever your number one competitor is doing to rank number one is what Google likes."
- "More keywords does not equal better rankings."
- "Higher density does not equal better rankings. Google increasingly interprets heavy keyword repetition as over optimization."
- "Don't edit any pages that are ranking, for the love of God."
- "If you're ranking number one, even if your SEO looks bad or something is bad... don't touch that page. You're doing what Google likes."
- On asking an LLM to find your competitors: "ChatGPT will bullshit you. It'll lie to you."
- On long-tail keywords beating giant authority sites (e.g. Mayo Clinic): "Everybody's banging on the front door, trying to get in, and we're running around the back of the store."
- "I like to eliminate the 80 [percent] of SEO that doesn't matter."
- "Waiting until you're ready means you're waiting forever. How are you going to be ready if you don't jump in? How are you going to learn to swim if you don't go in the water?"
- "What you put into the group is what you get out."
- "Like, grade seven, grade eight reading level. Like, if you can't explain it to a kid, you can't explain it."
- "Is that video appealing to you, or is it appealing to a person looking to hire you?"
- "The reason I can't do this live for you guys is because it's going to take so much processing power... it's not going to cost me thousands of dollars to run this [if it stays Insiders-only]."

## Tradeoffs & nuance

- Refreshing an already-#1 page is "in theory a good idea" but in practice pure downside — there's no ranking upside above #1, only risk of losing the spot; the only reason to touch it is if it isn't converting, and even then, change incrementally.
- Ranking for an adjacent keyword (photographer on wedding-venue terms) is framed as a net positive, not a conflict, provided the site is clear elsewhere about what's actually offered.
- SEMrush vs. Ubersuggest is explicitly budget-gated advice, not a blanket recommendation: SEMrush is "a leap" in price (~$150/mo vs ~$30–40/mo) but a correspondingly bigger leap in capability ("you get a lot of stuff... it's a lot more than Ubersuggest").
- Keeping vs. changing your brand name when expanding to a new city is framed as genuine preference — keep it (append the city) unless you already have name recognition in the new market, in which case the old name carries less benefit there.
- Exact-match domains (competitor's "trout flies" domain) can correlate with ranking but aren't required — Matt's own counter-example (outranking "Hamilton SEO" for "Hamilton SEO") shows content/backlinks can beat them.
- Foreign-language sites can still be evaluated with the same framework (keyword placement, CTA clarity, page structure) even without reading the language; running English + native-language versions can double a keyword's ranking surface and pick up incidental cross-border/traveler search traffic even with no intent to sell there.
- Multi-product sites in one niche (finished goods + materials + a course) are fine on one domain as long as the IA disambiguates the visitor's path — this doesn't automatically extend to genuinely distinct/distant markets (see Scott's NYC-vs-Albany case, where a separate site was recommended instead).
- A ballooning word count isn't always a content problem: one attendee's page hit 6,500+ words because a Google-reviews widget silently rendered 80–90 reviews into the page's text (in a scrolling frame, invisible to the eye). Suggested fix is a hypothesis to test (remove the widget and rescan, or cap displayed reviews with a "read all reviews" link to Google), not a guaranteed diagnosis.
- Cleaning up HTML bloat and implementing FAQ schema are both presented as high-effort, unproven-payoff tactics that Matt deliberately deprioritizes relative to the core mechanics (title tag, meta description, H1, keyword density, word count, page speed, trust signals) — not "wrong," just not where he spends time.
- Bilingual/international content decisions (Lorena, online sex therapist working across US/Mexico/Spain) hinge on writing to the *specific pain-point question* a prospect already searches, rather than trying to rank the broad service-category term directly — informational content earns the click; the money page itself should stay a shorter-tail term.
