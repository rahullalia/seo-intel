# Web Design for SEO — 04.02.2026 (Leanne Jones, Leanne Digital)

## Tactics & step-by-step how-to
- **Design-first workflow**: mock up every page in a design tool (Figma, or Canva/Photoshop — "whatever works best for you") before building live in the page builder. Lets you work out layout/spacing "kinks" cheaply before you're constrained by the builder.
- This design-first step is **optional, not mandatory** — building straight into the page builder and iterating there is a valid alternative.
- **Figma setup for a new interior page**: hold Option and duplicate the homepage frame, then delete all inner elements — keeps the new page on the same canvas/frame settings as the homepage so the site stays visually cohesive (same colors throughout = visitors don't feel like they left the site).
- Frame preset used: "Desktop" (shown as "Desk" in-tool); expand/resize by holding Control.
- For mobile mockups, switch the frame preset to a phone size (e.g., "iPhone 17") to check how font sizes and spacing actually look on a real device width, independent of desktop settings.
- **Layout guide / grid**: set a 12-column grid, centered, when creating a new frame — this is what organizes every section consistently.
- Keep a running Google Doc of your design-system specs (grid, colors, spacing) as you build, so you can share the spec sheet with your team/community afterward.
- **About-page structure built live** (Winnipeg massage therapist example), in order:
  1. Hero: brand-color full-width background, white H1 with a manual (true) line break at a natural reading point, plus a short one-line "approach" subheading directly under it (a longer paragraph was cut down for being "a little bit too long").
  2. Centered H2 trust/benefit statement referencing keyword + location (e.g., "Helping Winnipeg clients feel better with their bodies").
  3. Two-column module: left-aligned text (~half page width) + a stock photo chosen to reassure on a specific objection, on a full-bleed light-teal section background (send the background rectangle to the back of the layer stack so it doesn't cover the content).
  4. Mirrored two-column module, "Why I became a [role] in [city]" — features a photo of the actual practitioner/founder to humanize the brand ("you are a real person, not just a stock photo template").
  5. CTA section (every page needs one): a narrower rounded container nested inside the full-width section, brand-color background, white centered heading + line, then a contrasting accent-color button linking to the booking/contact action.
- **Reuse homepage styles** for interior pages: literally copy the already-styled H1/H2 text layers from the homepage frame and paste them into the new page frame so font, size, and color match without re-styling from scratch.
- **Preview cohesion**: hit Figma's "Play" button to enter prototype view, then toggle between frames (homepage vs. about page) to visually confirm the pages feel like one site.
- **Image sourcing**: use Pexels (free stock photos) when you don't have real product/team photography yet. Pick images for the *feeling*/vibe you want (e.g., "a professional, comfortable, consent-based massage therapy experience" — directly answers a customer's unspoken fear), not just literal subject matter.
- **Adding visual depth without more literal photos**: layer a secondary mood/texture image (example used: rocks, to evoke a calming massage vibe) behind or beside the main photo, add rounded corners to it, and mute/reduce its opacity slightly — reads as intentional design rather than "copy and paste."
- **Export workflow**: crop/export each image at the exact pixel size of its placeholder frame in Figma ("building everything to scale") so nothing is oversized on the live site — protects page load speed.
- **Export format rule**: export as JPEG by default (smallest usable size); only export as PNG when you need transparency (e.g., a logo). Figma can't export WebP directly — rely on your page builder/host's own image plugin to auto-convert uploads to WebP.
- Figma has a built-in background-removal tool — useful for stripping a logo's white background before exporting it as a transparent PNG.
- Always write descriptive, keyword-and-location alt text on images (e.g., "Winnipeg massage therapist giving a relaxing massage"; refined "giving" to "providing" as the better word for a second image).
- **Live build in WordPress + Elementor** (mirroring the Figma mock 1:1):
  - In Page Settings, hide the auto-generated page title, then build your own styled H1 inside a container instead.
  - Set container background via Style → Background Type → Classic → paste in the exact brand hex code copied from the Figma fill.
  - Explicitly set each text widget's HTML tag (H1, H2, etc.) — visual styling alone doesn't make it a semantic heading.
  - When pasting copy from a Google Doc/Word doc, paste into the **code editor**, not the visual/WYSIWYG editor — the visual editor silently carries over hidden style tags from the source document and can make the text render wrong.
  - Two-column sections = one full-width "parent" container holding two "child" containers; set the parent's layout direction so the children sit side-by-side instead of stacking.
  - Use Layout → "Align items: center" on a row container to vertically center text against an adjacent image column.
  - Padding fields have a link/unlink toggle — unlink it to set top/bottom (or per-side) padding independently instead of uniformly.
  - Preview an unpublished page via Save Draft → Preview rather than publishing it live.
- Verify on-page SEO post-build by checking that your target keyword + location actually appear across the H1 and H2 tags (confirmed live: "massage therapist," "Winnipeg," "Winnipeg massage therapist" all present).
- Next step flagged but not done live (ran out of time): a dedicated mobile-responsiveness pass on the built page in Elementor.

## Rules / dos & don'ts
- Purpose of an About page: it is **not** "our life story" — it's a trust page. Visitors are checking if you're a real person, whether you can help with what they need, and if it's a good fit.
- Keep the same color palette across every page — never let an interior page look like a different website.
- H1 tags should be descriptive, not "showy" — both the human reader and Google need to understand the page topic immediately.
- **Never right-align** body text — reading direction is left-to-right, so it's uncomfortable to read.
- **Minimize center-aligned text** too — fine for a short H2/headline, but don't overuse it; it's harder on the eyes than left-aligned copy for longer blocks.
- Every page on the site must end with a CTA section telling the visitor what to do next.
- Aim for **at least one visual element per section** — a photo, icon, or graphic — or the page reads as bland "text title, text title" regardless of copy quality.
- **Grid**: 12 columns, centered; column width 72px; gutter (space between columns) 32px.
- **H1 style** (this build): Noto Serif (Google Font), white, text-transform capitalize, centered, font-size 60px, line-height 83.
- **H2 style** (this build): brand teal, font-size 40px, line-height 60.
- **Line-height rule of thumb**: start the line-height value equal to the font-size in pixels, then nudge it up by eye until no line touches the descenders (g/y/p) of the line above/below.
- **Standard section padding** used throughout: 94px top and bottom.
- **CTA inner box**: nested container 1140px wide, 16px border-radius, ~100px internal padding, button also ~16px border-radius.
- **Desktop hero side-padding trick** (used to force a visual line break instead of a hard return): 255px left and right.
- **Mobile equivalent of that same padding**: shrink to ~50px left/right (255px would exceed an entire iPhone-17-width viewport) — and likely shrink the font size too so it still fits.
- Body copy font color: not pure black — use a slightly gray shade; it's easier on the eyes and reads more polished, as long as contrast stays sufficient.
- On tinted/light section backgrounds, keep text close to white with just a hint of the brand hue rather than the full saturated brand color.
- Export rule: JPEG by default (smallest file size); PNG only when transparency is needed (logos) — PNG keeps transparency but is larger; convert to WebP via your host/builder's own plugin (Figma can't export WebP itself).
- Never let two "About your X" duplicated text boxes stack in a way that produces two separate H1 tags — one H1 per page, always.

## Tools, prompts & resources
- **Figma** — primary design/mockup tool. Paid plan used mainly for extra file storage (many project files) and to buy a paid seat for the developer, who logs in directly to export assets/specs.
- **Canva / Photoshop** — explicitly named as equally valid alternatives to Figma for the mockup step; "it's whatever works the best for you."
- **Pexels** — free stock photo site used to source images when no real product/team photography exists yet.
- **WordPress + Elementor** — the CMS/page builder combo used for the live build demo.
- **GoHighLevel** — flagged by name as the platform with the specific "return creates two H1 tags" bug; the fix is padding, not a hard return.
- **Google Fonts** — Noto Serif is pulled from here for the H1.
- A running **Google Doc** is kept for design-system specs (grid settings, colors, etc.) and shared with the group afterward.
- Presenter offered to post a written **About-page template** (section breakdown + copy strategy) directly in the Hey Tony community as a follow-up resource (not included in this transcript).
- No AI writing prompts were used or quoted in this session — the entire call is manual design/build technique, not AI-assisted copywriting.

## Case studies / examples / results
- **Running worked example**: a fictional "Winnipeg massage therapist" business, used to build a complete About page live, end-to-end, in Figma then WordPress/Elementor — see Tactics section for the full section-by-section structure and exact numbers. Presenter's own claim: the whole thing — mockup plus live build — took **"almost exactly one hour."**
- **Samantha** (new to the group, site built on Shopify, unfamiliar with Figma) — asked whether any of this applies to her platform. Answer: this is a platform-agnostic planning step (works the same conceptually whether you build in Shopify, WordPress, or Wix), it's optional, and she can apply the design *tips* to revise her existing About page without redoing it from scratch.
- **HighLevel-using attendee** (mentions she and "Dr. Karen" both build on GoHighLevel) — flagged that pressing return inside an H1 field on HighLevel creates two H1 tags. Presenter's fix, confirmed from her own experience: use container padding to force the visual line break down instead of hitting return, which keeps a single true H1.
- **Karen** — asked, at the very end of the live build, why the spacing looked off under the transparent global nav bar. Diagnosis: the nav bar was overlapping the hero because the hero's top padding didn't account for it. Fix demoed live: added roughly 200 extra pixels of top padding to the hero container.
- **Unnamed member's existing About page** (built with help from an outside developer/"the guy that's helping me now") — audited live as too copy-heavy and visually bland ("text title, text title"). Guidance given: expand thin copy, and target roughly one visual element (photo, icon, or graphic) per section, referencing the presenter's own homepage (which uses small graphic elements like a "stars" icon even in mostly-text sections) as the benchmark. For a niche where literal photos felt over-used/limited, the presenter demoed pulling a "vibe" texture image (rocks, for a calming massage-therapy mood) and layering it behind the existing photo with rounded corners and reduced opacity to add depth without adding more literal pictures.

## Notable verbatim quotes
- "When people go to the about page, they're not really looking for our life story, but they're really looking to see if you're a real person, can they help you with what they're looking for, and if this is a good fit for working together."
- "When people trust you, people will shop with you."
- "It's, it's really about like a trust page."
- "We don't want it to look like people are landing on a completely different website."
- "This isn't a mandatory step... it's just a step to help you get your ideas organized before going into your website."
- "What we never really want to do is right align, because people don't read comfortably this way, because our way of reading is left to right."
- "So then you would have two H1 tags, which we don't want."
- "Even though this is mostly type, I have visual elements in here."
- "Even though it seems like an extra step to design things first, it actually can save you time in the long run, because you're not kind of fiddling around trying to figure out what you actually want to do."
- "We basically designed and built it all out in almost exactly one hour."
- On layering a texture image over a stock photo: "It just gives it more texture, more sense, more depth, more appeal."

## Tradeoffs & nuance
- Design-first (Figma/Canva/Photoshop) vs. build-first is explicitly framed as a preference, not a rule — some people prefer to build and adjust directly inside the live page builder, and that's "totally okay too."
- The padding-instead-of-line-break fix is platform-specific triage (needed on GoHighLevel because of its double-H1 bug), not a universal recommendation to abandon line breaks everywhere.
- A padding value tuned for desktop can actively break mobile — 255px of side padding looks right on desktop but is wider than an entire iPhone viewport, so mobile needs its own independently-set (much smaller, ~50px) value, possibly paired with a smaller font size.
- Center-aligned text isn't banned outright, just rationed — acceptable for a short headline, but overusing it across body copy hurts readability versus left-alignment.
- Pure black body text isn't wrong so much as suboptimal — gray is preferred for eye comfort and polish, but only as long as contrast against the background stays sufficient.
- JPEG vs. PNG vs. WebP is a three-way tradeoff: JPEG is smallest but no transparency, PNG keeps transparency but is bigger, WebP is best overall but isn't producible directly from Figma — so the real workflow leans on the page-builder's own conversion plugin rather than solving it in the design tool.
- When a niche's literal photo options feel limited or overused (massage therapy, in this case), the presenter's answer wasn't "add more literal photos" but to reach for adjacent mood/texture imagery and treat it as a layered accent (muted opacity, rounded corners) rather than a standalone image — a stylistic workaround, not a hard rule.
- The one-hour build claim is presented as evidence *for* the design-first workflow (less "fiddling" mid-build) rather than a guaranteed time for everyone — it assumes the styles/grid/colors were already established from the homepage build.
