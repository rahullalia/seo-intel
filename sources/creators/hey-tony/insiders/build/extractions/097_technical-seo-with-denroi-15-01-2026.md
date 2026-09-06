# Technical SEO with Denroy — 15.01.2026 (Call #097)

Format: live Q&A, raised-hand queue, live screen-share audits. Denroy = head of technical SEO at Hey Tony, 5 years working with Matt (updated from "6 years" cited in call #007), background spans every SEO discipline plus web dev/design, WordPress, Shopify, Google Ads, GMB. Described as one of the biggest calls he's run (second-biggest ever). Next call scheduled for the 29th.

## Tactics & step-by-step how-to

- **Diagnosing mobile site speed:** run the URL through pagespeed.web.dev, check the Mobile tab separately from Desktop (desktop often scores fine while mobile doesn't). Look for flagged issues like high LCP and heavy JavaScript.
- **Previewing mobile rendering/animations in Chrome:** right-click → Inspect → click "toggle device toolbar" (top-right of DevTools) → pick a device (e.g. iPhone 12) to see what's actually loading/animating on mobile.
- **Fixing slow template-based sites (Wix/Shopify/WordPress purchased templates):** have a developer audit for leftover unnecessary code/scripts from the template; disable non-essential animations, especially on mobile; defer scripts into a CDN (e.g. Cloudflare).
- **Wix-specific speed fixes:** since users can't access hosting-level settings (no cPanel/host manager), contact Wix support directly to adjust those settings.
- **Before changing a page's target keyword (homepage rebrand scenario):**
  1. Run the candidate keyword through a keyword research tool to confirm real search volume — don't assume a desired phrase ("Waste Solutions") has volume just because you want to rank for it.
  2. Check Google Search Console to see what the page currently ranks for.
  3. If it already ranks well for the existing keyword, leave that page/keyword as-is; build or optimize a separate page for the new target keyword instead of overwriting.
  4. If research does support the new keyword, update the title tag (target keyword + business name), match the meta description to the exact keyword, and sprinkle the keyword through H2s.
  5. Change the old page's own copy/keywords too, so the two pages aren't competing for the same term (cannibalization).
- **Local-intent title tag fix:** rewrite a broad/regional title (e.g. "Northwest Lien") to name the specific state/city being targeted (e.g. "Mechanics Lien in California"); same fix for meta description. Narrow to a specific city if possible — lower competition.
- **Local SEO expansion sequence:** rank in one small area first, win it, then branch outward geographically (Hey Tony's own example: start in Hamilton, then expand to Toronto or Windsor).
- **Domain rebrand (e.g. "Northwest Lien" → "NW Lien Service" ahead of nationwide expansion):** set up a 301 redirect from the old domain to transfer domain authority.
- **Expanding into multiple states/cities:** add a "Locations" or "Service Areas" nav item, build a dedicated page per location.
- **Fixing an under-indexed site (only homepage indexed in GSC):** go through every blog post, find mentions of relevant terms (VPS, dedicated hosting, domain registrar, domain transfer, etc.), and add internal links from those mentions to the matching service pages — across the entire blog back-catalog, not just new posts.
- **Auditing internal links:** don't trust a visual scan alone — unstyled/white link text can hide that a link exists. Hover/inspect to confirm, not just look for color.
- **When a keyword target is extremely high-difficulty and the site has weak internal linking/backlinks:** stop pushing the head term; go narrower/lower-difficulty, including adding a location modifier (e.g. "Texas website hosting" if most clients are in Texas), to get traction faster.
- **Title tag keyword ordering:** if the primary keyword is buried after a modifier (e.g. "Colorful and Cute Combat Boots"), move the primary keyword to the front — provided keyword research confirms it's the higher-value term.
- **Meta description length:** shorten to roughly 140–145 characters so it doesn't get cut off in search results.
- **Fixing heading hierarchy so H1 is truly first:** find any H2/H3 tags used purely for nav/menu styling that render above the real H1 in page order, convert those to div or plain paragraph tags, recheck the page visually, and patch with CSS if the tag swap breaks formatting.
- **Shopify Dawn theme H1 fix specifically:** open the theme.liquid file, find the existing (often generic/ugly) H1 tag, change it to a div or paragraph tag, verify formatting after.
- **Trimming AI-sounding/keyword-stuffed copy:** e.g. rewrote "Why Rainbow City Colorful Cute Combat Boots Are Different" down to something like "Cute combat boots are different."
- **Testimonial/review sections:** always external-link each testimonial to its actual source (Google, Yelp, a specific review page, etc.).
- **Accordion/toggle content with thin copy:** expand the content behind each toggle to include the target keyword/variations rather than one short line; if there's nothing substantial to say, skip the toggle entirely and list the content directly instead.
- **CRO-adjacent fixes flagged as beyond pure SEO but worth doing:** make scroll-arrow buttons bigger/bolder if easy to miss; add padding to balance an off-center carousel start; fix low-contrast (thin light-gray-on-white) text; place a CTA button near end-of-page content (e.g. beside a sizing chart) so the page doesn't dead-end with nothing left to click.
- **Compounding authority into one target page:** keep adding internal links to it from new blog content over time — this alone can be enough (see Hey Tony's own SEO page case study below).
- **Homepage title tag fix for a branded intro (e.g. "Welcome to Teton Excursions... Teton Excursions"):** replace with the actual money keyword up front ("Yellowstone Tours"), then extend with researched modifiers ("multi-day Yellowstone tours," "national park tours").
- **Rewriting generic on-page intros that read like a blog post and never mention the keyword:** either move the section further down the page or replace it with keyword-relevant copy (e.g. benefits of a guided tour).
- **Making generic section headers keyword-specific:** "What our customers say" → "What our customers say about our Yellowstone tours"; repeat per-product on individual tour/product pages (reviews heading made specific to that exact tour, not a reused generic block).
- **Finding where uneditable on-page text lives:** check if it's a plugin/shortcode-generated block (e.g. something like `[testimonials]`); if so, the copy must be changed in the plugin's settings, not the page content editor.

## Rules / dos & don'ts

- **One keyword per page** — site-wide rule, no exceptions: "you want to rank for one keyword per page... focus on that singular keyword per page."
- **Never use the company/brand name as an H1** (or any header tag) — it's assumed knowledge; put it in a normal paragraph or H2 if needed at all.
- **Don't put the brand name in H2s on non-homepage pages** (service/product pages) — unnecessary; brand-name ranking happens automatically if everything else is done right. More acceptable on the homepage, especially for a brand-new business establishing itself.
- **H1 must be the literal first heading** to appear in the page's rendered/DOM order — nav or other elements using H2/H3 above it breaks this and must be fixed.
- **Heading hierarchy explicitly matters for SEO** (confirmed directly: "does hierarchy matter when you're doing header tags? Yes.").
- **Meta description target length: ~140–145 characters** to avoid truncation.
- **CTA/button copy can use the exact target keyword directly** — no need to create a "natural" variation specifically for buttons.
- **Always check keyword research (SEMrush, Ahrefs, or similar) before changing a page's target keyword** — never assume a desired phrase has search volume.
- **Don't overwrite a page that's already ranking well** for a keyword just to chase a new one — build a separate page for the new target and keep the old page/keyword intact.
- **Click depth (crawl depth) — clicks from homepage to reach a page — has recently mattered more** for getting service/product pages to rank (per Hey Tony's own internal testing); minimize unnecessary extra clicks (e.g. a hover-menu turned into a click-to-open menu costs an extra click).
- **Testimonial/review blocks should always external-link to the original source.**
- **~90% keyword difficulty is a red flag for a low-authority site** — cited for "web hosting," "VPS hosting," "shared hosting"; these require heavy internal linking + backlinks + content investment before they'll move, not realistic as a first target.
- **Local ranking approach: always start in the smallest viable geographic area, win it, then expand outward** — don't go wide immediately.
- **Domain/brand renames: always use a 301 redirect** from old to new to preserve authority.

## Tools, prompts & resources

- **pagespeed.web.dev (PageSpeed Insights)** — free Google tool, analyzes one page at a time for speed/technical SEO/accessibility with separate Mobile and Desktop scores.
- **Hey Tony Page Audit tool** — free Chrome extension built by Hey Tony; type in a target keyword and it returns keyword occurrences and keyword density for that page. Functionally similar to Detailed SEO.
- **Detailed SEO** — Chrome extension, Denroy's personal daily-driver ("a much older tool," used out of habit rather than because it's objectively better).
- **SEMrush / Ahrefs** — named for checking search volume and keyword difficulty ("almost anything" works, not tool-exclusive).
- **Google Search Console** — used to check current indexing status and existing rankings before making keyword/content changes.
- **Chrome DevTools** — Inspect → toggle device toolbar for mobile emulation/preview.
- **Cloudflare** — named as an example CDN to defer scripts through for page-speed gains.
- **Yoast SEO (WordPress plugin)** — SEO title and meta description fields live here, positioned just above the URL slug in the page editor.
- **WordPress builders named:** Avada (Denroy's personal favorite, paired with WooCommerce, used across many Hey Tony client sites — "we've used Avada the most of any WordPress website builder"), Elementor, Divi.
- **Shopify Dawn theme** — default H1 tag lives in the theme.liquid file.

## Case studies / examples / results

- **Hey Tony's own SEO service page:** left un-optimized for roughly 3 years, but reached the #1 ranking spot purely from cumulative internal linking out of "dozens of blog posts" over time — cited as direct proof that internal linking alone can carry a page to the top.
- **Hey Tony's own local rollout:** starts in Hamilton (Matt's home base) before expanding outward to cities like Toronto or Windsor — the model used for "win small area, then expand."
- **Katie (Wix site):** mobile PageSpeed issues traced to a purchased template with heavy scripts/animations; fix path = developer script cleanup + Wix support ticket + disabling non-essential mobile animations.
- **Anthony (NJ Dumpster Rentals → full waste-hauling brand, "Jersey Specialized Hauling"):** homepage currently ranks well for "NJ Dumpster Rentals"; plan is to keep that page/keyword and its ranking signal intact while building a "Waste Solutions"-targeted homepage, and consolidate dumpster-specific keyword strength onto the existing dedicated dumpster service page. (He also raised a question about safely changing the Google Business Profile category without risking suspension — not directly answered on the call.)
- **Lux (mechanics-lien company, branded "Northwest Lien," planning rename to "NW Lien Service" for nationwide expansion):** California-focused for now, getting high traffic from California but poor conversion; site on WooCommerce with a hidden/extra-click nav menu flagged as both a UX and click-depth problem; considering Avada as the new theme after current developer called the existing build "unnecessarily complex."
- **Thomas (web hosting company, site ~2 years old):** only the homepage indexed in GSC; targeting "web hosting," "VPS hosting," "shared hosting" (all cited at ~90% keyword difficulty); had already requested indexing and removed spam backlinks, but had near-zero internal linking from blog to service pages and a thin About page competing with the homepage for brand-name ranking. Existing "internal links" were white/unstyled text, easy to miss on a visual scan.
- **Heather (clothing brand, "cute combat boots" product line):** building a dedicated money page targeting "Cute combat boots," confirmed via her own keyword research as high search volume / low keyword difficulty; site runs Shopify's Dawn theme, which had a stray H1 ahead of the true H1 in the theme code; page already had good fundamentals (canonical link present, all images alt-tagged, single H1).
- **Aaron (Teton Excursions, Yellowstone-area tour operator, WordPress + Avada):** homepage title tag led with "Welcome to Teton Excursions... Teton Excursions" instead of the money keyword ("Yellowstone Tours"); business sells mostly multi-day tour packages but treats Yellowstone tours as the flagship/"wheelhouse" product; reviews sections on both the homepage and individual tour product pages needed keyword-specific headings rather than generic "What our customers say." He also raised a site-speed concern, but the call ran out of time before it was addressed in detail.

## Notable verbatim quotes

- "You want to rank for one keyword per page. You want to focus on that singular keyword per page."
- "That should never be a title tag. I mean a header tag." — on why a company name should never be an H1.
- "When Google send its crawl bots to scrape a site, one thing you always want to look out for is click depth, sometimes considered crawl depth... click depth seems to matter a lot more for getting service pages, product pages ranking higher."
- "When you're trying to rank locally, one thing you always want to do is start in a much smaller area, and then once you win that area, start branching outwards."
- "You will rank for your brand name no matter what you do. As long as you're doing everything else right, your brand name will rank no matter what."
- "Otherwise why are these in dropdowns? They could just be listed as is." — on thin accordion/toggle content.
- "Very often with templates, not just on Wix, Shopify, WordPress, there is some unnecessary code in there that can... slow things down."
- "We didn't optimize it for I think three years and over time from just internal linking to it from dozens of blog posts, it eventually got to that number one spot."

## Tradeoffs & nuance

- **Keeping an existing ranking vs. rebranding a page's keyword:** don't force a rewrite where a page already ranks well — build a second page for the new target and let the two divide the keywords, provided their content doesn't overlap/compete.
- **Aggressive keyword targets vs. site authority:** chasing a ~90%-difficulty head term (e.g. "web hosting") is possible in theory but impractical without heavy internal linking/backlinks first; the recommendation was to deliberately go narrower/lower-difficulty (including going local) for faster wins rather than keep pushing the harder term.
- **Design vs. SEO tension acknowledged directly:** a designer not wanting an ugly default H1 element visible is valid, but the underlying heading hierarchy still needs fixing — resolved by demoting/hiding the tag visually via CSS rather than skipping the SEO fix.
- **CRO advice explicitly flagged as adjacent to, not part of, core SEO** (button visibility, padding, contrast, end-of-page CTA placement) — offered anyway because it affects whether ranking traffic actually converts, but called out as a separate concern from the ranking work itself.
- **Brand name in headings:** acceptable on the homepage (especially for a new business establishing name recognition) but explicitly unnecessary on inner service/product pages.
- **Platform constraints change what's fixable directly:** Wix limits user-level access to hosting/speed settings (must go through Wix support); WordPress/Shopify issues (theme.liquid, plugin shortcodes) are usually fixable by a developer with code access — the practical fix path depends entirely on the platform.
- **Tool choice (Detailed SEO vs. Hey Tony Page Audit tool)** flagged as personal habit/familiarity, not one being objectively better — described as functionally equivalent.
