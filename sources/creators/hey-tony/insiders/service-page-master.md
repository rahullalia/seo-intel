# The Service Page Master (HeyTony / Matt Diamante)

Everything Matt Diamante teaches about building a service page (a "money page"), organized SEO-first. This is pure HeyTony canon, distilled from the HeyTony Insiders course: 124 coaching-call transcripts, the curriculum, and his tools. Source of record: `heyTonyPlaybook.md`.

The body (sections 1 to 10) is pure HeyTony canon, exactly what came from the course. The appendix (section 11) adds independent 2026 research (NN/G, Backlinko, Ahrefs, Google Search Central) that confirms and extends Matt's method, kept separate so you can always tell what is Matt and what is outside data. This is the single consolidated service-page reference.

## Table of contents

1. SEO first (the foundation everything sits on)
2. The elements (what goes on the page, top to bottom)
3. The visuals (what, and what sort)
4. The metrics (numbers to show, and the SEO numbers)
5. The FAQs
6. CTAs and conversion
7. How to actually build or fix one (workflow + exact prompts)
8. Getting cited by AI (AEO)
9. The don'ts (Matt's kill-list)
10. The tools
11. Appendix: what independent 2026 research adds and confirms

---

## 1. SEO first (the foundation everything sits on)

**The one belief:** SEO is answering real customer questions with real expertise, one page at a time. Google and AI reward genuine, niche, helpful content that says something not already on the internet. The thing competitors and generic AI cannot copy is your experience, opinions, stories, numbers, and cases. Never chase the algorithm; ask "would this genuinely help this customer?" If yes, ship it.

**What a money page is:** any page a visitor lands on when they are ready to buy or hire. Service pages, product pages, collection pages, and location pages are all money pages and all get the same discipline. Blog posts, contact pages, and booking pages are NOT money pages ("those pages don't rank"). The money page sends the visitor to the intake form; the form itself is not the money page. If stuck, ask an LLM: "I am a [realtor], what would be my money page?"

**The five governing rules (these override everything below):**

1. **One keyword per page. Always.** Two pages chasing the same intent cannibalize and Google ranks neither. Word-order and plural variants are the SAME keyword ("Chicago newborn photographer" = "newborn photographer Chicago"). One page CAN rank for many phrasings of one intent. Adding a city makes it a new keyword (a new page).
2. **Never touch a page ranking #1 to #3.** Even if it stuffs the keyword 35 times, has duplicate H1s, or hidden text. You cannot beat #1, so editing is pure downside. If it ranks but does not convert, make tiny UX/CTA edits only (one button, one sentence), never a rewrite. Reinforce it externally instead (blog posts + internal links pointing in). "Don't edit any pages that are ranking, for the love of God."
3. **Match what is currently ranking, never a fixed number.** There is no universal ideal word count, density, or H2 count. Google the exact keyword, pull the top 3, match or slightly exceed. "If you're not ranking, you're either doing too little or too much." Both are equally common.
4. **Do not chase 100% on any audit tool.** 80%+ on a page is fine, 90% site health is fantastic. The composite score does not predict rank. "Sometimes you need that D to help you rank."
5. **On-page content is the #1 lever.** Content beats schema, backlinks, and technical polish. Fix a thin or broken page before adding location pages, channels, or tools. You cannot optimize what does not exist.

**Money page vs blog, the dividing test:** would the searcher Google it to *learn* or to *hire*? Learn = blog (informational). Hire = money page (transactional). A blog post's target keyword should never be your homepage's or money page's primary keyword.

**Homepage vs money page targeting, by business model:**
- **Local / service business:** target `[service] + [city]` on the homepage. The single highest-revenue service becomes the homepage's keyword; every other service gets its own dedicated page.
- **National / virtual with no base:** optimize the homepage for the largest nearby metro, then spin out location pages.
- **If your homepage naturally outranks your intended money page** for the term, stop fighting it: treat the homepage as the money page and point future links there.

**The non-obvious SEO truths (things most people get wrong):**
- **Higher keyword density than your competitors means you are over-optimized.** Matt's own page hit 5.04% density (keyword 35 times) vs competitors at 1.76% and 0.9% and fell from #1 to #9. "Higher density does not equal better rankings."
- **Low-competition and local keywords often need only 2 to 3 keyword mentions** to hit the top, not 10 to 12.
- **Internal linking is the single biggest lever** (see section 2). His own SEO service page climbed from position 13 to #1 over years on internal links alone, content untouched.
- **Never put "near me" in a URL or on-page copy.** Google geolocates the searcher automatically; it does nothing and reads as amateur SEO.

---

## 2. The elements (what goes on the page, top to bottom)

### The canonical money-page skeleton
Copy first, then layout (the message dictates the section structure). One section = one H2 = one idea, alternating background tints "like a slide deck." Most important messages near the top, "the longer it is, the less likely people reach the bottom."

1. **Hero:** H1 (focus keyword + city for a local page, plain language) + supporting subhead + one CTA button, all visible with zero scrolling. A trust signal (stars/stat/logos) in or right below it.
2. **Trust row:** pick about 3 of: years of experience, number of happy clients, 5-star rating, licensed/insured, awards, association logos.
3. **About / intro:** what you do, how, who you serve. An audience-identifier layout (icon boxes per persona) so visitors self-identify.
4. **Services / products overview:** brief intro to each, each linking to its own dedicated page (two-tier IA, see below).
5. **Testimonials:** pasted real reviews as text, or a Google reviews widget.
6. **How it works / process:** plain numbered steps of what happens after they book (defuses first-time-buyer anxiety).
7. **FAQ** tied to that page's one focus keyword (see section 5).
8. **Final CTA** at the very bottom of every page (a full-scroll visitor must still have a next action).

Build the body with lists, tables, and explicit numbered steps. For a collection/ecommerce page, put the long informational copy BELOW the product grid (someone landing there is ready to buy, not read).

### Service-page information architecture (two tiers)
- An **overview / parent page** that summarizes and links to each service (not pushed hard for ranking).
- **Individual child service pages, one per service,** where you go hard on SEO. Clean parent-to-child URL nesting (`/services/website-design`).
- Long service lists: keep core services prominent, push the long tail into a mega menu, each item linking to its own page.

### On-page SEO elements (every one you control)

| Element | The rule |
|---|---|
| **H1** | Exactly one, the literal first heading in DOM order, contains the exact keyword, no brand name, live text (never an image). Style it any size via CSS; the tag matters, not the size. |
| **Title tag** | 50 to 60 chars (ideally under 55). Keyword at the very front. Every non-home page = keyword first, brand name last or dropped. |
| **Meta description** | 120 to 155 chars, keyword near the front, unique per page, written as a sales pitch to win the click ("the billboard saying click me"). Google may rewrite it; set one anyway. |
| **URL / slug** | Short, includes the keyword, parent/child structure. No year, no "near me." Change a slug only if the page is not ranking AND has no traffic AND no backlinks (all three). |
| **Headings (H1 to H3)** | H2s support the H1's topic, phrased with the keyword where natural, one more H2 than the top competitor (5 to 10 normal). Never skip a level going down. Avoid H4 to H6. |
| **Word count** | Competitor-relative. Match the top 3 or add ~100 to 200 words (~10%). Trim if you overshoot. Measure body only. Longer must mean more complete, not padded. |
| **Keyword density** | No fixed target. Match the top 3 "plus one." Density higher than competitors = over-optimized. Place the keyword in the H1, title, meta, first 100 words, at least one H2, an FAQ, one image alt + file name. |
| **Readability** | 7th to 8th grade. Paragraphs of 2 to 3 sentences, vary sentence length. "If you can't explain it to a kid, you can't explain it." |

### Internal linking (Matt's #1 growth lever)
"The more internal links you build to a page, the more Google will understand this page is important." Pages have hit #1 on internal links alone. The two rules:
1. **Outbound:** every new blog post links to 3 to 5 other posts + at least 1 money/service page.
2. **Inbound (the half everyone skips):** every time you publish, go back into 3 older, already-indexed posts and add a link from each INTO the new page. Because Google already trusts those old pages, this gets the new page indexed fast, sometimes within hours.

Mechanics: descriptive anchor text that names the destination (never "click here," "learn more," "website"); vary the anchor across links to the same page; in-body contextual links beat a bottom "related" block; a money page links OUT to only 2 to 3 essential resources; 10 to 20 links per page ceiling (hard max 50 to 100); use the CMS's existing-page link picker, not a pasted URL; keep every money page within 3 clicks of the homepage.

### External linking
1 to 2 credible external links per page (zero reads as a crawl dead-end). **Never hyperlink a direct competitor** (naming or comparing them is fine, linking is not). On money pages, external-link to your own legitimacy profiles (Chamber of Commerce, Trustpilot). Contact and About pages are exempt.

### Cannibalization guard
More than one page targeting the same keyword costs you both rankings. A collection page vs a longer-tail blog post is fine. A location added is a new keyword. If a blog post and a service page both already rank and both convert, leave it alone.

---

## 3. The visuals (what, and what sort)

### Images
- **Density:** roughly 1 image every 200 to 300 words, minimum 4 per page, ideally one per section. Every page needs at least a featured image. Do not stuff pretty pictures; every image illustrates a point.
- **Sourcing priority: your own real photos and screenshots > AI-generated > stock.** Real photos build trust ("everyone is a little on high alert on the internet, nervous about scams"). **Exception: for charts and infographics specifically, AI goes to the top** ("they make really great graphics"). Never stock-photo-looking imagery on a page meant to convey a real team.
- **Real artifacts are the strongest imagery a service business has:** real dashboard screenshots, real client-site frames, annotated metrics. Unfakeable by competitors.
- **File names:** rename the actual file to a keyword-descriptive name before upload ("west-african-wedding-ceremony-toronto.jpg", not "1234.jpg"). Google reads the file name as its own signal.
- **Format:** WebP (or AVIF) at ~70% quality, same look at ~1/10th the size. Delete the old originals after converting. Body image ~750px, hero ~1440x720, compress anything over ~1MB. Lazy-load below the fold, but keep the hero eager.
- **Alt text on every image:** identify the medium (photo/illustration/graphic) + a real description. Keyword only where it fits, on at most half the images, never the identical phrase across every image.

### Video
- **Never self-host.** Embed via YouTube or Vimeo (both still get indexed). Google indexes one video per page.
- Not required to rank. Weigh a hero autoplay video's page-speed and mobile cost: "is that video appealing to you, or to a person looking to hire you?"

### The conversion visuals that touch SEO
- **Never use an auto-rotating slider/carousel as a hero, and never an autoplaying hero video.** Most visitors never see slide 2, yet every load downloads every slide, and a carousel that freezes on hover hides the page's own H1. Replace with one static hero (real people/crew) plus persistent descriptive text. "I fucking hate carousels. People don't stick around for it."
- **Trust visuals:** a hero star-rating build (5 gold stars matching Google's color + "Rated 5 stars on Google" hyperlinked to the real review link), in one prominent placement, not repeated. Real team photos beat stock. Screenshots read as more authentic than over-polished imagery.
- **Maps:** replace a live Google Maps iframe with a static WebP screenshot linked to the real listing (Google's own embed is a speed drag and nobody interacts with it).

### Typography
- One "spicy" heading font + one plain body font. More than 3 fonts slows the site; 2 is safe. Google Fonts is the default safe source.
- Body never below 16px (16 to 20px range, 20 standard); H1 ~48px start; line-height ~1.8. Avoid cursive/script for anything read quickly.
- Never use a graphic or image as a heading; it must be live text (Google cannot read baked-in image text).

### Color
- Complementary colors (opposite the wheel) for maximum CTA contrast; keep one color dominant and use the complement only as a small pop. Never split a complementary pair 50/50.
- **Contrast self-check: mentally strip the color and view in grayscale.** If the text is not clearly readable, contrast is too low (this manual test catches failures automated checkers miss). Never pure black on pure white (it "vibrates"); use soft dark gray (#191919). Gold text fails on white, passes on black.
- **Color to audience:** clean blues = trust/B2B; pinks/pastels = playful/kids; muted greens/beiges = organic/natural; bold on dark = gym/fitness; gold on black = luxury. Search "[vibe] color palette" on Pinterest.
- **Corner radius as a brand dial:** more rounded = friendlier (massage, baby photography), less = serious (cybersecurity, B2B).

---

## 4. The metrics (numbers to show, and the SEO numbers)

### 4a. Metrics to display ON the page (proof)
- **The trust row:** pick about 3 real numbers: years of experience, number of happy clients, 5-star rating, licensed/insured, awards, association logos. Put them in or right below the hero.
- **Reviews belong on every money page,** not just a reviews page. Hand-paste 2 to 3 real reviews as plain TEXT (Google cannot read text in a screenshot image), rotating which reviews appear on which page so the same text is not repeated everywhere. Put location-specific testimonials only on the matching location page.
- **Reporting with real numbers is the ethos:** the differentiator is showing what is actually working (real dashboards, real KPIs). A quantified proof row ("204 keywords ranked in 6 months," "60X ROAS") beats vague claims. If it is not true, do not show it. Real numbers or nothing.
- **A live Google-reviews plugin sends NO extra trust signal to Google** beyond the visible text and can slow the page; the pasted text is what carries the SEO value.

### 4b. The SEO numbers (every threshold in one place)

| Element | Rule / number |
|---|---|
| Keyword targeting | One keyword per page, always |
| Title tag | 50 to 60 chars (ideally under 55); keyword at the front |
| Meta description | ~120 to 155 chars; keyword near front; unique per page |
| URL slug | Short, keyword in, no year, no "near me"; change only if not ranking + no traffic + no backlinks |
| H1 | Exactly one, first heading in DOM, exact keyword, no brand name |
| H2 count | One more than the top-ranking competitor; 5 to 10 normal |
| Heading order | Never skip a level going down; skipping up is fine |
| Word count | Match top 3 +100 to 200 (~10%); 750 to 1,500 baseline; 400 to 500 for zero-difficulty; ~2,000 ceiling |
| Keyword density | Match competitors "plus one"; your density above competitors = over-optimized |
| Readability | 7th to 8th grade; paragraphs 2 to 3 sentences |
| Images | 1 per 200 to 300 words; min 4; alt on every image; WebP; keyword in at most half the alts |
| Internal links | 3 to 5 to other posts + 1 money page per new post; +3 inbound from older posts after publishing |
| Internal link ceiling | 10 to 20 per page (hard max 50 to 100) |
| External links | 1 to 2 per page, credible, never to a competitor |
| FAQ | 3 to 4 per page; plain text, never behind an accordion; H2 questions |
| Crawl depth | Money pages within 3 clicks of the homepage |
| Audit score | Ignore the composite; 80%+ per page / 90% site health is fine |
| Ranking pages | Never edit content/structure of a page ranking #1 to #3 (UX/CTA polish only) |
| Money-page fix order | Title, then meta, then H1, then wait 1 to 2 weeks |

**Patience numbers for a page you changed:** judge a title/meta/H1 nudge after ~2 weeks to 1 month; a content change after ~2 to 3 months. Give any newly published or edited page ~1 month before touching it again. A non-ranking page: wait 3 months, then 6 months (internal-link meanwhile) before rewriting. First real movement takes 3 to 6 months minimum; inflection can be month 12 to 14. "SEO only works if you don't give up."

---

## 5. The FAQs

- **Cap at 3 to 4 questions per page, each tied to that page's one focus keyword.** 10+ generic FAQs bolted on after the CTA does nothing ("is this actually helpful to a human being? Probably not"). Each additional real question can become its own blog post.
- **Plain question-then-answer text directly on the page.** Mark each question as an H2 (or plain question-then-answer, no literal "Q:"/"A:"). Answer directly and briefly, then link out to the fuller blog post for depth (the FAQ to blog to money-page chain).
- **Never hide FAQs behind an accordion, toggle, or dropdown** for important SEO content. It adds parsing friction for Google and AI crawlers. "Well, if this information is so important, why is it hidden in a box?" (Supplementary technical detail inside an accordion is fine.)
- **Answer-first for AI:** restate the question, then answer it plainly in the first sentence so an AI can lift it whole.
- **Put an FAQ tied to that page's one keyword on every page, not one central FAQ page.** "If you have all your FAQs on one page, what are we ranking for?" Never repeat identical FAQ text verbatim across pages.
- **Where to source the questions:** real questions customers ask on sales calls, People Also Ask, Reddit, Google Search Console query rows, and your own support tickets. Mine call transcripts with: "What are all the questions and answers that happened in these calls?" ("a gold mine").
- **FAQ schema is deprioritized.** Matt runs no custom schema and it has not moved his AI-citation odds. Turn on a plugin's default schema (free) and skip complicated custom schema. The value is the visible answer text.

---

## 6. CTAs and conversion

- **One primary CTA per page.** Solid, bold, single high-contrast color. Any secondary CTA (call vs form) must visually recede (outline/neutral). "If people have too many choices, they sometimes just choose not to make any choice." A repeated live fix: 5 competing CTAs (Book Now / Call Now / Email / WhatsApp / Inquire) trimmed to one.
- **Do not stop at one CTA top and one bottom.** Add 2 to 3 more spaced through the body so a reader convinced mid-page can act.
- **CTA copy names the specific action.** Never a bare "Learn more," "Contact us," or "Book today." Use "Book a massage appointment," "Start your logo design." Upgrade to keyword-bearing versions where natural: "Shop Now" to "Shop Organic Dog Treats."
- **Phone numbers and emails must be tap-to-call / clickable everywhere,** especially on mobile; anchor a labeled clickable number at the bottom of the screen for a mobile-heavy audience.
- **Call the pricing page "Pricing," not a euphemism** like "Investment" (people search "[service] pricing"). Avoid cursive/script for anything read quickly.
- Keep one dedicated "Get a Quote" page, but also add a small inline quote form (name, phone, email, short message) on each service page.
- **Diagnostic:** traffic fine but form-fills low? The first lever is CTA button color and contrast, not the copy.

---

## 7. How to actually build or fix one (workflow + exact prompts)

### The 5-step money-page audit (run for your page + the top 3 competitors)
1. Copy the audit spreadsheet. Enter your money-page URL + your one focus keyword (never "near me," never a generic term).
2. **pageaudit.com** to paste URL + keyword to Analyze. **Ignore the overall %.**
3. Content tab: copy word count, keyword occurrences, keyword density into the sheet.
4. Metadata tab: copy the title tag and meta description. (Fallback when a page returns all "NA," usually bot-blocked: the "PA" Chrome extension, "Copy All Headings.")
5. pagespeed.web.dev on the URL (mobile + desktop).
6. Repeat identically for the top 3 organic competitors: Google the exact keyword in incognito, skip ads, Reddit, Yelp, directories, take the next 3 genuine ranking business sites.

### The competitor-benchmark method (the core diagnostic)
Never optimize to a fixed number; always benchmark the top 3 and match or slightly exceed. **Cross-check against the LOWEST-ranked of the top 3, not #1** (if #3 ranks with 500 words, aim for ~600, not 3,000 because #1 has 3,000). Verify competitor word counts by eye, not just by tool (tool numbers are often flatly wrong, and review-carousel plugins inflate phantom word counts).

### The two-prompt rewrite (verbatim)

**Prompt 1, SEO tags update:**
> "Here are my current tags and my focus keyword. Update them so the keyword appears naturally, is front-loaded where possible, and matches the style and brand of my business. Also make sure each one is better than my two competitors':
> [PASTE YOUR AUDIT]
> Competitor 1 (Same Order As Mine)
> [PASTE COMPETITOR AUDIT]
> Competitor 2 (Same Order As Mine)
> [PASTE COMPETITOR AUDIT]"

**Prompt 2, full page rewrite:**
> "Here is the content from my product/service page:
> [PASTE YOUR CONTENT]
> Here are the top 2 competitor pages that rank for my keyword:
> Competitor 1: [paste content]
> Competitor 2: [paste content]
> My focus keyword: [keyword]
> Rewrite my page so that:
> - It is clearer, more helpful, and more persuasive
> - Word count is between: [comp low] - [comp high] words
> - Keyword density is similar to the competitors
> - Includes the keyword in natural positions
> - Adds missing topics my competitors include
> - Improves structure, readability, and expertise
> - Keeps my brand voice
> - Uses headings where appropriate
> - Does NOT keyword-stuff
> Produce the final optimized version I should publish."

**Other useful prompts:**
- Identify the page: "I am a [realtor], what would be my money page?"
- Internal links in: "I'm looking for 3 incoming internal linking opportunities to this service/product page: [LINK]. Find me 3 relevant opportunities from my sitemap pasted below. [PASTE SITEMAP]"
- Deepen a section with your expertise: "Ask me five questions to write a better unique piece of content using my expertise, experience, etc." (folds the interview method into the rewrite).
- Get unstuck on any CMS: screenshot the screen, upload it, "Where do I click? What do I do? Talk to me like I'm an idiot."

### Rewrite discipline
- **Never trust the AI's self-reported word or keyword count.** Live, it targeted 2,200 words and delivered ~1,700; targeted 20 to 45 keyword occurrences and delivered 13. Paste the output into **wordcounter.net** and land in the SAME band as competitors, not above or below.
- Copy output to a blank doc, confirm the keyword is present and front-loaded, strip AI formatting, and rewrite any H2 that does not sound like a real person wrote it.
- **Fix priority order: title tag, then meta description, then H1** (keyword front-loaded in all three, ~5 to 10 minutes), then **wait 1 to 2 weeks** before touching on-page content further. Re-run the audit on the new draft before publishing.
- **Do not trust an AI's SEO opinions over the data.** ChatGPT agrees with whatever you propose and "will make shit up" about best practices. "You are the expert." Challenge it: "then why aren't I ranking #1?"

### The 30-day money-page plan (about 1 to 2 hours/week)
Each week: publish 1 blog post linking to 2 to 3 posts + 1 money page; fix 5 red audit issues; fix that week's money page (title + meta, ~5 min); add 3 internal links into that week's money page. Over 30 days: 4 money pages, 4 blog posts, ~20 issues fixed.

---

## 8. Getting cited by AI (AEO)

- **It is all just SEO.** LLMs run a live Google/Bing search at answer time and synthesize from roughly 5 to 10 existing top results. Rank on Google and AI citation follows. **Never block AI crawlers** (do not use Cloudflare's "block AI bots" toggle); if they overwhelm your host, fix it with better hosting + a firewall.
- **Answer the target question immediately, at the very top.** Restate the question as a subheading, answer it plainly in the first paragraph, repeat the keyword near the top. Google effectively weighs the first ~500 words. Cut the hedging, just state it.
- **Back the claim, then pivot.** Google's AI generates a claim first, then finds content that supports it. Read what the AI Overview asserts, state that same claim first, then pivot to your differentiated info. "The average kitchen renovation costs $50 to $75,000 in [area]. However, we can do it for $25,000." Contradicting the claim outright will not get you cited.
- **Structure for extraction:** question-phrased headings, bullet lists, numbered steps, and comparison tables get pulled; dense paragraphs do not.
- **Schema is not the deciding factor.** Extractability of the answer matters more than schema's presence. Turn on a plugin's default schema and move on.

---

## 9. The don'ts (Matt's kill-list for a money page)

- Do not edit a page that already ranks #1 to #3 (or even weakly on page 3). UX/CTA polish only.
- Do not use an auto-rotating carousel/slider hero or an autoplaying hero video.
- Do not hide FAQ or important content behind an accordion/toggle.
- Do not run multiple competing primary CTAs, or a bare "Learn more."
- Do not put "near me" or a year in a URL or on-page copy.
- Do not use a graphic/image as the H1; do not fake a heading with a styled div.
- Do not hyperlink a competitor, ever.
- Do not use stock-looking imagery on a page meant to convey a real team.
- Do not paste reviews as screenshots (Google cannot read image text); use real text.
- Do not chase 100% on an audit tool, or fix a page just because a tool flags a gap vs #1.
- Do not trust an AI's self-reported word/keyword count, or its SEO opinions over real data.
- Do not copy a competitor's "trick" (keyword stuffing, hidden text); they may rank despite it, and it can penalize you.
- Do not keyword-stuff; density above your competitors reads as over-optimization.

---

## 10. The tools

**HeyTony Insiders tools (app.htinsiders.com, same email as your Stripe subscription):**
- **Money Page Doctor:** paste a money-page URL; in ~10 seconds it infers the keyword, finds competitors, checks their title/H1/density, and flags gaps ("keyword mismatch," "content is thin," "blog post detected, competitors are dedicated service pages") or a "you're already ranking #1" banner.
- **Money Page / Service Page Analyzer:** analyzes a service page vs competitors (capped ~20/month).
- **Blog Post Writer, Blog Idea Finder, Reddit Keywords, Topic Cluster Analyzer, Link Gap Analyzer, Keyword Conflict Detector,** and a per-page target-keyword guesser. Built-in "Wisdom" search answers questions from the full call archive with source links.

**Free audit tools:**
- **pageaudit.com** (+ "PA" Chrome extension): per-page title/meta/heading/word-count/keyword-density, can read JS-rendered content.
- **Detailed SEO** (Chrome extension): non-caching live title, meta, canonical, headings, Open Graph.
- **wordcounter.net / characterCounter.net:** verify AI-reported word count, density, and character counts (never trust the AI's own numbers).
- **Image Alt Text Viewer:** every image + alt + file name on a page in one view.
- **pagespeed.web.dev** for speed; **Google Search Console** as the primary diagnostic; **GA4** for AI-referral traffic (session source contains "chatgpt"/"claude"/"perplexity").

**The AI model stack:** ChatGPT for the voice/interview capture (its Whisper voice-to-text is "the best of the best"), Claude for the actual writing (follows word-count/format instructions precisely, edits conservatively, best at spreadsheets). Claude Code builds tools and on-domain pages inside your existing CMS, not the whole website.

---

## 11. Appendix: what independent 2026 research adds and confirms

Everything above is Matt's. This appendix is outside data (Nielsen Norman Group, Backlinko, Ahrefs, Google Search Central, Search Engine Land/Journal, CXL), included because it either confirms his method with hard numbers or extends it where he is light. The reassuring headline: the paid course and independent research agree on every big lever.

- **Above the fold (confirms "most important messages near the top"):** NN/G eye-tracking (57,453 fixations) found 57% of viewing time happens above the fold, 74% in the first two screenfuls, and 42% on the top 20% of the page, regardless of page length. Put the keyword, promise, and proof in that zone.
- **Word count (confirms match-the-top-3):** Backlinko's 11.8M-result study found the average top-10 result is 1,447 words, but word count is evenly distributed across the top 10, meaning length itself is not a ranking factor. What correlates is subtopic coverage, not length. Matt's "match the top 3, do not maximize" is exactly right; 800 to 1,500 is the practical band once process, proof, and FAQ are included.
- **Real photos (confirms real > stock):** faces draw gaze ~38% faster and hold attention ~2x longer than object shots (NN/G); a real photo beat stock by ~35% conversion and a real person beat a generic icon by 48% (CXL); stock actively erodes trust in categories where the relationship is the product (agency, legal, health, home services). Video lift is cited at 20 to 86% (directional).
- **Trust signals (adds numbers to "reviews on every page"):** directional CRO lift ranges: testimonials ~+34%, video testimonials ~+80%, trust badges ~+42%, risk-reversal guarantee ~+27% (matters more as price rises); 73% of B2B buyers rate case studies crucial. External proof (Google, G2) outweighs self-hosted quotes because users assume on-site testimonials are cherry-picked (NN/G). Place proof near every CTA, not in one carousel.
- **FAQ schema (confirms "schema deprioritized," now with a hard date):** Google fully deprecated FAQ rich results in May 2026 (per Search Central), ending even the 2023 gov/health carve-out; no site gets the rich result anymore. The one controlled study (Ahrefs, 1,885 pages that added JSON-LD vs 4,000 controls) found FAQPage schema does not move AI citations. Keep it (harmless), but the value is the visible answer text, exactly as Matt says. BreadcrumbList and Service schema still matter and stay.
- **AEO (confirms and sharpens answer-first):** lead each heading with a self-contained 40 to 60 word answer so an LLM can lift it whole; use question-phrased H2s that mirror real queries; use extractable formats (lists, steps, tables); name the service, location, and credentials explicitly (entity clarity); be concretely specific ("response times average 45 minutes, 24/7" gets cited; "fast, reliable service" does not). Freshness is a real lever: ~83% of AI citations for commercial queries came from pages updated within 12 months, 60%+ within 6 months, so include the year and keep pages fresh.
- **One nuance Matt is light on, high-consideration CTAs:** for expensive or considered services, a low-commitment CTA above the fold ("See our work," "See pricing") with the harder ask ("Book a call") repeated after the proof can outperform leading with the hard ask. Matt's "one dominant CTA repeated" still holds; this just softens the first one.
- **A risk worth naming, sitewide quality:** Google's Helpful Content signals are sitewide, so a batch of thin, templated, city-swapped service pages can suppress rankings across the whole domain, not just those pages. This is exactly why Matt insists location pages carry genuinely unique content, never a template with the city swapped.

Sources: Nielsen Norman Group (attention, trust), Backlinko (word count, internal links), Ahrefs (the JSON-LD / AI-citation study), Google Search Central (FAQ deprecation, helpful content), Search Engine Land and Search Engine Journal (FAQ sourcing, AEO), CXL (real vs stock imagery).

---

*Sources: HeyTony Insiders coaching calls + curriculum (Matt Diamante), distilled in `heyTonyPlaybook.md` (sections 1 to 10); plus the 2026 external research cited in the appendix (section 11). This is the single consolidated service-page reference. Em/en-dash-free per workspace rule.*
