# Keywords, Search Intent & The Content Engine

The engine room of the whole method. Everything here answers two questions: *what do my customers actually type into Google?* and *how do I publish the single most helpful, most uniquely-mine answer to it?* Get these two right and rankings, traffic, and clients follow. Get them wrong and no amount of technical polish saves you.

## Governing Beliefs (read first)

- **SEO is answering real customer questions with real expertise.** The founding story, retold in every cohort: Marcus Sheridan, a pool-installation owner near bankruptcy in 2008 with zero SEO knowledge, wrote down and answered the exact questions he heard on sales calls every night at his kitchen table. Result: #1 pool website in the world within 2 years, and eventually a nine-figure exit. "He was truly helpful. That is what is ranking now." The AI interview method below is that same idea, sped up with tools.
- **We don't care about SEO, we care about getting clients.** SEO is just the vehicle. "The objective is not to game the algorithm, it's to write a piece of content so unique it talks to somebody with that specific problem." If your framing is "I want to rank because I want people to pay me," that is backwards. Write to genuinely help the searcher; ranking and revenue follow.
- **~15% of Google's ~2 billion daily searches are brand new**, never searched before, and will never appear in any keyword tool (SEMrush, Ahrefs, Moz, Ubersuggest only show terms they have already detected). Zero historical volume is not proof of zero future demand. This is the entire justification for answering full-sentence questions instead of only chasing measured keywords. It cuts both ways: a niche site invisible to competitor research is also one you cannot forecast or prove ROI on before publishing.
- **Overwhelm is the #1 thing that ruins SEO**, not the tactics. People quit because they feel behind, not because the method stopped working. The whole program is engineered to fit in **~1 hour/week**. "Don't overthink anything. Don't let that take you off track and go down a rabbit hole."
- **AI is a tool, never a brain-replacement.** Google and AI do NOT penalize AI-written content. They penalize **regurgitated, generic, same-as-everyone content**. "Google and AI hate AI-written posts? They do not. They hate regurgitated information that's the same that everybody else is saying over and over." What avoids the penalty is injecting your own real expertise, experience, opinions, and stories via the interview method.

---

# PART 1 — Keyword & Question Research

## 1.1 What a keyword actually is

- Plain definition: **exactly what people type into Google.** Not random words stuffed on a page. Keywords are the *questions and problems* your customers already search for: "how much does SEO cost," "best coffee shop near me," "how do I fix a leaky faucet."
- **Short-tail** = 3 words or fewer. Broad, high volume, high competition, hard to rank. Avoid as a primary target for a smaller site (e.g. "photographer" pits you against the world).
- **Long-tail** = 4+ words, usually a full question or statement. Specific, lower volume, easier to rank, faster traffic (e.g. "elopement wedding photographer Hamilton"). A long-tail target does not have to be phrased as a question; a plain statement ("how long can I keep my LED lights on for," a "top 10 X" list) works just as well.

## 1.2 The keyword opportunity matrix

| Traffic | Competition | Verdict |
|---|---|---|
| High | High | **Avoid.** Everyone's chasing these; you'll struggle and get discouraged. |
| Low | Low | **Default starting point.** Easiest realistic wins. |
| High | Low | **Unicorns / gold.** Rare. Always prioritize when found. |
| (any) | (any) | **High-intent** long-tail: fewer searches, far higher conversion, bottom-of-funnel. |

Guiding line for competition, repeated constantly: **"Pigs get fat and hogs get slaughtered."** Never try to grab an entire market or head term at once. Take a slice, win it, then expand. "People want the whole pizza. They don't want a slice, they want to take the whole thing" is exactly the mistake.

## 1.3 The research workflow (free-first, then paid)

**Free, tool-less (AnswerThePublic):**
1. Go to **answerthepublic.com**. No account = 1 free search/day; free account = 3/day. Set region to your **target country** (usually United States), not where you live.
2. Type in the **broadest** version of what you sell ("hot sauce," "plumber," "web hosting"). Broad beats specific for seeding. If a narrow term returns nothing ("ColdFusion web hosting," "tiles"), broaden it ("web hosting," "bathroom tile") and fold the niche back into the answer body later.
3. Click **Search Engines -> Questions**. Use the plain **List view**, not the Wheel (unreadable). Ignore Volume/CPC columns at this stage.
4. **Skip page 1. Use page 2, 3, or 4.** Competitors rarely click past page 1, so later pages are less contested. This is the single most-emphasized tactic in the whole discovery step.
5. Scroll further down for a **second, hidden question set sourced from Bing** that most people miss. Bing carries ~4% of global search, and ChatGPT pulls from both Google and Bing, so Bing-only questions are still worth targeting.
6. Pick a question you can **personally answer today** (no research required), that's specific and fits your business.

**Google's own SERP (a fully equivalent substitute):** Google your core term -> scroll to **"People Also Ask"** -> click a question to surface more -> also check **"People Also Search For."** Pull 4 different questions, not near-duplicate angles.

**Paid tools (optional cross-check, never required):** SEMrush (Matt's daily driver), Ubersuggest (cheapest), Ahrefs, KeySearch. Any works. Set the tool's **location to your target country** every time (a recurring self-inflicted bug: leaving it on the wrong default).
- **Method A, single competitor:** Google your industry + location, open the #1-3 organic (never paid) results, paste a domain into Organic Research, scan its easy keywords by Volume + KD.
- **Method B, Keyword Gap / Content Gap:** enter your domain + a big content publisher's domain. The competitor does NOT need to be a direct rival; **the bigger/more authoritative the comparison site, the more opportunities surface** (Matt uses neilpatel.com). Filter to **"Untapped"** (they rank, you don't), ignore "Shared" (targeting those = cannibalization), sort by KD ascending. Live results: 47 untapped vs a small local competitor, 927 vs neilpatel.com.
- **Competitor sitemap gap (no paid tool):** grab `[competitor]/sitemap.xml` (on Yoast sites open the **post-sitemap** to isolate blog posts), paste into ChatGPT with: *"Using my competitor's sitemap, tell me content gaps that I can write about on my website that likely have an easier difficulty."* Red flags that mean pick a different competitor: single-line sitemap, no post links, or no sitemap at all (signals they're not doing well on Google). Jessa got 24 content-gap ideas this way: "a roadmap for the next six months."
- **Reddit mining:** Insiders' **Reddit Keywords tool** crawls subreddits for a seed term and returns the real questions people ask, plus pain points and content ideas. No tool? Google `site:reddit.com [keyword]` (Reddit's own search is weak, Google indexed it thoroughly). Especially powerful for **LLM/AI visibility**: brands are outranking competitors in ChatGPT/Gemini largely off Reddit mentions.

## 1.4 Thresholds: difficulty, volume, referring domains

- **Keyword Difficulty (KD):** ideal band **0-15** (tighten to under 14 for a brand-new/low-authority site); up to **25 "still possible"**; ~31 "a little more difficult than I'd like"; **90-100 = never going to rank** (e.g. "website design," no location, ~60,000 US searches, 100% KD). KD is best read as roughly the Domain Authority you'd need to rank page 1. Higher-volume keywords are "9 or 9.9 times out of 10" harder than low-volume long-tail, even when no difficulty score shows.
- **Volume:** **~10 searches/month is an acceptable target.** Don't dismiss it: "even if there's only 10 people searching that, those 10 people are looking to work with an SEO agency." Rough floors for low-authority sites (not hard rules): product pages **≥~30/mo**, collection pages **≥~50/mo**; go lower for a brand-new site. If a tool shows **N/A** difficulty, refresh/update its metrics (~1 min) rather than treating it as zero.
- **Zero/near-zero volume is NOT a disqualifier** if difficulty is near-zero AND other demand evidence exists (a subreddit already discussing it, a competitor already ranking, an active People Also Ask box). Tools under-report hyper-local and brand-new terms.
- **Referring domains, not raw backlink count**, is the metric to check on a SERP's current winners. A page ranking on page 1 with **0-2 referring domains** is genuinely winnable with no link-building. "Backlinks are expensive and time-consuming to get. If I can avoid it, I will avoid it at all costs." KD itself is calculated largely from the backlink profiles of currently-ranking pages, so a 0-volume term can still score ~60 KD if the incumbents are heavily linked.

## 1.5 Keyword phrasing & variants (match the market, don't educate it)

- **Always follow the keyword research and never guess. Never** — even against your own pride or attachment to a product name.
- When a term has multiple spellings/forms ("stand-up" vs "standup," "web design" vs "website design," "permanent makeup" vs "permanent-makeup," "paddle" vs "padel"): **check which variant the market and competitors actually use and which gets real traffic, then target that.** "Your job is not to train people. Just use the terms that people use in real life and look at what your competitors are doing because they've built a roadmap for you." Matt lost visibility for "website design" while both competitors beating him used "web design."
- **Match competitors' exact phrasing, not a close synonym**, in structural tags (title, H1, meta). Use variants only in body copy. Singular vs plural: use whichever form the research shows people search. Google treats natural variations as equivalent, so don't force an exact-match into a sentence that sounds wrong spoken aloud ("Tampa Bay Boat Rental Tampa").
- **Misspelled / "wrong" / layperson terms:** if the top-volume variant is technically misspelled, backwards, or the non-professional term, still target it and use the post to explain why it's technically wrong. Reputation-sensitive niches (law, plastic surgery) may legitimately choose correctness over matching sloppy search behavior; that's a brand values call, not an SEO rule.
- **Name products/pages what real searchers type, not invented brand language.** A beaver-fur hatmaker renamed off a trendy invented name to "beaver fur hat" (260 searches/mo Canada, 880 US). Jackie's Irish-language candles became "[Scent] Soy Candle" with the Irish name appended at the end. Lead the title with the real keyword; append the brand/invented name last, never the reverse.
- **Novel/category-defining products with no existing demand:** don't force the question workflow. Write an "old thing vs new thing" comparison post instead.
- **Cross-language:** run keyword research natively in the target language from scratch. Don't translate English content; the real search phrase is often different from a literal translation. For blog/general content most solo operators should pick one language and rely on browser auto-translate; only money/service pages need the customer's real language.

## 1.6 Secondary keywords

- Prompt: *"Please give me 10 secondary keywords that are SEO optimized"* (paired with the primary). **Cap at 5-10 per piece.** Only use the ones that fit naturally; no obligation to work every one in.
- One practitioner's personal rule: skip volume/difficulty scoring for secondaries, just check topical relevance ("secondary keywords are a dance"). Build research into **lists/themes** rather than one rigid keyword: "Using it more as a concept. You don't want to jam all of these in, but you have them to use."

## 1.7 Word count & keyword density: benchmark competitors, never a fixed number

**There is no universal ideal word count, keyword count, or density.** The only real benchmark is whatever is *currently* ranking #1-3 for that exact keyword, and it moves as the competitive set changes.

- **Word count:** Google the exact keyword, check the actual top 3 pages, and **match them or add ~100-200 words** (some cohorts phrase it as **"level plus one" / ~10% more / "0.0001% more"**). Real competitor pages for one keyword ranged from ~500 to 2,500 words in the same SERP, proving word count itself is not the driver. **Over-optimization (too long) is one of the most common live failure modes** and gets you told to *trim*, not add. Anchors seen across calls: **~400-500 words** is plenty for a zero-competition long-tail; a **~700-800-word floor** for a normal post; a rough **~2,000-word ceiling** per page. A 2,000-word page has outranked a 3,200-word page in the same niche when intent/format matched better.
  - *Note on the old curriculum:* Level-0 foundations state "~2,000 words correlates with #1-4" and "even the homepage should hit 2,000+." The live calls supersede this: it is a rough anchor only. The competitor-relative rule wins.
- **Keyword density:** no fixed %. "Use it three or four times and see what happens" as calibration, then match the actual #1 competitor's count (seen ranging from once to 27 times). **Split the phrase into components** (location + service) and count each separately across competitors. **Density red flag:** if yours sits meaningfully higher than competitors', you are almost certainly over-optimized. Matt's own page: **5.04% density (keyword used 35 times) vs competitors' 1.76% and 0.9%** correlated with a drop from #1 to #9. "More keywords does not equal better rankings. Google increasingly interprets heavy keyword repetition as over-optimization."
- **Never trust a single tool's word/density number.** Extensions disagree by hundreds of words; tools scrape hidden popups, review-widget text, mobile-duplicated text, and currency selectors. One page: 808 (tool) vs 511 (manual). A plugin was once silently injecting 2,000 words of hidden text onto every page. **Verify by copy-pasting visible text into wordcounter.net.** Tools also lump keyword variants together, inflating counts (a "35 uses" reading was ~5 literal uses plus a related variant).
- **Ignore keyword-density plugins entirely** (Yoast/Rank Math) for long-tail/question content: they are geared toward 3-4-word short-tail phrases and actively work against full-question posts. Chasing a plugin's "use the keyword N times" rule can literally CREATE the over-optimization and cross-page cannibalization problems.

## 1.8 Keyword tools quick reference

| Tool | Use | Notes |
|---|---|---|
| **AnswerThePublic** | Question mining | Free 1/day (no acct) or 3/day; not a full keyword tool |
| **Google People Also Ask** | Question mining | Fully equivalent substitute |
| **Insiders Reddit Keywords / PAA / Quora tools** | Real-question mining | Reddit tool especially strong for LLM visibility |
| **SEMrush** | Volume, KD, Keyword Gap, SERP analysis | ~$130-150/mo; trust **Keyword Difficulty**, don't over-weight "Competitive Density"; cancel free trial immediately (charges, no refund) |
| **Ubersuggest** | Cheapest research | ~$20-40/mo; volume often inflated (grouped) |
| **Ahrefs** | Research, difficulty cross-check | Lite ~$29/mo, 100 searches/mo cap; **trust Ahrefs over Ubersuggest 100% of the time** on difficulty disagreements |
| **KeySearch / Mangools** | Cheaper alternatives | KeySearch ~$20-24/mo, 200 searches/day |
| **Hey Keywords (heykeywords.com)** | Matt's own; pulls live from Google Ads | Base ~$29/mo (50 searches + 10 domain analyses); keyword/backlink/gap views |
| **Insiders Blog Idea Finder / findquestions.com** | Topic/question finder | In-platform, no email gate |
| **wordcounter.net / characterCounter.net** | Manual word/density/char verification | The real source of truth over any extension |

**Cross-tool disagreement is expected** (each vendor applies its own undisclosed adjustment on top of the same Google Ads data). Treat all numbers as directional. Google Search Console is the more accurate ground truth for actual organic traffic; the research tools are for planning. Don't use Google Trends to judge volume.

---

# PART 2 — Search Intent

Intent determines the *format* of the page and whether it should exist at all. Choosing the wrong format loses regardless of content quality.

## 2.1 Funnel mapping (TOFU / MOFU / BOFU)

- **Bottom-funnel (BOFU):** searcher already knows they need your exact service (e.g. "web design" or "personal trainer in Vancouver"). High intent, lower volume.
- **Middle/top-funnel (MOFU/TOFU):** searcher doesn't yet realize your service is the fix ("why aren't I getting business," "when was hot sauce invented"). **Most available search volume sits here**, not at the bottom. Don't stay stuck only answering BOFU questions.
- Client-discovery question to surface MOFU/TOFU topics (Kira): *"If I could wave a magic wand and give you anything, what problem would I solve?"* The literal answer ("I want consistent leads") is raw material: write about the underlying problem, not the service name.
- **The content itself walks the reader down-funnel:** answer the informational question, then a contextual internal link/CTA ("check out our hot sauces ->").

## 2.2 Match content format to what is actually ranking

**Before writing or optimizing any page, Google the exact target phrase and look at the SERP.** Is it dominated by product/collection pages, directories/listicles, service pages, or blog posts? Build the matching format. Writing the "wrong" format for that SERP will not rank regardless of quality.
- "best video production company in NY" is dominated by list/directory sites (Clutch); a single-company "we are the best" page fights the wrong intent.
- "ski t-shirt," "tennis shirts" SERPs are dominated by **collection pages**, so optimizing a *product* page for that term fights the wrong format.
- If the top results are all "platform" types (Vimeo-style, marketplaces) and you're a local service business, that keyword's intent doesn't match you; deprioritize even at 0 difficulty.

## 2.3 Money page vs blog post: the dividing test

- **The test:** if content ends with a "conclusion," is purely informational, or answers a *question*, it's a **blog post**, regardless of what page type it was built as. A **money page** (service, product, collection, location) assumes the visitor is already past education and just needs to know you offer the solution and how to book.
- Rank Week phrasing: if someone would Google the topic for *information*, write a blog post; if they'd Google it to *hire someone*, write a service page. Same topic, different content, never blended.
- **Blog posts are informational-intent by default and usually aren't meant to convert directly.** Their job is trust and topical authority. A high-ranking blog post with weak conversion is not broken; it may just need a business-relevant CTA added, not a rewrite into a sales page. Sometimes a blog post's only job is passing internal-link authority to a money page.
- **You cannot rank for a keyword without a page built around that exact keyword.** "You can't rank for a keyword if you don't have a page about that keyword." Put transactional terms ("Scorpio candle") on collection or product pages, not blog posts.

## 2.4 Homepage targeting by business model

- **Local/service businesses:** target `[service] + [city]` on the homepage ("dentist in Hamilton," "Residential Roofing in Cincinnati").
- **Ecommerce / content / national sites:** do NOT rank the homepage for a keyword. Ranking happens on collections, products, and blog posts; the homepage just orients a visitor who landed from an entry page. Make it a branded page (H1 = brand name, title tag = brand + what you sell).
- **National/virtual with no physical base:** optimize the homepage for the single largest nearby metro, then spin out location pages for smaller markets.
- **A blog post's target keyword should never be your homepage's primary keyword** (self-cannibalization). Use secondary/variant keywords in blog content.

## 2.5 "Near me" and adjacent keywords

- **Never target "near me" as a keyword** or bake it into copy. "The sign of somebody who doesn't know how to do SEO." Google already connects searcher location to your business automatically; you rank locally from other signals. If "near me" is already a top organic referrer, leave the page as-is; don't engineer it.
- **Ranking for an adjacent keyword is fine, not a conflict** (a photographer ranking on "wedding venue" searches). Capture it via a sidebar/popup/downloadable guide rather than fighting it, as long as your real service is clearly stated elsewhere.

## 2.6 The two-question business-priority filter (Kira)

Before picking any tactic, answer: (1) **"What are my priorities for the next 3-6 months?"** (revenue/leads vs authority vs brand) and (2) **"Is my business hyperlocal, or do I serve broadly?"** The combination decides which levers matter now. There is no universal rank-order across businesses.
- Plenty-of-leads-but-wrong-fit (a surgeon getting calls for procedures they don't do): stop chasing more high-traffic keywords; narrow/optimize specific service pages describing exactly what you do and don't do.
- Needs-more-leads, non-hyperlocal: deprioritize Google Business Profile; prioritize high-traffic/low-competition content + conversion-rate work.
- Brand-new/near-zero traffic: prioritize **low difficulty even at low volume** to generate visible momentum fast (a confidence play as much as a traffic play).

**Positioning/differentiation angles (Kira):**
- **Reposition away from head-term competition:** a voiceover artist stopped fighting "voiceover" against 100,000+ competitors and repositioned around a real differentiator ("48 years of business experience") aimed at the much larger pool of small businesses.
- **Competitor brand name as a secondary (never primary) keyword:** you won't outrank a competitor for their own name; work it into body copy as a comparison ("Compared to Suavecito pomade, our pomade is...").
- **Radical-honesty "problems with X" posts:** write about the real downsides of hiring/buying your own product/service type. Title: "The problems with hiring/buying [X] that no one talks about." Competitors won't write it, so you become the honest voice. Must be genuinely honest, never a disguised pitch.

---

# PART 3 — Keyword Cannibalization

**The single most-repeated rule in the entire curriculum: one keyword per page, always.** "If you have the exact same keyword on two different pages, Google looks at them and goes, I don't know which page to rank. Maybe I'm not going to rank either." Google will only ever surface one page from your domain per query, so unmanaged overlap directly costs you.

## 3.1 What is and isn't cannibalization

- **IS:** two pages/posts on your own site whose *topic* (exact keyword or its natural variant) competes. It is about the page's topic, not link destinations, so many blog posts can all link to the same money page without cannibalizing, as long as each post's own topic differs.
- **IS NOT — different locations = different keywords by definition.** "We buy junk cars, Dallas" and "...Houston" never cannibalize no matter how similar the template, provided the exact keyword differs and the local content is genuinely substantive. "If you add a location, that is a whole new keyword." (Live proof: "we buy junk cars, Dallas" at volume 210 beat both the "...Dallas, Texas" and the ChatGPT-suggested root "junk car buyer" variants.)
- **IS NOT — topical authority via many similar pages** is fine and encouraged, as long as (a) no two pages exact-match the same keyword and (b) content is meaningfully different, not re-skinned. Hot-sauce demo: 4 posts plus a money page all mentioning "hot sauce" don't cannibalize, because each *full question* is its own keyword ("what is hot sauce made of" is not "what is the healthiest hot sauce"). "If a dentist could only talk about teeth on one page because teeth is a keyword, that doesn't make sense."
- **IS NOT** — a collection/category page and a blog post on similar subject matter, provided the blog targets a distinctly different (usually longer-tail) keyword. Product-comparison pages (Botox vs Dysport vs Xeomin) are a valid consideration-stage content type, not cannibalization of the individual product pages.

## 3.2 Within-page cannibalization

Using 3+ near-duplicate phrase variants inside one page ("indigenous art fly net hat," "mosquito net hat," "indigenous art protection print fly net hat") confuses the target signal. Commit to one primary phrase per page.

## 3.3 Detection & fixes

- **Detection:** the Insiders **Cannibalized Keywords Scanner** / **keywordconflict.com** (auto-pulls sitemap, ~50-page default scan, adjustable toward 500); Hey Tony **Money Page Tool** (reports which of *your* pages actually ranks #1 for a keyword, surfacing when your homepage is stealing your service page's term); GSC (click a Query -> Pages tab to see every URL ranking for it). **False positives are common:** date-based archive slugs redirecting to the homepage, or pages that 301-redirect to the canonical, get flagged but aren't real conflicts. Cross-check flagged URLs against `sitemap.xml` and `robots.txt`; if absent from both, they're redirect artifacts. Near-synonyms ("photography" vs "photographer") show similar volume because tools group them semantically; don't worry about cannibalization between them.
- **Fix:** consolidate the two pages into one, or 301-redirect the lower-traffic page into the higher. To de-cannibalize, paste both pages' full content into Claude and ask it to compare and recommend what to change on each so they stop competing.
- **Never A/B test two pages/posts for the same keyword** — that IS cannibalization. A/B testing works for Reels or YouTube thumbnails, not blog posts chasing the same term. Test variants sequentially over time instead.
- **Never rewrite/republish a post to "refresh" it.** Edit the existing post in place in the CMS regardless of original publish date; a literal copy-paste repost is a real cannibalization risk.
- **Blog + money-page guard:** the money page owns the exact buyer-intent phrase; blog posts cover adjacent educational angles and reference the exact money-page phrase **at most once**, typically near the bottom as a link back, never repeated throughout.
- **The golden exception:** if a blog post and a service page are already both ranking for the same keyword and it's working, **leave it alone.** Don't "fix" a technically-cannibalizing setup that's delivering results.

---

# PART 4 — The Content Engine: The AI Interview Blog Workflow

This is the recurring weekly drill, taught and re-taught in nearly every session. It is the spine of the whole method.

## 4.1 Why blog posts work (the compounding case)

Blog posts are "the lifeblood of a website. It gives you authority. It shows Google that you know what you're talking about." The seven mechanisms:
1. **Traffic + trust** — easy long-tail ranks fast; visitor engagement (time on site, clicks, form fills) signals quality.
2. **Internal-linking equity** — every post is a fresh chance to pass keyword-anchored links to money pages.
3. **Unlocks harder keywords over time** — accumulated traffic/trust eventually lets you compete for terms you couldn't touch on day one.
4. **Organic backlinks** — unique content earns natural links; people link to informational content far more readily than to a sales page.
5. **The avalanche / snowball method** — keep stacking small, zero-competition, near-zero-volume question posts, all interlinked. Individually they barely move traffic; the accumulated topical authority is what eventually unlocks the harder head keywords. "The snowball's small, then we get more traffic, Google trusts us more, ChatGPT starts picking us up."
6. **Consumer trust/recognition** — answering prospects' exact questions early builds expert positioning that pays off at the purchase decision.
7. **Topical authority** — modern Google favors sites tightly focused on one field.

Case proof: a blog-only client hit **$120K/month** after ~2.5 years with SEO as the only channel. A therapist told to "write one blog post a week and answer your customers' questions" now runs a 3-month waitlist, fully booked, no ads, invisible to every keyword tool for "male therapist Hamilton" yet ranking live on Google and ChatGPT.

## 4.2 The weekly loop (step by step)

1. **Source a real customer question** (Part 1.3). Or use one you personally heard from a customer at an expo, on a client call, or in a niche Facebook group.
2. **Open a brand-new chat** in ChatGPT / Claude / Gemini / any LLM (interchangeable for this step). Paste the **interview prompt** (4.3) with your question substituted in.
3. **Answer the AI's clarifying questions one at a time**, in the same thread. **Voice mode is strongly preferred** ("I'll digress and might reveal something else I wouldn't think of if I was typing"). Tangents are fine; rambling trains the AI to sound like you. 2-3 sentences per answer is enough as long as each reflects genuine experience/opinion. Budget ~1 min/question, ~20-30 min for 10.
4. **Run the write-the-post prompt** (4.3) in the same thread so it references the interview context. Or relay the Q&A into a second AI (4.4).
5. **Copy the entire draft into a blank Google Doc / Word doc first.** Never build directly in the CMS. (Pasting through plain text also strips a hidden AI-generated tag some CMS backends store; alternatively use WordPress's paste-as-code button, or have the AI output raw HTML and paste into the code tab.)
6. **Clean-up pass, line by line** (4.5) — strip the AI tells.
7. **Add images** (4.7) and internal links (4.10).
8. **Write title tag + meta description** by asking the AI (4.3), confirming the target keyword appears in both.
9. **Publish** (4.10). Fine to publish text-first and add images later ("get something up rather than not"); caveat: if Google crawls before images exist, it picks up later-added images noticeably slower.
10. **Close the loop:** go into 3 older, already-indexed posts and add a link from each into the brand-new post.

**Never publish the first draft as-is.** Review every section: is it actually helpful, or a thin bullet list? Verify every first-person claim the AI invented ("I've helped businesses rank for...") against what's actually true for you; cut anything inaccurate. "Don't publish anything that you can't stand behind."

## 4.3 The exact prompts (verbatim, by function)

**Interview / clarifying-questions prompt (canonical):**
> "I'm writing a blog post answering this question: [paste the question]. Ask me anything you need to know the answer to in order to write a blog post that is truly helpful and unique. It should include my experience, expertise, case studies, examples, opinions, etc. Keep it limited to 10 questions. Ask me them one at a time. I'll be using voice mode to answer them. Give me time to breathe as well before going to the next question."
- **Cap the questions at 5-10.** Uncapped it defaults to ~30 ("way too much"). Different cohorts standardized on 5 or 10; 7-8 is common. Add the voice-mode instruction separately if needed: *"I'm going to answer these in voice mode. Ask me one at a time and leave room for me to breathe. Don't write the blog post. I will prompt you after."*

**Write / final-draft prompt (canonical):**
> "Write this as a clean WordPress ready blog post using my expertise, experience, opinion, stories, etc. Use H2 and H3 headings only. No horizontal rules, section dividers, tables, call out boxes or other formatting elements. Just headings, paragraphs, and bullet points where appropriate."
- "Doesn't matter if you're using WordPress or not, it's just verbiage" to make the AI strip its own formatting clutter.

**Simpler relay version (ChatGPT Q&A -> Claude):** *"Write me this blog post using this information."* / *"I just did this with ChatGPT, write me the blog post using my answers."*

**Fuller relay (Carol's):** *"Here's my chat with ChatGPT about writing a blog post. There are questions it asked me and my transcript I did in voice mode to answer. Please write me a blog post using this information plus whatever searches you need to do online to get the most accurate information."*

**Rewrite bullets -> prose:** *"Rewrite the following. I don't want it to be a bunch of bullet points, that's not helpful. Elaborate on it a bit and ensure there's at least one paragraph. It can still include bullets if useful, just not as the whole section."*
- Length control add-ons: *"This is a bit long now, shorten it to three to four paragraphs, and don't end it with 'finally.'"* / *"Same with this, but keep it under 250 words."*
- Subheading breakup: *"Let's do some H3 tags or something to break this up a bit."*

**Direct-answer rewrite (AEO):** *"The first paragraph should directly answer the question posed in the title / main keyword."*

**Key Takeaways / TL;DR:** *"Give me a TL;DR at the top of this blog post. Five points max. Call it 'Key Summary.'"* Prefer "Key Takeaways" / "Key Summary" over "TL;DR" (that term reads Reddit-native). Also: *"write me key takeaways for the end."*

**Secondary keywords:** *"Please give me 10 secondary keywords that are SEO optimized."*

**Meta description:** *"Write me a killer, compelling, click-worthy meta description for this page."* Generate ~5, pick the best.

**Title tag:** *"Write me a title tag for this page under 60 characters. The focus keyword is [X]."* (Or "five compelling title tag options, make sure it includes [keyword]," pick the best.)

**Featured image (attach 2-4 on-brand images as style refs):** *"Using the style of the images attached, create me a featured/cover image for this blog post. Here is [the topic]. You don't need any text on the image (no title, no question). [Optional mood: it should be someone who is frustrated or unsure what to do.]"* Add *"make sure not to include any of the exact images that are in these, make new ones in that style"* to avoid copying reference elements.

**Infographic:** *"Make an infographic for this page."* / *"Create me an infographic for this content."*

**Big Five ideation (Marcus Sheridan's framework, to avoid re-summarizing competitor lists):**
1. First: *"summarize this"* on each of the top-3 ranking articles, one at a time (trains the AI on what's ranking).
2. Then: *"I only want 20 blog post ideas that work for any business, not for specific industries. The keyword I'm trying to rank for is [X]. I want you to come up with topics based on Marcus Sheridan's Big Five blog posts."*
3. Then: *"Write me a blog post based on these ideas. Knowing the keyword is [X], it should be helpful, unique, and include my personal expertise, experience, case studies, etc. Use any relevant info from previous chats."*
- The five categories center on cost & pricing (how much, what affects price, is it worth it, cheap vs expensive), comparisons, "best of," problems, and reviews. Add one external link to the framework's source (Sheridan's own site).

**Knowledge-base seeding (carry context into Claude):** *"I want to make a .md file that has everything you know about me and everything another AI would need to know in order to operate the same way you do with me. Give me that whole breakdown, make it into this file."* Paste the result into Claude as standing context, or save it as a Claude Project / custom GPT. (Condense to ~25-30 pages max; ~50 pages dilutes output.)

**Mining client-call transcripts:** *"What are all the questions and answers that happened in these calls?"* Feed a client Zoom transcript in. Captures real Q&A plus natural brand voice. "A gold mine for content."

**Repurpose a transcript/podcast/video (append to the interview prompt):** *"Here's a transcript from a conversation I had. Use that information when you can and where you can to pull my expertise, experience, all that kind of stuff."* Never just hand over a raw transcript and ask for "a blog post."

**E-A-T self-audit:** after editing, paste/describe the content to Claude/ChatGPT and ask for a grade on each E-A-T category plus specific improvements.

**Reverse-engineer an AI citation (when Google AI Mode/Gemini names your business):** *"what did you analyze to recommend these companies"* and *"what search terms did you search for."*

## 4.4 Model selection & voice mode

- **The dominant split:** use **ChatGPT for the voice/interview stage** (Whisper transcription is "the best of the best"), then **paste the full Q&A into Claude for the actual writing.** "Claude is just better for like 99% of things. All my agency stuff, all the output is with Claude." Reasons Claude wins for writing: follows word-count/format instructions far more precisely, "writes like a person" vs ChatGPT's bullet-point/summary defaults, makes conservative minimal edits on rewrites vs ChatGPT's over-rewriting, and is stronger on spreadsheet/data tasks.
- **Any LLM works for the interview** (ChatGPT, Claude, Gemini, Grok, Copilot, Perplexity). **Gemini** (free tier) is notably strong on meta-description length compliance and image generation from reference photos. Grok is interchangeable.
- **ChatGPT reasoning setting:** use **"Instant"** for the fast Q&A stage, switch to **"High"** for the actual writing (deeper but slower). If ChatGPT degrades to one-line answers after ~10 posts in one thread, switch effort level or move to Claude.
- **Voice mode mechanics:** click the voice icon (not "dictate"), answer one question at a time, and **do not tap the mic again until it has fully stopped** or you risk silently losing the transcript. If screen-sharing on a live call, **stop sharing before pasting real answers** to avoid exposing client data. Personal/sensitive question? Write that answer yourself and use the AI only for the structural framework around it.
- **The Insiders AI Blog Post Writer** (app.htinsiders.com) is a Claude-powered, free alternative that runs this whole workflow: type a topic, it interviews you (~7-10 questions), then drafts following Matt's own rules. Cap: 10 generations/account (a failed run still burns a slot). Output is HTML only.
- **There is no way to fully automate this.** Even the best pipeline needs a human to answer the interview and review the draft. Skipping that is what produces generic "oatmeal" / "AI slop." "There's no way to automate writing blog posts."

## 4.5 Draft cleanup: the AI tells to strip manually

Strip every one of these before publishing (they mark content as AI-written and read as unedited):
- Horizontal rule / divider / spacer bar lines (they paste in as stray blocks).
- Random/unnecessary **bold** text and decorative arrows.
- **Emojis** — a "gratuitous amount" reads as AI; never put emojis in heading tags (pollutes what Google reads as the heading).
- Checkmark-style bullets and plain numbered-list markers (1, 2, 3) unless the post is genuinely a listicle.
- The stray leading space before a line's first word.
- Generic **"Conclusion" / "Final Thoughts"** headers (replace with a specific, content-tied closer) and the closing phrase **"and finally..."**
- Self-promotional/CTA-style subheads that don't belong in a pure answer post.
- Jargon/framework references the reader won't recognize (cut "Big Five" from the body even if you used it as an ideation lens).
- A **"Key Takeaways" H2 on every single post** can itself tip off that copy is unedited ChatGPT; use judgment.

**Em dashes:** treated by most of the community and by Kira's editing bar as an AI tell to cut. (Matt personally has said em dashes are fine to leave in during Rank Week; note this is his stated position, not a universal rule, and it is moot regardless since raw AI output should never go straight to the site.) In WordPress, run **Clear Formatting** after pasting, then manually rebuild real bulleted/numbered lists.

## 4.6 The humanizing stance and the AI-content line

- Content does **not** need to be "100% human." It needs to be **"100% helpful"** and use your own real expertise/experience. Weaving your own offer into educational content is fine; the actual violation is a **bait-and-switch** (searcher wants X, content only pitches unrelated Y).
- **Never run an AI-detector on your own writing and never "humanize" AI output.** Philosophically contradictory ("using AI to look at AI doesn't make any sense"). "We don't want to humanize our content. We want to write human content and have AI take our words and frame it coherently. Every piece should be from you, not random AI slop."
- **AI-generated content is NOT a ranking disadvantage.** Proof: Matt's own "SEO when building a website" post, ~99% AI, ~30 min total, ranked #1 on his machine and #2 on Semrush with **zero backlinks, zero referring domains**, beating Squarespace, Reddit, Shopify, Wix.
- **The unacceptable use is mass unedited publishing at unrealistic volume** — 300-500 AI posts in a day (or even a month) is unrealistic even for a site with a writing staff, and Google reads it as gaming the system. One escape-room site had ~3,000-5,000 fake-name AI pages, ~2,000 indexed, none ranking. AI-generated *images* are fine for ranking; AI-generated *video* is not (YouTube actively cracks down on it).
- The trend is toward **more authenticity, more off-the-cuff, more real** — 30-second real clips of an actual team member on site beat faceless content. "Who wrote this? That is telling who is writing the content on the internet."

## 4.7 Content structure for direct answers and AEO

- **Direct-answer-first:** restate the question as a subheading/lead-in, then answer it immediately and plainly in the first paragraph. LLMs and AI Overviews scan for direct Q->A pairs, so put the pairing at the very top and repeat the keyword/question near the top more than once. Model: *"Yes, ChatGPT can help with SEO, but it can't do it on its own"* (answering "Can ChatGPT do SEO?").
- **Key Takeaways block** at the end of every post: 4-5 bullets, worth doing regardless of length.
- **TL;DR / Summary at the very top:** only for *longer* content whose first paragraph doesn't already carry the direct answer. Write it so an AI Overview could clip it verbatim (~100 words). Matt is actively A/B testing "conclusion" vs "key takeaways" labels; results "mixed but leaning positive," more valuable as a differentiator when rivals aren't doing it.
- **AI Overview citation mechanism (Matt's ~100-query study):** ranking #1 organically does NOT reliably correlate with being cited in AI Overviews. Google's AI generates a claim/statistic first, then finds content that **supports** it. So Google the query, read what the AI Overview asserts, then **state that claim first in your content and pivot after** with your differentiated info: *"The average kitchen renovation costs $50-75,000 in [area]. However, we can do it for $25,000."* Contradicting the claim outright won't get you cited.
- **FAQs are not a free SEO win.** Stacking ~10 generic FAQs at the bottom after the CTA does nothing on its own ("is this actually helpful to a human? Probably not"). If used, **cap at 3-4 questions max**, mark as **H2 with plain question-then-answer text**, never behind an accordion/toggle/dropdown (adds parsing friction for Google and AI crawlers). An FAQ-*style* piece of content overall can genuinely help. Each standalone FAQ question can also become its own blog post.
- **Schema markup / "optimizing specifically for AI search":** largely unnecessary as a separate initiative. "If you rank high on Google and do all that work to get there, you'll likely rank in all these AIs too." Matt's own tool found non-ranking pages had *more* schema than ranking ones (one site, unvalidated). Turn on a plugin's default schema (free), skip complicated custom schema.
- **Reading level: 7th-8th grade throughout.** "If you can't explain it to a kid, you can't explain it." Rule of thumb: if an eighth grader could understand it, you're good. Paragraphs of 2-3 sentences; vary sentence length. Don't chase an all-green Yoast readability score; the algorithm "is not 100% accurate." Ignore transition-word and keyphrase-density complaints entirely.

## 4.8 Images (content side)

- **Density:** roughly one image, video, or chart every **200-300 words**, "as often as makes sense." Separate floor: **at least 4 images per post**, ideally one per H2. Every post needs at minimum a hero/featured image. (An acceptable substitute where an image doesn't fit a section: a heading-tag break.)
- **Sourcing priority:** your own real photos/screenshots (fully unique, unreplicable) > relevant AI-generated (never random filler) > stock. Exception: **AI goes to the top for graphs/graphics** ("they make really great graphics"). Never stock-photo-looking filler. Reduce AI friction by generating only the *featured* image with AI and filling in-body slots with real screenshots (SEMrush, Looker Studio reports) that show recent date ranges to prove recency.
- **Specs:** ~750px wide, 16:9 or square (be consistent sitewide). No text baked into the image. **Compress:** if over ~1MB, convert PNG -> WebP at ~70% quality (Photoshop, or Google "PNG to WebP converter," or tinyjpg.com). Real results: 537KB -> 32KB; 1.9MB -> 102KB, "looks exactly the same." Note: GoHighLevel and one of Wix/Squarespace don't accept WebP uploads.
- **File name + alt text:** rename the actual file to a plain description including the target keyword *before* uploading ("west-african-wedding-ceremony-toronto.jpg," not "1234.jpg") — Google reads the file name as a distinct signal. Set alt text to the same descriptive phrase, ~5-6 words. **Alt-text keyword rule:** use the exact keyword on roughly half (or fewer) of a page's images; never repeat the identical phrase sequentially across every image ("Newborn photographer Chicago 1/2/3/4"). Keep each page's images focused on that page's one keyword; differentiate per variant (each diamond shape gets shape-specific alt text, not all "diamond").
- **Batch images separately from writing.** The writing is fast (~15-45 min); sourcing/formatting/compressing images is what eats time (45 min to 1.5 hrs). Publish text-first, drop images in during a dedicated later block.
- **Canva copyright trap:** never export a bare unmodified stock element from Canva's library (violates their terms; Canva has demanded takedowns). Add something on top (title text, an outline) before exporting. Stick to a small, provable set of licensed sources (Pexels free + Adobe Stock paid) so licensing can be proven if challenged.
- Turn a post into an **infographic**, embed it, then cross-post to Pinterest; infographics are a content type other sites re-embed with credit, which becomes a backlink.

## 4.9 Titles and the search-intent title audit

- **Title the post as the literal question**, tightening only if the AI's version is generic ("SEO when building a website" -> "SEO when building a website, getting it right from day one"). Keyword toward the front; **≤60 characters, ideally under ~55**, or it gets cut off on Google/mobile. "The Ultimate Guide to X" framing is fine if it converts. This is "the psychology of it vs the SEO of it."
- **Never format a title/URL as "[Post Title] - [Target Keyword]"** ("What to Pick in Your Hospital Bag - Chicago Newborn Photographer"). "If it feels spammy, it probably is spammy." The keyword belongs to its own dedicated page.
- **The title-intent audit (Kira/Rank Week):** for every existing title, ask *"what would a real person actually Google to find this?"* Editorial/poetic titles that don't map to a real search query need reworking, even when the content is strong. Live: "When your strength tattoo feels like a lie" reworked toward "strength tattoo pros and cons"; "Soft is not the opposite of strong" flagged as a non-search. Titles that worked: "Are temporary tattoos safe?", "How to stay motivated on low energy days." "It's not that the titles suck, it's the intent of this piece of content."
- **Don't let a title/H1 render with a trailing "..." (truncation)** — Google literally can't read past the cutoff. Note that the on-page rendered title is often the H1, not the actual `<title>` tag; the real title tag shows on Google's results, browser tabs, and social shares. Fixing the wrong layer won't solve a truncation complaint.
- Differentiate near-duplicate topics by **angle/audience**, not just wording ("what to do when my wife has sexual avoidance" vs "...husband..."; or listicle vs explainer vs pros-and-cons).

## 4.10 Publishing mechanics + the internal-link publish loop

- **Categories: exactly one per post** (max 2 for a genuinely cross-cutting piece), never "Uncategorized." **5-10 categories total** sitewide; don't create categories until you've published ~10-20 posts. **Never use tags** ("never, ever, ever") — each tag spins up a thin near-empty archive page that bloats the site; delete existing ones.
- **URL slug = the core target keyword only** (not the long auto-generated slug, not filler words). CMS auto-lowercases and hyphenates.
- Set the SEO plugin's **focus keyphrase** to the exact target. Set **featured image + alt text**. **Disable comments sitewide** ("the only thing you'll get on blogs is spam"). Save as draft frequently; keep a backup copy outside the CMS.
- **Preview before publishing, always** — confirm internal links rendered and lists/code aren't rendering as unstyled paragraphs.
- **Publish as soon as it's ready** ("the sooner you publish, the sooner it indexes"). Don't wait for perfection given the ~3-month SEO lag: "no one's gonna see it yet anyway."
- **The internal-link publish loop** (integral to publishing a post; the fuller architecture lives in the on-page theme):
  - **Outbound:** every new post links to **3-5 other blog posts + 1 money page** (scale down to 2-3 + 1 for a brand-new post/site; 1 link is acceptable if you have nothing else yet). Use descriptive anchor text (never "click here"). Find targets with `site:yourdomain.com "keyword"` in Google.
  - **Inbound (the trick most people skip):** after publishing, run the same `site:` search to find **3 *different* older, already-indexed posts** and add a link from each pointing *into* the new post. Because Google already crawls those old pages, the new page gets discovered fast, "sometimes within an hour to two hours." "This is a trick that a lot of people don't talk about. It's honestly a huge advantage."
- **Speed indexing:** GSC gives **10 free URL-inspection "Request Indexing" submissions/day**; pages often index within ~2 hours. But manual requests are optional; Google usually finds new content on its own within ~3 weeks to a month. New-post indexing anywhere from ~2 hours to a week is normal; don't fixate on one post, keep publishing.

## 4.11 Cadence

- **1-2 posts/week, maximum.** One published post/week is "fantastic," two is "great." "I wouldn't do any more than two, it's going to get sloppy." Agency clients: **4-8 pieces every 28 days**, 2/week reserved for top-paying clients.
- **Never publish two on the same day** — space them (Monday/Thursday). Consistency of cadence beats which days.
- **New-site launch exception:** a brand-new site may batch **5-6 (or launch with 10)** at once, then drip the rest at 2/week. An already-live site should NEVER dump a dozen at once; Google reads high velocity on a steady site as spam-like instability. Historical lesson: sites that pushed to ~500 pages/week saw rankings drop as Google "retaliated."
- Higher sustained cadence (one member ran 5/week building a ~50-post hub) is acceptable only if quality holds and a defined goal justifies it. Framed as the exception, not the default. Topics realistically never run out: one seed term returns 40+ questions, another term 40 more.
- **Batch-write, paced-publish:** write/schedule in batches weeks ahead; decouple writing effort from publish cadence.
- **Don't chase perfect before publishing.** A post is never perfect, and polish doesn't guarantee ranking. Hit publish, revise later.

## 4.12 Repurposing & content-as-asset

- **Podcast/video -> blog:** never publish a raw transcript as an indexed page (a podcast is "a shotgun, you're not going to hit anything"; a blog is "laser focused"). Instead write a blog post answering an actually-searched question and reference the episode inside it as supporting authority ("Jim and I talked about this on our recent episode, here's what Jim said"). Feed the transcript to the LLM as training material: *"remember this for the future when I'm writing a blog post."* Only repurpose a video when it's tied to a real keyword/question (keyword first, blog second, video attached underneath).
- **Recurring support/onboarding question -> one-time blog post**, then send that link instead of repeating the walkthrough. Matt's team wrote "how to add and remove users from Meta Business Manager" once; it replaced a 30-60 min onboarding call for every new client and later earned organic traffic.
- **Free blog post -> longer paid guide** sold standalone (Jackie's curly-hair guide).
- **Blog -> video:** feed a post to ChatGPT for a video script, film it, post it (starts indexing, reaches more people). Fine and not duplicate content as long as you add more/different info than the post and it isn't AI-generated video.
- **Facebook-group / Reddit Q&A -> answer with a blog-post link**, not an inline reply or a bare homepage link. AI and Google now pull from local Facebook groups and Reddit ("real people, community chats").
- **Client-call mining:** run a 30-60 min recorded interview with a new client, feed the transcript into a standing reference doc the LLM pulls from for future posts in their voice. Batch multiple call transcripts into one file for hard-to-reach clients. "You literally look like a genius by asking your client the questions ChatGPT gives you."
- **Social redistribution** (post the link with ~100 words of your own framing on LinkedIn/X/Facebook/Reddit/Pinterest, never a bare link) doesn't move rankings directly but signals a legitimate active business and is an active experiment for AI-citation visibility. Never post links on Instagram/TikTok (no clickable links). Never publish the *same full content* on both your site and LinkedIn (LinkedIn has higher authority; Google can flag your copy as duplicate).

---

# PART 5 — The Two-Prompt Money-Page Rewrite Workflow

The Rank Week Day 3 workflow for rewriting an existing money page against its competitors. Distinct from the blog interview method, but same keyword/content logic.

**Prep (Day 2 audit):** for your money page + the top 3 organic competitors (Google the exact focus keyword incognito; skip ads/Reddit/Yelp/directories), run **pageaudit.com** and record into a shared sheet: word count, keyword occurrences, keyword density %, title tag, meta description, H1, H2/H3 structure, and pagespeed. Ignore the tool's overall score entirely.

**Prompt 1 (metadata rewrite):** paste your title tag, meta description, H1, H2s, and keyword density, then each competitor's column in the same row order. It returns an updated title tag, meta description, H1, and H2s. Copy the output into a separate doc. Confirm the keyword is present and front-loaded; swap in a better-testing variant if your data showed Google prefers it.

**Prompt 2 (full rewrite):** paste your entire existing page content; for each competitor, try pasting just their URL first (ChatGPT can sometimes read the live page), falling back to full content. Set the word-count target from competitor data (competitors at 2,500 and 2,300 -> target ~2,200). Answer any clarifying question it asks first.

*(The exact text of these prompts lives on heytony.ca/prompts and comes down after Rank Week; only their input/output behavior was demonstrated on calls.)*

**Rules:**
- **Never trust the AI's self-reported word/keyword count.** Live: it targeted 2,200 words and delivered ~1,700; targeted a 20-45 keyword band and delivered 13. Paste the output into **wordcounter.net** and land in the *same band* as competitors, not above or below.
- **Whatever the #1 competitor does, Google likes; mirror it, then slightly outdo it** ("level plus one"). Don't just add more (words, keyword repeats); over-optimizing past the competitor who outranks you can suppress rankings.
- **Cross-check every AI suggestion against the real SERP**, especially the *lowest-ranked* of the top 3 (if #3 ranks at 500 words, aim for ~600, not 3,000 because #1 has 3,000). "ChatGPT will bullshit you. It'll lie to you." Don't trust its guess at who your competitors are; verify by Googling the keyword.
- Refine one section at a time by pasting it back: *"can you rewrite this section to be more funny and personable"*; *"you forgot these H2 tags, write a couple paragraphs each"*; or deepen it with *"ask me five questions to write a better unique piece using my expertise"* — which folds the Day-1 interview method into the rewrite (produces stronger results than treating this output as final).
- Re-run the page-audit tool on the new draft before publishing.

**Money-page fix priority order:** (1) title tag, (2) meta description, (3) H1, keyword front-loaded in all three, then **wait 1-2 weeks** before touching on-page content further. Most of this "takes 5-10 minutes."

---

# Cross-Cutting Rules & Cautions

- **Never edit a page that is already ranking (#1-3, or even weakly on page 3).** "Don't edit any pages that are ranking, for the love of God." Even if it violates every rule (duplicate H1s, keyword stuffed 35x, thin content). You can't rank higher than #1, so touching it is pure downside. If #1 but not converting: tiny incremental edits only (one sentence, one button), never a full rewrite. Reinforce it externally instead (blog posts + internal links pointing in). Matt's own SEO page reached #1 after ~1 year on internal links alone, untouched.
- **Freshness-gaming:** Google sometimes suppresses a newly-published/edited page temporarily, then rechecks whether you panic-edit (which itself reads as a spam signal). Give a page **~1 month** after publishing before re-updating; don't knee-jerk to a dip within days.
- **Don't trust an AI's SEO opinions over the data** ("combine these two keywords," "is this a good idea"). ChatGPT tends to agree with whatever you propose and "will make shit up" about best practices. "You are the expert, you're doing the research." Validate any AI SEO claim against what's working for real accounts, human logic, and a second source. Use AI for drafting/orientation, never as the final decision-maker on keyword/architecture calls.
- **Copying a competitor's "trick" isn't automatically safe.** They may rank #1 despite keyword-stuffing/hidden text because their term has near-zero competition; replicating it risks a penalty on your site for no benefit. Correlation (they rank #1 and do X) is not causation (X is why).
- **Timelines:** SEO takes **3-6 months minimum** of consistent work; real inflection can land as late as month 12-14. Ranking within 2 weeks is "magic," not the norm. Most people quit after ~3 months without results; the long game wins. "SEO only works if you don't give up."
- **The human-vs-optimized spectrum (Kira):** every choice (title, hyphenation, grammar, density) sits on a line between fully-human voice and fully-optimized-but-robotic. There is no universal right answer; choose deliberately per business and brand values. "Learn the language before you decide to break it": execute every step exactly as taught first, deviate only once you know why.
- **Quantity-then-quality sequencing:** while working through a backlog, ship everything first; shift to per-post polish once you're on a steady rhythm.
- **Gut checks that override any plugin score:** *"Would my customers actually need this and read this? If yes, publish it."* And after drafting: *"Am I proud of this?"* Don't chase 100% on any audit tool; **80%+ is fine, 90% is fantastic**, and 100% doesn't mean better-optimized than 50%.
