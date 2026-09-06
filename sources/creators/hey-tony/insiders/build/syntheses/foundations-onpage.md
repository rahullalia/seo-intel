# Foundations — On-Page, Off-Page & Technical SEO (HeyTony Insiders, level0-understandingSeo)

Synthesis of 34 short curriculum videos. Framework used throughout: SEO = **on-page** (elements you control) + **off-page** (elements you don't) + **technical** (a more nuts-and-bolts subset of on-page). Recurring source example across on-page lessons: the HeyTony (heytony.ca) website and blog; recurring SERP example: a "Hamilton web design" Google search used for title tag / meta description comparisons.

## Why SEO Matters (framing)

- Google searchers have the **highest purchase/learning intent of any marketing channel** — they're telling you directly what they want.
- Costs **time and effort, not money** — no ad budget required to compete.
- Search engines don't charge for the #1 organic spot (unlike ads) — ranking #1 organically "can absolutely change your business," growing traffic progressively rather than overnight.
- SEO makes it easier to dominate a local market or niche.
- Content-driven ranking = **soft-selling** (answering questions, building trust) vs. hard-selling.

---

## Quick-Reference Thresholds & Rules

| Element | Rule / Threshold |
|---|---|
| Title tag | ~60 characters (give or take, varies by device/Google); focus keyword at/near the start |
| Meta description | ~156 characters (give or take); focus keyword near the start; no fixed formula |
| URL | No character limit, but shorter performs better; include focus keyword (except homepage); one unique URL per page |
| Word count | ~2,000 words correlates with #1–4 rankings; homepage should also be 2,000+ words |
| Readability (Yoast-style tool) | Flag if >25% of sentences exceed 20 words (example flagged page: 30.6% vs. the 25% max) |
| Heading tags | Exactly one H1 per page; multiple H2s and H3s allowed; H4–H6 rarely used |
| Images | ~1 image per 200 words minimum; never publish with zero images |
| Keyword density | No fixed rule; worked example = 10 uses / 1,000 words = 1%; some #1 pages run ~10%; flag if it reads like stuffing |
| Internal linking | Every new post should get retro-linked from relevant older posts (and vice versa) |
| External linking | At least 1 outbound link per page to a credible/reputable source |
| Crawl depth | ≤3 clicks from homepage (homepage load doesn't count as a click); 4+ clicks = effectively ignored by Google |
| Sitemap indexing | If new pages aren't indexed within ~1 month, check the sitemap was submitted to Search Console |

---

## PART 1 — ON-PAGE SEO (elements you control)

On-page SEO = all content elements on your own site: title tags, meta descriptions, URLs, content quality, word count, readability, heading tags, anchor text, bullets/lists, images, alt text, video, keyword density, internal links, external links.

### Title Tags
- Tells users (and Google) what the page is about; shown as the blue clickable link text in SERPs, the browser tab text, and the title in social-share link previews.
- "Title tag" and "meta title" are used interchangeably.
- Directly impacts click-through rate — a bad title tag suppresses clicks.
- **Limit: ~60 characters**, give or take, depending on device and what Google is doing that day.
- Include the **focus keyword at (or very near) the beginning**.
- Case study — "Hamilton web design" SERP, top 4 organic results all front-load the keyword: *"Hamilton Web Design, your local web design company"*; *"Top Web designers in Hamilton 2022 reviews"*; *"Massive Web Design Hamilton Web Design & SEO"*; *"Web Design website Development Hamilton."*

### Meta Descriptions
- Gives users more detail about the page than the title tag and should be persuasive enough to earn the click; also impacts CTR.
- **Limit: ~156 characters**, give or take.
- Include the focus keyword near the beginning.
- **No fixed formula** — write differently per page/goal; you may revise these over time.
- Same "Hamilton web design" SERP examples: *"Hamilton's award winning web design and development agency"* (keyword + city up front); *"Top web designers in Hamilton"* listing the top local firms; *"Massive Web Design is an established Hamilton web design firm that specializes in creating unique imagery for web design"* (keyword repeated naturally). One ranking result's strong position was attributed to possible high domain authority rather than meta copy alone — domain authority covered in a later module.

### URLs (Slugs)
- Also called a "slug" or "link" depending on CMS; should reflect the title tag and tell users what the page is about.
- Designed to replace raw IP addresses; provides a memorable, typeable, readable structure — good UX.
- Include the **focus keyword** in the URL (homepage is the exception — it's just the root domain).
- **No character limit, but shorter performs better.** Every page needs a unique URL.
- Bad example (keyword stuffing): `balamedia.ca/hamilton-website-designers-web-design-hamilton` — repeats the keyword needlessly; should have been trimmed to just `hamilton-website-designers`.
- Good example: `sociallyinfused.com/services/website-design` — simple, succinct, hierarchical (services → specific service).

### Content Quality
- "Being useful pays off" — content is the foundational element; you can't optimize what doesn't exist (need words, images, video on the page).
- Well-written, informative content keeps users on the page longer → signals quality to Google.
- Content should answer a question or solve a problem.
- Hard to quantify, but the throughline: **long-form, well-formatted, genuinely useful content ranks higher.**

### Word Count
- Pages with **~2,000 words** typically rank #1–4; fewer words correlates with lower rankings (per the lesson's ranking-position graph).
- Longer content should mean more *complete* information, not padding.
- **Even the homepage should hit 2,000+ words.**
- HeyTony tactic: the homepage doesn't look word-heavy on first scroll (services, a testimonial, FAQs) because content is tucked into **accordions/sliders** ("Our approach to growth marketing" expands into more copy per item) and an **FAQ section** listing each service with an expandable answer. This lifts word count substantially while keeping the visible page scannable — recommended technique if you need to grow homepage word count without a wall of text.

### Readability
- Definition: how easily anyone (down to grade-school/high-school level) can understand the writing — simplifying content **grows your addressable audience**.
- Factors: transition words, word/sentence complexity, paragraph length, sentence length, passive voice, consecutive-sentence patterns, subheading distribution, and jargon.
- Rule of thumb: avoid industry jargon that forces readers to "open a dictionary"; write so a first-time learner can follow and build on the concepts.
- Case study: a HeyTony blog post flagged by an SEO tool for **30.6% of sentences containing more than 20 words**, against a **recommended maximum of 25%** — flagged as run-on sentences needing to be split or tightened.
- **Tool: Yoast** (Y-O-A-S-T) — free WordPress plugin (Shopify support unconfirmed in-lesson) that scores readability and flags these issues; workflow = **write first, then edit against the tool's feedback.**

### Heading Tags (H1–H6)
- Prioritizes/organizes information; breaks content into subtopics and sub-subtopics for both users and search engines.
- Six levels exist (H1 → H6); **H1–H3 are the ones that matter most** in practice; H4–H6 rarely used.
- **Rule: exactly one H1 per page** (the page's main topic, usually near-identical to the title tag), **multiple H2s allowed** (each reinforces the H1), **multiple H3s allowed** (each reinforces the H2 it sits under).
- Full worked example — HeyTony's *"What Is Domain Authority and How Can You Improve It?"* article (~2,000–3,000 words):
  - H1 = the full question/title.
  - H2 (intro section) → H2 *"What is domain authority"* → H2 *"Domain authority versus page authority"* with H3s splitting into a Domain Authority sub-section and a Page Authority sub-section → H2 *"The importance of domain authority"* → H2 *"What is a good domain authority score"* → H2 *"How can I check my domain authority"* → H2 *"Why is domain authority important"* → H2 *"What are some examples of domain authority / is it better to have higher or lower"* → H2 *"How can I improve my domain authority to rank my website"* with H3s under it: *publishing quality content, guest posting, directories, participating in forums* → section on *"DA strategies to avoid"* (buying links, link trading) → closing *"real-world domain authority analysis"* section.
- Payoff: when an H2 directly answers a question, Google can pull that section as a **rich/featured snippet** shown right in search results — "it could help you jump right to number one."

### Anchor Text
- Definition: the word/phrase used to link to another page — describes what that destination page is about, to both users and search engines.
- **Never use non-descriptive anchor text** — banned words: "here," "learn more," "website." Anchor text must always describe the linked destination.
- Applies both on-page (internal linking) and off-page (backlinking).
- Case study — HeyTony homepage services list: "website design," "website conversion optimization," "local SEO" each link to their own respective service page. Footer services list does the same. Blog cross-links use phrases like *"how to create shareable content on Facebook"* and *"how to use Instagram to grow your business"* as the literal anchor into those topic pages.

### Bullets & Lists
- Improve readability/comprehension by breaking paragraphs into digestible chunks; help users scan and locate information fast.
- Case study 1: HeyTony's *"How to Perform an SEO Audit"* article uses bullets instead of consecutive paragraph blocks to avoid a "wall of text."
- Case study 2: HeyTony's **"87 SEO Tools"** article (~10,000 words) opens with a **jump-link index** ("quick index of all the types of SEO tools discovered on this page") — clicking a category (e.g., link-building tools, rank-tracking tools, analytics tools) anchor-scrolls the user straight to that section. Effective pattern for very long pages.
- Guidance: use bullets/lists where they genuinely help; don't force them where they don't.

### Images
- Improve time-on-page, conversion rate, trustworthiness, and readability (breaks up text walls).
- **Rule: ~1 image per 200 words** where feasible; never publish a page with zero images/graphics.
- **Never use stock photos or stock-looking images** — reads as "not a real team/product." Custom graphics, hired photography, or self-shot photos build more credibility.
- **Use next-gen image formats** — same visual quality as JPEG/PNG at roughly **1/10th the file size**, which improves load time (feeds directly into Site Speed / Core Web Vitals).
- Case studies:
  - *"How to Increase Organic Reach on Instagram"* — custom graphics per section (organic reach, Insta Stories, engaging influencers, "setting a SMART goal"); ~5–6 images total; the 200-word rule is broken in places but compensated for by heading-tag breaks (acceptable substitute when an image doesn't make sense for a section).
  - *"How Does the TikTok Algorithm Work"* — custom graphic per major section; images carry alt text that helps the images themselves rank in Google Image search and drive click-throughs / attribution backlinks when others reuse the image.
  - *"What Is Newsjacking and How Does It Affect SEO"* — closes with a shareable **infographic**, also cross-posted to Pinterest and other sites, functioning as a link-building magnet: people who just want the gist can read the infographic, and sites embedding/referencing it link back to the full article.

### Alt Text
- Most-frequently-skipped SEO element. Describes an image for: (1) search engines, (2) screen-reader/visually-impaired users, (3) fallback text if the image fails to load. Also a vehicle for **additional keyword targeting**.
- **Formula: identify the medium (photo / illustration / graphic / infographic) + be descriptive.**
- Worked quality ladder (blueberry pancakes example):
  - "pancakes" — terrible, no real description.
  - "blueberry pancakes" — still thin.
  - "stack of blueberry pancakes in a kitchen" — better, fully descriptive.
  - "illustration of a stack of blueberry pancakes in a kitchen" — best, *if* it's actually an illustration (state the medium accurately).
- Implementation pitfall called out live: missing spaces between words in the alt attribute breaks it/renders it useless — proofread the actual string.
- Business application: a business specializing in a product (e.g., a restaurant's specialty pancakes) should pack relevant descriptive keywords into alt text (ingredients, toppings/sauces) so it ranks in Google Image search and nudges the page itself slightly higher for those terms.

### Video
- Google indexes **one video per page**, even if it's just an **embedded YouTube video** rather than natively hosted — it still surfaces in search results.
- Like images, breaks content into more digestible sections.
- Increases dwell time (time on page) — a positive ranking signal.
- Not mandatory, but valuable for trust/authority-building, especially self-filmed video (talking-head or screen-share) vs. an embedded third-party video — the latter still helps rankings via engagement but doesn't build brand trust the way filming it yourself does.

### Keyword Density
- Definition: (number of times the focus keyword appears) ÷ (total words on the page). Worked example: 10 uses in a 1,000-word page = **1% density**.
- **No fixed/universal target percentage** — some pages rank #1 with density as high as ~10%; judge case by case. Historical reference point: "keyword stuffing" (repeating a keyword mechanically, e.g., 500 times in a 1,000-word page) is why density is monitored at all — Google disqualifies pages doing this from ranking for that term.
- Practical guidance: a page genuinely, thoroughly about a topic will naturally reuse the keyword multiple times through its own subheadings (worked example: a true "blueberry pancakes" page naturally generates phrases like *"best temperature to cook blueberry pancakes at"* or *"when to flip blueberry pancakes"* — 3–5+ natural mentions without trying).
- **Use keyword variations** — reordering, singular/plural ("blueberry stacked pancakes," "pancakes with blueberries," "blueberry pancake" vs. "blueberry pancakes") all count toward density.
- **Tool: Yoast** — flags density as too high with a red warning icon (WordPress; free plugin).

### Internal Linking
- Definition: a link from one page on your site to another page on your site, reinforced by descriptive anchor text (ties directly back to the Anchor Text rules above).
- Helps both users and search engines discover related content and reinforces topical/keyword relevance.
- Often neglected by agencies, SEO teams, and DIY site owners — frequently done wrong (using "click here"/"learn more" instead of descriptive anchors).
- Case studies:
  - Nav menu itself is internal linking: Work → Services → Contact → Blog.
  - Homepage service list ("SEO," "Local SEO," "Facebook Ads," "Instagram Ads," "TikTok Ads") each link to that service's dedicated page.
  - Case-study brand name as anchor — "Neutral Vodka" links to that specific case-study page; "Web Design" links to the portfolio category archive of all web design case studies.
  - Blog cross-linking example: a *"how to find content ideas for your website's blog"* post internally links to *"How to Create Instagram Reels," "Turning Your FAQs into Blog Posts," "User-Generated Content in Your SEO Strategy," "Newsjacking,"* and *"How to Do Keyword Research."*
- **Standing workflow**: every time a new post/page is published, go back through existing older posts and add a link to the new content wherever topically relevant (retroactive, bidirectional interlinking) — called out explicitly as "one of the number one things you do outside of writing the content" itself.
- Effect at scale: creates an interconnected "web" that increases the odds search engines fully crawl/index the site and increases user time-on-site.

### External Linking
- Definition: a link from your page out to a **different domain**, used to cite sources/statistics and build credibility with both users and search engines ("we're not just making this up").
- **Rule: every page should have at least 1 external link.**
- Case study — *"E-Commerce Stats in Canada 2022"*: three separate cited claims, each linked to its source — (1) "In 2020, Canada set a record by becoming the fastest growing e-commerce market in the world"; (2) "over the last five years, online shopping sales have increased by almost 300%"; (3) "45% of e-commerce sales are made up of purchases from non-Canadian websites."
- Secondary pattern: a service page can link out to the *platform's own* documentation to borrow authority — e.g., a Facebook Ads service page linking to Facebook's own ads support/help content.

---

## PART 2 — OFF-PAGE SEO (elements outside your direct control)

Off-page = ranking variables that live off your own site: link building/backlinks, content marketing, local SEO (Google Business Profile + citations), social media, and reviews.

### Backlinking / Link Building
- Definition: a link from *another* website to yours (the inverse of external linking). "Backlinks," "link building," and this concept are used interchangeably.
- Alongside content itself, this is framed as **the most important element of any SEO strategy.**
- **Quality over quantity**: a link from a highly reputable, long-established domain (CNN, New York Times) carries far more weight than volume of low-quality links.
- Backlinks from untrustworthy/spam sources can actively **hurt domain trust/authority.**
- Historical/algorithmic note: Google issued updates specifically to stop **negative SEO** — competitors buying spammy backlinks and pointing them at a rival's site to tank that rival's rankings; Google has since corrected for this attack vector, but acquiring links from spam sources remains bad practice regardless of who buys them.

### Content Marketing
- Definition: producing free content (blog posts, graphics, videos, TikToks, YouTube tutorials/how-tos) without explicitly, directly pitching your product/service — builds brand trust, awareness, and thought leadership.
- Core philosophy: **"give away 99.99% of your knowledge for free."**
- Concrete cadence example: HeyTony publishes **3–5 new blog articles per week.** Cited published titles: *"10 Simple Ways to Improve Your Google Search Rankings," "How Long Before Google Indexes My New Page," "How to Redesign Your Website Without Losing SEO Rankings," "Why Your Blog Post Should Have External Links," "What Is Newsjacking," "Here's a Negative Keyword Google Ad Strategy."*
- Funnel logic: readers who consume enough free content self-qualify and reach out when they're ready to buy / when it's outside their own depth — no hard selling required.
- Side benefits: attracts backlinks and social shares from people referencing your free content.

### Local SEO
- Relevant only to local/brick-and-mortar businesses with a physical location — **skip this section entirely if you're not local.**
- Two core components: **Google Business Profile** (formerly "Google My Business"/GMB) and **citations** (directory listings).
- Directories that matter: Google Maps, Yelp, Apple Maps, Instagram, and other local/industry directories.
- Tactic: keep **business name, phone number, and address identical/consistent** across every directory listing, plus submit a website link and service descriptions to each profile — inconsistency undermines the "legitimate business" signal Google is looking for.

### Social Media
- **Minor, non-vital ranking factor** — not required for ranking, but can act as a **tiebreaker**: with two otherwise-comparable competing pages, more social shares can push one above the other.
- Primary value is indirect: driving referral traffic increases overall time-on-site and traffic volume, both of which are themselves ranking signals.
- Great content naturally gets shared, compounding this effect.

### Reviews
- Trust/credibility signal — "reputation is transparent." Heavy negative reviews suppress new-customer acquisition; strong reviews build trust faster with prospects.
- Ranking impact: businesses with strong reviews get shown higher in **local pack** results; for e-commerce, a product's review volume/rating is itself a ranking factor for that product listing (worked example: a product with ~5,000 five-star reviews gets surfaced above comparable products with fewer/weaker reviews).
- Applies across three contexts: local/service businesses (local pack visibility), general website trust badges/testimonials, and e-commerce product pages.
- Tactic: actively solicit reviews after service/product delivery, and have "a system to monitor" for legitimacy (detailed workflow deferred to a later module).

---

## PART 3 — TECHNICAL SEO (the infrastructure subset of on-page)

Technically a subset of on-page SEO, but nuts-and-bolts/infrastructure-focused rather than content-focused: site speed, responsive design, Core Web Vitals, schema markup, sitemaps, robots.txt, crawl depth, duplicate tags, broken links, orphaned pages.

### Site Speed
- Definition: how quickly a user's browser can load your content.
- Causal chain stated directly: **slow load → higher bounce rate (user hits back, picks a faster competing result) → lower search ranking.** Fast-loading sites dominate rankings.
- Detailed speed *techniques* are deferred to a dedicated how-to module (not covered in this lesson beyond the causal framing above).

### Responsive / Mobile-Friendly Design
- Definition: content must render and function correctly across every device/screen size — phone, tablet, laptop, desktop, oversized displays.
- Search engines actively prioritize mobile-friendly, responsive sites.
- Most modern CMS/builders (WordPress, Shopify, Wix) handle the bulk of responsive behavior automatically; manual tweaks may still be needed.
- Failure mode: unresponsive design → higher bounce rate (mobile users literally can't read/use the content) → lower rankings.
- Named case study: the original **Space Jam** movie website — still live, unmodified since its 1990s launch — cited as the canonical example of a completely unresponsive legacy site when viewed on a phone.

### Core Web Vitals
- Framing: "just think user experience." A Google initiative providing unified quality signals for web UX.
- Named concept: **Cumulative Layout Shift (CLS)** — illustrated via the common experience of visiting an ad-heavy quiz/content site where the page shifts mid-load and the user accidentally taps an ad they never meant to click.
- Rule: a page should render into its final designed structure immediately and hold — nothing should load in afterward and push or reposition existing content.
- Composite "good CWV" bar: fast load, readable fonts/copy, fast image load, and zero layout shift.

### Schema Markup
- Definition: a structured-data file, invisible to end users, that hands search engines explicit metadata about the page/business — hours of operation, address, logo, business/product descriptions, product pricing, review count/average rating, and the page's *type* (service page, blog post, article, product page, etc.).
- Primary payoff: enables **rich snippets** displayed beneath the title in search results.
- Example: searching **"can dogs eat pineapple"** surfaces a rich-snippet answer directly in the SERP, no click-through required.
- Tradeoff/caveat directly stated: Google has started pulling rich snippets from ordinary articles even **without** schema markup present — so schema is no longer strictly required for snippet eligibility. Still recommended: sites with properly structured data get a competitive edge over rivals who skip it.

### Sitemaps
- Definition: a file hosted on the site (not user-facing) listing which pages/files the owner considers important, plus metadata like last-updated date and alternate language/version info.
- **Auto-generated** by all major CMS/builders (WordPress, Wix, Squarespace, Shopify); standalone sitemap-generator tools exist for fully custom builds.
- Must be **manually submitted to Google Search Console** — this is the one non-automatic step, and it's explicitly called "super important."
- Diagnostic threshold: **if new pages aren't indexed within ~1 month of publishing, check whether the sitemap has actually been submitted to Search Console.**

### Robots.txt
- Definition: a crawler-directive file (technically accessible, just not surfaced to normal users) that manages Googlebot's crawl traffic and can keep specific files/pages out of the index — specific images, PDFs, login-gated pages, or orphan pages.
- **Auto-generated** by CMS/site builders as a baseline feature — if your platform doesn't generate one automatically, "you need to switch your website builder."
- Case study: HeyTony's own robots.txt simply allows all pages to be indexed and declares the sitemap's location.

### Crawl Depth
- Definition: the number of clicks required to reach any given page starting from the homepage (**the homepage load itself doesn't count as a click**).
- **Threshold: ≤3 clicks** — sites with shallow crawl depth (every page reachable in 3 or fewer clicks) rank higher.
- **4+ clicks deep and Google effectively stops caring**: "if they don't care to feature that content, then why should we feature that content."
- Fix: strengthen site architecture / internal-linking strategy, or remove/prune content that isn't worth surfacing — "don't bury your content or no one will find it, including Google."

### Duplicate Tags
- Definition: multiple pages sharing the same title tag, meta description, and/or H1 — usually a sign of overlapping/duplicate topical coverage.
- Consequence: Google can't determine which page is canonical and may **suppress all of them from ranking** — explicitly framed as "cannibalizing your own search rankings" and as a form of self-plagiarism (which Google penalizes, even though less severely than cross-site plagiarism).
- Two fixes offered: (1) **merge the duplicate pages into one longer, comprehensive piece** and signal to Google that the old URL no longer exists / now resolves to the merged page, or (2) manually rewrite each page's tags and content to be unique.

### Broken Links
- Definition: a link pointing to a page that returns a 404 / no longer exists.
- Consequence: signals to Google (and to users who hit the dead link) that the site isn't diligently maintained — "if you're not looking after your broken links, what else are you not looking after."
- **Fix immediately** on discovery. If linking out to a study/resource that has vanished, either find a replacement source, or — notably — **write your own new blog post covering that gap and swap the dead external link for an internal link to your own content**, turning a broken-link audit into a content and internal-linking opportunity simultaneously.

### Orphaned Pages
- Definition: a published page with **zero inbound internal links** from any other page on the site — reachable only by someone who already has the direct URL.
- Consequence: invisible to both users and Google — "essentially useless," and it signals a lack of site diligence.
- Fix: apply internal-linking discipline so every page is reachable by clicking through from at least one other page — as simple as adding a single relevant link to it.
