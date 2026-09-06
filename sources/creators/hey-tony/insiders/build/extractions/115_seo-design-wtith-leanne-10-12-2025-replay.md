# SEO Design with Leanne — 10.12.2025 (Leanne Jones, Leanne Digital)

## Tactics & step-by-step how-to
- Two-tool audit before touching any redesign: (1) paste the URL into **Google PageSpeed Insights** for speed/image/alt-tag errors, (2) paste the URL + target keyword into the **Hey Tony Site Audit tool** for heading-structure/keyword errors — log every finding to a doc before designing anything.
- Run a second, separate **design audit** using designer judgment on top of the SEO audit: headline clarity, copy quality, image relevance, wall-of-text, over-centered alignment — treat SEO errors and design errors as two distinct passes.
- Clone the live page in the builder and rebuild the clone; keep the original live until the rebuild is ready, then publish over it.
- Turn off default entrance/animations on cloned elements — "not necessary," people want the content, not "a bunch of pizzazz."
- Rewrite all copy in a doc first with explicit H1/H2/H3 structure marked, before touching the builder.
- Rule of thumb: **every H2 = its own section** (one container/visual block per H2) — makes content easier to digest.
- When moving written copy from Google Docs into the builder: paste into the **code editor** view first (strips Google's inline styling), then switch to the visual editor to style it — pasting straight into the visual editor carries forward all the Doc's styling and will fight your page styles.
- Alternate layout patterns section-to-section to avoid monotony and improve scannability: hero (left-align + CTA) → full-width center-aligned intro → 3-column icon grid → text/image → image/text → text/image → about section (photo swap) → center-aligned closer → FAQ accordion → final CTA block.
- Build a 3-column grid: one parent container, three child containers inside it (duplicate the child 3x), then set the parent's direction arrow so children stack horizontally.
- Build a 2-column (half/half) layout: one parent + two child containers, direction arrow set horizontal. To "flip" the pattern for the next section (image-left vs. image-right), just swap/drag-and-drop the two containers' order instead of rebuilding.
- Add an icon above each H3 in a multi-column feature section to visually reinforce the topic (e.g., a pen icon for "custom logo design," a multi-mark icon for "brand identity," a book icon for "digital/printing/branding assets/brochures"); style icons in the brand accent color; left-align icon + heading + body together.
- Name every container/section in the builder's layer panel (e.g., "Intro," "Services," "Process," "Why," "About Me") — pure workflow/handoff aid, not an SEO factor; makes it easier to find things or hand the file to someone else.
- Pick hero/section imagery specific to the exact service being sold (e.g., actual logo design examples for a logo-design page), not generic stock imagery.
- Image production pipeline: build/source the graphic in Figma or Canva → set the canvas to the actual target pixel size before exporting → export PNG only if transparency is needed, otherwise JPEG (smaller file size) → run the file through a WebP converter (e.g., Free Convert) for an even smaller final size → upload and fill in alt text for every image.
- Sizing rule of thumb for on-page graphics: if the image occupies roughly half of a ~1200px-wide content column, export at about 500–700px wide.
- Put a CTA button inside the hero section itself, not just at the page bottom, so a ready-to-buy visitor can convert immediately.
- Always add a final CTA block at the very bottom of the page, after all the convincing content — the whole page functions like a sales team that closes at the end.
- Check color contrast on any colored button/text pairing before shipping; swap the text color if it fails.
- Add border-radius to buttons as a matter of course for rounded-corner polish.
- Use padding (space inside a section) vs. margin (space pushing sections apart) deliberately — e.g., zero left/right padding but add bottom padding under a specific element for breathing room.
- Set spacing/padding in **em units, not pixels**, so it scales automatically across browsers/devices.
- After finishing the desktop design, switch to mobile preview and manually adjust font sizes per device.
- Vertically align an image with adjacent text via the container's "align items: centered" setting; accept that perfect alignment won't hold at every breakpoint — use judgment per section.
- Build FAQs with an accordion component; set the accordion title tag to H2 where the builder allows it (see tradeoff below on the time cost of doing this).
- Re-run both audit tools after the rebuild to confirm the score improvement before calling the job done.

## Rules / dos & don'ts
- Exactly **one H1 per page** — think of it as the book's title; every other heading nests under H2 or H3.
  - Exception: two H1s in the code are fine only if they come from separate desktop/mobile layout blocks (one hidden per breakpoint) with the exact same text.
- Never use a graphic/image as your H1 — H1 must be live, real text: Google can't read text baked into an image, and image-text doesn't scale responsively for mobile the way real text does.
- Footer titles above menu columns should be **H4 or smaller**, never H1/H2/H3 — those tags belong to the page's own content.
- FAQ question titles: use **H2** ("Matt recommends using H2 tags for the FAQs... he's the expert in that").
- Every image needs alt text, written to be descriptive of the actual image AND include the focus keyword where it fits naturally — dual purpose of SEO + screen-reader usability.
- Don't keyword-stuff — high keyword density reads as "gibberish to the average person" and gets flagged as an SEO error.
- Don't skip heading levels illogically (the audited page jumped from no H1/H2 straight into H3s and H5s with no structure) — flagged as a concrete error.
- Avoid big wall-of-text sections — nobody reads them; break copy into short, scannable chunks.
- Don't overuse centered-alignment text — harder on the eyes at length; left-align is easier to read, reserve centering for select sections for visual variety.
- Oversized images are a flagged page-speed error — check actual dimensions (right-click → open image in new tab) before shipping.
- Missing alt tags is a flagged error — always fill them in.
- Font-size rule of thumb: **H1 ≈ 48px, H2 ≈ 36px**, H3 smaller again; adjust in increments of 5 or 10px; exact number depends on the specific font (some fonts read bigger/smaller at the same size).
- Real photos of your actual business/product beat stock photos; if stock is unavoidable, at minimum pick images relevant to the specific service on that page, never generic imagery.
- Even a phone photo of your own business beats most stock photography for representing who you are.

## Tools, prompts & resources
- **Google PageSpeed Insights** — paste URL to surface image-size/performance/alt-tag issues.
- **Hey Tony Site Audit tool** (Matt's tool) — paste URL + target/focus keyword; returns an SEO score plus a specific error list (missing H1, keyword density, heading misuse, etc.).
- **Elementor** — the page builder used for the whole rebuild. Features used: nested containers + direction arrows for row/column stacking; per-widget heading-tag selector (set any text element to H1/H2/H3/H4); code-editor paste mode (strips inline styling) vs. visual editor; "align items centered" container setting; border-radius control; padding/margin controls with em units; duplicate-element workflow for speed; drag-to-reorder containers to flip a layout; accordion widget with configurable title tag for FAQs.
- **Figma** — used to store source graphics and a personal icon library ("loads of loads of icons").
- **Canva** — alternate graphic tool; lets you set an exact target pixel size on export.
- **Pexels** — free stock photo site, used as a fallback image source.
- **Free Convert** — free web tool to convert images to WebP for smaller file size/better page speed (rate-limited after a few conversions per session — hit the daily cap after "a couple trial sessions" live on the call). Alternative: some WordPress plugins or page builders auto-convert images to WebP.
- Target/focus keyword used in the demo: **"Winnipeg Logo design."**
- Example alt text written live: **"Winnipeg logo designer Leanne Jones"** (for the about-me photo).
- Example CTA button copy used live: **"Start your logo design."**

## Case studies / examples / results
- Subject: Leanne's own **Winnipeg Logo Design** service page, audited and rebuilt live on the call.
- Original page errors found: Hey Tony Site Audit score **71**; missing H1; keyword density too high (stuffing); zero H2s; H3s and H5s present with no logical structure; one image flagged by PageSpeed Insights as oversized and also missing its alt tag; vague headline ("designed to make your business stand out" — doesn't say what's being designed); weak copy ("Our company does logos"); generic stock imagery not specific to logo design; one section a big wall of text; one section over-using centered alignment.
- After the rebuild: Hey Tony Site Audit score went **71 → 96** on the same target keyword.
- Re-running Google PageSpeed Insights on the rebuilt page returned **97**, then a further check showed **"98 and 100%, basically"** ("I think we did a perfect job here").
- Example optimized image spec used in the rebuild: **500px wide × 375px tall** (about half the ~1200px content width).
- Hero CTA button styling used live: teal accent-color background, dark navy text (switched from white for contrast), **16px border-radius**.
- Hero section padding used live: **10em** bottom, 0 left/right.
- Icon-grid section padding used live: **4em** bottom, plus added top padding by feel.

## Notable verbatim quotes
- "We don't need to wow them with a bunch of pizzazz. We just want to give them the content in a way that's structured and makes sense."
- "My rule of thumb when I'm designing, every H2 tag should be its own section."
- On one H1 per page: "If it were a book, that would be the title of the book. And we don't have multiple titles for our one book."
- On the hero CTA: "if someone has already decided they want to shop with you, giving them the quickest way to do that is the best way to convert them."
- "It's kind of like our sales team here, our website" — describing the page's scroll-to-convert flow.
- On FAQ heading tags: "Matt recommends using H2 tags for the FAQs. So I would take his advice on that. He's the expert in that."
- On AI-written copy: "This is all generated with chat GPT, but I do like multiple rounds of refining it... making sure that it sounds like me and that it isn't like, too AI... I do take a lot of Matt's approach to writing copy."
- On duplicating text while designing fast: "sometimes when you're in the flow of it, you can forget that... you didn't update that text as well. And then you're looking at it and you see that you have three of the same headlines."
- "Sometimes the longest part of my job is just finding the right icons that visually represent the topic that I'm talking about."

## Tradeoffs & nuance
- Real/authentic photos of the actual business are always preferred, but stock (e.g., Pexels) is an acceptable fallback when no good representation exists yet — the non-negotiable is topical relevance over generic imagery, whichever source you use.
- Centered-alignment text isn't banned, just easy to overuse; deliberately mix left-align, center-align, and multi-column grids across sections for both readability and visual variety.
- Multiple H1 tags are normally wrong, but not automatically an error if they're a byproduct of separate desktop/disabled-mobile layout blocks carrying identical text — context (is it truly duplicated content or a breakpoint artifact) matters more than raw tag count.
- Styling an accordion's titles as true H2/H3 in Elementor is possible, but changing the tag reverts the element to default (dark) styling, requiring extra restyle time — under live-demo time pressure this was consciously skipped ("I don't think we have enough time to fix that. So I'm just going to leave it like this for now."), showing SEO-purity can lose to deadline/time constraints even in an SEO-focused rebuild.
- Vertically centering an image against a text block is a nice-to-have, not a hard rule — responsive design makes it impossible to guarantee perfect alignment at every viewport size, so it comes down to per-section designer judgment.
- AI-generated copy is a starting point, not a finished product — every page's content runs through multiple refinement passes to match the individual's voice and avoid sounding "too AI"; content is a paid deliverable bundled into the website design package price rather than billed as a separate line item, and clients get it as a jumping-off point to revise for their own brand.
- Animations are deliberately stripped out even though the builder supports them — treated as a distraction from content rather than a feature worth keeping.
