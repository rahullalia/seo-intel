# Playbook digest (hey-tony-playbook.md)

Source: `/Users/rahullalia/Developer/my-business/seo-intel/sources/creators/hey-tony/insiders/hey-tony-playbook.md` (2137 lines, six Parts). Every bullet below is one rule, number, threshold, step, prompt, or example taken from the playbook, with the Part and section in brackets. Part IV has named sections rather than numbered ones, so its citations name the section (e.g. [Part IV Web Design]). Part VI citations use the sub-section number, whose first digit is the PART (e.g. [Part VI 3.2] = PART 3 Ecommerce, 3.2). Quotes in quotation marks are verbatim. Prompts are copied in full. Where the playbook has nothing on a page type, the heading says so and lists only the adjacent rules that apply.

## 1. Homepage (including homepage-vs-money-page targeting by business model)

Targeting by business model
- Local / service business: target `[service] + [city]` on the homepage ("dentist in Hamilton," "Residential Roofing in Cincinnati"). [Part II 2.4; Part III 3.2]
- The single service that makes the most revenue becomes the homepage's target keyword; every other service gets its own dedicated page. [Part III 3.2; Part IV Governing Rules]
- Homepage = your true home-base / flagship market on the single service that makes the most revenue. [Part VI 2.2]
- Ecommerce / content / national sites: do NOT rank the homepage for a keyword. Ranking happens on collections, products, and blog posts; the homepage just orients a visitor who landed from an entry page. Make it a branded page: H1 = brand name, title tag = brand + what you sell. [Part II 2.4]
- Ecommerce: "Stop trying to rank the ecommerce homepage for one keyword." Give each featured product a clean homepage section with descriptive text; push actual ranking onto collection and product pages. "The homepage just needs to make a visitor understand what the site is once they land from an entry page." [Part III 3.2; Part VI 3.1]
- National / virtual with no physical base: optimize the homepage for the single largest nearby metro, then spin out location pages for smaller markets. [Part II 2.4; Part III 3.2]
- The homepage counts as a money page if there is no dedicated page. [Part III 3.1]
- If your homepage naturally outranks your intended money page for the target term, stop fighting it: treat the homepage AS the money page (add the keyword/topic there) and point future blog links at the homepage. Jessa's case: her homepage ranked #2 for "online intimacy course for couples" while the dedicated course page ranked nowhere; the fix was to promote the course page to homepage (WP Settings -> Reading) and monitor, or accept the homepage as the money page. [Part III 3.2]
- Swapping a better-ranking sub-page in as the new homepage is "a little bit risky": do it if warranted, but the mitigation is monitor-and-revert (watch rankings for days/weeks, revert if they drop), never "avoid testing." [Part I 3]
- A blog post's target keyword should never be your homepage's primary keyword (self-cannibalization). Use secondary/variant keywords in blog content. [Part II 2.4; Part III 2.13]
- The Hey Tony Money Page Tool reports which of your own pages actually ranks #1 for a keyword, surfacing when your homepage is stealing your service page's term. [Part II 3.3]
- About, contact, and blog category/taxonomy pages behave like the homepage: not keyword-targeted, not expected to independently rank. [Part III 3.2]
- Too small/new to rank at city level: target state-level keywords first, then build pages for the top 10-20 highest-population cities. [Part VI 2.2]

Homepage tags
- Title tag structure: homepage = brand name + focus keyword. Every other page = focus keyword first, brand name at the end (or dropped). [Part III 2.1; Part IV Title Tags]
- URL: the homepage is the bare root domain, already correct; do not "optimize" it further. [Part III 2.3]
- H1: brand name in the H1 is more acceptable only on the homepage of a brand-new business establishing recognition; otherwise the H1 is the exact target keyword with no brand name. [Part III 2.4; Part IV Heading Structure]
- Ecommerce homepage H1 = brand name. [Part II 2.4]
- Open Graph: OG Title mirrors the title tag; OG Image = featured image (1200 x 628) on any page you would want shared. [Part III 4.6; Part IV Title Tags]

Homepage layout (the canonical wireframe)
- Copy first, then layout: write all page copy before opening a design tool; the message dictates the section structure. Wireframe/mock up first (Figma, Canva, pencil, anything) to surface bad ideas early and lock image sizes; optional, not mandatory. Reuse, do not rebuild: duplicate a working section, flip which side the image/text sits on, swap the background color. [Part IV Web Design]
- Canonical homepage wireframe (default service-business skeleton): Hero (H1 = focus keyword in plain language + subhead + one CTA, all visible with zero scrolling, plus a trust signal) -> Trust row (~3 of: star rating, years, happy clients, licensed/insured, association logos) -> About/intro (with its own CTA and audience-identifier icon boxes) -> Services overview (each linking to its own page) -> Testimonials -> "How it works" process steps -> FAQ -> Final CTA. Product sites reuse the same wireframe with product categories. [Part IV Web Design]
- Most important messages near the top: "the longer it is, the less likely people reach the bottom." [Part III 3.3; Part IV Web Design]
- One section = one H2 = one topic; alternate background tints section-to-section so each reads as distinct ("like a slide deck, one idea per slide"). [Part III 3.3; Part IV Web Design]
- Hero proportions: the header/contact block should occupy roughly 1/6 of the page, not half. Shrink oversized logos ("what the fuck is your logo doing so big", one ate a third of the screen). Do not show the logo twice (image + text) in the header. [Part IV Web Design]
- Never use an auto-rotating image slider/carousel or an autoplaying hero video as the hero. Replace with one static hero image (ideally real people/crew) plus persistent, always-visible descriptive text. A carousel that froze on hover hid a page's own H1 from most visitors; every load still fetches every slide's image. "I fucking hate carousels. People don't stick around for it." Avoid the WordPress Revolution Slider (a speed drag). [Part III 3.4; Part IV Conversion elements]
- Ecommerce: the rotating promo hero should NOT carry the H1; put a fixed keyword-targeted H1 + short paragraph directly below it so the hero can change while the H1 stays put. [Part IV Conversion elements]
- Hero trust-signal build: 5 gold stars matching Google's color + "Rated 5 stars on Google" hyperlinked to the real Google review link, consolidated into one prominent placement, not repeated. [Part IV Conversion elements]
- Weigh a hero autoplay video's appeal against its page-speed and mobile cost: "is that video appealing to you, or is it appealing to a person looking to hire you?" [Part III 2.9]
- Homepage modules (services bar, "recent posts", category links) make pages 1 click deep (homepage load = 0 clicks; a page linked from the nav or a homepage module = 1 click). [Part III 2.11; Part IV Crawl Depth]
- Link new local pages directly from the homepage ("areas we serve") to index faster; footer-only links index slower. [Part VI 2.2]
- On the homepage and money pages, external-link to your own legitimacy profiles (Chamber of Commerce, Trustpilot, Glassdoor) rather than an unrelated site. [Part III 2.12]
- Word count: the old Level-0 curriculum said "~2,000 words correlates with #1-4" and "even the homepage should hit 2,000+"; the live calls supersede this, the competitor-relative rule wins. A homepage measured at 10,000 words (2,000 inside heading tags alone) is over-optimized. [Part II 1.7; Part III 2.5]
- Local-business schema for a multi-city service area: main schema (matching the GBP) on the homepage listing every service-area city. [Part IV Schema]
- On a brand-new site with nothing else to link to, a new post's only links can be the money page + homepage. [Part IV Internal Linking]
- An externally hosted landing page (Netlify) can convert but likely will not rank; still link back to your homepage from it. [Part IV Page-Builder]
- Mobile hero content order: Headline -> Copy -> CTA -> Photo, stacked strictly top to bottom; never a photo beside text on mobile; do not force a full desktop hero photo into a mobile background (place it below the text). [Part IV Mobile]
- Keep NAP (name/address/phone) present and crawlable in the site footer, linking to the GBP via the CID link: Google "looks for that to determine if it's a local business." [Part V 4.4]

## 2. Service pages (parent/overview and child pages) and money pages in general (structure, CTAs, audit thresholds, rewrite prompts)

Definition and scope
- "A money page is any page a visitor lands on when they are ready to buy or hire." Product pages, service pages, collection pages, and location pages are all money pages, and they all get the same discipline. [Part III 3.1]
- Blog posts, contact pages, and booking/appointment pages are NOT money pages ("those pages don't rank"); a third-party booking tool is explicitly not your money page even though your money page may link out to one. "The money page is the page that sends a visitor TO the intake form; the form itself is not the money page." [Part III 3.1]
- If stuck, ask an LLM directly: "I am a realtor, what would be my money page?" [Part III 3.1; Part VI 1.7]
- Examples: dentist -> dental implants / Invisalign; realtor -> "homes for sale in Scottsdale"; plumber -> 24-hour emergency page; hot sauce co. -> "buy ghost pepper hot sauce" / a collection; magician -> one page per event type; ecommerce -> collection or product page. A single business can and should run multiple money pages (one per service/offer), each pointing to the same lead form. [Part III 3.1]
- The page-vs-post dividing line: "We offer this service in this town" = a dedicated page. "X vs. Y" / comparison / informational / local-color content = a blog post. A brand-new business location gets a page, not a post. Static/evergreen info meant to rank for a money keyword = page; a specific one-off question = post. [Part VI 2.1]
- The test: if content ends with a "conclusion," is purely informational, or answers a question, it is a blog post regardless of what page type it was built as. A money page assumes the visitor is already past education and just needs to know you offer the solution and how to book. Rank Week phrasing: if someone would Google the topic for information, write a blog post; if they'd Google it to hire someone, write a service page. Same topic, different content, never blended. [Part II 2.3]
- "You can't rank for a keyword if you don't have a page about that keyword." Put transactional terms on dedicated pages, not blog posts. [Part II 2.3]
- Before writing or optimizing any page, Google the exact target phrase and look at the SERP; build the matching format. "best video production company in NY" is dominated by list/directory sites (Clutch); a single-company "we are the best" page fights the wrong intent. If top results are all platform types (Vimeo-style, marketplaces) and you're a local service business, deprioritize even at 0 difficulty. [Part II 2.2]
- Money Page Doctor flags "blog post detected, competitors ranking are dedicated service pages, consider building one." [Part III 4.4]
- Plenty-of-leads-but-wrong-fit (a surgeon getting calls for procedures they don't do): stop chasing more high-traffic keywords; narrow/optimize specific service pages describing exactly what you do and don't do. [Part II 2.6]
- Cross-language: only money/service pages need the customer's real language; run keyword research natively in that language, never translate. [Part II 1.5]
- Revenue is capped by fulfillment capacity, not lead volume; past that point conversion-rate improvement and pricing are the levers, not more traffic. [Part I 11; Part VI 5.1]

Architecture: parent/overview and child pages
- Service-page IA (two tiers): an overview/parent page that summarizes and links to each service (not pushed for ranking) + individual child service pages, one per service, where you go hard on SEO. Gives clean parent-to-child URL nesting. [Part III 3.3; Part IV Web Design]
- Good URL example: `sociallyinfused.com/services/website-design` (simple, hierarchical, parent -> child). Keep the slug short even when the H1 is long: H1 "Bookkeeping services in St. Petersburg, Florida for small businesses", URL `/services/bookkeeping`. [Part III 2.3]
- Long service lists: keep core services prominent, push the long tail into a mega menu/dropdown, each item linking to its own page. [Part IV Web Design]
- Collapse per-condition/per-service nav links into one "Services" hub linking to sub-pages. [Part IV Web Design]
- One keyword per page, always, no exceptions. A phrase can be 3-4 words, one full question, or one tight cluster of variants, but one target. Never combine multiple distinct services, cities, or topics onto one page. [Part III 1.1]
- Word-order and pluralization variants count as identical: "Chicago luxury newborn photographer" / "Chicago photographer newborn" / "Chicago newborn photography" is ONE topic, not three. [Part III 1.1]
- Every page you want ranked must be <=3 clicks from the homepage; 4+ clicks is the danger zone: "the harder it is for a human to find your page, the less likely Google will care about it." Ensure the money page is reachable from nav, not buried. [Part III 2.11; Part IV Crawl Depth]
- Fundamentals before tactics: fix a broken or thin page before adding location pages, channels, or new tools. "You can't optimize what doesn't exist." [Part III 1.5]

Structure: the canonical service-business page skeleton [Part III 3.3]
- Copy first, then layout; the message dictates section structure. One section = one H2 = one topic, alternating background tints so each reads distinct. Most important messages near the top, because "the longer it is, the less likely people reach the bottom."
- 1. Hero: H1 (focus keyword + city for a local page, descriptive/plain language) + supporting subhead + one CTA button, all visible with zero scrolling. A trust signal (stars/stat/logos) in or right below the hero.
- 2. Trust row: pick ~3 of years of experience, # of happy clients, 5-star rating, licensed/insured, awards, association logos.
- 3. About / intro: what you do, how, who you serve; an audience-identifier layout (icon boxes per persona) so visitors self-identify.
- 4. Services/products overview: brief intro to each, each linking to its own dedicated page.
- 5. Testimonials: pasted real reviews or a Google reviews widget.
- 6. "How it works" / process: plain numbered steps of what happens after they book (defuses first-time-buyer anxiety).
- 7. FAQ tied to that page's focus keyword.
- 8. Final CTA at the very bottom of every page (a visitor who scrolls all the way down must still have a next action).
- Build the body content with lists, tables, and explicit numbered steps. [Part III 3.3]
- H1 in natural, readable language (not "gobbledygook"); rewrite marketing-speak to match how people search: "romantic storytelling wedding photography in Toronto" became "Timeless wedding photography in Toronto." [Part IV Heading Structure]
- Keyword-first title/H1/meta: "Sell your house fast, Delaware, Ohio," not "Looking to sell your Delaware home quickly." Match the abbreviation people actually type ("St. Lucie," not "Saint Lucie"). [Part III 3.5]
- Title tag local reorder example: "Movers in Washington D.C. | Free Quotes | Your Moving Men", keyword/city front, brand last. [Part IV Title Tags]
- Convert FAQ and service content into always-visible H2 + plain paragraph so crawlers read it without triggering a toggle. [Part IV Conversion elements]
- H2s must directly support the H1's specific topic, not generic value-prop or marketing lines; demote flowery marketing sentences to plain paragraph text. [Part III 2.4]
- Cut vague, generic brand copy that does nothing. Matt's test: if an unrelated business in a different niche could reuse the exact line verbatim ("every woman is uniquely beautiful," "and more"), it is too generic to keep. [Part III 2.5]
- Placement checklist, keyword should appear in: product/page name (= H1), title tag, meta description, the first 100 words of copy, naturally through the body, at least one H2, an FAQ, image alt text, and the image file name. As close to the front as possible in title, meta, and H1. [Part III 2.6]
- Low-difficulty and local keywords often need only 2-3 mentions, not 10-12 (one case ranked top-3 for "mechanic" on 3 mentions vs. 0 for all three competitors). [Part III 2.6]
- Word count for a money page: match the top 3 or add ~100-200 words; Matt's own "SEO in Hamilton" service page hit #1 after ~1 year on 600-800 words, purely from internal links; his website-design page held #1 for ~2 years on 600-800 words, then got outranked once competitors ran 2,300-2,500 words on the same term. [Part I 3; Part III 1.2]
- Low-word-count audit flag: the tool's 100-word minimum is outdated; real floor 500+, agency target 1,000-1,500; measure body only. [Part III 4.6]
- Matt's own SEO page ranks #1 in Hamilton with "Hamilton" appearing nowhere in the URL, H1, or H2: a hard local keyword does not require URL keyword-stuffing. [Part III 2.3]
- List pricing/cost ranges on your own site even as a premium provider ("if you don't have any prices, you're getting left out entirely"); a luxury provider whose buyer decides through an in-person/call experience can validly hide prices. [Part VI 5.1]

CTAs and conversion elements [Part III 3.4; Part IV Conversion elements]
- One primary CTA per page: solid, bold, single high-contrast color. Any secondary CTA (call vs. form) must visually recede (outline/neutral). "If people have too many choices, they sometimes just choose not to make any choice." Repeated live fix: 5 competing CTAs (Book Now / Call Now / Email Now / WhatsApp Now / Inquire Now) trimmed to one.
- Do not stop at one CTA top and one bottom: add 2-3 more spaced through the body so a reader convinced mid-page can act immediately. Part IV version: a CTA in the hero, in every section, and at the very bottom of every page.
- CTA copy names the specific action. Never a bare "Learn more," "Contact Us," or "Book Today." Use "Book a massage appointment," "Start your logo design," "Start your corporate video today." Upgrade keyword-bearing versions where natural: "Shop Now" -> "Shop Organic Dog Treats."
- Diagnostic: traffic fine but form fills low? First lever is CTA button color/contrast, not copy. [Part IV Conversion elements]
- Phone numbers and emails must be tap-to-call / clickable everywhere, especially mobile; anchor a labeled clickable number at the bottom of the screen for a mobile-heavy audience (bottom beats top for thumb reach). An icon-only floating button with no visible clickable number tanked call conversions. [Part III 3.4; Part IV Mobile]
- Naming: call the pricing page "Pricing," not a euphemism like "Investment" (people search "[service] pricing"). Avoid cursive/script for anything read quickly.
- Reviews belong on every money page, not just a reviews page. Hand-paste 2-3 real reviews as plain text (Google cannot read text in a screenshot image), rotating which reviews appear on which page so the same text is not repeated everywhere. Location-specific testimonials only on the matching location page. Never use a review-carousel plugin (found adding ~1,000 words of markup and hurting load; users scroll past carousels).
- A live Google-reviews plugin can slow the page and sends NO extra trust signal to Google beyond the visible text; pasted review text still contributes word count/SEO. [Part IV Conversion elements]
- Quote/inquiry forms: keep one dedicated "Get a Quote" page, but also add a small inline quote form (name, phone, email, short message) on each product/service page (more on-page conversion signal, mirrors competitors).
- Anchor-link CTA technique (Elementor/Divi/Showit/Squarespace): give a section a CSS ID and point a button at `#contact` to scroll instead of loading a new page. [Part IV Web Design]
- Real photos of the actual team build more trust than stock or AI; screenshots read as more authentic than over-polished imagery. [Part IV Conversion elements]
- UX/CTA polish (button color, adding a contact link, layout reflow) is the one carve-out allowed on a page that is already ranking. [Part III 1.2]

Linking rules on money pages
- Direction rule: blog posts link TO money pages; money pages link OUT to blog and external sources but do not link out to blog content "as a feature." Money pages reference at most 2-3 essential resource pages and always include a convert CTA. [Part III 2.11; Part IV Internal Linking]
- A blog post references the exact money-page phrase at most once, typically near the bottom as a link back, never repeated throughout. [Part II 3.3; Part IV Internal Linking]
- Cap blog links from any one location/service page at 2-3; do not repeat the same blog link across every location page. A pricing money page can link to a relevant blog post and vice versa. [Part IV Internal Linking]
- Vary anchor text across links pointing at the same money page ("our SEO services," "done-for-you SEO services," "professional SEO services"); repeating the identical anchor reads as manipulation. [Part III 2.11]
- External links on money pages: point to your own legitimacy profiles (Chamber of Commerce, Trustpilot, Glassdoor); never link out to a page targeting the same keyword you're trying to rank for. Matt's own core SEO service page has zero external links and still ranks; his web-design page does link out; check what competitors do on their equivalent money pages. [Part III 2.12]
- Prompt for inbound links: "I'm looking for 3 incoming internal linking opportunities to this service/product page: [LINK]. Find me 3 relevant opportunities from my sitemap pasted below. [PASTE SITEMAP]" [Part III 2.11; Part VI 1.7]
- Reuse the GBP CID link inside service pages wherever it fits; make the on-site business address a clickable CID link. [Part V 4.3]
- GBP post formula points each target keyword at the specific service page you want it to rank. [Part V 4.2]
- Backlinks land more naturally on blog posts than money pages; write the post, then point paid links at it rather than the sales page. One relevant link pointed at the exact page can beat ~700 sitewide backlinks. [Part V 1.1]
- Chamber of Commerce member page: ask for 2-3 links to specific service pages, not one generic "visit website." [Part V 1.3]

Auditing a money page (what to read, thresholds)
- Ignore the audit tool's overall composite score entirely and read only three things: (a) how many times the target keyword is used vs. competitors, (b) total word count vs. competitors, (c) keyword density vs. competitors. "Ignore everything else. It's there. It's like nothing. Zero." [Part III 4.1]
- The 5-step audit (pageaudit.com), for your page + top 3 competitors into one shared sheet: 1. enter URL + one focus keyword (never "near me," never a generic un-localized term). 2. pageaudit.com -> Analyze; ignore the overall %. 3. Content tab: word count, keyword occurrences, density. 4. Metadata tab: title tag + meta description. 5. "PA" Chrome extension as fallback when a page returns all "NA" (bot-blocked): title, meta, H1/H2/H3 ("Copy All Headings"), word count, density; wait ~30 seconds or scroll to bottom and back if it doesn't populate. 6. pagespeed.web.dev on the money-page URL (mobile + desktop). 7. Repeat for the top 3 organic competitors: Google the exact keyword incognito, skip sponsored/ads, skip Reddit/Yelp/IG, skip directories/aggregators, take the next 3 genuine ranking business sites. 8. Do NOT rewrite yet. [Part III 4.2; Part II PART 5 prep]
- Word count differs slightly between pageaudit.com and its extension; anything within ~100-200 words is close enough. [Part III 4.2]
- Competitor-benchmark method: word count = match the top 3 or add ~100-200 words (trim if you overshoot); keyword frequency = split the phrase into components (service term and location term), count each separately across the top 3, match or "plus one"; heading count = one more H2 than the top competitor. [Part III 4.3]
- Verify competitor data by eye, not just by tool: one reported "1300 words" was manually 174; another set of 2,200-3,400 could not be located on the page; a review-carousel plugin can inflate a real page to 3,000-4,000 phantom words. [Part III 4.3]
- Benchmark the lowest-ranked of the top 3, not the highest: if #3 ranks with 500 words, aim ~600, not 3,000 because #1 has 3,000. [Part III 4.4; Part VI 4.4]
- Full "why doesn't it rank" comparison once on-page checks out: who ranks #1-3, their backlink/referring-domain count, how often and where they use the keyword, whether their content is simply better, whether they use a top summary or key-takeaways block, how many internal links point at their page. [Part III 4.3]
- Diagnostic default: "if you're not ranking, you're either doing too little or too much." [Part III 4.3]
- Money Page Doctor (Insiders, capped ~20 audits/month): paste a URL, in ~10 seconds it infers the keyword, identifies competitors, flags gaps ("keyword mismatch: competitors appear to target [X] instead," "content is thin," "density too low/high") or shows a "you're already ranking #1" banner. Always check where you actually rank before acting; if already #2, do not touch the page just because it flags a gap vs. #1. [Part III 4.4; Part VI 1.4]
- Competitor gap analysis prompt + pasted audit spreadsheet: output across up to 8 dimensions (title tag, meta description, H1, H2/H3 structure, word count, keyword density, page speed, trust signals), each gap with an exact fix and a priority flag (red = do first / yellow = this week / green = nice to have) plus a 3-bullet Quick Wins summary. Challenge vague or self-serving AI claims ("then why aren't I ranking #1?"). "ChatGPT will bullshit you." [Part III 4.4]
- Never run a site-wide audit against a site still mid-construction. Expect a 12+ hour lag before an audit tool re-crawls a fix. [Part III 4.1]
- Audit flags that are fine to ignore on money-adjacent pages: orphan/low word count on thank-you, ad landing, contact, category/archive, and funnel pages. [Part III 4.1]

Rewriting a money page (the exact prompts)
- SEO tags update prompt (verbatim): "Here are my current tags and my focus keyword. Update them so the keyword appears naturally, is front-loaded where possible, and matches the style and brand of my business. Also make sure each one is better than my two competitors': [PASTE YOUR AUDIT] Competitor 1 (Same Order As Mine) [PASTE COMPETITOR AUDIT] Competitor 2 (Same Order As Mine) [PASTE COMPETITOR AUDIT]" [Part III 4.4; Part VI 1.7]
- Money page rewrite prompt (verbatim): "Here is the content from my product/service page: [PASTE YOUR CONTENT] Here are the top 2 competitor pages that rank for my keyword: Competitor 1: [paste content] Competitor 2: [paste content] My focus keyword: [keyword] Rewrite my page so that: - It is clearer, more helpful, and more persuasive - Word count is between: [comp low] - [comp high] words - Keyword density is similar to the competitors - Includes the keyword in natural positions - Adds missing topics my competitors include - Improves structure, readability, and expertise - Keeps my brand voice - Uses headings where appropriate - Does NOT keyword-stuff Produce the final optimized version I should publish." [Part III 4.4; Part VI 1.7]
- Two-prompt Rank Week workflow: Prompt 1 (metadata): paste your title tag, meta description, H1, H2s, keyword density, then each competitor's column in the same row order; it returns updated title, meta, H1, H2s; copy to a separate doc; confirm the keyword is present and front-loaded; swap in a better-testing variant if data showed Google prefers it. Prompt 2 (full rewrite): paste your entire page; for each competitor try pasting just the URL first (ChatGPT can sometimes read the live page), fall back to full content; set the word-count target from competitor data (competitors at 2,500 and 2,300 -> target ~2,200); answer any clarifying question first. The exact prompt text lives on heytony.ca/prompts during Rank Week. [Part II PART 5]
- Never trust the AI's self-reported word/keyword count: it targeted 2,200 words and delivered ~1,700; targeted a 20-45 keyword band and delivered 13. Paste into wordcounter.net and land in the same band as competitors, not above or below. [Part II PART 5; Part III 4.4]
- "Whatever the #1 competitor does, Google likes; mirror it, then slightly outdo it" ("level plus one"). Over-optimizing past the competitor who outranks you can suppress rankings. [Part II PART 5]
- Rewrite discipline: copy output to a separate blank doc, confirm the keyword is present and front-loaded, swap in the better-testing semantic variant if the data showed one, strip labels/bold, and rewrite any H2 that does not sound like a real person wrote it. [Part III 4.4]
- Section refinement prompts (same thread): "can you rewrite this section to be more funny and personable"; "you forgot these heading two tags, write a couple paragraphs each and expand on the ideas"; "ask me five questions to write a better unique piece using my expertise" (folds the interview method into the rewrite; stronger than treating the output as final). [Part II PART 5; Part III 4.4; Part VI 1.7]
- Re-run the page-audit tool on the new draft before publishing. [Part II PART 5; Part III 4.4]
- Money-page fix priority order: (1) title tag, (2) meta description, (3) H1, keyword front-loaded in all three (~5-10 minutes), then wait 1-2 weeks before touching on-page content further. [Part I 9; Part II PART 5; Part III 4.4]
- Cross-check every AI suggestion against the real SERP; don't trust its guess at who your competitors are; verify by Googling the keyword. [Part II PART 5]
- 30-day plan: each week publish 1 blog post linking to 2-3 other posts + 1 money page; fix 5 red audit issues; fix that week's money page's title tag + meta description (one prompt does both in ~5 minutes) then H1; add 3 internal links to that week's money page from other pages. Total: 4 money pages, 4 blog posts, ~20 issues fixed. [Part I 9; Part III 4.5]
- Agency standard: 2 deliverables/week per client (one new blog post + one existing money-page rewrite) + 4 backlinks/month. [Part I 11; Part VI 5.1]

The freeze: never touch a ranking money page
- "Don't edit any pages that are ranking, for the love of God." Applies to pages ranking #1-#3, or ranking for anything at all, even a keyword other than the one intended, and even when the page violates every other rule (duplicate H1s, keyword stuffed 122 times, hidden overlay text, thin content, zero backlinks). "I don't give a shit if you have 31 heading one tags when you should only have one. If you have 31 of them and you're ranking number one, I'm not touching that page." [Part I 3; Part III 1.2; Part VI 4.1]
- Evidence: Ellen Mitchell ranks #1 for a probate keyword using "probate" 122 times, two duplicate H1s, and hidden overlay text behind the nav; Brett ranks #2 for "Miami probate Realtor" on a thin page with zero backlinks. Both left alone. [Part III 1.2]
- Redesign scope is conditioned on ranking status: strong existing rankings -> preserve verbiage, keywords, and URLs, restructure visually only; weak or no rankings -> free to rewrite from scratch. [Part III 3.6]
- If #1 but converting at zero: tiny incremental edits only (one sentence, one button, a CTA higher on the page), never a full rewrite. Wait for the rank to actually drop before touching anything larger. [Part I 3; Part III 1.2]
- If ranking but flat-traffic: don't rewrite; keep publishing easier-keyword blog posts and internally link them to it. [Part VI 4.1]
- "Set and forget" has an expiration date: a page holding #1 for years on little content can lose it once competitors escalate; that drop (not before) is the trigger to redo the competitive audit. [Part I 3; Part III 1.2]
- Guardrail: if a page already ranks for a keyword, never strip that exact keyword out of the title while "improving" it. [Part III 2.1]
- If a blog post and a service page are both ranking for the same keyword and it's working, leave it alone. [Part II 3.3; Part III 2.13]

## 3. Location / city / service-area pages (architecture, uniqueness rules)

Targeting and architecture
- "One page = one keyword = one service = one location." Never build a page for the same city targeting two services ("you're not even getting a slice"). Never combine multiple cities in one post; cycle city by city. [Part III 3.5; Part VI 2.1]
- Adding a location makes it a whole new keyword. "We buy junk cars, Dallas" and "...Houston" never cannibalize no matter how similar the template, provided the location-specific body copy is genuinely substantive. Live proof: "we buy junk cars, Dallas" at volume 210 beat both the "...Dallas, Texas" and the ChatGPT-suggested root "junk car buyer" variants. [Part II 3.1; Part VI 2.1]
- Home-base exception: your flagship market can carry a separate page per service ("Chicago Newborn Photographer" AND "Chicago Family Photographer"). Every satellite location gets only ONE service page (whichever service is easiest to rank there); mention other services in passing. [Part III 3.5; Part VI 2.2]
- Prioritize smaller towns/suburbs over the big nearby city: almost nobody targets them, and searchers type their specific town, not a regional abbreviation. A location page usually cannot outrank a genuine local competitor's homepage (their de-facto money page, most-backlinked page) without dedicated backlinks, so retarget adjacent smaller markets instead of fighting head-on. A Toronto-area photographer was told to drop "GTA wedding photography" entirely for "Toronto wedding photographer," then build individual pages for Hamilton, Stouffville, Mississauga, Oakville, King City. [Part III 3.5; Part VI 2.2]
- City-size sizing rule: a ~500,000-population city (Hamilton, ~15,000 small businesses) justifies targeting the whole city; a 3-4 million metro (Toronto) is too big, go neighborhood-level ("junk removal Leslieville," "landscape lighting Montreal"). People won't cross a huge city for a local service. [Part III 3.5; Part VI 2.2]
- Too small/new to rank at city level: target state-level keywords first, then build pages for the top 10-20 highest-population cities. A brief mention + link at the bottom of an otherwise-generic post ("if you're looking for website design in West Virginia ->") is enough; a full hub/pillar structure isn't required. [Part VI 2.2]
- Service-area hierarchy, not a flat link dump: top page lists sub-regions/counties -> each links to a county page listing its towns -> each town gets its own page (which can list neighborhoods). One case replaced a flat list with ~10-20 pages. [Part VI 2.2]
- Do not build every location x service combination "just in case" (one case would have been 66 pages: 25 cities x 6 event types; only ~5 of 66 had real volume; a ~200-page HVAC service x city matrix was flagged as overreach). Build one page per location with sections per service, and run keyword research to confirm a specific combo genuinely gets searched before building a dedicated combo page. "Pigs get fat and hogs get slaughtered." [Part III 3.5; Part VI 2.2]
- Zero-volume location keywords are still worth a page if difficulty is near-zero (tools under-report hyper-local terms; ~15% of searches are brand-new each day). [Part III 3.5]
- National KD can badly mislead local intent (a term can show KD 88 nationally with no single city accounting for that volume). [Part VI 1.2]
- Nav: a "Locations" hub in header/footer -> hub lists every location -> each links to its page. Link new local pages directly from the homepage ("areas we serve") to index faster; footer-only links index slower. Nest location pages under a standalone Locations hub, never inside one service page. [Part VI 2.2]
- Location pages can cross-link to neighboring location pages. Cap blog links from any one location/service page at 2-3; don't repeat the same blog link across every location page. [Part IV Internal Linking]
- Build service-area pages on the site, each linked to the matching GBP service category. [Part V 4.4]
- Agency cadence without backlink work: 1 blog post/week + 2 city/location pages/month (a 3-month engagement that ended with the client "at capacity"; delivered via a pre-mapped plan of 12 blog topics + 6 city pages). [Part I 11; Part VI 5.1]
- Rollout: ~1-2 unique pages/week. A 12-location build finishes in ~3 months without burnout; even a huge client is paced at ~2/week ("sniper rifle" over "shotgun"). Stop once a subset is already ranking/converting; you don't have to finish the whole list. [Part VI 2.2]
- Expect 3-6 months (up to a year) for a new location page to move. [Part VI 2.2; Part VI 5.2]
- A Super-Bowl-driven location page starts ~6 months ahead of the demand spike. [Part VI 3.4]

Uniqueness rules (the real cannibalization risk)
- Genuinely unique content per location, not a template with the city swapped. Reference real local landmarks, venues, neighborhoods, delivery specifics, seasonal color; a florist names funeral homes/hospitals/high schools; for non-delivery/remote businesses anchor in local hooks (nearest hospitals, grocery stores carrying your product, local gyms/trails). "You need 100 original, my friend." Copy-paste-with-city-swapped at scale risks demotion. Multiplying pages is not the risk; duplicate/templated copy across them is. [Part III 3.5; Part IV Canonicals; Part VI 2.2]
- Low-stakes near-duplicates (an escape-room booking page for Anaheim vs. Connecticut) can sometimes get away with differentiating only the title tag + meta description ("Booking - Anaheim"); a page meant to independently rank for its own local keyword needs real unique body copy. [Part IV Canonicals; Part VI 3.3]
- Never repeat identical FAQ text verbatim across pages; put location-specific testimonials only on the matching location page. [Part III 2.10; Part III 3.4]
- Word count: 400-500 words is fine for a low-competition term; if competitive, audit who ranks and match their depth (up to ~2,000). Always organize it so a human reader can consume it and decide to hire you. [Part III 3.5]
- Keyword-first title/H1/meta ("Sell your house fast, Delaware, Ohio"); match the abbreviation people type ("St. Lucie"). [Part III 3.5]
- "Near me" is never a target keyword, never in a URL or copy: "the sign of somebody who doesn't know how to do SEO." Support proximity with real local signals instead (explicit service-area names, a visible address). [Part II 2.5; Part III 2.3; Part VI 2.1]
- Schema for multi-city: a separate page-specific schema on each city page naming only that one city; a full separate schema per physical location/GBP; main schema on the homepage listing every service-area city. [Part IV Schema]
- Layer local into broad content: even a broad how-to post should carry a local CTA with an anchor link ("If you're looking for a hairstylist in Denver, [link] give us a call") plus NAP in the footer and a link to your GBP. [Part VI 2.2]
- Do NOT jam your target city into general how-to posts to force geo-relevance: one member's edit inserting a town name into broad-ranking posts (on ChatGPT's advice) dropped traffic; reverting all affected posts at once is fine, give it 1-2 months. [Part VI 2.6]
- Out-of-area traffic that can never convert locally is still worth it: it builds engagement/authority signals that indirectly help local rankings. [Part VI 2.6]
- For AI Overviews, broaden geographic scope in written content (write around the full state/province, not just one city). [Part V 7.2]
- Locale/geo duplicates (Shopify EN-CA vs default English): pull GSC to see which variant ranks; for blog content redirect the loser to the winner; for product pages don't force a redirect (use a switcher). Bilingual URLs on subfolders (`/fr/`), not subdomains; set hreflang. [Part IV Canonicals]

## 4. Product, collection, category pages (ecommerce: homepage/collection/product keyword split, Shopify collection structure, product naming)

Keyword split
- Stop trying to rank the ecommerce homepage for one keyword; give each featured product a clean homepage section with descriptive text; push actual ranking onto collection and product pages. [Part VI 3.1]
- Collection page = the broad, competitive keyword (repeated in the collection title, every product title in it, and body copy). Product page = specific/attribute-based ("polyester paddle shirt," "18-karat gold engagement ring"). Reinforce a collection by repeating its exact keyword phrase in every product title inside it. [Part VI 3.1]
- Shopify collection pages CAN and do rank (unlike blog category/tag pages, which basically never do); optimize them like money pages. [Part IV Page-Builder; Part VI 3.1]
- Put high-intent/transactional terms ("Scorpio candle," "buy ghost peppers hot sauce") on collection or product pages, not blog posts. "Everybody's trying to get through the front door... I want to go through the back door where nobody else is going." [Part II 2.3; Part VI 3.1]
- Rough volume floors for a low-authority site: product pages >= ~30 monthly searches, collection pages >= ~50 (go lower for a brand-new site). [Part II 1.4; Part VI 3.1]
- Singular vs. plural can carry very different difficulty; check both ("tennis t-shirts" KD ~16 vs. "tennis t-shirt" KD 8 at higher volume; the singular won). [Part VI 3.1]
- Match SERP format: "ski t-shirt," "tennis shirts" SERPs are dominated by collection pages, so optimizing a product page for that term fights the wrong format. [Part II 2.2]
- A collection/category page and a blog post on similar subject matter are not cannibalization provided the blog targets a distinctly longer-tail keyword ("natural granola" collection vs. "benefits of natural granola" post). Product-comparison pages (Botox vs. Dysport vs. Xeomin) are a valid consideration-stage content type, not cannibalization of the individual product pages. [Part II 3.1; Part III 2.13]
- Portfolio strategy when no single head term has enough volume: build many small transactional variants (per zodiac sign, per birth month, "funny tennis shirts") plus one hub/master post linking to each. "Cosmos Within" candle brand: "horoscope candles" ~19 KD / ~110 per month, "Scorpio candle" zero difficulty. [Part VI 3.3]
- Multi-niche stores (tennis + padel + horseback apparel) create per-niche research friction but can work under a unifying "sports" frame. [Part VI 3.3]

Shopify collection-page structure
- "The biggest missed opportunity when I look at a Shopify store": intro sentence(s) -> product grid -> long blog-length paragraphs with images underneath, covering the collection in depth. Put marketing/info copy BELOW the grid, never above it (someone on a collection page is ready to buy, not read; especially on mobile). [Part III 3.3; Part VI 3.2]
- Add real product photography (a person using/wearing the item) with descriptive alt text. [Part VI 3.2]
- FAQs on collection pages first (broadest reach, far less labor than per-product), built as Shopify's native collapsible-row component. Write them as plain H2 questions (not labeled "FAQ") answered in natural human language that reincorporates the keyword a few more times ("How long does the temporary tattoo last?"). Two payoffs: preempt purchase-blocking questions (conversion) and feed long-tail/AI search. For near-identical SKUs (jewelry, collectibles), write product-specific FAQs (carat, metal, care); never duplicate the same FAQ block across every page. [Part VI 3.2] (Note the tension with the general rule elsewhere that important FAQ content should never sit behind an accordion/toggle [Part III 2.10]; the playbook states both.)
- Supplementary technical detail (product specs) inside an accordion is fine. [Part III 2.10]
- Use the native blog, skip third-party blogging apps. Shopify blog pagination often defaults to 6 posts/page; set to ~30 (then 60, 100 as it grows, since more posts per page slows load). Ensure every post has a featured image. [Part IV Page-Builder; Part VI 3.2]
- Shopify H1 is auto-placed in the logo; duplicate H1s commonly injected by page-builder apps (GemPages); fix in `product.liquid` / `theme.liquid` via Edit Code, self-fixable with ChatGPT or Sidekick; workaround is a redundant second H1 containing the keyword plus escalation to Shopify support. A Shopify H1 sitting on a "limited time offer" element far down the page had to be moved to the top. [Part IV Heading Structure; Part IV Page-Builder]
- Dawn theme auto-appends the store name to titles (find the toggle or the `[store name]` shortcode; flipping it retroactively changes every page). The URL-edit screen has a checkbox to auto-create a redirect. [Part IV Page-Builder]
- Shopify meta descriptions: never rely on the auto-pulled excerpt; one real case pulled EU product-safety warning copy, a dead giveaway the field was never filled. [Part III 2.2]
- Shopify speed checklist (four things): CDN set up; images served as WebP; image lazy loading enabled; CSS/JS deferred. [Part IV Site Speed]
- Shopify robots.txt over-blocking (disallow lines for blog/collections/products) is usually injected by a third-party app; disable the suspect plugin. [Part IV Robots.txt]
- Dynamic URLs (a `?` or `=` near the end) are inventory/search-result pages that will not rank; ignore them in GSC, confirm they are not in the sitemap, build a static page for anything that needs to rank. [Part IV Canonicals]
- "You may also like" / related-product blocks count as internal links toward the 10-20 per page ceiling. Strip heading tags from "Related products", cart/quantity modules, breadcrumbs. [Part IV Heading Structure; Part IV Internal Linking]
- Product sites reuse the homepage wireframe with product categories. [Part IV Web Design]
- Add a small inline quote form on each product/service page. [Part III 3.4]

Product naming and keywords
- Name products what real searchers type, not invented brand language. Type the plain physical/functional description into a keyword tool, find the phrase with real volume + low competition, and rename the actual product title (not just alt text) to that phrase; append the cute/brand name at the end, never the reverse. Cases: a "cream beaver fur hat" under a made-up name -> "beaver fur top hat" (260/mo Canada, 880/mo US); Irish-named candles -> "Vanilla Soy Candle" (~30/mo) with the Irish name appended; a product filed under generic "novelty bongs" -> "octopus bong." Get explicit client sign-off before overriding a preferred name. [Part II 1.5; Part VI 3.3]
- "Always follow the keyword research and never guess. Never," even against your own attachment to a product name. [Part II 1.5]
- Novel product with no search demand: don't force the keyword nobody Googles; identify the underlying problem the user searches ("nobody buys my book, what do I do") and build content around that, write an "[established competitor product] alternative" page, or an "old thing vs new thing" comparison post. [Part II 1.5; Part VI 3.3]
- Competitor brand name as a secondary (never primary) keyword, in body copy as a comparison ("Compared to Suavecito pomade, our pomade is..."). [Part II 2.6]
- Placement: keyword in the product/page name (= H1), title tag, meta, first 100 words, at least one H2, an FAQ, alt text, image file name. [Part III 2.6]
- Image file names like `black-flame-paddle-shirt.jpg`, not `1234.jpg`. Per-variant alt text: every diamond-shape photo (round, cushion, pear, emerald) getting identical alt text "diamond" is a missed opportunity; use shape-specific alt text and file names. [Part III 2.8]
- Product/Article schema via manual JSON-LD (reviews, prices) pasted into the page header; Yoast default schema is enough for most. [Part IV Schema]

Seasonal, stock, reviews, pipeline
- Publish supporting content BEFORE the thing is ready so it is indexed when demand hits: a florist optimizes for major gifting holidays ~6 months out; write "gifts for a May birthday" months before the spike. [Part VI 3.4]
- Seasonal/annual pages: keep ONE evergreen URL with no year in it; update the title/meta/H1 to the new year each year (2026 -> 2027) rather than making a new page. Never put the year in an evergreen URL. [Part III 2.3; Part VI 3.4]
- Seasonal money pages: a dedicated page per key season (Black Friday, Christmas, Valentine's); keep the URL live year-round but pull the nav link out of season. [Part VI 3.4]
- Never straight-404 a product that might restock; hide "Add to Cart" or set inventory to zero and leave the page live. Only fully remove (zero stock + 301) permanently discontinued products. A permanently discontinued service = 410. [Part IV Migrations]
- Reviews are a direct ranking factor for ecommerce product listings (a product with ~5,000 five-star reviews gets surfaced above comparable products). [Part VI 3.4]
- If directories outrank you, get listed on them (free) rather than out-content them. GBP for ecommerce only for a real storefront/service area. Skip local directories for a nationally-shipped brand with no storefront. [Part VI 2.4; Part VI 3.4]
- Blog-to-paid-product pipeline: publish the free/shorter version as a blog post, sell a longer detailed version as a standalone paid guide (Jackie's curly-hair guide). [Part VI 3.4]
- Platform blockers: SmugMug (templated image URLs like "image12345" get canonicalized as duplicates), legacy gallery-only templates with zero ability to add text/headings; Square has no true H1 field. [Part IV Page-Builder]

## 5. About / team pages

- The About page is a trust page, not a life story. [Part IV Web Design]
- Keep the exact same palette as the rest of the site (never let an interior page look like a different website). [Part IV Web Design]
- At least one visual element per section. [Part IV Web Design]
- Include a real founder/team photo (humanizes: "you are a real person, not just a stock photo template"). Real photos of the actual team build more trust than stock or AI. [Part IV Web Design; Part IV Conversion elements]
- Never right-align body text; minimize centered text. [Part IV Web Design]
- About pages should not be keyword-targeted: like the homepage, contact, and blog category pages, they are not expected to independently rank, and SEO gaps on them usually do not matter. [Part III 3.2]
- Contact and About pages are exempt from external-linking minimums. [Part III 2.12]
- Move non-essential nav items (store, careers, policies) into the footer or an About dropdown. [Part IV Web Design]
- The About/intro section inside a money page or homepage: what you do, how, who you serve, with an audience-identifier layout (icon boxes per persona) so visitors self-identify, and its own CTA. [Part III 3.3; Part IV Web Design]
- The trend is toward more authenticity: "Who wrote this? That is telling who is writing the content on the internet." 30-second real clips of an actual team member on site beat faceless content; AI avatars kill trust (~12 views capped vs. ~1,000-2,000 once the real person appeared). [Part II 4.6; Part V 5]
- E-A-T self-audit: after editing content, paste it to Claude/ChatGPT and ask for a grade on each E-A-T category plus specific improvements. [Part II 4.3; Part VI 1.7]
- Nothing else in the playbook is specific to About/team page structure, length, or headings.

## 6. Contact / quote / booking pages

- Contact page contents: phone, email, hours, socials, contact form, map/location. Put the highest-priority contact method above the fold. [Part IV Web Design]
- The contact page H1 does not need the keyword; label it "Contact Us." [Part IV Web Design]
- Never two contact forms on one page. [Part IV Web Design]
- Use a static linked map screenshot, not a live embed. Replace live Google Maps iframe embeds with a static WebP screenshot linked to the real Maps/GBP listing: PageSpeed flags Google's own embed as a drag, and visitors do not interact with the live map anyway (confirmed on Hey Tony's own site). [Part IV Web Design; Part IV Images; Part V 4.4]
- Anchor-link CTA technique (Elementor/Divi/Showit/Squarespace): give a section a CSS ID and point a button at `#contact` to scroll instead of loading a new page. [Part IV Web Design]
- Contact pages and booking/appointment pages are NOT money pages ("those pages don't rank"); a third-party booking tool is explicitly not your money page, though the money page may link out to one. The money page sends the visitor TO the intake form; the form itself is not the money page. [Part III 3.1]
- Contact pages are not keyword-targeted and not expected to rank. [Part III 3.2]
- Contact and About pages are exempt from external-linking minimums. [Part III 2.12]
- Audit flags (orphan page, low word count) on contact, thank-you, ad landing, category/archive, and funnel pages are routinely intentional and fine to ignore. [Part III 4.1; Part III 4.6]
- Quote forms: keep one dedicated "Get a Quote" page, and also add a small inline quote form (name, phone, email, short message) on each product/service page. [Part III 3.4]
- Phone numbers and emails tap-to-call / clickable everywhere, especially mobile; anchor a labeled clickable number at the bottom of the screen for a mobile-heavy audience; an icon-only floating button with no visible number tanked call conversions. [Part III 3.4; Part IV Mobile]
- Make the on-site business address a clickable CID link rather than plain text (these links exist for the search engine, not human click-through). [Part V 4.3]
- Keep NAP identical across every listing and present/crawlable in the site footer. [Part V 4.4; Part V 4.5]
- Don't publicly list a home address in schema/GBP for a remote business (safety). [Part V 4.1]
- Missed/unanswered calls hurt local rankings (Google reads it as a bad user outcome). [Part V 4.1]
- Low-stakes booking pages for two cities (escape room, Anaheim vs. Connecticut) can differentiate on title tag + meta description alone ("Booking - Anaheim"). [Part IV Canonicals; Part VI 3.3]
- Lead-magnet quizzes and internal-only pages may be deliberate orphans; pair them with a no-index tag. [Part IV Crawl Depth]

## 7. Pricing pages

- Call the pricing page "Pricing," not a euphemism like "Investment" (people search "[service] pricing"). [Part III 3.4]
- List pricing/cost ranges on your own site even as a premium provider: "if you don't have any prices, you're getting left out entirely" from price-shoppers who will shop regardless. Nuance: a luxury provider whose buyer decides through an in-person/call experience can validly hide prices; the test is your buyer's actual decision process. [Part VI 5.1]
- A pricing money page can link to a relevant blog post and vice versa. [Part IV Internal Linking]
- Cost and pricing content is the first of Marcus Sheridan's Big Five (how much, what affects price, is it worth it, cheap vs expensive). [Part II 4.3]
- AI Overview citation pattern for price claims: state the consensus figure first, then pivot: "The average kitchen renovation costs $50-75,000 in [area]. However, we can do it for $25,000." Writing only "we do it for $25-35K" will not get cited. [Part II 4.7; Part V 7.2]
- Manual JSON-LD schema can carry prices (Product type) if you choose to add it; paste into the header. [Part IV Schema]
- Hey Tony Watchdog monitors competitor pricing changes with a before/after diff. [Part VI 1.4]
- Nothing else in the playbook is specific to pricing-page layout, tables, or length.

## 8. FAQ pages and per-page FAQ blocks

- Plain question-then-answer text directly on the page. Mark each question as H2 (or plain question-then-answer, no literal "Q:"/"A:" prefix). Answer directly and briefly, then link out to the fuller blog post for depth (FAQ -> blog -> money page chain). [Part III 2.10]
- Cap at 3-4 FAQs per page. 12 on one page is too many; split onto a dedicated page. Each standalone FAQ question can become its own blog post. [Part II 4.7; Part III 2.10; Part V 7.3]
- Never hide FAQs behind an accordion/toggle/dropdown for genuinely important SEO content; it adds parsing friction for Google and AI crawlers. "Well, if this information is so important, why is it hidden in a box?" Supplementary technical detail (product specs) inside an accordion is fine; accordions are also acceptable to pad thin word count where the expanded content is genuinely substantive. [Part III 2.10; Part IV Conversion elements]
- Put an FAQ tied to that page's one focus keyword on every page, not one central FAQ page. "If you have all your FAQs on one page, what are we ranking for?" Never repeat identical FAQ text verbatim across pages. [Part III 2.10; Part IV Conversion elements]
- FAQs are not a free SEO win: stacking ~10 generic FAQs at the bottom after the CTA does nothing on its own ("is this actually helpful to a human? Probably not"). An FAQ-style piece of content overall can genuinely help. [Part II 4.7; Part III 2.10]
- Keyword placement checklist includes "an FAQ" as one of the places the keyword should appear. [Part III 2.6]
- Collapse redundant closers: don't stack separate TL;DR + Conclusion + Key Takeaways + FAQ that all restate the same thing. [Part V 7.3]
- Shopify: FAQs on collection pages first (broadest reach), as plain H2 questions (not labeled "FAQ") in natural language that reincorporates the keyword ("How long does the temporary tattoo last?"), built as the native collapsible-row component; product-specific FAQs for near-identical SKUs; never duplicate the same FAQ block across every page. [Part VI 3.2]
- FAQ schema: deprioritized by Matt's own testing (after a year, "no more or less useful"; showed no measurable difference). Skipping it carries no penalty; only worth the manual dev effort for high-competition keywords. [Part I 2; Part IV Schema; Part VI 4.4]
- FAQ schema via AI: describe your on-page Q&A to Claude/ChatGPT/Gemini, ask it to generate the schema, paste into the code-injection block. [Part IV Schema]
- FAQ schema is double-edged: it can drive real "Google's AI now recommends me" outcomes but can also draw heavy AI/training-bot crawl traffic (one case spiked to 150,000 visits/day vs. ~40 normal; another triggered 100,000+ simultaneous legitimate bot hits that crashed shared hosting even with Cloudflare's AI-block on). Fix: block the bad bots (take the snippet to Claude and add a bad-bot rule) and upgrade hosting (~$30/mo cloud/VPS + WAF); never strip the schema earning the visibility. [Part IV Schema; Part V 7.4]
- A "Key Takeaways" or FAQ block bolted onto every post after the CTA does not itself help; the bar is "is this actually helpful to a human being?" [Part II 4.5; Part III 2.10]
- Reddit-sourced questions and People Also Ask questions are the raw material for FAQ questions and standalone posts. [Part II 1.3; Part V 6]

## 9. Blog index and blog post pages (structure, length, images, headings, CTAs, internal-link publish loop, AEO structure)

Blog index / roll / archive / categories
- The blog roll/archive is optimized for usability, not ranking; the individual post earns traffic. [Part IV Web Design]
- Blog roll structure: 5-10 category names as plain links at the top (each to a real category archive), then the chronological preview list (newest first, capped ~50), no repeated category links partway down. [Part IV Web Design]
- Never build a filter widget that appends a `?taxonomy=` query string (Google does not treat it as a real page). [Part IV Web Design]
- Blog listing/category pages must never show full post content: only a thumbnail and an excerpt with a click-through. Full content on both listing and post gives Google two identical pages and it fails to index one. Truncate auto-excerpts to a fixed length (~200 characters). [Part IV Canonicals]
- Categories: exactly one per post (max 2 for a genuinely cross-cutting piece), never "Uncategorized." 5-10 categories total sitewide; don't create categories until you've published ~10-20 posts. Never use tags ("never, ever, ever"): each tag spins up a thin near-empty archive page; delete existing ones. [Part II 4.10; Part IV Quick Reference]
- Blog category/taxonomy pages should not be keyword-targeted; duplicate H1s or SEO gaps on them usually do not matter. Shopify blog category pages basically never rank. Low word count on category/archive pages is fine to ignore. [Part III 3.2; Part III 4.6; Part VI 3.1]
- If blog content was mistakenly built as Pages and is already ranking, leave the URLs alone and use Posts going forward. Use blog posts (they auto-populate the roll and category archives), not static pages. [Part IV Web Design; Part IV Crawl Depth]
- Put "Blog" in the nav and keep the label "Blog" (do not rename to "Learn Hub"). [Part IV Crawl Depth]
- Shopify blog pagination often defaults to 6 posts/page: set to ~30 (raise to 60/100 as the blog grows). Use the native blog, skip third-party blogging apps. [Part IV Page-Builder; Part VI 3.2]
- Kajabi puts a blog-index title as an H1 above every post's own H1 (convert the index title to H2/paragraph); Kajabi's roll pulls a body H2 oversized (patch with inline `<span style="font-size:Npx">`; the underlying heading should be H3/plain). GoHighLevel auto-creates two blog pages by default (delete the unused one). [Part IV Heading Structure; Part IV Page-Builder]
- Elementor: build a custom single-post template in Theme Builder (Post Content widget auto-pulls the body; a Table of Contents widget anchors only H2/H3); a second active single-post template throws a conflict error; new templates apply retroactively to every existing post. [Part IV Page-Builder]
- Disable comments sitewide ("the only thing you'll get on blogs is spam"). [Part II 4.10; Part VI 4.2]
- Open the `post-sitemap.xml` to isolate blog posts for AI tools. [Part IV Sitemaps]

Why and what to write
- Blog posts are "the lifeblood of a website. It gives you authority." Seven mechanisms: traffic + trust, internal-linking equity, unlocks harder keywords, organic backlinks, the avalanche/snowball, consumer trust, topical authority. [Part II 4.1]
- Blog posts are informational-intent by default and usually aren't meant to convert directly; a high-ranking post with weak conversion may just need a business-relevant CTA, not a rewrite into a sales page. Sometimes a post's only job is passing internal-link authority to a money page. [Part II 2.3; Part IV Internal Linking]
- Title the post as the literal question a customer asks. Pick a question you can personally answer today. Source from AnswerThePublic pages 2-4, People Also Ask, the hidden Bing set, Reddit, client calls. [Part II 1.3; Part II 4.2; Part II 4.9]
- Long-tail = 4+ words; ~10 searches/month is acceptable; KD 0-15 ideal (under 14 for a new site), up to 25 possible; a page-1 winner with 0-2 referring domains is winnable with no links. [Part II 1.1; Part II 1.4]
- A blog post's target keyword should never be your homepage's primary keyword. The money page owns the exact buyer-intent phrase; blog posts cover adjacent educational angles and reference the money-page phrase at most once, near the bottom as a link back. [Part II 2.4; Part II 3.3]
- Differentiate near-duplicate topics by angle/audience, not just wording ("what to do when my wife has sexual avoidance" vs. "...husband..."; listicle vs. explainer vs. pros-and-cons). Never A/B test two posts for the same keyword. [Part II 3.3; Part II 4.9]
- "Problems with X" radical-honesty posts: title "The problems with hiring/buying [X] that no one talks about"; must be genuinely honest, never a disguised pitch. [Part II 2.6]
- "Best [service] companies in [city]" list: name every competitor, say genuinely positive things, never hyperlink any of them, internally link hard toward your own converting pages; you don't have to include your own company. [Part III 2.12; Part V 1.3]
- Big Five ideation (cost/pricing, comparisons, "best of," problems, reviews): first "summarize this" on each of the top-3 ranking articles one at a time, then "I only want 20 blog post ideas that work for any business, not for specific industries. The keyword I'm trying to rank for is [X]. I want you to come up with topics based on Marcus Sheridan's Big Five blog posts.", then "Write me a blog post based on these ideas. Knowing the keyword is [X], it should be helpful, unique, and include my personal expertise, experience, case studies, etc. Use any relevant info from previous chats." Add one external link to Sheridan's own site. [Part II 4.3]
- Novel/category-defining products: write an "old thing vs new thing" comparison post instead of forcing the question workflow. [Part II 1.5]
- Never publish a raw podcast/video transcript as an indexed page; write a post answering a searched question and reference the episode inside it. Only repurpose a video when it's tied to a real keyword/question (keyword first, blog second, video attached underneath). [Part II 4.12]
- A recurring support/onboarding question becomes a one-time how-to post (Matt's "how to add and remove users from Meta Business Manager" replaced a 30-60 min onboarding call and later earned traffic). [Part II 4.12]
- Never publish the same full content on your site and LinkedIn (LinkedIn has higher authority; your copy can be flagged duplicate). Never republish a guest post on your own site. [Part II 4.12; Part V 1.3]

The writing workflow (interview method)
- Open a brand-new chat; paste the interview prompt (canonical 10-question version): "I'm writing a blog post answering this question: [paste the question]. Ask me anything you need to know the answer to in order to write a blog post that is truly helpful and unique. It should include my experience, expertise, case studies, examples, opinions, etc. Keep it limited to 10 questions. Ask me them one at a time. I'll be using voice mode to answer them. Give me time to breathe as well before going to the next question." [Part II 4.3]
- Five-question canonical variant: "I'm writing a blog post answering this question. [paste in the question you found] Ask me five questions you need to know the answer to in order to write a truly unique and helpful blog post. It should include my expertise, experience, case studies, opinions, etc. Ask me the questions one at a time and wait for my answer before asking me the next question." [Part VI 1.7]
- Cap questions at 5-10 (uncapped defaults to ~30). Voice mode strongly preferred; 2-3 sentences per answer; ~1 min/question; ChatGPT for voice (Whisper), paste the Q&A into Claude for the writing. [Part II 4.2; Part II 4.4]
- Write prompt (canonical): "Write this as a clean WordPress ready blog post using my expertise, experience, opinion, stories, etc. Use H2 and H3 headings only. No horizontal rules, section dividers, tables, call out boxes or other formatting elements. Just headings, paragraphs, and bullet points where appropriate." [Part II 4.3; Part VI 1.7]
- Relay versions: "Write me this blog post using this information." / "Here's my chat with ChatGPT about writing a blog post. There are questions it asked me and my transcript I did in voice mode to answer. Please write me a blog post using this information plus whatever searches you need to do online to get the most accurate information." [Part II 4.3]
- Rewrite bullets to prose: "Rewrite the following. I don't want it to be a bunch of bullet points, that's not helpful. Elaborate on it a bit and ensure there's at least one paragraph. It can still include bullets if useful, just not as the whole section." Length add-ons: "This is a bit long now, shorten it to three to four paragraphs, and don't end it with 'finally.'" / "Same with this, but keep it under 250 words." Subheading breakup: "Let's do some H3 tags or something to break this up a bit." [Part II 4.3]
- Copy the entire draft into a blank Google Doc / Word doc first, never build directly in the CMS (pasting through plain text strips a hidden AI-generated tag some CMS backends store; or use WordPress paste-as-code, or have the AI output raw HTML into the code tab). [Part II 4.2]
- Clean-up pass, strip every AI tell: horizontal rules/dividers/spacer bars; random bold and decorative arrows; emojis (never in heading tags); checkmark bullets and plain numbered markers unless a genuine listicle; the stray leading space; generic "Conclusion" / "Final Thoughts" headers (replace with a specific content-tied closer) and "and finally..."; self-promotional CTA-style subheads in a pure answer post; jargon like "Big Five"; a "Key Takeaways" H2 on every single post can itself tip off unedited ChatGPT. Em dashes: treated by most of the community and Kira's bar as an AI tell to cut (Matt personally says they're fine; moot since raw output never goes live). In WordPress run Clear Formatting after pasting, then rebuild real lists. [Part II 4.5]
- Never publish the first draft as-is; verify every first-person claim the AI invented; "Don't publish anything that you can't stand behind." Gut checks: "Would my customers actually need this and read this? If yes, publish it." / "Am I proud of this?" [Part II 4.2; Part II Cross-Cutting]
- Never run an AI-detector on your own writing, never "humanize" AI output. AI-written content is not penalized; regurgitated generic content is. Matt's ~99% AI "SEO when building a website" post ranked #1/#2 with zero backlinks. [Part II 4.6]

Post structure and headings
- Direct-answer-first: restate the question as a subheading/lead-in, then answer it immediately and plainly in the first paragraph; repeat the keyword/question near the top more than once. Model: "Yes, ChatGPT can help with SEO, but it can't do it on its own." Prompt: "The first paragraph should directly answer the question posed in the title / main keyword." Cut hedging ("the short answer is no"). [Part II 4.3; Part II 4.7; Part V 7.3]
- H2 and H3 only; exactly one H1 (the title) containing the keyword; H2s support the H1; one more H2 than the top competitor (5-10 normal); never skip a level going down; turn generic step labels into keyword-carrying headings ("Clean the door gaskets," not "Step 1"). [Part II 4.3; Part III 2.4]
- H2s should contain the keyword in all, or at least a healthy majority, but don't force it into literally every H2 if there are 10. [Part IV Heading Structure]
- Key Takeaways block at the end of every post: 4-5 bullets, worth doing regardless of length. Prompt: "write me key takeaways for the end." [Part II 4.7; Part V 7.3]
- TL;DR / Summary at the very top only for longer content whose first paragraph doesn't already carry the direct answer; write it so an AI Overview could clip it verbatim (~100 words). Prompt: "Give me a TL;DR at the top of this blog post. Five points max. Call it 'Key Summary.'" Prefer "Key Takeaways" / "Key Summary" over "TL;DR" (reads Reddit-native). [Part II 4.3; Part II 4.7]
- The "AI Markdown" three-extraction-point structure (the version that hit Google Discover with no other change): 1. labeled TL;DR/Summary at the very top answering in 1-2 sentences; 2. restate the answer with more context in the opening paragraphs; 3. Key Takeaways at the end (4-5 bullets). Collapse redundant closers. Only test this on 2-3 pieces at a time. [Part V 7.3]
- Front-load: Google effectively evaluates roughly the first ~500 words; a post that used the keyword 91 times with its takeaways block after dense research stayed "crawled - not indexed." [Part V 7.3]
- AI Overview citation: Google the query, read what the Overview asserts, state that claim first, then pivot with your differentiated info; contradicting outright won't get you cited. Bake in time-relevance (include the current year in content, never in the URL). [Part II 4.7; Part V 7.2]
- Reading level 7th-8th grade; paragraphs of 2-3 sentences; vary sentence length; don't chase an all-green Yoast readability score; ignore transition-word and keyphrase-density complaints. [Part II 4.7; Part III 2.7]
- FAQ on a post: 3-4 max, H2 questions, plain text, never accordion. [Part II 4.7]
- Secondary keywords: "Please give me 10 secondary keywords that are SEO optimized." Cap at 5-10 per piece; only use the ones that fit naturally. [Part II 1.6]
- Keyword density on question posts: the literal question IS the keyword; it appears naturally ~3-4 times with no deliberate insertion; ignore Yoast/Rank Math density tools for long-tail/question content. [Part II 1.7; Part III 2.6]

Length
- No universal word count: Google the exact keyword, check the actual top 3, match them or add ~100-200 words ("level plus one"). Anchors: ~400-500 words is plenty for a zero-competition long-tail; ~700-800-word floor for a normal post (Part III: ~500-800); program baseline 750-1,500 (later 800-1,000); rough ~2,000-word ceiling. A 2,000-word page outranked a 3,200-word one when intent/format matched better. Over-length is one of the most common live failure modes; trim, don't add. [Part II 1.7; Part III 2.5]
- Measure body content only, verify in wordcounter.net (tools disagree by hundreds of words). [Part III 2.5]

Images, video, and embeds on posts
- Roughly one image, video, or chart every 200-300 words, "as often as makes sense"; at least 4 images per post, ideally one per H2; every post needs at minimum a hero/featured image. Where an image doesn't fit a section, a heading-tag break substitutes. [Part II 4.8; Part III 2.8]
- Sourcing: your own real photos/screenshots > relevant AI-generated > stock; AI goes to the top for graphs/graphics; never stock-looking filler. Generate only the featured image with AI and fill in-body slots with real screenshots showing recent date ranges. [Part II 4.8]
- Specs: ~750px wide, 16:9 or square (consistent sitewide); no text baked in; compress anything over ~1MB to WebP ~70% (537KB -> 32KB; 1.9MB -> 102KB). Featured/OG 1200 x 628. GoHighLevel and one of Wix/Squarespace don't accept WebP uploads. [Part II 4.8; Part III 2.8]
- Rename the file before upload ("west-african-wedding-ceremony-toronto.jpg"); alt text the same descriptive phrase, ~5-6 words; exact keyword on roughly half or fewer of a page's images, never sequentially ("Newborn photographer Chicago 1/2/3/4"). [Part II 4.8]
- Featured image prompt (attach 2-4 on-brand refs): "Using the style of the images attached, create me a featured/cover image for this blog post. Here is [the topic]. You don't need any text on the image (no title, no question). [Optional mood: it should be someone who is frustrated or unsure what to do.]" Add "make sure not to include any of the exact images that are in these, make new ones in that style". Infographic: "Make an infographic for this page." Turn a post into an infographic, embed it, cross-post to Pinterest (re-embeds with credit become backlinks). [Part II 4.3; Part II 4.8]
- Canva trap: never export a bare unmodified stock element from Canva's library; add something on top; stick to provable licensed sources (Pexels free + Adobe Stock paid). [Part II 4.8]
- Batch images separately from writing (writing ~15-45 min; images 45 min to 1.5 hrs). Fine to publish text-first and add images later, but if Google crawls before images exist it picks up later-added images noticeably slower. [Part II 4.2; Part II 4.8]
- Video: never self-host; embed YouTube/Vimeo; embed the matching video inside the post under an H2 like "How to Clean X - Video", only when the video already performs. Embed Instagram posts / YouTube Shorts to raise time-on-page; never a widget auto-pulling your latest social posts. [Part III 2.9; Part V 5]

Titles, tags, URL
- Title the post as the literal question, tightening only if generic ("SEO when building a website" -> "SEO when building a website, getting it right from day one"). Keyword toward the front; <=60 characters, ideally under ~55. "The Ultimate Guide to X" is fine if it converts. [Part II 4.9]
- Never "[Post Title] - [Target Keyword]" ("What to Pick in Your Hospital Bag - Chicago Newborn Photographer"): "If it feels spammy, it probably is spammy." [Part II 4.9; Part III 2.1]
- Title-intent audit: for every title ask "what would a real person actually Google to find this?" "When your strength tattoo feels like a lie" -> "strength tattoo pros and cons"; "Soft is not the opposite of strong" is a non-search; "Are temporary tattoos safe?" and "How to stay motivated on low energy days" work. [Part II 4.9]
- Don't let a title/H1 render with a trailing "..."; the on-page rendered title is often the H1, the real `<title>` shows in SERPs/tabs/shares. [Part II 4.9]
- Title prompt: "Write me a title tag for this page under 60 characters. The focus keyword is [X]." Meta prompt: "Write me a killer, compelling, click-worthy meta description for this page." (generate ~5, pick the best). Confirm the keyword appears in both. [Part II 4.2; Part II 4.3]
- URL slug = the core target keyword only (not the long auto-generated slug, no filler words). Set the SEO plugin's focus keyphrase to the exact target; set featured image + alt text; save drafts frequently; keep a backup outside the CMS. [Part II 4.10]
- Preview before publishing: confirm internal links rendered and lists/code aren't unstyled paragraphs. [Part II 4.10]

CTAs on posts
- The content walks the reader down-funnel: answer the informational question, then a contextual internal link/CTA ("check out our hot sauces ->"). [Part II 2.1]
- Every blog post should link to at least one location or service page; broad how-to posts carry a local CTA with an anchor link ("If you're looking for a hairstylist in Denver, [link] give us a call"). [Part IV Internal Linking; Part VI 2.2]
- Weaving your own offer into educational content is fine; the violation is a bait-and-switch. Strip self-promotional subheads from a pure answer post. [Part II 4.5; Part II 4.6]
- Capture an adjacent keyword (a photographer ranking on "wedding venue") via a sidebar/popup/downloadable guide rather than fighting it. [Part II 2.5]

The internal-link publish loop
- Outbound: every new post links to 3-5 other blog posts + 1 money page (2-3 + 1 for a brand-new post/site; 1 link acceptable if you have nothing else; money page + homepage if nothing exists). At least one link must point to a money/service page (or whatever you sell, or the homepage). [Part II 4.10; Part III 2.11; Part IV Internal Linking]
- Inbound (the half everyone skips): after publishing, find 3 different older, already-indexed posts and add a link from each into the new post; Google already crawls those pages, so the new page gets discovered "sometimes within an hour to two hours." "This is a trick that a lot of people don't talk about." [Part II 4.10; Part III 2.11]
- Finder: `site:yourdomain.com "keyword"` (no space after the colon, phrase in quotes), once pre-publish for 3 pages to link TO, once post-publish for 3 different pages to link FROM. [Part III 2.11; Part IV Internal Linking]
- Descriptive anchor text naming the destination (never "click here," "learn more," "here," "website"); in-body contextual links placed higher up outperform a bottom "related posts" block; write a bridging sentence if no natural anchor exists ("We have a full breakdown on how much does SEO cost at Hey Tony"). Use the CMS's existing-page link picker, never a pasted raw URL; internal links open in the same tab. [Part III 2.11; Part IV Internal Linking]
- Ceiling 10-20 links per page (some framing 5-10 at ~1,000 words); hard max 50-100. [Part III 2.11]
- External: 1-2 links per post, at or near the top within the first few paragraphs, hyperlinking the exact phrase to the study; never to a competitor; never to a page targeting your own keyword. [Part III 2.12]
- Prompt: "Using my sitemap, give me three internal linking opportunities from this blog post [using existing text]." Follow-up: "Anchor text, where to place it, give me a sentence where I can add this." [Part III 2.11]
- New sites: just publish; once at ~10-20 posts go back and add ~3 internal links per post. [Part III 2.11]
- Indexing: GSC Request Indexing (10 free/day, often ~2 hours); ~2 hours to ~1 week normal; don't fixate on one post. [Part II 4.10]
- Publish-day promotion: GBP post, newsletter (if genuinely helpful), Reddit, LinkedIn/X/Facebook/Pinterest summary + link (~100 words of your own framing, never a bare link), ask an adjacent business to link, client posts it on their LinkedIn; never links inside Instagram/TikTok posts. [Part II 4.12; Part V 5]

Cadence and refreshing
- 1 post/week floor; 1-2/week ceiling ("I wouldn't do any more than two, because it's going to get sloppy"); never both on the same day (Mon/Thu); new-site launch may batch 5-6 or launch with 10 then drip 2/week; established site never a dozen at once (~500 pages/week got "retaliated" against); hub exception 5/week only if quality holds; batch-write, paced-publish; publish as soon as ready ("no one's gonna see it yet anyway"). [Part I 7; Part II 4.11]
- Refresh old posts every few months: at minimum update the date, ideally revise; prioritize by Search Console (high-impression, low-click first). Never rewrite/republish a post as a new post to "refresh" it; edit in place (a copy-paste repost is a cannibalization risk). [Part I 7; Part II 3.3]
- Reviving a stuck old post: change something so it reads fresh (update copy, tie to a newer post, add a backlink), then request indexing every 2-4 days until it resolves. [Part IV Indexing]
- Refresh schema: Yoast's default schema toggle is enough; Article/Blog manual JSON-LD only if you want it. [Part IV Schema]

## 10. Portfolio / gallery / case-study pages

- Nothing in the playbook prescribes a portfolio, gallery, or case-study page structure. The adjacent rules that apply:
- Put excess photography on a separate gallery page: every image on a content page should illustrate a specific point; do not stuff photos "because people like pretty pictures." [Part IV Images]
- Legacy gallery-only templates with zero ability to add text/headings are a genuine platform blocker; SmugMug's templated image URLs ("image12345") get canonicalized as duplicates; Ghost has clean image handling and alt-text support (a positive for photographers vs. SmugMug). [Part IV Page-Builder]
- Image rules still apply: descriptive file names before upload, alt text on every image with the medium + a real description, keyword on at most half the images, never sequential identical alt text ("Newborn photographer Chicago 1/2/3/4"), per-variant alt text (round/cushion/pear, not all "diamond"). [Part III 2.8]
- Photographer H1 example: "romantic storytelling wedding photography in Toronto" -> "Timeless wedding photography in Toronto." Word-order variants ("Chicago newborn photographer" / "newborn photographer Chicago" / "Chicago newborn photography") are ONE topic, one page. [Part III 1.1; Part IV Heading Structure]
- Never use a graphic or image as the H1 (Google can't read baked-in image text). [Part III 2.4]
- Screenshots read as more authentic than over-polished imagery; real photos of the actual team/crew in the hero build trust. [Part IV Conversion elements]
- Case studies belong inside content as proof: the interview prompt explicitly asks for "case studies, examples, opinions"; the E-A-T self-audit grades the result. [Part II 4.3]
- Heading hygiene on gallery-style pages: client-name callouts, logos, signage graphics, and animated elements should never carry heading tags (one audit found 13 H1s firing from the logo, signage graphics, and animated elements). [Part III 2.4; Part IV Heading Structure]
- Squarespace animated section reveals are a crawl risk (Google's bot "scrolls" at a set pace and may miss unrendered content): cut reveal timing roughly in half. Lazy loading can break images with attached effects/animations; test after enabling. [Part IV Images; Part IV Page-Builder]
- Image sizing for galleries: under 1000px wide except banners; source under 2K resolution (downsize DSLR captures); half-width images ~500-700px; check actual pixel dimensions via "open image in new tab." [Part IV Images]

## 11. Testimonials / reviews pages (and the reviews micro-site tactic)

On-site testimonials and reviews pages
- Reviews belong on every money page, not just a reviews page. Hand-paste 2-3 real reviews as plain text on each money page, rotating which reviews appear where so the same text is not repeated everywhere. [Part III 3.4; Part V 3]
- Link each testimonial to its real source (Google/Yelp) plus a "Read more reviews" button to the full profile. [Part V 3]
- Embed review text, not just screenshots: Google can't read text inside an image. A screenshot is fine for human visual trust; to carry SEO/AI weight, feed screenshots into Claude and have it transcribe them as real text. [Part V 3; Part VI 2.5]
- Pasted review text contributes word count/SEO; a live Google-reviews plugin can slow the page and sends NO extra trust signal to Google beyond the visible text. [Part IV Conversion elements]
- Never use a review-carousel plugin (added ~1,000 words of markup per page, hurt load time, users scroll past carousels). [Part III 3.4; Part V 3; Part VI 2.5]
- Put location-specific testimonials only on the matching location page. [Part III 3.4; Part V 3]
- A testimonial quote must never carry a heading tag; strip the tag and convert to plain styled paragraph text (do not even demote to H2). [Part III 2.4; Part IV Heading Structure]
- Testimonials section sits fifth in the canonical money-page/homepage skeleton (pasted real reviews or a Google reviews widget). [Part III 3.3; Part IV Web Design]
- Hero trust signal: 5 gold stars matching Google's color + "Rated 5 stars on Google" hyperlinked to the real Google review link, consolidated into one prominent placement, not repeated. [Part IV Conversion elements]
- Trust row options: years of experience, # of happy clients, 5-star rating, licensed/insured, awards, association logos (pick ~3). [Part III 3.3]
- Reviews feed a press release: gather 5-6 recent reviews max (screenshots fine), upload to Claude, have it weave ~5 reviews around "[Business] is a top-rated [service] in [City]"; the release opens with an aggregate rating ("holds a 5-star average across 111 Google reviews"). [Part V 2.1]
- Review-request rules that shape what lands on the page: ask every customer via a direct, unfiltered GBP link; never review-gate; never specify "5-star"; no on-site solicitation while being watched; no review trains; a sudden cluster (5 within 20 minutes) is a red flag. AI-drafted review replies are fine if reviewed before posting. [Part V 3]
- External-link from money pages/homepage to your own review profiles (Trustpilot, Glassdoor, Chamber). [Part III 2.12]
- Reviews are a direct ranking factor for ecommerce product listings; in local, review velocity (~1/week) can outpace a stagnant competitor with more total reviews. [Part V 3; Part VI 3.4]
- Schema for reviews: manual JSON-LD via any generator, pasted into the header, only if the data is accurate (wrong/misleading schema is the only penalty case). [Part IV Schema]

The reviews micro-site tactic (AI reputation) [Part V 7.6; Part VI 1.6; Part VI 4.3]
- Openly not white-hat: "it is to manipulate the search results, which they don't want you to do." A low-cost, disputed, outcome-based bet.
- 1. Register a domain like "[BusinessName]Reviews.com": its own separate root domain, never a subdomain/hyphenated path off the main site (reads as a more independent third-party source to Google/Bing/ChatGPT).
- 2. Fill it with real reviews written out as real TEXT, not screenshot images (feed screenshots into Claude/Claude Code and have it transcribe while building). Pull reviews from anywhere they exist: Google, Reddit, email, verbal.
- 3. Build it cheaply/fast via Claude Code ("shouldn't take more than a couple hours"): dump review screenshots in, describe the business, "here's what I like, build this out"; host on Railway (free -> ~$5/mo) or Netlify.
- 4. Link FROM your main site TO the reviews site (direction matters) from an already-indexed blog post; keep your on-site testimonials too (additive).
- 5. Do NOT connect/verify these domains in Google Search Console. If registering multiple, don't redirect them into each other.
- Genuinely disputed even among practitioners (one call frames it as something Matt does with no seen downside; another as unproven/secondhand and untested by Matt himself, publicly disputed by another SEO). Theory: AI models may pick it up as a positive reputation signal; cheap enough to test either way. Matt's through-line on gray-hat: "if it seems like you're trying to game the system, don't do it. If it feels bad, if it feels sneaky, don't do it."

## 12. Legal pages (privacy, terms, cookies, disclaimers)

- Nothing in the playbook addresses privacy, terms, cookie, or disclaimer pages directly. Adjacent rules that touch them:
- Move non-essential items (store, careers, policies) out of the top nav into the footer or an About dropdown; keep ~7-8 top-nav items max. [Part IV Web Design]
- Only add robots.txt `disallow` lines for things deliberately hidden (admin dashboard, throwaway pages); Matt does NOT recommend most people hand-edit robots.txt (easy to block the whole site). [Part IV Robots.txt]
- Deliberate orphans (internal-only pages, job postings, lead-magnet quizzes, thank-you and ad landing pages) are fine when paired with a no-index tag; anything you want ranked must never be orphaned. [Part IV Crawl Depth]
- Low word count / orphan flags are fine to ignore on pages you never intended to rank (contact, category/archive, funnel pages); ask first "do I actually want this page found, indexed, and ranking?" [Part III 4.1]
- A Shopify meta description auto-pulled EU product-safety warning copy, a tell that the meta field was never set; always set the field yourself. [Part III 2.2]
- Contrast failures carry real WCAG/lawsuit exposure; the grayscale self-check caught a failure an automated checker missed. [Part IV Typography and color]

## 13. Landing pages, thank-you, 404, sitemap pages, press pages, any other page type

Landing / funnel pages (paid traffic)
- Strip navigation to just a logo linking home; never list them in site nav. [Part IV Web Design]
- Do NOT chase on-page SEO structure on them (it is fine, even expected, that an SEO tool flags them as orphaned); consider noindexing; exactly one CTA color; keep the one job undiluted. [Part IV Web Design]
- Ad landing pages are legitimate deliberate orphans; pair with a no-index tag. [Part III 4.6; Part IV Crawl Depth]
- Landing pages should stay on your own domain when ranking matters; an externally hosted page (Netlify) can convert but likely will not rank; still link back to your homepage from it. [Part IV Page-Builder]
- Build custom on-domain pages/tools with Claude Code inside your existing CMS/theme so the code pastes into your native editor and stays on your domain; do NOT run a website on Claude Code as the platform; back up before any AI touches theme/`functions.php`. [Part IV Page-Builder; Part VI 1.6]
- Launch-timing sequence (CJ): ~2 months before launch, publish a blog post about the program + build its landing page as a placeholder (don't link it yet); on launch day publish a new post about the launch; immediately add a backlink from the original placeholder-era post to the correct new page (verify the URL); an incognito AI search 6 hours later returned the business as the sole direct answer. [Part V 7.5]
- Never publish a "coming soon" placeholder. [Part VI 4.2]

Thank-you pages
- Legitimate orphans; no-index them; audit flags (orphan, low word count) on them are intentional and fine. [Part III 4.1; Part III 4.6; Part IV Crawl Depth]
- Nothing else in the playbook on thank-you page content.

404 and dead pages
- Nothing in the playbook on designing a 404 page itself. Rules around 404s: broken links (a link to a 404) signal "we're not on top of our site's UX"; fix ~10/week by updating the URL, replacing with an internal link to your own content, or removing; external sites that block crawlers produce false positives ("manually validate"). [Part IV Crawl Depth; Part III 4.6]
- Deleting content with nothing to replace it = let the old URL 404, do not redirect; replacing content under a new URL = 301 old to new (topically related); permanently discontinued service = 410; never 404 a product that might restock. [Part IV Migrations]
- "Not found (404)" on pages that should rank is one of the two GSC exclusion reasons worth chasing (with "Crawled - currently not indexed"). [Part IV Indexing]
- Prune dead pages (zero impressions, zero indexing, zero traffic, no backlinks) via GSC; on a spam cleanup set zero-click pages to DRAFT (never delete), and do NOT manually 404, redirect, or request a recrawl. Matt's own mass-delete of 70 dead posts had zero negative impact (unreconciled with the draft-and-wait rule). [Part IV Crawl Depth; Part VI 4.4]
- "Fixing 404 Errors" is cited as a well-framed title tag example. [Part III 2.1]

Sitemap (XML; no HTML sitemap page guidance exists)
- Auto-generated by every major platform (Yoast/Rank Math, Wix, Squarespace, Shopify); never hand-build one; view at `/sitemap.xml` (some `sitemap_index.xml`); formatted page or raw code both fine. [Part IV Sitemaps]
- The one manual step: submit it once to Google Search Console (Indexing -> Sitemaps; 99% of cases the path is `sitemap.xml`); test it loads in a browser first; an immediate "Error" often flips to "Success" on refresh. Never manually resubmit after publishing/fixing content (exception: after a full site redesign). [Part IV Sitemaps]
- One sitemap per site is the norm; segmented sitemaps (posts, pages, categories, authors) must each be submitted individually; submit the specific sub-sitemap path (e.g. `sitemap/blogs`). [Part IV Sitemaps]
- A deleted sitemap is catastrophic (one client dropped "from hundreds of thousands to zero"); a dead sitemap reference in robots.txt silently blocks discovery. Sitemap totals are NOT the true indexed count (they still list redirected and 404 pages). [Part IV Sitemaps]
- GoHighLevel must be manually regenerated + resubmitted after each new post; GoDaddy's builder has failed to auto-generate; Showit runs a separate sitemap from its WordPress blog (submit both). [Part IV Sitemaps]
- llms.txt: check `yourdomain.com/llms.txt`; Yoast auto-generates it (WordPress, or Shopify via plugin); not mandatory, no confirmed ranking impact. [Part V 7.8]

Press / newsroom pages and press releases
- Never publish the press-release text on your own website: the outlets are already linking to you, so hosting the same copy creates a reciprocal-linking pattern. Share it on social + your email list instead. [Part V 2.3]
- Press release structure (on the wire, not your site): "For Immediate Release" + dateline, headline, an aggregate-rating opening, a placeholder owner quote swapped for a real one, review quotes, an "About [Company]" boilerplate; PR Type = "web only"; skip the meta-tags section; title field = headline only; <=500-character summary; a real screenshot image (never stock, never-before-used so pickups are traceable); platform allows 5 links, use only 2-3 (a Google Reviews link + a service-page link, real keyword anchor, CID link for anything pointing at the GBP). [Part V 2.1]
- One release = one topic / one business / one location / one keyword; 1-2 releases/month max, ~2 weeks apart; no real news needed ("[Business] is a top-rated [service] in [City]", launch angle, milestone/anniversary). PR copy does not need a humanizing pass. [Part V 2.3]
- Book-launch title structure: topic keyword + "book" + author ("How to Build a Bookkeeping Business: Book Launched by [Name]"); follow-up = topic keyword + "book" + accolade. [Part V 2.3]
- Providers: AB Newswire ~$80 web-only / ~$110 with USA Today / ~$500 bulk; EIN Presswire $149; PR Newswire demo-gated; full human-reviewed service ~$1,500-2,000. [Part V 2.2]

Other page types named in the playbook
- Comparison pages: "X vs. Y" comparison/informational content = blog post; product-comparison pages (Botox vs. Dysport vs. Xeomin) are a valid consideration-stage type; "[established competitor product] alternative" page for a novel product; "old thing vs new thing" post. [Part II 1.5; Part II 3.1; Part VI 2.1; Part VI 3.3]
- "Best [X] in [city]" listicle naming every competitor without hyperlinking any, internally linked to your converting pages. [Part III 2.12; Part V 1.3]
- Hub/master post linking to many small transactional variant pages (per zodiac sign, per birth month); a ~50-post content hub is an acceptable higher-cadence exception. [Part I 7; Part VI 3.3]
- Seasonal pages: one evergreen URL per season, no year, nav link pulled out of season. [Part VI 3.4]
- Paid guide page: a longer detailed version of a free blog post sold standalone. [Part VI 3.4]
- State-level pages, county pages, town pages, neighborhood pages in a service-area hierarchy. [Part VI 2.2]
- Dynamic URL pages (inventory/search results with `?`/`=`) will not rank; ignore in GSC; exclude the pattern in robots.txt; build a static page for anything that should rank. [Part IV Canonicals]
- Paginated, feed, and author pages are GSC noise ("duplicate without canonical," "blocked," "Alternate page with proper canonical tag"); ignore. [Part IV Indexing]
- Bilingual pages: language versions on subfolders (`/fr/`), not subdomains; an English-slug-plus-"fr" URL is "good enough" if the on-page content is genuinely in that language; set hreflang. [Part IV Canonicals]
- Chamber of Commerce member landing page (on their site): ask for your logo + 2-3 links to specific service pages, not one generic "visit website." [Part V 1.3]
- Guest-post pages (on host sites): only ONE link back to your own site, placed in the top half, specific/geo-qualified descriptive anchor ("clean comedian, Boca Raton"), also link to one of the host's own internal articles, never republish the same/similar piece on your own site. [Part V 1.3]
- Reddit threads / your own subreddit as off-site pages: mentions alone move AI Overview visibility; answer with a blog-post link, not a bare homepage link. [Part V 6]
- Social profile bio link: avoid Linktree/aggregators, link directly to the destination. [Part V 5]

## 14. Cross-page elements: header/navigation/menu, mega menu, footer, sidebars, pop-ups, chat widgets, breadcrumbs

Header and navigation
- Simplify navigation: ~7-8 top-nav items max; move non-essential items (store, careers, policies) into the footer or an About dropdown. [Part IV Web Design]
- Collapse per-condition/per-service links into one "Services" hub linking to sub-pages; never build a giant per-niche dropdown (terrible on mobile). Nav labels should match how the business actually breaks down (not a generic "Services"). [Part IV Web Design]
- Hand the site to a non-technical person and watch, unassisted, whether they can find a page. [Part IV Web Design]
- Put "Blog" in the nav and keep the label "Blog" (not "Learn Hub"). Add a "Locations" hub in header/footer linking to every location page. [Part IV Crawl Depth; Part VI 2.2]
- A page linked from the nav is 1 click from the homepage; money pages must be reachable from nav, not buried, and every ranked page <=3 clicks deep. [Part III 2.11; Part IV Crawl Depth]
- Header block (header/contact area) ~1/6 of the page, not half; shrink oversized logos; do not show the logo twice (image + text). [Part IV Web Design]
- The logo must never be an H1 (developers "very commonly" mark the logo or every heading as H1; Shopify hard-wires the H1 to the site logo). [Part IV Heading Structure; Part IV Page-Builder]
- Hidden overlay text behind the nav is a cloaking pattern to remove on sight, unless the page is ranking (Ellen Mitchell's probate page), in which case it is left alone. [Part III 1.2; Part III 2.4]
- If the header nav is not sticky, replicate its links in the footer so the footer is never a dead end. [Part IV Web Design]
- Landing/funnel pages strip the nav to a logo linking home. [Part IV Web Design]
- Seasonal money pages: pull the nav link out of season, keep the URL live. [Part VI 3.4]

Mega menus and dropdowns
- Long service lists: core services prominent, long tail into a mega menu/dropdown, each item linking to its own page. [Part IV Web Design]
- Dropdown/mega menus do not add a click themselves (only leaving the page counts), but overstuffed dropdowns hurt usability, especially on the ~50-60% of traffic that is mobile. [Part IV Crawl Depth]

Footer
- Footer titles above menu columns should be H4 or smaller (or plain text), never H1/H2/H3. [Part III 2.4; Part IV Heading Structure]
- Keep NAP (name/address/phone) present and crawlable in the footer, linking to the GBP via the CID link; Google "looks for that to determine if it's a local business." NAP identical across every listing. [Part V 4.4; Part V 4.5; Part VI 2.2]
- Footer-only links to new local pages index slower than homepage links. [Part VI 2.2]
- A bottom/footer "related posts" block carries less weight than in-body links placed higher; acceptable only as a fallback. [Part IV Internal Linking]
- "Powered by / website design by" footer credit links are a legitimate early-stage backlink tactic for new web designers only. If any single external/client site is responsible for >100 backlinks to you (e.g. a sitewide footer link), remove your link from it; one footer link responsible for 100,000s of backlinks read as spam and suppressed indexing. [Part V 1.3; Part V 1.6]
- Measure word count on body content only; exclude footer, nav, and sidebar boilerplate. [Part III 2.5]
- Footer is part of a page's outgoing paths; a dead-end page has zero outgoing links (no internal, external, nav, or footer). [Part IV Crawl Depth]
- A dead sitemap reference / nofollow attributes can hide in footer code; View Source and Ctrl+F "nofollow" when a linked page still flags as orphan. [Part IV Crawl Depth]

Sidebars
- In-body contextual links carry more weight than a sidebar or footer "related posts" block. [Part IV Internal Linking]
- Capture an adjacent keyword via a sidebar/popup/downloadable guide rather than fighting it on the page. [Part II 2.5]
- Sidebar boilerplate is excluded from word count. [Part III 2.5]

Pop-ups and promo elements
- Popup/promo elements carrying their own heading tag create duplicate H1s: change the popup's heading to plain paragraph, restyle visually so nothing changes for the visitor. [Part III 2.4]
- Tools scrape hidden popups, review-widget text, mobile-duplicated text, and currency/country selectors, inflating word and density counts (808 tool vs. 511 manual); a plugin once silently injected 2,000 words of hidden text onto every page. Verify in wordcounter.net. [Part II 1.7; Part III 2.5]
- A popup/downloadable guide is an acceptable way to capture adjacent-keyword traffic. [Part II 2.5]

Sliders, carousels, widgets
- Never an auto-rotating slider/carousel or autoplaying hero video; never the Revolution Slider; never a review-carousel plugin (~1,000 words of markup); never a widget that auto-pulls your latest social posts (slows it, adds nothing); a live Google-reviews plugin slows the page with no extra trust signal; replace live Google Maps iframes with a static WebP screenshot linked to the listing. [Part III 3.4; Part IV Conversion elements; Part IV Images; Part V 5]
- "You may also like" / related-product blocks count toward the 10-20 internal links per page ceiling. [Part IV Internal Linking]
- Automated interlinking plugins (Link Juicer / Internal Linking Juicer) are fine but Matt avoids relying on them (no human judgment, redundant links). [Part IV Internal Linking]
- Table of Contents widget (Elementor) anchors only H2/H3. [Part IV Page-Builder]
- Mobile/desktop duplicated blocks (Avada, Wix, Squarespace, GoHighLevel, Shopify) load the same heading twice; build one truly responsive block with per-breakpoint settings. Claude Code prompt: "make this mobile friendly in the same blocks without duplicating the content." [Part III 2.4; Part IV Heading Structure]

Chat widgets
- Nothing in the playbook on chat widgets. Closest rules: phone numbers/emails tap-to-call everywhere; a labeled clickable number anchored at the bottom of the mobile screen; an icon-only floating button with no visible clickable number tanked call conversions; missed/unanswered calls hurt local rankings. [Part III 3.4; Part IV Mobile; Part V 4.1]

Breadcrumbs
- Breadcrumbs must not carry heading tags; strip the tag and convert to plain text (same rule as "Related products", cart/quantity modules, taglines, logos). [Part IV Heading Structure]
- Nothing else in the playbook on breadcrumbs (no breadcrumb schema guidance).

Cross-page trust signals and CTAs
- One consolidated prominent trust placement (hero star-rating build), not repeated everywhere. [Part IV Conversion elements]
- A CTA in the hero, in every section, and at the very bottom of every page; one dominant CTA color per page; phone/email clickable everywhere. [Part III 3.4; Part IV Conversion elements]
- Anchor-link CTAs to `#contact` scroll instead of loading a new page. [Part IV Web Design]
- Reuse the CID link wherever it fits (blog posts, service pages, linked address). [Part V 4.3]

## 15. Per-element rules for every page

### Title tags
- The blue clickable headline in search results, browser-tab text, and social-share title; directly drives CTR. "Title tag" and "meta title" are interchangeable. [Part III 2.1]
- Length 50-60 characters, ideally under ~55 (longer truncates with "..." in the SERP; gets cut off on mobile). [Part II 4.9; Part III 2.1; Part IV Title Tags]
- Target keyword at (or very near) the front: "really important" / "highest-value tactic." [Part III 2.1; Part IV Title Tags]
- Structure: homepage = brand name + focus keyword; every other page = focus keyword first, brand name at the end (or dropped). Local reorder: "Movers in Washington D.C. | Free Quotes | Your Moving Men". [Part III 2.1; Part IV Title Tags]
- Unique per page; duplicates come from running 2+ SEO plugins (Yoast + Rank Math + AIOSEO each inject tags) or a custom build hardcoding the tag twice; keep exactly one plugin. "Missing" is hard to trigger (CMS auto-populates); restore an old revision if it happens. Edit in the plugin's SEO Title field at the bottom of the editor. [Part III 2.1; Part III 4.6; Part IV Title Tags]
- Frame the title as the exact phrase or question people search. Good: "How long should a URL be for SEO?", "Custom WordPress Development," "Fixing 404 Errors," "Disadvantages of Market Mapping: A Comprehensive Guide," "How to Edit Captions in Facebook Reels." Bad: "10 Simple Ways to Improve Your Google Search Ranking" ("not a well optimized title at all"). [Part III 2.1]
- Never "[Post Title] - [Target Keyword]" ("If it feels spammy, it probably is spammy"). [Part II 4.9; Part III 2.1]
- Match competitors' exact phrasing, not a close synonym, in structural tags (title, H1, meta); Matt lost "website design" visibility while both competitors beating him used "web design." [Part II 1.5; Part III 2.6]
- Don't panic when Google strips the trailing brand name from the SERP display; the HTML is unchanged (verify with the Detailed SEO extension). Don't let a title/H1 render with a trailing "..." on-page: Google literally can't read past the cutoff; the on-page rendered title is often the H1, not the `<title>`. [Part II 4.9; Part III 2.1; Part IV Title Tags]
- Guardrail: if a page already ranks for a keyword, never strip that exact keyword out of the title while "improving" it. [Part III 2.1]
- Prompt: "Write me a title tag for this page under 60 characters. The focus keyword is [X]." Or "five compelling title tag options for this, make sure it includes [keyword]" and pick the best. [Part III 2.1; Part VI 1.7]
- "The Ultimate Guide to X" framing is fine if it converts ("the psychology of it vs the SEO of it"). [Part II 4.9]
- Title-intent audit: for every existing title ask "what would a real person actually Google to find this?" [Part II 4.9]
- Evergreen yearly pages: update the year in title/meta/H1 in place each year; never in the URL. [Part VI 3.4]
- Shopify Dawn auto-appends the store name to titles (toggle or `[store name]` shortcode; flipping it changes every page). [Part IV Page-Builder]
- Money-page fix order starts with the title tag (then meta, then H1), then wait 1-2 weeks. [Part III 4.4]
- Title/meta/H1 nudges can be judged in ~2 weeks to 1 month. [Part I 4]

### Meta descriptions
- Not a direct ranking factor; it is your pitch to win the click ("the billboard saying click me instead of your competitors"). [Part III 2.2; Part IV Title Tags]
- Length roughly 120-155 characters before truncation (guidance clustered at 140-145 and 155-160; a 124-char example was "kind of where we want it to be"); Part IV: ~120-150 displayed, ~155-160 hard cutoff. Precision matters less now: Google increasingly rewrites descriptions, and Yoast cuts them shorter; still always set one. [Part III 2.2; Part IV Title Tags]
- Keyword near the front (in the first 5 words alone can flip a Yoast score yellow-to-green). [Part III 2.2; Part IV Title Tags]
- Unique per page, never duplicated across the site, even across near-identical variants; a common Yoast template bug auto-inserts the same boilerplate into every post; duplicates across a site usually mean 2+ SEO plugins. [Part III 2.2; Part IV Title Tags]
- Benefit-forward, an independent sales pitch naming specific services or differentiators and previewing the payoff; never a copy of the title tag. [Part III 2.2]
- Don't force a secondary keyword in because a tool suggests it ("it'll come up naturally"). [Part III 2.2]
- Don't rely on an auto-pulled excerpt (Shopify pulled EU product-safety copy). Yoast set to pull an excerpt silently overrides an Elementor meta; fix in Yoast's own box. Meta keywords field: ignore, dead since the 90s. [Part III 2.2; Part IV Title Tags]
- CTR fix workflow: ranking well but near-zero clicks almost always traces to a missing/weak meta and/or uncompelling title; write one with the keyword and a specific preview (for "size of Facebook cover photo," promise the exact dimensions plus a click for details); first confirm the impressions are current. [Part III 2.2]
- Prompt: "Write me a killer, compelling, click-worthy meta description for this page." Generate ~5, pick the best. Gemini (free tier) is notably strong on meta-description length compliance. [Part II 4.4; Part III 2.2]
- Open Graph: OG Title mirrors the title tag; OG Image = featured image (1200 x 628); if ALL OG issues fire across most pages, no SEO plugin is installed; check via Detailed SEO "Social" tab. [Part III 4.6; Part IV Title Tags]

### URLs / slugs
- Include the focus keyword; homepage is the exception (bare root domain). No character limit, but shorter performs better; every page needs a unique URL. [Part III 2.3]
- URL slug = the core target keyword only (not the long auto-generated slug, not filler words); CMS auto-lowercases and hyphenates. [Part II 4.10]
- Keep the slug short even when the H1 is long: H1 "Bookkeeping services in St. Petersburg, Florida for small businesses", URL `/services/bookkeeping`. Matt's SEO page ranks #1 in Hamilton with "Hamilton" nowhere in the URL, H1, or H2. [Part III 2.3]
- Bad (stuffing): `balamedia.ca/hamilton-website-designers-web-design-hamilton` (should have been `hamilton-website-designers`). Good: `sociallyinfused.com/services/website-design` (simple, hierarchical, parent -> child). [Part III 2.3]
- Never "near me" / "near you" / zip codes in a URL or copy. [Part III 2.3; Part VI 4.2]
- Never a year in an evergreen page's URL ("best-dental-services-2025"); keep the URL static, update the on-page year in place, 301 any old dated URLs into it. [Part III 2.3; Part IV Migrations]
- URL-change decision framework: is it ranking? does it get traffic? does it have backlinks? Change only if all three are "no." A changed URL is a brand-new page to Google ("new kid at school, nobody knows who they are"); even a textbook 301 does not always preserve traffic. "Update this with extreme caution." If you change it, update every internal link and set a 301. [Part III 2.3; Part IV Migrations]
- Never redirect a redirect; never blindly re-redirect back and forth; redirect loops are penalized; 301 priority when retiring pages: similar ranking page -> similar category page -> similar blog post -> homepage (last resort). [Part IV Migrations]
- Dynamic URLs (`?`, `=`) won't rank; build a static page. Bilingual: subfolders (`/fr/`), not subdomains. [Part IV Canonicals]
- Shopify's URL-edit screen has a checkbox to auto-create a redirect; Rank Math's redirect manager can silently "accept" a 301 without applying it (use a dedicated redirect plugin). [Part IV Page-Builder]
- Use the CMS's existing-page link picker, never a pasted raw URL, for internal links so they auto-update if a slug changes. [Part III 2.11]
- Migration: keep every URL identical (including www vs non-www); launch the entire duplicated site at once; full domain changes lose essentially all rankings ("almost like starting from scratch"). [Part IV Migrations]

### Headings H1-H6
- Book analogy: H1 = book title (the one topic/keyword), H2 = chapter titles (subtopics reinforcing the H1), H3 = subheadings within a chapter. Keywords weigh heavier in headings than body copy. [Part III 2.4; Part IV Heading Structure]
- Exactly one H1 per page, the literal first heading in DOM order (not just visually biggest, not buried under a hero or a run of H3s). "You don't have a secondary title before the book starts." The only tolerated exception: two H1s with identical text from a desktop block and a mobile block (flagged by tools, not a real problem, though Matt now suspects even this reads as gaming). [Part III 2.4; Part IV Heading Structure]
- The H1 must contain the exact target keyword in natural, readable language and no brand name (brand is already in the title tag and URL; brand in the H1 is more acceptable only on a brand-new business's homepage). [Part III 2.4; Part IV Heading Structure]
- Never skip a level going down (H1 -> H3, H2 -> H4); skipping up (H3 back to H2) is fine. "If you skip a step going down the stairs, you're gonna trip. But if you skip a step going up, you're fine." [Part III 2.4; Part IV Heading Structure]
- H2s must directly support the H1's specific topic, not generic value-prop/marketing lines (demote those to paragraph text). H2s should contain the keyword (or a variant or local modifier) in all or a healthy majority, but don't force it into literally every H2 when there are 10. Avoid generic "Learn More"-style headings. [Part III 2.4; Part IV Heading Structure]
- H2 count: one more than the top-ranking competitor (top page has 5, go 7-8); 5-10 H2s is "totally fine" for a normal article; don't drastically overshoot (top page has 50, going to 200 is over-optimizing). [Part III 2.4; Part IV Heading Structure]
- Avoid H4-H6 in practice; convert unnecessary H4s to paragraph text; footer titles above menu columns H4 or smaller/plain, never H1-H3. [Part III 2.4; Part IV Heading Structure]
- Semantic tag is independent of visual size: style an H1 small via CSS (the "split H1" trick: the real keyword phrase in a small `<h1>`, a punchier tagline beside it as a larger H2). In Elementor use the Heading widget's HTML Tag field; in Wix Edit Text -> SEO and Accessibility -> HTML tag. Use the Heading element, not a styled text/paragraph element; never fake a heading with a styled `<div>` or bolded paragraph; JS-rendered pages (React + Tailwind) must emit real `<h1>`/`<h2>` elements. [Part III 2.4; Part IV Heading Structure]
- Never use a graphic or image as the H1 (Google can't read baked-in image text; it doesn't scale responsively). Never emojis in heading tags. [Part II 4.5; Part III 2.4; Part IV Typography and color]
- Turn generic step labels into keyword-carrying headings ("Clean the door gaskets," not "Step 1"). [Part III 2.4]
- Duplicate/mis-tagged H1 two-path fix, applied to every extra heading ("does this support what the page is about?"): real topical content mis-tagged as H1 -> downgrade to H2 (example: "What Wedding Band Styles Couples Like" corrected to H2); NOT real content (hero/lead-magnet box, CTA, testimonial quote, tagline, logo, name callout, breadcrumbs, "Related products", cart/quantity modules) -> strip the heading tag entirely to plain styled paragraph text, don't even demote to H2. [Part III 2.4; Part IV Heading Structure]
- Duplicate-H1 sources: mobile/desktop block duplication (Avada, Wix, Squarespace, GoHighLevel, Shopify) -> one truly responsive block with per-breakpoint settings; popup/promo headings -> paragraph; Avada Page Title Bar auto-generates an empty duplicate H1 (disable per-page or globally); Kajabi blog-index title above every post's H1; Shopify H1 wired into the logo (redundant second H1 in `theme.liquid`/`product.liquid` + Shopify support); developers marking every heading H1; pressing Enter mid-headline (force the break with container padding, especially GoHighLevel); a headline wrapping to two visual lines can register as two; Square has no true H1 field. [Part III 2.4; Part IV Heading Structure]
- Hidden text (white-on-white) to stuff a keyword is cloaking; remove on sight. Never ship a different H1 for mobile vs desktop via responsive show/hide (Matt's own "website design in Hamilton" page fell #1 -> #7 with this cited as a contributing cause). [Part III 2.4; Part IV Heading Structure]
- Squarespace H1 size/style is globally template-locked (accept the large H1, keep the keyword in it). [Part IV Page-Builder]
- Diagnostics: Detailed SEO or Page Audit extension for live H1/H2/H3 structure ("Copy All Headings"); View Page Source + Ctrl/Cmd-F "h1" to locate an injected duplicate; a dedicated heading extension lists each H1 (one case found 13 from logo, signage graphics, animated elements). [Part III 2.4; Part IV Heading Structure]
- Blog posts: H2 and H3 only (the write prompt); "Let's do some H3 tags or something to break this up a bit." [Part II 4.3]
- The Golden Rule overrides all of this: 31 H1s on a page ranking #1 get left alone. [Part I 3]

### Word count
- No universal ideal. Google the exact keyword, check the actual top 3, match them or add ~100-200 words (~10%, "level plus one," "0.0001% more"). Real competitor pages for one keyword ranged ~500 to 2,500 words on the same SERP. [Part II 1.7; Part III 2.5]
- Anchors: program baseline 750-1,500 (later refined to 800-1,000); normal blog post floor ~500-800 (Part II: ~700-800); zero-volume/zero-difficulty ~400-500 is plenty; ceiling to watch ~2,000 per page; a homepage at 10,000 words (2,000 inside heading tags) is over-optimized; location pages 400-500 for low competition, up to ~2,000 if competitive; low-word-count audit floor 500+, agency target 1,000-1,500. Old Level-0 "~2,000 words correlates with #1-4" is superseded. [Part II 1.7; Part III 2.5; Part III 3.5; Part III 4.6]
- Over-optimization by length is a common live failure: trim, don't add. A 2,000-word page outranked a 3,200-word page when intent/format matched better; Matt's 600-800-word pages held #1 for 1-2 years. [Part I 3; Part III 2.5]
- Benchmark the lowest-ranked of the top 3 (if #3 ranks at 500, aim ~600, not 3,000). [Part III 4.4; Part VI 4.4]
- Measure body content only (exclude footer, nav, sidebar). Never trust one tool: extensions differ by hundreds of words (2,000 / 1,900 / 2,400; 808 vs 511 manual); inflation from popups, review widgets, mobile-duplicated text, currency selectors, injected hidden text. Verify by pasting visible text into wordcounter.net. Never trust an AI's self-reported count (2,200 -> ~1,700). [Part II 1.7; Part III 2.5; Part III 4.4]
- Longer should mean more complete, not padded; don't pad to match a bigger competitor whose length is filler. Cut generic brand copy an unrelated business could reuse verbatim. [Part III 2.5]
- Front-load: Google effectively evaluates roughly the first ~500 words. [Part V 7.3]
- Rewrite prompt sets "Word count is between: [comp low] - [comp high] words." [Part III 4.4]
- Accordions are acceptable to pad thin word count only where the expanded content is genuinely substantive. [Part IV Conversion elements]

### Keyword density and placement
- One keyword per page, always; a page can rank for many phrasings of that one intent; within-page cannibalization (3+ near-duplicate phrase variants like "indigenous art fly net hat," "mosquito net hat," "indigenous art protection print fly net hat") confuses the signal; commit to one primary phrase. [Part II 3.2; Part III 1.1]
- No fixed density target. "Use it three or four times and see what happens" as calibration, then match the actual #1 competitor's count (seen ranging from once to 27 times), "plus one." [Part II 1.7; Part III 2.6]
- Placement checklist: product/page name (= H1), title tag, meta description, first 100 words, naturally through the body, at least one H2, an FAQ, image alt text, image file name; as close to the front as possible in title, meta, H1. [Part III 2.6]
- Split the phrase into components (service + location) and count each separately across the top 3; feed into a spreadsheet; match the exact phrasing competitors use, not a synonym. [Part III 2.6]
- Red flag: density meaningfully higher than competitors' = over-optimized. Matt's page at 5.04% (keyword 35 times) vs. competitors' 1.76% and 0.9% correlated with #1 -> #9. "More keywords does not equal better rankings." [Part II 1.7; Part III 2.6; Part VI 4.2]
- Low-difficulty/local keywords often need only 2-3 mentions ("mechanic" top-3 on 3 mentions vs. 0 for competitors). Question posts: the literal question IS the keyword, ~3-4 natural uses. [Part III 2.6]
- Ignore Yoast/Rank Math density scoring for long-tail/question content; chasing a plugin's "use the keyword N times" can create over-optimization and cannibalization. Absurd readings (600%+, "923%") mean the keyword field was blank and the tool defaulted to the domain name. [Part II 1.7; Part III 2.6]
- Tools lump variants together ("35 uses" was ~5 literal + a variant); verify manually. [Part II 1.7]
- Don't copy a competitor's stuffing (they got away with it on a near-zero-competition term; copying risks a penalty for no benefit). [Part II Cross-Cutting; Part III 2.6]
- Singular vs plural: use whichever form the research shows; Google treats natural variations as equivalent; don't force an exact-match that sounds wrong aloud ("Tampa Bay Boat Rental Tampa"). [Part II 1.5]
- Secondary keywords: 5-10 per piece, only where natural; competitor brand names as secondary only. [Part II 1.6; Part II 2.6]
- Alt text: exact keyword on roughly half or fewer of a page's images. [Part III 2.8]
- Blog posts reference the exact money-page phrase at most once (near the bottom). [Part II 3.3]
- GBP service descriptions: city/keyword once per listing. [Part V 4.1]
- Money-page rewrite prompt: "Keyword density is similar to the competitors ... Does NOT keyword-stuff." [Part III 4.4]

### Readability
- Target 7th-8th grade: "If you can't explain it to a kid, you can't explain it"; if an eighth grader could understand it, you're good (the model for Matt's own book). [Part II 4.7; Part III 2.7]
- Paragraphs of 2-3 sentences; vary sentence length (drives the Flesch/ease score). [Part III 2.7]
- Avoid industry jargon that forces a reader to "open a dictionary" ("help desk" -> "how do I fix my computer"); cut framework references the reader won't recognize. [Part II 4.5; Part III 2.7]
- Simplifying widens the addressable audience, a wider ranking net, not just accessibility. [Part III 2.7]
- Don't chase an all-green Yoast/readability score ("not 100% accurate"); ignore transition-word, "key phrase in introduction," and density checks; Yoast flags >25% of sentences over 20 words (one case 30.6%): treat as a directional prompt to tighten run-ons. [Part III 2.7]
- Never right-align body text; minimize centered text; left-align mobile body text. [Part IV Web Design; Part IV Mobile]
- Body font never below 16px, ~1.8 line-height; no cursive/script for anything read quickly. [Part IV Typography and color]
- Lists, tables, explicit numbered steps on money pages; bullets only where useful on posts, never whole sections of bullets. [Part II 4.3; Part III 3.3]
- Strip AI tells (dividers, random bold, emojis, checkmark bullets, "Conclusion," "and finally," stray leading spaces). [Part II 4.5]
- Audit scores: 80%+ is fine, 90% "fantastic," never chase 100% ("Sometimes you need that D to help you rank"). [Part I 8; Part III 1.4]

### Images and alt text
- Density: roughly one image/video/chart every 200-300 words; minimum 4 per post, ideally one per H2; every post needs at least a featured image; never zero. Where an image doesn't fit, a heading break substitutes. Don't stuff photos; put excess photography on a gallery page. [Part II 4.8; Part III 2.8; Part IV Images]
- Sourcing: own real photos/screenshots (unique, unreplicable) > AI-generated ~ stock (Part II ranks AI above stock; Part IV calls them roughly equivalent after real photography). For graphs/infographics AI goes to the top ("they make really great graphics"). Never stock-looking imagery on a page meant to convey a real team/product. Stock/AI do not hurt SEO with proper alt text; the only concern is brand fit. Sources: Pexels/Unsplash free, Adobe Stock/Creative Market paid; keep a small provable set of licensed sources. AI-generated images are fine for ranking; AI-generated video is not. [Part II 4.6; Part II 4.8; Part III 2.8; Part IV Images]
- File names: rename the actual file before upload to a plain descriptive keyword phrase, 4-5 words (`black-flame-paddle-shirt.jpg`, `west-african-wedding-ceremony-toronto.jpg`, not `1234.jpg`); Google reads the file name as a signal distinct from alt text (a minor nudge, not a real lever). [Part II 4.8; Part III 2.8; Part IV Images]
- Format: WebP (or AVIF) at ~70% quality export (roughly 1/10th the file size of JPEG/PNG, "looks exactly the same"); fall back to compressed JPEG only where unsupported (Squarespace rejects AVIF, WebP version-dependent; Wix accepts WebP; GoHighLevel does NOT accept WebP for course/video uploads; Canva can't export WebP). Tools: WebP Converter for Media (preferred over the heavier Imagify), Squoosh, Photoshop batch/Save As WebP, Free Convert (~10/day), tinyjpg.com. Results: 537KB -> 32KB, 1.1MB -> 27KB, 1.9MB -> 102KB, 5.4MB PNG -> ~300KB. After converting, physically delete the old PNG/JPEG originals from the server. Bulk-convert existing sites with a plugin, never all at once; change one page and verify first. [Part II 4.8; Part IV Images]
- Sizing: under 1000px wide except banners; source under 2K resolution (downsize DSLR captures); compress anything over ~1MB before upload; hero ~1440x720 or 1400x740; half-width ~500-700px; body image ~750px wide by 400-500px tall; blog images ~750px wide, 16:9 or square, consistent sitewide; featured/OG 1200 x 628; GBP photos 1,000 x 1,000. No text baked into images. Check actual dimensions via right-click "open image in new tab." [Part II 4.8; Part III 2.8; Part IV Images; Part V 4.2]
- Alt text formula: identify the medium (photo/illustration/graphic/infographic) + be descriptive: "pancakes" (terrible) -> "blueberry pancakes" (thin) -> "stack of blueberry pancakes in a kitchen" (good) -> "illustration of a stack of blueberry pancakes in a kitchen" (best, if it really is an illustration). ~5-6 words. Every image needs alt text; none empty (screen-reader users first, then search, then fallback text; helps Google Image search). Proofread the string (missing spaces break it). [Part II 4.8; Part III 2.8; Part IV Images]
- Alt-text keyword rule: exact keyword only where natural and on at most half the images on a page; never the identical phrase sequentially across every image ("Newborn photographer Chicago 1/2/3/4"); keep each page's images focused on that page's one keyword; per-variant (round/cushion/pear/emerald, not all "diamond"). [Part II 4.8; Part III 2.8; Part IV Images]
- Prompt: upload the image and ask "give me an SEO friendly title in alt text for this image." [Part III 2.8]
- Lazy loading loads only near-viewport images; it can break images with attached effects/animations (test after enabling); Hey Tony's own production site runs with lazy loading fully disabled. Images popping in as you scroll is a good sign. [Part IV Images; Part IV Site Speed]
- Cross-device bug (images render locally but vanish in incognito/other devices): describe the symptom to an AI coding assistant; never batch-convert a whole site at once. [Part IV Images]
- Replace live Google Maps iframes with a static WebP screenshot linked to the real listing. [Part IV Images]
- Publish text-first and add images in a dedicated later block; Google picks up later-added images slower if it crawled first. [Part II 4.2; Part II 4.8]
- Featured image prompt (attach 2-4 refs): "Using the style of the images attached, create me a featured image for this blog post. Here is [topic] - you don't need any text on the image. Make sure not to include any of the exact images that are in these; make new ones in that style." [Part VI 1.7]
- Canva: never export a bare unmodified stock element; add something on top. [Part II 4.8]
- Image Alt Text Viewer audits every image + alt + file name on a page in one view. [Part III 4.7]
- GBP photos: batch ~10, then a week-to-month gap; geotag to the service location (disputed, low-cost). [Part V 4.2; Part V 4.4]

### Video
- Never self-host video; embed via YouTube or Vimeo even on a strong server ("even then YouTube is just better"). Google indexes one video per page; an embed still surfaces in search. YouTube embeds carry extra weight since Google owns YouTube. [Part III 2.9; Part V 5]
- Video breaks content into digestible sections and increases dwell time; Vimeo vs YouTube is a UX/aesthetics tradeoff, not a penalty. [Part III 2.9]
- Not required to rank. Weigh a hero autoplay video's appeal against page-speed and mobile cost ("is that video appealing to you, or is it appealing to a person looking to hire you?"); never an autoplaying hero video. [Part III 2.9; Part IV Conversion elements]
- Embed the matching video inside the corresponding blog post under an H2 like "How to Clean X - Video", only when the underlying video already performs; the video sits underneath the keyword-first post, not the reverse. [Part II 4.12; Part III 2.9]
- Blog -> video: feed a post to ChatGPT for a script, film it, post it; fine and not duplicate content as long as it adds different info and isn't AI-generated video (YouTube cracks down on AI video). [Part II 4.6; Part II 4.12]
- 30-second real clips of an actual team member on site beat faceless content; AI avatars capped ~12 views vs ~1,000-2,000 once the real person appeared. Transcripts (not just captions) get indexed/cited. [Part II 4.6; Part V 5]
- Embed Instagram posts / YouTube Shorts on blog pages to raise time-on-page; never an auto-pulling social widget. [Part V 5]
- Video counts toward the one-visual-per-200-300-words density. [Part II 4.8]
- GoHighLevel does not accept WebP for course/video uploads (use JPEG/PNG there). [Part IV Images]

### Internal linking
- "Internal links for the HeyTony site were the biggest factor and the biggest differentiator in why things were ranking really well." "The more internal links you build to a page, the more Google will understand this page is important." Go heavy: "4, 5, 6, just go insane with it." [Part III 2.11; Part IV Internal Linking]
- Evidence: HeyTony's SEO service page climbed position 13 -> #1 over ~3-4 years on internal links alone; Matt ranked a page #1 in 3 hours via internal linking (witnessed live); a member ranked a dormant page #1 for a competitive keyword using internal linking only. [Part III 2.11; Part IV Internal Linking]
- Rule 1 (outbound): every new blog post links out to 3-5 other blog posts + 1 money page (3 on a short post; 2-3 + 1 on a brand-new site; money page + homepage if nothing else exists). "Doing half of Google's work for them." [Part III 2.11; Part IV Internal Linking]
- Rule 2 (inbound, "the circle"): every time you publish, add a link from 3 different older, already-indexed posts into the new post; indexing "sometimes within an hour or two." "If you join a circle where everybody introduces you to the next person, everybody's going to know about you; if you're standing outside the circle saying 'I know those people over there,' you won't get invited in." [Part III 2.11; Part IV Internal Linking]
- Finder: `site:yourdomain.com "keyword"`, once pre-publish, once post-publish. [Part III 2.11]
- Anchor text must describe the destination page, ideally its exact primary keyword (or something close/natural); banned: "click here," "learn more," "here," "website," "get your copy here" (-> "get your copy of [book title] here"), the single word "most" (-> "the most common questions about pest control"). Vary anchors pointing at the same money page. Write a bridging sentence if no natural anchor exists. [Part III 2.11; Part IV Internal Linking]
- In-body contextual links, placed higher up, outperform a bottom/sidebar/footer "related posts" block (acceptable only as a fallback). Mix weighted toward inline. [Part III 2.11; Part IV Internal Linking]
- Direction: blog posts link TO money pages; money pages link OUT to blog and authoritative sources (at most 2-3 essential resources) and always include a convert CTA; every blog post should link to at least one location or service page; location pages cross-link to neighbors; pricing page <-> blog allowed; cap blog links from any one location/service page at 2-3. [Part III 2.11; Part IV Internal Linking]
- Ceiling: 10-20 links per page (some framing 5-10 at ~1,000 words); hard max 50-100 ("you'll actually get more out of doing less"); related-product blocks count. [Part III 2.11; Part IV Internal Linking]
- Use the CMS's existing-page link picker, never a pasted raw URL; internal links open in the same tab (UX call, zero SEO effect). [Part III 2.11; Part IV Internal Linking]
- Crawl depth <=3 clicks from homepage (0 = homepage, 1 = nav/homepage module, 2 = a specific post, 3 = a page linked from that post); 4+ = Google effectively ignores it. "If I can't get to it from your homepage, Google's not going to index it." [Part III 2.11; Part IV Crawl Depth]
- Orphan page = zero inbound links: fine only when deliberate (thank-you, ad landing, lead-magnet quizzes, job postings, internal-only) + no-index; anything you want ranked must never be orphaned; triage a large orphan count by picking the ~10 most important and adding 1-2 links each; a page can flag as orphan if its inbound links are `nofollow`. Dead-end page = zero outgoing links: target 3-5 outgoing per page. [Part III 4.6; Part IV Crawl Depth]
- New sites: publish first; at ~10-20 posts go back and add ~3 internal links per post (retroactive links work but take longer to show). [Part III 2.11]
- Automated interlinking plugins (Link Juicer) are fine but Matt avoids relying on them. Never build reciprocal cross-site exchanges or PBN "review trains" (the inbound-from-old-posts move is within one site and exactly what you want). [Part IV Internal Linking]
- Prompts: "Using my sitemap, give me three internal linking opportunities from this blog post [using existing text]." / "Anchor text, where to place it, give me a sentence where I can add this." / "I'm looking for 3 incoming internal linking opportunities to this service/product page: [LINK]. Find me 3 relevant opportunities from my sitemap pasted below. [PASTE SITEMAP]" [Part III 2.11]
- Fixes for "Discovered - currently not indexed" and "Crawled - currently not indexed": more internal links pointing at the page, publish content that links to it; don't resubmit manually. [Part IV Indexing]
- 30-day plan: add 3 internal links to that week's money page from other pages. [Part I 9]
- Post-migration, prioritize internal linking over immediate H1 cleanup. [Part IV Migrations]
- Reuse the GBP CID link inside posts/pages (a link for the search engine, not humans). [Part V 4.3]

### External linking
- At least 1 external link per page (blog: 1-2, at or near the top, within the first few paragraphs). Zero outbound reads as a crawl dead end: "when Google's crawl bots go from another site to yours, it stops there, it can't move on." Cite sources by hyperlinking the exact phrase to the study, not a separate references list. [Part III 2.12; Part IV Crawl Depth]
- "The number one rule with linking is never link to a competitor." Naming, praising, or comparing them in a table is fine; hyperlinking is not. [Part III 2.12]
- Never link out to a page targeting the same keyword you're trying to rank for; write the post first, then place external links to sources clearly unrelated to your own target keyword. [Part III 2.12]
- On money pages and the homepage, external-link to your own legitimacy profiles (Chamber of Commerce, Trustpilot, Glassdoor). [Part III 2.12]
- "Best-of" list technique: name every competitor, say positive things, never hyperlink any; internally link hard to your converting pages. [Part III 2.12; Part V 1.3]
- Nuance: strongest for blog content; Matt's core SEO service page has zero external links and ranks; his web-design page links out; check competitors' equivalent pages. Contact and About pages are exempt from linking minimums. [Part III 2.12]
- Add one external link to Sheridan's site when using the Big Five framework. [Part II 4.3]
- Never reciprocate links ("destroys the link equity you're building"); ABC linking is fine; never link to friends' sites in a mutual hub (link to members' social profiles instead). Never publish press-release copy on your own site (reciprocal pattern). [Part V 1.2; Part V 2.3]
- Guest posts on other sites: ONE link back, top half, specific/geo-qualified anchor ("clean comedian, Boca Raton"), plus a link to one of the host's own articles. [Part V 1.3]
- Social-media links to your own page "don't really count for much"; Reddit links are nofollow but still a positive mention. [Part IV Internal Linking; Part V 6]
- Broken external links: false-positive when the external site blocks crawlers (manually validate); real redirect -> update to the final URL; no replacement -> remove, or turn it into an internal link to your own content. [Part III 4.6; Part IV Crawl Depth]
- Link the logo itself on sponsor/charity pages, not just alt text. [Part V 1.3]

### Schema
- Deprioritized overall: schema was more important in the past, less so now; Matt runs no custom schema on his own site; it has NOT moved AI-Overview citation odds in his testing; his own analyzer found non-ranking pages had more schema than ranking ones (one site, unvalidated). Explicitly on the "skip the rest" list with FAQ schema, messy HTML, and "AI blocks." [Part I 2; Part II 4.7; Part IV Schema; Part V 7.2]
- "If you write good content, then that matters a lot more than just having a schema markup on the page." On-page content is the #1 lever, ranked above schema. [Part III 1.5; Part IV Governing Rules]
- Turn on Yoast's schema toggle: auto-generates standard/generic schema across every page type with zero setup, essentially free; enough for most businesses. Skip complicated custom schema. [Part II 4.7; Part IV Schema]
- Manual JSON-LD for anything specific (reviews, prices, FAQ): use any schema-markup generator, pick the type (Product, Article/Blog), fill fields (include the keyword in the description), copy the JSON-LD, paste it into the page's header (Rank Math header dropdown, a header field, or a plugin). Header placement is non-negotiable (loads before the page, same as an analytics script). [Part IV Schema]
- FAQ schema via AI: describe your on-page Q&A, ask it to generate the schema, paste into the code-injection block. Skipping FAQ schema carries no penalty; only worth the manual dev effort for high-competition keywords; after a year of testing "no more or less useful." [Part I 2; Part IV Schema]
- Schema is only penalized when the data is wrong or misleading (wrong hours = slight penalty; claiming "restaurant" when you're a PR firm = major penalty). Missing or incomplete but accurate fields are not penalized. [Part IV Schema; Part V 7.2]
- Local-business schema for a multi-city service area: main schema (matching the GBP) on the homepage listing every service-area city; a separate page-specific schema on each city page naming only that one city; a full separate schema per physical location/GBP. Don't publicly list a home address in schema for a remote business. [Part IV Schema; Part V 4.1]
- FAQ schema is double-edged: can drive real "Google's AI now recommends me" outcomes and can draw heavy AI/training-bot crawl traffic (100,000+ simultaneous bot hits; 150,000 visits/day vs ~40). Fix: block the bad bots (take the snippet to Claude and add a bad-bot rule) + better hosting (~$30/mo) + WAF; never strip the schema. [Part IV Schema; Part V 7.4]
- AI is optimizing to "pull the answer out and hand it back": extractability of the answer matters more than schema's presence. Don't build custom schema hoping for AI citation. [Part V 7.2; Part V 9]
- Detailed SEO extension shows OG/schema live. llms.txt is auto-generated by Yoast; not mandatory. [Part IV Title Tags; Part V 7.8; Part VI 1.4]
- Schema, geotagging, FAQ schema, and the reviews micro-site are all low-cost, outcome-based bets, not proven mechanisms. [Part VI 4.4]

### Speed / Core Web Vitals
- Causal chain: slow load -> higher bounce -> lower ranking. But page speed is deliberately the last thing to fix, only after content and keyword targeting are confirmed equal-or-better than competitors: "You gotta fix your pages first and then you can look at page speed after that." Speed's impact is relative (if everyone in a niche is equally slow it doesn't cost you; Matt has "seen slow websites outrank fast ones"); don't trust the "feels fast" proxy. [Part IV Site Speed; Part IV Weekly Audit-Fix]
- Core Web Vitals = "just think user experience." Cumulative Layout Shift (CLS) is the one members hit most: the page should render into its final structure immediately and hold, nothing loading in afterward that pushes content. Good bar: fast load, readable fonts, fast image load, zero layout shift. [Part IV Site Speed]
- Targets: mobile page-speed score 80%+ (check the Mobile tab separately at pagespeed.web.dev); WordPress plugins 15 or fewer; PHP 8.2 or higher; fonts 2 safe, more than 3 noticeably slows. [Part IV Quick Reference; Part IV Site Speed]
- Fix sequence (least to most disruptive): 1. audit and cut plugin count (remove unused ones, they still load); 2. caching plugin (WP Rocket ~$59/yr, CDN add-on ~$7-10/mo: File Optimization tab minify CSS, minify JS, delay JS execution; caching on; "Add missing image dimensions"; preload; Advanced Rules to exclude pages; if a toggle breaks JS-driven images/animations, un-toggle just that one and clear cache; alternatives SiteGround Speed Optimizer, LiteSpeed; one attendee ~20 -> 75 -> 100); 3. image compression to WebP (Imagify or WP Rocket's image add-on for bulk); 4. change the theme only if the above is not enough (forces a full visual rebuild); 5. ask Claude Code directly for advanced fixes. [Part IV Site Speed]
- Server levers: PHP 8.2+ (verify plugin compatibility first); enable OPcache, Redis, Memcached; re-test after each change; hosting execution limit default 30 seconds, triple to 90 if needed; delay specific long-rendering scripts from the PageSpeed report then re-test function (load order matters); self-host Google Fonts via the OMGF plugin; Cloudflare as a CDN to defer scripts, but never its one-click "block AI bots" toggle. [Part IV Site Speed]
- Shopify speed checklist: CDN set up; images served as WebP; image lazy loading enabled; CSS/JS deferred; if all four, speed "should be very, very good." [Part IV Site Speed]
- Platform ceilings: Squarespace (image optimization basically the only lever; "unused JS/CSS" unfixable; mobile score will likely never be high); GoHighLevel (CLS/Total Blocking Time typically unfixable); Kajabi (unused JS/CSS, large image payloads unfixable); Wix (no hosting-level access; contact Wix support; disable non-essential animations, especially mobile). [Part IV Site Speed]
- Image rules that drive speed: WebP ~70%, under 1000px wide, compress over ~1MB, delete old originals, lazy loading (test), static Maps screenshot instead of iframe; no review carousels (~1,000 words of markup), no Revolution Slider, no auto-pulling social widgets, no live Google-reviews plugin; sliders download every slide on every load. [Part III 3.4; Part IV Images; Part IV Conversion elements]
- Squarespace animated section reveals: cut timing roughly in half (Google's bot may miss unrendered content). [Part IV Page-Builder]
- Remove any `crawl-delay` directive in robots.txt (triggered a bot-challenge screen returning "only nine words"). Bot-blocking diagnostic: paste the URL into ChatGPT, Claude, and Google with "How many words are on this page?"; consistently far fewer words = the host is blocking bots. [Part IV Robots.txt; Part VI 1.7]
- AI-crawl floods: fix with cloud/VPS hosting (~$30/mo) + a WAF, never by blocking bots; "if bots are flooding you, feed them more (publish more), don't throttle." [Part V 7.4]
- PageSpeed Insights' "agentic browsing" score (out of 3: llms.txt, Web MCP, CLS, accessibility-tree order) does NOT currently affect ranking in AI Overviews or ChatGPT. [Part V 7.8]
- HTTPS everywhere; after a rebuild bulk-swap hardcoded `http://` with "Better Search and Replace" (back up first). [Part IV HTTPS]
- Audit-severity order: broken links and missing alt text outrank title-length/heading-count errors; page speed last; fix 5-10 issues/week. [Part III 4.1; Part IV Weekly Audit-Fix]

### Mobile / responsive
- Google has done mobile-first indexing since ~2016; visually cut-off or non-reflowing mobile content is a direct negative regardless of desktop quality (the original Space Jam site is the canonical unresponsive-legacy example). ~50-60% of traffic is mobile. [Part IV Mobile; Part IV Crawl Depth]
- A clean heading audit is not proof of responsiveness (independent axes): test by resizing the browser / the builder's device toggle / Chrome DevTools "toggle device toolbar" and watch whether content reflows vs. gets cut off or forces horizontal scroll (theatregym.co.uk passed headings, failed responsiveness). [Part IV Mobile; Part IV Site Speed]
- Build order: design the largest breakpoint (desktop) first, then step down through laptop, tablet, phone in sequence; never start from a mid-size/"square" breakpoint and hold it both ways. After finishing desktop, switch to the phone preview and manually rearrange if the auto-layout looks off. Squarespace and some platforms support only two breakpoints. [Part IV Mobile; Part IV Page-Builder]
- Mobile hero content order: Headline -> Copy -> CTA -> Photo, stacked strictly top to bottom; never a photo beside text on mobile; don't force a full desktop hero photo into a mobile background (place it below the text). Left-align mobile body text; keep side padding so nothing touches the screen edge. [Part IV Mobile]
- A desktop padding value can break mobile outright (a 255px side-padding trick exceeded an iPhone viewport; mobile needs ~50px). Font size is the one thing allowed to shrink slightly (17.5px desktop / 16px under a ~720px breakpoint); spacing/margins stay generous. [Part IV Mobile]
- Never duplicate a block for desktop and mobile (loads the same content and heading twice, duplicate H1s, reads as gaming): one truly responsive block with per-breakpoint design settings (different font size, image size, or background per breakpoint is fine; the text/heading must not be a second element). Never ship a different H1 for mobile vs desktop via show/hide. Claude Code prompt: "make this mobile friendly in the same blocks without duplicating the content." [Part III 2.4; Part IV Heading Structure]
- Phone tap targets: phone numbers and emails tap-to-call everywhere; anchor a labeled clickable number at the bottom of the screen (bottom beats top for thumb reach); an icon-only floating button with no visible number tanked call conversions. [Part III 3.4; Part IV Mobile]
- Mobile page-speed score target 80%+; check Mobile separately from Desktop; Wix: disable non-essential animations on mobile; Squarespace mobile score will likely never be high. [Part IV Site Speed]
- Overstuffed dropdowns / giant per-niche dropdowns are terrible on mobile; ~7-8 top-nav items. [Part IV Crawl Depth; Part IV Web Design]
- On a Shopify collection page put copy BELOW the product grid, "especially on mobile." [Part VI 3.2]
- Tools count mobile-duplicated text twice, inflating word count. [Part II 1.7; Part III 2.5]
- Rank Report Card scores mobile as a pass/fail factor. [Part III 4.7]
- Title tags over ~55-60 characters get cut off on mobile. [Part II 4.9]

### Typography
- One "spicy" heading font + one "boring" plain body font; the contrast creates hierarchy. More than 3 fonts noticeably slows the site; 2 is safe (extra important on Wix). Google Fonts is the default safe source; self-host them via OMGF for speed. [Part IV Typography and color; Part IV Site Speed]
- Font style does not matter for SEO directly; readability does. [Part IV Typography and color]
- Sizes: body never below 16px (16-20px working range, 20px standard); H1 ~48px start (60/64 used); H2 40px+; H3 32px; CTA 20px; body line-height ~1.8. Mobile may drop to 16px under a ~720px breakpoint from 17.5px desktop. [Part IV Quick Reference; Part IV Typography and color; Part IV Mobile]
- Avoid cursive/script for anything that must be read quickly ("any friction is friction"), including CTAs and pricing. [Part III 3.4; Part IV Typography and color]
- Never use a graphic/image as the H1: it must be live text (Google cannot read baked-in image text, and it does not scale responsively). [Part IV Typography and color]
- Heading styling never matters for SEO; the semantic tag does; an H1 can be styled smaller than an H2 (the "split H1" trick). Squarespace H1 size is globally template-locked (accept it); Squarespace font-size fields can render in REM/% (switch to pixels). [Part III 2.4; Part IV Heading Structure; Part IV Page-Builder]
- Never right-align body text; minimize centered text; left-align on mobile. [Part IV Web Design; Part IV Mobile]
- Paragraphs 2-3 sentences; 7th-8th grade; vary sentence length. [Part III 2.7]
- Never pure black on pure white (reads as "vibrating"); soft dark gray (`#191919`) on near-white. [Part IV Typography and color]
- Strip random bold, decorative arrows, emojis, checkmark bullets from AI drafts; no emojis in headings. [Part II 4.5]
- Paste Google-Docs copy into Elementor's code editor, not the visual one (hidden style tags); run WordPress Clear Formatting after pasting, then rebuild real lists; Divi: inline CSS with `!important` as the standing workaround. [Part II 4.5; Part IV Page-Builder]

### Color
- Complementary colors (opposite on the wheel) for maximum contrast on CTAs; analogous colors (adjacent) for cohesive backgrounds. Keep one color dominant and use the complementary color only as a small pop; never split a complementary pair 50/50 (mute the background, keep the CTA saturated). [Part IV Typography and color]
- One primary CTA in a solid, bold, single high-contrast color; secondary CTAs recede (outline/neutral); exactly one CTA color on landing pages; "When in doubt, make it black." If traffic is fine but form fills are low, the first lever is CTA button color/contrast. [Part III 3.4; Part IV Conversion elements; Part IV Web Design; Part IV Typography and color]
- Contrast self-check: mentally strip color and view in grayscale; if the text is not clearly readable there is not enough contrast (this manual test caught a failure an automated checker missed; real WCAG/lawsuit exposure). Midtone grays fail most often; gold text fails on white but passes on black. [Part IV Typography and color]
- Never pure black on pure white; use soft dark gray (`#191919`) on near-white. [Part IV Typography and color]
- Color-to-audience: clean blues = trust/B2B; pinks/pastels = playful/kids; muted greens/beiges = organic/natural; bold lime or red on dark = gym/fitness; gold on black = luxury. Source palettes by searching "[vibe] color palette" on Pinterest. [Part IV Typography and color]
- Corner radius as a brand dial: more rounded = friendlier (massage, baby photography), less = serious (cybersecurity, B2B). [Part IV Typography and color]
- Alternate background tints section-to-section so each section reads as distinct ("like a slide deck, one idea per slide"); duplicate a working section and swap the background color. [Part III 3.3; Part IV Web Design]
- Keep the exact same palette on interior pages (About) as the rest of the site. [Part IV Web Design]
- Wix accent-color swatches are capped at exactly 4 (plan the palette to fit); set Wix global Color Theme and Text Theme first on a new build. [Part IV Page-Builder]
- Hero star rating: 5 gold stars matching Google's color. [Part IV Conversion elements]
- Hidden text with font color matching the background is cloaking; remove on sight. [Part IV Heading Structure]

### Page builders
- "Google doesn't care about the platform you're using." Any platform can rank with unique URLs, a sitemap, and good content; WordPress just has the most SEO features and control (unrestricted custom code, no plugin ceiling, email/push), which is why agencies favor it. Don't platform-hop chasing a "gold standard"; migrating means redoing everything and risks a dip. Real blockers: WordPress.com (hosted blogging service; migrate to WordPress.org), SmugMug (templated image URLs canonicalized as duplicates), legacy gallery-only templates with no text/headings. [Part I 2; Part IV Page-Builder]
- WordPress: default stack WordPress + Avada ("the number one WordPress theme"); Elementor and Divi in active use; add plugins one at a time, <=15 total; exactly one SEO plugin; Rank Math's redirect manager can silently "accept" a 301 without applying it and its no-index toggle backdates a page if used long-term; Divi scatters styling controls (inline CSS with `!important`); Avada's Page Title Bar auto-generates an empty duplicate H1 (disable). [Part III 4.6; Part IV Heading Structure; Part IV Page-Builder]
- Elementor: the Heading widget (not a text element) locks the semantic tag (HTML Tag field); a shared Elementor template means canonical/heading fixes apply to every page built on it; clone a page via WP admin (Pages -> Clone) then update title + slug; paste Google-Docs copy into the code editor, not the visual one; Theme Builder single-post template (Post Content widget, Table of Contents widget anchors H2/H3 only; a second active single-post template throws a conflict error, remove the old Display Condition first; new templates apply retroactively); Yoast set to pull an excerpt overrides an Elementor meta description. [Part IV Page-Builder; Part IV Title Tags]
- Shopify: collection pages CAN rank (optimize like money pages), blog category pages basically never; H1 auto-placed in the logo; duplicate H1s injected by page-builder apps (GemPages), fix in `product.liquid`/`theme.liquid` via Edit Code with ChatGPT or Sidekick; Dawn appends the store name to titles; blog pagination 6 -> ~30 (60/100 later); URL-edit auto-redirect checkbox; native blog, skip third-party blogging apps; meta auto-pulls arbitrary text (EU safety copy) if unset; robots.txt over-blocking from third-party apps; speed checklist CDN/WebP/lazy load/defer; EN-CA locale duplicates via geolocation app settings; Yoast-for-Shopify plugin generates llms.txt. [Part III 2.2; Part IV Page-Builder; Part IV Robots.txt; Part IV Canonicals; Part V 7.8]
- Squarespace: H1 size/style globally template-locked (accept the large H1, keep the keyword in it); font-size fields in REM/% (switch to pixels); only two responsive breakpoints; category/tag archives editable only via code injection; animated section reveals are a crawl risk (cut timing roughly in half); image optimization is basically the only speed lever; rejects AVIF, WebP support version-dependent; HTTPS automatic. [Part IV Page-Builder; Part IV Images; Part IV HTTPS]
- Wix: accepts WebP; accent-color swatches capped at 4; no server/code access (online converter for images; Wix support for hosting-level speed); built-in background remover; template lock-in; new-build sequence: skip the AI/ADI wizard, Blank Template, set global Color Theme and Text Theme first (page transitions to None), add the Blog as an App (not a page), then build sections; Edit Text -> SEO and Accessibility -> HTML tag for heading tags; disable non-essential animations; fonts extra important (2). [Part IV Heading Structure; Part IV Page-Builder; Part IV Site Speed]
- GoHighLevel: pressing Return in an H1 field creates two H1s (use padding for the line break); developers mark every heading H1; sitemap not auto-surfaced (manually regenerate + resubmit after each post); Core Web Vitals largely unfixable; auto-creates two blog pages (delete the unused one); does NOT accept WebP for course/video uploads; fine for fundamentals but sacrifices CSS/speed control; not recommended unless tied to the CRM. [Part IV Images; Part IV Page-Builder; Part IV Sitemaps]
- Square: no true H1 field (hover image-description reads as alt text only). Kajabi: inflexible blog template, blog-index title as H1 above posts, oversized body H2 on the roll (inline span or CSS patch), unused JS/CSS unfixable. Showit: sitemap fetch failures (suspected platform limit), limited HTML control, separate sitemap from its WordPress blog (submit both); migrating off it to WordPress preserves authority if the domain stays. Ghost: clean image handling and alt-text support. GoDaddy builder: has failed to auto-generate a sitemap. [Part IV Page-Builder; Part IV Sitemaps]
- Builders in general: visual size and HTML tag are independent (always verify the actual tag); never fake headings with styled divs; never duplicate desktop/mobile blocks; duplicating a section and flipping image/text sides is the right reuse pattern; wireframe before building (optional). [Part IV Heading Structure; Part IV Web Design]
- Claude Code: describe your CMS/theme and ask it to build the page in that builder so the code pastes into your native editor; don't build a website directly on Claude Code as the platform; always back up before letting an AI touch theme/`functions.php`; it can write speed fixes, bot-blocking rules, CSS patches; its capacity estimates aren't reliable. [Part IV Page-Builder; Part VI 1.6]
- Platform-mechanics prompt for any CMS: "How do I add a link to a blog post or to another page on my site from highlighted words?" then name your platform; screenshot the screen/error, upload it, "Where do I click? What do I do?" + "Talk to me like I'm an idiot." [Part VI 1.7]
- Never run 2+ SEO plugins (duplicate titles/metas); if ALL OG issues fire sitewide, no SEO plugin is installed. [Part III 4.6; Part IV Title Tags]
- Robots.txt/sitemap are auto-generated by every major platform; if yours has no robots.txt "you need to switch your website builder." [Part IV Robots.txt; Part IV Sitemaps]
- Landing pages built off-domain (Netlify) convert but likely won't rank; reviews micro-site hosted on Railway/Netlify is the exception by design. [Part IV Page-Builder; Part V 7.6]

### AEO / answer-first structure
- "It's all just SEO. AEO is part of SEO." Rank on Google first; LLMs run a live Google/Bing search at answer time and synthesize from roughly 5-10 existing results. "If you rank on Google, you will get recommended by AI." Bing is ~4% of search but ChatGPT pulls from both. [Part I 1; Part V 7.1]
- Answer the target question immediately, at the very top: restate the question as a subheading, answer it plainly in the first paragraph, repeat the keyword/question near the top more than once. "There's no way to know how far they crawl on every page, which is why I put the answer right at the top." Models: "Do backlinks help ranking on Google? The answer is yes... however, it depends on which kind and how many." / "Yes, ChatGPT can help with SEO, but it can't do it on its own." Cut hedging ("the short answer is no"). Prompt: "The first paragraph should directly answer the question posed in the title / main keyword." [Part II 4.3; Part II 4.7; Part V 7.3]
- The "AI Markdown" three-extraction-point structure: 1. labeled TL;DR/Summary at the very top answering in 1-2 sentences an AI could clip verbatim (~100 words; only for longer content whose first paragraph doesn't already carry the answer); 2. restate the answer with more context in the opening paragraphs; 3. Key Takeaways at the end, 4-5 bullets reinforcing the same facts. Collapse redundant closers (no TL;DR + Conclusion + Key Takeaways + FAQ stack). Prefer "Key Takeaways" / "Key Summary" over "TL;DR." Test on only 2-3 pieces at a time. Results "mixed but leaning positive." [Part II 4.7; Part V 7.3]
- Front-load: Google effectively evaluates roughly the first ~500 words. [Part V 7.3]
- There is NO reliable correlation between ranking #1 and being cited in an AI Overview (same site cited ~30% of the time across three identical searches). Mechanism (100+-query study): Google's AI generates a claim/statistic first, then looks for content that supports it. Tactic, "back up the claim, then pivot": Google the query, read what the Overview asserts, state that claim first, then pivot with your differentiated info. Example: "The average kitchen renovation costs between $50 and $75,000 in [area]. However, we can do it for $25,000." Contradicting outright won't get you cited; a competitor who copied Matt's idea but aligned with Google's claims out-cited him in 5 days. [Part II 4.7; Part V 7.2]
- Broader AI levers: broaden mentions across as many different mediums as possible (press releases, social, Reddit; presence/volume over single-source authority); broaden geographic scope (full state/province); bake in time-relevance (include the current year, as models silently append it, e.g. Gemini appending "2026"); build a Reddit presence (mentions alone move AI Overview visibility). [Part V 6; Part V 7.2]
- FAQ blocks: plain Q-then-A text on the page, never behind an accordion; 3-4 max. [Part V 7.3]
- Schema is not the deciding factor; extractability is. Don't build custom schema for AI. [Part V 7.2]
- "Write for humans, not 'for AI.'" AI evaluates content by how valuable it is to humans; "framing content to please an AI is the wrong mental model." [Part V 7.3]
- Never block AI crawlers; no Cloudflare "block AI bots" toggle. [Part V 7.4]
- You cannot manipulate ChatGPT/Claude recommendations via your own private sessions; using multiple AI tools to draft doesn't improve external visibility. [Part V 7.1]
- Tracking: no tool can track AI visibility ("anybody selling AI visibility, they are making up terms"); AI referral traffic is trackable in GA4 ("session source" contains "chatgpt"/"claude"/"perplexity"; one dashboard +375% YoY); Bing Webmaster Tools "grounding queries" report; GSC "Generative AI" report (impressions only); manual check by Googling the query. [Part V 7.5]
- Reverse-engineer a citation: "what did you analyze to recommend these companies" / "what search terms did you search for." [Part II 4.3; Part V 7.7]
- Press releases get treated as "in the news" and AI descriptions have pulled language directly from a client's release; Amazon #1-bestseller badge + release reinforces a claim for AI answer engines; a ranking bump can last ~1 week. [Part V 2; Part V 2.3]
- Reviews and their text are a direct AI-recommendation lever ("automatically looks for the ones with the most reviews and the highest average star rating"); GBP has little pull on AI answers. [Part V 3; Part V 4]
- Cross-platform citation test: write a "who's the best [service] in [city]" post naming your business at #2/#3, post identical content to Facebook, X, LinkedIn (no hashtags), check `site:` indexing, force indexing via primeindexer.com (~7 days), recheck; comments are not pulled into AI systems. [Part V 7.5]
- CJ's launch sequence got an AI to name the business within 6 hours (placeholder post + landing page 2 months ahead, launch post, immediate backlink from the old post). [Part V 7.5]

### Patience windows after editing a page
- Re-edit a freshly published/updated page: wait ~1 month before touching it again. Freshness-gaming is real: Google sometimes deliberately suppresses ("tanks") a new/updated page, then waits days to see whether you panic-edit; that panic-editing itself reads as a spam signal. A dip within days or a week of an edit is expected noise. [Part I 4; Part II Cross-Cutting; Part IV Governing Rules; Part VI 4.1]
- Change one core element, then let it simmer; never batch changes to H1s, target keywords, or multiple pages at once; during a live Google core update touch one page at a time and check impact before the next. [Part I 4]
- Judging a change: small title/meta/H1 nudges ~2 weeks to 1 month; content-level changes ~2 to 3 months of productive waiting (keep publishing and internally linking to the changed page). [Part I 4]
- Money-page fix order: title tag -> meta description -> H1, then wait 1-2 weeks before touching on-page content further. [Part I 9; Part III 4.4]
- Non-ranking page: wait 3 months, then 6 months (internal-linking with descriptive anchor text meanwhile) before rewriting; after 6 months redo the full competitive audit and rework. [Part I 4; Part VI 4.1]
- Rank volatility after a legitimate change is normal (#7, then #9, then vanishing for over a week). Page 3 is not position 3; a member who kept re-optimizing after reaching page 3 fell out entirely ("you're probably doing too much"). [Part I 4]
- A drop after a publishing gap is not "Google punishing you"; resume cadence, don't edit the page. [Part I 4]
- Audit tools lag 12-24 hours (up to a week for Google-side reports) after a fix; an apparent dip right after a fix is usually caching. After a fix (alt text, etc.) wait roughly a month before re-checking. [Part III 4.1; Part IV Governing Rules; Part IV Indexing]
- Reverting a bad batch edit (town names jammed into broad posts) all at once is fine; give it 1-2 months. [Part VI 2.6]
- Check performance monthly, not daily: compare 28 days vs the previous 28 (never 7 vs 7); "You can look at it every day, but don't make actions on it every day." Cancel daily rank-alert tools. [Part I 2; Part IV Indexing]
- Indexing: new post ~2 hours to ~1 week (faster with reciprocal internal links); low-authority site up to ~2 months; brand-new site 2-3 weeks to ~2 months before Google crawls at all; don't request a recrawl on a page you are still editing; reviving a stuck post: change something, request indexing every 2-4 days. [Part I 5; Part IV Indexing]
- Timelines: 3-6 months minimum before a real traffic increase; inflection can land at month 12-14; ranking in 2 weeks is "magic"; brand-new site zero movement for 2 weeks to 2 months; new location page 3-6 months up to a year; Insiders report movement in ~1 to 1.5 months. [Part I 5; Part VI 2.2; Part VI 5.2]
- Refresh old posts every few months (update the date at minimum); edit in place, never republish as new. [Part I 7; Part II 3.3]
- Only test the AEO structure on 2-3 pieces at a time so you can attribute cause. [Part V 7.3]
- Swapping a sub-page in as the homepage: monitor for days/weeks and revert if rankings drop. [Part I 3]
- A PR-driven ranking bump can fade after ~1 week. [Part V 2]
- Set-and-forget expiration: re-audit only after a long-held #1 actually drops, never preemptively. [Part I 3]

### The don'ts list
- Don't edit a page that is ranking (#1-#3, or ranking for anything at all), "for the love of God"; UX/CTA polish is the only carve-out. [Part I 3; Part III 1.2; Part VI 4.1]
- Don't target two keywords on one page, or the same keyword on two pages; don't A/B test two pages for one keyword; don't target your homepage's keyword with a blog post. [Part II 3.3; Part III 1.1; Part III 2.13]
- Don't use "near me" / "near you" / zip codes as keywords, in copy, or in URLs. [Part II 2.5; Part III 2.3; Part VI 4.2]
- Don't keyword-stuff; don't exceed the #1 competitor's count beyond "plus one"; don't copy a competitor's stuffing. [Part III 2.6; Part VI 4.2]
- Don't use hidden text, a duplicate desktop/mobile H1 hack, hover-hidden keyword text, or an image as the H1; don't fake headings with styled divs; don't put emojis or the brand name in headings; don't skip heading levels going down. [Part II 4.5; Part III 2.4; Part IV Heading Structure; Part VI 4.2]
- Don't format a title as "[Post Title] - [Target Keyword]"; don't let a title render with a trailing "..."; don't strip a ranking keyword out of a title. [Part II 4.9; Part III 2.1]
- Don't change a URL that has any ranking, traffic, or backlinks; don't put a year in an evergreen URL; don't redirect a redirect; don't re-redirect back and forth; don't change an established domain to force a keyword in. [Part III 2.3; Part IV Migrations]
- Don't pad word count with fluff; don't trust a single tool's or an AI's word/density count; don't chase Yoast/Rank Math density or readability scores on question content. [Part II 1.7; Part III 2.5; Part III 2.7]
- Don't leave alt text empty; don't repeat the identical keyword alt text across every image; don't bake text into images; don't upload uncompressed >1MB images; don't export bare stock elements from Canva. [Part II 4.8; Part III 2.8]
- Don't self-host video; don't autoplay a hero video; don't publish AI-generated video. [Part II 4.6; Part III 2.9]
- Don't use "click here" / "learn more" anchors; don't paste raw URLs for internal links; don't exceed 10-20 internal links per page (hard max 50-100); don't link out to competitors or to pages targeting your own keyword; don't leave a page with zero outbound links; don't leave a page you want ranked orphaned or 4+ clicks deep. [Part III 2.11; Part III 2.12; Part IV Crawl Depth]
- Don't hide FAQ or important service content behind accordions/toggles/dropdowns; don't centralize all FAQs on one page; don't bolt 10 generic FAQs after the CTA; don't repeat identical FAQ text across pages. [Part III 2.10; Part IV Conversion elements]
- Don't use auto-rotating sliders/carousels as a hero, the Revolution Slider, review-carousel plugins, live Google-reviews plugins, auto-pulling social widgets, or live Google Maps iframes. [Part III 3.4; Part IV Conversion elements; Part IV Images; Part V 5]
- Don't run more than one CTA color/primary CTA per page; don't write bare "Learn more" / "Contact Us" / "Book Today" CTAs; don't call the pricing page "Investment"; don't use cursive for quick-read text; don't put two contact forms on one page. [Part III 3.4; Part IV Web Design]
- Don't put the logo twice in the header, don't let the header eat half the page, don't put more than ~7-8 items in the top nav, don't build giant per-niche dropdowns, don't rename "Blog" to "Learn Hub," don't nest location pages inside a service page. [Part IV Crawl Depth; Part IV Web Design; Part VI 2.2]
- Don't duplicate blocks for desktop/mobile; don't design from a mid-size breakpoint; don't place photos beside text on mobile; don't carry a 255px desktop padding to mobile; don't use more than 3 fonts or body text under 16px; don't use pure black on pure white; don't split complementary colors 50/50; don't right-align body text. [Part IV Mobile; Part IV Typography and color; Part IV Web Design]
- Don't show full post content on blog listing/category pages; don't use tags; don't use "Uncategorized"; don't create more than 5-10 categories; don't build `?taxonomy=` filter widgets; don't allow blog comments. [Part II 4.10; Part IV Canonicals; Part IV Web Design]
- Don't publish a raw transcript as a page; don't publish the same full content on your site and LinkedIn; don't republish a guest post on your own site; don't host press-release text on your own site; don't republish a post as new to "refresh" it. [Part II 3.3; Part II 4.12; Part V 1.3; Part V 2.3]
- Don't publish the first AI draft as-is; don't "humanize" or AI-detect your own writing; don't fully automate content/publishing; don't leave "Conclusion" / "and finally" / dividers / random bold / emojis in; don't put a "Key Takeaways" H2 on literally every post without judgment. [Part II 4.2; Part II 4.5; Part II 4.6; Part VI 4.2]
- Don't mass-dump posts on a live site (a dozen at once; ~500 pages/week got "retaliated" against); don't publish two posts the same day; don't ramp volume up then cut down; don't publish a "coming soon" placeholder. [Part I 7; Part II 4.11; Part VI 4.2]
- Don't build every location x service combo; don't template location pages with only the city swapped; don't jam a city name into broad how-to posts; don't combine cities or services on one page. [Part III 3.5; Part VI 2.2; Part VI 2.6]
- Don't build custom schema hoping for AI citation; don't ship wrong/misleading schema; don't strip FAQ schema that is earning visibility (block bad bots instead); don't block AI crawlers or use Cloudflare's "block AI bots" toggle; don't add `crawl-delay`; don't hand-edit robots.txt casually; don't hand-build or manually resubmit sitemaps; don't delete a sitemap; don't mash "Validate Fix." [Part IV Robots.txt; Part IV Schema; Part IV Sitemaps; Part V 7.4]
- Don't chase 100% on any audit tool; don't fix the whole audit at once (5-10/week); don't audit a site mid-construction; don't "fix" a flag without checking where the page ranks; don't act on daily rank noise. [Part I 8; Part III 1.4; Part III 4.1; Part IV Weekly Audit-Fix]
- Don't platform-hop chasing a "gold standard"; don't run 2+ SEO plugins; don't exceed 15 WordPress plugins; don't click "Apply All" on Google's recommended edits; don't build a whole site on Claude Code; don't let an AI touch theme files without a backup. [Part IV Page-Builder; Part IV Site Speed; Part V 4.1]
- Don't disavow backlinks, ever; don't reciprocate links or run PBNs/review trains; don't buy Fiverr/bulk links; don't say "backlink" to a non-SEO person; don't review-gate or ask for "5-star"; don't solicit reviews on-site while watched; don't fake a reviews cluster. [Part V 1.2; Part V 1.4; Part V 1.5; Part V 3]
- Don't treat a tool's AI-visibility score, GBP, or your own private AI chats as AI-answer levers; don't connect the reviews micro-site to GSC. [Part V 7.1; Part V 7.5; Part V 7.6; Part V 9]
- Don't let ChatGPT decide keyword/architecture calls ("ChatGPT will bullshit you"); don't trust its competitor guesses or its self-reported counts. [Part II Cross-Cutting; Part IV Governing Rules]
- The through-line: "if it seems like you're trying to game the system, don't do it. If it feels bad, if it feels sneaky, don't do it." [Part VI 4.3]
