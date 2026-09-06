# 104 — Work Session: Writing A Blog Post (29.12.2025 Replay)

## Tactics & step-by-step how-to

- **Full live workflow demonstrated (Matt wrote and published his own post, "Can I learn SEO on my own?", during the call):**
  1. Go to **answerthepublic.com**, type in what you sell (e.g., "SEO," "real estate," "plumbing").
  2. Go to **Search Engines → Questions**, scroll down to the question list.
  3. **Skip page 1** of the questions — go to **page 2 or 3**, because these show lower (apparent) search volume and are "a lot easier to rank for."
  4. Pick a question you already know the answer to (Matt's pick: "Can I learn SEO on my own?").
  5. Paste the question into a blank doc labeled question/keyword.
  6. Open ChatGPT (or Claude) and use the interview prompt (see Tools section) with the question pasted in.
  7. Answer the AI's follow-up questions — Matt used **voice mode** to answer instead of typing, so he could "run on sentences and digress," making it feel more natural.
  8. Pull your sitemap: go to `yourdomain.com/sitemap.xml`. It may redirect to `sitemap_index.xml`. Look specifically for the file named **post-sitemap.xml** (not page-sitemap.xml) — select all (Cmd+A) and copy it.
  9. Paste the "internal linking opportunities" prompt (see Tools) followed by the full sitemap text into the AI chat.
  10. Take the 3 suggested internal-link opportunities and manually weave them into the existing text of the new post (pick anchor text already in a sentence, turn it into a link) rather than leaving it as raw AI output.
  11. If the AI's draft is heavy on bullet points, feed each section back in with a "rewrite to prose + bullets" prompt (see Tools), one section at a time — for each section: paste it in, ask for the rewrite, then say "elaborate a little bit" if it's now too thin, then move to the next section the same way.
  12. Clean up formatting manually: remove double/stray spaces, remove leftover bold/font-weight styling pasted in from ChatGPT, remove emojis.
  13. Log into WordPress → Posts → Add New → paste the content into the default editor, then click **Clear Formatting** to strip bolding/font styling that came in with the paste.
  14. Save as a draft frequently while working.
  15. Use **Preview** to confirm the internal links actually rendered/landed correctly in the post.
  16. Set the post's **category** before publishing (don't leave it "Uncategorized").
  17. Generate a featured image: grab 2-3 existing related-post images from your site as style references, feed them to the AI image generator with the image-gen prompt (see Tools).
  18. Download the generated image (comes out as PNG), open in Photoshop, **Save As WebP at ~70% quality**, name the file to match the post/topic.
  19. Upload the compressed WebP as the featured image.
  20. Reciprocal internal linking — open the 3 old pages the sitemap prompt suggested (the ones it said to link *from* into the new post) and edit each one to add a link *to* the new post from within its existing text; **bold the anchor text** so readers can see it's a link.
     - Fallback if you can't find a natural anchor phrase in the existing text: add a lazy "Related: [Post Title]" line/section instead of forcing it into a sentence.
     - Skip adding a link on a page if that page already has "a lot of internal links... almost too many."
  21. Optional: add a **"Key Takeaways"** block at the top of the post (ask the AI to write it) rather than calling it "TL;DR."
  22. Post your published link into the Insiders community section for accountability/feedback.
- **Homepage/blog structure to reduce crawl depth:** have a main "Blog" page listing all posts (auto-sorted, newest at top) reachable in 1 click from the homepage; also link directly to the latest post from the homepage. This also surfaces category links 1 click from the homepage, so even an old post (5-6 months old) sits only 2 clicks from the homepage via its category page.
- **Finding a question when a niche is too narrow/hyper-local:** broaden the seed term in AnswerThePublic (e.g., a small-town Pilates studio should search a broader term like "Pilates," not something over-narrowed) rather than tacking on a city/state name — local businesses don't need to add their location to the seed term.

## Rules / dos & don'ts (keep every threshold, number, specific)

- Skip AnswerThePublic's page 1 of questions; use **page 2 or 3** — lower shown volume = more likely to rank (but the tool doesn't reveal true search volume, only a relative signal).
- AnswerThePublic free/logged-in tier = **3 free searches per day**.
- AI interview prompt should be capped at **"ten questions"** — keep it limited.
- Content does **not** need to be "100% human," but does need to be **"100% helpful"** and use your own personal expertise/experience.
- **Do not overuse bullet points** — if the AI output is bullet-point-heavy, rewrite section by section into paragraphs-plus-bullets for readability.
- **Remove emojis** from blog post copy — considered unprofessional and an AI "tell" in written blog content (fine in texting/social, not in blog posts).
- Always **clear formatting** after pasting AI content into WordPress (strips stray bold/font-weight tags).
- Always **set a category** before publishing — never leave a post "Uncategorized."
- Use **post-sitemap.xml**, not page-sitemap.xml, when pulling sitemap content for internal-link prompts.
- Internal link count: aim for roughly **3 internal linking opportunities** generated per post; when adding reciprocal links from old pages back to the new post, "you should do three times" but Matt deliberately only did it **twice** on his own post, to be able to measure the impact.
- Don't call the summary block "TL;DR" (it's a Reddit-native term) — use **"Key Takeaways"** instead (TL;DR is still usable if you want it, just not Matt's preference).
- Featured image export: compress to **WebP at ~70% quality** — cut Matt's file from **537 KB (PNG) down to 32 KB (WebP)**. An online converter works fine too; Photoshop is just faster for him since he already has it open.
- No text/title/question rendered on the featured image itself — instruct the AI generator not to add on-image text.
- This exercise deliberately **skips secondary keyword research, ideal word-count targets, and keyword-density rules** — because you're targeting a low-competition, directly-asked question rather than a competitive head-term, "we don't necessarily need to play by all those other rules."
- Pricing for done-for-clients blog posts: no fixed rule — "however much you want," can be hourly ($20/hr or $50/hr mentioned as examples) or per-post. Matt's own agency pricing for this kind of post: he first says **"350,"** then self-corrects to **"about 250 or 300 bucks per post"** (their posts are "obviously doing a lot more than this," i.e., worth more than a bare-bones version).

## Tools, prompts & resources

- **answerthepublic.com** — free-tier keyword/question research tool (Search Engines → Questions). 3 free searches/day even when logged into an account.
- **ChatGPT** (with **voice mode** for answering interview questions hands-free) and **Claude** — both used live on the call; several attendees said they were redoing the exercise in Claude. Chat commentary: "Claude's great for writing. ChatGPT is great for brainstorming and strategy." Also referenced in chat: Gemini, Copilot, and custom GPTs (Matt's team builds client-specific custom GPTs loaded with each client's info so outputs "pull specifically from that," but Matt personally doesn't do this for himself since his own ChatGPT history is mixed with personal stuff).
- **Interview/ideation prompt** (paste the target question in, then run this): *"I'm writing a blog post answering this question: [question]. Ask me questions you need to know [before writing it] — keep it limited to ten questions."*
- **Internal-linking prompt (sitemap-based), used twice in two phrasings:**
  1. *"Using my sitemap, give me three internal linking opportunities from this blog post using existing text."* (paste full post-sitemap.xml content directly after this prompt)
  2. *"Give me three pages from my sitemap that I can internal link to this new blog post."*
- **Bullet-to-paragraph rewrite prompt:** *"Rewrite the following to include a paragraph or two along with bullet points. Make it easier for someone to consume the content and understand it."* — run section-by-section, following up with "elaborate a little bit" if needed.
- **Featured image prompt:** *"Generate a featured image in this same style, but don't use the same images [attach 2-3 existing related-post images as style references]. Here is [the topic] for this blog post — you don't need any text on the screen, e.g. the blog title or the question."*
- **Key-takeaways prompt (paraphrased):** ask the AI to "write key takeaways to include at the top of this blog post," then paste the output in at the top of the post.
- **Photoshop** — used to convert the generated PNG featured image to WebP at ~70% quality; a generic online PNG→WebP converter is an equally valid substitute.
- **WordPress default block editor** — paste content, use **Clear Formatting** to strip inherited styling; Preview before publishing to verify internal links landed.
- Matt's own book **"Get Found"** (Amazon, described as "#1 bestseller in search engine optimization") used as an internal/external link target inside his demo post — anchor text was the book title, linking to Amazon.com specifically (not a country-specific Amazon domain) "because a lot of people are in the US."
- Matt's lead-magnet/landing page **"Understanding SEO"** used as another internal link target inside the demo post — explicitly called out as an "orphan page" that stops being orphaned once this internal link exists.

## Case studies / examples / results

- **Matt's own demo post**, built live: seed keyword "SEO," question chosen = **"Can I learn SEO on my own?"** Final published post: **2,600 words** ("a bit long, but it's okay — there's a lot of expertise, experience in there"). Included internal links to his "Get Found" book on Amazon and to his "Understanding SEO" lead-magnet landing page. Featured image: AI-generated, PNG at 537 KB, compressed to WebP at 32 KB. Category set to "SEO." After publishing, he opened 3 existing related posts and added reciprocal links back to the new post — did it on 2 of 3 pages (skipped the third for having too many internal links already), bolding the anchor text.
- **Marla** — physical therapy/Pilates studio in a small town in Alabama; struggled to find matching questions on AnswerThePublic because her seed terms were too narrow/hyper-specific. Advised to broaden the seed keyword (e.g., just "Pilates") rather than appending a location like "Alabama" — local relevance doesn't require geo-modifying the seed term.
- **Attendee accountability check-ins during the 30-minute working break:** Katie, Charles, Michael, Ralph, and Marla/Marlo all reported finishing or being close to finishing their posts; several (Katie, others) redid the exercise using Claude instead of ChatGPT.
- **A participant** ("I published my very first blog post and created a new section in the menu blog...") asked about linking the latest post from the homepage — Matt walked through his own site's blog index + homepage latest-post link + category structure as the model answer (see crawl-depth tactic above).
- End-of-call ask: attendees who finished were told to post their published links into the Insiders community/comment thread; only one link had been posted at the time Matt checked, despite Michael and Ralph confirming completion — repeated ask to actually paste the URLs in.

## Notable verbatim quotes

- "Topical authority shows Google, it shows AI what your website is about."
- "It doesn't need to be 100% human, but it needs to be 100% helpful and use your personal expertise."
- "Even if it is an orphan page, that's totally fine. Now it's not orphaned."
- "This is what we call crawl depth. The harder it is to find a page from your homepage, the less likely it is going to be to rank."
- On emojis: "I get rid of emojis because I feel like... that's how we text, but that's not how we type in \[a blog\]... I feel like that makes you not look professional or makes it look like it's written by AI."
- "However much you want. Depends on your business... you could charge 20 bucks an hour, you could charge 50 bucks an hour, you could charge by the post."
- "I don't write blog posts for my own website. Usually I have my team doing that. But because I'm on this call, I'm like, I might as well do it and I'm going to show and prove that this actually works."
- "We just did SEO for an hour. Hell yeah, I'm pumped."

## Tradeoffs & nuance

- AnswerThePublic's "lower volume" signal on page 2-3 questions is a proxy, not a confirmed metric — Matt is explicit: "we don't actually know the real volume, but it's lower, and which may... means it's likely easier to rank for." Treat it as a heuristic, not a guarantee.
- Ranking #1 for a genuinely low-search-volume question isn't really the point — even if the post never gets much direct traffic, it still pays off via topical authority, backlink-ability, and internal-linking connective tissue across the site. This was raised directly as a question (paraphrased: "is it necessary to reach #1 given the low volume of searches?") and Matt's answer reframes the goal away from rank/traffic and toward site-wide authority building.
- Deliberately skipping standard technical-SEO rigor (secondary keyword research, target word count, keyword density) is a considered tradeoff specific to this low-competition, direct-question content type — it is not presented as a universal practice, only as acceptable "because this is a question that people are asking and nobody else is really answering."
- Internal-link quantity is itself being tested live: Matt chose to add only 2 reciprocal links instead of the recommended 3 specifically "because I want to see what the impact is" — an explicit small experiment rather than a fixed rule.
- Local businesses drawing traffic from outside their service area (e.g., ranking for a broad topical question that pulls visitors from another state) is treated as a net positive, not noise — "I don't really care... because that's helping push me locally as well" via domain-wide authority/credibility with Google, even though the direct traffic isn't locally relevant.
- Custom, per-client GPTs are useful for agency-scale content production (Matt's team uses them) but he avoids the practice for his own personal writing since his personal ChatGPT history is comingled with non-work content — a workflow choice, not a universal recommendation.
