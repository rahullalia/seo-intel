# 123 — Work Session: Writing A Blog Post

## Tactics & step-by-step how-to

- **Full live workflow (Matt's own example, "SEO when/and building a website"):**
  1. Open AnswerThePublic (free version), log in, go to **Search Engines → Questions** (not the "wheel" visualization — Matt skips that and scans the plain list of questions instead).
  2. Type in the thing you sell/teach as the seed term (Matt used "SEO," James used "dishwasher"/"deep clean dishwasher").
  3. Scan the generated questions and **pick one you can already answer today** — don't pick something you'd need to research.
  4. Sanity-check the candidate question in **Semrush** for keyword difficulty and volume before committing to it.
  5. Open a blank Google Doc, title it `keyword/question` (Matt: "I'll have a template for this in the future"), and title the future blog post the same way.
  6. In ChatGPT, paste the interview prompt (see Tools section) with the question inserted.
  7. If ChatGPT comes back with too many clarifying questions (it asked ~30), tell it: **"ask me only 10 questions."**
  8. Answer the questions via **ChatGPT voice mode on your phone** — read the questions off the desktop screen, answer out loud instead of typing, to save time.
  9. Also paste/keep the questions in the Google Doc as a backup record of the Q&A.
  10. Let ChatGPT generate the full blog post draft from your answers.
  11. Copy the entire draft and paste it into the Google Doc (formatting will break/need cleanup).
  12. Manually strip anything that signals "this is purely ChatGPT written": vertical divider lines/spacers, checkmark-style bullets ("people don't do that"), numbered list markers (1, 2, 3…).
  13. Rewrite the H1/heading to something shorter and more natural than the raw question (Matt shortened his to "Getting it right from day one").
  14. Paste the cleaned content into WordPress using the **default editor** (not a page-builder template), assign it a **category**, do not add tags, save as draft, and preview.
  15. Add internal linking (see below), add a meta description, add a cover image, then publish.
  16. Check back in about a week (Matt: "by Friday") to see if/how the post is ranking.
- **Internal linking — outbound (new post → existing pages):**
  1. Realize/remember to have ChatGPT include internal-link callouts in the draft (Matt forgot and had to add manually — lesson: build this into the *first* prompt next time).
  2. Add a closing section, e.g. an H2 "Want help with your SEO?"
  3. Link out to 3 existing pages: your core service/money page (Matt linked his SEO services page), a supporting cost-explainer post ("How much does SEO cost" → "here's an SEO cost breakdown"), and a tools/process post ("SEO tools at Hey Tony").
  4. Save draft again and double-check the links actually landed.
- **Internal linking — inbound (existing pages → new post), to speed up discovery:**
  1. Search your own site/WordPress admin for a keyword relevant to the new post's topic (Matt searched "redesign").
  2. Open ~3 existing, already-indexed posts that use that word.
  3. Turn that word/phrase into a hyperlink pointing at the brand-new post in each of the 3 pages.
  4. Logic: Google already crawls those older indexed pages regularly, so it discovers the new page fast via the fresh outbound link, instead of waiting to stumble onto the new orphaned page on its own.
- **Image workflow:**
  1. Pull a couple of existing on-brand photos/screenshots you already like from other live pages on the site.
  2. Prompt an AI image tool: *"make me a cover photo for this blog posts in the style of the images attached."*
  3. If the result isn't right (e.g., unwanted text baked into the image), regenerate until you get something usable.
  4. Save/export the image, rename the file to the **exact target keyword**, convert to **.webp** (Matt used Photoshop to do the conversion).
  5. Upload to WordPress; set **alt text = the same title/keyword text**.
- **Meta description:** ask ChatGPT/AI to "write me a meta description for this page," paste the result into the SEO plugin's meta description field, and set the **focus keyphrase** field to the exact target keyword/question.
- **Repurposing existing video content into a blog post (James's method, referenced as his standing strategy):** identify a video that already performed well → turn it into a blog post. When ChatGPT's interview asks for a step-by-step process, pull the steps straight from an existing YouTube video's script/outline instead of writing from scratch; plan to go back later and grab screenshots directly from that video for the post's step-by-step section/images.
- **Final pre-publish checklist Matt talks through on his own post:** fast page, genuinely helpful content, includes case studies/personal opinions, correct heading-tag structure, internal links in and out, image with alt text, meta description + focus keyphrase set.

## Rules / dos & don'ts (keep every threshold, number, specific)

- Pick a question you can answer **today** / already know the answer to — not one requiring research.
- Always check competition before writing: Matt's example had Semrush **keyword difficulty 0, volume 50** — "that is a really good question" to target. James's pick showed **no measurable volume** and Matt still said "that's okay" — greenlit anyway.
- **Never copy-paste directly from ChatGPT onto the site** — always edit first.
- Strip AI "tells" before publishing: vertical spacer lines, checkmark bullets, numbered list markers (1, 2, 3…).
- **Do not use tags in WordPress.** Direct quote: "Nobody should use tags because nobody uses them properly and it's kind of doesn't make sense." Do put every post into a **category**.
- **Internal links: 3 to 5 per blog post** (Matt's direct answer when asked for a recommendation), and **at least one must point to a service/money page** — or, if you don't have a dedicated service page (James's case), point it at whatever you actually sell (e.g., an affiliate page) or the homepage instead.
- Tell ChatGPT to cap clarifying questions (e.g., "only 10 questions") — left unchecked it can ask ~30, which is excessive.
- On an easy/low-competition question, don't over-edit: "if the question's easy, you should be able to rank without doing too, too much editing." But Matt flags his own draft is "pretty thin" in spots and would add more if he were investing more time — thinness is an accepted tradeoff on easy wins, not a universal standard.
- Set the SEO plugin's **focus keyphrase** to match the target keyword/question exactly.
- Name the saved image file the **exact target keyword**; convert to **.webp**; alt text = same title/keyword.
- **Publish as soon as it's ready** — "the sooner you can get it published, the better because then it'll start indexing."
- Crawl frequency after an update/edit "depends on how often they're crawling your site" — sites that publish regularly over years get crawled more often; sites that update once a year get crawled far less. It varies site to site, not a fixed number of days.
- Realistic time budget: finishing a post end-to-end (screenshots, image, publish) once the ChatGPT draft exists should take **roughly half an hour to an hour, at most**.
- EM dashes / "invisible spacer" characters that ChatGPT inserts are a known "tell" that content was AI-written (can reportedly be stripped via certain tools/sites), but as of this call **Matt states it is not currently a Google crawling/ranking issue** — it's a style/authenticity concern, not an algorithmic penalty, and moot anyway since you shouldn't be copy-pasting raw ChatGPT output regardless.

## Tools, prompts & resources

- **AnswerThePublic** (free version) — Search Engines → Questions tab; type in your product/service as the seed term to surface real user questions. Matt deliberately skips the "wheel" visualization in favor of the plain question list.
- **Semrush** — used live to check keyword difficulty and search volume for candidate questions before writing (example: difficulty 0, volume 50).
- **Google Docs** — blank doc titled `keyword/question`, used to store the target keyword and the ChatGPT Q&A backup; Matt: "I'll have a template for this in the future."
- **ChatGPT** — core drafting engine, used both via desktop text and mobile **voice mode**.
  - Exact interview-starter prompt (quoted): *"I'm writing a blog post answering this question [paste question]. Ask me any questions you need to know the answer to in order to create a truly unique, helpful blog post. It should include experience, case studies, etc."*
  - Exact follow-up to cap volume of questions: *"ask me only 10 questions."*
  - Exact meta description prompt: *"write me a meta description for this page."*
  - Exact image prompt: *"make me a cover photo for this blog posts in the style of the images attached"* (attach existing on-site photos as style reference).
- **ChatGPT voice mode (mobile app)** — used to answer the AI's clarifying questions out loud instead of typing, reading the questions off the desktop screen; faster but Matt hit a glitch where the transcript didn't save once, forcing him to redo the entire Q&A pass.
- **AI image generation** (continuation of the same session/tool) — Matt frames the value prop: **~$20/month now** for effectively unlimited cover images vs. **"2 or 300 bucks"** he used to pay per image in the past. Not perfectly reliable — added unwanted text to the image on the first try, and ignored extra reference images, only riffing off one.
- **WordPress** — default editor (not a page-builder template) for pasting content; SEO plugin (Matt calls it "the yo stuff" — appears to be Yoast) for meta description + focus keyphrase, which shows a positive indicator ("it likes it") once set correctly.
- **Photoshop** — used to rename/save the AI-generated cover image as **.webp**.
- Matt's own demonstration site is his own agency ("Hey Tony") — internal links added point to his SEO services page, an "SEO cost breakdown" post, and an "SEO tools" post/page.

## Case studies / examples / results

- **Matt's live example** — target question sourced from AnswerThePublic (phrased in-call as "SEO when building a website" / "SEO and building a website," transcript uses both). Semrush: **keyword difficulty 0, volume 50** — near-zero competition. Wrote the full post live via ChatGPT interview + voice answers; final on-site title: "SEO and building a website, getting it done right from day one" (heading shortened to "Getting it right from day one"). Added 3 internal outbound links (SEO services page, SEO cost breakdown, SEO tools page) plus 3 inbound links from existing posts found by searching "redesign." Generated and uploaded a cover image, set meta description + focus keyphrase, published live on the call. Plan: check ranking by the following Friday.
- **James's example** (dishwasher deep-cleaning business, has existing YouTube/social content) — target question: **"How often to deep clean a dishwasher?"**, sourced from AnswerThePublic; Semrush showed no measurable search volume, greenlit anyway ("that's okay"). James pulled the step-by-step process directly from an existing YouTube video his son made, planning to also lift screenshots from that same video for the post's visuals. His business monetizes via affiliate links (Walmart, Amazon, and "Lowe's is the big push at the moment") rather than a dedicated service page, so the internal "money link" would point to an affiliate page or the homepage instead. James's existing content strategy, stated on the call: identify already-successful videos, then turn them into blog posts. Assigned to finish the post (screenshots + publish) same day/by the next Friday or Monday and report back on ranking.
- **Matt's own time log:** roughly **10 minutes** per pass to voice-answer ChatGPT's interview questions; had to redo the whole pass because the transcript failed to save once, doubling his actual time spent on that step. Estimated **30–60 minutes** for a participant to finish a post end-to-end once the AI draft exists.

## Notable verbatim quotes

- "Find a question that you can answer today or that you know the answer to."
- "I'm writing a blog post answering this question... Ask me any questions you need to know the answer to in order to create a truly unique, helpful blog post. It should include experience, case studies, etc."
- "If the question's easy, you should be able to rank without doing too, too much editing here."
- "Nobody should use tags because nobody uses them properly and it's kind of doesn't make sense."
- "You want to make sure that your site's fully linked."
- "The sooner you can get it published, the better because then it'll start indexing."
- "Using AI to generate images is massive... years ago I would have paid like 2 or 300 bucks for one of these... but now it's 20 bucks a month and I get all this stuff."
- "It's fast. It's a helpful piece of content. It has my case studies, personal opinions." — Matt's own verbal pre-publish checklist.
- On em dashes/AI "spacer" characters: "that's not an issue with Google crawling it at this point" — followed immediately by "we're not going to copy paste directly from ChatGPT" anyway.

## Tradeoffs & nuance

- **Speed vs. depth:** on an easy, zero-competition question, minimal editing is enough to have a shot at ranking — but Matt openly admits his own draft is "pretty thin" in places and would add more "if I was taking more time." Thin content is an accepted tradeoff specifically because the keyword has no competition, not a general endorsement of thin content.
- **Voice-mode answering** is faster and more natural than typing out answers, but carries execution risk — Matt's transcript failed to save once, forcing a full redo and doubling his time on that step.
- **Capping ChatGPT's clarifying questions** (10 instead of the ~30 it defaults to) trades some potential depth/personalization for speed.
- **AI "tell" removal** (spacers, checkmarks, numbered lists) is treated as a style/authenticity issue, not — per Matt, at time of recording — an actual Google ranking or crawling penalty; he still insists on removing them and never publishing raw ChatGPT output as-is.
- **Internal linking is bidirectional and serves two different jobs:** outbound links (3–5, to money/service/support pages) route users and link equity toward pages that make money; inbound links from already-indexed older posts exist purely to accelerate Google's discovery/crawling of the brand-new page.
- **No dedicated service page isn't a blocker** for the "must link to something you sell" rule — an affiliate page or the homepage can substitute.
- **AI image generation isn't fully reliable** on a single pass (unwanted text appeared, extra reference images got ignored) — accept "not bad" results or keep regenerating; the cost math (~$20/month vs. $200–300 per image previously) still favors AI heavily despite the inconsistency.
- **Crawl frequency after publishing/editing is site-dependent**, not a fixed timeline — an actively-publishing, established site gets crawled far more often than one that updates rarely, so "how fast will Google see this" has no single universal answer.
