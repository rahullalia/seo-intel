# Blog posts and the blog index

*Part of the HeyTony page-type research (`page-types/`). The rules every page inherits are in `00-rules-for-every-page.md`; the citation key, sources, and file map are in `README.md`.*

## What it is for and what it targets

- Blog posts are informational-intent pages, not built to convert directly. They exist for seven reasons: traffic and trust, internal-linking equity, unlocking harder keywords, organic backlinks, the "avalanche" compounding effect, consumer trust and recognition, and topical authority ("Google wants to see experts in a specific field") [course: power of blog posts; playbook II 4.1].
- "For most websites, blog posts are the primary driver of visitors. They're the front door." [book ch. 2] They also power the money pages: linking every post to one service page with keyword-rich anchor text got those pages ranking #1 a year later with zero edits to them [book ch. 2, ch. 9].
- A post's title is the literal question a real customer would type into Google, sourced from AnswerThePublic (pages 2-4), People Also Ask, Reddit, and client calls [calls 026, 065; playbook II 1.3, 4.2].
- One topic per post, matching the "every page is about one main topic" rule: a title like "could you be ruining your teeth with these five bad habits?" is cited as a bad, keywordless topic [course: one topic per page].
- The blog post's target keyword should never double as the money page's own primary keyword: the money page owns the buyer-intent phrase, and a post can reference it once near the bottom as a link back [playbook II 2.4, 3.3].
- Long-tail (4+ words) is favored; roughly 10 searches/month is acceptable; keyword difficulty 0-15 is ideal for a new site, up to 25 possible; a page-1 result with 0-2 referring domains is winnable without any backlinks [playbook II 1.1, 1.4].
- Low-volume math: 2 posts/week at about 50 searches each is roughly 400 potential searches/month, about 4,800/month after 12 months; authority to compete for harder terms opens up around the 6 to 9 month mark, the "avalanche technique" [book ch. 36].
- Evergreen beats dated: a 2023 HeyTony post has brought in over 82,000 visitors and just needs updating "now and then" [book ch. 3].
- Sometimes a post's only job is passing internal-link authority to a money page, or acting as a sales/support tool, not a ranking asset: Matt's "how to add and remove users from Meta Business Manager" post saved 20 to 60 minutes per onboarding call [playbook II 2.3, 4.12; calls 024, 087].
- The blog index itself is not built to rank: "we don't really need our blog role to be ranking... usually the post itself gets more traffic than the blog role." It exists so Google, and humans, can find every post [call 008; playbook IV Web Design].

## What goes on it, top to bottom (the structure)

- Single post, top of page: title, then a short featured snippet or excerpt, author, date, then a full-width featured image, then the body [call 008]. Byline: author name linked to an author page, date, and read time, a custom script that counts words, shown as "8 minute read" [calls 038, 030].
- Answer-first opening: the literal first sentence answers the question in the title, no hedging. Matt's rule of thumb: "can the first sentence be an answer to the question in the title tag." Cut "the short answer is no" in favor of a direct "No. Real estate agents cannot perform official appraisals in the Quad Cities." [calls 056, 094].
- Optional TL;DR / "Key Summary" block directly under the title, only for longer posts whose opening paragraph does not already carry the full answer: about 100 words, five bullets max, written so an AI Overview could lift it as-is. Call it "Key Summary" or "Key Takeaways," not "TL;DR" ("that is a Reddit term") [calls 099, 112; playbook II 4.3, 4.7].
- Table of contents: sits in a left sidebar (roughly a quarter width), pulling H2s only or H2 and H3, anchored or sticky. Never a large block sitting on top of the content itself, that "looks stupid" and reads "like a recipe website where you have to scroll through a bunch of bullshit" [calls 054, 080, 111].
- Body: one H1 (the title, with the keyword), H2 and H3 headings only in the generated draft [calls 122, 124; playbook II 4.3].
- Images every 200 to 300 words minimum, ideally one per H2 [calls 012, 048, 057, 111; course: images].
- Optional embedded video, hosted externally, placed under its own H2 such as "How to Clean X, Video" [calls 073, 124; playbook III 2.9].
- Key Takeaways block near the end: 4 to 5 bullets, worth doing "regardless of length" [calls 091, 099, 112; playbook II 4.7].
- Optional FAQ block at the very end: 3 to 4 questions max, plain H2 questions with plain-text answers, never an accordion [playbook II 4.7].
- CTA at the end, and optionally mid-post: a natural sentence, not a shouty heading, e.g. "we can help you with your content marketing, just contact us today" [calls 073, 081].
- Comments disabled sitewide [calls 013, 103, 111].

## Layout and design

- The fullest build on record is Leanne's Elementor template copying HeyTony's own layout [call 111]. Blog roll/archive: a hero with the blog name, an archive-posts widget, 2 to 4 columns (5 "looks very busy"), card title around 22px, a background color per card so posts do not visually blend, medium image resolution rather than large, and a configurable excerpt length with a per-post override.
- Single-post template, same source: two sections. Hero is two columns, featured image roughly one-third width on one side, title plus post-info (author, date, read time) on the other, plus an author box. Content is two columns: a sidebar half the width of the content column, next to the Post Content widget. HeyTony runs sidebar-left, content-right; a single long column also works [call 111].
- Sidebar contents: the table-of-contents widget (H2/H3 only, numbers switched to bullets), plus optional static items such as a phone number, hours, or a "shop with us after reading this" CTA [call 111].
- Featured image ratio: 16 by 9 is the standard, though HeyTony itself uses a square crop; the same image shows on the blog roll card and in the post hero [call 111].
- Typography (call 111): body copy starts at 16px minimum (10px is "too hard to read"); Leanne's build runs 18px, HeyTony's 20px; headings on Leanne's site run H1 48px, H2 36px, H3 26px, HeyTony's post-title H1 at 72px. A simple sans serif (Inter, Open Sans) covers most body copy; save personality for the headline font, where serif reads "classier."
- Huckberry reference numbers, a separate teardown (call 008): single column capped at 940 to 1,000px, body 17px desktop and 16px under 720px wide, line height 1.8, darker headline against gray body copy, near-white background.
- Spacing: use ems, not pixels, for padding so it scales on mobile; hero padding tested from 2em up to 4 to 6em top and bottom [call 111].
- One H1 per post, always: a theme or index that prints its own title as H1 above the post's real H1 must have that duplicate demoted to H2 or plain paragraph text [calls 008, 010]. Denroy's caveat: the styling does not matter, the H1 does not have to be the largest text, as long as the tags run in order [call 007].
- Make internal links visually obvious: underline them, bump link font weight to 700, or shift the color so they "pop" against body text [calls 010, 008, 103].

## Visuals

- Cadence: an image, chart, or embed every 200 to 300 words is the number repeated across nearly every source [calls 012, 048, 057, 111, 073; playbook II 4.8; book ch. 12].
- Minimum: at least a featured image on every post, plus roughly 3 to 4 in-body images per the internal checklist, or "at least four" per call 111, ideally one per H2.
- Source priority: your own real photos or screenshots first ("nobody else can make those real pictures"), then stock, then AI, except for graphs and infographics, where AI generation goes to the top of the list [calls 012, 017, 019, 048; playbook II 4.8].
- Featured image prompt pattern: upload 2 to 4 on-brand reference images and ask for a new image "using the style of the images attached," with no text or title baked in [calls 069, 112; playbook II 4.3, 4.8].
- Format: convert to WebP, compressed to roughly 70% quality (1.1MB down to 27KB, 537KB down to 32KB); GoHighLevel and some Squarespace/Wix setups reject WebP, fall back to compressed JPEG [calls 010, 030, 111, 112].
- Dimensions: in-body images around 750px wide; featured or OG image 1200 by 628px [calls 009, 067; playbook II 4.8].
- Alt text and file names: describe the image plainly, like a photo caption, not keyword-stuffed, and rename the file the same way before upload. Keyword in at most half a page's images, never sequentially, e.g. never "Newborn photographer Chicago 1, 2, 3, 4" [calls 002, 065, 069; playbook III 2.8].
- Embeds: your own Instagram posts and YouTube Shorts are fine and keep visitors on-page longer; avoid TikTok embeds, which force a sign-in; never upload video directly to WordPress or Wix, host on YouTube or Vimeo instead [calls 002, 064].
- Geotagging blog images is unnecessary, "that is more for your Google Business Profile" [calls 001, 066].

## Length, keyword density, and on-page SEO

- No single magic number: check the actual top 3 ranking pages for the target keyword and match or slightly exceed them individually, not combined [email 2025-07-03; book ch. 2, ch. 37].
- The 10% rule (Denroy): "aim to be 10% better than whoever is doing the most" among the top 3, so leaders at 800, 1,000, and 500 words become roughly 1,100, not a jump to 2,000-3,000, "we want to avoid over optimizing" [call 030].
- Program sweet spot: 750 to 1,500 words, Matt's standing guidance ("you don't really want to go over 1500"), with 1,000 to 1,200 words as "perfect" [calls 010, 012]; the internal checklist sets a 1,000-word floor, "equal to or more than the top 3 individual search results" [email 2025-07-03].
- For zero-competition long-tail keywords, length stops mattering: "I write 300 words and I rank" [call 120]; a 2,000-word page has even beaten a 3,200-word one on format fit alone [playbook II 1.7].
- Keyword density "plus one" rule: "if they say it 10 times, you say it 11" [call 030], echoed as "if your competitors are using the keyword 7 times, use it 8 times" [book ch. 37].
- On a pure question post, the question itself is the keyword and recurs naturally 3 to 4 times without deliberate insertion; ignore Yoast or Rank Math density tools built for short-tail keywords [calls 051, 065; playbook II 1.7, 4.7].
- Title: keyword near the front, 60 characters max, ideally around 55 before mobile truncation. Never append the city or service as a title suffix, e.g. never "Post Title, Chicago Newborn Photographer": "if it feels spammy, it probably is spammy" [calls 026, 070].
- Meta description: 120 to 156 characters, keyword near the front [email 2025-07-03]; generate about 5 with the prompt "write me a killer, compelling, click-worthy meta description" and pick the best [call 112].
- URL: the slug should be the core target keyword only, never the platform's long auto-generated slug, and flat off the root, e.g. heytony.ca/answering-question-keywords, not nested under about-us/news/slug [calls 026, 101]. Never date the URL of evergreen or annually-updated content [calls 049, 108, 110].
- Reading level 7th to 8th grade throughout. Heading rules: H2s carry the keyword in most, not necessarily all, of them; never skip a level; a normal target is one more H2 than the top competitor, 5 to 10 total [calls 002, 024; playbook II 4.3, III 2.4].
- Internal Content Checklist in full (email 2025-07-03): title under 60 characters, meta 120-156 characters, one H1, several H2s with the keyword in 2-3 of them, 1,000+ words matching the top 3, Yoast readability green, 3-4 internal links (one to a service or product page, favoring older pages), 1-2 external links to non-competitors, 3-4 webp images with keyword-aware alt text, keyword in the URL, a cannibalization check, a Google Business Profile link, and a sweep for punctuation, homophones, and stock AI phrases ("delve into," "enter a world of," "today's digital landscape," "a tapestry," "in conclusion," "in summary," "skyrocket").

## CTAs and conversion

- Blog posts are informational by default and usually are not meant to convert directly; a high-ranking post with weak conversion often just needs a business-relevant CTA added, not a rewrite into a sales page [playbook II 2.3].
- End-of-post CTA as a plain sentence, not a heading: "we can help you with your content marketing, just contact us today," rather than a section literally labeled "CTA" [calls 073, 081].
- Vary the CTA across posts instead of repeating the same pitch everywhere; agencies rotate to the same offer "every third or fourth post," mixing tools, lead magnets, and services [call 053].
- If a post already ranks well but converts poorly, move the actual conversion element higher on the page (a "file your lien today" button that was buried far down) and leave the ranking content untouched [call 081].
- Funnel logic inside the post: answer the top-of-funnel question first, then a contextual link deeper in, e.g. a post on "when was hot sauce invented" ending with "check out our hot sauces" [course: first blog post].
- Sidebar CTA option alongside the table of contents: a static block such as a phone number, hours, or "come shop with us after reading this blog post" [calls 111, 106].
- Local CTA line for broad how-to posts that are not location-specific: "if you're looking for a hairstylist in Denver," linked to the location or service page [call 095].
- A Google Business Profile link (the CID link) belongs inside posts "wherever you can insert the link naturally"; it passes authority and raises profile visibility [call 047; email 2025-07-03].
- Weaving your own offer into educational content is fine; the failure mode is bait-and-switch, not promotion itself [playbook II 4.5, 4.6].
- An in-content lead magnet between paragraphs can work well; a sidebar lead magnet is "not very effective," people have "banner blindness" to it [call 081; book ch. 46].

## Links, indexing, and where it sits in the site

- Outbound rule: every new post links to 3 to 5 other blog posts plus 1 money page ("two blog posts and one money page" as the floor for a brand-new site) [calls 001, 004, 022, 073, 096; playbook II 4.10].
- Inbound rule, "the half everyone skips": after publishing, link into the new post from 3 different, already-indexed older posts. This alone has gotten pages indexed within one to two hours, and one operator ranked #1 in three hours from internal linking alone [calls 001, 073, 099, 121].
- Finder technique: `site:yourdomain.com "keyword"` to find existing pages on the topic, before publishing for outbound targets and after for inbound ones [course: publishing; playbook III 2.11].
- Anchor text must describe the destination page, never "click here" or "learn more"; use the CMS's link picker, not a pasted URL, so links survive a slug change [calls 009, 058; playbook III, IV].
- Placement matters: links higher in the content "hold the heaviest weight"; in-text contextual links plus a bottom "you might also like" block is "the sweet spot" [calls 072, 050].
- External links: 1 to 2 per post to authoritative, non-competing sources near the top (government, Harvard, or MIT-tier sources "carry a lot of weight"). Never link a competitor, even an AI-suggested one, and never build a reciprocal link circle, it "destroys any link equity" [calls 002, 044, 054, 065, 071; playbook III 2.12].
- Categories versus tags: 5 to 10 categories sitewide, one per post (two max for a cross-cutting piece), never "Uncategorized"; wait until 10 to 20 posts exist before creating categories. Never use tags: each spawns a thin single-post page that wastes crawl budget without helping SEO; delete existing ones once Search Console confirms they aren't ranking or driving traffic, and noindex any tag/category archive you keep, "they don't provide any value" [multiple calls; playbook II 4.10, IV Quick Reference].
- Crawl depth and pagination: don't dump hundreds of posts on one paginated archive, every pagination click is a click deeper for Google; surface categories from the homepage, footer, or a mega menu so posts stay one or two clicks deep. Shopify's default of 6 posts/page is too low, raise it to about 30, then 60 to 100 as the blog grows [calls 015, 086; playbook IV Crawl Depth].
- Indexing: no need to request it if internal linking is solid; check back after two weeks to a month if a post still isn't indexed, then request indexing in Search Console. No indexing, no backlinks, and no traffic after months to a year makes it a drafting candidate, not a redirect or 404 candidate [calls 002, 009, 022; playbook II 4.10, IV Indexing].
- Update and Boost: Matt's own term for refreshing an older post rather than writing something new, meaning fresh stats, improved structure, and added internal links, paired with the rule that brand-new posts should chase "an easy-win keyword you'll actually rank for" [email 2025-12-04].
- Comments off sitewide: "the only thing you'll get on blogs is spam" [calls 013, 103, 111].

## Don'ts

- Don't skip the H1, and don't let a post render with two of them, whether from a duplicated blog-name header or a repeated title styled as a second H1 [calls 008, 010, 038, 094].
- Don't put the money keyword in a blog title unless the post is genuinely about that exact service, that's cannibalization; don't add the target city or a name-address-phone block to every post either, link to the money page instead [calls 004, 009].
- Don't run a finished post through a keyword-count tool and edit it to satisfy the tool, and don't publish placeholders, neither "coming soon" pages nor "(coming soon)" mentions inside a post [calls 001, 027].
- Don't paste an AI draft straight to the site unedited, and don't run it through a "humanizer" or AI-detector pass afterward; Google penalizes regurgitated generic content, not AI authorship [calls 022, 024, 026; playbook II 4.6].
- Before publishing, strip AI tells: horizontal rule dividers, random bolding, decorative arrows, emoji (especially in headings), checkmark or plain "1, 2, 3" numbering unless it's a genuine listicle, the stray leading space, generic "Conclusion"/"Final Thoughts" headers, "and finally," and self-promotional subheads in a pure answer post; em dashes are disputed, see below [calls 077, 108, 120, 122, 123; playbook II 4.5].
- Don't repeat one boilerplate "for more resources" link block verbatim across every post, that becomes duplicate content, and don't A/B test two posts targeting the same keyword or spin secondary keyword variations of one post into a second [calls 022, 026; playbook II 3.3].
- Don't use tags, on this point almost every source agrees without exception, and don't republish the same content verbatim on LinkedIn or Medium, or publish a raw podcast/video transcript as a post; never let a social platform become the "source of truth" copy [calls 004, 013, 065; playbook II 4.12].
- Don't obsess over one underperforming post: across six to eight posts a month, one or two typically carry most of the traffic, and that is normal [call 002].

## From the calls: live examples

- David, auto repair (Texas): three internal service links plus one authoritative external link per post; ranks #1 for long-tail queries like "Chevy Cruze transmission problems," and moved from around 7th or 8th to #1 in the map pack and #1 organic [calls 044, 061, 065].
- Matt's own voice-to-blog engine output: 1,500 words with title tag, meta description, internal linking, and FAQs generated automatically; he only tweaked the title and made the header image with ChatGPT, published essentially as-is, and it ranked [call 034].
- Chuck's Garage blog index review: social-share buttons ate the entire above-the-fold section so a visitor could not tell it was a blog page at all, on top of missing post images and duplicated meta descriptions across posts [call 027].
- The magician's "What magic tricks can I see on an iPad?" post repeated the same phrase three times running, title, giant graphic, first H2, "am I an idiot? Like, why are you telling me this three times?" [call 063].
- A dishwasher how-to guide at 2,500 words outranked a member's 697-word post on the same topic, using descriptive step headings instead of "Step 1, Step 2, Step 3" and screenshots pulled straight from an existing video [call 124].
- "Can I learn SEO on my own?" added a Key Takeaways block at the top and "hit Google Discover," 2,200 clicks in a few days [call 099].

## Where the sources are thin or disagree

- Word count has no consensus number: ranges run from "300 words is fine" for zero-competition long-tail, to a 750 to 1,500 sweet spot, to "1,500 to 2,000 words to compete," to a hard 1,000-word floor in the internal checklist. The one constant: check the actual top 3 and match or slightly beat them [calls 010, 012, 120, 030; email 2025-07-03].
- The TL;DR / "key takeaways at the top" block is explicitly unresolved even in Matt's own words: "mixed results, leaning more towards good than bad." Test it on 2 to 3 posts before rolling it out further [call 015; playbook V 7.3].
- Em dashes: the community consensus and Kira's checklist both treat them as an AI tell worth stripping, while Matt personally says "em dashes are fine" [calls 120, 122, 123; playbook II 4.5].
- Internal link count ranges from "two blog posts and one money page" as a floor, to "three to five plus one" as the norm, to Denroy's outlier position of "go crazy with internal links, 4, 5, 6, just go insane with it." Treat 3 to 5 out and 3 in as the median, not a hard ceiling or floor [calls 012, 073, 121].
- Schema on posts is inconsistent even within Matt's own practice: one call has him adding Article schema (type, URL, headline, image, description) [call 039], another has him saying he no longer bothers with schema because "their content was actually just better" than a competitor's that used review and product schema [call 094].
- Table of contents and SEO: treated as a user-experience nicety rather than a proven ranking factor. "I don't know if the table of contents actually improves SEO. It is useful for user experience so that could result in better SEO." [call 111]

