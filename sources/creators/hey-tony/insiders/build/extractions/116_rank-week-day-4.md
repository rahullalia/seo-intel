# Rank Week Day 4 (Call 116)

Source: HeyTony Insiders Call Replay (hash: 92QbPmQMDp) | 97m 17s | ~16,178 words

## Tactics & step-by-step how-to

- **Core internal linking process (7 steps, done live on the call):**
  1. Find 5 "money pages" (your products/services) and list them in Column C of the shared spreadsheet.
  2. Locate your sitemap, usually at yourwebsite.com/sitemap.xml. If you can't find one, fix that first, Google needs it to discover your pages.
  3. Use the internal linking ChatGPT prompt (exact text below) to find 3 incoming link opportunities per money page: paste the prompt, replace the bracketed link with your money page URL, then paste your full sitemap content underneath (no need to clean it up first, paste it as is).
  4. Take the 3 URLs ChatGPT recommends and paste them into the column next to that money page.
  5. Go into each of those 3 pages on your live site and add a link back to the money page, using your own judgment: don't blindly copy the AI's suggestion, confirm the link makes contextual sense, and check you aren't already linking to that page from that post.
  6. Repeat for the remaining money pages.
  7. Repeat for as many additional money pages as you want, more is better ("internal linking = instant SEO momentum").
- **Sitemap troubleshooting:** if your sitemap is an index page (sitemap_index.xml, Matt's own has 10 sub-sitemaps), find the sub-sitemap specifically for blog posts (often labeled "post-sitemap.xml") and use that content for the prompt. WordPress with Yoast, Wix, and Shopify all auto-generate a sitemap; if you get a 404, something is broken and needs fixing.
- **Reusing the prompt for pages 2 through 5:** don't re-paste the sitemap each time. In the same ChatGPT thread, just say something like "use the sitemap previously provided" and give it the next money page link.
- **If ChatGPT's output is missing detail** (no reasoning, no anchor text, no example sentence), reprompt it directly: ask for "why it's a good fit," "suggested anchor text," and an "example sentence" for each of the 3 links.
- **Adding the link in the editor** (demoed live in WordPress): open the source page, highlight the anchor text, click Insert/Edit Link, paste the money page URL, hit Apply, then Update the page. Refresh to confirm the sentence and link landed.
- **Scope note:** this session covers internal linking only. External linking (e.g. linking out to a review site, referenced from Matt's Instagram content) and a separate, more involved GSC-based internal-linking method (also referenced from his YouTube content) were both explicitly named as different topics not covered today; today's method is described as "the easiest, quickest way to do this."
- **Local/service-area keyword structure** (for a business with no fixed location, just service areas): keep a consistent base keyword and vary only the location. Tier 1 = main city keyword; tier 2 = neighborhood keyword. Don't repeat the tier 1 wording on tier 2 pages, let the neighborhood name be the differentiator. Let keyword research (volume, difficulty) decide the exact variant.
- **Separating content types on WordPress** (for a manufacturer with news, blogs, and case studies): use custom post types, limit yourself to 2 to 3 custom post types total (e.g. one for case studies, one for services) and let the regular post type cover the blog; case studies specifically should be styled/treated as pages, not standard blog posts.
- **Shopify collection-page structure:** a sentence or two up top, then the product grid, then long paragraphs underneath (near blog-post length, with images) covering the collection in depth. Called "the biggest missed opportunity when I look at a Shopify store."
- **Accordion/dropdown content on product or collection pages:** don't hide genuinely important SEO content in a box, surface it directly on the page and work with the designer to make expanded content look good. Supplementary technical detail (e.g. product specs people actually click into) in an accordion is fine, it's not an absolute ban, just don't hide everything that matters.
- **Reverse-engineering a competitor's on-page pattern** when you're not ranking at all: if a competitor doing something unusual (e.g. two H1 tags on a page) is ranking number one, try copying that specific pattern since you have nothing to lose; keep the actual text/copy unique even if the structural approach matches.
- **Consolidating a bloated flat catalog during a site migration** (steel-product variants, roughly 1,000 near-duplicate pages): the specific option raised was a 302 redirect from every variant page down to 1 or 2 consolidated pages. Matt's guidance: keep any page that's already ranking or getting traffic exactly as is; for the rest, run keyword research to find which specific size/variant people actually search for and build individual pages only for those, using category pages/filters for everything else.
- **Deciding whether to delete old blog content:** check Google Search Console and Analytics. Not indexed, no traffic, no backlinks = safe to delete. If there are backlinks or the content still has reuse value (e.g. a recurring tour), keep it or update it instead of deleting.
- **Deciding whether to redirect a ranking blog post into a category page:** first check if that post's ranking is backlink-supported. If it is, expect to lose some backlink value on the redirect, it's a workable move, not a clean win.
- **Diagnosing inflated keyword density caused by on-page reviews:** when comparing your word count/keyword density against competitors, mentally exclude the review text from your own page (keep the reviews live for social proof and conversion, just don't count them in the density comparison). Note: running a review/product description through an AI tool (Grok, in this case) to shorten it for readability can unintentionally push keyword density even higher, check density again after any AI rewrite.
- **Deciding whether near-identical "bundle" pages of the same core product should stay separate:** run keyword research per bundle. Keep them separate if the search intent differs page to page; merge them if it doesn't.
- **Backlink building for a business with no walk-in storefront:** join your local chamber of commerce or business groups (often hands you a backlink), get listed in local directories, and set up a Google Business Profile even without foot traffic.
- **"Why doesn't this rank" review** (Matt's own recurring Friday process, also run inside Insiders): for an underperforming page, walk through keyword research, backlink quality (is it trash or real?), and whether the URL itself is worth keeping versus redirecting.

## Rules / dos & don'ts (keep every threshold, number, specific)

- Start with 5 money pages; find 3 incoming internal link opportunities per money page as the baseline.
- Sitemap convention: yourwebsite.com/sitemap.xml. If you don't have one or can't find it, fix that immediately, it's how Google discovers your pages.
- Don't blindly copy/paste AI's link suggestions, verify contextual fit yourself first.
- Before adding a link, check you aren't already linking to that target page from that same source page, no point linking to the same page twice from one post.
- Vary anchor text across links pointing at the same money page (Matt's own example set: "our SEO services," "done for you SEO services," "professional SEO services"). Repeating the exact same anchor/keyword every time reads as manipulation to Google.
- Don't copy a competitor's blog content to link it to your own pages. Google already indexed it under them, so you get flagged as duplicate content and it can hurt your site; it likely won't hurt theirs since they posted first.
- Automated internal-linking plugins (named: Internal Linking Juicer) are fine to use ("you absolutely can"), but Matt avoids relying on them in his own work: there's no human judgment behind the automation, so it can add a redundant link to a page that's already linked for that same keyword.
- Blog cadence: 1 to 2 posts per week. Consistency matters more than volume, Google likes to see a site updated on a consistent basis.
- Do not mass-produce blog posts: "I don't want to see anybody posting 100 blog posts that are all written by AI," it won't help you rank. Slow is the stated pace for SEO generally.
- Don't build a keyword/location page for every possible service times city combination (a roughly 200-page plan for 2 HVAC clients was flagged as overreach). Pick one keyword per location instead, chosen by keyword research and by which service is actually worth the most per job.
- No acceptable percentage of duplicate content across near-identical service pages, the bar given was "100 original."
- Never target the same keyword on more than one page (stated flatly to two different attendees, this is cannibalization).
- Internal links can run blog to money page or money page to money page when contextually relevant (e.g. a web design page mentioning SEO services too), but don't force an irrelevant link (an Instagram-ads page shouldn't pitch a new website).
- Blog posts must be visible: have a dedicated Blog page and a nav menu link to it. If Google or a visitor can't find the posts, neither will care about them.
- Link count per blog post: 5 to 10 links is fine at roughly 1,000+ words.
- You cannot outrank sponsored/Google Ads placements organically, those are paid.
- Go after low-volume keywords (0, 10, 20 monthly searches) rather than only chasing high-volume terms, they're winnable and still convert.
- Priority order when you don't know what to fix: helpful content first (can't optimize what doesn't exist), then internal linking as you write (this takes care of itself if done concurrently), then backlinks.
- A single relevant backlink to a specific underperforming page can push it over the edge, even with a large sitewide backlink count already in place (roughly 700 backlinks cited in one case), it's about relevance to that exact page, not aggregate count.
- Backlinks: links from your own country are best; links from other English-speaking countries (US, Canada, UK) are fine too.
- Don't let SEO dictate every page. Pages that exist purely for ads/email traffic (landing pages) don't need optimizing and can duplicate content, as long as they don't compete keyword-wise with a page you actually want to rank (Matt ran 6 versions of the same Rank Week landing page, one per traffic source, with zero SEO concern).
- On Shopify, paying monthly for Yoast is unnecessary if you're already manually setting title tag and meta description yourself.
- Ranking higher on Google also raises your odds of surfacing in ChatGPT, Perplexity, and similar AI answer engines, treated as a direct byproduct of the same internal-linking and authority work, not a separate task.

## Tools, prompts & resources (exact prompt wording if quoted; tool names; settings)

- **Internal linking ChatGPT prompt (verbatim):**
  "I'm looking for 3 incoming internal linking opportunities to this service/product page: [LINK TO PAGE IN COLUMN C]
  Find me 3 relevant opportunities from my sitemap pasted below.
  [PASTE SITEMAP]"
- **Reprompt add-on** if the output lacks detail: ask ChatGPT to also provide, per link, why it's a good fit, suggested anchor text, and an example sentence to insert.
- **Shared Google Sheet template**: use the "make a copy" link, not a request-access link (an explicit fix after a prior day's access-request pileup). Column C holds the 5 money pages; the adjacent column holds the 3 recommended incoming-link URLs per page; rows are grouped/color-coded in sets of 3. An Excel version was also offered for anyone who wants to upload it into Google Sheets themselves.
- **ChatGPT tier**: if pasting the full sitemap triggers an "input too large" error, you need a paid ChatGPT plan (the roughly $20/month tier is enough).
- **Keyword research tools**, in Matt's own order of preference: **SEMrush** (his current go-to; flagged that Adobe just acquired SEMrush, so its status as his go-to tool in 2 to 5 years is uncertain); **Ahrefs** ("also really good," direct competitor and industry top leader); **Ubersuggest** (cheapest option, by Neil Patel, weaker stats but "a thousand times better than doing nothing" if it's all a business can afford).
- **Yoast SEO**: on Shopify it's a paid monthly add-on, called "super annoying" to pay for and unnecessary if you're manually handling title tag and meta description.
- **Rank Math**: Matt "likes aspects of" it but doesn't run its automation.
- **Internal Linking Juicer** (WordPress plugin): named specifically as the automated internal-linking plugin discussed; usable, but not what Matt relies on himself.
- **Google Search Console + Google Analytics**: used to decide whether to delete or update old blog posts (check indexing status, traffic, and backlink presence).
- **"Why doesn't this rank" session**: Matt's own recurring Friday review, also run for Insiders members, examining keyword research, backlink quality, and whether a URL is worth keeping.
- **HeyTony Insiders program**: $57/month, one single plan, no trial period, no commitment, cancel anytime; includes recurring weekly calls plus the Friday "why doesn't this rank" session. **Denroy** named as the resident local SEO and technical SEO expert running dedicated calls (credited by name for helping one attendee, Victor, move up in the map pack).
- **Matt's own agency pricing**, disclosed as an ROI anchor for the $57/month pitch: he charges **$2,500/month**; landing one client from the Insiders more than covers a full year of membership.
- **Today's signup bonus**: ebook pre-release of Matt's book (also referred to in the call as "Tuesday's bonus"). Yesterday's bonus, a list of "10 blog posts every website should have," is also available to same-day signups; anyone who signed up on Day One (Sunday) gets all bonuses stacked.
- **support@heytony.ca**: contact for replay access or missed follow-up emails.
- **Recording turnaround**: uploaded roughly within an hour of the call ending; general replay access stated as available until December 17, permanently available inside HeyTony Insiders.
- **Live YouTube Shorts experiment**: Matt posted a Short link mid-call and asked attendees to watch, like, and comment simultaneously to observe real-time analytics movement, a repeat of an earlier experiment where he tried getting many people to comment the same target keyword on a post to see if it would rank number one on Google for that term.

## Case studies / examples / results (names, niches, numbers)

- **Matt's own site**: sitemap_index.xml with 10 sub-sitemaps; the specific sitemap referenced live contained 331 URLs. Money page = "web design in Hamilton." ChatGPT recommended linking from his "ways to improve user experience" blog post (among others), suggesting anchor text "Professional web design in Hamilton" and "Hamilton Website Design Agency."
- **Live YouTube Shorts test**: video views jumped to roughly 2,000 and gained 31 subscribers within the call after Matt sent waiting-room attendees (described as "3, 4, 500" people) to watch/like/comment; views were noted as trailing off again by the end of the session.
- **Victor** (moving company, Insider for about 6 months): applying Denroy's local SEO guidance pushed his business to number 1 in the map pack for a period; since settled to roughly top 3 or 4.
- **Coach D** (car recycling business, service areas only, no physical location, site still in progress): worked example of 1 main city plus 3 neighborhoods per city, up to 21 total location/keyword variants, using a stable keyword root (e.g. "we buy junk cars," "sell my car fast") with the neighborhood as the only variable, not full-keyword duplication.
- **Unnamed moving-company prospect** (separate attendee): example money-page keyword ideas discussed: "home furniture movers," "home appliance movers," "apartment movers," possibly a city-to-city long-tail like "moving from New York to Washington."
- **Mike K** (wire and cable manufacturer, thousands of products): uses WordPress custom post types to separate news, blog, and case studies; case studies recommended as standalone pages rather than posts.
- **Kirill** (Wix agency, personally close to 100 sites built; migrating a steel-products client): client currently has roughly 1,000 near-duplicate variant pages (e.g. 8"x8", 9"x9" steel pieces like corner guards and kick plates) causing customer confusion; considered a bulk 302 redirect of all variants into 1 to 2 pages; advised instead to preserve ranking/traffic pages as is and use keyword research to decide which size variants deserve their own page going forward.
- **Sean / Shanji** (agency, HVAC vertical, 2 clients, considering a service times city matrix of about 200 pages): redirected to pick one keyword per city instead, prioritized by per-job value (one service earns about $350 per job versus another at about $100 per job, focus location pages on the $350 service).
- **Gurab** (B2B/ecommerce SEO, about 4 years of experience): raised the accordion/"read more" pattern on collection and product pages; told to surface important content directly instead of hiding it in a box.
- **Teal** (new to Shopify, prior WordPress background): collection-page content strategy (intro sentence, products, then blog-length paragraphs with images) called the single biggest missed opportunity Matt sees on Shopify stores; also runs accordions on technical product pages, judged acceptable since people actually use them; considered adapting location pages to a product-based interior-design business, called "tough to migrate" either way.
- **Map** (Shopify services/store-builder business, name as transcribed): every keyword variation tested came back with search volume around 0, 10, or 20 monthly searches across Answer the Public, Ubersuggest, and SEMrush; reframed by Matt as the desired outcome rather than a problem, since low-competition terms convert once someone finds them and becomes "the obvious result."
- **Catherine** (silk nightwear reseller): ranks number 10 for a target keyword via a blog post rather than her category page; the rest of page 1 is other resellers'/brands' product pages; a paid backlink service she used previously suggests the ranking blog post carries real backlink equity, complicating a straight redirect to the category page.
- **Stephanie** (golf accessories business, about 11 months old): flagship product, a golf cart seat towel, sits on page 5 of Google Shopping; her category is premium and competitors don't blog, framed as a wide-open content gap. Suggested blog angles: best towel materials/absorbency; plus organic social video showing the product solving the "wet seat" problem.
- **Wendy** (large UK county tourism/events site): "what's on" content plus a "features" blog category; example cited: 36 pantomime-show blog posts, each linking back to one central business page; confirmed 5 to 10 links per post is fine at that length.
- **Jordan Moses** (travel agency, Alaska tour packages with rotating "headliner" acts): advised to link Alaska-themed blog posts to a master "all Alaska events" hub page rather than to individual headliner pages, since headliners change often and per-headliner links would require constant upkeep.
- **Jimbo** (national park tour company): historically relied on paid Google Ads rather than SEO; old (2023) blog posts are essentially photo dumps (a couple of sentences plus about 10 images); plan is to check Search Console (indexing, traffic, backlinks) and likely retire those in favor of a properly built new post library.
- **mj** (Calgary, hosts WordPress via GoHighLevel): page speed flagged as the likely issue, attributed to unoptimized images.
- **Andreas**: keyword-density audit tool was reading inflated numbers because 15 to 20 customer reviews sit below the product description; used Grok to shorten the long description for readability, which pushed density even higher rather than solving it. Fix: manually exclude review text when comparing word count/density against competitors rather than removing the reviews (kept for conversion value). Separately, has 3 "bundle" pages of what is functionally the same core product framed for different buyers; told to run keyword research per bundle and keep them separate only if intent differs.
- **Umair Umar** (custom T-shirt printing business, UK, warehouse-based, no walk-in storefront): backlink plan = chamber of commerce/business-group memberships, local directory listings, and a Google Business Profile despite no foot traffic (Matt's own home-address GBP anecdote: no unwanted visitors in years running it that way). Also asked about copying a competitor's duplicate-H1-tag pattern since that competitor outranks him; Matt confirmed it's worth testing given nothing to lose, as long as the text itself stays unique.
- **Sanjay**: asked about copying a competitor's blog outright and linking it into his own sitemap; told not to, it flags as duplicate content on his own site since Google already indexed the original under the competitor.
- **Tim Donahue**: roughly 700 backlinks per SEMrush but mostly from low Domain Authority sites; stuck around position 3 to 5 for a target keyword despite strong content and internal linking; advised that 1 to 2 well-targeted backlinks to that specific page, not more generic sitewide link volume, could be the missing push.
- **Ashley / Eric and Jess** (attended with a baby on camera): blog posts were not visible on the live site; fix confirmed as needing a dedicated Blog page plus a nav menu link, since neither Google nor visitors can find posts otherwise, regardless of internal linking.

## Notable verbatim quotes (only memorable/strategic ones)

- "Internal linking = instant SEO momentum."
- "I was going to call this internal linking on crack."
- "It's like running in shoes without shoelaces... We want everything to be together... and we want people to be able to get where they're going."
- "What is the percentage of originality that I can get away with without getting dinged as a duplicate page? You need 100 original, my friend."
- "This is what my old accountant used to tell me: pigs get fat and hogs get slaughtered." (on building roughly 200 thin service times city pages instead of a focused set)
- "Slow is the name of the game... when it comes to SEO here."
- "This is the best time in human history to be a business owner. SEO is free... You can pull out your phone, you can record yourself talking about your product or service and press send."
- "Google, ChatGPT, they're looking at you as a whole now and not just what's happening on your website... They want to know that you are the authority, that you are the best option for their user."
- "My whole outlook on automated SEO is that there's no human brain behind it."
- "Well, if this information is so important, why is it hidden in a box?" (on burying key content in accordions)
- "Doing it this way is the most overlooked SEO strategy."
- "SEO is a long game. I don't want this to become your entire life... I don't want you to be an SEO expert."

## Tradeoffs & nuance

- AI/automation speeds up finding link opportunities but has no judgment: it can suggest a link that's contextually off, or duplicate a link to a page that's already linked from that same keyword, human review before publishing stays mandatory.
- Anchor text needs variation, not exact-match repetition, to look natural; over-optimizing the same keyword on every link risks looking like manipulation to Google.
- Blog volume versus quality: 1 to 2 posts a week beats a burst of AI-mass-produced posts; consistency signals to Google outweigh raw count, and 100 AI-written posts at once was explicitly rejected as a strategy.
- Expanding location/service pages is a tradeoff between more ranking surface and thin-content risk: more pages can mean more chances to rank, but padding out a service times city matrix without keyword-research backing risks looking like gaming the system and can hurt the whole site; letting actual search volume and per-job value gate which pages get built is the stated resolution.
- Redirecting a ranking blog post into a category page can consolidate authority onto the page you actually want to rank, but risks losing some backlink equity in the move, framed as "a way to do it," not necessarily "the right way."
- Reviews help conversion and trust but distort keyword-density tooling, and running AI over a product description to fix one problem (readability) can quietly worsen the other (density); the fix is adjusting how you measure and re-checking after any AI edit, not stripping the reviews.
- Deleting old content: safe to delete if Search Console shows no indexing, no traffic, and no backlinks; keep or update if any of those exist, or if the underlying content (e.g. a recurring tour) still has reuse value. Content age or writing quality alone isn't the deciding factor.
- Not every page needs to compete for rankings: ad-traffic and email-traffic landing pages can duplicate content and skip optimization entirely, as long as they don't cannibalize a keyword you actually want a different page to rank for.
- On multi-channel strategy, Matt frames the next 5-plus years as an omnichannel signal game (social, YouTube, email, ads, and SEO all feeding how Google and LLMs judge authority) rather than any single channel winning alone, flagged by Matt himself as a take that "might upset some people," i.e. his opinion, not a settled fact.
- Hiding content in accordions/dropdowns is discouraged for genuinely important SEO content, but treated as fine for supplementary technical detail that a real subset of users actually opens; this is a judgment call per page, not a blanket rule.
- Reverse-engineering a competitor's exact on-page structure (duplicate H1s, etc.) is framed as a reasonable experiment only when you have "nothing to lose" (i.e. you're not ranking anyway); Matt is explicit that he isn't "the end all be all" on strategy and treats this as testing, not doctrine.
- Automated internal-linking plugins are not forbidden ("you absolutely can" use one), but Matt's own practice avoids them, a case of an acceptable shortcut he personally still chooses to skip in favor of manual judgment.
