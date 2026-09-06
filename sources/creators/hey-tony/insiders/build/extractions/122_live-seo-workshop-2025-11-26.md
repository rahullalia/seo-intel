# 122 — Live SEO Workshop (2025.11.26)

## Tactics & step-by-step how-to

- **Full "AI blog post that ranks with zero backlinks" workflow**, demoed live end-to-end (~30 min for Matt solo, ~40–70 min for the group with Q&A):
  1. Go to **answerthepublic.com**. Type in the broadest version of what you sell/do (e.g. "hot sauce," "air conditioning," "leaky sink," "SEO," "engagement rings"). Broad beats specific here.
  2. On the left, click **Search Engines → Questions**.
  3. Scroll **past** the top of the results (highest-volume questions) — these are too competitive. Go to page 2 or 3 of the list, looking for questions with volume around **10–20** searches.
  4. Pick one question you can personally answer right now, that's specific, and makes sense for your business (examples pulled live: "where to store hot sauce," "which tile is best for bathroom walls," "how podcasting works," "how to start a small business consulting firm," "how much does private tutoring cost," "what bridal accessories do I need," "questions to ask a house painter").
  5. Copy that question into a blank doc (title the doc after the question, or call it "blog").
  6. Paste a prepared prompt into ChatGPT (or Claude) and swap in your question. (Prompt itself was pasted into the Zoom chat, not read aloud — see Tools section for the closest reconstructed wording.) The prompt is built to return **only the 10 most important interview questions** back to you — Matt added "keep it limited to 10 questions" because without that constraint it was asking 30–40.
  7. Answer the 10 AI-generated questions in your own doc or directly in the chat — **2–3 sentences each is enough**, doesn't need to be grammatically correct. Budget **~1 minute per question** (10 min nominal; the live group got 30 min). Include your real expertise, case studies, specific examples, "family secret" type details — the goal is content that doesn't already exist anywhere on the internet. Repeating yourself slightly across answers is fine.
  8. Optional: answer via ChatGPT's voice mode on your phone instead of typing — but answer **one question at a time** and **do not tap the mic again until it has fully stopped**, or you risk losing the transcript.
  9. Once done, tell it: **"Write me a blog post based on my answers."** (If it hasn't already auto-generated one.)
  10. Copy the output into your CMS (Matt uses WordPress → Posts → Add New). Clean it up for a human reader: strip stray formatting artifacts (vertical lines/dividers), remove list numbering if it's not literally sequential steps, remove emojis, remove any self-promotional CTA-style subheads that don't belong in a pure answer post (Matt cut a "How much does SEO cost in the Hey Tony process" subhead because a blog post answering a question shouldn't pitch your service page in the title/headers).
  11. Set the **title and URL slug** around the core question/topic — pick whichever AI-generated title reads best, don't just default to the literal question text.
  12. Save as **draft**, then **Preview** to check the render.
  13. **Internal linking, phase 1 (before publishing):** in a new tab, Google `site:yourdomain.com "keyword"` — colon immediately after `site`, no space, then the keyword/phrase in quotes — using a keyword that's relevant to your new post's topic. This surfaces existing pages on your own site that already mention that keyword. Open 3 of those pages, find matching anchor text inside your new draft, and hyperlink each to one of those 3 pages (3 outbound internal links total from the new post).
  14. **Publish** the new post.
  15. **Internal linking, phase 2 (after publishing):** run the same `site:` search again to find **3 different pages** (not the same 3 as phase 1). Edit each of those older pages, find matching anchor text, and add a link **from** each of them **to** the brand-new post. This gets already-indexed pages (that Google will recrawl anyway) pointing at the new URL, which speeds up Google discovering it.
  16. Generate a featured/cover image: upload existing on-site images to ChatGPT/Claude and prompt it to create a cover photo "in the style of" those images (see exact phrasing in Tools section). Optionally add "make sure not to include any of the exact images that are in these, make new ones... but in that style" to avoid literal image reuse.
  17. Set **1–2 categories** (never leave "Uncategorized"), leave tags/hashtags/keywords fields **empty**, then hit Publish.
  18. Use the **Page Audit tool/extension** to confirm heading hierarchy is correct (H1 → H2 → H2 → H2, with H3s nested under H2s where relevant) before/after publishing.
- **Client-answer workaround** when you can't personally answer the AI's questions (e.g., they're client-specific): take the list of AI-generated questions into a **recorded Zoom call with your client**, ask them the questions live (can be up to ~50 questions in one call), then feed that transcript to ChatGPT to generate the blog post(s) quickly.
- **Personal/sensitive-topic workaround**: if a question is too personal or sensitive for the AI to answer on your behalf, write that answer yourself, and use ChatGPT only to build the structural framework of the post around it.
- **Speeding up Google's discovery of a full site redesign/relaunch**: post about the new site on social media and email people the link — more real interaction/traffic signals help Google find and crawl the site faster. If the old version of a redesigned site never ranked, don't bother trying to preserve anything from it — just start fresh.
- **Complementary keyword-vetting step (optional)**: before/after picking a question from Answer the Public, paste the exact phrase into **Ubersuggest** or **Semrush** to check search volume and keyword difficulty, to sanity-check how easy it'll be to rank.

## Rules / dos & don'ts (keep every threshold, number, specific)

- Answer the Public: **1 free search/day** with no account; **3 free searches/day** with a free account (no credit card required to sign up).
- Target question **search volume ~10–20**, not the highest-volume questions on the wheel (those might be 1,000+ searches and are far more competitive) — "people are greedy... they want the whole pizza," so don't compete head-on for the biggest slice.
- Ubersuggest example given live: "which tile is best for bathroom walls" → volume **10**, difficulty **5** ("that means it's low... the chances of us ranking are pretty high"). Semrush example: same type of long-tail keyword showed difficulty **NA** (i.e., essentially no competitive data — very low competition).
- Answer each AI-generated question in **2–3 sentences**; don't overthink, doesn't need correct grammar.
- Do **not** put emojis in **heading tags** — "when you have emojis in [a heading], that adds to the keyword," polluting what Google reads as the heading text. Emojis are optional to keep in body copy, but a "gratuitous amount" of emojis anywhere reads as AI-written and should be cut back.
- Do **not** rely on **Index Now** — "kind of like BS... I don't think it really does anything."
- Do **not** use **tags/hashtags/keywords** fields on posts at all — "they don't do anything and people misuse tags," creating dead-end pages. Use **categories** instead.
- Recommended: **5–10 categories total** for a whole site; assign each post to **1–2 categories** (Matt usually does just 1). Never leave a post **"Uncategorized."**
- Internal linking is not optional, but sequencing is flexible: **you can publish without internal links already added, but go back and add them right away — "it's very, very important."**
- Never publish anything you "can't stand behind" — must be genuinely helpful/accurate, especially where AI may have invented an example that doesn't match what you actually said.
- Don't use your literal core-service keyword as a blog title if you're just answering a question — Matt: "if it's for a service page, yes [include service in title], but... we're writing a blog post answering a question," so leave service-page CTAs and terms out of that title/body.
- Local/service businesses (realtor, plumber, etc.): **do not** force-localize every blog post to your city — non-local traffic still helps (see Tradeoffs).
- **Do not** treat social media links to your page as internal/backlink equivalents — "social media links don't really count for much."
- **Do not** use a page found in Google search results if it's a paid/sponsored (Google Ads) result as your internal-linking target — skip sponsored placements.
- If you don't yet have 3 existing posts to link out to, **1 link is acceptable for now** — write more content over time to build out the full internal web.
- There is **no official "site ranking" metric** — authority score (in tools like Semrush) is explicitly called a **vanity metric**: "gives us some idea, but it's not the complete idea."
- Bot traffic does **not** help authority/rankings — only genuine traffic from real sources (organic, social, ads, email, direct/brand search) counts.

## Tools, prompts & resources

- **answerthepublic.com** — free question-mining tool (search-engine "People Also Ask"-style data), 1 free search/day (3/day with a free account, no card).
- **ChatGPT or Claude** — used for (a) generating the 10 interview questions from a topic/question, (b) writing the full blog post from your answers, (c) generating a cover image.
- **Reconstructed prompt content** (exact text was pasted into Zoom chat, not spoken — the AI's own reply reveals the gist): the prompt asks for a fixed list of interview questions framed as something like *"here are 10 sharp questions that will let me write a killer, story-driven, unique, uniquely-mapped blog post on [topic], with your expertise, wild examples and case studies, energy baked in"* — with an explicit instruction appended limiting it to **10 questions** (default without that cap: 30–40 questions).
- **Verbatim follow-up prompt** (quoted directly): *"Write me a blog post based on my answers."*
- **Cover-image prompt** (as Matt described typing it): upload existing site images, then *"make me a cover photo for this blog post [in] the style of the images attached."* Optional add-on to force originality: *"make sure not to include any of the exact images that are in these. Make new ones... but in that style."*
- **WordPress** — Matt's CMS (Posts → Add New → default editor). Workflow is CMS-agnostic ("if you're on any other one, find where your posts are").
- **Google site: search trick** — `site:yourdomain.com "keyword"` (no space after the colon, keyword phrase in quotes) — used twice per post: once pre-publish to find pages to link *from* the new post, once post-publish to find pages to link *to* the new post.
- **Ubersuggest** (paid) — used to check exact-keyword search volume and keyword difficulty; explicitly framed as a complement to Answer the Public, not a replacement.
- **Semrush** — used both for keyword-difficulty lookups and for checking real-world Google ranking position (Matt was ranking #2 on Semrush, based in Canada, vs. #1 on his own machine).
- **Page Audit tool/extension** — used to verify heading tag structure/order (H1/H2/H3) is correctly applied.
- **"They Ask, You Answer"** by Marcus Sheridan — the foundational book/strategy this whole method is a faster, AI-assisted version of.
- **HeyTony Insiders platform** (newly launched) — resources referenced: Monday work sessions with Matt; Denroy for technical fixes (e.g., cart/heading bugs); Kira for in-the-weeds content-writing training; "SEO Makeover" sessions with Leanne (website-design focused); Friday segment **"Why Doesn't This Rank?"** where Matt reviews pages that aren't ranking and diagnoses why. Onboarding is leveled: **Level 1** (~12 minutes of video) covers registering your site with Google (Search Console), submitting a sitemap, and setting up Google Analytics; completing it unlocks **Level 2** (keyword research, etc.). Members only see their current level; admin sees all levels.

## Case studies / examples / results

- **Matt's own live example** — blog post answering "SEO when building a website," written primarily with AI ("I used AI to do like 99% of this"), took **~30 minutes** total. Result: ranking **#1** on his own machine, **#2** on Semrush (Canada-based check) — with **zero backlinks, zero referring domains**. Beat out Squarespace (which has many backlinks), Reddit, Shopify, "mtu," Wix, and bdc.ca in the SERP.
- **Marcus Sheridan / "They Ask, You Answer"** — manually (no AI, no Answer the Public) answered every question he heard daily from customers with a dedicated blog post; took his business from "on the brink of bankruptcy" to a "**over a nine-figure exit**." Cited as the origin case study for this whole strategy — today's version is the same idea sped up with AI tools.
- **Nikki** (sticker business) — live-published during the call: post titled around "how long do scratch and sniff stickers last and how to keep them smelling [good]." Issues caught live: gratuitous emoji use (flagged as reading like AI-written content), a broken heading hierarchy (jumped from H1 straight to H3, skipping H2). Added 2–3 internal links; fixed and published on the call.
- **Dana** (tile showroom) — searching literally "tiles" returned no results on Answer the Public; switching to "bathroom tile"/"kitchen tile" worked. Landed on question "which tile is best for bathroom walls" — Ubersuggest showed volume 10 / difficulty 5 (low); Semrush showed difficulty NA for the same term.
- **Timothy** — some AI-generated questions were answerable only by his client, so he scheduled a client Zoom call to gather answers instead of guessing.
- **Jessa** (sex therapist) — example question surfaced live: "does hot sauce improve sex life." Also asked Matt to compare this method against the other taught method ("writing content that ranks" using high-ranking article summaries + outlines) — Matt's answer: both work, effectiveness varies by industry/keyword; this session's method is just fast to demonstrate live.
- **Esther and several unnamed others** — published live during the session (multiple "another one's published" call-outs); several more were mid-edit or had linking still in progress when the call wrapped.
- Other example questions surfaced from participants' Answer the Public searches during the exercise: "how podcasting works," "how to start a small business consulting firm," "how much does private tutoring cost," "what bridal accessories do I need," "questions to ask a house painter," "what stickers are popular right now."

## Notable verbatim quotes

- "I have zero backlinks, zero referring domains. I didn't do anything else except what we're going to do today."
- "People are greedy. People want the whole pizza. They don't... want a slice, they want to take the whole thing." — on why not to chase the highest-volume question first.
- "This is a trick that a lot of people don't talk about, a lot of people don't do, and a lot of people forget about. But it's honestly like a huge, huge, huge advantage for you." — on the post-publish internal-linking trick to speed up indexing.
- "Index now is kind of like BS. I don't think it really does anything."
- "You literally can look like a genius by just asking the questions that ChatGPT gives you to your client on a Zoom call... Don't tell your client that it doesn't — it only takes like 10 minutes to do."
- "When there's like a gratuitous amount [of emojis]... I'm like, this is like AI written."
- "If I'm getting traffic from five towns over, somebody's not going to hire me. That's totally fine. That is helping my website show up higher in my local area because I'm getting more traffic and I'm ranking for more keywords and I'm helping more people."
- "There's no like site ranking metric. If you're talking about authority score, that is a vanity metric. That gives us some idea, but it's not the complete idea."
- "Don't publish anything that you can't stand behind."
- "You just got SEO done, baby. You're flying."

## Tradeoffs & nuance

- This "Answer the Public + ChatGPT interview" method is positioned as **fast and easy to demo live**, not as universally superior to other taught methods (e.g., the "writing content that ranks" approach using high-ranking article summaries/outlines) — Matt's explicit take: different methods work better depending on industry and keyword; pick per situation.
- Voice mode is a faster way to answer the AI's interview questions, but carries a real risk: stopping/restarting the mic before it fully finishes can silently drop the transcript, forcing a redo. Typing is more reliable if you don't want to risk losing answers.
- Publishing speed vs. completeness: it's fine to publish before internal links are fully in place, but that's a "get to it immediately" exception, not a "skip it" license — the linking is called out as "very, very important."
- AI-drafted posts need human quality control before shipping: watch for fake-looking hyperlinks the AI inserts, wrong heading hierarchy, emoji overuse, and invented examples/details that don't match what you actually said in your answers.
- Non-local traffic for local/service businesses is a deliberate tradeoff: visitors from outside your service area will never convert, but the resulting traffic volume and topical/keyword breadth still lift your authority signal, which in turn helps you outrank competitors for the searches that *do* matter locally — visitors who'll never buy are treated as a net positive, not noise to filter out.
- Redesign-and-preserve-rankings guidance is conditional: only worth worrying about preservation if the old site actually had rankings to lose; if it never ranked, skip the preservation question entirely and just rebuild.
- Extending this to product pages: same blog-to-page (and page-to-blog) internal linking logic applies to ecommerce/product pages, not just blog posts — link "how to use/clean/care for" content to and from the relevant product page.
- Incomplete link inventory is handled gracefully, not treated as a blocker: if you don't have 3 pages to link to/from yet, 1 link now is acceptable, with the expectation that the internal "web" fills in as you publish more content over time.
