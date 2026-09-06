# Web Design for SEO — 10.06.2026 (Wix build → live site reviews)

## Tactics & step-by-step how-to
- New-site build order: (1) set up branded styles first to match the Figma document, (2) build the homepage first, (3) build remaining pages after.
- Design order: copy first (work out SEO copy), then figure out the layout that conveys it — prevents a "big wall of text" or content crammed into too small an area.
- **Go-to homepage wireframe** (presenter's default, "works for most websites"):
  1. Hero — headline (impactful message) + CTA button + image/graphic relating to the business.
  2. Trust-building elements within or right below the hero.
  3. About Us — introduce the business (what you do, how, who you serve); treat the visitor like it's their first interaction with you.
  4. Services/products outline.
  5. Testimonials.
  6. "How it works" section — eases the anxiety of a visitor who's never worked with a business like yours before.
  7. FAQs, near the end — good for Google and for pre-answering objections that stop people reaching out.
  8. CTA at the very bottom, so a visitor who scrolls all the way down still has something to do next (also keep a CTA up top).
- FAQ placement rule: put an FAQ section on **every page**, not one central FAQ page — every page should target one focus keyword, and the FAQ is where you answer questions tied to that specific keyword. ("If you have all your FAQs on one page, what are we ranking for?")
- FAQ display balance: fully open FAQs read better for crawlers (per SEO folklore an attendee cited — hidden/accordion content may be weighted less), but too many open ones overwhelm visitors. Working rule: ~5 open FAQs is fine; beyond that, use an accordion. For ~4 FAQs, an alternative is a 2-column layout (2 questions per row) instead of an accordion.
- Figma export workflow: select the object(s) → Export panel → choose format. Shift-click to multi-select layers, then export them together in one action.
- SVG vs raster: only export as SVG if the source art is actually vector-based (icons/illustrations) — smallest file size and infinite scaling with no pixelation. Exporting a photo/raster image as SVG gives zero benefit; it's still pixel-based underneath.
- Save exported assets into an organized folder (not just the desktop) for easier asset management.
- Image title/alt workflow: leave the **Title** tag blank (that's literally what shows in the hover tooltip / Finder hover) but always fill in the **Alt** tag with descriptive text; verify via right-click → Inspect Element to see the `title="..."` attribute directly on the image.
- CTA conversion diagnostic: if a site gets traffic but few contact-form fills or contact-page visits, the first lever to pull is the CTA button color — pick a color with real contrast so it visually stands out and gets clicked.
- **Modernizing a dated hero** (live demo on Aspire Peak Properties, via the HTML to Design Figma plugin):
  1. Remove box-shadows on containers/cards — called out as an "early 2000s" web-design tell.
  2. Add a subtle background color per section instead, to define/separate sections.
  3. Switch buttons to a solid color for more contrast/attention.
  4. Swap a default/Times-New-Roman-style body font for a clean sans-serif (e.g. Open Sans); keep a serif headline if it matches the existing logo — the contrast between serif headline / sans body is the goal.
  5. Increase line-height on body copy — improves readability and gives text "breathing room" even with no other changes.
  6. Add empty space around and between sections rather than worrying about page length.
- Text-over-image legibility fixes (used on Louise's real-estate/reno hero): remove text-shadow (makes letters less crisp); instead either (a) split into two columns — image on one side, plain background + text on the other, or (b) keep one background image but add a black/dark overlay to lift text contrast. A colored block placed only behind the text within a busy collage is a weaker third option — still layers too many visual elements.
- Collage-hero technique: for a business spanning multiple sub-topics (real estate + renovation), build a photo collage as one combined graphic (Canva has ready-made collage templates), then place headline + body text beside the collage rather than on top of it. 3 images was used as "a good number" in the live mockup.
- Alternating-layout technique: Section 1 = text left / image right, Section 2 = reverse (image left / text right), and keep alternating down the page — adds visual interest and signals to the reader that a new section/topic has started.
- Font identification + substitution: use the **Font Ninja** plugin to identify a live site's font (found "Tahoma Bold" on Louise's site); if you don't own the identified font, substitute a default sans-serif like Open Sans rather than trying to source it.
- Palette sourcing: search a descriptive term on Pinterest (e.g. "navy blue color palette") to quickly pull a coordinated set — a dark shade for headlines/footer, a body-copy shade, an accent/alternate-background shade (e.g. sandy beige/tan), and an off-white.
- Footer tactic: go dark (e.g. dark navy) for the footer; reuse a navy already present in the site's logo/brand so it stays consistent.
- Match built pages to the Figma spec precisely — when translating the demo button into Wix, presenter set text to the exact Figma values: 20px, Open Sans, Bold.
- Landing/sales page structure (distinct from a standard homepage or service page): keep a strong hero as-is if it already has product image + clear CTA above the fold, but lengthen the rest of the page with more FAQs, more testimonials, more descriptive copy about the offer (without giving away the actual content/tips), a personal founder-story block that mirrors the reader's pain point, and a contact form at the bottom.
- Claude Design workflow: design at least the homepage fully in Figma first so the AI understands the brand direction, then upload that Figma file into Claude Design so it can render out the remaining pages — faster than letting it build unguided.
- Don't build/iterate a full live website end-to-end inside Claude/Claude Design — use it for design/rendering only, then build the actual site in a separate platform (WordPress/Wix/Squarespace), because token cost escalates fast if you try to develop everything inside it.
- When screen-sharing while running design software (Figma), close unused programs/windows first — combined load of design app + Zoom + extra windows visibly tanked performance this session (one button took ~10 minutes to place in Wix).

## Rules / dos & don'ts
- SVG only for vector art (icons/illustrations); WebP for photographic images (convert from JPEG/PNG — don't bother converting SVGs to WebP, they're already small enough).
- Font count vs. site speed: **more than 3 fonts** causes a noticeable speed decrease; **2 fonts** is safe with no noticeable speed difference. (Flagged as extra important on Wix, which already "has such a high speed issue.")
- Body copy: sans-serif, not serif — serif reads fine for headlines (especially if it matches the logo) but a serif body font "looks standard," undesigned.
- Remove box-shadows on cards/sections (dated, "early 2000s" look) and remove text-shadow on hero text over images (hurts legibility) — solve contrast with overlays/layout instead.
- Image Title tag: leave blank. Image Alt tag: always fill in with descriptive text — don't leave it as a placeholder long-term.
- One FAQ section per page (tied to that page's one focus keyword), not one page holding every FAQ.
- FAQ accordion threshold: roughly 5 open FAQs is fine; more than that, use an accordion, or use a 2-column layout for ~4 FAQs.
- Every page should target one focus keyword.
- Don't cut existing copy to make a page "more minimal" — "I wouldn't recommend reducing the text you already have on your web page," even though the presenter's own demo intentionally used bare-minimum copy for a clean look; going hard on SEO means adding more copy, not less.
- Don't worry about a page being too long — fix scanability with spacing, not by trimming content.
- Avoid pure white and pure black in a palette — use off-white / near-black; a "hint of color" elevates the design and avoids looking basic.
- Never leave text sitting unprotected on a busy background image — fix with a column split, dark overlay, or contrast method.
- CTA button must have real contrast — don't default it to blend into the rest of the brand palette.
- Include a CTA both near the top (hero) and at the very bottom of every page.
- If a page isn't ranking yet, it's fine to keep iterating its homepage headline/title; once it starts ranking, stop touching the title.

## Tools, prompts & resources
- **Figma** — free tier available; used to lay out a site before building; presenter's primary design/communication tool between design and build.
- **Canva** — valid lower-cost alternative to Figma for laying out a site pre-build; has ready-made collage templates useful for hero graphics.
- **Wix** — page builder being demoed live; visual drag-and-drop; branded styles set up first; called out (by attendee Chantel) as already having speed issues, which is why font count matters more here.
- **WordPress** (presenter's home platform) and **Squarespace** — the other two platforms referenced/compared throughout.
- **Cadence** — WordPress theme in use on Louise's real estate/renovation site.
- **WP Rocket** — image/speed optimization service Louise is using on her WordPress site.
- **HTML to Design** — Figma app/plugin; paste in a live site's URL and it imports the site's existing design/styles into a Figma document so you can mock up revisions non-destructively before touching the live site. Has a free version. Used live on Aspire Peak Properties (got stuck at 90% load once during the demo).
- **Font Ninja** — plugin used to identify which fonts a live website is using (found "Tahoma Bold" on Louise's site).
- **Claude / Claude Design** ("cloud design") — AI design tool; workflow is design homepage in Figma → upload Figma file into Claude Design → it infers brand direction and renders remaining pages. Presenter calls it "very powerful," has only played around with it (not used it to build/develop a live site), and flags token cost as a real constraint for full site development. A dedicated future workshop on it is planned.
- **Lovable** — mentioned only as an attendee question; presenter has no personal experience with it.
- **Pinterest** — used live to search "navy blue color palette" and pull a coordinated palette (dark/headline shade, body-copy shade, accent/background shade, off-white) for a client site.
- **Inspect Element** (browser dev tools) — used live to show where the image hover-tooltip text (the `title` attribute) comes from.

## Case studies / examples / results
- **Aspire Peak Properties** (Chantel) — property management company, Calgary and Edmonton. Feedback: dated hero (box-shadows, default/Times-New-Roman-style body font, low text contrast, three unclear options with no obvious next click). Live revision via HTML to Design: removed box-shadows, added subtle per-section background colors, switched to solid-color buttons, swapped body font to Open Sans while keeping the serif headline (matches logo), increased line-height. Presenter's read mid-demo: "even though I didn't do much, I think this is already starting to improve a few things."
- **Louise's real estate/renovation blog** (WordPress, Cadence theme, WP Rocket) — deliberately spans two markets (real estate + property renovation/DIY) to differentiate from Zillow/Trulia with "more in-depth, more specific, more experience-based" content instead of "vague bloggy stuff." Not yet ranking highly by Louise's own account. Monetization plan: renovation/design products, targeting sellers, buyers, and owners of property. Issues found: busy background hero image killing text contrast, text-shadow further hurting legibility, hero image cropping inconsistently across iPad/desktop/phone. Fixes proposed: rebuild hero as a 3-image collage with text placed beside it (not overlaid); drop the text-shadow; pull the site's existing teal accent color into the homepage (presenter liked the teal + orange combination); reorganize blog posts into 3 clickable "process" groupings (e.g. a "selling your home" blog category group) instead of one flat list.
- **Sign-language interpreter site** (Squarespace, ~10 days old, a second business alongside the owner's established yoga studio site) — intentionally rough ("it looks like crap... made in Squarespace in like a week") but landed the owner's first huge assignment within 10 days and is generating "tons of work." Presenter's read: text is very easy to read, and because visitors arrive already urgently needing an interpreter and she's "one of the only people doing this in the area," conversion doesn't depend on polish. Known bugs: Squarespace layout drifts across desktop/iPad/phone a few days after being set; hero video stops autoplaying roughly weekly and must be deleted + re-uploaded to fix. Desktop traffic beats mobile because the business is B2B, so the owner prioritizes desktop appearance — a real constraint since Squarespace only supports desktop/mobile breakpoints (unlike other platforms with more granular sizes). Recommended fix: rebuild the image section with a prebuilt layout, alternating text-left/image-right then image-left/text-right per section.
- **Maritzia's "buy my book" landing/sales page** — book titled "Kickstart Your Stand Up Comedy" (helps beginners write jokes, get on stage, positioned as a shortcut to "look like professionals... quicker"). Current page: product image + "download it now" CTA above the fold, speaks to the target audience immediately. Presenter's verdict: "I think this is really solid right off the bat." Recommendation: lengthen with more FAQs, more testimonials, more descriptive copy about the book (without leaking its actual content), a personal founder-story section, and a contact form at the bottom.

## Notable verbatim quotes
- "We want it to be noticeable enough that people will click it." (on CTA button contrast)
- "If you find like you're getting like a ton of traffic but you're not like getting a lot of people like filling out a contact form... the first thing I would try changing would be your button colors."
- "If you have all your FAQs on one page, what are we ranking for?"
- "I wouldn't recommend reducing the text you already have on your web page."
- "I don't worry about websites being super long."
- "If you have more than three fonts, you are going to see a decrease in your speed. But I think we can have two fonts and not notice a difference for your site speed."
- "This is the time to start like playing around until you get something you like and then you stop touching it." (on iterating a homepage headline before it ranks)
- On the interpreter's rough Squarespace site: "It looks like crap... but it's working." / "By the time people land here they really need an interpreter."
- "I do try to avoid pure whites and pure blacks because it just... makes it look basic." — "if you just add a little hint of color [it] elevates your design."
- On Claude Design: "It is very powerful"... but "Claude actually gets quite expensive if you are developing everything in Claude because you'll run out of tokens very quickly."
- "I would call this like a sales or landing page because you have one thing that you're trying to sell... but I guess it would be a money page too." (distinguishing a sales/landing page from Matt's "money page" term — Matt's money pages are a site's core revenue-driving offerings)

## Tradeoffs & nuance
- FAQ accordion vs. fully open: SEO folklore says crawlers may weight hidden/accordion content less, but too many open FAQs overwhelms human visitors — presenter frames this as a balance (open up to ~5, accordion or 2-column beyond that), not a hard rule.
- Minimal copy vs. full SEO optimization: presenter's own demo intentionally used bare-minimum copy for a clean look, but states that going "really hard with SEO" means adding more copy — a direct tension between polish and maximal on-page SEO text.
- Single hero image vs. collage: one background image is cleaner but can fail to represent a business spanning multiple sub-topics and risks text-contrast problems; a collage represents breadth but risks looking busy — the compromise used was collage-as-graphic with text kept fully off the image (beside it, not overlaid).
- Polish vs. conversion reality: the interpreter's deliberately rough Squarespace site is outperforming on conversions purely on urgent buyer intent + text readability — direct evidence that aesthetic polish isn't a precondition for conversion when intent and message clarity are high.
- Desktop vs. mobile: the interpreter site's B2B audience skews desktop, so the owner accepts worse mobile cropping to prioritize desktop — a deliberate tradeoff, constrained further by Squarespace only offering two breakpoints.
- Service pages vs. location pages (raised by the interpreter site owner): flagged as a real tradeoff ("without doing extra work I don't need to do") but not resolved with a concrete rule in this call.
- Homepage title/headline changes: fine and encouraged pre-ranking (near-free experimentation), but to be avoided once a page starts ranking well, since retitling then risks the ranking already earned.
- Claude Design: powerful for design generation/iteration but too token-expensive to use as a full site-build tool — better used as a design/prototyping layer that hands off to a separate build platform.
- Wix performance this session was severe enough (one button taking ~10 minutes to place) that the presenter abandoned the live build mid-session and pivoted to site reviews — attributed partly to design software + Zoom + too many open windows, but not fully diagnosed live.
