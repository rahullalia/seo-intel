# Web Design for SEO with Leanne Jones — 12.24.2025 Replay (Christmas Eve AMA)

## Tactics & step-by-step how-to
- Ranking-but-no-traffic diagnosis path: if service pages already rank on page 1 but traffic is flat, don't rewrite them — leave the content alone, keep blog posting (targeting easier-to-rank keywords), and internally link those blog posts back to the service pages to help push them higher.
- For pages that aren't ranking yet: same fix — more time + more interlinking/blog posts pointing at them, not necessarily a content rewrite, if the pages are already "set up correctly."
- Backlink starting point for a site with zero backlink strategy: join your local Chamber of Commerce and similar business associations for easy, legitimate backlinks; also check Matt's Insiders group material on backlink building.
- General on-page SEO structure to apply to every page: one H1 → H2s that relate to the H1 → H3s that relate to their parent H2 → ~1,000–1,500 words on the page → image alt text containing the target keyword but written naturally (not stuffed).
- **Removing a background from a photo (WordPress has no native tool for this):**
  - Photoshop method: double-click the layer to unlock it → use the built-in AI "Remove Background" tool (one click) → use the Crop tool to trim the now-empty canvas space down to just the subject → File → Export → Save for Web → choose PNG and check the **Transparency** box → save. (Skipping the Transparency checkbox saves a plain white background instead.)
  - Canva method: upload the image → open the editor → use the Background Remover tool (Canva **Pro** feature only, not free tier).
  - Wix has this as a native one-click AI feature; WordPress doesn't — you have to go outside the platform (Photoshop, Canva, or a plugin) to do it.
- **Fixing a dropdown/nav menu item wrapping to two lines** (e.g., "Dumpsters and Demolition" breaking mid-phrase): the fix is the container's width/padding — widen the dropdown box (demoed by setting it to 300px wide) so the full phrase fits on one line. Desktop and mobile need to be adjusted separately since the layout changes when the screen collapses to the mobile breakpoint.
- **Building a jump-link / anchor link to scroll to a section (e.g., a contact form) — same method on any builder:**
  1. Select the container/section you want the click to land on.
  2. Give that container an ID — in Elementor: Advanced tab → CSS ID → type an id like `contact`. Divi has the same concept via its own CSS ID field (may not be labeled identically).
  3. On the button/link that should trigger the jump, set its link target to `#contact` (hashtag + the same id name).
  4. Publish — clicking now scrolls straight to that section.
- **Shopify on-page SEO audit/fix order** (used live on Fernando's bestbrows.com — transcript renders the domain both as "bestbrowns.com" and "bestbrows.com"):
  1. Run the site through Matt's Page Audit tool first; start with the homepage.
  2. In Shopify: Online Store → Pages → open a page → scroll to the bottom → "Edit website SEO" (search-engine-listing) section → fill in Page Title (should be that page's focus keyword) and Meta Description (should describe the page's topic). Fernando's site had neither set on any page.
  3. Fix the H1: it should describe the actual product/topic, not just be the brand name alone (his H1 was literally "Best Brows," the store name, with nothing more descriptive). Leanne's own Shopify site was used as the model: H1 = "Ontario Artist [Name]," H2s = "Ontario Artist Capturing the Beauty of Canadian Wildlife," "About," and "Nature" (a secondary/related keyword for a nature-focused artist).
  4. You can optimize/edit all your product and service pages this way in one single session — safe to batch. (Contrast with blog posts below.)
  5. Known Shopify quirk: it messes up your H1/H2 hierarchy and ordering automatically — Leanne called this fixable but said it's involved enough that she might run a dedicated future session just on that fix.
- Keyword-per-page split: product/service pages should describe that page's actual product/topic (H1 focused on the offering itself); blog posts are where you go after "easier to rank" keywords, then link those posts back into the service/product pages to lift them.
- **Heading-tag cleanup:** on Benjamin's site, H5s and H6s were being used where H3s belonged — fix is simply converting them to proper H3s to restore a clean H1→H2→H3 hierarchy.
- **Service-naming decision (e.g., "web development" vs. "web design"):** run both terms through a keyword research tool to see which has more search volume/is easier to rank, and think about what your actual target audience types into Google (small businesses are more likely to search "web design"/"website design" than "web development"). Rather than fully renaming the service page, add the higher-volume term as an additional/parallel service page.
- Cross-link two related service pages via a blog post — example given: write a post titled roughly "What's the difference between web design and web development?" and link out to both service pages from inside it.
- **Multi-country/location SEO:** don't run one combined page for multiple countries or regions served (Benjamin had one page covering both US and UK) — split into one dedicated page per location. Model cited: an agency site listing "serving clients in [multiple cities]," with a separate page built per city, plus separate pages built per industry vertical targeted.
- Even when the underlying service is nearly identical location to location (Lux's example: a lien-filing service where county-to-county differences are mostly just price) — still build the separate city/county pages; just vary the on-page wording/lingo per page rather than the substance.
- **Blog/page conversion fixes:**
  - Add a CTA in the page sidebar (example shown: a "write for us" CTA in a sidebar).
  - Add a CTA mid-scroll through the content.
  - Always add one more CTA at the very bottom of the page/post — otherwise readers who scroll all the way through hit the end with nothing to do and just leave.
  - Rewrite vague/jargon CTA copy into plain language — flagged example was CTA text using legal jargon a layperson wouldn't understand; swap toward something like "Contact Us" or "Want to learn more?" and test variations of the wording.
- **Homepage CTA audit:** confirm a CTA exists near the top for immediate contact; if there's intro text with no button directly under it, add one (example given: add a "Get a Free Quote" button directly beneath the top text).
- **Cut page weight from a live embedded Google Map:** replace the embedded iframe map with a static image of the map that links out to the real Google Maps listing — avoids loading the embed code entirely. Cited as what Matt's own "Hey Tony" site does.
- **Diagnosing a single user's "can't load your site" complaint:** run Google PageSpeed Insights first. If the site scores fast, the problem is very likely on the visitor's end (an old computer, or an outdated browser like Internet Explorer) rather than a site-side image/performance issue — don't assume it's your images without testing first.
- **WordPress page-speed fix order before ever considering a rebuild:** (1) install an image-optimization plugin (referenced inconsistently in the transcript as "Image," "Imify," "ImageFi" — almost certainly **Imagify**) to convert images to WebP for a smaller file size; (2) install and configure **WP Rocket** for caching; (3) only after those, consider a full rebuild. Rebuilding was explicitly called the last resort.

## Rules / dos & don'ts
- One H1 per page — not more.
- H2s must relate to/support the H1; H3s must relate to/support their parent H2.
- Target roughly 1,000–1,500 words per page.
- Alt text should include the target keyword, written naturally — not keyword-stuffed.
- Safe to batch-edit all product/service pages (titles, meta descriptions, H-tags) in one sitting — this will not hurt rankings.
- NOT safe to publish/dump a big batch of new blog posts all at once — that can hurt SEO. Blog posts should go out more gradually.
- New sites/redesigns need real time to start ranking — the caller's site was ~1 year post-redesign and still building traffic despite page-1 rankings on some terms; upward movement = "on the right track," not a problem to panic-fix.
- If a service page already ranks, leave its content alone — don't over-edit pages that are working; put the effort into blogging + internal linking instead.
- Don't platform-hop (Wix ↔ WordPress ↔ GoDaddy ↔ Shopify) just because of a learning curve or because "X is supposed to be the gold standard" — you don't gain SEO by switching, and you have to redo everything if you migrate. Platform is "almost a personal taste"; any platform can work if you stick with it.
- Photoshop Save for Web: must select PNG **and** check the Transparency box, or the export defaults to a plain white background instead of transparency.
- Canva's background remover is Pro-only (paid), not available on the free tier.
- WordPress has no native background-removal tool — needs an external app or plugin.
- Page title = the page's focus keyword; meta description = a summary of that page's topic — every page should have both set (Fernando's Shopify pages had neither).
- H1 should describe the actual product/service/topic, not just repeat the brand/business name with no other context.
- Give every location you serve its own dedicated page rather than combining multiple regions/countries on one page; same logic for distinct industry verticals.
- Even for near-duplicate local service pages (service barely differs by county except price), still build them as separate pages — vary wording, not necessarily substance.
- Every blog post/page needs a clear, plain-language CTA; avoid jargon-heavy button copy laypeople won't parse.
- Always place a CTA at the very bottom of long-form content, not just top/middle — otherwise readers who finish the page have nothing to do and leave.
- Avoid a live embedded Google Map iframe if page speed matters — use a static image linked out to the Maps listing instead.
- After installing WP Rocket, manually test every button, link, and dropdown on the site — it can silently break JavaScript-dependent functionality.
- Rebuilding a whole website for performance problems should be the last step, tried only after image optimization (Imagify/WebP) and caching (WP Rocket) have already been attempted.

## Tools, prompts & resources
- **Matt's Page Audit tool** — recommended first step for auditing any site (used on Fernando's Shopify homepage).
- **Hey Tony Insiders group** — has existing material on how to get more backlinks; also flagged as the right place to ask Matt directly why a well-structured, page-1-ranking site still isn't converting traffic (backlinks are "Matt's specialty," not Leanne's).
- **Google PageSpeed Insights** — used live to test Susan's seed-company site (came back fast, ruling out image size as the cause of her friend's load complaint) and Benjamin's agency site (used to evaluate whether a rebuild was warranted).
- **Photoshop** — background removal via its built-in one-click AI "Remove Background" tool, plus Crop tool and File → Export → Save for Web (PNG + Transparency checked).
- **Canva (Pro)** — Background Remover tool, paid-tier only.
- **Elementor** — page builder; Advanced tab → CSS ID field used to build the anchor/jump-link technique.
- **Divi** — same anchor-link concept applies via its own CSS ID equivalent field.
- **Shopify's built-in SEO fields** — Online Store → Pages → scroll to bottom → "Edit website SEO" section for Page Title + Meta Description.
- **Ubersuggest** — the keyword research tool Fernando is currently using; he described it as overwhelming for deciding a keyword per page (Leanne didn't specifically critique or endorse it beyond acknowledging general keyword-tool use).
- **Imagify** (transcribed inconsistently as "Image," "Imify," "ImageFi") — WordPress plugin to convert images to WebP for smaller file sizes/faster load.
- **WP Rocket** — WordPress caching/performance plugin; Leanne uses it on her own site; called "a little pricey" but "worth it."
- **Astra** — WordPress theme (Susan's site).

## Case studies / examples / results
- **Anonymous caller #1:** site redesigned ~1 year ago (prior version ran ~2 years before that); ranking page-1 for some keywords but still near-zero traffic; no backlink strategy at all; just started blog posting herself in the past year and doing her own keyword updates. Leanne's read: structurally the site looks fine — probably just needs more time plus backlinks (Chamber of Commerce suggested as an easy first move).
- **Anthony:** WordPress + Divi site. Removed an oversized badge/icon from the page header and relocated it to the footer. Wanted background-removal tooling like Wix's native one-click AI feature; walked through Photoshop and Canva Pro alternatives live. Also had a dropdown nav item ("Dumpsters and Demolition") wrapping to two lines — fixed conceptually by widening the container to 300px. Platform history: GoDaddy → Wix → WordPress, moved because "WordPress is supposed to be the gold standard" for SEO; currently finding WordPress less intuitive than Wix.
- **Grace:** SEO specialist at the University of Arizona working with indigenous communities; building a report-audit landing page in Divi (normally uses Elementor); based in Tucson; needed a jump-link from a button down to a signup form on the page — solved with the CSS-ID anchor technique.
- **Fernando — bestbrows.com** (Shopify): brand new to SEO, felt overwhelmed about where to start. Site had no page title or meta description set anywhere. H1 was just the brand name "Best Brows" with no descriptive keyword. Walked through Shopify's SEO fields and H1/H2 fix using Leanne's own "Ontario Artist" site as the working example. Currently uses Ubersuggest for keyword research. Also asked about Meta-advertised services charging roughly $40–50 to get a client "published on Forbes and other media outlets" as a backlink play — Leanne deferred entirely to Matt as the backlink expert.
- **Benjamin:** runs a web development and mobile development agency; WordPress site with performance issues mainly on mobile, was considering a full rebuild. Found using JPEGs (recommended Imagify → WebP) and H5/H6 tags used where H3s belonged (recommended converting). Competitors rank for "web design" while his own page targets "web development" — advised to add "Web Design" as a parallel service/page rather than replace, plus write a "web design vs. web development" blog post cross-linking both service pages. Company is registered in both the US and UK but ran as one combined page — advised to split into separate location pages, modeled on another agency's "serving clients in [multiple cities]" page structure plus separate industry-targeted pages. Also shifting his target market in the new year from small/medium businesses to medium/large businesses.
- **Lux:** took over SEO for a site last October; rewrote articles that were previously "just a wall of text" with no CTA. Result: **~30% traffic increase from California** specifically, their current target market — but conversion still lagging behind the traffic gain. Diagnosed the friction as unclear/jargon CTA copy (flagged phrasing along the lines of "file [a] mechanics lien now," confusing to a layperson) and no CTA at the bottom of the post. Also asked about building California city-specific pages for a lien-filing-type service where the underlying service barely differs by county except price — advised to build them anyway, varying wording per city.
- **Unnamed final caller** (name unclear in transcript, phonetically close to "Xavier"/rendered as "savior"): WordPress site with SEO and heading structure already "great" per Leanne; already had CTAs near the top. Site was running a bit slow on mobile and desktop — advised WP Rocket + Imagify, and to add an additional "Get a Free Quote" button directly under the top text, plus to swap a live embedded Google Map for a static linked image (per Matt's own "Hey Tony" site).
- **Susan:** seed company, lots of product images plus AI-generated images. A friend reported he couldn't load her site on his old computer. Leanne ran PageSpeed Insights live — site scored fast, ruling out image size as the cause; concluded the likely culprit was the friend's old hardware or an outdated browser (e.g., Internet Explorer), not the site itself. Platform: WordPress, Astra theme.

## Notable verbatim quotes
- "It does take a little bit of time for a new website to start ranking higher on Google. But if you are seeing like you are going up, then I would say that you are on the right track."
- "If your service pages are ranking, I would just leave them alone and continue posting on your blog posts. And then with your blog post, you're targeting easier to rank keywords. And then within those blog posts, you're linking internally to some of these service pages to help these service pages start to rank higher as well."
- "Some easy backlinks you can get is like joining chamber of commerce and things related to your business to get some easy backlinks."
- "For every page, you should have one H1 tag, and then in your pages, you should have H2 tags that are related to the H1 tag. And then with your H3s should be related to the H2s. And then you should have about like a thousand to fifteen hundred words per page."
- "WordPress allows people who are web designers and SEO experts to really hone in on optimizing their site... but really, any platform can work. You just — it's almost a personal taste."
- "I don't want people to just like jump ship to a different platform right away... if you just stick with it, you can make it work."
- "You could do that all in one shot. It's just for blog posts that you shouldn't just like dump a whole bunch of blog posts all at once."
- "I feel like your H1 tag should describe the product or the topic of your page the most. And then in your blog post, that's when you're really focusing on trying to rank for easier to rank keywords."
- "Rebuilding your site would be probably my last thing that I would do because it looks great. It looks like it's set up correctly in terms of SEO."
- "The thing with WP Rocket is you have to test out all your buttons and links and your drop downs because sometimes they can mess with your JavaScript."
- "It's all the same product. They just changed up the lingo for each of these service pages... to target a different location."
- "So when someone gets to the bottom of your page, okay, there's nothing for them to do. So they'll land here and then they'll just leave. So I would have one right at the bottom to capture the last remaining people that make it through all the way to the bottom."
- "Honestly, it's a solid website. It's got all the, all the right bones to it."

## Tradeoffs & nuance
- Page-1 rankings without traffic isn't treated as a structural failure — Leanne's default read is time + missing backlinks, but she explicitly flags backlinks as Matt's specialty rather than hers and defers the deeper "why isn't this converting to traffic" question to him.
- The rule "don't touch pages that already rank" trades short-term perfectionism for a steadier growth lever (blogging + internal linking) — the implication is that editing settled, ranking pages carries more downside risk than upside.
- Batch risk differs by content type: on-page elements (titles, meta descriptions, H-tags) are safe to change site-wide in one sitting, but publishing a large batch of new blog posts simultaneously is treated as a distinct, higher-risk action.
- Platform choice (WordPress/Wix/GoDaddy/Shopify) is explicitly framed as not a real SEO lever by itself — the switching cost (redoing everything) generally outweighs any platform's marketed advantage, and Leanne actively discourages "platform hopping" even when a client is frustrated with a learning curve.
- A single user's page-load complaint isn't automatically treated as a site defect — the triage order is test the site first (PageSpeed Insights), and only suspect the visitor's own hardware/browser once the site itself tests fast.
- Renaming a service to chase a higher-search-volume term (web design vs. web development) isn't posed as a straight swap — the recommended middle path is additive (keep both, add the new one as a parallel page), informed by both keyword volume and an intuition read of what the target audience actually searches.
- Near-duplicate local service pages (same service, different city, price the main variable) are still worth building separately for SEO purposes — the value of the dedicated page is judged to outweigh the thinness of the real differentiation, so the fix is wording variation rather than requiring genuinely different content.
- A full site rebuild is explicitly de-prioritized below cheaper/faster interventions (image compression, caching) even when a client is actively considering one — reframed as a last resort, not a first response to a performance complaint.
- WP Rocket's speed win comes with an explicit tradeoff: it can quietly break JavaScript-driven interactive elements, so the speed gain requires a manual QA pass across the whole site afterward before calling it done.
