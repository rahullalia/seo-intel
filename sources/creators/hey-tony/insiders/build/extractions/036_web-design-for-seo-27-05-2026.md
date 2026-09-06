# Web Design for SEO — 27.05.2026 (Wix homepage build from Figma, live)

Source: HeyTony Insiders Call Replay (hash: 6DbdGYVbqz) | 66m 0s | ~8,371 words

## Tactics & step-by-step how-to

**New Wix site setup:**
- Dashboard, Create a New Site, skip every Wix AI-tool prompt (ADI wizard) deliberately, even if it re-offers, then Templates, Blank Templates, Start from Scratch: chosen specifically so attendees learn to build/modify from nothing rather than depend on a template.
- If you have a domain, connect it during site creation (skipped for this demo since it's a throwaway site).
- Global styles first, always: Site Design > Color Theme, before touching any page. Set up once so the rest of the build goes faster ("we've already done the thinking ahead of time").

**Color theme setup (Site Design > Color Theme):**
- Set base colors first: font color and background color, pasted in as hex codes copied straight from the Figma file (works the same pulling hex from Canva or any other design tool).
- Wix's color picker actively flags insufficient contrast in real time as you pick colors, called out as "a bonus with Wix."
- Accent colors are capped at exactly 4 swatches. Wix blocks adding a 5th ("it only lets me add in four").
- Personal technique for tracking a palette in Figma: build small filled rectangles as color swatches so the whole palette is visible at a glance instead of hunting through layers for hex values.
- Advanced Settings (under Color Theme) auto-assigns colors to titles, links, and buttons based on the base and accent picks; review and correct each one manually (e.g. retarget "titles" and "links" from the default gray to the brand teal if that matches your design).
- Button theming is the fiddliest part and can require real trial and error live: attempted a gold fill, Wix flagged the button text as failing contrast against gold, tried substituting gray, tried sourcing a darker gold specifically for the hover state (see hover rule below), hit the 4-swatch limit trying to add that new shade, and ended up setting hover to switch the fill to the teal accent color with white hover text instead.
- Hover-state design rule demonstrated: default Wix hover behavior is just an outline; override it. For a same-color hover, pick a darker shade of the same base color. Alternatively, swap to a different theme color entirely on hover (as ultimately done here: teal fill plus white text on hover).

**Typography setup (Site Design > Text Theme):**
- Pick a Google Font for headings (used Noto Serif); check/set weight to bold if your design uses bold headlines (Wix defaults it differently; verify against your actual live headline sample).
- Pick a second Google Font for paragraph copy (used Open Sans), and set the custom paragraph font size to 20px ("kind of the standard").
- Font-pairing heuristic (see Rules) justified the Noto Serif plus Open Sans combination.
- Page background: set to match brand color (used the primary teal as the page-wide background).
- Page transitions: set to None as a personal default.

**Pages and blog setup:**
- Pages panel, add each page as a blank page: About, Service, Locations, Contact (built in that pass).
- Blog is not added as a page. It's added as an app: Apps search, search "blog," wrong hits surface first (e.g. an unrelated "5 Loyalty" app), correct path is Apps > Communication category > Blog, confirm the listing is actually published by Wix ("WIX Blog") before installing.
- After installing, drag the auto-created Blog nav item into position immediately before Contact in the site menu, the typical nav placement convention.

**Logo setup:**
- Use Wix's global top search bar (not the sidebar), search "Logo," opens the logo/business-info panel; explicitly skip Wix's own AI logo generator that surfaces here.
- Export logo from Figma: click the asset, format dropdown, JPEG / PNG / SVG / PDF (PDF essentially never needed for a logo).
- Format decision tree: SVG is the smallest file size and ideal for a logo, but only works if the source art is genuinely vector-based; a ChatGPT-generated logo is a raster image, not a vector, so SVG export doesn't apply to it. PNG preserves transparency (needed if the logo sits on colored or photo backgrounds). If you can't isolate a transparent background, fall back to JPEG, a smaller file than PNG but one that drops any transparency.
- Upload two logo versions: a full-color version for the header, a white version for the footer (naming convention demoed: base name plus a descriptor, e.g. "Serenity logo" plus "color").
- Fill in the Business Info fields that populate here (business name, category, demoed with "Personal Services").

**Header build:**
- Add Section, blank section, double-check it actually landed inside the Header region (it can silently not attach there).
- Add Element > Strip > Classic Strip ("a container within a container" that supports columns).
- Layout, add 2 columns (one for logo image, one for nav).
- Add Element > Image, drag into the first column; Add Element, search "menu" (wrong hits surface first), Menu Anchors, choose the Theme Menu variant specifically (it auto-inherits the site's theme colors and typography rather than needing separate styling).
- Manually shorten the header's height as much as possible: a deliberate prioritization of the hero section below it as the site's real "valuable real estate" for the core message.
- Switch to the mobile/phone preview icon and manually rearrange header elements if the auto-generated mobile layout looks off.

**Hero section build:**
- Click the hero section, change its background type to Image (not color); double-check via the Layers panel that the actual image layer is the one selected, not a different element in that section.
- Export the hero photo from Figma using a descriptive, keyword-bearing filename (demoed: "massage therapy"), framed as a minor, optional SEO nudge, not a real ranking factor.
- Upload Media, drag and drop the image in as the section background; increase the section's height afterward so the image has room to breathe.
- Add the headline as an H1 text element (Add Elements > Text > H1), position it, paste in the Figma copy, then manually recolor it (white, in this case) since the theme default color won't have contrast against a photo background.
- Verify the actual semantic tag, not just the visual style: open Edit Text, scroll to SEO and Accessibility, HTML tag dropdown; lets you set H1/H2/paragraph/etc. completely independent of font size, since "just because the font is bigger" doesn't mean the tag is actually an H1.
- Add supporting copy as a Theme Text element (not a generic paragraph box) specifically so it inherits the site-design paragraph styling already configured; recolor white to match the background image.
- Add a Theme Button: label it with the real CTA copy ("Book a massage appointment"); if the theme's configured button color doesn't actually show up on the placed instance (happened live, expected gold, got something else), manually reset Design > Customize Design > Background Fill (and separately set its own hover Background Fill state too, layered independent of the earlier global theme hover setting).
- Set the button's Link: Choose a Page, e.g. Contact, or, for businesses using a dedicated booking tool (mentioned as "JN app," almost certainly "Jane App," a scheduling platform common with massage therapists), link out to that instead.
- Resize the button box if the label text is visibly clipped after applying the link.

**Star-rating strip (inside the hero):**
- Add Elements > Decorative > Basic Shapes, pick a star shape. Wix's own basic shapes render as true SVGs internally, so the fill color is fully editable (set to gold here).
- Duplicate that star (rather than re-adding from the library) to build the row quickly.
- Add an adjacent text element: "Rated five stars on Google"; hyperlink it directly to your business's real Google review link (pulled from your own Google Business profile) so it both showcases and collects reviews.
- Recolor that text white; remove its default underline, and note the control isn't where you'd expect ("Change Text Direction" is the wrong stop); it's a separate Underline toggle.
- Multi-select technique: click one element, then Shift-click the rest, to move/align a whole group (stars plus text) together in one action instead of nudging each individually.

**"Why Choose Us" section:**
- New blank section, Add Elements > Text > H2, paste the Figma copy ("Why choose Winnipeg Massage Therapy Clinic"), center-align.
- Turn on Wix's boundary-outline toolbar toggle so section/container edges are visible while positioning elements precisely.
- Use the alignment icon panel to center horizontally; when vertically positioning, "align to top" exists but deliberately don't snap all the way to the top edge; leave a whitespace margin above the heading for readability.
- Add a supporting paragraph beneath it the same way (Add Elements > Text > paragraph), center-align, resize the text box, re-center via the alignment tool; considered bolding this subhead line too.

**Four-column feature grid (only column 1 completed live, time-boxed):**
- New blank section, Add Element > Strip > Classic Strip, Layout, add columns up to 4 total via Manage Columns.
- Measure the exact horizontal gap between columns directly in the Figma file (a "designer trick" using onscreen measurement squares); found 32px, set that as the column gap value in Wix.
- Check the Figma container's internal padding too; found 26px, but when applied in Wix it landed on the strip container instead of the intended scope, so it was zeroed back out rather than kept at 26px. A reminder to check which layer a padding value is actually hitting before trusting it.
- Select each column individually, Design panel, set corner radius to 16 to match the rounded box style from Figma.
- Locate the edge-to-edge vs. contained-width toggle (Stretch); not obvious where it lives (checked Shape Dividers and Animation Effect first, both wrong); toggle it off so the strip sits within the site's normal margins instead of running full-bleed.
- For the per-column icon: export it from Figma as SVG (it's vector art), Upload Image, drag into the target column; vector scales up or down with zero pixelation, unlike a raster export.
- Add paragraph text under/beside the icon, resize the box height to match the design, then repeat the whole column pattern 3 more times to finish the grid (not completed live; ran out of time after the first column).

**Post-build workflow (WordPress/Elementor plus GSC and sitemap, from Q&A):**
- Editing meta title/description without leaving Elementor Pro's visual canvas: inside Elementor, open Page Settings; Rank Math or Yoast's meta box is available right there. (Matt's own personal habit is still to exit to the plain WP admin Pages > Edit screen and scroll down to the same Rank Math/Yoast box there instead.)
- Cloning a page instead of Elementor's "save as template" flow: WP admin > Pages, hover the source page, Clone; works even on an Elementor Pro built page. Immediately update the clone's Title and URL/slug afterward so it doesn't sit live as a duplicate (e.g. "about-2").
- Requesting fast indexing on a brand-new page: Google Search Console > Pages report (the "Discover / not indexed" tab is the wrong stop), All Known Pages tab, paste the specific page URL in, Request Indexing.
- Troubleshooting one SEO tool reporting "no sitemap" while other tools see it fine:
  1. WP admin > Settings > Reading: confirm the "Search Engine Visibility" checkbox is unchecked (checking it blocks all robots from crawling the entire site).
  2. Yoast > Tools > File Editor, open robots.txt, confirm the sitemap URL line actually points at the real domain, not a stale placeholder like "yoursite.com"; fix and Save if wrong.
  3. Paste the sitemap URL directly into a browser address bar to confirm the XML file itself actually renders. If it does, the sitemap exists and the problem is discovery (robots.txt / crawl visibility), not the sitemap itself.
  - Root cause not fully resolved live for Keith; deferred to a follow-up look at his site link.

## Rules / dos & don'ts
- Skip Wix's (and any platform's) AI site-builder wizard if you want actual control over the build: a deliberate, repeated choice on this call.
- Set global colors and fonts (Site Design) before building any page. Do the "thinking" once, up front.
- Accent-color swatches: max 4 in Wix's Color Theme panel; plan your palette to fit that ceiling.
- Button/CTA rule: only ever put visual focus on one primary call to action per view; if a second CTA exists, it must read as clearly secondary. "Makes the choice a lot easier for people."
- Hover-state rule: same color, just darker; or, if switching colors entirely on hover, also swap the text color for contrast (e.g. teal fill plus white text).
- Font-pairing rule: pair one "spicy"/interesting font (headings) with one "boring"/plain font (body). The contrast is what creates visual hierarchy; two competing "interesting" fonts fight each other.
- Paragraph/body font size: 20px treated as the standard baseline.
- Column gap and corner-radius values must be measured from the actual design file, not eyeballed. Demoed at 32px gap, 16px corner radius.
- Verify padding actually lands on the element you intended before trusting the number in the design file; the same padding value can apply at the wrong scope (strip vs. column) depending on where you set it.
- Page transitions/animations: default to none; fewer animations directly helps page load time.
- Header height: keep it as small/short as possible. The hero section is the highest-value "real estate" on the page and shouldn't be pushed below the fold by an oversized header.
- Logo file format: SVG only if the source art is truly vector; PNG when transparency is required; JPEG (smaller, no transparency) as the fallback when a transparent background can't be produced.
- Upload two logo versions to a site: a color one (header) and a white one (footer).
- Blog is added as an app, never as a page, in Wix.
- Blog nav position: immediately before Contact Us.
- Don't assume a big font automatically means an H1 tag; always verify/set the actual HTML tag explicitly (SEO and Accessibility panel), independent of visual styling.
- File-name keyword stuffing on exported images is a harmless minor SEO nudge, not a real ranking lever: "not needed for SEO, but any little bit helps."
- Sitemap: never resubmit in Search Console more than once, except after a full site redesign; new pages get picked up automatically via re-crawl.
- WordPress "Search Engine Visibility" checkbox (Settings > Reading) must stay unchecked, or robots are blocked from the entire site.
- After cloning a WP page, update both the Title and the URL/slug; don't leave the auto-generated duplicate slug live.

## Tools, prompts & resources
- **Wix**: full site build demoed live. Blank-template flow, Site Design (Color Theme, Text Theme, Advanced Settings, Page Background, Page Transitions), Pages panel, Apps marketplace (Blog), Strip/Classic Strip element with Manage Columns, Menu Anchors > Theme Menu, Decorative > Basic Shapes (native SVGs), Edit Text > SEO and Accessibility HTML-tag override, and the global top search bar as a shortcut to jump straight to settings/elements instead of browsing nested menus.
- **Figma**: source design file for the whole build. Used for hex-code color values, the export panel (JPEG/PNG/SVG/PDF), a swatch-box technique for at-a-glance palette reference, and a measurement technique ("squares") for pulling exact pixel gap, padding, and corner-radius values straight from the design.
- **ChatGPT**: used previously to generate the demo logo artwork; flagged as producing a raster image, not a vector, so it can't be exported as a true scalable SVG. No exact generation prompt text was quoted on this call.
- **Google Fonts** (fonts.google.com): browse, filter, and live-preview fonts before choosing a pairing; no dedicated pairing-preset resource was offered beyond the "spicy plus boring" heuristic.
- **Creative Market**: source for downloadable logo templates that include both SVG and vector-based artwork files.
- **Google Search Console**: Pages report (All Known Pages tab) used to paste a URL and Request Indexing; also covers sitemap resubmission guidance.
- **Yoast SEO** (WordPress): Settings for sitemap location; Tools > File Editor for direct robots.txt editing/verification.
- **Rank Math** (WordPress): Matt's own preferred SEO plugin; meta title/description editing referenced alongside Yoast.
- **Elementor Pro** (WordPress): Page Settings panel houses the Rank Math/Yoast meta box without leaving the editor; page Clone action (hover a page in WP admin > Pages) as the fast alternative to Elementor's "save as template" flow.
- **Google Business reviews**: link copied directly from the business's own review page to hyperlink a "Rated five stars on Google" element.

## Case studies / examples / results
- **Demo build**: a fictional "Winnipeg Massage Therapy Clinic" (logo file named "Serenity logo"), rebuilt live in Wix from a Figma design developed over "the past... couple months" of prior sessions. Completed live: full color theme and text theme setup (Noto Serif headings, Open Sans 20px body), header (logo plus Theme Menu, 2-column strip), hero (background photo, H1 headline, theme-text subhead, "Book a massage appointment" gold CTA button linking to Contact, 5-star gold rating row linked to Google reviews), and a "Why choose Winnipeg Massage Therapy Clinic" H2 plus subhead section. The four-column feature grid was started (32px gap, 16px corner radius, SVG icon, paragraph copy) but only 1 of 4 columns finished before time ran out.
- **Attendee whose name transcribes inconsistently as Maritzi/Maritia/Lian**: has a pre-existing, unresolved border issue on her live site's menu; Matt had already applied CSS to force the border to disappear before this call. Side effect surfaced live: the menu items' hover color-change effect (home/locations text changing color on hover) stopped working, suspected tied to that same earlier CSS fix. Matt deferred a fresh, more scoped fix to after the call.
- **An attendee referred to as "Leanne"**: during the color-theme setup, flagged that Matt's chosen "black" font-color hex (393939) is actually a dark gray, not true black. Matt confirmed.
- **Lupita**: asked for (1) a previously shared Google Drive link containing custom-icon resources, and (2) a resource showing pre-paired Google Font "sets" (primary plus secondary shown working together), since she's struggled pairing fonts herself ("when I find the fonts that I like and I try to bring them together as a set... they don't match well"). Matt had no dedicated pairing-preset resource to point to, gave the spicy/boring heuristic instead, and pointed her to Creative Market for logo templates, noting the tradeoff between unique-but-non-vector AI logos and vector-but-non-unique purchased templates. Offered to possibly post logo-designer recommendations in the Hey Tony community group afterward.
- **Keith**: WordPress plus Elementor Pro user on Rank Math, joined late. Three issues worked through: (1) couldn't find where to edit page meta title/description without leaving Elementor, resolved via Elementor's own Page Settings panel; (2) didn't know about page-cloning, had been manually rebuilding pages via Elementor's "save as template" flow, shown the WP admin Pages > Clone shortcut instead; (3) one of the "HT Insiders" community's own SEO tools was reporting his site has no sitemap while other tools reported it fine, walked through the WP Reading-visibility checkbox and Yoast robots.txt checks live, root cause not conclusively found on the call, deferred to a private follow-up.

## Notable verbatim quotes
- "I want the control. So I'm just going to skip all of their AI tools here." (on bypassing Wix's AI site builder)
- "We always want to put the focus on one call to action and then have like a secondary call to action. But we want to make sure that there's only focus on one. That just makes the choice a lot easier for people."
- "I prefer almost no animations unless like is absolutely necessary because it will help your page load times, the less animations that you have."
- "You want one font that is... kind of more spicy, more interesting. And then you want the paragraph font just to be more boring... you want contrast, so... now there's a little bit of hierarchy."
- "This section of our website is super valuable for real estate... we want to make sure that we have our message as clear as day when someone is arriving on our site." (on keeping the header small vs. the hero)
- "We think just because the font is bigger, it means it's an H1, but that isn't always the case."
- "That's the one con with Squarespace... to make it an H1, it has to be styled as the global H1." (on why Matt doesn't typically recommend Squarespace)
- "We can kind of sneak in some extra focus keywords in our file names as well. It's not needed for SEO, but... any little bit helps."
- "AI is a little bit better that way because then you get a unique logo... but a lot of designers aren't super happy with AI right now."
- "You don't need to enter in your sitemap more than once. Unless you just did a complete redesign of your website, then you would want to resubmit your sitemap."
- "It's like none of them suck. Okay. They all do. Good. As long as you are comfortable working on it." (on WordPress vs. Wix vs. Webflow vs. Squarespace: no platform is objectively bad, pick whichever you can maintain yourself)
- "I wouldn't get too focused on whatever platform you're using. Use whatever platform works best for yourself, whatever you are most comfortable with... I think those are the best websites for you, rather than focusing on the exact platform."

## Tradeoffs & nuance
- PNG vs. JPEG for logos: PNG preserves transparency but is a larger file; JPEG is smaller but drops transparency entirely. The choice is dictated by whether you can actually isolate a transparent background, not just "which is better."
- SVG only pays off over a raster export when the source art is genuinely vector. A ChatGPT-generated logo looks fine but is technically a standard raster image, so it doesn't get any SVG benefit even if exported with an .svg extension.
- AI-generated logos vs. purchased template logos (Creative Market): AI gives a unique mark but non-vector artwork, workable only if you find an "AI-friendly" designer willing to vectorize it ("a lot of designers aren't super happy with AI right now"); a purchased template gives clean SVG/vector files immediately but isn't unique since anyone else can buy the same one.
- Theme-level styling doesn't reliably cascade to every placed component. The hero CTA button didn't inherit its expected gold theme fill live, meaning per-instance manual overrides (fill, hover fill, hover text color) should be expected even after global theme setup is "done."
- Edge-to-edge ("Stretch") vs. contained-width layout is a real per-section design decision in Wix, not a fixed default. Toggled off here to keep the 4-column grid inside the site's normal margins, but the setting exists precisely because some sections do want full-bleed.
- Platform choice is explicitly framed as a non-issue in general ("none of them suck... they all do"), with one concrete, real exception called out: Squarespace forces H1 elements into a single global H1 style, so headline size and semantic tagging can't be decoupled the way Wix (and implicitly WordPress/Elementor, via Rank Math/Yoast's own settings) allow.
- Keyword-bearing image filenames are explicitly downgraded to a "nice-to-have," not a real SEO lever, contrasting with the weight given to on-page tag structure (H1 verification) elsewhere in the same session.
- Sitemap troubleshooting nuance: a sitemap file existing and rendering correctly (verified by pasting its URL into a browser) doesn't guarantee tools/crawlers can find it. Visibility settings (WP's search-engine-visibility checkbox) and the sitemap reference inside robots.txt are separate failure points from the sitemap file itself.
