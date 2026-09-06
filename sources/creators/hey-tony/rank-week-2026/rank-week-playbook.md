# Rank Week 2026: Complete SEO Playbook

Everything Matt Diamante ("Tony" / HeyTony) taught across all 5 days of Rank Week 2026,
extracted from the full session transcripts and organized by topic. This is the master
reference: every tactic, strategy, rule, do, don't, tool, and tradeoff he covered.

Source: the five `transcripts/dayN_transcript.txt` files. The exact AI prompts he used live in
`resources/prompts/`. The audit spreadsheet is in `resources/spreadsheets/`.

---

## 1. Core Philosophy (the mental models everything rests on)

- **Be genuinely helpful.** Helpful content is what ranks now, and it is what AI surfaces too. This is repeated every single day.
- **The enemy is regurgitated information, not AI.** Google and AI do not hate AI-written content. They hate content that says the same thing as everything else already out there. Your job is to add information that is not already on the internet.
- **Differentiate with YOUR expertise, experience, opinions, stories, and case studies.** That is the one thing competitors and generic AI cannot copy. Every content workflow he teaches is built to pull this out of you.
- **Consistency beats intensity.** "The people who get results aren't the ones who learn the most in a single week. They're the ones who keep going afterwards." Most people who fail simply stopped too early.
- **Pigs get fat, hogs get slaughtered.** Dominate a slice (one city, one neighborhood, one niche) before reaching for the whole pie. Try to rank for everything and you rank for nothing.
- **Dominate local first, then expand**, even if you serve nationally. Local is less competitive and gives you a foothold.
- **AEO and GEO are just SEO.** Answer Engine Optimization and Generative Engine Optimization are not separate tracks. If you rank on Google, your odds of being cited by AI go way up. Do the same work.
- **AI is a secretary, not a brain.** It takes your expertise as raw input and structures it into output. You provide the experience and review/fact-check everything. Never let it generate from scratch and ship unreviewed.
- **Don't chase Google updates.** Focus on your business and on helpful, expert content. That is what ranks regardless of algorithm changes.
- **Quality over quantity, one page at a time.** Every page is "a door into your business." Build one solid door at a time rather than a hundred weak ones at once.
- **SEO is not mandatory for every business.** If another channel is already working (Instagram, partnerships, profitable ads), scale that. Do not spend a third of your revenue on slow SEO when a faster channel is paying now.

---

## 2. The Rank Week System (the 5-day arc)

The week is one connected workflow. Each day builds on the last:

1. **Day 1: Find a question and write a blog post.** Use a question tool, interview yourself with AI, publish a genuinely helpful post, link it internally.
2. **Day 2: Audit your money page.** Run your money page and your top 3 organic competitors through Page Audit, feed it to AI, drop the data into the audit spreadsheet.
3. **Day 3: Fix your money page.** Use AI to find the gap between you and competitors, then rewrite your page to match what is ranking and slightly outdo it.
4. **Day 4: Internal linking.** Connect your blog post to your money page, and wire your whole site so Google can crawl it and pass authority.
5. **Day 5: The ongoing plan.** A repeatable ~1-hour-a-week routine that cycles through pages and posts forever.

---

## 3. Keywords & Search Intent

### The four search intents

- **Informational**: someone has a problem and wants to learn (the target of blog posts / Day 1).
- **Navigational**: someone wants a specific page ("Netflix login").
- **Commercial**: someone comparing before buying ("this camera or that camera").
- **Transactional**: someone ready to buy now ("emergency plumber"). This is what money pages target.

### Rules and approach

- **One keyword per page. Always.** Two pages targeting the same keyword causes cannibalization: Google cannot decide which to rank and may rank neither. (Heavily emphasized.)
- **You rank pages, not websites.** Your individual page must beat the individual competitor pages ranking for that keyword.
- **Match the keyword to the page type Google already rewards.** If Google ranks collection pages for a term, optimize your collection page, not a product page. If it ranks a features page, optimize that. Look at what type of page sits at positions 1 to 3 and match it.
- **For local businesses, target city + service** (e.g., "Hamilton electrician"). More specific beats broad: neighborhood-level ("movers Leslieville") is easier than city-level ("movers Toronto").
- **Narrow geographically to escape giant competitors.** If page one is Stripe, Wix, and national brands, add a location ("how much to start a cleaning business **in Ontario**"). Local searchers include their region anyway.
- **Target low-volume and even zero-volume keywords on purpose.** Low volume means low competition and high buyer intent, and competitors ignore them. 15% of all Google searches every day are brand new and have never been searched before, so a tool showing zero volume does not mean zero searchers.
- **Keyword research is getting less important**, especially as AI search grows. Do not get hung up on exact volumes.
- **Every keyword-volume number is an estimate.** SEMrush, Ubersuggest, Google Keyword Planner, and HeyKeywords all give different numbers from proprietary algorithms. Treat them as directional only.
- **Drill from broad to narrow to find a keyword in a thin niche:** type a broad term into a keyword tool, look at the variations, pick the one closest to your offer, search that, look at its variations, and repeat until you find one with real volume.
- **Blog posts and money pages must use different keywords.** Blog = informational, money page = transactional. A blog post about "best areas to live in Virginia Beach" links to the "homes for sale in Virginia Beach" money page, it does not compete with it.
- **Keyword overlap inside your blog is fine** as long as each post targets a distinct angle ("roof replacement cost," "roof replacement timeline," "how long does roof replacement take" all share words but are distinct).

### Don'ts

- Don't use the same keyword on two pages.
- Don't trust volume numbers as precise.
- Don't target ZIP codes. People don't search by ZIP code, they use city names.
- Don't target keywords so broad you cannot win them ("website design" gets localized by Google, nobody ranks for it generically).

---

## 4. Writing Blog Posts (the content engine)

### The two-prompt AI workflow (Day 1)

This is the heart of the content method. Exact prompts are saved in `resources/prompts/day1-blogPrompt.md`.

1. Find a real question your customers ask (see tools below).
2. Open ChatGPT, Claude, or Gemini and run **Prompt 1**: tell it the question and ask it to interview you with 5 questions, one at a time, to pull in your expertise, experience, case studies, and opinions.
3. Answer the 5 questions. **Voice mode is Tony's preferred way** to answer, it is faster and more natural.
4. Run **Prompt 2**: ask it to write a clean, WordPress-ready blog post using your answers, with H2/H3 headings only, no horizontal rules, dividers, tables, or callout boxes.
5. Paste into a draft (do NOT publish yet).
6. Add internal links (see Section 6).
7. Title the post with the question you answered.
8. Add images (see below), set a featured image, publish.

### Content rules

- **Write at an 8th-grade reading level** (about age 12 to 13). Easier to read means more readers and more conversions. Tony writes his book at this level.
- **Word count does not matter for informational blog posts.** Helpfulness and expertise matter. (Word count only matters competitively on money pages, see Section 5.)
- **Title = the question** you answered.
- **Use the phrase "WordPress-ready"** in the writing prompt even on Wix, Squarespace, Shopify, or custom sites, because AI understands that format. The one exception: do not use it for Substack.
- **Train your AI on your real voice.** Paste a podcast transcript (or any content in your voice) into Claude/ChatGPT and tell it to remember it as a reference for future posts.
- **Blog posts don't have to be questions.** Questions are the easiest entry point, but statements and studies work too.
- **Blog posts don't have to be about your product.** Educational industry content counts (e.g., "how to write a business plan" for a martial-arts-studio SaaS).

### Images

- Add roughly **one image every 200 to 300 words**.
- Always set a **featured image**.
- Use your own original photos when you can.
- **Alt text**: just plainly describe what the image shows. It is a small SEO factor, don't overthink it.

### Frequency

- **1 to 2 blog posts per week. Never more than 2.** One is the minimum; two is what the highest-paying clients get. Publishing in bulk or auto-publishing looks like spam/AI to Google.
- At 1 to 2 a week you build roughly 100 pages in a year, 200 in two years. Each is a new door into your business.

### Don'ts

- Don't tell AI "write me a blog post about X." That produces regurgitated junk. Always use the interview workflow.
- Don't auto-publish or batch-publish. Review every post.
- Don't publish a blog post on the same keyword as a money page.

---

## 5. Money Pages: Audit (Day 2) and Fix (Day 3)

A **money page** is any product or service page where someone lands wanting to buy or hire (Invisalign page, residential-roofing page, "sell your home" page, a single ecommerce product page). Start with just one.

### The audit workflow (Day 2)

Prompt is in `resources/prompts/day2-moneyPageAudit.md`; spreadsheet in `resources/spreadsheets/`.

1. Go to **pageaudit.com**, paste your money page URL, enter your target keyword, click Analyze. **Ignore the score/percentage entirely** (repeated several times).
2. Open the **Content** tab, select all (Cmd/Ctrl+A), copy.
3. Paste into ChatGPT or Claude. Do NOT press Enter yet.
4. Paste the audit prompt underneath, then press Enter.
5. Paste the AI output into **Column B** of the audit spreadsheet.
6. Open the **Metadata** tab, copy the title tag and meta description into the spreadsheet.
7. Repeat for your **top 3 organic competitors**: search the keyword in incognito, skip all ads and directories (Yelp, Instagram, Reddit), open the top 3 real business results, audit each as Competitor 1/2/3.
8. If a competitor returns all NA (they block bots), use the **Page Audit Chrome extension** on their live page to pull title, meta, headings, word count, and keyword density manually.

### The fix workflow (Day 3)

Prompt is in `resources/prompts/day3-fixMoneyPage.md`.

1. Open your audit spreadsheet and ChatGPT/Claude.
2. Paste the Day 3 prompt, press Enter to initialize, then paste your full spreadsheet data into the same thread.
3. Optionally upload the spreadsheet as a file so the AI can try to crawl the competitor URLs for live data.
4. Read the output: it tells you exactly why competitors outrank you and what to change.
5. **Challenge over-positive output.** If it says "your page is already the strongest," ask "then why am I not ranking number one?"
6. Implement the changes on your money page.

### Strategy for money pages

- **Mirror competitors, then slightly outdo them.** They are doing something Google likes. Match it, then add more of the *right* information users want, not just more words.
- **Word count: match the ranking pack, not the leader.** If position 3 has 500 words, do 600. Do not write 3,000 just because position 1 does. Look at the lowest-ranked page that still ranks.
- **Differentiate against giant/institutional competitors with real, unique value:** real screenshots, real client experience, real depth a generic site can't fake.
- **Keep money pages conversion-focused.** If everyone has the "basics," don't bloat your money page with them. Write a separate blog post with the basics and link to it from the money page.
- **For a brand-new/thin niche, you may need to create awareness of the term itself**, not just rank for it.
- **CRO affects SEO indirectly.** Button/CTA wording is conversion optimization, not SEO. But if visitors land and click nothing, Google reads that as the page not satisfying intent and can rank a competitor higher. Let bigger competitors spend money testing CTAs, then do something similar without copying.

### Don'ts

- Don't worry about the Page Audit score number.
- Don't treat AI output as the bible (word counts especially).
- Don't add generic info to a money page just to hit a word count; use a linked blog post instead.
- Don't try to rank a single landing page or a non-website page (Flowdesk, a Flodesk/squeeze page). You need an actual multi-page website.

---

## 6. Internal Linking (the high-leverage, under-used tactic)

Tony calls this "so easy" that pro agencies forget it, yet "massive" for rankings. Prompt is in `resources/prompts/day4-internalLinking.md`.

### The rules

- **Every blog post links to 3 to 5 other blog posts AND 1 money page.** Roughly 1,000 words means aim for 5 blog links; shorter posts, 3. (Day 1's simpler version: link a new post to your homepage, a service page, and one related post.)
- **Every time you publish a new post, go into 3 older posts and add a link to the new one.** This is how Google finds new content fast by crawling from already-indexed pages. (Emphasized repeatedly.) Make sure those older posts are on related topics.
- **Place links where they make contextual sense** throughout the post, not stacked at the bottom.
- **Rotate which money page you link to.** If you have several, don't always point to the same one; alternate every other week.
- **Anchor text**: link from words that actually describe the destination page.

### Using the Day 4 AI prompt

Paste the prompt into ChatGPT, give it your blog post (URL or full text), then your money page URL plus a description. It returns the best anchor text, the destination, the rationale, the exact paragraph to edit, and a rewritten paragraph with the link in place. Copy that paragraph back into your post.

### Don'ts

- Don't over-link. 2 to 3 is the sweet spot for a new informational post, up to 5 max. Too many links hurts.
- Don't repeat the same link on the same word/phrase multiple times. One link per destination.
- Don't create an identical block of links at the bottom of every page. That is duplicate content; Google wants every page unique.
- When adding a link, **don't tick no-opener, no-referrer, no-follow, or sponsored.** Use a plain regular link.

---

## 7. Technical SEO

### Crawl depth and crawl budget

- **Crawl depth** = how many clicks from the homepage to reach a page. Homepage = 0, nav/homepage links = 1, blog post off the listing = 2. **Keep important pages within 3 clicks.** Four or more clicks deep and Google likely stops caring.
- **Crawl budget** = Google only crawls a limited number of pages per site (the number is undisclosed and varies). Wasting it on dead/orphan/tag pages means your valuable pages get crawled less.

### Pruning dead content

- Delete (or better, **set to draft**) blog posts that have **no traffic, no backlinks, and aren't indexed.** They waste crawl budget.
- Tony deleted **70 dead posts at once** from his own site with zero traffic drop.
- **Mark as draft first** so you can restore. Give a new post **6 months to a year** before pruning it, internal linking can rescue a slow starter.
- Use Google Search Console to find **low-hanging fruit**: posts on page 2 or 3 with real impressions are worth optimizing; posts with near-zero impressions are not.

### WordPress categories vs tags

- **Categories: use them. 5 to 10 max, exactly one per post.**
- **Tags: don't use them at all.** Each tag spawns an orphan page Google won't index; 5 tags across 50 posts = 250 wasted orphan pages.

### Sitemaps

- A broken sitemap stops new posts from indexing. If you rename your blog slug, **resubmit the sitemap.**
- Multiple sitemaps (one for pages, one for posts) are fine and preferred; a master sitemap referencing sub-sitemaps also works.
- Check indexing with **URL inspection** in Google Search Console. With proper internal linking you usually don't need to request indexing manually.

### Bot blocking / crawlability

- **Turn off Cloudflare bot protection** and ask cheap hosts why bots are blocked. Blocking bots hides your site from Google and AI crawlers.
- **Test it with AI:** paste your page URL into Claude/ChatGPT and ask "how many words are on this page?" If it reports far fewer than reality, bots are being blocked.
- If a competitor blocks bots, that is good news: AI can't crawl, rank, or recommend them either.

### Page speed and other

- **Don't embed heavy catalogs/PDFs** that slow the page. Use a thumbnail image that links out to the catalog in a new tab.
- **Tony dislikes carousels/sliders.** People don't wait for the next slide, and they can hurt the word count Google sees. (Social-media carousels are a separate, fine thing.)
- **Schema markup: skip it.** Tony explicitly calls it the classic 80/20 trap: the work that takes 80% of your time for 20% of the result. (Shopify gives you schema automatically, which is one reason he likes it.) Note: his book disagrees and recommends schema, see Section 17.
- **Accessibility helps SEO.** Screen-reader friendliness, contrast, simple language all align with ranking.
- Page-audit/technical tools (SEMrush, Ahrefs, Ubersuggest) overwhelm beginners with noise; he built **audit.heytony.ca** to cut to the issues that matter.

---

## 8. Local SEO & Google Business Profile (GBP)

- **Set up a GBP in every market you want to rank in.** Without it you won't appear in Maps / the local pack or accumulate local reviews.
- Fill the GBP out fully, then go back and **add service descriptions.**
- **Build a dedicated location page on your site for each market**, each with **unique text** (never duplicate content across location pages).
- Put all locations on a single **"locations" page**; don't nest cities under your service URL structure.
- **Location pages must be linked from your site** or Google can't find them. Hidden/secret pages with no inbound internal link are invisible.
- **Word count for location pages:** 400 to 500 words is fine for a non-competitive area; up to 2,000 is not too much if competitive. Mimic the ranking competitors.
- **Reviews:** ask each customer which platform they personally use and get the review there. A mix (Google, TripAdvisor, etc.) is fine. Google reviews matter most.
- **GBP posts:** repurpose blog content into a short GBP post with an image and a "Learn More" button linking back to the full post. Aim for **2 to 3 GBP posts per week.** (If a GBP post is rejected, the image file may be too large.)
- **Local authority building:** local press, chamber of commerce, local partnerships, associations (Rotary), local sports sponsorships.
- **Multiple GBP locations** theoretically amplify reach but split your reviews across profiles. Start with one, learn the workload, then expand.
- **GBP verification** now often requires a video of you physically entering the building.
- Your GBP should link to **your website or menu, never your Facebook page.** Facebook is built to keep people scrolling, away from your business.

---

## 9. Off-Page SEO & Authority

- **On-page is "very, very important." Off-page still matters but differently than before.** Raw backlink count is no longer the game.
- **LLMs build an expertise profile of you** from signals across the web: guest posts (backlinks), podcast features, and mentions. They want to see you as a professional and an expert.
- **Press releases work:** one Insiders member issued a press release and Gemini began recommending her within weeks.
- **Don't buy backlinks.** A student who bought paid backlinks ended up with many bad links that had to be removed, paying twice (to add, then to clean up).
- **Don't let outside vendors post on your blog/marketplace.** Spammers will exploit your domain authority to push links elsewhere.
- **Get traffic from non-Google sources** (email newsletters, social media). Google treats outside traffic to your pages as a positive signal that you're not just gaming search.
- **Linking out to an external checkout on another domain is fine.** You don't have to take payment on your own site.

---

## 10. AI & Tools

### How to use AI

- **AI is a secretary.** It structures YOUR expertise; it doesn't replace your brain. Review and fact-check everything before publishing.
- **The best prompts interview you** (like the Day 1 prompt) and use your stories, opinions, and case studies as raw material.
- **Don't use AI detection / "humanizer" tools.** Tony: "AI detection tools are shit. Don't use those." The fix isn't humanizing AI output, it's starting from genuinely human input.
- **Don't add "AI blocks" to articles** for ranking; there's no evidence yet that they help.
- **Cross-check across models:** run the same analysis in ChatGPT and Claude and compare.
- **Vibe-coded / AI-built sites can rank.** Tony built a site by telling Claude to "put this on the internet," set up GitHub + hosting through it, and it ranks #1 to #2 for "backlink gap." Client-side rendering didn't block ranking.
- **ChatGPT vs Claude:** Tony's current favorite for writing is **Claude** (he and attendees independently found its writing better). **ChatGPT** is still his pick for image generation. Either works for the workflows.

### Tool directory

| Tool | Use |
|---|---|
| **findquestions.com / rankweektraining.com** | Tony's free tools: type what you sell, get customer questions to answer |
| **answerthepublic.com, answersocrates.com, alsoasked.com, Ubersuggest** | Alternative free question-finders |
| **pageaudit.com** + Chrome extension | Pull a page's title, meta, headings, word count, keyword density (the extension is the fallback when a site blocks bots) |
| **audit.heytony.ca** | Tony's full technical site audit (flags red issues with how-to-fix tutorials). Free first month, then ~$10/mo |
| **heykeywords.com** | Tony's cheap keyword research tool (volume + difficulty) |
| **SEMrush / Ahrefs** | Powerful but expensive and noisy; Tony has largely moved off SEMrush (cost, billing horror stories) |
| **Google Search Console** | Indexing status, impressions, low-hanging-fruit posts, and (rolling out) AI-mention tracking |
| **Google Keyword Planner** | Free volume estimates (still just estimates) |
| **Google Trends** | Relative popularity/trend over time, NOT search volume. Pair with a keyword tool |
| **ChatGPT / Claude / Gemini** | The content + audit + title/meta workflows |
| **Shopify** | Best ecommerce platform per Tony: built-in schema, strong SEO defaults, blogging |
| **NotebookLM** | A student turns posts into AI podcast audio embedded above the fold (Tony: theoretically good, unproven) |
| **MailChimp / Kit (ConvertKit) / HubSpot / GoHighLevel** | Email; "they all do the same thing." Email new posts to your list |

---

## 11. The Ongoing Weekly Plan (Day 5): about 1 hour/week

Set up once: find 4 questions to answer (findquestions.com) and pick 4 money pages, drop them into the 30-day plan spreadsheet (one per week).

Each week, repeat:

1. **Publish 1 new blog post.** Link it to 3 other blog posts and 1 money page.
2. **Run audit.heytony.ca and fix 5 serious (red) issues** (each has a how-to-fix tutorial).
3. **Fix the title tag** of one money page (use an LLM to write it).
4. **Fix the meta description** of that same money page.
5. **Add 3 internal links** to that money page from other pages.
6. **Next week: rotate** to the next money page and next blog question.

After 4 weeks, refill the list with 4 new questions and 4 pages (or loop the same ones).

**Bonus reinforcement:** email your list every time you publish (include a few older posts too) and share on social. The outside traffic is a positive ranking signal. Keep a consistent send schedule (e.g., every Monday); time of day doesn't matter, frequency consistency does (don't blast 10 emails in a week or people unsubscribe).

**The mindset:** every week you don't publish, a competitor might. The pack at positions 2 and 3 is doing this work.

---

## 12. Master DO list

- Answer your customers' real questions on your website.
- Use the two-prompt interview workflow for every blog post; use voice mode to answer.
- Title each post with the question it answers.
- Add a featured image and an image every 200 to 300 words; write plain alt text.
- Publish 1 to 2 posts per week, consistently.
- Link every post to 3 to 5 other posts and 1 money page.
- Every time you publish, add a link to it from 3 older related posts.
- Audit your money page and your top 3 organic competitors before fixing anything.
- Mirror what ranks, then slightly outdo it; match the ranking pack's word count.
- Challenge over-positive AI output ("then why am I not ranking #1?").
- One keyword per page.
- Match your page type to what Google already ranks for the keyword.
- Target specific, lower-volume, higher-intent keywords; narrow geographically to dodge giants.
- Write at an 8th-grade reading level.
- Give each location page unique content; build them one at a time.
- Make a separate page for every distinct service/product you want to rank for.
- Add informational content under ecommerce collection grids; add unique FAQs per product.
- Keep important pages within 3 clicks of the homepage.
- Use WordPress categories (5 to 10, one per post); prune dead posts to draft.
- Set up a GBP per market, add service descriptions, post 2 to 3 times/week with a "Learn More" link.
- Get reviews on whichever platform each customer actually uses.
- Build authority via guest posts, podcasts, press releases, local mentions.
- Email and share every new post to drive non-Google traffic.
- Use Claude for writing; review and fact-check all AI output.
- Spend at least 1 consistent hour per week, forever.
- Save/screenshot the prompts and download the spreadsheet before the member pages come down.

## 13. Master DON'T list

- Don't tell AI "write a blog post about X" with no interview.
- Don't publish regurgitated, generic content.
- Don't auto-publish or batch-publish; don't exceed 2 posts/week.
- Don't put the same keyword on two pages (cannibalization).
- Don't reuse the same FAQ set across products or duplicate location-page text.
- Don't over-link, repeat the same anchor link, or stack a duplicate link block on every page.
- Don't tick no-follow/no-opener/no-referrer/sponsored on internal links.
- Don't use WordPress tags.
- Don't bury pages 4+ clicks deep.
- Don't block bots (Cloudflare/cheap hosts); don't keep carousels or heavy embedded catalogs.
- Don't waste time on schema markup.
- Don't worry about the Page Audit score.
- Don't bloat a money page with "basics"; link to a blog post instead.
- Don't trust keyword volume numbers as exact, and don't rely on Google Trends for volume.
- Don't target ZIP codes or keywords too broad to win.
- Don't try to rank a single landing page or a non-website page.
- Don't delete posts permanently (use draft) or prune a post younger than 6 to 12 months.
- Don't buy backlinks or let outside vendors post on your site.
- Don't use AI detection/humanizer tools; don't add "AI blocks."
- Don't build on an expired domain without checking its history.
- Don't put your GBP link to Facebook.
- Don't force SEO if a faster channel is already paying.
- Don't quit early. That is the number one reason people fail.

---

## 14. Rules, Numbers & Thresholds (quick reference)

| Item | Rule |
|---|---|
| Title tag length | ~55 to 60 characters (cuts off after, especially mobile) |
| Keyword per page | Exactly 1 |
| Internal links per post | 3 to 5 blog links + 1 money page (~1,000 words = 5; shorter = 3); 2 to 3 for a simple new post |
| New post inbound links | Add a link from 3 older posts |
| Images | ~1 per 200 to 300 words, plus a featured image |
| Blog frequency | 1 to 2 per week, never more than 2 |
| Build rate | ~100 pages/year at that cadence |
| Reading level | 8th grade (~age 12 to 13) |
| Competitors to audit | Top 3 organic (skip ads + directories) |
| Money page word count | Match the ranking pack, not the leader |
| Location page word count | 400 to 500 (non-competitive), up to 2,000 (competitive) |
| Crawl depth | Keep key pages within 3 clicks of home |
| WordPress categories | 5 to 10 max, 1 per post |
| WordPress tags | 0 |
| Prune dead posts after | 6 months to 1 year; criteria = no traffic + no backlinks + not indexed |
| Weekly plan | 1 post, fix 5 red audit issues, fix 1 title + 1 meta, add 3 internal links to a money page |
| GBP posts | 2 to 3 per week |
| Ranking timeline | A few rank in 24 hours; realistic is 3 to 6 months |
| New Google searches | 15% of daily searches are brand new |
| Time commitment | ~1 hour per week, consistently |

---

## 15. Pros & Cons / Tradeoffs

- **Informational blog posts vs transactional money pages.** Posts build broad reach, authority, and AI visibility but attract info-seekers who may never buy. Money pages target buyers directly. You need both, on different keywords.
- **Accepting non-local traffic vs deleting it.** Out-of-area visitors won't hire you, but the engagement signals authority that improves your local rankings. One owner deleted such pages and lost hundreds-to-thousands of monthly visitors. Keep the content.
- **One blog post/week vs two.** Two accelerates results (what top clients get) but only if sustainable. Consistent one beats two-then-zero.
- **High-volume vs low/zero-volume keywords.** High volume = more competition, harder. Low/long-tail = easier, higher intent, compounds. Zero-volume can still convert (15% of searches are new).
- **Broad vs narrow geographic keywords.** Broad is dominated by big brands; narrow (neighborhood/region) is winnable and more targeted.
- **Long cornerstone content vs short focused posts.** Tony does NOT recommend 5,000-word pillar pages; users want direct answers. Break topics into smaller specific posts (also more ranking opportunities).
- **Page Audit main tool vs Chrome extension.** Main tool is faster; the extension is the fallback when a competitor blocks bots.
- **Wix vs Shopify (ecommerce).** Keep Wix if you're already ranking; rebuild on Shopify if you're starting over or not ranking (better built-in SEO/schema). Keep any shop on the same domain.
- **Radical page overhaul vs incremental changes.** When unsure, make small changes (a couple of paragraphs or FAQs), wait two weeks, observe, iterate.
- **Deleting dead posts vs keeping them.** Deleting frees crawl budget; the safe middle ground is mark-as-draft so you can restore.
- **Google Ads vs organic SEO.** If ads are profitable, keep running them while SEO builds; don't kill a profitable channel to "do SEO."
- **DIY weekly plan (~1 hr/week, ~free) vs hiring an agency ($1,200+/mo).** Time vs money. The plan is designed so you can do it yourself.
- **Expired domain vs fresh domain.** Expired can carry value but also inherited penalties/shadow bans. Use expired domains only as redirects to your main site, never as the foundation.
- **Multiple GBP locations.** Amplifies reach but splits reviews and doubles the work. Start with one.

---

## 16. Proof points (selected case studies he cited)

- **Marcus (pool company, 2008):** near bankruptcy, answered customer questions on his site each night with no SEO tools, became the #1 pool website in the world within 2 years. The origin story of the whole method.
- **Robert Starling:** spent ~$105K over 3 years with an agency and got nothing; after Rank Week went to #1 and outranked competitors.
- **Victoria (cleaning):** followed the free content for a year, went from $1K to $3K/month marketing spend to $0, now #1 in her city; built her new coaching site with Claude Code.
- **Colin (Scotland, balloons):** wrote a post Monday, was being cited by AI by Wednesday.
- **Tony's own site:** deleted 70 dead posts with zero traffic loss; built a vibe-coded site that ranks #1-2 for "backlink gap."
- **Expired-domain client:** stuck at 30 to 40 visitors/month for a year; moved to a fresh domain and traffic jumped within one month.
- Plus many beginners (Veruna, Yvonne, Maritza) who ranked fast simply by following the steps and not quitting.

---

## 17. From the Book *Get Found* (curated needle-movers)

His 283-page book covers the same system in depth. Below is only the high-impact delta:
the specific, actionable things that ADD to or sharpen the live-training playbook above.
Basics, definitions, and motivation were filtered out. Most of this is net-new because the
live training stayed light on backlinks, technical thresholds, page-type optimization, and
the paid/funnel side.

### On-page specifics (sharper than the training)

- **Front-load the keyword in the title tag** (as close to the start as possible), not just "somewhere in it." People scan in milliseconds.
- **Five required keyword placements per page:** H1, at least one H2, the URL slug, the title tag, and the meta description. Use this as a checklist on every money/content page.
- **H2s should carry keyword variations and subtopics** (this widens your ranking footprint); H3s do NOT need keywords. If you ever need H4 to H6, that is the signal to split the content into a separate page.
- **Meta description: 80 to 156 characters, written for click-through.** Google often rewrites it to match the query, but it always shows on social shares, so write it to earn the click.
- **Never use your target keyword as the anchor text for an external (outbound) link.** You hand your ranking signal to the page you are trying to beat. Use neutral anchors like "source." Keep external-link anchors 1 to 5 descriptive words, and keep external links inside content, never in nav or footer.
- **"Slightly outdo," quantified:** if the competitor uses the keyword 5 times, use 6 (not 16); if they have 1,000 words, write 1,100. Over-optimization is itself a red flag.

### Images, video & speed (Core Web Vitals)

- **Image format and size are hard rules:** convert to **.webp** (a 10MB image drops to ~100KB with no visible quality loss), then .jpg, avoid .png. Keep images **under 250KB (ideally under 100KB)**, full-width images **<=1600px**, in-content **<=800px**.
- **Never host video on your own server. Embed it** (YouTube, Vimeo, Loom) so it doesn't slow the page. Bonus: Google indexes one video per page as an extra search surface, and YouTube auto-transcribes for free (feed that transcript to AI to draft the post).
- **Core Web Vitals targets:** LCP **<=2.5s** (aim faster), INP **<200ms**, CLS **~0** (no layout shift while loading).

### Backlinks & off-page (the training barely covered this)

- **Track referring domains, not raw backlink count.** A site with ~548 referring domains can outrank one with thousands of links. Google effectively counts only ~5 to 10 links per domain; the rest is discounted (his accidental 400K-links-from-one-domain test changed nothing).
- **Target Domain Authority 30 to 60 sites**, not Forbes/NYT. Prioritize niche-relevant links; treat big-authority links as a bonus, not the goal.
- **Copy your competitors' backlinks:** audit your top 3 to 5 competitors' backlink profiles and get listed everywhere they are (directories, Chamber of Commerce, local associations). Repeatable system, not luck.
- **Free backlink tactic:** when an agency emails asking you to link to their client, counter-offer ("get me a dofollow link from a third-party site first, then I'll link back"). They do the outreach; you get the link at zero cost.
- **Podcast appearances = free high-authority backlinks** (every show-notes page links to you) plus a lift in branded searches, which are themselves a ranking signal.
- **NAP (name, address, phone) must be character-identical across every directory/citation.** Any mismatch weakens local verification. Automate with BrightLocal or Semrush.
- **Do not touch Google's Disavow tool** unless you received an actual manual-action notice in Search Console. Google already ignores most junk links; disavowing can remove links that are quietly helping.

### Local & discovery extras

- **Claim Bing too:** import your Google Business Profile into **Bing Places** and your GSC into **Bing Webmaster Tools** (a few clicks each). Bing is ~4 to 5% of search with far less competition.

### Page-type optimization (the most practical part of the book)

- **Product pages:** the H1/title must be a **searchable descriptor, never an invented brand name** ("Mid-Century Modern Sofa," not "Florpavia"), or Google can't connect it to demand. Keep the top clean (photo, name, rating, price, button); put H2 sections, related-product internal links, and an FAQ **below** the add-to-cart fold. **Never paste manufacturer descriptions** (the same text on 50+ sites won't rank).
- **Category/collection pages:** split by specific sub-type (separate pages for "drip coffee makers" and "espresso machines," not one "coffee machines"), each with its own H1 and keyword. Put the **product grid first, optimized content (H2s, buyer guide, FAQ) below it.**
- **Service pages must explicitly state:** the cost (or a range), how long it takes, your process, and what to expect when you show up. These specifics convert comparison shoppers and add rankable content.

### The page-deletion guardrail (refines "prune dead posts" in Section 7)

- **Before deleting ANY page, run two gates: does it have backlinks? does it get organic traffic?** If yes to either, **update it, don't delete.** Deleting a trafficked page destroys domain authority, topical authority, the internal link equity it was passing to your money pages, and any backlinks pointing at it, all at once. So "prune dead posts" means only posts with **no traffic AND no backlinks AND not indexed.**
- **If an edit tanks a page, roll back** to the prior version, watch it recover, then re-optimize in small increments.

### Tools the book adds

- **HeyTony Watchdog:** weekly competitor on-page change monitoring (title, meta, content, links, new pages) in plain English. Knowing what competitors *changed*, not just where they rank, lets you counter.
- **BrightLocal:** local citation submission plus map-grid rank tracking (your rank at different points across a city).
- **Yoast SEO (free):** edit title tags and meta descriptions with a traffic-light score (WordPress and Shopify).
- **Looker Studio (free):** one dashboard combining GSC + GA4 (the book offers a template at getfoundbook.com/looker).
- **GSC tips:** register only once the site is fully live (registering signals Google to crawl immediately); submit the sitemap once at the domain level, don't add individual URLs.

### Channels that feed SEO (Part VI)

- **Diversified traffic is a trust signal** ("spammers don't spend on ads"). You don't need every source, but a mix (organic, paid, social, email, referral, direct) builds legitimacy.
- **The "Subscribe to Newsletter" box is dead.** Capture emails by placement and intent, best to worst: exit-intent popup (bottom corner, doesn't block content) > in-content offer between paragraphs > nav tab > sticky banner. Don't stack a top and bottom sticky banner.
- **Instagram is the best follower-to-email channel** (automate DM-to-email capture with ManyChat).
- **The funnel sequence (his "tying it all together"):** TOP = multi-channel traffic to lead magnets and trust content; MIDDLE = retarget visitors/subscribers plus email nurture; BOTTOM = retarget high-intent (service/product/pricing) visitors with a page-mirrored, time-sensitive, single-CTA ad, plus behavior-triggered emails (visited-but-didn't-convert nudge; abandoned-checkout 10% off within 24 hours); POST-SALE = onboarding content, complementary offers, referral asks.

### Noted discrepancy: schema markup

- **The book RECOMMENDS schema markup** (easy to generate with AI, boosts rich snippets and click-through). **The live Rank Week training said SKIP it** (the 80/20 time-trap, see Section 7). The training is the more recent take. Practical reconcile: with AI it is low-effort, so it is a fine "nice to have" for rich snippets, but it is not a priority next to content, internal links, and the weekly plan.

---

*Compiled 2026-06-19. Sections 1 to 16 are from the Rank Week 2026 session transcripts;
Section 17 is curated from Matt Diamante's book* Get Found *(283 pages, filtered to
needle-movers). Exact AI prompts are in `resources/prompts/`; the audit spreadsheet and the
book are in `resources/`.*
