# Rules that apply to every page

*Part of the HeyTony page-type research (`page-types/`). The rules every page inherits are in `00-rules-for-every-page.md`; the citation key, sources, and file map are in `README.md`.*

## The governing rules

- One keyword per page, always. Plurals and synonyms count as the same keyword; a new location or service modifier makes a new page. Two pages chasing one term split the signal, and Google indexes at most one of them. "You want to rank for one keyword per page. You want to focus on that singular keyword per page." [call 097]
- Never touch a page ranking number one to three, or any page ranking at all, past a UX or CTA tweak. Editing something that already works resets trust for no gain. "The Golden Rule overrides all of this: 31 H1s on a page ranking number one get left alone." [playbook I 3]
- Match what ranks, never a fixed number. Word count, keyword count, and heading count are set by auditing the actual top three results for the exact keyword, then adding a little, never by a universal target. "Length is set by the top three competitors for that keyword, plus a little." [call 001]
- Do not chase 100% on audit tools. A score in the 80s or low 90s is normal; perfection is not the goal, and a lower score can still outrank a cleaner page. "Sometimes you need that D to help you rank." [call 063]
- Content is the number one lever, ahead of schema, backlinks, and speed. "If you write good content, then that matters a lot more than just having a schema markup on the page." [playbook III 1.5]
- Copy first, then design. Layout exists to carry the words, not the other way around. "Our layout is to help communicate our message." [call 079]
- Every page is a door into the business. Build and finish one before starting the next. "Build one door at a time to make sure it's solid." [call 025]
- Accessibility is the SEO foundation, not a side checklist. Real headings, live text, alt text, and contrast serve a screen reader and Google's crawler with the same fix. "Good SEO is build on the exact same foundations as accessibility." [email 2026-07-16]
- Rank on Google first; AI answers follow the same signal, not a separate one. "It's all just SEO. AEO is part of SEO." [playbook I 1]
- Be human and answer real customer questions, consistently, on the business's own site. "The people ranking right now are the ones answering their customers' questions. Consistently. On their own website. That's it. That's the whole thing." [email 2026-05-09]
- If it feels sneaky, do not do it. A gray-hat shortcut can win a ranking and then lose it. "If it feels bad, if it feels sneaky, don't do it." [playbook VI 4.3]
- Patience is structural, not optional. Real movement takes months; judging or re-editing too soon is the most common self-inflicted failure. "You can look at it every day, but don't make actions on it every day." [playbook I 2]

## The universal page spec, element by element

### Title tags
- Length: 50 to 60 characters; past that Google truncates with "...", worse on mobile. [playbook III 2.1; book ch. 4]
- Keyword as close to the front as possible, called out repeatedly as the single highest-value on-page move. "It's important to include your focus keyword at the beginning of your title tag." [course: title-tags]
- Structure: homepage is brand plus keyword; every other page leads with the keyword and puts the brand at the end or drops it. [playbook III 2.1]
- Never write it as "[Post Title] - [Target Keyword]," never strip a keyword the page already ranks on, and keep it unique per page in exactly one SEO plugin's field. [playbook III 2.1; course: title-tags-all-issues]

### Meta descriptions
- Length runs roughly 120 to 156 characters before truncation; Google increasingly rewrites it anyway, so having one matters more than the exact count. [playbook III 2.2; book ch. 5]
- Not a direct ranking factor, but the click-through pitch; always write a unique one and never leave it blank. "It should also be convincing enough to get them to click. This also impacts click through rate." [course: meta-descriptions]
- Keyword near the front, never forced if it reads awkwardly; never let it just repeat the title tag. [playbook III 2.2]
- Never duplicate the same description across pages, even near-identical variants; duplicated metas read to Google as duplicate pages. [playbook III 2.2; book ch. 5]

### URLs and slugs
- Include the focus keyword in the slug on every page but the homepage; no hard character limit, but shorter and plainer outperforms long or stuffed. [course: urls; playbook III 2.3]
- Keep it hierarchical (`/services/website-design`), never a stuffed run-on like `hamilton-website-designers-web-design-hamilton`. [playbook III 2.3; book ch. 6]
- Never change the URL of a page that ranks, gets traffic, or has backlinks; change only when all three are false, then 301 it and update every internal link, since traffic sometimes still does not fully carry over. [course: 10x-your-traffic]
- Never a year in an evergreen URL, and never "near me" or a zip code in a URL. [playbook III 2.3]

### Headings (H1 to H6)
- Exactly one H1 per page, the literal first heading, carrying the exact keyword; H2s reinforce it like chapter titles, H3s support each H2. [playbook III 2.4]
- H2 count is competitor-relative, roughly one more than the top-ranking page, not a fixed number; never skip a level going down, though skipping back up is fine. "If you skip a step going down the stairs, you're gonna trip. But if you skip a step going up, you're fine." [playbook III 2.4]
- Visual size never decides the tag. "The styling does not matter. The H1 does not have to be the largest text." [call 007]
- Duplicate H1s are almost always a builder bug (theme title bars, duplicated desktop and mobile blocks, popups), not a choice; fix by demoting real content to H2 and stripping the tag entirely from non-topical elements like CTAs or testimonials. [playbook III 2.4]

### Word count and content depth
- No universal target: match the actual top three results for the exact keyword plus roughly 10%; a page can win at 400 words or lose at 3,000 depending only on the SERP. [call 001; playbook III 2.5]
- Recurring anchors: roughly 500 to 800 words as a blog floor, 1,000 to 1,500 as a common target; treat these as starting points to check against the SERP, not rules. [playbook III 2.5; email 2025-07-03]
- Count body content only, never nav, footer, or sidebar text, and never trust a single tool's or an AI's self-reported count. [playbook III 2.5]
- Longer must mean more complete, never padded; the real answer belongs in roughly the first 500 words, the part weighed most heavily. [playbook III 2.5, V 7.3]

### Keyword density and placement
- No fixed percentage: count the actual top three results' use of the exact phrase and beat it by one or two. [course: keyword-density]
- Placement checklist repeated everywhere: title tag, meta description, H1, at least one H2, naturally through the body, the URL if possible, and some image alt text. "If you do that, you'll be better off than 90% of websites out there!" [email 2025-06-19]
- Natural variations and plurals count as the same keyword; no separate treatment needed. [call 010]
- Red flag: density visibly above competitors', which is over-optimization, not extra credit; one tracked page fell from number one to number nine sitting at 5.04% against competitors' 1.76% and 0.9%. "More keywords does not equal better rankings." [playbook III 2.6]

### Readability and formatting
- Write at roughly a seventh to eighth grade level, using the plain term a customer would actually type. "If you can't explain it to a kid, you can't explain it." [playbook III 2.7]
- Paragraphs of two to three sentences, varied sentence length; a plugin flag of over 25% long sentences is a nudge to break up run-ons, not a target. [playbook III 2.7]
- Headings, bullets, and images all function as readability tools that feed rankings indirectly through time on page. [course: readability]
- Never chase an all-green readability score once the page genuinely reads well to a human. [playbook III 2.7]

### Bullets, lists, tables, and steps
- Use bullets or numbered lists wherever a block of text runs long with nothing breaking it up; readers skip straight to them. "People can basically skip these sections here and then they can start reading the bullet points." [course: bullets-lists]
- Numbered steps for anything sequential, each carrying a real keyword-bearing label rather than a bare "Step 1"; bullets for facts or features. [playbook III 2.4]
- A bulleted index with anchor links can double as navigation on a very long page. [course: bullets-lists]
- No hard rule that every page needs them: "use them where you can, don't use them if you don't need to." [course: bullets-lists]

### Images (format, size, file names, density, sourcing)
- Format: WebP or AVIF at roughly 70% quality, about a tenth the file size of the same PNG or JPEG with no visible loss; fall back to compressed JPEG only where a platform rejects WebP. [playbook IV Images; book ch. 12]
- Density: roughly one image per 200 to 300 words, at least one per section, never a page with zero. [call 012; book ch. 12]
- Sizing: under about 1,000px wide except hero or banner images (roughly 1,400 to 1,600px), compressed under about 1MB; delete the old originals after converting. [call 007; playbook IV Images]
- Rename the file to a plain, descriptive four or five word phrase before upload, never a raw camera filename. [call 067]
- Sourcing order: real, original photos first for trust, then AI for graphs and infographics, stock last with genuinely descriptive alt text; never an obviously stock-looking image on a page meant to show a real team. [playbook III 2.8]

### Alt text
- Every image gets alt text, never empty; the formula is medium plus description, so "illustration of a stack of blueberry pancakes in a kitchen" beats the bare word "pancakes." [course: alt-text]
- Keep it to roughly five or six words, keyword only where honestly descriptive, and only on about half or fewer of a page's images, never the identical phrase down every image. [call 117; playbook III 2.8]
- Its first job is a screen reader describing the image; ranking sits behind that, not in front of it. "So like people who can't see, visually impaired people have something to hear." [call 125]

### Video and audio
- Never self-host video; embed from YouTube or Vimeo, which also lets Google index one video per page and pull it into results. "Never ever host your own videos. Videos take a lot of space and a lot of server capacity." [call 007]
- Not required to rank; used to add credibility, break up text, and raise time on page. [course: video]
- A real, short clip of an actual person beats a faceless or AI-avatar clip by a wide margin, and AI-generated video specifically draws platform enforcement that AI-generated images do not. [playbook II 4.6, V 5]
- Never an autoplaying hero background video; weigh its appeal against its cost to speed and mobile data. [playbook III 2.9]

### Internal links and anchor text
- The single most repeated high-leverage move in the whole corpus: every new page links out to three to five others, including at least one money page, and gets links back in from roughly three older, indexed pages. "Internal linking = SEO momentum." [email 2025-12-10]
- Anchor text must describe the destination, ideally its own keyword; never "click here," "learn more," or a bare "here." [course: anchor-text; book ch. 8]
- There is a ceiling as well as a floor: a soft range of ten to twenty links per page, a hard outer limit of fifty to one hundred. [playbook III 2.11]
- Keep every important page within about three clicks of the homepage. "If I can't get to it from your homepage, Google's not going to index it." [playbook III 2.11]

### External links
- At least one external link on every page, including the homepage and money pages, ideally within the first few paragraphs, citing a real source. [course: external-linking; book ch. 10]
- Never link to a competitor, ever; naming or comparing them in text is fine, hyperlinking them is not. "The number one rule with linking is never link to a competitor." [playbook III 2.12]
- Never link out to another page targeting the exact same keyword. [playbook III 2.12]
- On money pages, a link to the business's own legitimacy profiles (chamber of commerce, Trustpilot) satisfies the rule. [call 010]

### Schema and structured data
- Deliberately deprioritized: described as the 80% of effort for 20% of the result, with no measured effect on AI Overview citation in the operator's own testing. "Doesn't matter... not worth the time." [call 020]
- For most sites, the SEO plugin's automatic schema toggle is enough; it is free and needs no further setup. [playbook IV Schema]
- Only penalized when the data is actively wrong or misleading; missing but accurate schema is never penalized. [playbook IV Schema]
- Manual, custom JSON-LD is worth the effort only for specific, high-competition needs, and belongs in the page header, not the body. [playbook IV Schema]

### Site speed and Core Web Vitals
- Deliberately the last thing to fix, only after content and keywords already match or beat the competition; speed is a tiebreaker among otherwise-equal pages, not a hard requirement. "You gotta fix your pages first and then you can look at page speed after that." [playbook IV Site Speed]
- Core Web Vitals in plain terms: fast load, readable fonts, fast images, nothing shifts after it renders. [playbook IV Site Speed]
- Target roughly 80% or higher on mobile PageSpeed and never chase 100%; fix order runs plugin count, then caching, then image compression, theme change last. [playbook IV Site Speed]
- Never block AI crawlers to solve a bot-traffic spike; upgrade hosting and add a firewall instead. [playbook V 7.4]

### Mobile and responsive
- Google has indexed mobile-first since roughly 2016, and mobile is over half of most sites' traffic; a page cut off or non-reflowing on a phone is a direct negative regardless of desktop quality. [playbook IV Mobile; book ch. 20]
- Design the largest breakpoint first, then step down; never duplicate a whole block for desktop versus mobile, since that reads as gaming the system. [playbook IV Mobile]
- Mobile hero order: headline, copy, call to action, photo, stacked top to bottom, never photo beside text; side padding must shrink sharply from desktop so nothing touches the edge. [playbook IV Mobile]
- Put a tap-to-call number where a thumb reaches it, generally near the bottom, and check every page's actual phone rendering. [playbook III 3.4]

### Typography
- One distinctive heading font paired with one plain body font; more than two or three fonts on a site measurably slows it down. [call 028]
- Body text never smaller than 16 pixels, roughly 1.8 line height; headings step down clearly in size. [call 008]
- Never cursive or script for anything read quickly, including buttons and pricing. "Any friction is friction." [call 045]
- Font choice carries no direct SEO weight; the semantic tag, not the visual size, is what Google reads. [call 045]

### Color and contrast
- Never pure black on pure white; it reads as "vibrating." Use a soft dark gray on near-white instead. [call 045]
- One primary call-to-action color, high-contrast and consistent; secondary actions recede, and a complementary pair should never split fifty-fifty. [playbook IV Typography]
- Self-check contrast by imagining the page in grayscale; if text is not clearly readable there, there is not enough contrast. [playbook IV Typography]
- Color should match the brand's audience and tone but carries no direct ranking weight; it is a trust and conversion lever. [calls 098, 100]

### Spacing, whitespace, and section rhythm
- Deliberate empty space around elements is treated as a real signal, and too little of it is an active negative. "White space doesn't mean just white, it just means the empty space around objects and assets." [call 055]
- Alternate the layout rhythm section to section, text left then image right and reversed, with a subtle background tint against white, so each section reads as one idea. [calls 028, 060]
- Give each section consistent top and bottom padding rather than ad hoc spacing. [call 067]
- Left-align body copy; reserve centered text for short blurbs only, since long centered text is harder to read. [calls 083, 100]

### Accessibility
- Treated as inseparable from technical SEO, not a separate checklist: real headings, live text, alt text, and contrast serve a screen reader and Google's crawler with the identical fix. [email 2026-07-16]
- The working test is literal: can someone who is legally blind actually use this page. "Can someone who is legally blind use it? Because if they can't, it's likely impacting your Google Rankings!" [email 2026-07-16]
- Sites must be zoomable, scalable, and usable by a screen reader as a baseline. [call 002]
- A Lighthouse accessibility score of 100 is realistic, since the fixes that get it there are the same fixes that clean up heading structure and alt text. [call 013]

### Page builders and platforms
- The platform does not matter to Google: any platform can rank with unique URLs, a working sitemap, and good content. "Google doesn't actually care about the platform you're using." [call 045]
- Real differences show up in control, not ranking ability: WordPress offers the most flexibility, while Wix, Squarespace, Shopify, and GoHighLevel each carry known ceilings on speed, headings, or image formats. [playbook IV Page-Builder]
- Never run more than one SEO plugin at once; two plugins writing tags independently causes duplicate title tags and meta descriptions. [course: title-tags-all-issues]
- On any rebuild, keep every URL, heading, and structural element identical to the live version; only the look should change, and anything that must move gets a 301. [call 013]

### AEO and answer-first structure
- Answer the literal question at the very top, in plain language, since there is no way to know how far down a human or an AI system reads. "There's no way to know how far they crawl on every page, which is why I put the answer right at the top." [playbook II 4.3]
- AEO is not a separate discipline: ranking on Google is what gets a page pulled into AI Overviews and chat answers. "It's all just SEO. AEO is part of SEO." [playbook I 1]
- The recurring pattern: a short direct answer immediately under the heading, more context in the next paragraph or two, and only on genuinely long pages, a short key-takeaways list at the end. [playbook V 7.3]
- Write for the human reader, not "for the AI." [playbook V 7.3]

### Indexing, sitemaps, robots, canonicals (as they apply to building a page)
- Submit the sitemap once inside Search Console; it updates itself after that on nearly every platform, and individual URLs should never be hand-submitted one by one. [book ch. 23, 29]
- The canonical tag must match the live, rendered URL exactly, including the trailing slash. [call 030]
- A page does not need a manual "request indexing" click for every edit; solid internal linking is what actually gets it crawled. [call 010]
- Leave robots.txt alone unless there is a specific reason to touch it; remove any leftover crawl-delay directive, and never blanket-block AI bots. [call 066]

### Patience windows and editing discipline
- After publishing or meaningfully editing a page, leave it alone for roughly a month; a dip right after a change is expected noise, not proof it failed. [playbook I 4]
- Judging windows scale with the change: about two weeks to a month for a title, meta, or H1 nudge; two to three months for a content rewrite; three to six months minimum, sometimes closer to a year, for a new or non-ranking page. [playbook I 4, I 5]
- Check performance in 28-day windows, never day to day. "You can look every day. Just don't take action on it." [call 010]
- Change one variable at a time on any page that does get touched; never batch-edit headings or keywords across many pages at once. [playbook I 4]

### Auditing a page (tools, what to read, what to ignore)
- Standard method: run the page's own URL and the number one and two ranking pages for its exact keyword through the same tool, then log title, meta, H1, H2s, word count, keyword usage, and mobile and desktop speed side by side. [email 2025-07-05]
- Fix severity order: broken links and missing or duplicate H1s, titles, and metas first; heading structure next; speed and schema last. [playbook III 4.1]
- Read a score as directional, not literal: 80% or higher, or "92 out of 100 with two fixes," is a normal, healthy result. [calls 013, 018]
- Discount keyword-density warnings and any absurd reading like 600% density, which just means a blank keyword field; remember tool caches lag hours to a week, so a dip right after a fix is usually the cache, not the fix. [call 007]

## The numbers table

| Element | Rule / number | Source(s) |
|---|---|---|
| Title tag length | 50 to 60 characters, ideal under ~55 | playbook III 2.1 |
| Title tag length | ~60 characters max (about 8-15 words) | book ch. 4; email 2025-07-03 |
| Meta description length | 120 to 155 characters | playbook III 2.2 |
| Meta description length | 80 to 156 characters | book ch. 5 |
| Meta description length | 140 to 145 characters | calls 097, 105 |
| Word count | Match top 3 ranking pages plus ~10%, no fixed number | calls 001, 010 |
| Word count | 750 to 1,500 words (later narrowed to 800-1,000) | playbook III 2.5 |
| Word count | 1,000 words minimum, 1,000 to 1,500 typical | course: word-count; email 2025-07-03 |
| Word count | 2,000+ words on the homepage | course: word-count (superseded, see disagreements) |
| H1 count | Exactly 1 per page | playbook III 2.4 |
| H2 count | About 1 more than the top-ranking competitor | playbook III 2.4 |
| Heading depth | Avoid past H3; never skip a level going down | playbook III 2.4; book ch. 7 |
| Keyword density | Match top competitor's count plus 1-2, no fixed percent | course: keyword-density |
| Keyword density | Red flag well above competitors (e.g. 5.04% vs 1.76%/0.9%) | playbook III 2.6 |
| Secondary keywords | 5 to 10 per page or post | course: finding-keywords-for-your-blog-posts |
| Image density | 1 image per 200 to 300 words | call 012; book ch. 12 |
| Images per post, minimum | 3 to 4 (email) vs 4, ideally 1 per H2 (playbook) | email 2025-07-03; playbook III 2.8 |
| Image width | Under ~1,000px except hero or banner | call 068 |
| Image width, hero | ~1,400 to 1,600px | call 008; book ch. 12 |
| Image file size | Under ~250KB, compress anything over ~1MB | book ch. 12 |
| Alt text length | About 5 to 6 words, descriptive | call 117 |
| Alt text keyword coverage | On about half or fewer of a page's images | playbook III 2.8 |
| Internal links per page | 3 to 5 in content | book ch. 9 |
| Internal links, ceiling | 10 to 20 soft ceiling, 50 to 100 hard max | playbook III 2.11 |
| Internal links, inbound | 3 older indexed pages link into each new page | playbook III 2.11 |
| External links per page | At least 1 | course: external-linking; book ch. 10 |
| Crawl depth | Within about 3 clicks of the homepage | playbook III 2.11; book ch. 27 |
| Body font size | 16px minimum, 17 to 20px used in practice | call 008 |
| Line height | About 1.8x body size | call 008 |
| Fonts per site | 2 safe, 3 is the practical max | call 028 |
| Mobile PageSpeed target | 80%+ | playbook IV Site Speed |
| WordPress plugin count | 15 or fewer | call 045 |
| FAQ items on a page | 3 to 4 max | playbook V 7.3 |
| Audit score target | 80%+ fine, never chase 100% | playbook III 1.4 |
| Audit tool cache lag | 5 to 24 hours, sometimes up to a week | call 007 |
| Patience, after any edit | About 1 month before re-editing | playbook I 4 |
| Patience, content-level change | 2 to 3 months to judge | playbook I 4 |
| Patience, new or non-ranking page | 3 to 6 months minimum, up to about a year | playbook I 4, I 5 |
| Indexing, new post | About 2 hours to 1 week | playbook I 5 |
| Indexing, brand-new site | 2 to 3 weeks to about 2 months before first crawl | playbook I 5 |

## Don'ts that apply to every page

- Don't target two keywords on one page, or the same keyword on two pages. [playbook III 1.1]
- Don't edit or redesign a page already ranking #1 to #3, or ranking at all, beyond a UX or CTA tweak. [playbook I 3]
- Don't keyword-stuff anywhere: body, URL, or hidden same-color text; don't copy a competitor's stuffing. [playbook III 2.6]
- Don't duplicate a heading block for desktop and mobile, and don't fake a heading with a styled paragraph or an image. [playbook III 2.4]
- Don't skip a heading level going down (H1 straight to H3); skipping back up is fine. [book ch. 7]
- Don't pad word count with filler, and don't trust a single tool's or an AI's self-reported count. [playbook III 2.5]
- Don't leave alt text empty, and don't repeat the identical alt phrase across every image on a page. [playbook III 2.8]
- Don't self-host video, autoplay a hero video, or publish AI-generated video. [playbook III 2.9]
- Don't use "click here" or "learn more" as anchor text, and don't paste a raw URL when the platform has a page picker. [book ch. 8]
- Don't exceed roughly 10 to 20 internal links per page as a habit, and never pile past 50 to 100. [playbook III 2.11]
- Don't link out to a competitor, ever, or to another page targeting the exact same keyword. [playbook III 2.12]
- Don't leave a page with zero outbound links, or a page you want ranked with zero inbound links or four-plus clicks deep. [playbook III 2.11]
- Don't hide FAQ answers or real service content behind an accordion or dropdown. [playbook V 7.3]
- Don't build custom schema hoping for an AI citation, and don't ship schema that misrepresents the business. [playbook IV Schema]
- Don't chase a speed fix before content and keywords already match the competition, and don't block AI crawlers to fix a bot spike. [playbook IV Site Speed]
- Don't run more than one SEO plugin at a time, and don't exceed about 15 active WordPress plugins. [course: title-tags-all-issues]
- Don't use more than 2 to 3 fonts on a site, set body text under 16px, or put pure black text on pure white. [playbook IV Typography]
- Don't right-align body text and don't over-use centered text, especially on mobile. [playbook IV Mobile]
- Don't chase 100% on any audit or readability tool, and don't act on a score change without checking where the page ranks. [playbook III 1.4]
- Don't check rankings daily; compare 28-day windows instead. [playbook I 2]
- Don't change a URL with any ranking, traffic, or backlinks, and never redirect a redirect. [playbook III 2.3]
- Don't publish a raw AI draft; strip AI tells (random bold, emojis, "in conclusion," "delve into") before it goes live. [email 2025-07-03]

## Where the sources disagree

- Accordion FAQs: one line of sources calls collapsed content safe to index. "Accordions/toggles are safe to index; agentic crawlers interact with menus and forms." [call 015] Another says the opposite: "hidden or collapsed text counts against you... dropdown FAQs," and FAQ answers should never sit behind an accordion. [call 109; playbook V 7.3] No source resolves this; displayed-open is the safer default.
- Schema: the course material is the most bullish source in the corpus, arguing structured data helps rankings directly. "Sites with properly structured data will help you rank higher." [course: schema-markup] The calls and the playbook flatten this to "doesn't matter... not worth the time," with no measured lift in citation testing. [call 020] Practical read: use the plugin default, skip a custom build.
- Word-count floors: four anchors coexist unreconciled: match the top 3 with no fixed number [calls 001, 010], 750 to 1,500 words as one program's baseline [playbook III 2.5], 1,000 words as the course's stated minimum [course: word-count], and 2,000+ words on a homepage as the course's older claim, which the playbook itself later marks as superseded. Newer material trusts the competitor benchmark over any fixed figure.
- Images per post: the density rule (1 per 200 to 300 words) is consistent, but the stated floor splits between 3 to 4 images in the emailed checklist [email 2025-07-03] and a minimum of 4, ideally one per H2, in the playbook. [playbook III 2.8] Both agree the real driver is density, not the count.
- Stock versus AI imagery order: the playbook disagrees with itself, one part ranking AI images above stock for anything but real team or product shots, another part calling AI and stock "roughly equivalent" once real photography isn't available. [playbook II 4.8, IV Images] A separate call hedges further, calling AI images simply "uncertain." [call 079] Only real, original photography is undisputed as the top choice.
- External links on money pages: the placement rule says every page, including money pages, needs at least one external link, yet the same source notes its own flagship SEO service page has zero external links and still ranks number one. [playbook III 2.12] The rule holds as the default; a page that already ranks is not required to retrofit one.
- Duplicate H1s from desktop and mobile blocks: earlier material calls an identical-text duplicate "tolerated," not a real problem, while the same source later adds that the practitioner now suspects "even this reads as gaming." [playbook III 2.4] A true single responsive block, not a duplicated one, is the safer target.
- Core Web Vitals priority: most sources build a real causal chain from slow load to lower rank and give an active fix sequence, while one call dismisses the category for a beginner entirely: "Core Web Vitals and web speed are web developer stuff... we don't even need to worry about all that" to start. [call 120] Both agree speed is not the first fix; they disagree on whether a new site should think about it at all yet.
