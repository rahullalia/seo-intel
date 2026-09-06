# Work Session — Writing a Blog Post (12.22.2025) (Call 108)

Source: HeyTony Insiders Call Replay (hash: RD6dxgkyqQ) | 86m 49s | ~12,733 words

## Tactics & step-by-step how-to

- **Keyword-gap method to find a blog topic (core drill of this session):**
  1. Open your keyword tool's competitor-comparison feature — Semrush "Keyword Gap," Ubersuggest "Competitor Analysis → Add Competitor," or Ahrefs' equivalent.
  2. Enter your own site + your biggest competitor's site. The competitor does **not** need to be local to you — pick the single biggest player in your niche/industry overall (Matt used neilpatel.com against his own SEO-agency site, reasoning any marketer can use a big content publisher like Neil Patel as the comparison even if they aren't a direct competitor).
  3. Click through to "Keywords Gap" → **View All** → filter to **Untapped** (keywords the competitor ranks for that you don't).
  4. Sort/filter by SEO/keyword difficulty, ascending. Start with **0–15** ("very easy"); if nothing usable shows up, widen to **0–30**.
  5. Scroll the list and pick a keyword that "makes sense" to write about — don't overthink it, don't guess at keywords manually ("I don't like using my brain when I don't have to or guessing at keywords").
  6. Click into a candidate keyword to see keyword **variations** — useful if the base term is too generic/head-term to build a sentence or title around (e.g., "website design" alone doesn't work, but "best free blogging platform" style variations do).
- **Turning the keyword into a post using ChatGPT:**
  1. Open the top 3 ranking articles/pages for your target keyword.
  2. Paste each one into ChatGPT and ask it to **"summarize this"** — one at a time, for all 3 (Matt frames this as "training ChatGPT" on what's already ranking).
  3. Don't just ask it to rehash/merge those summaries into another giant list (that's all the top-ranking pages already are). Instead pivot: ask ChatGPT to generate ideas through a **named framework** you bring (Matt used Marcus Sheridan's "Big Five").
  4. Prompt used (close to verbatim): *"I only want 20 blog post ideas that work for any business, not for specific industries. The keyword I'm trying to rank for is blog post ideas. I want you to come up with topics based on Marcus Sheridan's big five blog posts."*
  5. Feed the resulting idea list back in with: *"Write me a blog post based on these blog post ideas. Knowing that the keyword is [X], it should be helpful, unique, and include my personal expertise, experience, case studies, etc. Use any relevant info from previous chats with you to do that."*
  6. Manually edit the draft:
     - Remove references to jargon/frameworks your reader won't recognize (cut "Big Five" from the title/body since the audience doesn't know that term).
     - Unbold random AI-inserted bold text (a detectable "AI tell").
     - Remove emojis.
     - Verify every experience/results claim the AI wrote in first person ("I have actually done this," "I've helped businesses rank for...") against what's actually true for you — cut anything that isn't accurate.
     - Pull "why this matters" reasoning out of its own sub-heading and weave it into a paragraph instead — avoids "a list inside a list," and naturally increases word count without padding.
     - Add one **external link** to a credible outside source backing a named framework/claim (linked to Marcus Sheridan's site for "Big Five," explicitly not to compete for his branded term — just credibility/citation).
     - Replace a generic "Conclusion"/"Final Thoughts" closing heading with a specific one tied to the content (used "Why these blog post ideas actually work").
  7. Internal linking: prompt ChatGPT with *"Using my site map, give me three internal linking ideas from this blog post."* Then for each suggested link, ask for placement/anchor text: *"Anchor text, where to place it — right after you mention [X]... give me a sentence where I can add this."* Manually swap in descriptive anchor text (e.g., anchor text "competitive keywords" pointing to the keyword-research post) rather than generic phrasing.
  8. Ask ChatGPT to smooth the ending: *"Make this sound better and natural as a finisher for the blog post."*
  9. Publish in WordPress: Posts → Add New → paste title → paste body → **Clear Formatting** (strips garbage inline font-weight spans carried over from pasting) → manually rebuild real bulleted/numbered lists → add a featured image (either get ChatGPT to generate one or reuse an existing image already on your site, since a site with a large post backlog likely already has something usable).
- **Small-steps cadence to avoid overwhelm/procrastination** (stated twice in slightly different cuts — treat as one system):
  - Step 1 (~10 min): find a question/keyword — via the keyword-gap method above, Answer the Public, or an actual question you've heard from a customer.
  - Step 2 (~20–30 min): get ChatGPT to answer/interview and produce a first draft.
  - Step 3: review/edit the draft.
  - Step 4: upload to the site, find/add an image, publish.
  - Step 5: add internal links.
  - Matt's framing: "If you feel overwhelmed, that's probably why" — the fix is smaller daily chunks, not one big Thursday session.
- **When your product/niche has no real search demand under its exact name** (Grace's sports-memorabilia hand-casting business): don't keep targeting the nonexistent literal term. Instead prompt ChatGPT/an AI for related real-world questions using a description of the business (Matt referred to this in-call as "Matt Diamante's answer the public strategy") to surface adjacent, actually-searched terms in the same gift/occasion category.
- **Consolidating a fragmented multi-site business onto one site** (Marla's vacation-rentals example): rather than splitting topically-related content (activities, golf-cart rentals, charters) across several separate sister sites that link back and forth to each other, put it all on the one primary site the topic most belongs to.
- **Avoiding keyword cannibalization within a single-subject blog** (Lou's vintage-moped blog): keep writing about your most popular/best-selling item, but deliberately branch into other items/models too for variety, even at lower search volume; differentiate same-model posts by angle (best features vs. worst features vs. pros/cons) rather than repeating the same angle+keyword.
- **Resolving cross-tool keyword-difficulty disagreement**: refresh the metrics in whichever tool shows the outlier number first; if the disagreement persists, default to trusting Ahrefs over Ubersuggest.
- **Finding who to reverse-engineer content from when direct competitors don't blog**: don't use a same-category competitor as your comparison site if they also don't publish content (you'll get near-zero useful keyword-gap data). Instead find any publisher/creator in the broader category who does blog, even if not a literal competitor, and out-write them.

## Rules / dos & don'ts (keep every threshold, number, specific)

- You need an actual keyword research tool — Google Search Console alone isn't enough (GSC shows what you already rank for, not new opportunities).
- Ubersuggest = cheapest option. Pricing seen live: ~**$29/month**, or a "lifetime" one-time deal at **$290 (individual)** / **$490** (a higher multi-site tier). Matt's take on lifetime deals: vendors profit MORE from lifetime buyers than monthly subscribers because most users churn out of SEO after 5–6 months — lifetime captures the money up front regardless.
- Ubersuggest free/base competitor tracking is capped at **5 competitors**; more requires a plan upgrade.
- Ubersuggest base features referenced: analyze 50 keywords at a time, ~1,000–10,000 scans/domain, 10 AI prompts — Matt: "I don't really give a shit about that," he only wants the competitor keyword-gap view.
- Semrush = Matt's daily-driver tool, roughly **$100–150/month**; he calls it more user-friendly with better-labeled data than Ubersuggest.
- Target keyword difficulty **0–15** for "very easy" first pass; widen to **0–30** if nothing usable turns up.
- Ignore Domain Authority / Authority Score when deciding what difficulty to chase — Matt calls it "a made up metric," inconsistent across tools (Ahrefs/Ubersuggest/Semrush each compute it differently). His own site's Authority Score is ~32–35, and he still only targets easy (0–15) keywords rather than "leveling up."
- You do **not** need backlinks to rank — they accrue naturally over time from good content; don't chase them as a prerequisite for going after a keyword.
- Don't target a keyword that already has an existing page on your site (e.g. your homepage's keyword) — this exercise is specifically about NEW blog-post opportunities, not re-optimizing an existing page.
- A blog post and a regular page rank identically to Google on the back end ("it's just content") — no inherent speed/favorability difference between the two content types. In practice, service/product pages tend to target moderately harder keywords; blog posts specifically go after very easy, question-answering keywords.
- Competitor picked for the keyword-gap comparison should be the single biggest player in the niche — geography doesn't matter. Example result: only 47 untapped keywords vs. a small local competitor (Socially Infused), but **927 untapped keywords** vs. neilpatel.com.
- Don't pick a same-service/same-model direct competitor for the keyword-gap comparison if they don't blog — you'll get almost no usable data (illustrated by the near-zero gap against a small local competitor).
- Don't try to out-rank branded/paid-driven competitors (e.g. major beauty brands) on their own branded terms if their traffic comes from paid ads, not content — you can't out-content a paid strategy on their exact keyword.
- Internal links per normal (non-guest) post: **3**, generated via the site-map ChatGPT prompt in this session.
- Don't publish an AI-written first-person claim ("I've helped businesses..." / "I have actually done this") unless it's true for you — verify before publishing.
- Strip AI "tells" before publishing: random/unnecessary bold text, unneeded emojis, references to named frameworks/jargon the reader won't recognize without context.
- Don't end a post with a generic "Conclusion" or "Final Thoughts" heading — use a specific, content-tied closing header instead.
- Don't publish a post that's just a giant list matching what competitors already have — weave in narrative/expertise context so it's differentiated for readers and gives AI/LLM answer engines more substantive material to pull from (a pure list gives them nothing extra).
- When two keyword tools disagree sharply on difficulty (example given: "dog anxiety at night" — Ubersuggest difficulty **44** vs. Ahrefs difficulty **1**): refresh metrics first; if it's still divergent, trust **Ahrefs over Ubersuggest 100% of the time**.
- If a product/niche term has no real search volume under its literal name, stop chasing that exact term — go after adjacent terms with actual demand instead.
- Consolidate genuinely related sub-topics of one business onto a single site rather than fragmenting across multiple sister sites with cross-linking — the multi-hop navigation "loses people."
- Vary the topic/angle across posts about the same underlying product to avoid cannibalizing your own keywords; it's fine to write about a lower-volume/harder-to-rank variant for the sake of topical variety.
- Don't try to do an entire post in one sitting if that's what's causing you to fall off — break it into small daily steps instead.
- Not every community call is mandatory — skip ones that don't match your current phase (example: skip the "website design for SEO" call if you're not yet at that stage; you can attend it later when relevant).

## Tools, prompts & resources

- **Ubersuggest** — cheapest keyword tool. Menu path used: Competitive Research → Content ideas/Keyword ideas → Competitor Analysis → Add Competitor → Keywords Gap → View All → Untapped filter, sorted by the SEO-difficulty column. Export-to-CSV option available if the UI is glitchy.
- **Semrush** — Matt's primary tool. Feature used: **Keyword Gap** (enter your domain + competitor domain) → filter keyword difficulty (0–15, widen to 0–30) → Untapped → sort ascending by difficulty. Also used: **Domain Overview → Authority Score** breakdown (shows natural link profile / link power / organic traffic as the score's components).
- **Ahrefs** — alternative tool with its own "keyword gap" feature; Matt previously had an account, canceled due to cost. Trusted **more** than Ubersuggest specifically for difficulty-number accuracy when the two disagree.
- **dib.com** — a keyword tool one attendee (Bob) uses; Matt is unfamiliar with it and couldn't troubleshoot why it was only surfacing ~12 obscure keyword suggestions for Bob.
- **Google Search Console** — good for seeing what you already rank for and how your site performs; explicitly NOT a substitute for a keyword-gap/opportunity tool.
- **ChatGPT** — used for: (1) summarizing each of the top 3 ranking competitor articles for the target keyword; (2) generating a content-idea list through a named framework; (3) writing the full post from that idea list plus personal expertise; (4) generating 3 internal-linking ideas "using my site map"; (5) generating placement sentences/anchor text for each link; (6) for novel/unbranded products, generating related real search questions from a description of the business, standing in for Answer the Public. Key prompt fragments (near-verbatim from the call):
  - *"I only want 20 blog post ideas that work for any business, not for specific industries. The keyword I'm trying to rank for is blog post ideas. I want you to come up with topics based on Marcus Sheridan's big five blog posts."*
  - *"Write me a blog post based on these blog post ideas. Knowing that the keyword is blog post ideas, it should be helpful, unique, and include my personal expertise, experience, case studies, etc. Use any relevant info from previous chats with you to do that."*
  - *"Using my site map, give me three internal linking ideas from this blog post."*
  - *"Anchor text, where to place it — right after you mention [X]... give me a sentence where I can add this."*
  - *"Make this sound better and natural as a finisher for the blog post."*
  - For unbranded/novel products: "give me questions related to my business" + a description of the business.
  - Matt's meta-tip: the more you use ChatGPT over time, the more it "knows you" from prior chats and can pull in your expertise/case studies automatically. If you're new to it (fewer than ~6–8 posts of history), instead ask ChatGPT to interview you with 5–10 questions first (as done in Rank Week) so it learns your voice/expertise before drafting. You can also upload a book, white paper, or past blog posts as source material for case studies/experience.
- **Marcus Sheridan's "Big Five" framework** — from his book *Endless Customers*. Used as the ideation lens for the ChatGPT prompt; Matt links out to Sheridan's site as a supporting external citation (not competing for the term). Only one of the five categories was actually elaborated in this call's output — **cost & pricing** — with sub-angles: how much does this cost, what factors affect price, is the product/service worth the cost, cheap-vs-expensive breakdown of what you actually get. (The other four category names weren't stated on this call.)
- **WordPress editor** — publish flow: Posts → Add New → default editor → paste content → Clear Formatting (strips inherited font-weight/inline styles from pasting) → manually rebuild real bulleted/numbered lists → add featured image.
- **Hey Tony Insiders community page** — where Matt posts a weekly "what are you working on this week" accountability thread; also the place to ask general/off-topic questions instead of derailing the live call.
- **Insiders homepage → Call Replays** — houses past session recordings.
- Upcoming session schedule mentioned: **Dec 23** = Kira (content writing/keyword research training), **Dec 24** = Leanne (website design for SEO), **Dec 26** = Matt ("Why doesn't it rank?"). No session Dec 25.

## Case studies / examples / results

- **Matt's own site (Hey Tony)** — Authority Score **32** (Semrush), described as "very good." Neil Patel keyword-gap comparison: **47** untapped keywords vs. a small local competitor (Socially Infused) but **927** untapped keywords vs. neilpatel.com.
- **"Blog post ideas"** — the keyword Matt picked live to write the demo post. Found via Semrush Keyword Gap: ~**50 searches/month**, difficulty **12** (worldwide); difficulty **16** for the US market specifically. When checked in Ubersuggest afterward, the term didn't surface in its results at all — used as the example of Ubersuggest missing keywords Semrush found easily.
- **"Best blogging platform"** — found via Ubersuggest at difficulty **30**; cross-checked in Semrush (after refreshing metrics) at difficulty **27**, which Matt called "pretty accurate" — but still passed over as too difficult in favor of "blog post ideas."
- **Joyce** (Korean skincare / Riemann distributor) — tried to rank for "Korean skincare" and "K-beauty" against major beauty brands and got nowhere because those brands win via paid traffic, not content. Pivoted to writing **6 blog posts** targeting the specific brand "Riemann" and adjacent long-tail terms: "Why is K-beauty so popular," "Skin care and your makeup," "How to transform your skin in 28 days," "What is the 7-step Korean skincare routine," "The 4 to 4 rule in skin care," "How much does Korean skincare cost." Problem: her comparison set (other Riemann distributors) also don't blog, so keyword-gap data against them is useless. Matt's advice: abandon "rank for the distributor/branded term" entirely; find bloggers/publishers in the broader skincare space to out-write instead. Separately, from doing "nothing" else on the site she was already getting ~25 page views from a simple site, with traffic spiking starting **December 7th** during a workshop; gets direct orders through the site while not being active on social media. A fellow member (20 years in skincare) volunteered content angles: "glass skin," "hydrated skin," "poreless skin," reframing to "get the glow in 5 products instead of 12" vs. the well-known 12-step Korean routine.
- **Dr. Karen** (fertility coaching) — found competitor keyword "chance of getting pregnant quiz," difficulty **27** vs. the rest at **67+**. Using it requires actually building a quiz; she already has a lead-magnet quiz but hadn't labeled/optimized it around that exact phrase.
- **Katie** — found a keyword fastest among the group ("how to stop dogs from [barking/playing]" — garbled in transcript).
- **Manny** (website design niche) — hit "website design" as an easy keyword-gap result but couldn't build a natural post/title around a bare two-word head term; guided to click into keyword variations for a usable long-tail phrasing, or skip it if none exists.
- **Marla** (East [Isla] Vacation Rentals — Isla Mujeres-type business) — wanted to rank "renting golf carts on the island" but had that content split across multiple separate sister sites (vacation rentals, things-to-do/activities, charters). Matt's call: consolidate all of it onto the one vacation-rentals site instead of cross-linking fragmented micro-sites — the multi-hop linking "loses people." Marla also wrote and finished a full blog post live during the call, posted as proof in the community thread.
- **Lou** (vintage moped blog) — writes deep-dive posts about specific bike builds/models but was over-concentrated on one popular model. Advice: keep the popular model's easy keywords, but deliberately branch into other models too for topical variety (even lower-volume/harder terms), and avoid cannibalizing within the same model's posts by varying the angle (best features / worst features / pros and cons).
- **Grace** ("Indigenous Soul Rising") — runs a sports-memorabilia hand-casting business (casts athletes' hands around game-used balls, e.g. a home-run ball); the literal term "sports hand casting" has no real search demand and is more associated with medical equipment. Had been targeting "baseball trophies" / "baseball award ideas" via Semrush. Matt + crowdsourced alternative keyword ideas (from Nick and Matt): "hand casting kits," "hand casting molds," "athlete gifts," "gifts for athletes" (not "sports fans"), "unique gifts for athletes," "birthday gifts," "home run gift." Recommended running a ChatGPT "interview" prompt off a description of the business in place of Answer the Public, since no direct keyword exists.
- **Denroy** (Hey Tony's technical SEO / local SEO / Google Ads lead) — last week's live call jumped from his usual **5–10 attendees** to **over 30**, which "blew him away."

## Notable verbatim quotes

- "I don't want to have to build backlinks, right. I don't want to have to do all this other shit. I want to get those easy wins that other people are just kind of ignoring because the traffic's not really there."
- "Don't even worry about your domain authority. [That's] a made up metric."
- "A blog post versus a page — it looks the exact same to Google... on the back end, whatever, it's just content."
- "The way around that and the way to outrank them is by answering these questions. Right. We're taking the backdoor approach."
- "I'm not like too, too stoked about this as it is, but I'm going to copy this anyways." — on a mediocre first ChatGPT draft, before heavy editing.
- "One big tell for if this was written by AI or not is like see how there's random bolded [text]... I'm just going to unbold that because that doesn't need to be bolded."
- "If it's not accurate, obviously don't write that."
- "The more that we use ChatGPT, the more it gets to know us."
- "Just make small progress instead of being like, I'm going to do this all on Thursday... If you feel overwhelmed, that's probably why."
- "I'm not going to rank for 'oh my God, that's so cool.'" — Matt, on Grace's un-searchable novelty product.
- "You don't need to join all these calls, right? Some of them are a little bit more specific... if you are not in that phase, you do not need to join that meeting."

## Tradeoffs & nuance

- Work-life balance vs. competitive drive: Matt flags his own conflict directly — knowing he "should" take holiday time off but choosing to push through and "overtake people" while competitors are off, citing the same pattern every August.
- Domain/Authority Score is directionally real (a higher score can theoretically support harder keywords) but Matt deliberately ignores that allowance and still only targets easy keywords regardless of his own site's authority level — a stated personal strategy choice, not a hard technical rule.
- Ubersuggest is "fine for keyword research" at a basic level but degrades for deeper digging — the same keyword-gap search that worked cleanly in Semrush failed to surface an obvious term ("blog post ideas") in Ubersuggest. Framed as the budget floor, not the ideal tool.
- Chasing your own branded/product term vs. answering adjacent informational questions: tempting to want to "own" your brand term in search (Joyce's instinct to out-rank other Riemann distributors), but Matt argues this is often the wrong fight when the top results are paid-traffic-driven rather than content-driven — better to abandon that specific ranking goal and build authority through adjacent helpful content instead.
- Single-site consolidation vs. multi-site sprawl: splitting content across topic-specific micro-sites for one underlying business seems organizationally clean but hurts users/rankings via excessive cross-site navigation; consolidating loses some administrative separation but wins on user experience and likely SEO.
- Keyword variety vs. keyword depth on one popular product: doubling down on the single highest-demand item (moped model) is efficient for traffic-per-post but risks monotony and cannibalization; Matt endorses deliberately sacrificing some volume to diversify topics.
- AI-assisted drafting speed vs. authenticity risk: ChatGPT dramatically accelerates ideation, drafting, and internal linking, but the raw output has detectable "tells" (random bolding, ungrounded first-person "experience" claims, generic conclusions) that must be manually stripped, and any experience/case-study claim it invents must be checked against what actually happened before publishing.
- List-format content matches user/competitor expectations (top-ranking pages are literally giant lists), so Matt still keeps some list structure rather than rejecting it outright — but tempers it with narrative/expertise context so it's differentiated for both readers and AI answer engines, which is a blend, not an avoidance of lists.
- Tool-reported keyword-difficulty numbers aren't to be taken at face value across tools; a sharp disagreement (Ubersuggest 44 vs. Ahrefs 1) requires a manual trust-call (refresh metrics, then default to Ahrefs) rather than averaging or picking whichever number is more convenient.
- Session-pacing feedback loop: Matt acknowledges he "lost" several attendees by covering too much new material at once in this session and commits to simplifying next week (pre-assigned topic/keyword, more guided steps) — an explicit admission that this session's density was a tradeoff that didn't fully land for everyone.
