# On-Page SEO, Money Pages & Audits

The elements you control on the page itself: the keyword each page targets, its title tag, meta description, URL, headings, content depth, keyword usage, images, links, and conversion elements. Plus the two page types that make money (money pages) and the process that diagnoses why any page ranks or doesn't (audits). On-page content is Matt's stated #1 ranking factor, ranked above schema, backlinks, and technical backend. "It all goes back to one keyword per page."

---

## 1. The Governing Rules (these override every rule below)

These five principles decide when to apply everything else. When a specific rule below conflicts with one of these, these win.

### 1.1 One keyword per page. Always. No exceptions.

The single most-repeated rule in the entire curriculum. Every page and every blog post maps to exactly one keyword (a phrase can be 3-4 words, or one full question, or one tight cluster of variants, but one target). "If you have the exact same keyword on two different pages, Google looks at them and goes, well, I don't know which page to rank. Maybe I'm not going to rank either of them." Never combine multiple distinct services, cities, or topics onto one page.

A page can legitimately rank for many *phrasings* of that one intent (people search the same thing differently). That is not a violation. What breaks the rule is two pages chasing the identical or near-identical intent. Word-order and pluralization variants count as identical: "Chicago luxury newborn photographer" / "Chicago photographer newborn" / "Chicago newborn photography" is ONE topic, not three.

### 1.2 Never touch a page that is already ranking #1-#3.

The single most emphatic rule for money pages and audits. "Don't edit any pages that are ranking, for the love of God." Applies even when the page violates every other rule below: duplicate H1s, keyword stuffed 122 times, hidden overlay text, thin content, zero backlinks. You cannot rank higher than #1, so touching it is pure downside (losing the spot) with zero upside.

- **Evidence:** Ellen Mitchell (realtor) ranks #1 for a probate keyword using "probate" 122 times, two duplicate H1 tags, and hidden overlay text behind the nav. Verdict: leave it. Brett ranks #2 for "Miami probate Realtor" on a thin page with zero backlinks and zero referring domains. Leave it. Matt's own "SEO in Hamilton" service page hit #1 after ~1 year on 600-800 words of never-touched content, purely from internal links.
- **If it's #1 but converting at zero:** tiny incremental edits only (one sentence, one button), never a full rewrite. Wait for the rank to actually drop before touching anything larger.
- **The one carve-out:** UX and CTA polish stays fair game on a ranking page (button color, adding a contact link, layout reflow). The freeze applies only to content and structure that could shift rankings, not to conversion-element polish.
- **"Set and forget" has an expiration date.** A page holding #1 for years on little content can lose it once competitors escalate. That drop (not before) is the trigger to redo the competitive audit. Matt's website-design page held #1 for ~2 years on 600-800 words, then got outranked once competitors ran 2,300-2,500 words.

### 1.3 Match what is currently ranking, never a fixed absolute number.

Word count, keyword frequency, keyword density, and H2 count have no universal "ideal." The only real benchmark is whatever is currently ranking #1-#2-#3 for that specific keyword, and that benchmark moves as the competitive set changes. Google the exact keyword, pull the top 3, match or slightly exceed them.

The rule cuts in both directions. Over-optimization (too many words, too much keyword repetition, too many pages) is as common a failure as under-optimization. Sometimes the fix is to trim, sometimes to add depth, depending purely on what the top 3 actually show. "Most of the time, if you're not ranking, you're either doing too little or too much."

### 1.4 Do not chase 100% on any audit tool.

Passing an audit checklist is decoupled from being correctly optimized (or from ranking). 80%+ on a page-audit tool is fine; a 90% site-health score is "fantastic." Chasing the last flags reliably wastes time and can actively produce the cannibalization problem (a plugin telling you to hit a keyword N times regardless of what the #1 competitor does). "Sometimes you need that D to help you rank." The one exception: a paid SEO provider's own site faces a higher credibility bar from prospects than a typical client site does, so Matt keeps his own near-perfect on purpose.

### 1.5 On-page content is the #1 lever.

"If you write good content, then that matters a lot more than just having a schema markup on the page." Content depth and genuine expertise outrank technical polish. Fundamentals before tactics: fix a broken or thin page before adding location pages, channels, or new tools. "You can't optimize what doesn't exist."

---

## 2. On-Page Elements

### 2.1 Title Tags

The blue clickable headline in search results, the browser-tab text, and the title in social-share previews. Directly drives click-through rate; a bad title tag suppresses clicks. "Title tag" and "meta title" are used interchangeably.

| Rule | Spec |
|---|---|
| Length | **50-60 characters**, ideally under ~55. Longer gets truncated with "..." in the SERP. |
| Keyword position | Target keyword **at (or very near) the front** ("really important" / "highest-value tactic"). |
| Structure | Homepage = brand name + focus keyword. Every other page = **focus keyword first, brand name at the end** (or dropped). |
| Uniqueness | Unique per page. Duplicates come from running 2+ SEO plugins (see 4.6). |

- **Do** frame the title as the exact phrase or question people actually search. Good examples cited directly: *"How long should a URL be for SEO?"*, *"Custom WordPress Development,"* *"Fixing 404 Errors,"* *"Disadvantages of Market Mapping: A Comprehensive Guide,"* *"How to Edit Captions in Facebook Reels."*
- **Don't** write editorial or vague titles that map to no real search. Matt's own flagged bad example: *"10 Simple Ways to Improve Your Google Search Ranking"* ("not a well optimized title at all" because the keyword isn't framed as the phrase being searched). Never format a title as "[Post Title] - [Target Keyword]" ("if it feels spammy, it probably is spammy").
- **Don't** panic when Google strips the trailing brand name from the SERP display. That is Google's rendering choice, not a defect; the brand name is still in your HTML (verify with the Detailed SEO extension).
- **AI prompt:** *"Write me a title tag for this page under 60 characters. The focus keyword is [X]."* Or *"five compelling title tag options for this, make sure it includes [keyword]"* and pick the best.
- **Guardrail:** if a page already ranks (or is #1) for a keyword, never strip that exact keyword out of the title while "improving" it. Edit around it, never delete it.

### 2.2 Meta Descriptions

The descriptive snippet under the blue title. Not a direct ranking factor, but it is your pitch to win the click over competing results, so it drives CTR ("the billboard saying click me instead of your competitors").

| Rule | Spec |
|---|---|
| Length | Roughly **120-155 characters** before truncation (guidance clustered at 140-145 and 155-160; a 124-char example was called "kind of where we want it to be"). Precision matters less now: Google increasingly rewrites descriptions on its own, and Yoast cuts them shorter than it used to. |
| Keyword | Include the target keyword **near the front**. |
| Uniqueness | **Unique per page**, never duplicated across the site (duplicates get flagged by audit tools; a common Yoast template bug auto-inserts the same boilerplate into every post). |

- **Do** write it benefit-forward, as an independent sales pitch that names specific services or differentiators and previews the payoff. Never a copy of the title tag.
- **Don't** force a secondary keyword in just because a tool keeps suggesting it ("it'll come up naturally").
- **Don't** rely on an auto-pulled excerpt. Shopify in particular pulls an arbitrary visible text block if none is set (one real case pulled EU product-safety warning copy, a dead giveaway the field was never filled).
- **CTR fix workflow:** ranking well but near-zero clicks almost always traces to a missing or weak meta description and/or an uncompelling title. Write one that includes the keyword and gives a clear, specific preview (for "size of Facebook cover photo," promise the exact dimensions plus a click for full details). First confirm the impressions are current, not a stale spike from months ago.
- **AI prompt:** *"Write me a killer, compelling, click-worthy meta description for this page."* (Generate ~5, pick the best.)

### 2.3 URLs / Slugs

Should reflect the title and tell users what the page is about.

- **Include the focus keyword.** Homepage is the exception (just the bare root domain, already correct, do not "optimize" it further).
- **No character limit, but shorter performs better.** Every page needs a unique URL.
- **Keep the slug short even when the H1 is long.** Put the long natural-language phrase in the H1/title (e.g. "Bookkeeping services in St. Petersburg, Florida for small businesses"), but keep the URL to the core keyword (`/services/bookkeeping`). Matt's own SEO page ranks #1 in Hamilton with "Hamilton" appearing nowhere in the URL, H1, or H2, proof a hard local keyword does not require URL keyword-stuffing.
- **Bad example** (stuffing): `balamedia.ca/hamilton-website-designers-web-design-hamilton`, should have been trimmed to `hamilton-website-designers`. **Good example:** `sociallyinfused.com/services/website-design` (simple, hierarchical, parent → child).
- **Never** put "near me" or "near you" in a URL or on-page copy. Google geolocates the searcher automatically; it does nothing for rankings and reads as "amateur SEO."
- **Never** put a year in an evergreen page's URL (e.g. "best-dental-services-2025"). It signals the page is tied to that year and goes stale. Keep the URL static and update the on-page year in place.
- **URL-change decision framework (check all three before touching a slug):** is it ranking? does it get traffic? does it have backlinks? Change the slug only if **all three** come back negative. Any single "yes" and you leave it: a changed URL is a brand-new page to Google ("new kid at school, nobody knows who they are"), rankings may not carry over, and backlinks to the old URL go void. Even a textbook-correct 301 does not always fully preserve traffic. "Update this with extreme caution."

### 2.4 Headings (H1-H6)

The book analogy: H1 = book title (the page's one topic / target keyword), H2 = chapter titles (subtopics reinforcing the H1), H3 = subheadings within a chapter. Keywords are weighted heavier in headings than in body copy.

**Core rules:**
- **Exactly one H1 per page**, and it must be the **literal first heading in the page's DOM order** (not just visually biggest, and not buried under a hero or a run of H3s). Google reads top-down. "You don't have a secondary title before the book starts."
- **The H1 must contain the exact target keyword and no brand name.** The brand name is already in the title tag and URL; you rank for it automatically. (Brand name in the H1 is more acceptable only on the homepage of a brand-new business establishing recognition.)
- **Never skip a level going down** (H1 straight to H3, or H2 to H4, trips you up). Skipping *up* a level (H3 back to H2) is fine. "If you skip a step going down the stairs, you're gonna trip. But if you skip a step going up, you're fine."
- **H2s must directly support the H1's specific topic**, not be generic value-prop or marketing lines. Demote flowery marketing sentences to plain paragraph text.
- **H2 count:** use **one more H2 than the top-ranking competitor**. 5-10 H2s is "totally fine" for a normal article. Do not drastically overshoot (top page has 50, going to 200 is way over-optimizing).
- **Avoid H4-H6 in practice.** Convert unnecessary H4s to plain paragraph text. Footer titles above menu columns should be H4 or smaller (or plain text), never H1/H2/H3.
- **Semantic tag is independent of visual size.** You can style an H1 small via CSS (the "split H1" trick: real keyword phrase stays inside a small `<h1>`, a punchier tagline sits beside it as a larger H2). Never use a graphic or image as the H1 (Google can't read baked-in image text). Never fake a heading with a styled `<div>` or bolded paragraph.
- **Turn generic step labels into keyword-carrying headings:** "Step 1 / Step 2" adds nothing. Use the action itself ("Clean the door gaskets").

**Duplicate / mis-tagged H1 fixes.** The two-path decision, applied to every extra heading on the page ("does this support what the page is about?"):
- **If it is real topical content mis-tagged as H1:** downgrade the tag to H2. Keep the copy, just fix the level.
- **If it is NOT real content** (a hero box, CTA, testimonial quote, tagline, logo, or client-name callout): strip the heading tag entirely and convert to plain styled paragraph text. Do not even demote to H2.

**Common duplicate-H1 sources to check:**
- **Mobile/desktop block duplication** (Avada, Wix, Squarespace, GoHighLevel, Shopify): a builder encourages duplicating a section and hiding one copy per breakpoint, loading the same heading twice. Fix by building one truly responsive block with per-breakpoint design settings, never by duplicating the block. (Matt's own "website design in Hamilton" page dropped #1 → #7 partly from a mobile/desktop dual-H1 hack; he flags this as gaming the system that "you won't get results" from.)
- **Popup / promo elements** carrying their own heading tag: change the popup's heading to plain paragraph, restyle visually so nothing changes for the visitor.
- **Theme injection:** Avada's Page Title Bar module auto-generates an empty duplicate H1; Kajabi puts a blog-index title above every post's H1; Shopify wires the H1 into the site logo; developers commonly mark every heading H1 by default.
- **Pressing Enter mid-headline** creates two H1 tags. Force the line break with container padding, not a hard return. A heading that wraps to two visual lines can also register as two.
- **Hidden text** (white-on-white) to stuff a keyword invisibly is a cloaking pattern Google devalues; remove on sight.

**Diagnostic tools for headings:** the Detailed SEO or Page Audit Chrome extension shows the live H1/H2/H3 structure and count instantly (use "Copy All Headings"). View Page Source + Ctrl/Cmd-F "h1" locates where a duplicate is injected. A generic "too many H1s" flag lacks specifics; a dedicated heading extension lists each one individually (one case found 13 H1s firing from the logo, signage graphics, and animated elements).

### 2.5 Content Quality, Word Count & Depth

Content is the foundational element. Well-written, genuinely useful, long-form content that answers a question or solves a problem ranks higher and keeps users on the page longer.

**Word count is competitor-relative, never a fixed target.** Google the exact keyword, pull the top 3 ranking pages, and match their count or add roughly **100-200 words (~10%) more**. "I want to do what is proven that Google likes. I just want to do it like 0.0001% more." This is proportional matching, not license to maximize.

| Situation | Rough anchor |
|---|---|
| Program baseline | 750-1,500 words (later refined to 800-1,000) |
| Normal blog post floor | ~500-800 words |
| Zero-volume / zero-difficulty keyword | ~400-500 words is plenty, no need to go deep |
| Ceiling to watch | ~2,000 words on a page; a homepage measured at 10,000 words (2,000 inside heading tags alone) is over-optimized |

- **Over-optimization by length is a common live failure.** A page far longer than the actual top rankers gets told to trim, not add. A 2,000-word page outranked a 3,200-word page from the same niche once intent and formatting matched better. Real competitor pages for one keyword ranged from ~500 to 2,500 words in the same SERP, proving word count itself is not the ranking driver.
- **Measure body content only.** Exclude footer, nav, and sidebar boilerplate.
- **Verify counts manually.** Never trust a single tool. Extension vs. extension vs. a manual copy-paste into wordcounter.net can differ by hundreds of words (one page read 2,000 / 1,900 / 2,400 across three sources). Inflation comes from popups, review-widget text, mobile-version text counted twice, currency/country-selector text, or a plugin injecting hidden duplicate text on every page. If a tool's count is wildly higher than what you can visually count, view the page source.
- **Longer should mean more complete, not padded.** Do not pad with fluff to match a bigger competitor whose length is mostly filler.
- **Cut vague, generic brand copy that does nothing.** Matt's test: if an unrelated business in a different niche could reuse the exact line verbatim ("every woman is uniquely beautiful," "and more"), it is too generic to keep.

### 2.6 Keyword Density & Placement

**No fixed density target exists.** Match the current top rankers, "level plus one."

- **Placement checklist (keyword should appear in):** product/page name (= H1), title tag, meta description, the **first 100 words** of copy, naturally through the body, **at least one H2**, an FAQ, image alt text, and the image file name. Put it **as close to the front as possible** in the title, meta, and H1.
- **Split the phrase into components and count each separately** across the top 3 competitors (e.g. count the service term and the location term individually, not just the literal full phrase). Feed the counts into a spreadsheet, then match or slightly exceed the top competitor ("plus one"). Match the exact phrasing competitors use, not a close synonym (Matt lost "website design" visibility because both competitors beating him used "web design").
- **Red flag:** if your density sits meaningfully higher than competitors', you are almost certainly over-optimized. Matt's own case: 5.04% density (keyword used 35 times) vs. competitors' 1.76% and 0.9%, nearly 5x higher, correlated with his page falling #1 → #9. "Higher density does not equal better rankings. Google increasingly interprets heavy keyword repetition as over-optimization."
- **Low-difficulty and local keywords often need only 2-3 mentions**, not 10-12, to hit the top (one case ranked top-3 for "mechanic" on 3 mentions vs. 0 for all three competitors).
- **Ignore density scoring tools for long-tail / question content.** Yoast and Rank Math are geared toward 3-4-word short-tail phrases and actively work against full-question posts. For a question post the literal question IS the keyword; it appears naturally through writing the answer (~3-4 times) with no deliberate insertion. Do not blindly copy a competitor's keyword-stuffing just because they rank: if their keyword has near-zero competition they did not need to stuff, and copying it risks a penalty on your own site for no benefit.
- **Absurd density readings (600%+, "923%")** mean the keyword field was left blank and the tool defaulted to the domain name. Fix the input, do not trust the number.

### 2.7 Readability

How easily anyone down to grade-school level can follow the writing. Simplifying widens your addressable audience, which is a wider ranking net, not just an accessibility nicety.

- **Target 7th-8th grade** ("if you can't explain it to a kid, you can't explain it"; the model for Matt's own book).
- **Paragraphs of 2-3 sentences; vary sentence length** (drives the Flesch/ease score). Avoid industry jargon that forces a reader to "open a dictionary" ("help desk" → "how do I fix my computer").
- **Do not chase an all-green Yoast/readability score.** The algorithm is "not 100% accurate." Ignore transition-word-count complaints, "key phrase in introduction," and "key phrase density" checks for question content. Yoast flags a page when >25% of sentences run over 20 words (one case flagged at 30.6% vs. the 25% max); use it as a directional prompt to tighten run-ons, not a mandate.

### 2.8 Images & Alt Text

Images improve time-on-page, trust, conversion, and readability (they break up walls of text).

**Density:** roughly **1 image every 200-300 words**, minimum **4 per post**, ideally one per H2 section. Every post needs at least a featured image. Break the 200-word rule where an image does not make sense for a section, compensating with heading breaks.

**Sourcing priority:** real/own photography > AI-generated > stock (real photos build trust; "everyone is a little on high alert on the Internet, nervous about scams"). Exception: for graphs and infographics specifically, AI goes to the top of the list. Never use stock-looking imagery on a page meant to convey a real team or product. AI and stock images are SEO-neutral with proper alt text; the only real concern is brand fit.

**File names and format:**
- **Rename the actual file before upload** to a keyword-descriptive name (4-5 words, e.g. `black-flame-paddle-shirt.jpg`, not `1234.jpg`). Google reads the literal file name as a distinct signal.
- **Use WebP / next-gen formats** (same visual quality as JPEG/PNG at roughly 1/10th the file size). Featured/OG image spec: 1200 x 628.

**Alt text:**
- **Formula:** identify the medium (photo / illustration / graphic / infographic) + be descriptive. Quality ladder: "pancakes" (terrible) → "blueberry pancakes" (thin) → "stack of blueberry pancakes in a kitchen" (good) → "illustration of a stack of blueberry pancakes in a kitchen" (best, if it really is an illustration).
- **Every image needs alt text; none empty.** Alt text serves screen-reader users first, then search engines, then acts as fallback text.
- **Include the target keyword only where it fits naturally, and on at most half the images on a page.** Never repeat the identical keyword phrase sequentially across every image ("Newborn photographer Chicago 1/2/3/4"). Make it specific per variant: every diamond-shape photo (round, cushion, pear, emerald) getting identical alt text "diamond" is a flagged missed opportunity; use shape-specific alt text and file names instead.
- **Proofread the string.** Missing spaces between words break the attribute.
- **AI prompt:** upload the image and ask *"give me an SEO friendly title in alt text for this image."*

### 2.9 Video

- **Never self-host video.** Embed via YouTube or Vimeo even on a strong server ("even then YouTube is just better"). Google indexes one video per page, and an embed still surfaces in search results.
- Video breaks content into digestible sections and increases dwell time (a positive signal). Vimeo embeds still get indexed; the choice is a UX/aesthetics tradeoff, not an SEO penalty.
- **Not required to rank.** Weigh a hero autoplay video's appeal against its page-speed and mobile cost: "is that video appealing to you, or is it appealing to a person looking to hire you?" Embed the matching video *inside* the corresponding blog post (add an H2 like "How to Clean X - Video"), only worth doing when the underlying video already performs.

### 2.10 FAQ Blocks

- **Plain question-then-answer text directly on the page.** Mark each question as **H2** (or plain question-then-answer, no literal "Q:"/"A:" prefix). Answer directly and briefly, then link out to the fuller blog post for depth (FAQ → blog → money page chain).
- **Cap at 3-4 FAQs per page.** 12 on one page is too many; split onto a dedicated page. Each standalone FAQ question can become its own blog post.
- **Never hide FAQs behind an accordion/toggle/dropdown** for genuinely important SEO content. It adds parsing friction for Google and AI crawlers. Supplementary technical detail (product specs) inside an accordion is fine. "Well, if this information is so important, why is it hidden in a box?"
- **Put an FAQ tied to that page's one focus keyword on every page**, not one central FAQ page. "If you have all your FAQs on one page, what are we ranking for?" Never repeat identical FAQ text verbatim across pages.
- A generic FAQ block bolted onto every post after the CTA does not itself help; the bar is "is this actually helpful to a human being?"

### 2.11 Internal Linking (the core on-page growth lever)

The most-repeated fix across every call and one of Matt's highest-performing tactics. "Internal links for the HeyTony site were the biggest factor and the biggest differentiator in why things were ranking really well." "The more internal links you build to a page, the more Google will understand this page is important."

- **Evidence:** HeyTony's own SEO service page climbed from **position 13 to #1** over ~3-4 years on nothing but accumulating internal links from dozens of blog posts, content otherwise untouched. Matt got a page to **rank #1 in 3 hours** using internal linking alone (witnessed live). One member ranked a page #1 for a competitive keyword using internal linking only, after a year of the page sitting dormant.

**The two rules ("your entire internal linking strategy, done"):**
1. **Every new blog post links out to 3-5 other blog posts + 1 money page** (scale to 3 other-post links if the post is short, or fewer for a brand-new site's first post). "Doing half of Google's work for them."
2. **Every time you publish, go back and add a link into the new post from 3 older, already-indexed posts** (different ones than the new post links to), so the new page has inbound links from day one. Because Google already trusts and crawls the old pages, this gets the new page discovered and indexed fast, sometimes within an hour or two. "This is something that experts even forget to do."

**Mechanics:**
- **Descriptive anchor text that names the destination, always.** Never "here," "learn more," "click here," "website," or "get your copy here." Vary the anchor across links pointing at the same money page ("our SEO services," "done-for-you SEO services," "professional SEO services"); repeating the identical anchor reads as manipulation.
- **In-body contextual links, placed higher up, outperform** a "related posts" block dumped at the bottom. Best practice is a mix, weighted toward inline.
- **Direction rule for money pages:** blog posts link TO money pages; money pages link OUT to blog and external sources but do not link out to blog content "as a feature." Money pages reference at most 2-3 essential resource pages. A blog post's only job is sometimes just passing internal-link authority to the money page (it does not always need to rank itself).
- **Link ceiling:** 10-20 links per page (some framing 5-10 at ~1,000 words); hard max 50-100 before it reads as spam. "You'll actually get more out of doing less."
- **Use the CMS's existing-page link picker, never a raw pasted URL**, when linking to your own pages, so the link auto-updates if that page's URL ever changes.
- **Find targets** with `site:yourdomain.com "keyword"` (no space after the colon, phrase in quotes): run once pre-publish to find 3 pages to link the new post TO, once post-publish to find 3 different pages to add links FROM.
- **New sites:** just publish; once you hit ~10-20 posts, go back and add ~3 internal links per post. Retroactively added links still work but take longer to show effect than links present at publish time.
- **Crawl-depth tie-in:** get every page you want ranked to **≤3 clicks from the homepage** (homepage load = 0 clicks; nav/homepage-module links = 1 click). 4+ clicks is the danger zone: "the harder it is for a human to find your page, the less likely Google will care about it." Fix by adding homepage service/recent-post modules and by ensuring the money page is reachable from nav, not buried.

**AI prompts for internal linking:**
> "Using my sitemap, give me three internal linking opportunities from this blog post [using existing text]." Follow-up: "Anchor text, where to place it, give me a sentence where I can add this."

> "I'm looking for 3 incoming internal linking opportunities to this service/product page: [LINK]. Find me 3 relevant opportunities from my sitemap pasted below. [PASTE SITEMAP]"

### 2.12 External Linking

- **At least 1 external link per page** (blog: 1-2, at or near the top, within the first few paragraphs). Zero outbound links reads to Google's crawler as a dead end: "when Google's crawl bots go from another site to yours, it stops there, it can't move on." Cite sources for stats and claims by hyperlinking the exact phrase to the study, not a separate references list.
- **Never link to a direct competitor, for any reason.** Naming, praising, or comparing them in a table is fine; hyperlinking is not. "The number one rule with linking is never link to a competitor."
- **On money pages and the homepage, external-link to your own legitimacy profiles** (Chamber of Commerce, Trustpilot, Glassdoor) rather than an unrelated site. Never link out to a page targeting the same keyword you're trying to rank for (it hands a competitor link equity toward your target). Write the post first, then place external links to sources clearly unrelated to your own target keyword.
- **The "best-of" list technique:** write "best [service] companies in [city]" naming every competitor (say genuinely positive things), but never hyperlink any of them; internally link the page hard toward your own converting pages. You do not have to include your own company. Ranks for "who is the best [X]" / "should I hire [X]" searches.
- Nuance: this is strongest for blog content. Matt's own core SEO service page has zero external links and still ranks; his web-design page does link out. Check what competitors do on their equivalent money pages. Contact and About pages are exempt from linking minimums.

### 2.13 Keyword Cannibalization

**Definition:** more than one page on your own site ranking or competing for the same keyword. Google reliably surfaces only one page per domain per query, so unmanaged overlap costs you the ranking on both. It is about the page's *topic*, not about link destinations (many different blog posts can all link to the same money page without cannibalizing, as long as each post's own topic differs).

- **Same exact keyword or its natural variant on two pages = cannibalization.** Word-order and pluralization variants count as identical.
- **Adding a location makes it a new keyword.** "We buy junk cars, Dallas" and "...Houston" are separate pages, not cannibalization, provided the location content is genuinely substantive (not a template with only the city swapped).
- **Not cannibalization:** a collection/category page vs. a blog post targeting a distinctly longer-tail keyword ("natural granola" collection vs. "benefits of natural granola" post); product-comparison pages (Botox vs. Dysport vs. Xeomin) as their own consideration-stage content type; two genuinely different keyword targets on separate pages ("small business bookkeeping services" vol 40 vs. "outsourced accounting services" vol 440).
- **A blog post's target keyword should never be your homepage's primary keyword.** Use secondary/variant keywords in blog content to avoid self-cannibalizing the homepage.
- **Fixes:** consolidate the two pages into one longer comprehensive piece and 301 the weaker into the stronger; or rewrite each page's tags and content to target distinct variants (or distinct format/angle: a listicle "12 ways to use honeysuckle perfume" vs. an explainer "what's in honeysuckle roll-on"). To de-cannibalize, paste both pages' full content into an LLM and ask it to compare them and recommend what to change on each so they stop competing.
- **The exception:** if a blog post and a service page are already both ranking for the same keyword and both converting, leave it alone. Do not "fix" a technically-cannibalizing setup that is delivering.
- **Never A/B test two pages for the same keyword** (that IS cannibalization). Test variants sequentially over time.
- **Detection tools:** the Money Page Tool (reports which of your own pages ranks #1 for a keyword), keywordconflict.com, and the Insiders Keyword Conflict Detector / Cannibalized Keywords Scanner (default ~50-page scan, adjustable toward 500; not 100% accurate). Cross-check flagged phantom URLs against the sitemap and robots.txt; if absent from both they are likely redirect artifacts, not real pages.

---

## 3. Money Pages

### 3.1 Definition

**A money page is any page a visitor lands on when they are ready to buy or hire.** Product pages, service pages, collection pages, and location pages are all money pages, and they all get the same discipline. The homepage counts as a money page if there is no dedicated page. Blog posts, contact pages, and booking/appointment pages are NOT money pages ("those pages don't rank"), and a third-party booking tool is explicitly not your money page even though your money page is allowed to link out to one. **The money page is the page that sends a visitor TO the intake form; the form itself is not the money page.** If stuck, ask an LLM directly: *"I am a realtor, what would be my money page?"*

Examples: dentist → dental implants / Invisalign; realtor → "homes for sale in Scottsdale"; plumber → 24-hour emergency page; hot sauce co. → "buy ghost pepper hot sauce" / a collection; magician → one page per event type; ecommerce → collection or product page. A single business can and should run multiple money pages (one per service/offer), each pointing to the same lead form.

### 3.2 Homepage vs. Money Page Targeting

Targeting depends on the business model:
- **Local / service business:** target `[service] + [city]` on the homepage (e.g. "dentist in Hamilton," "Residential Roofing in Cincinnati"). The single service that makes the most revenue becomes the homepage's target keyword; every other service gets its own dedicated page.
- **Ecommerce / content / national site:** do NOT target the homepage for one keyword. Ranking happens on lower pages (collections, products, blog posts); the homepage just needs to make a visitor understand what the site is once they land from an entry page. Give each featured product its own homepage section with descriptive text and push actual ranking effort onto individual collection/product pages.
- **National / virtual with no physical base:** optimize the homepage for the single largest nearby metro, then spin out location pages for smaller markets.
- **If your homepage naturally outranks your intended money page** for the target term, stop fighting it: treat the homepage AS the money page (add the keyword/topic there) and point future blog links at the homepage. Jessa's case: her homepage ranked #2 for "online intimacy course for couples" while the dedicated course page ranked nowhere; the fix was to promote the course page to homepage (WP Settings → Reading) and monitor, or accept the homepage as the money page.
- **About, contact, and blog category/taxonomy pages should not be keyword-targeted.** They behave like the homepage, are not expected to independently rank, and duplicate H1s or SEO gaps on category pages usually do not matter (they were never going to rank anyway).

### 3.3 Money Page Structure

The canonical service-business page skeleton (copy first, then layout, message dictates section structure). One section = one H2 = one topic, alternating background tints so each reads distinct ("like a slide deck, one idea per slide"). Most important messages near the top, because "the longer it is, the less likely people reach the bottom."

1. **Hero:** H1 (focus keyword + city for a local page, descriptive/plain language) + supporting subhead + one CTA button, all visible with zero scrolling. A trust signal (stars/stat/logos) in or right below the hero.
2. **Trust row:** pick ~3 of years of experience, # of happy clients, 5-star rating, licensed/insured, awards, association logos.
3. **About / intro:** what you do, how, who you serve; an audience-identifier layout (icon boxes per persona) so visitors self-identify.
4. **Services/products overview:** brief intro to each, each linking to its own dedicated page (two-tier IA: overview/parent page for navigation, individual/child pages where you go hard on SEO per service).
5. **Testimonials:** pasted real reviews or a Google reviews widget.
6. **"How it works" / process:** plain numbered steps of what happens after they book (defuses first-time-buyer anxiety).
7. **FAQ** tied to that page's focus keyword.
8. **Final CTA** at the very bottom of every page (a visitor who scrolls all the way down must still have a next action).

Build the body content with lists, tables, and explicit numbered steps. Shopify collection-page structure specifically ("the biggest missed opportunity when I look at a Shopify store"): intro sentence(s) → product grid → long blog-length paragraphs with images underneath, covering the collection in depth. On a collection page put informational copy BELOW the grid, since someone landing there is ready to buy, not read.

### 3.4 CTAs & Conversion Elements

- **One primary CTA per page.** Solid, bold, single high-contrast color. Any secondary CTA (call vs. form) must visually recede (outline/neutral). "If people have too many choices, they sometimes just choose not to make any choice." Repeated live fix: 5 competing CTAs (Book Now / Call Now / Email Now / WhatsApp Now / Inquire Now) trimmed to one.
- **Do not stop at one CTA top and one bottom.** Add 2-3 more spaced through the body so a reader convinced mid-page can act immediately.
- **CTA copy names the specific action.** Never a bare "Learn more," "Contact Us," or "Book Today." Use "Book a massage appointment," "Start your logo design," "Start your corporate video today." Upgrade keyword-bearing versions where natural: "Shop Now" → "Shop Organic Dog Treats."
- **Phone numbers and emails must be tap-to-call / clickable everywhere**, especially mobile; anchor a labeled clickable number at the bottom of the screen for a mobile-heavy audience.
- **Naming:** call the pricing page "Pricing," not a euphemism like "Investment" (people search "[service] pricing"). Avoid cursive/script for anything read quickly.
- **Reviews belong on every money page**, not just a reviews page. Hand-paste 2-3 real reviews as plain text (Google cannot read text in a screenshot image), rotating which reviews appear on which page so the same text is not repeated everywhere. Put location-specific testimonials only on the matching location page. Never use a review-carousel plugin (found adding ~1,000 words of markup and hurting load; users scroll past carousels).
- **Never use an auto-rotating slider or carousel as a hero.** A carousel that freezes on hover hid a page's own H1 from most visitors; every load still fetches every slide's image. Replace with one static hero (real people/crew) plus persistent descriptive text. "I fucking hate carousels. People don't stick around for it."
- Quote/inquiry forms: keep one dedicated "Get a Quote" page, but also add a small inline quote form (name, phone, email, short message) on each product/service page (more on-page conversion signal, mirrors competitors).

### 3.5 Location Pages (as money pages)

The most fully-worked money-page type. **One page = one keyword = one service = one location.** Never build a page for the same city targeting two services.

- **Home-base exception:** your flagship market can carry a separate page per service ("Chicago Newborn Photographer" AND "Chicago Family Photographer"). Every satellite location gets only ONE service page (whichever service is easiest to rank there); mention other services in passing.
- **Prioritize smaller towns/suburbs over the big nearby city.** Almost nobody targets them, and searchers type their specific town, not a regional abbreviation. A location page usually cannot outrank a genuine local competitor's homepage (their most-backlinked page) without dedicated backlinks, so retarget adjacent smaller markets instead of fighting head-on.
- **Keyword-first title/H1/meta:** "Sell your house fast, Delaware, Ohio," not "Looking to sell your Delaware home quickly." Match the abbreviation people actually type (searchers type "St. Lucie," not "Saint Lucie").
- **Genuinely unique content per location, not a template with the city swapped** (the real cannibalization risk). Reference real local landmarks, venues, neighborhoods, delivery specifics, seasonal color. For non-delivery/remote businesses, anchor in local hooks (nearest hospitals, grocery stores, gyms, trails). Multiplying pages is not the risk; duplicate/templated copy across them is.
- **Do not build every location x service combination "just in case"** (one case would have been 66 pages: 25 cities x 6 event types). Build one page per location with sections per service, and run keyword research to confirm a specific combo genuinely gets searched before building a dedicated combo page. "Pigs get fat and hogs get slaughtered."
- **Word count:** 400-500 words is fine for a low-competition term; if competitive, audit who ranks and match their depth (up to ~2,000). Always organize it so a human reader can consume it and decide to hire you.
- **City-size sizing rule:** a ~500,000-population city (Hamilton, ~15,000 small businesses) justifies targeting the whole city; a 3-4 million metro (Toronto) is too big, target a neighborhood instead.
- **Zero-volume location keywords are still worth a page** if difficulty is near-zero (tools under-report hyper-local terms). Roughly 15% of searches are brand-new each day.

### 3.6 The "Don't Touch a Ranking Money Page" Rule Applied

(See Governing Rule 1.2.) The money-page-specific corollary: **redesign scope is entirely conditioned on ranking status.** Strong existing rankings → preserve verbiage, keywords, and URLs; restructure visually only. Weak or no rankings → free to rewrite from scratch. A "technically broken" money page (duplicate H1s, keyword stuffing, thin content, zero backlinks) should stay broken if it ranks and converts; fixing it "for correctness" risks breaking what drives the business. UX/CTA polish remains the one safe category.

---

## 4. Auditing a Page

### 4.1 Audit Philosophy: what to read, what to ignore

When working a money page, **ignore the audit tool's overall composite score entirely** and read only three things: (a) how many times the target keyword is used vs. competitors, (b) total word count vs. competitors, (c) keyword density vs. competitors. "Ignore everything else. It's there. It's like nothing. Zero."

- **Not every flagged issue needs fixing.** Before fixing anything, ask: do I actually want this page found, indexed, and ranking? Thank-you pages, ad landing pages, contact pages, category/archive pages, and funnel pages routinely trigger "orphan page," "low word count," or similar flags, and that is often intentional and fine.
- **Priority within an audit:** fix red/serious issues first, starting with the lowest-count ones to build momentum. Broken links and missing alt text outrank a title-tag length overage ("having broken links is way worse than having too many characters in your title"). Fix 5-10 issues per week, not the whole report at once (overwhelm is the #1 cause of people quitting).
- **Never run a site-wide audit against a site still mid-construction** (results are dominated by temporary build errors).
- **Cross-check tool output against a non-caching source before "fixing."** Expect a 12+ hour lag before a full site-audit tool re-crawls a fix; an apparent ranking dip right after a fix is often just caching, not a regression.

### 4.2 The 5-Step Money Page Audit (pageaudit.com)

The homework workflow, run for your own money page plus your top 3 competitors, into one shared spreadsheet:

1. Copy the audit spreadsheet. Enter your money-page URL + your one **focus keyword** (never "near me," never a generic un-localized term).
2. **pageaudit.com** → paste URL + keyword → Analyze. **Ignore the overall %.**
3. **Content tab:** copy word count, keyword occurrences, keyword density into the sheet.
4. **Metadata tab:** copy the title tag and meta description.
5. **Chrome extension ("PA" icon)** as the fallback when a page returns all "NA" (usually bot-blocked): surfaces title tag, meta description, H1/H2/H3 (use "Copy All Headings"), word count, and keyword occurrence/density. If it does not populate, wait ~30 seconds or scroll to the bottom then back (lazy-load).
6. **pagespeed.web.dev** on the money-page URL itself (mobile + desktop scores).
7. **Repeat identically for the top 3 organic competitors:** Google the exact focus keyword in incognito, skip sponsored/ad results, skip Reddit/Yelp/IG, skip directories/aggregators, take the next 3 genuine ranking business sites into the same sheet.
8. Do NOT rewrite yet; this is prep for the rewrite (4.4).

pageaudit.com cost ~$30,000-$40,000 to build and is given away free. Word count differs slightly between pageaudit.com and its extension; anything within ~100-200 words is close enough.

### 4.3 The Competitor-Benchmark Method (the core diagnostic)

The single most-repeated diagnostic-and-fix technique. Never optimize to a fixed number; always benchmark against whoever currently ranks #1-#3 for your exact keyword, then match or slightly exceed.

- **Word count:** match the top 3 or add ~100-200 words. Trim if you overshoot.
- **Keyword frequency:** split the phrase into components, count each separately across the top 3, match or "plus one."
- **Heading count:** pull your H1/H2 outline with an extension, use one more H2 than the top competitor.
- **Verify competitor data by eye, not just by tool.** Tool-reported competitor word counts can be flatly wrong (one reported "1300 words" was manually 174; another set of 2,200-3,400 could not be located on the actual page, suspected hidden/popup content). A review-carousel plugin can inflate a real page to 3,000-4,000 phantom words. Sanity-check anything unusual before setting your own target.
- **The full "why doesn't it rank" comparison** (once on-page signals check out): who ranks #1-3, their backlink/referring-domain count, how often and where they use the keyword, whether their content is simply better, whether they use a top summary or key-takeaways block, and how many internal links point at their page.
- **Diagnostic default:** "if you're not ranking, you're either doing too little or too much." Both under- and over-optimization are equally common; always resolve against the actual top 3, never a fixed rule.

### 4.4 The Money Page Rewrite (exact prompts)

**Money Page Doctor** (Insiders tool): paste a money-page/homepage URL; in ~10 seconds it infers the target keyword (double-checking against on-page content), identifies competitors, checks their title/H1/density usage, and flags gaps ("keyword mismatch: competitors appear to target [X] instead," "content is thin," "density too low/high," "blog post detected, competitors ranking are dedicated service pages, consider building one"), or shows a "you're already ranking #1" banner. Always check where you actually rank before acting on any recommendation: if already ranking well (e.g. #2), do not touch the page just because it flags a gap vs. #1.

**Competitor gap analysis:** paste the gap-analysis prompt, then paste your entire audit spreadsheet (your data + all competitor columns) under it. Output analyzes across up to 8 dimensions (title tag, meta description, H1, H2/H3 structure, word count, keyword density, page speed, trust signals), each meaningful gap getting an exact fix with a priority flag (red = do first / yellow = this week / green = nice to have) plus a 3-bullet Quick Wins summary. Challenge vague or self-serving AI claims ("then why aren't I ranking #1?"). Cross-check every suggestion against the real SERP, especially the **lowest-ranked of the top 3**, not the highest (if #3 ranks with 500 words, aim for ~600, not 3,000 just because #1 has 3,000). "ChatGPT will bullshit you."

**SEO tags update prompt (verbatim):**
> "Here are my current tags and my focus keyword. Update them so the keyword appears naturally, is front-loaded where possible, and matches the style and brand of my business. Also make sure each one is better than my two competitors':
> [PASTE YOUR AUDIT]
> Competitor 1 (Same Order As Mine)
> [PASTE COMPETITOR AUDIT]
> Competitor 2 (Same Order As Mine)
> [PASTE COMPETITOR AUDIT]"

**Money page rewrite prompt (verbatim):**
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

**Rewrite discipline:**
- **Never trust the AI's self-reported word count or keyword count.** Verify every time in wordcounter.net (one live demo: targeted 2,200 words, got ~1,700; targeted 20-45 keyword occurrences, got 13). Land in the same band as competitors, not above or below.
- Copy output to a separate blank doc, confirm the keyword is present and front-loaded, swap in the better-testing semantic variant if the data showed one, strip labels/bold, and rewrite any H2 that does not sound like a real person wrote it.
- Refine one section at a time by pasting just that section back: *"can you rewrite this section to be more funny and personable"*; *"you forgot these heading two tags, write a couple paragraphs each and expand on the ideas."*
- **Fix priority order:** title tag → meta description → H1 (keyword in all three, ~5-10 minutes), then **wait 1-2 weeks** before touching on-page content further to see if rankings move. Re-run the page-audit tool on the new draft before publishing.

### 4.5 The 30-Day Money-Page Action Plan

Four weekly cycles, ~1-2 hours/week, same four tasks with a new blog post and a new money page each week:
1. Publish 1 blog post linking to 2-3 other posts + 1 money page.
2. Fix 5 red-flagged audit issues.
3. Fix that week's money page: title tag + meta description (~5 min, one prompt does both).
4. Add 3 internal links to that week's money page from other pages.

Total over 30 days: 4 money pages, 4 blog posts, ~20 issues fixed. Scope is deliberately capped (5 issues, not all of them) to prevent the burnout-driven quitting that stops people by week two. "This is not a sprint, it is a marathon."

### 4.6 Common Flagged Issues & Their Fixes

- **Title tag / meta description "missing / multiple / too long / too short":** "multiple defined" is almost always 2+ SEO plugins running at once (Yoast + Rank Math + AIOSEO each inject their own tags), or a custom build hardcoding the tag twice. Fix: keep exactly one SEO plugin active. "Missing" is hard to trigger (nearly every CMS auto-populates a default). Too long/short: edit in the plugin's SEO Title / meta snippet field at the bottom of the editor.
- **No H1 / multiple H1s:** see 2.4. Detailed SEO extension to count, View Source to locate, demote real content to H2 / strip non-content to plain text.
- **Open Graph issues:** OG Title should mirror the title tag; OG Image is the featured image (set one on any page you'd want shared). If ALL OG issues fire across most pages at once, it almost always means no SEO plugin is installed at all, check that first.
- **Orphan page** (zero inbound internal links): legitimate for thank-you and ad landing pages. If it should be findable, add a link from any relevant page using descriptive anchor text; if it serves no purpose, delete it.
- **Dead-end page** (zero outgoing links): add 3-5 internal links out.
- **Broken link:** manually test the destination. False-positive (external site blocks crawlers): click "manually validate." Real redirect: update your link to point directly at the new URL. No replacement: remove the link.
- **Low word count:** the tool's default 100-word minimum is outdated; real floor is 500+, agency target 1,000-1,500. Measure body only. Fine to ignore on contact, category/archive, and funnel pages.

### 4.7 On-Page Audit Tools

| Tool | Use | Cost |
|---|---|---|
| **pageaudit.com** (free tool + "PA" Chrome extension) | Per-page title/meta/heading/word-count/keyword-density inspector; extension "Copy All Headings" and can see JS-rendered content | Free |
| **Detailed SEO** (Chrome extension) | Non-caching live title tag, meta, canonical, headings, Open Graph | Free |
| **Money Page Doctor** | Auto competitor-gap read on a money page; infers keyword, flags gaps | Insiders |
| **Money Page / Service Page Analyzer** | Analyzes a service page vs. competitors; capped ~20 audits/month | Insiders |
| **HeyTony Site Audit Tool** (audit.heytony.ca) | Site-wide crawl: duplicate/missing tags, orphan pages, broken links, missing H1s, low word count; ~12-24hr recrawl lag; up to 3 sites | $10/mo or $99.99/yr |
| **Rank Report Card** | Full-site score out of 100, pass/fail per factor (H1, page speed, alt text, meta length, mobile) | Insiders |
| **Cannibalized Keywords Scanner / Keyword Conflict Detector** / keywordconflict.com | Flags multiple pages targeting one keyword (~50-page scan cap) | Insiders / free |
| **wordcounter.net / characterCounter.net** | Manual verification of AI-reported word count, keyword density, and character counts (the tool numbers are never trusted) | Free |
| **Image Alt Text Viewer** | Audits every image + alt text + file name on a page in one view | Free |

---

## 5. Quick-Reference: Every Threshold in One Place

| Element | Rule / number |
|---|---|
| Keyword targeting | One keyword per page, always |
| Title tag | 50-60 chars (ideally <55); keyword at the front |
| Meta description | ~120-155 chars; keyword near front; unique per page |
| URL slug | Short, keyword-in, no year, no "near me"; change only if not ranking + no traffic + no backlinks |
| H1 | Exactly one, first heading in DOM, exact keyword, no brand name |
| H2 count | One more than the top-ranking competitor; 5-10 normal |
| Heading order | Never skip a level going down; skipping up is fine |
| Word count | Match top 3 +100-200 (~10%); 750-1,500 baseline; 400-500 for zero-difficulty; ~2,000 ceiling |
| Keyword density | Match competitors "plus one"; your density > competitors = over-optimized |
| Readability | 7th-8th grade; paragraphs 2-3 sentences |
| Images | 1 per 200-300 words; min 4/post; alt text on every image; WebP; keyword in ≤half of alt texts |
| Internal links | 3-5 to other posts + 1 money page per new post; +3 inbound from older posts after publishing; anchor = descriptive |
| Internal link ceiling | 10-20/page (hard max 50-100) |
| External links | 1-2/page, credible, never to a competitor |
| FAQ | 3-4 per page; plain text, never behind accordion; H2 questions |
| Crawl depth | Money pages ≤3 clicks from homepage |
| Audit score | Ignore the composite; 80%+ / 90% is fine |
| Ranking pages | Never edit content/structure of a page ranking #1-#3 (UX/CTA polish only) |
| Money-page fix order | Title → meta → H1, then wait 1-2 weeks |
