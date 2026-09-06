# Web Design for SEO with Leanne — 05.03.2026 (Leanne Jones, Leanne Digital)

## Tactics & step-by-step how-to
- Design fully before touching development — she uses Figma, but the same layout rules apply if you use Canva, Adobe XD, Photoshop, or literally pencil and paper; this is a layout-logic session, not a Figma tutorial.
- Copy-first workflow: write ALL page copy before laying out design — the message dictates the layout, not the other way around. Demoed live by pasting pre-written copy into each section as she built the page.
- Treat each H2 as its own visually distinct section (different background color per section) — conceptualize the page "like a slide deck," one idea per slide/section.
- **Homepage structure recap** (from a prior session, referenced again as the model):
  1. Hero — focus keyword worked into the headline + a supporting sentence + one CTA button in a color that visually pops against the background (deliberately impulse-clickable, "even without thinking, someone might just click this button").
  2. Intro/H2 section — reuses the focus keyword again with natural variation (hero: "Massage Therapy in Winnipeg" → H2: "Winnipeg Massage Therapy") — introduces the business and names who it serves (persona list: busy professionals, athletes, desk workers, people recovering from injury) so visitors self-identify with a pain point.
  3. Services overview section.
  4. Trust section — testimonials/reviews (Google reviews, or video testimonials).
  5. "How it works" process explainer — reduces anxiety for people unfamiliar with the service ("I've never been to a massage clinic, what happens next?").
  6. FAQ section — doubles as a word-count booster that doesn't feel like padding.
  7. Final CTA section — every page ends with one.
- **Service-page IA**: build one **service overview (parent) page** that briefly summarizes each service and links out, plus one **individual service (child) page** per service — gives a clean, crawlable URL nesting (parent page, then each service as a child page under it) that's easy for both Google and users to parse.
- **Individual service page structure**, demoed end-to-end on "Deep Tissue Massage":
  1. Hero — H1 = focus keyword + city name for local SEO ("Winnipeg Deep Tissue Massage"), short descriptive subhead trimmed down from ChatGPT's draft, hero image.
  2. "Who is [service] for?" — turned a long bullet list (6 points) into a row of icon boxes/cubes instead (aimed for 3 cubes) to visually break up what would otherwise be a dense list; bullet copy that didn't fit the cubes got added as a short line of text underneath.
  3. "Benefits of [service]" — reused the same colored-dot checklist style from the overview page (improving range of motion, reducing chronic pain, breaking down muscle adhesions/knots, improving circulation, supporting injury recovery).
  4. "What to expect during your treatment" — plain paragraph copy, deliberately no bullets/checklist here, to vary the page's visual rhythm.
  5. CTA section with a local-keyword headline ("Book a Deep Tissue Massage in Winnipeg").
- Keep every page's hero/header treatment visually identical site-wide (same style, spacing, weight) — cohesion signals "same site" to the visitor.
- Building bullet/checklist sections: use a rounded, colored (brand-color) check-mark/dot bullet, bold the key phrase after it, and Option-key-drag-duplicate in Figma to repeat the element fast instead of rebuilding it each time.
- CTA copy must always name the specific thing being offered — never ship a bare "Learn more" button; write something like "Learn more about our deep tissue massage services," then run it through ChatGPT to tighten if it's too long.
- Image cropping in Figma: when a horizontal stock photo doesn't fit a vertical frame, switch the fill mode to "fill" (not the default crop) so it fills the frame, then fine-tune the crop afterward; Figma also has an orientation filter (e.g. "vertical") to help surface better-fitting stock photos on a search.
- Don't redesign every section from scratch — duplicate a working section, flip which side the image/text sits on, and swap in a new background color so it visually reads as a new section without rebuilding the layout.
- "Equal spacing" check: draw small, bright-red reference squares between sections to visually compare gap sizes and catch uneven spacing before handing off to dev.
- Line-height hack: start line-height equal to the text's pixel size (40px text → start at 40px line-height), then nudge up a few pixels if it reads too tight — landed on 46px here — and reuse that exact number across matching sections for consistency.
- Note exact pixel measurements in the design file so padding maps 1:1 to CSS on handoff — a 68px reference square in Figma becomes 68px top/bottom padding in dev.
- Never reuse the same photo across more than one page of the site — every page should carry its own unique photography so it reads as a distinct page with its own message.
- Two-CTA-button hierarchy (e.g. "book online" vs. "call"): pick the one action you actually want people to take and make it the solid/filled button; demote the other to an outline-only button (strip its background fill, add a stroke — white, in the demo). Flip which button is filled vs. outlined depending on which channel actually converts better for that specific business.
- Export final image assets straight from the design tool's export feature at the size they'll actually display at (not oversized originals) — keeps page weight down and helps page speed once live.
- When buying an icon pack, first list every concept you need represented (desk work, chronic tension, neck/shoulder tightness, lower back pain, etc.), then vet the pack against that list before buying — avoids ending up with an incomplete or mismatched set partway through a build.
- Prefer smaller, tightly-themed icon packs over huge bundles — a giant pack takes too long to sift through mid-build.
- Use built-in elements/shapes already inside your design platform (checkmarks, bullets, etc.) instead of custom-building every small graphic from scratch, when the platform already has them.

## Rules / dos & don'ts (keep every threshold, number, specific)
- Every page — not just the homepage — ends with a final CTA section; never leave a scrolled-to-the-bottom visitor with nothing to do.
- Every individual H2 gets its own section with a background color distinct from its neighbors.
- Don't center-align large blocks of body copy — normal reading habits are left-aligned; centered text is only for short blurbs (a line or two), not full sections.
- Verify text/background contrast before finalizing a section — caught live on this call: white-on-near-black works, dark-gray-on-near-black is functionally invisible.
- Keep every page's header/hero styling identical across the whole site — inconsistent headers read as unprofessional and create doubt about whether the user is still on the same domain.
- Include the focus keyword in every H1 and major headline, but keep it descriptive/natural — never let it read as keyword-stuffed.
- Add the city/location name into individual service-page headlines for local SEO — the overview/hub page used the broader "massage therapy services" keyword with no city; the child "Deep Tissue Massage" page added "Winnipeg" specifically to help it rank locally.
- CTA button copy must always name the specific action/service — a bare "learn more" is not specific enough.
- Original photography is always the better choice over stock, for both SEO (original content) and trust/branding.
- Stock photos will NOT hurt your SEO — but only if you include proper alt tags.
- AI-generated images: Leanne's honest answer was a hedge, not a confident rule — "I don't think it would hurt you... but I don't have the stats for that" — still conditioned on using proper alt tags.
- Never reuse a photo across multiple pages of the same site.
- Always design against a grid (toggle grid guides on/off to check) — ungridded layouts read as unbalanced and unintentional; gridded layouts make elements "feel like they belong there."
- Pull bullet/icon colors from the business's existing brand palette — this demo brand had 3 core colors: teal, green, gold.
- Line-height starting rule: set it equal to the text's pixel size, then adjust up in small increments (this build landed on 46px line-height against 40px text).
- Padding/spacing should be measured in exact pixels in the design file so it translates directly into dev CSS.

## Tools, prompts & resources
- **Figma** — primary design tool used for: toggleable layout/grid guide overlay, a live browser-style Preview mode, Option-key-drag duplicate shortcut, per-image export feature (outputs at final display size), and image fill/crop filter controls (including an orientation filter for finding better-fitting stock photos).
- **ChatGPT** — used to generate first-draft page copy (e.g. the deep tissue massage hero copy), which Leanne then manually trims/edits for tone, local relevance, and length; also used to shorten over-long CTA button copy.
- **Pexels** — Leanne's go-to free stock photo site (noted that massage-therapy-specific photography is hard to find well on it).
- **Adobe Stock** — Leanne's paid source for icon packs; her reasoning: free icon options are limited, so she buys a themed pack (search terms demoed live: "massage therapy icons," "wellness icons," "physiotherapy icons") only after confirming it covers every concept she needs.
- Alternative design tools named as equally valid for applying the same layout principles: **Canva, Adobe XD, Photoshop**, or pencil and paper.

## Case studies / examples / results
- Demo business built live: **"Serenity"** massage therapy clinic in Winnipeg (domain floated on the call as serenity.com / serenitymassage.com). Brand palette: 3 core colors — teal, green, gold ("really earthy"). Target personas: busy professionals, athletes, desk workers, people recovering from injury. 3 core services: Deep Tissue Massage, Relaxation Massage, Sports Massage.
- Built live on this call: (1) the full **Services Overview page** (hero, 3-service summary blocks each with an icon/bullet layout, alternating image/text sides and background colors, closing CTA), and (2) the full **Deep Tissue Massage individual service page** (hero, "who it's for" icon-box section, benefits checklist, "what to expect" paragraph section, closing local-keyword CTA).
- Attendee **Lux** asked whether stock photos or AI-generated photos hurt SEO versus original photography — see Rules section above for Leanne's answer.
- Only two attendees remained by the end of the call (**Fay** and **Lux**); no further questions were raised.

## Notable verbatim quotes
- "It's great to know how to do SEO, but it's also another thing to lay things out in a way that isn't just like a big wall of text... Google also doesn't like it if your website is just like one wall of text either. So it's good to have a balance."
- "It's great to impress someone, but if we just impress someone and we don't give them an idea of what to do next, they're not going to convert."
- "I always start with the copy first because our layout is to help communicate our message."
- "If you have a different header section for every individual page, it can make your website look unprofessional and it can also confuse the user whether or not they're on the same website."
- "Original photos are always the best to use, but if you're using like stock photos, it's not going to hurt your SEO as long as you include like proper alt tags."
- "Having authentic photography automatically helps with people feeling like it's not a scam, and it's a real business."
- "It's a nice clean URL structure and this will make it really easy for Google to understand your site... it also helps your users because then they can clearly understand what services you offer."
- "I try to break things down into clear, easy to digest sections on your website, and if you do that, that will really help with your user experience."

## Tradeoffs & nuance
- Stock photography is a safe fallback (won't hurt SEO with proper alt tags), but original photography wins on both trust and SEO uniqueness — even photography that "doesn't look as nice as stock" still beats stock for authenticity/trust signal, a quality-vs-authenticity tradeoff Leanne resolves firmly in favor of authenticity.
- AI-generated imagery is the one question Leanne answered without confidence — no data either way, just a hunch that it "probably" doesn't hurt as long as alt tags are handled, explicitly flagged as not backed by stats.
- Center-aligned text isn't banned outright, just scoped — fine for a short block (a sentence or two), actively bad for readability once it's a larger section of copy.
- The two-CTA-button pattern (solid vs. outline) isn't fixed to "always push online booking" — whichever action gets the solid/primary treatment should follow whichever channel that specific business actually converts best on (some businesses do better getting people on the phone than through a form).
- A 6-bullet-point section forced a real design compromise: the "ideal" visual (3 cubes) didn't cleanly fit all 6 points, so the excess got demoted to plain leftover text below the cubes rather than forcing an awkward 6-cube layout — a practical patch, not a clean solution.
