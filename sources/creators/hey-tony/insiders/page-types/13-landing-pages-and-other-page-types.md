# Landing pages and other page types

*Part of the HeyTony page-type research (`page-types/`). The rules every page inherits are in `00-rules-for-every-page.md`; the citation key, sources, and file map are in `README.md`.*

## Paid-ad landing pages

Intent and process:
- Ad clickers are high intent, "in the mood to buy," so the whole design goal is reducing friction: contact form and CTAs at the very top, no scrolling required to act. [call 016]
- Build order: copy first, then wireframe (Figma, grid paper, Canva, or Photoshop), then build. [call 016]

Hero and trust indicators:
- The hero leads with an image or a form; the CTA sits in "a color that stands out from the rest of the colors." [call 016]
- One dominant action only: "if we have several different decisions that they can make and they're all about equal value people will end up just not picking one," any secondary option is styled subtler. [call 016]
- Three trust indicators sit in the hero (years of experience, number of happy clients, licensed or insured, five-star reviews), "people are automatically hesitant... assuming everything is a scam." [call 016]

Full section order, every section carries its own CTA:
1. Hero: image or form, CTA, trust indicators
2. Why choose us, with a CTA
3. A reduce-anxiety callout, which also breaks up the layout
4. Services or offerings in a grid
5. Testimonials
6. Process steps ("remove uncertainty... clear steps of what's happening next"), with another CTA
7. FAQs, to handle objections
8. Final CTA, "our last chance"
9. Optional repeat of the hero's trust indicators
10. A response-time reassurance line: "I respond within 24 hours," "a real person will review this," or naming the actual person
[call 016]

Nav and footer removal:
- Remove the navigation, or cut it to a logo linking home, "not entirely trap them, but reduce people's distractions"; the nav's usual CTA button is dropped; footer slimmed down too. [call 016] [playbook IV]
- Caveat: a sales page stripped of all navigation wasn't converting and had its checkout page indexed by Google; Matt added the menu back, "a no-nav one-pager is not trusted and cannot rank." Reserve nav-stripping for pages that are genuinely ad-only traffic. [call 113]

Noindex and out of nav:
- Never list an ad landing page in the site nav: "exclusively for paid ads... I would never put this in the navigation... you probably don't want Google to index these pages." [call 016]
- An orphan-page audit flag is fine and expected "if you intended for that to be an orphan page." [call 016] [playbook III] [playbook IV]

CTA color contrast:
- Use color-wheel opposites deliberately: a red CTA blended into a brownish-red hero and converted poorly; a muted green background makes it pop, "not a bright green and a bright red because that'd be very jarring." [call 016]
- A too-busy hero (blurry background, overlaid images) hurt conversion; "a plain color background... less is more" reads as the safer default. [call 016]

FAQ placement:
- FAQs sit late, after testimonials and process steps, right before the close; on a landing page generally, keep FAQs to three or four questions at most. [call 016] [call 091]

Worked examples: a services business picks one offer ("I would pick one") and sells the benefit; an e-card company runs ads per occasion with about five samples shown; a campaign/event page states the dates up front, with a "reserve your spot" CTA repeated about halfway down, a countdown timer, and results shown. [call 016] [call 084]

## Funnel and high-ticket landing pages

Full section order:
1. Hero hook naming the problem ("frustrated, stuck, overwhelmed... we get it and we have a solution"), with a video or product picture
2. Empathize ("we've been there too")
3. Identify their challenges ("it's not you, you just need the skills")
4. How we help, in steps
5. What to expect / what's included
6. CTAs at every section, as jump links to the bottom form, a pop-up form, or straight to checkout ("buy now")
7. Success stories, video and screenshot testimonials in a slider
8. "Who is this good for," to filter leads
9. Meet the founder
10. FAQ
11. Emotional final CTA ("You don't have to figure this out alone") with a contact form
[call 016]

- Use this template for genuinely high-ticket offers ("a luxury car... or a course that's like a grand"); a moderate bundle isn't automatically high ticket, but nothing stops you from testing the format anyway. [call 016]

Hosting and checkout:
- Keep the sales/landing page on your own domain if ranking matters at all, "I would keep everything housed on your website"; checkout itself can live off-domain without hurting it, Rank Week's page ranks number one and checks out via SamCart. [call 051] [playbook IV] [call 031] [call 022]
- Ebook sold via Gumroad: the on-site page is the actual sales page (add a video testimonial on why you wrote it); every CTA points to Gumroad, which is just the checkout, the friction is the cost, not the flow. [call 016]

Worked example, a book sales page: liked hero image clearly describing the product, a "download it now" CTA, copy speaking to the target audience, all above the fold; to lengthen, add more testimonials, more of what people get, the author's own story, an FAQ, and a contact form at the bottom. [call 028]

## Thank-you pages

- Legitimate orphan pages by design: "They can't get to a thank you page just by clicking on your website. They have to input a form and then they get redirected." Noindex them; orphan and low-word-count flags are intentional and fine; robots.txt is a valid way to keep them, and checkout flows, out of the index. [course: orphaned-page-no-internal-links-point-to-it] [playbook III] [playbook IV] [book ch. 24]
- Content: thank you, what to expect on the call, optional further reading. [call 085]
- A campaign or webinar page and its confirmation page can both be drafted (unpublished) once the campaign ends, so "Google won't see it at all"; left live and unlinked they become "a bunch of unlinked orphan pages... that's unhealthy for your site." [call 050]

## 404 pages

- Nothing in the sources on the 404 page's own layout or copy, only on handling dead URLs; 404s sitting in Search Console don't hurt rankings by themselves, "what will hurt your ranking is if you are linking from content to 404s." [playbook IV] [call 082]
- Redirect general 404 URLs to the homepage, then click Validate in Search Console; clearing can take months and "you're not getting penalized for it" meanwhile. [call 015]
- Decision rule: nothing to replace it, let it 404; content moved to a new URL, 301 old to new; a permanently discontinued service, use 410; never 404 a product that might restock. Deleting genuinely dead pages (zero impressions, indexing, traffic, backlinks) is safe; the cautious version sets them to DRAFT instead. [playbook IV] [playbook VI]

## Sitemap pages

- The sources are almost entirely about the XML sitemap; multiple slices explicitly state, "HTML sitemap pages: nothing in this slice." [calls 022, 023, 024]
- Every site needs an XML sitemap at /sitemap.xml, auto-generated by WordPress, Wix, Squarespace, and Shopify: "do not make a sitemap yourself... you want to use a plugin." [course: do-you-have-a-sitemap]
- Submit it once in Search Console; it updates itself, never resubmit after normal publishing, the one exception is after a full site redesign. [call 013] [playbook IV]
- Submitting it is "the number one thing" for crawling and indexing; a one-page site's sitemap holding just one URL is part of why it can't rank. [calls 059, 061]
- A missing sitemap is catastrophic: clients who deleted theirs saw traffic "drop from hundreds of thousands to zero," and one GoDaddy site had none at all. [calls 116, 110, 113]
- Segmented sitemaps (posts, pages, categories, authors) are fine if each sub-sitemap path is submitted individually; Showit runs a sitemap separate from its WordPress blog, submit both; GoHighLevel sitemaps don't auto-update; Squarespace and Wix have each broken sitemap generation in practice (a slug rename once stopped Wix updating it). [calls 099, 013] [calls 102, 105]

## Careers pages

- Keep careers out of the main nav, move it to the footer or under an About dropdown: a therapy practice had "Career" in the main menu next to booking-focused items, "if you want them to book, why is there a career button?", moved under About. [call 058] [playbook IV] [call 096] [call 070]
- Exception: a real-estate school's state-mandated designations page and its continuing-education listing both stayed in the nav because each targets a distinct keyword. [call 003]

## Press and media pages

- Never publish the release text on your own site or link to it, "you don't want to do reciprocal linking" since the outlets already link to you, share on social and email instead; a "featured in" logo strip with no links is a fine, lightweight press page, but a "media" page of unrelated videos is "useless." [call 021] [call 029] [playbook V] [call 012] [call 042]
- Pricing runs from about $80 web-only (AB Newswire) up to a full human-reviewed service at about $1,500-2,000; a real AB-Newswire-style package (about $200 for two) landed coverage on AP News, USA Today, Benzinga, and the Globe and Mail. [playbook V] [call 124]
- One release covers one topic, one business, one location, one keyword; cap it at 1-2 releases a month, no real news required, and don't claim "best." [playbook V] [call 088]

## Resources, guides, and lead magnets

- Guide and ebook pages should lean on "free guide," "free resource," "free," "do it yourself," "DIY" language so you're not competing against bigger institutional players. [call 001]
- Gate a PDF lead magnet behind an email address, frame it as concrete value ("$100 of value, free"), follow with email automation; never repurpose someone else's PDF as your own. [call 005]
- The resource/guide page sells the service, the how-to blog post builds trust; break long cornerstone guides (around 5,000 words) into smaller posts, a repeated paragraph of "for more resources" links is not fine. [call 081] [call 024]
- Book's placement ranking: in-content between paragraphs works best when related to the post, a blog sidebar barely works ("banner blindness"), exit-intent pop-ups are most effective; economics: "give away what other people charge for," but "do not work for free or get into a discount race to the bottom." [book ch. 46]

## Alternatives and comparison pages

- A "[popular product] alternative/alternatives" page lists your own products; an "X vs. Y" comparison lives as a blog post, while a genuine product-comparison page (Botox vs. Dysport vs. Xeomin) is a valid consideration-stage page. [call 013] [playbook II] [playbook VI]
- A "best of" or "dupe" comparison page gets linked from the footer as a resource-style page, but never a sponsored/paid-ads page found on Google. [call 114] [call 122]
- Off-site reputation risk: a competitor's "my business vs. his business" page with false claims can rank for your brand name; options are cease-and-desist/trademark action, or out-publishing it with more content and a professional rebuttal. [call 003]

## Lead-magnet sites and standalone tools

- Matt builds standalone lead-magnet sites and tools (a backlink-gap tool, a topic-cluster analyzer, a rank report card) with Claude Code in about an hour, vibe-coded, mostly unbranded beyond a "brought to you by" line, driving thousands of signups. [calls 011, 020, 063, 064]
- A minimal one-page tool can outrank major competitors: LinkGap.io runs "35 words on this page. One heading, one tag. There's no meta description," no Search Console or Analytics, one backlink from heytony.ca, and ranks number 2 for "backlink gap" above Semrush, Moz, and Ahrefs, credited to browsing and conversion signals (roughly 15,000 email sign-ups). [call 051]
- Show the tool itself near the top, not below a wall of copy, "you have to scroll past a bunch of stuff... so you go back to Google," and add a path to purchase after the result; a good one becomes a traffic magnet by itself, an employment lawyer's severance calculator "brings in so much traffic... you look like the hero." [call 033] [call 063]

## Author pages

- Missing meta descriptions on author pages are "really non issues," fix an unfinished one only if it's actually getting traffic; paginated, feed, and author pages are ordinary Search Console noise ("duplicate without canonical," "blocked"), safe to ignore. [call 078] [call 013] [playbook IV]

## Taxonomy, tag, and archive pages

- Tag archive pages are treated as low-quality dead ends: delete and 301 them; keep category pages to a small number, missing meta descriptions on them are a non-issue. [call 121] [call 122] [call 103] [call 078]
- Public taxonomy/filter pages shouldn't exist as crawlable URLs: a directory's "0-2 years in practice" filter prompted "having a taxonomy page that is public, like that doesn't make sense"; keep the filter client-side instead. [call 017]

## Other page types mentioned

- Client portal or login (e.g., app.yourdomain.com): fine to run, walled off from rankings but can build authority through time-on-site and branded "login" searches. [call 005]
- Guest post pages, on someone else's site: title becomes the H1 and URL slug, exactly one link back using a money keyword as anchor, at least one internal link to a host-site article, CTA at the bottom; never republish the same piece on your own site, "you're just going to be competing with yourself." [calls 009, 006] [playbook V]
- Directory sites: fine to host, but every entry needs a real CTA, not just a member logo; quizzes "in most cases... probably aren't doing anything for you," drop them unless they demonstrably get traffic or convert. [call 061] [call 052]
- Chamber of Commerce profile page, on their site: ask for your logo and 2-3 links to specific service pages, not one generic "visit website" link. [call 052] [playbook V]
- Podcast and event/webinar pages: a podcast site needs just a homepage, booking, featured guests, and a sample playlist, an episode-page index is fine but won't rank, nobody searches individual episodes; a webinar landing page is conversion-only, "don't have links to anything else." [call 017] [call 065] [call 052]
- Seasonal pages: one evergreen URL without the year, updating only the title tag, meta description, and H1 each cycle; pull the nav link out of season. [call 069] [playbook VI]
- One-page websites: generally avoid them for anything meant to rank, since one page can't hold internal links or attract backlinks; a landing/sales page is the accepted exception. [call 096] [call 026]
- Bilingual pages: a second-language version can rank for the same keyword as the English page; use subfolders, not subdomains. [call 074] [playbook IV]
- Never publish a public "coming soon" page; avoid Linktree-style link-in-bio pages too, "link directly to the website or the page you want." [call 027] [call 121]
- Rename a generic "News" section to "Blog" unless the content is genuinely timely; the default content strategy stays evergreen. [call 101]

