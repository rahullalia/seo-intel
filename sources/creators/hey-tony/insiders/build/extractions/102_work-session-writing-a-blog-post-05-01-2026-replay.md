# 102 — Work Session: Writing A Blog Post (05.01.2026 Replay)

## Tactics & step-by-step how-to

- **Full blog-writing workflow walked live:**
  1. Go to **Answer the Public**, type in what you sell (e.g., "SEO," "real estate," "dumpster rental," "search engines"), and go to the **Questions** tab to harvest real searcher questions.
  2. Pick one question as your topic (skip ones you don't like the phrasing of, keep browsing pages until one clicks).
  3. Paste into ChatGPT: *"Ask me 10 questions you need to know the answer to in order to create a truly helpful, unique piece of content that uses my expertise, experience, case studies, etc."*
  4. Immediately follow with a pacing instruction so it doesn't draft prematurely: *"I don't want you to write the entire post until I tell you. After answered all the questions, ask me one question at a time and wait for my answer."* / *"I'll wait for your response before moving to the next question."*
  5. Answer each of the 10 questions using **ChatGPT Voice Mode** — talk through your real answer like you're explaining it to someone with zero background (Matt's own framing: "this is how I explain SEO to my mom"), so the transcription captures genuine expertise/experience/case studies instead of generic filler. Rambling/long-winded answers are fine — they add personality.
  6. Expect ~20-30 minutes to answer all 10 questions this way.
  7. Once ChatGPT turns the answers into draft sections, don't accept them — review each section and judge whether it's actually helpful or just a thin list of bullets.
  8. For weak, bullet-only sections, prompt ChatGPT per-section: *"rewrite the following. I don't want it to be a bunch of bullet points. That's not helpful. Elaborate on it a bit and ensure there's at least one paragraph."* (It can still include bullets if useful — you decide per section, e.g. keeping a short bullet list at the top as a summary is fine.)
  9. Manually delete the horizontal divider lines ChatGPT/Google Docs insert between sections before publishing — in WordPress these paste in as their own stray block.
  10. Add images/video/charts roughly every 200-300 words, more if the topic is naturally visual (data, cost breakdowns, screenshots of social proof), less if it's more conceptual — but every post needs at minimum a hero/featured image.
  11. Check the top 3 Google results for your target query: match (then slightly exceed) their word count and their keyword usage frequency.
  12. Before publishing, add internal links from inside the new post: 2 links to other existing blog posts + 1 link to a money/service page.
  13. After publishing, go back and edit 2-3 *other* existing blog posts to add a link pointing to the brand-new post — this is a separate step from #12 and helps Google discover the new page faster.
  14. Publish. That's the assigned homework for the week (write, add the internal links both directions, publish, then post the link in the Insiders community).
- **Narrow-niche fix (few/no direct questions in Answer the Public):** broaden the seed keyword to the parent category (e.g., search "Yellowstone" instead of "Yellowstone tours") to surface enough topical content, then softly connect back to your offer inside that broader piece (e.g., "if you're staying at [X RV park], you can book your tour here").
- **Bilingual/multilingual posts:** don't run a full post through ChatGPT for translation in one shot — do it section by section, or content gets mixed up/dropped. Set hreflang correctly between the language versions of a page.
- **Checking a page's real ranking:** don't just Google it yourself in a normal browser — check Google Search Console for that specific URL/query instead.
- **Submitting a sitemap in GSC:** don't try to paste one giant sitemap dump. Open the site's root `sitemap.xml`, find the sub-sitemap you actually want (e.g., a "blogs" sitemap listed inside the index), and submit that specific sub-sitemap path (e.g. `sitemap/blogs`) in Search Console.
- **Alternate/supplementary tactic (participant recalled from a Matt Reel, confirmed still valid):** pull up the top 3 ranking pages for your query, feed them to ChatGPT, and ask it to produce a "mixed"/better version of what they cover — but pair this with the 10-question personal-interview method rather than using it standalone.

## Rules / dos & don'ts (keep every threshold, number, specific)

- Image/media cadence: **roughly one image, video, or chart every 200-300 words**.
- Every post needs at least a hero/featured image, even a plain, text-heavy one.
- Word count target: **match the top 3 SERP results, then add a bit more** (example given: they run ~1,500 words → you write ~1,550-1,600).
- Keyword frequency target: same logic — if competitors use the target keyword ~100 times, use ~101 ("a crazy example, but that kind of illustrates the point" — not a literal formula to hit exactly).
- Internal linking rule per new post: **minimum 2 blog-post links + 1 money-page link**, placed inside that post.
- Homework linking rule: also go find **2-3 other existing posts** and add links from those back to the new post.
- Do not run an entire multi-language post through ChatGPT translation in one pass — do it in sections.
- Bilingual pages need correct **hreflang** tags between language versions.
- Remove ChatGPT/Docs auto-inserted horizontal divider lines before pasting into WordPress (renders as a stray block otherwise).
- **Answer the Public is not a full keyword research tool** — "it kind of is, but it's not a full thing." Use it for topic/question discovery; pair with a real keyword tool or GSC for actual volume/ranking data.
- A Google Search Console property only shows history **from when it was registered/connected**, not the site's true full history — a site live since 2022 but only connected to GSC in November will show data starting in November, not before.
- Indexing/ranking after publishing is not instant — allow **roughly 3 weeks to a month** depending on how often Google crawls the site; a "0" in GSC right after publishing is not necessarily a failure.
- **Sitemaps auto-update and get auto-recrawled** by Google on their own — you do not need to manually resubmit a sitemap every time you publish new content.
- Don't force unnatural keyword-variant stuffing in non-English markets — write how people actually speak; if a market genuinely uses several synonymous terms, it's fine to vary the word used across different posts rather than cramming every variant onto one page.
- Weaving your own offer into topical/educational content is not automatically "tricking SEO" — the actual violation is a **bait-and-switch** (someone searches for one thing, e.g. printer ink, and the content only pitches an unrelated service); a genuine, relevant tie-in is fine.

## Tools, prompts & resources (exact prompt wording if quoted; tool names; settings)

- **Answer the Public** — enter your core product/service, then open the "Questions" view to get real searcher questions as topic seeds. Explicitly *not* a full keyword research tool per Matt.
- **Google Search Console** — used across the call for: checking real click/impression performance on a specific post/query; understanding why history only goes back to the property's registration date; verifying real ranking/indexing status instead of a manual self-search; finding and submitting the correct sub-sitemap.
- **ChatGPT (including Voice Mode)** — core drafting tool. Exact prompts used, in sequence:
  1. *"Ask me 10 questions you need to know the answer to in order to create a truly helpful, unique piece of content that uses my expertise, experience, case studies, etc."*
  2. *"I don't want you to write the entire post until I tell you. After answered all the questions, ask me one question at a time and wait for my answer."* / *"I'll wait for your response before moving to the next question."*
  3. Per weak section: *"rewrite the following. I don't want it to be a bunch of bullet points. That's not helpful. Elaborate on it a bit and ensure there's at least one paragraph."*
  - Voice Mode specifically used so answers get transcribed as natural, first-person, experience-based speech rather than typed generic text.
- **Google Docs** (blank doc) — where Matt drafts the post before moving it to WordPress.
- **WordPress** — CMS destination; watch for stray divider blocks from pasted ChatGPT/Docs content.
- **Claude** — Matt says he wants to start testing it for this same workflow going forward (stated intent only, not yet demonstrated in this call).
- Internal training note: Matt mentions he just recorded an internal training video answering "how many images should you include in a piece of content" for a new internship program starting the following Monday — source of the 200-300-word image-cadence rule.

## Case studies / examples / results

- **"Can I learn SEO on my own?"** (Matt's own SEO-business blog, published the prior week): plain, heavy-text page — headings + bullet points only, no images — yet drove **almost 2,000 clicks in one week** per Search Console, with **no backlinks or other off-page work** behind it, pure content. Also lifted the whole site's clicks/impressions, not just that one page (used as evidence that individual hits "lift everything up across the site").
- **"How much does SEO cost in 2026?"** (Matt's blog, the "should have more images" example): includes an actual data chart, H2 subheadings, embedded **Reddit screenshots** as social proof/"what people are actually saying," a bulleted cost breakdown ("results, not just hype"), and a video near the end.
- **Aaron** — niche: Yellowstone/Grand Teton national park tours. Problem: Answer the Public surfaces almost no direct questions for such a narrow tour product. Resolution: broaden to the parent topic ("Yellowstone" the park itself), write broad park content, and contextually link tour offers (e.g., near an RV park).
- **Wendelly** — niche: brand photography services. Insight (from her own observation): people searching "how to [do] brand photography" are often DIYers who don't even know what "brand photography" is, not necessarily buyers. Matt's take: still valuable — answering how-to questions builds topical authority/expertise signal, and tying the offer to an adjacent value angle (e.g., "how good brand photography impacts your online presence") is legitimate as long as it's not a bait-and-switch.
- **Anja / Anya** (Belgium, Dutch-language) — runs a training-software company, currently building an AutoCAD-training site. Dutch has roughly four different words for "training," including "cursus" and "opleiding"/"operating"; her current site is optimized around one variant while a competitor ranks using another. Matt's answer: no universal right answer — test blog posts using different variants and compare via Search Console; okay to vary the word used across separate posts rather than force one term everywhere.
- **Manny** — asked about bilingual (French/English) site structure. Answer: duplicate the post per language with correct hreflang, translate properly, and if using ChatGPT for translation, do it in sections rather than the whole post at once.
- **Virginie ("V"), site motivink.com** — GSC sitemap paste stopped returning full data (used to copy/paste a long string, now nothing). Root cause: was pasting the wrong sitemap level. Fix: navigate the root sitemap.xml to find the sub-sitemap listing (e.g., "blogs"), and submit that specific sub-sitemap path in GSC instead.
- **Carl** — asked for a min/max word-count target; answered with the "match top 3 competitors, then add a bit more" rule.
- **Home Hardware anecdote** (Matt's own experience, Canada) — staff diagnose the actual underlying problem (a running toilet) before selling a part, sometimes telling him he doesn't need to buy anything at all (adjust the chain, use needle-nose pliers) — used as the model for how genuinely helpful, non-salesy content builds return trust and authority.

## Notable verbatim quotes

- "The general rule is like every two to 300 words, there should be some kind of image or video or something to break it up."
- "As often as you can. As often as it makes sense." — on image frequency.
- "A big part of SEO is like... it's almost like a volume game, like a quality and a volume game. Not everything is going to hit, but when things do start hitting, that's going to lift everything up across the site."
- "At the end of the day, we are here to help real people solve their problem."
- "It's not really tricking SEO" — on weaving your own offer into educational content, contrasted with: "it's almost like a bait and switch... people are looking for printer ink, but then you're just talking about your other service."
- "We want to give Google like a ton of information so that they know what our website is about."
- "Talk about the park until you're blue in the face."
- "Look at the top three results on Google and see what they're doing. We're not trying to outshine everybody. We're trying to match what they're doing and like, just do a little bit more."
- "If they're using the keyword 100 times, you need to use 101 times. That's a crazy example, but that kind of illustrates the point."
- "[The hardware store is] helping you solve a problem without expecting you to buy from them. And that makes you want to go back to that hardware store because they're helping you."
- "We need to test and basically come up to our own conclusions as to what works and what doesn't work."
- "Be patient, keep moving forward, keep writing blog posts, keep doing the internal linking, all that kind of stuff, and eventually you will see results."
- "People are using ChatGPT as an additive, not as a replacement to Google."
- On the internal-link homework: "That's gonna help Google find it a lot quicker."

## Tradeoffs & nuance

- ChatGPT's default answers to the 10-question interview tend to come back as thin bullet fragments ("that's not really helpful... that's not a section, that's not a lot of content") requiring a manual rewrite pass — but Matt also kept some bullet sections as-is when they worked well as a summary block, so it's a per-section judgment call, not a blanket "always expand" rule.
- Broadening topic scope beyond your exact offer (Aaron's tours-vs-whole-park debate) trades some ICP precision for much greater available search demand and topical authority; Matt's position is that it's worth it since the broader-topic audience (e.g., people staying near the park) is still plausible business.
- Multi-language keyword-variant choice has no universal right answer — it depends on language, business, and industry, and must be tested per market rather than solved theoretically.
- Rewording a question slightly (adding "SEO" as a parenthetical, adding "in simple words," etc.) may change ranking outcomes — Matt frames this explicitly as an open, unresolved experiment rather than a known result.
- The "steal the top 3 ranking pages via ChatGPT" shortcut is valid, but Matt frames it as a supplement to the personal-interview method, not a replacement — pure competitor-synthesis risks losing the first-person, experience-based differentiation that (per the "Can I learn SEO on my own" case) is what actually drove results.
- A member asked whether checking rankings needs a VPN to avoid personalized search results; Matt didn't confirm or deny the VPN approach — he redirected to using Search Console plus patience (3 weeks-1 month indexing lag) as the reliable method instead.
- Sitemap submission strategy (individual sub-sitemaps vs. the master sitemap) is something Matt says he's still testing on his own site ("trying different things, seeing what works better and what doesn't") — no single confirmed best practice was asserted, just an empirical, ongoing test.
