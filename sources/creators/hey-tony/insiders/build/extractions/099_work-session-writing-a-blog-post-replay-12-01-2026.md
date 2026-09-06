# 099 — Work Session Replay: Writing A Blog Post (12.01.2026)

## Tactics & step-by-step how-to

- **Competitor sitemap → content-gap exercise (core of the call):**
  1. Pick a competitor (same niche/city as you).
  2. Go to `[competitor-domain]/sitemap.xml`.
  3. If they run Yoast, open the **post sitemap** specifically (not the index) — isolates just their blog posts.
  4. Copy the entire sitemap page's contents.
  5. In ChatGPT: paste "Here's my sitemap first" + your own sitemap, then paste the competitor's sitemap, then ask for content ideas with an easier keyword difficulty (exact prompt below).
  6. Alternative one-shot version: paste only the competitor's sitemap and ask directly for content gaps.
  7. Scan the returned list and pick a topic/question you actually want to answer — skip generic "best X in [city]" ideas (see Rules).
  8. Optional gut-check: run the topic through SEMrush or Ubersuggest to confirm it's low-competition/low-volume before committing.
- **Blog-drafting workflow once a topic is picked:**
  1. Paste the chosen question/title into a doc or straight into ChatGPT.
  2. Run the "ask me questions first" interview prompt (exact wording below) so ChatGPT interviews you before drafting anything.
  3. Answer via ChatGPT voice mode, one question at a time, pacing it so it waits for you to finish talking (not talk over you).
  4. Let ChatGPT produce the full draft from your answers.
  5. Manually delete formatting cruft (horizontal divider bars) ChatGPT inserts.
  6. Re-prompt for a more comprehensive, less bullet-heavy rewrite.
  7. Re-prompt again with a hard word-count ceiling (Matt used 250 words) to tighten it.
  8. Where a paragraph is really covering several distinct ideas, prompt ChatGPT to break it into H3-tagged subsections.
  9. Read the entire draft yourself before publishing — never ship the first pass.
  10. Do internal linking, add images, add meta description, categorize, publish.
- **Internal-linking method:** paste your own sitemap plus the finished post text into ChatGPT and ask for 3 internal linking opportunities; find the suggested phrase inside your draft and hyperlink it to the matching existing page. Works even off a messy/unstructured sitemap dump ("it's dirty, it's sloppy... but so it's like, okay, how to do keyword research... I'll link the word keyword research to that page").
- **Post-publish backlink step:** separately go back and add a link **into** the new post from 3 other already-existing blog posts (linking is bidirectional across the site, not just outbound from the new post).
- **External linking:** pick one authoritative external resource tied to a concept in the post (example used live: linking the word "crawl" to Google's own "Overview of crawling" page) so the post isn't "just making all this stuff up."
- **Squarespace sitemap workaround:** if your own sitemap is bloated with thousands of per-image URLs (a lightbox feature auto-generates a URL per image), ignore your own sitemap for this exercise and use only the competitor's sitemap as ChatGPT's input.
- **If a competitor's sitemap won't load into ChatGPT (too long):** pick a different competitor, manually browse their blog and eyeball topics yourself, or convert the sitemap to a PDF and upload the PDF instead.
- **Community accountability step:** after publishing, paste your blog link into the group's work-session thread; review at least one other member's post and give feedback on heading tags, internal/external links, and formatting.
- **Getting a keyword-cost/expectations idea onto the site even if you won't rank for it personally:** ChatGPT suggested "How much does SEO cost in 2026?" as a topic; Matt already has a similar post and says it's still worth having on a site for client-facing/informational reasons even without expecting to outrank others for it.

## Rules / dos & don'ts

- Don't write "best SEO agency / best dentist / best plumber in [city]" style list posts anymore — AI now tends to just surface whichever single business already has the most mentions/citations rather than reward a ranked list; this used to be a viable strategy and no longer is (see Tradeoffs).
- Don't take ChatGPT's first draft and publish it as-is — always iterate on it.
- Keep posts short: Matt enforced a **250-word** ceiling on this draft via prompt.
- Don't over-use bullet points — keep them only where truly helpful for understanding; prefer prose elsewhere.
- Every new post needs internal links to **3 other pages** on the site, and **one of those 3 must be a money page** (a product or service page).
- Every new post should also get a link pointed **at** it from **3 existing blog posts** once it's published.
- Use descriptive (ideally fully descriptive) anchor text for internal links, not generic phrasing.
- Add **at least one external link** per post, to a credible/authoritative source.
- Add a meta description to every post.
- Put every post into **1-2 categories**.
- **Do not use tags** on your website.
- Add images: Unsplash, AI-generated (ChatGPT or Gemini), or turn the post's content into an infographic.
- If posting **2x/week**, never publish both on the same day — space them out (e.g., Monday/Thursday or Tuesday/Friday); consistency of cadence matters, not which specific days.
- Client pre-publish approval is the default; ask the client around **month 3-4** of the relationship whether they'll allow auto-publish going forward — some say yes, some no.
- A competitor sitemap that's a single line with no post links, or a competitor with no sitemap at all, signals they're "probably not doing well on Google" — pick a different competitor to analyze.
- You don't technically need an XML sitemap to rank, but having one "helps a lot."

## Tools, prompts & resources

- **Tools named:** ChatGPT (primary tool used live, including voice mode); Claude (Matt announced he's about to start testing it for blog writing next, after hearing claims it produces much better content — "next week on this call, if you see me using Claude, you can use that"); Gemini (alternate LLM, also usable for image generation); SEMrush and Ubersuggest (keyword research/difficulty checks — the two tools Matt expects everyone on the call to have access to); Ahrefs (referenced in the Reddit case study as "hrs," for domain authority/traffic estimates); Unsplash (stock images); Yoast (WordPress SEO plugin — determines the "post sitemap" structure); Squarespace (platform behind the image-bloated sitemap issue); Reddit (source of the case-study thread); TikTok (where Matt's 1,400-click claim was originally posted); Audible / Spotify (Matt's own audiobook, tangential — Spotify version has no chapter titles, just sequential numbered tracks).
- **Exact prompt — content gaps from competitor sitemap:** "Tell me some content that I can write about on my website that likely have an easier keyword difficulty" (used after pasting "Here's my sitemap first" + your sitemap, then the competitor's sitemap).
- **Exact prompt — alternate single-shot version:** "Using my competitor['s] sitemap, tell me content gaps that I can write about on my website that likely have an easier difficulty."
- **Exact prompt — interview-before-writing:** "I'm writing a blog post about this. Ask me any questions you'd [need] to know the answer to in order to write a truly helpful blog post using my expertise, experience, opinions, case studies, etc. Ask me one question at a time and wait for me to finish talking."
- **Exact prompt — rewrite for depth / fewer bullets:** "I want this to be more comprehensive and give more information. There's too many bullet points. Feel free to elaborate on them and only include them if it's truly helpful for understanding these concepts."
- **Exact prompt — length constraint:** "Same with this, but keep it under 250 words."
- **Exact prompt — subheading breakup:** "Let's do some H3 tags or something to break this up a bit."
- **Exact prompt — internal linking:** "Using my sitemap, give me three internal linking opportunities from this blog post" (paste sitemap + the draft post text).
- **Getting the sitemap:** append `/sitemap.xml` to a domain; on Yoast sites specifically open the **post sitemap** entry (isolates blog posts from everything else).
- **Oversized sitemap workaround:** convert the sitemap to a PDF, then upload that PDF to ChatGPT.
- Matt's own referenced content assets: his post "Can I learn SEO on my own?"; his book "Get Found" (self-narrated audiobook, took ~4-5 days to record; on Audible and Spotify); an existing post of his on "how much does SEO cost."

## Case studies / examples / results

- **Matt's own post, "Can I learn SEO on my own?"** — hit Google Discover and got roughly **2,200 clicks within a couple of days**; the keyword itself normally only gets about **20 searches/month**; now "dead in the water" — a "flash in the pan." Checked in actual Search results afterward: real organic clicks for the same query are only in the **1-3 click** range, which Matt says lines up with the real search volume.
- **Matt's TikTok claim** (referenced from ~3 weeks earlier, said to have been verified live on a prior call): **~1,400 clicks in a couple of days** using only AI content, AI images, and a few internal links, in 2026.
- **Unnamed Reddit poster** — copied/"skyscraped" Matt's "Can I learn SEO on my own?" post and structure, targeting the identical title/keyword. Their site: domain rank/authority score **29**, ~**600 visitors/month**. Matt's site cited (via Ahrefs/"hrs"): ~**9,000 visitors/month**. Poster asked how many backlinks they'd need to outrank Matt.
- **Aaron** (call participant) — announced as having ranked #1 for a keyword term; called out by name for the community accountability post.
- **Heather Playford** (call participant) — finished a full blog post with **4 internal links** during the live exercise.
- **Jessa** (call participant) — moved fastest through the exercise (already onto finding internal links while others were still drafting); got **24** content-gap ideas from the sitemap-gap prompt, which she said gave her "a roadmap for the next six months."
- **Dr. Karen** (call participant, Squarespace site) — sitemap bloated to almost **5,000 lines**, nearly all individual per-image URLs from a lightbox feature that gives every image its own link — unusable for the gap-analysis prompt.
- **Nick** (call participant) — asked ChatGPT for 10 interview questions and got 10 questions plus 3-5 sub-questions each, ending up answering roughly **33 questions total** — versus others (e.g. another participant) who got only 5 questions from a similar prompt.
- **Wendell** (call participant) — asked about 2x/week publishing cadence; Matt confirmed he runs both 1x/week and 2x/week client tiers.
- **Manny / competitor sitemap dead-ends** — one participant's chosen competitor's sitemap.xml had only a single line ("generated by Yoast... meant for consumption by search engines... one link, the main link") — flagged as a sign that competitor likely isn't doing well on Google; told to pick someone else. Another participant (Sarah Clark / "Fab Fertile") had competitors ranking for blogs with no sitemap at all.

## Notable verbatim quotes

- "According to a statement SEO dreams are made of" — on the 1,400-clicks-in-days AI-content claim.
- "We're trying to go in through the back door here" — on ranking low-competition question topics without needing backlinks/domain authority yet.
- "This is very much a flash in the pan... we do not want flashes in the pan. We want to get proper traffic to our website." — on Google Discover traffic.
- "Don't just take the first iteration of what it puts out and then paste it on your website."
- "If people don't read your content, it could be the best in the world. You could have the cure for cancer. But if you can't convince somebody to read it, it's not going to be great."
- "The ones who let us do whatever we want typically get the best results." — on clients who allow auto-publish without approval.
- "You get more out of this... or you get out of this what you put into it." — on the community feedback/accountability norm.
- "I have an external link that's showing that I'm not just making all this stuff up."
- "If somebody says definitively this is the best platform and they're not testing other platforms, you know, they're not being truthful." — on LLM choice (ChatGPT vs. Claude vs. Gemini).

## Tradeoffs & nuance

- Backlinks, domain authority, and topical authority genuinely matter for competitive terms — Matt's answer to "do we need domain authority/backlinks" is explicitly "yes and no," not a claim that authority is irrelevant. The tactic here just deliberately targets low-competition question topics to sidestep needing them for now; real backlink work "will come with time."
- Google Discover can deliver a short, high-volume traffic burst disconnected from real search demand (a 20-searches/month keyword still pulled 2,200 Discover clicks) — Matt is explicit this isn't the traffic they're optimizing for. He's not certain what triggers Discover pickup: guesses it's tied to a user's search/interest history, and floats (without confirming) that the "key takeaways at the top" formatting choice might have helped.
- "Best X in [city]" listicles used to be a legitimate ranking strategy; AI answer engines now tend to just recommend whichever single business already has the most citations instead of rewarding a ranked list — framed as a strategy that's shifted over time, not an absolute ban on the format everywhere.
- Internal/external linking guidance is strongest for blog content specifically. Matt's own core "search engine optimization" service page has **zero external links** and still ranks well, while his web design services page does link out (Chamber of Commerce, Google Reviews, Bark.com) — so the linking rules are a strong default for blog posts, not a rigid universal requirement for every page type; also worth checking what competitors do on their equivalent money pages.
- Posting 2x/week produces "a lot more progress" than 1x/week, but Matt frames 1x/week as still genuinely valuable, not an inferior fallback — no penalty is claimed for either cadence, only against publishing twice in the same day.
- Client auto-publish trust is earned over time (~month 3-4) rather than granted upfront, and Matt observes auto-publish clients "typically get the best results" — presented as an observed pattern from experience, not a rigorously isolated causal claim.
- Matt is openly still evaluating which LLM is best for SEO/blog writing (using ChatGPT live on this call, about to test Claude next based on others' claims) and explicitly distrusts anyone claiming a definitive "best platform" without testing alternatives themselves.
- A participant's ChatGPT flow surfaced a prompt asking about a "Google snippet"; Matt couldn't confidently explain what it meant (guessed schema markup or rich results) — left unresolved in the call, flagged here as an open question rather than settled guidance.
