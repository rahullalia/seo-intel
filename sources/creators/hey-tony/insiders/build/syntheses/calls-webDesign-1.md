# Web Design for SEO — Synthesis (webDesign group, 15 calls)

Source calls: mostly Leanne Jones (Leanne Digital) teaching sessions/live builds/live critiques, plus Matt Diamante-led critique and color-strategy calls. Covers 08.07.2026 → 10.12.2025.

---

## 1. Design Process & Workflow

- **Copy first, then layout.** Write all page copy before opening a design tool — the message dictates the layout/section structure, not the other way around. Repeated as the single most consistent workflow rule across calls.
- **Wireframe/mock up before building live** (Figma, Canva, Adobe XD, Photoshop, or pencil and paper — tool doesn't matter). Benefits: surfaces bad ideas before you're fighting the page builder; locks image sizes/copy in advance so you're not repeatedly uploading "maybe this works" test photos into the CMS media library (bloats it with unused files); prevents mid-build detours (one attendee who skipped wireframing in Divi had to jump to Photoshop mid-build to resize images).
- **This step is optional, not mandatory.** Building straight into the page builder and iterating there live is a valid alternative — "do whatever works best for you." If a site is already built/styled, skip wireframing and go straight to building new pages.
- **Reuse, don't rebuild:** copy already-styled H1/H2/text layers from a finished homepage frame into a new interior-page frame so font/size/color match with zero re-styling. Duplicate a working section, flip which side the image/text sits on, swap the background color — reads as a new section without rebuilding the layout.
- Keep a running Google Doc of design-system specs (grid, colors, spacing, fonts) as you build so the spec sheet can be handed to a developer or shared with a team afterward.
- Note exact pixel measurements (padding, gaps, corner radius) directly in the design file so they map 1:1 to dev CSS on handoff — don't eyeball them.
- **"Equal spacing" QA check:** draw small bright-colored reference squares between sections in the design file to visually compare gap sizes and catch uneven spacing before handoff.
- Preview cohesion: use Figma's **Play** button to enter a click-through prototype view, then toggle between frames (e.g., homepage vs. about page) to confirm pages feel like one site.
- Name every container/section in the builder's layer panel (e.g., "Intro," "Services," "Process," "Why," "About Me") — pure workflow/handoff aid, not an SEO factor.
- When screen-sharing while running design software, close unused programs/windows first — design app + video call + extra windows can visibly tank performance (one Wix button took ~10 minutes to place in a live session under this load).
- **Claude / "Claude Design" workflow:** design the homepage fully in Figma first so the AI understands brand direction, then upload that Figma file into Claude Design so it can render the remaining pages — faster than letting it build unguided. Explicitly **do not** build/iterate a full live website end-to-end inside Claude — use it for design/rendering only, then build the actual site in WordPress/Wix/Squarespace, because token cost escalates fast developing a full site inside it ("Claude actually gets quite expensive if you are developing everything in Claude because you'll run out of tokens very quickly").

---

## 2. Site & Page Architecture (Information Architecture)

### 2.1 Canonical homepage wireframe
Recurs (with minor variation) across nearly every call as the default starting skeleton for a service business:

1. **Hero** — H1 (focus keyword, descriptive/plain language) + supporting subhead/paragraph + one CTA button, all visible with **zero scrolling**. Put a trust signal (reviews/stat/logos) directly in the hero or immediately below it.
2. **Trust-building elements** — 5-star rating, years of experience, # of happy clients, licensed/insured, awards, association logos. Pick ~3 for a hero-adjacent row.
3. **About Us / intro** — introduce the business (what you do, how, who you serve); treat the visitor like it's their first interaction with you. Include an audience-identifier layout (icon boxes per customer persona) so visitors self-identify ("yeah, I'm actually a person working at my desk with back pain — this speaks to me"). Include its own CTA.
4. **Services/products overview** — brief intro to each service/category, each linking to its own dedicated page.
5. **Testimonials / past clients** — Google reviews widget, pasted reviews, or video testimonials.
6. **"How it works" / process section** — plain numbered steps of what happens after someone books/inquires; defuses first-time-buyer anxiety (e.g., massage: book appointment → assessment → target treatment; moving co.: get a quote → plan your move → moving day).
7. **FAQ section** — anxiety-reduction + Google rewards on-page Q&A + low-friction way to add word count without a wall of text.
8. **Final CTA** — every single page ends with one; a visitor who scrolls all the way down should still have something to do next. Keep a CTA at the very top too.

Rationale for ordering: "the longer it is, the less likely people are going to reach the bottom of it. So you always want your most important messages near the top." Divide the page into sections where **one section = one H2 = one topic** (same logic as essay headers/paragraphs); alternate background colors/tints section-to-section so each reads as visually distinct (think of it "like a slide deck," one idea per slide).

Product-based sites: reuse the exact same wireframe, swap "services" for **product categories**.

### 2.2 Service-page IA
Two-tier structure, repeated across many calls:
- **Overview/parent service page** — briefly summarizes every service, exists mainly for navigation, links out to each individual page. Not a page you push hard on ranking.
- **Individual/child service pages** — one per service; this is where you go hard on SEO for that specific service (dedicated keyword targeting + more content = better for both SEO and conversion clarity). Gives clean, crawlable URL nesting (parent → child) that's easy for both Google and users to parse.

**Individual service-page structure** (demoed end-to-end on "Deep Tissue Massage"):
1. Hero — H1 = focus keyword + city name for local SEO (e.g., "Winnipeg Deep Tissue Massage"), short descriptive subhead, hero image.
2. "Who is [service] for?" — turn a long bullet list into a row of icon boxes/cubes (aim for ~3 cubes); anything that doesn't fit the cubes becomes a short text line underneath.
3. "Benefits of [service]" — reuse the same colored-dot checklist style from the overview page.
4. "What to expect during your treatment" — plain paragraph copy, deliberately no bullets/checklist, to vary the page's visual rhythm.
5. CTA section with a local-keyword headline (e.g., "Book a Deep Tissue Massage in Winnipeg").

Long service lists (e.g., general contractor): don't dump every micro-service on the homepage — list core services prominently, push the long tail into a **mega menu/dropdown**, each item linking to its own detail page. No fixed cap on homepage service count; the rule is "keep core accessible, push depth into the mega menu."

Cluttered "who we serve" / client-niche lists: treat as a **layout** problem, not a content problem — repeat a clean card/section design per niche instead of dense paragraphs, or spin it into its own dedicated page linking to per-niche detail pages.

### 2.3 Landing / funnel pages (built for paid traffic — distinct from homepage/service pages)

**Google Ads landing page** (high-intent, already-searching traffic):
1. Hero: one clear CTA + contact form as close to the top as possible — zero scrolling to convert.
2. Trust indicators row (pick ~3): years of experience, # happy clients, licensed/insured, 5-star reviews.
3. "Why choose us" + its own CTA.
4. Reduce-anxiety callout section (reassurance blurb; also breaks up the layout).
5. Services/offerings grid.
6. Testimonials (reviews widget, pasted reviews, video, screenshots).
7. Process section (plain numbered steps) + CTA.
8. FAQ — handle objections directly.
9. Final CTA at the very bottom, repeating the hero's trust indicators as a second reassurance pass.
10. A small "we do respond" trust line near the bottom — specific number ("we respond within 24 hours"), ideally personalized ("Amanda will review this and get back to you").

**High-ticket / funnel landing page** (cold/emotional-decision traffic):
1. Hero: hook the specific problem immediately (frustrated/stuck/overwhelmed) + video or product image.
2. Empathize section — "I've been there too."
3. Name the specific challenges/obstacles.
4. Explain your method/process (numbered steps).
5. Outline exactly what's included in the offer.
6. CTA at every section; use jump-links so mid-page CTAs scroll straight to the form/checkout (or route straight to checkout if no live conversation is needed).
7. Success stories — video + testimonials, deliberately heavy volume ("as many testimonials as you can").
8. "Who is this for" — filters good leads in, bad leads out, lets the reader self-identify.
9. "Meet the founder" — trust/personality section; needed for service/course offers, skippable for pure product offers.
10. FAQ section.
11. Final CTA appealing to emotion + contact form.

**Landing page rules:**
- Strip navigation to just a logo linking home — no full nav, no secondary CTA competing with it.
- Never list a paid landing page in site navigation — treat it as intentionally hard to browse into.
- Don't chase on-page SEO structure (H1/H2 keyword density) on paid LPs — traffic is bought, not organic. It's fine — expected — if an SEO tool flags the page as "orphaned"; consider noindexing.
- Exactly one CTA color per page.
- Rough threshold for "needs a funnel page": priced like a serious course or something people won't buy on a whim (comparison used: "a luxury car" or "a course that's like a grand"); a £450 bundle was judged probably below that bar.
- If checkout is off-platform (e.g., Gumroad), still build a full trust-building page on your own site and route every CTA out only for the actual transaction step — don't rebuild the full pitch on the external platform.
- Multi-pricing-model businesses (hourly/project/retainer): pick ONE model to sell per landing page rather than splitting into three.

### 2.4 Location & multi-audience strategy
- Homepage: pick **one** primary location + the focus keyword (e.g., "[keyword] in [City]") — far easier to rank than targeting broadly (e.g., the whole US).
- Many locations served: build one **"Locations Served" hub page** linking to an individual page per location, rather than proliferating pages endlessly ("I wouldn't make like a bazillion pages").
- Multi-location **and** multi-service (e.g., 12 locations × 2 services): don't build the full location×service matrix — use **location-first pages**, covering all relevant services within each location page; keep separate general/overview service pages at the site level too.
- Multi-audience-segment businesses: name location + role on the homepage, link out to one page per audience segment.
- Multi-country/region businesses: split into **one dedicated page per country/region** rather than one combined page, even in the same language — same rule applies internationally (confirmed for a Thai-language site: put the keyword in the URL in Thai, same logic as English).
- Even when the underlying service is nearly identical location to location (e.g., a lien-filing service where county differences are mostly just price): still build separate per-location pages — vary the on-page wording/lingo, not necessarily the substance.

### 2.5 E-commerce structure
- No paid traffic yet + simple/low-priced catalog: a dedicated landing/funnel page isn't necessary until there's a reason for focused traffic (high-ticket item, themed sale/blowout, or a single product being advertised).
- Multi-product ecommerce homepage: **stop trying to rank the homepage for one keyword.** Give each featured product its own clearly organized homepage section with descriptive text; push actual SEO/ranking effort onto **individual product and collection pages** instead.
- Keyword-reinforcement for a collection: repeat the exact target keyword phrase in **every product title** in that collection (e.g., every piece titled with "canvas art print" to reinforce ranking for "canvas art prints").
- Category/collection pages get the more specific, competitive keyword (repeated in category title, every product title, and body copy); the homepage H1 stays broader/durable.
- Off-Square e-commerce platform recommendations: **Shopify** top pick; **Squarespace** if product count is low; **WooCommerce**/**BigCommerce** also work but need a developer to set up ("a little tricky to set up by yourself," though WooCommerce "works great" once done).

### 2.6 Contact page
- Checklist of what must be included: phone number, email, opening hours, socials, contact form, map/location.
- Put the contact form (or the single highest-priority contact method) as close to the top/hero as possible — "above the fold." If phone calls are the real priority over form fills, put the phone number up top instead of the form.
- H1 rule for non-ranking pages: doesn't need the focus keyword — just label it plainly ("Contact Us"). (Ranking pages: keyword in H1 **and** first paragraph.)
- **Never** two contact forms on one page — one per page, full stop, even though some SEO advice suggests repetition helps; for a page that isn't a ranking target anyway, it's redundant UX.
- Instead of live-embedding Google Maps, screenshot the map, upload as a static image, and hyperlink the whole image out to the real Google Maps listing — protects page speed (confirmed this is what Hey Tony's own site does).
- Lead-form volume/quality lever: **add** qualifying questions (e.g., "what's your budget?") to filter low-quality leads when there are too many bad ones; **remove** questions (even the phone-number field) to raise completion volume when there aren't enough leads coming in.
- Anchor-link CTA technique (platform-agnostic, works in Showit/Squarespace/WordPress/Elementor/Divi): give a section an ID (Elementor: Advanced tab → CSS ID, e.g. `contact`; Divi has an equivalent field), then point the button's link at `#contact` so clicking scrolls to that section instead of loading a new page. Neither right nor wrong versus a dedicated contact page — an implementation choice (faster perceived experience vs. more conventional/fuller context).
- Corner radius as a brand-personality dial: more rounded = friendlier/softer (massage therapy, baby photography); less/no radius = more serious (cybersecurity/hard B2B). Applies to buttons, cards, boxes uniformly.

### 2.7 About page
- Purpose: **not** "our life story" — it's a trust page. Visitors are checking: are you a real person, can you help with what they need, is this a good fit.
- Structure demoed live: Hero (brand-color full-width bg, white H1 with a manual line break at a natural point, short one-line "approach" subheading) → centered H2 trust/benefit statement (keyword + location) → two-column module (text ~half width + a stock photo addressing a specific objection) → mirrored two-column module "Why I became a [role] in [city]" featuring the actual founder's photo (humanizes — "you are a real person, not just a stock photo template") → CTA section (narrower rounded container nested in the full-width section).
- Keep the exact same color palette as the rest of the site — never let an interior page look like a different website.
- At least one visual element (photo, icon, graphic) per section, or the page reads as bland "text title, text title" regardless of copy quality.
- Never right-align body text (reading direction is left-to-right); minimize center-aligned text too (fine for a short H2/headline, not for longer blocks).

### 2.8 Blog / blog roll
- Blog roll/archive pages are optimized for **usability, not ranking** — don't spend ranking effort there; the individual post is the page expected to earn traffic. Naming the blog page itself ("Blog" or "Insights") doesn't need SEO effort.
- FAQ placement rule (recurs constantly): put an FAQ section on **every page**, tied to that page's one focus keyword — not one central FAQ page. ("If you have all your FAQs on one page, what are we ranking for?") Never repeat identical FAQ text verbatim across pages — Google penalizes duplicated content.
- FAQ display balance: fully open FAQs may read better for crawlers (SEO folklore: hidden/accordion content may be weighted less) but too many open ones overwhelm visitors — ~5 open FAQs is fine; beyond that use an accordion, or a 2-column layout (2 Qs per row) for ~4 FAQs.
- Elementor: build a custom blog/archive template in **Theme Builder**, assign it to the blog roll — every new post auto-formats into it.
- If the platform allows custom excerpt length, truncate the auto-pulled snippet to a fixed character count (~200 characters) instead of a raw heading+paragraph fragment.
- WordPress Pages-vs-Posts mistake: if blog content was mistakenly built as Pages instead of Posts and it's already ranking, leave the existing URLs alone — use the actual Post function for new content going forward rather than migrating and risking a redirect/URL change.
- Blog post volume caution: safe to batch-edit all product/service pages (titles, meta, H-tags) in one sitting — **not** safe to publish/dump a big batch of new blog posts all at once; roll posts out gradually.

---

## 3. Heading Hierarchy & On-Page SEO Structure

### 3.1 H1 rules
- **One H1 per page, period.** Sole exception: two H1s containing **identical text**, typically from a separate desktop-H1 block and mobile-H1 block — an audit tool may flag this but it isn't an actual problem.
- The H1 must be the literal **first heading tag** on the page — never place another heading (or an untagged "hook" line) above it, regardless of what should be visually biggest/first. "It's like the title of the book. You don't have a secondary title before the book starts."
- H1 can be styled to **any visual size** — semantic tag and visual size are independent in builders like Elementor/Wix ("not all website editors let you do this"). Don't assume a big font automatically means H1 — verify/set the actual HTML tag explicitly (Elementor: click the heading → HTML Tag field/dropdown, or the widget's SEO/Accessibility panel; Wix: Edit Text → SEO and Accessibility → HTML tag dropdown).
- **Split H1 trick:** the real (SEO-friendly, often plain/boring) keyword phrase stays inside the actual `<h1>` tag, styled visually small; a punchier, non-SEO "impactful headline" sits next to/below it styled bigger (tagged H2). Example: Leanne's own site — H1 = "digital marketing services" (small), H2 = an impactful tagline (large).
- Never use a graphic/image as the H1 — it must be live, real text: Google can't read text baked into an image, and image-text doesn't scale responsively for mobile the way real text does.
- Keep the H1 **consistent long-term** on pages meant to hold rank — don't swap it every time a seasonal promotion changes; let a rotating hero/promo area carry the seasonal messaging instead. E-commerce specifically: hero (rotating promo) should NOT carry the H1 — put a fixed, keyword-targeted H1 + short paragraph directly below the hero so the hero can change constantly while the H1 stays put.
- Homepage vs. service-page keyword targeting isn't mandatory everywhere: Leanne's own homepage deliberately skips a primary keyword target and pushes keyword-targeting to her service pages instead — not every business needs to fight for homepage rank.

### 3.2 H2 / H3 / H4 nesting
- **Section = H2; one H2 = one topic** — same logic as essay headers/paragraphs.
- Go one level deeper (H3) only for subtopics within that H2 section. Don't go deeper than H3 in normal cases ("you probably won't need to go to like H4"); H4 is reserved for one further layer still (e.g., listing specific professional types under an H3 about "who we help").
- FAQ question titles: use **H2** ("Matt recommends using H2 tags for the FAQs... he's the expert in that").
- Footer titles above menu columns: **H4 or smaller**, never H1/H2/H3 — those belong to the page's own content.
- Heading-hierarchy bugs recur across every platform and skill level — treat as a common blind spot for non-developer self-builders, not a one-off mistake. Common causes: (a) theme/template auto-outputting a title AND a second H1 sitting in the post body — identify the true page-level H1 and strip the duplicate; (b) a platform auto-pulling a body H2 as an oversized "category" headline on a blog roll — where the tag can't be changed directly, wrap the snippet in inline HTML (`<span style="font-size: 30px">...</span>`) or ask ChatGPT to generate the custom HTML/CSS needed; (c) H5/H6 used where H3 belongs — just convert them; (d) skipping a level (H2 → H6) is a lesser, tolerable issue if H1/H2/H3 are otherwise correct — the ideal fix is re-tagging the skipped text to H4, but not urgent.

### 3.3 Platform-specific heading bugs (reference table)
| Platform | Bug | Fix |
|---|---|---|
| Shopify | Always puts its H1 tag in the site logo | Known quirk; workaround exists but not detailed — treat product/page title field as the real H1 target |
| Square | No true H1 field at all — the hover-to-reveal image-description field is read by Google as **alt text**, not H1 | Treat the platform's one available text field as the de facto H1; no real fix exists |
| GoHighLevel | Pressing Return inside an H1 field creates **two H1 tags** | Use container **padding** to force the visual line break instead of hitting Return — keeps a single true H1 |
| Squarespace | H1 size/style is globally template-locked — can't resize per-instance | Accept the large H1 (H1s should be big/impactful anyway); just verify it isn't visually bigger than the page's separate "title" style; keep the focus keyword in it regardless of size |
| Kajabi | Blog template auto-pulls a body H2 as an oversized "category" heading on the blog roll | Inline `<span style="font-size:Npx">` wrapper, or ask ChatGPT for custom HTML/CSS; ideally the underlying heading should be H3 or plain text |
| Elementor/WordPress | Visual style ≠ semantic tag if a developer only styled things to "look" right | Use the Heading element (not a text/paragraph element) and its explicit HTML Tag setting; if font styling goes "crazy" after retagging, it's likely inheriting a global style tied to that tag — check global settings |

### 3.4 Keywords, URLs, word count
- **One focus keyword per page.** Focus keyword = what someone actually types into Google to find you — not a full sentence, not a random string of adjectives.
- URL/slug rule: put the page's focus keyword in the URL — applies in any language (confirmed for Thai) — "a positive single ranking signal."
- H1 rule: focus keyword must be in the H1 (and in the first paragraph, for ranking pages); pad with natural surrounding words so it doesn't read as keyword-stuffed (ChatGPT prompt: *"give me some ideas — use this focus keyword and write a headline with it"*).
- Prefer **"[keyword] + [location]"** targeting over broad/national targeting — much easier to rank.
- Word count targets (multiple figures cited across calls — treat as a range, not one fixed number): **~1,000–1,500 words/page** given as a general rule; separately, **~2,000 words** cited as Matt's guidance target for a specific site (competitor benchmarked at ~2,000–2,200 words).
- FAQ accordions are the recommended way to pad thin word count without it reading as more visible text on the page.
- Don't keyword-stuff — high keyword density reads as "gibberish to the average person" and is flagged as an SEO error by audit tools.
- Don't cut existing copy to make a page "feel more minimal" — going harder on SEO means **adding** more copy, not less; fix scanability with spacing, not by trimming content. No fixed "too long" ceiling on page length as long as it's broken into digestible, well-spaced chunks.

### 3.5 Meta title / description
- Every page should have both set: **Page Title** = that page's focus keyword; **Meta Description** = a summary of the page's topic. (Shopify path: Online Store → Pages → open page → scroll to bottom → "Edit website SEO.")
- Elementor Pro: edit meta title/description without leaving the visual canvas via **Page Settings** (Rank Math/Yoast box appears right there); Matt's own habit is still to exit to plain WP admin → Pages → Edit and use the same box there.

### 3.6 Alt text & image file names
- Image **Title** tag: leave blank (that's literally what shows in the hover tooltip). Image **Alt** tag: always fill in with descriptive text.
- Include the focus keyword in alt text **only when it fits naturally** — don't force it into every image. Example: a massage photo's alt text should include "massage therapy"; a decorative heart icon's alt text should just be descriptive ("heart icon in a teal color"), not keyword-stuffed.
- Example alt texts used live: *"Winnipeg logo designer Leanne Jones"*; *"Winnipeg massage therapist providing a relaxing massage"* (refined from "giving" to "providing").
- ChatGPT prompt for alt text: upload the image and ask, in effect, *"give me an SEO friendly title in alt text for this image."*
- Image file names: descriptive, **4–5 words max**, keyword optional (e.g., "Woman receiving relaxing massage.jpeg"). Keyword-bearing filenames are a harmless minor SEO nudge, not a real ranking lever — "not needed for SEO, but any little bit helps."
- Featured/OG image size: **1200 × 628px**.

---

## 4. Typography

- **Font-pairing heuristic:** one "spicy"/interesting font (headings) + one "boring"/plain font (body) — the contrast is what creates hierarchy; two competing "interesting" fonts fight each other. Equivalent framing: get creative/fancy with the headline font (low readability cost — big, short text); keep the body font simple (sans-serif or serif), different enough from the headline font that they don't visually compete.
- Serif headline = "classier"/"bougie"/luxurious feel (especially if it matches an existing serif logo); sans-serif = "down to earth," standard/hardworking, easiest default for most sites and for body copy specifically. Mixing font *styles* (e.g., script + serif) within one line of text can accidentally break the line into two separate heading tags — avoid that.
- Font choice (script/serif/sans-serif) doesn't matter for SEO directly — readability is what matters.
- **Font count vs. site speed:** more than **3 fonts** causes a noticeable speed decrease; **2 fonts** is safe with no noticeable difference (flagged as extra important on Wix specifically, which already has speed issues).
- **Body copy size:** never below **16px** on any device; **16–20px** is the standard working range; **20px** repeatedly cited as "kind of the standard" baseline; 18px used in several specific fixes when bumping up an undersized body font.
- **H1 size:** start around **48px**, push bigger for impact; uppercase is an option for more punch. Specific builds used 60px and 64px with Noto Serif.
- **H2 size:** **40px+**.
- **H3 size:** **32px** (individual-service headline nested under an H2 section).
- **CTA/body button text:** standard **20px**.
- **Line-height rule of thumb:** set it equal to the font's pixel size first, then nudge up by eye until no line touches the descenders (g/y/p) of the line above/below — don't guess a number upfront. Target for body copy specifically: **~1.8** line-height (live-tested 0.8 → 1.2 → 1.8, with 1.8 judged easiest to read, "almost 2x"). One build landed on 46px line-height against 40px text.
- Desktop font can run larger than mobile (screen sits closer to the eyes on mobile) — e.g., 17.5px desktop / 16px mobile under a ~720px breakpoint — but this is the *one* thing allowed to shrink; spacing/margins should stay generous regardless of screen size.
- **Google Fonts**: free, available in every major website builder, safe from copyright issues, guarantees correct loading/rendering — the default safe source. No dedicated font-*pairing*-preset resource exists in Leanne's materials; the spicy/boring heuristic is the substitute.
- Fonts used repeatedly in the recurring massage-therapy demo build: **Noto Serif** (headings) + **Open Sans** (body, 20px). **Avenir** (thin weight) tested live for an elegant yacht-brand feel.

---

## 5. Color & Contrast

- **Complementary colors** (opposite sides of the color wheel) = maximum contrast → use for anything that needs to stand out (CTAs). **Analogous colors** (adjacent on the wheel) = harmonious/cohesive/relaxing feel → use for backgrounds and sections that should feel unified.
- **Dominant + accent ratio:** keep one color dominant across most of the page, use the complementary color only as a small "pop" (CTA/accent). Never split a complementary pair 50/50 — full-bright-on-full-bright is jarring and cancels the contrast effect; mute the background, keep the CTA saturated.
- **CTA color-pop tactic:** pick the CTA color and the background color from opposite sides of the wheel, but mute the background rather than using full saturation on both.
- **Contrast self-check (manual, more reliable than tools in at least one live case):** mentally strip all color and view the design in black-and-white — if the text isn't clearly readable in grayscale, there isn't enough contrast, regardless of how good the two brand colors look together. Automated accessibility/contrast checks are a backstop, not a substitute — one live case showed an automated check failing to flag a contrast problem the manual grayscale test caught.
- Dedicated **color-contrast-checking tool** (unnamed website, pass/fail per hex pair; a Chrome extension version also exists) — sample the actual background/text hex values and iterate. Darker backgrounds (near-black, e.g. `#191919`) with white text reliably pass; **midtone grays are the most likely to fail** — test each color pairing independently, don't assume one passing combination generalizes (e.g., gold text generally fails on white but passes on black).
- Real legal stakes: an actual lawsuit was referenced where an attorney defended a client sued over insufficient site contrast for visually impaired users — treat WCAG contrast as a compliance/liability issue, not just aesthetics.
- Never pure black on pure white (or vice versa) — reads as visually "vibrating," harder to read. Use soft/dark gray for body text, near-white (not muddy gray) for backgrounds. Avoid pure white and pure black in a palette generally — a "hint of color" elevates the design and avoids looking basic; a dark navy works better than pure black against a light/pastel brand color to avoid stark clash.
- Color-to-audience associations used repeatedly:
  - Clean/soft **blues** → trust, professional/corporate (B2B, office workers).
  - **Pinks/pastels** → playful, kids/birthday-party audiences.
  - **Muted, unsaturated greens and beiges** → organic, clean-ingredient, natural products.
  - **Bold lime green or red on a dark background** → energy, gym/fitness/bulk-up audiences.
  - **Gold against black** → rich/luxury feel (used for a yacht brand).
- Yellow is inherently attention-grabbing (aside: the Simpsons are yellow specifically because Matt Groening wanted a color that stood out while people were flipping channels) — great as a small accent, risky as a large background because the same "stand out" property overwhelms at scale. Generally, yellow/gold is hard to see on white.
- **Building "gold" as a usable color:** gold almost never works as one flat hex value — build it as a gradient using several gold-adjacent tones; keep the lightest stop from getting too close to white (unreadable text on top), darken any stop reading too pale, and still add a dark overlay/gradient before placing white text on it. A gold hex landed on in one session: approximately **#A58D66** (transcribed inconsistently, treat as approximate).
- **Multiply blend + gradient legibility trick:** draw a rectangle over a photo, set both gradient stops to black with one end's opacity dropped to transparent, turn off its border, set blend mode to **Multiply** — deepens/darkens the photo under text without fully hiding it. Available in essentially any design tool.
- Palette sourcing: search **"[color] color palette"** or **"[vibe] color palette"** directly on Pinterest (e.g., "navy blue color palette," "health conscious earthy tones," "playful color palette") to pull coordinated real-world palettes — Leanne's and Matt's go-to method. Fuller workflow: (1) ask AI to help define your target audience, (2) ask AI what "vibe" that audience responds to, (3) search that vibe phrase on Pinterest for mood boards/palettes.
- Wix-specific: accent-color swatches capped at exactly **4** in the Color Theme panel — plan the palette to fit; Wix's own color picker flags insufficient contrast in real time as you pick.
- Logo constraint: max **3 colors** (1 primary + 2 secondary) keeps print reproduction and color-selection simple; never use gradients inside a logo (hard to reproduce in print). Exception: online-only brands with no print constraint can use more.
- A brand's logo carries only a fraction of its overall "vibe" signal — color and font choices carry most of the audience-fit signal and can be revisited independently of a logo redesign (demonstrated: the same logo supported two completely different audience-facing vibes on one agency's own site, purely via a color/font swap).

---

## 6. CTA Design & Conversion

- **One dominant/primary CTA per page or section** — solid, bold, high-contrast color. Any secondary CTA (e.g., "book online" vs. "call") must visually recede: outline/transparent style, or a neutral/white fill. "If people have too many choices, they sometimes just choose not to make any choice" / "it eliminates decision fatigue because we're telling people exactly what we want them to do." Which action gets the solid/primary treatment should follow whichever channel that specific business actually converts better on — not a fixed default.
- **Hover-state rule:** default outline-only hover is weak — override it. Same-color hover = a darker shade of the same base color. Full-swap hover = switch to a different theme color entirely, and also swap the text color for contrast (e.g., teal fill + white text on hover).
- CTA copy must always name the specific thing on offer — never ship a bare "Learn more," "Contact Us," or "Book Today." Examples used live: *"Start your corporate video today"*; *"Book a massage appointment"*; *"Start your logo design"*; *"Learn more about our deep tissue massage services"* (run an overlong version through ChatGPT to tighten); *"Discover [what's weakening your body]"* — intriguing verbs over flat action labels.
- Placement: a CTA in the hero, a CTA in every section, and a final CTA at the very bottom of **every** page on the site (not just the homepage/landing pages) — a visitor who scrolls to the bottom should always have a next action.
- Diagnostic: traffic is fine but form fills are low → the first lever to pull is CTA button **color/contrast**, not copy or offer.
- Response-time trust line near a CTA: a specific number ("we respond within 24 hours"), ideally personalized with a name ("Amanda will review this and get back to you") so it feels human, not automated.
- Iterating on an already-converting site: don't guess-and-change. Establish current lead/quote volume first, then test **one variable at a time** (e.g., CTA color) and measure for roughly **a month** before deciding a change actually helped — testing intuition doesn't always predict outcomes (one attendee's own A/B test of moving a "featured on" press-logos section to the top performed *worse*, with no clear reason found).
- **Anchor-link CTA** (see §2.6) as a scroll-to-section alternative to a hard page-load CTA — same technique across Elementor, Divi, Showit, Squarespace.

---

## 7. Trust Signals & Social Proof

- Hero trust row: pick **~3** from years of experience / # happy clients / licensed-insured / star rating.
- Star-rating build (Figma or any tool): 5 star shapes (native SVGs if using a shape tool), duplicate rather than re-add each one, gold/yellow fill (matches Google's star color), pair with bold text like "Rated 5 stars on Google" hyperlinked directly to the business's real Google review link (pulled from the Google Business profile) — showcases and can collect reviews simultaneously. Consolidate into **one** prominent placement (e.g., in the hero, replacing a generic "Welcome" headline) rather than repeating the same trust signal in multiple spots on one page — repetition dilutes rather than reinforces. Don't turn it into a big clickable button; the goal is display, not sending traffic away to the reviews page.
- Don't stack every trust-builder (photos, star ratings, org logos) at the very top all at once — reads as busy/overwhelming; place them in a simple row further down instead.
- **Screenshots read as more "real"/authentic than over-polished imagery**, especially now that so much content is visibly AI/"vibe coded" — prefer screenshots and slightly unpolished proof for testimonials/results.
- Testimonials: no single dedicated page required — sprinkle contextually on the homepage **and** the specific service pages they're relevant to; a standalone reviews page can exist in addition, not instead. Always use **real** reviews in production — fake/ChatGPT-generated testimonial text is for demo/illustration only, never ship it live.
- Real photos of the actual team/business build more trust than stock or AI images ("everyone is always a little bit on high alert when they are on the Internet... nervous about scams" / "having authentic photography automatically helps alleviate some of that anxiety"). A founder/team photo on an About page humanizes the brand — "you are a real person, not just a stock photo template."
- Embedding a live Google-reviews plugin vs. pasting review text: a plugin can slow the page (verify with PageSpeed Insights) but pasted text still contributes word count/SEO value — the plugin sends **no extra trust signal to Google** beyond the visible text ("it doesn't send a signal to Google — it just kind of sees the text on your website").

---

## 8. Images, Media & Icons

### 8.1 Hero image specs
- Recommended dimensions (multiple values cited across calls — all in the same ballpark, use whichever matches the platform's canvas): **1440×720px**, **1400×740px**, **1440×740px**. Export as **WebP**.
- Design/export desktop images at roughly the size they'll actually display, not oversized — one designer's working canvas width for a full-width desktop hero context was **1400px**; don't go bigger unless designing specifically for a TV/large screen. A half-screen-width image should be exported around **500–700px** wide (a ~1200px content column, half-width image ≈ 500–700px; one call cited 540–600px for the same scenario).
- Checking for an accidentally oversized upload: right-click the live image → **"open image in new tab"** to see its actual rendered pixel dimensions, then compare to how much screen space it visually occupies.

### 8.2 Format decision tree
- **SVG**: only for genuinely vector-sourced art (icons/illustrations) — smallest file size, infinite scaling, zero pixelation. Exporting a photo/raster image as SVG (or a ChatGPT-generated "logo" that's actually raster) gives zero benefit — it's still pixel-based underneath.
- **PNG**: preserves transparency (needed on colored/photo backgrounds, or logos) — bigger file than JPEG.
- **JPEG**: default/smallest usable size when transparency isn't needed; fallback when a transparent background can't be isolated.
- **WebP**: best for photographic images generally — not producible directly inside Figma; rely on a WordPress plugin (name transcribed inconsistently as "Imagify"/"Image 5"), a page-builder's own image plugin, or a free web converter (e.g., **Free Convert** — free tiers commonly cap around **10 conversions/day**; rotate to another free converter once capped). One case: manually converting ~500 Shopify product images one-by-one after bulk tools failed, landing around **11–19KB** each.
- Two logo versions are standard: a full-color version for the header, a white version for the footer.

### 8.3 Background removal
- **Figma**: built-in one-click "Remove Background" (works on a solid/white-background source image).
- **Photoshop**: double-click the layer to unlock → built-in AI "Remove Background" (one click) → Crop tool to trim empty canvas → File → Export → Save for Web → **PNG** + check the **Transparency** box (skipping this box saves a plain white background instead).
- **Canva**: Background Remover tool — **Pro-only feature**, not available on the free tier.
- **Wix**: has this natively as a one-click AI feature. **WordPress has no native tool** — you must go outside the platform (Photoshop, Canva, or a plugin).

### 8.4 Photo sourcing & quality
- Preference order: **real/own photography** (of the actual team/product/work) > **stock** ≈ **AI-generated** (roughly equivalent to each other after real photography). Stock will **not** hurt SEO as long as proper alt tags are included. AI-generated images: no confirmed data either way ("I don't think it would hurt you... but I don't have the stats for that") but likewise conditioned on proper alt tags; AI images don't hurt ranking — the only real concern is brand fit/clash, a design judgment, not an SEO one.
- **Pexels** — go-to free stock source. **Adobe Stock** and **Creative Market** — preferred *paid* sources, especially for icons (colors are customizable, keeps a site's visual language from looking like everyone else's); **Shutterstock** flagged as having declined in quality "lately." Explicit advice against pulling images directly from Google for a live site.
- Never reuse the same photo across more than one page of a site — every page should carry unique photography so it reads as a distinct page with its own message.
- Pick images for the actual **feeling/vibe** you want to evoke, not just literal subject matter (e.g., "a professional, comfortable, consent-based massage therapy experience" directly answers a customer's unspoken fear) — and sanity-check accuracy (don't use a couples-massage photo if the business doesn't offer that service).
- **Low-res/no-good-photo workarounds**: AI upscaling tools — **Image Upscaler**, **Upscale Media**, Canva's built-in upscaler (confirmed to "work pretty well"). Layout alternative: layer a smaller, higher-resolution inset photo of someone performing the service over a blurred/zoomed background image, rather than forcing one big low-quality photo.
- **Adding visual depth without more literal photos**: layer a secondary mood/texture image (e.g., rocks, to evoke a calming massage vibe) behind or beside the main photo, add rounded corners, mute/reduce its opacity slightly — reads as intentional design rather than "copy and paste."
- **Collage-hero technique** for a business spanning multiple sub-topics (e.g., real estate + renovation): build a photo collage as one combined graphic (Canva has ready-made collage templates — 3 images was "a good number" in one live mockup), then place headline + body text beside the collage rather than on top of it.
- **Alternating-layout technique**: Section 1 = text left / image right, Section 2 = reverse, keep alternating down the page — adds visual interest, signals a new section has started, and is a reliable way to lengthen a page without it feeling padded (paired with two-column text splits, subtle background-color shifts between sections, and FAQ accordions as other page-lengthening techniques that don't look like more visible text).
- **Text-over-image legibility fixes**: remove text-shadow (makes letters less crisp); instead split into two columns (image one side / plain background+text the other), or keep one image but add a black/dark or brand-color overlay (opacity slider) to lift contrast, or draw a gradient rectangle + Multiply blend (see §5). A colored block placed only directly behind text within an otherwise busy collage is a weaker, still-cluttered option.

### 8.5 Video
- Don't put sliders or autoplay video at the top of a page — hurts load speed far more than one correctly sized/optimized static hero image. Avoid video backgrounds generally where possible (real tradeoff: only keep if it demonstrably helps conversion/branding enough to justify the slower load).
- If used, turn the video **off on mobile, keep it on desktop** — worst speed hit is mobile-side. Replace a hero video that's just promotional/campaign footage (not showing the literal product) with a static image + text overlay; keep video only when it actually demonstrates the real product/service in action (explicit exception carved out once for a live-calligraphy business, since motion communicates a live-skill service better than a photo ever could).
- Elementor: select the section/container, paste a Vimeo or YouTube background-video link directly into the background-video setting. Prefer **Vimeo** over YouTube for a "nice clean player."
- Screenshot-a-video-frame trick: when full-screen background video isn't available/working on a builder, grab a still frame from the existing video, open in Photoshop, remove any logo/text baked into the frame, and use that as a static full-bleed hero image instead of a small boxed video player.
- Avoid **WordPress Revolution Slider** — flagged repeatedly as a page-speed drag; replace with a single static image.

### 8.6 Icons
- Prefer **buying** icons over free sources: Adobe Stock and Creative Market are the go-tos; buy in **SVG** so color is fully customizable in Figma/Adobe XD to match brand. Free sources like Flaticon require a visible backlink/attribution, which "looks silly" next to small icons on a real site.
- Before buying a pack: list every concept you need represented (e.g., desk work, chronic tension, neck/shoulder tightness, lower back pain), then vet the pack against that list — avoids ending up with an incomplete/mismatched set partway through a build. Prefer smaller, tightly-themed packs over huge bundles (faster to sift through).
- Don't rely on AI (ChatGPT) to generate icons directly — results rarely match intent, and iterating can take as long as sourcing a paid icon. If using AI for icons at all, feed it a reference icon's *style* and ask it to generate in that style, rather than prompting from a blank slate.
- Use a design platform's own built-in shapes/elements (checkmarks, bullets, star shapes) instead of custom-building small graphics from scratch when the platform already has them (e.g., Wix's Decorative → Basic Shapes render as true, recolorable SVGs internally).

---

## 9. Page Speed Optimization

- **Google PageSpeed Insights** is the standard first diagnostic — run it before guessing at any speed complaint. Don't assume a stated cause (e.g., "adding text over images slowed my site") without checking the actual report first; one case's real bottleneck was images that were already correctly WebP but a 7-slide testimonial carousel was the actual drag — proving WebP conversion isn't automatically "the fix" without checking what PageSpeed actually flags.
- Score examples cited live: a glass-jars e-commerce site scored **44** before fixes; a GoHighLevel-built site scored **~88** ("good enough"); a rebuilt logo-design service page went from an SEO-audit score of 71→96 and a PageSpeed score of ~97 up to "98 and 100%, basically" after a full rebuild.
- **WP Rocket** — effective WordPress caching/speed plugin, but can break JavaScript/interactivity; **toggle one feature at a time and retest** after each change, reverting anything that visibly breaks; explicitly test every button/link/dropdown after installing it.
- **LiteSpeed** — Leanne's personal hosting/caching choice.
- **Imagify** (WordPress plugin, name transcribed inconsistently) — converts images to WebP in bulk for smaller file size.
- Font count: more than 3 fonts causes a noticeable speed decrease; 2 is safe — flagged as extra important on **Wix** specifically, which already runs a higher baseline speed issue.
- Common speed killers, repeated across calls: unoptimized/oversized JPEGs; sliders and autoplay hero video (worst on mobile); embedded social-media feeds (Instagram in particular — also sends traffic the wrong direction, away from your site); live-embedded Google Maps iframes (replace with a static linked screenshot); unnecessary plugins/widgets when raw text+CSS would do (a testimonial plugin or embedded review widget is a common candidate to replace with static content if PageSpeed flags a problem); excessive animations/page transitions (default to **none** as a personal baseline — fewer animations directly helps load time).
- Platform speed ceilings: **Squarespace** has "only so much control" over site speed — optimize what's controllable, then shift remaining effort elsewhere rather than chasing an unreachable score; mobile performance score on Squarespace will likely never be very high even with full effort, though performance is only one ranking signal among many.
- Rebuilding a whole site for performance should be the **last resort** — tried only after image optimization (WebP/Imagify) and caching (WP Rocket) have already been attempted.
- A single user's "can't load your site" complaint isn't automatically a site defect: run PageSpeed Insights first — if the site scores fast, the problem is very likely the visitor's own hardware or an outdated browser, not a site-side issue.
- Reading **lazy-loading** as a good sign during a live scroll/PageSpeed check: images visibly popping in as you scroll means only near-viewport assets are loading, which speeds up initial load.
- Sitemap: never resubmit in Search Console more than once, except after a full site redesign — new pages get picked up automatically via re-crawl.

---

## 10. Responsive / Mobile Design

- **Design order: always build for the largest breakpoint (desktop) first**, get that right, then step down through each smaller size in sequence (laptop → tablet → phone) — never start from a mid-size breakpoint and try to make it hold in both directions. A client who designed against a mid-size/"square" ratio first ended up with a layout that skewed on both desktop and mobile.
- Mobile hero content order: **Headline → Copy → CTA → Photo**, stacked strictly top to bottom — never place a photo beside the text on mobile; don't force a full desktop hero photo into a mobile background (won't fit/read well) — place it below the text block instead.
- Left-align mobile body text (reads easier than centered). Keep visible padding on both sides of mobile text blocks so nothing touches the screen edge.
- A padding value tuned for desktop can break mobile outright — one build's 255px side-padding trick (used to force a visual line break) exceeded an entire iPhone-width viewport; mobile needs its own, much smaller value (e.g., ~50px) and possibly a smaller font size to match.
- Font size can legitimately shrink slightly on mobile vs. desktop (screen sits closer to the eyes) — e.g., 17.5px desktop → 16px under a ~720px breakpoint — but this is the *one* thing allowed to shrink; spacing/margins should stay generous regardless of device.
- After finishing a desktop design, switch to the mobile/phone preview and **manually rearrange** elements if the auto-generated mobile layout looks off — don't assume it will just work. In Figma, switch the frame preset to a phone size (e.g., "iPhone 17") to check real-device font sizes/spacing independent of desktop settings.
- Squarespace and some platforms only support two breakpoints (desktop/mobile) rather than more granular sizes — a real structural constraint some businesses (e.g., B2B audiences skewing desktop) have to accept and design around rather than fight.

---

## 11. Platform-Specific Playbook

### 11.1 Wix — new-site build sequence (most detailed step-by-step across all calls)
1. Dashboard → Create a New Site → **skip every Wix AI-tool prompt** (ADI wizard), even if it re-offers → Templates → **Blank Template** → Start from Scratch (deliberate, so you learn to build/modify from nothing).
2. **Global styles first, always**: Site Design → Color Theme, before touching any page.
   - Set base colors (font + background) via hex codes pasted straight from Figma/Canva.
   - Wix's color picker flags insufficient contrast in real time.
   - **Accent colors capped at exactly 4 swatches** — plan the palette to fit.
   - Advanced Settings auto-assigns colors to titles/links/buttons based on base+accent picks — review and manually correct each (e.g., retarget "titles"/"links" from default gray to the actual brand color).
   - Button theming is the fiddliest part — expect real trial and error (contrast failures, hitting the 4-swatch cap while sourcing a hover shade); hover-state fallback used live: switch fill to a different accent color entirely + white hover text.
3. Site Design → Text Theme: pick a Google Font for headings, a second for paragraphs (20px "kind of the standard"); set page background to brand color; set page transitions to **None**.
4. Pages panel: add each interior page as a **blank page**. Blog is added as an **App** (Apps search → Communication category → Blog → confirm it's the actual published "WIX Blog" listing before installing), never as a page — then drag the auto-created Blog nav item into position immediately before Contact.
5. Logo: use the global top search bar → "Logo" (skip Wix's AI logo generator that surfaces here) → export from Figma (SVG only if source art is truly vector; PNG for transparency; JPEG fallback) → upload a color version for the header and a white version for the footer.
6. Header: Add Section (verify it lands in the Header region) → Add Element → Strip → Classic Strip → 2 columns (logo image + nav) → Add Element → Menu Anchors → **Theme Menu** variant (auto-inherits site theme colors/typography). Manually shorten header height as much as possible — the hero below it is the real "valuable real estate," don't push it below the fold.
7. Hero: change section background type to **Image**, verify via Layers panel it's the right layer; export the hero photo with a descriptive keyword-bearing filename (minor nudge, not a real ranking factor); Upload Media, increase section height; add H1 text element (Add Elements → Text → **H1**), recolor for contrast against the photo; verify the actual semantic tag via Edit Text → SEO and Accessibility → HTML tag dropdown (independent of font size); add supporting copy as a **Theme Text** element (inherits site paragraph styling) recolored to match; add a **Theme Button** with real CTA copy, manually reset its Background Fill (and separate hover Background Fill) if the theme color doesn't carry over to the placed instance (a real, expect-it gap between global theme setup and per-instance behavior); set the button's link (a page, or an external booking tool like "Jane App" for service businesses).
8. Star-rating strip: Add Elements → Decorative → **Basic Shapes** (native SVGs, fully recolorable) → star shape, duplicate to build the row → adjacent hyperlinked text ("Rated five stars on Google" → real Google review link) → remove default underline via the separate Underline toggle (not "Change Text Direction"). Multi-select (click + Shift-click) to move/align the group together.
9. Section-by-section builds: new blank section per H2, center-align headline/subhead, use the boundary-outline toolbar toggle to see container edges while positioning, leave a whitespace margin above headings (don't snap fully to the top).
10. Multi-column grids: Strip → Classic Strip → Manage Columns (up to 4) → measure exact gap/padding values from the Figma file rather than eyeballing (one build: 32px gap, 16px corner radius) → verify which layer a padding value actually lands on (strip vs. column) before trusting it → locate the Stretch (edge-to-edge vs. contained) toggle if a section runs full-bleed unexpectedly.

### 11.2 Squarespace
- H1 size/style is globally template-locked — can't resize per instance; accept the large H1 as correct, just verify it isn't visually bigger than the separate "title" style.
- Font-size fields can be set in **REM/percentage units** rather than fixed pixels, causing inconsistent rendering across browsers/devices — switch that field to pixels for standardization.
- Only two responsive breakpoints (desktop/mobile) vs. more granular sizing on other platforms.
- Speed and layout-structure control are both capped relative to WordPress — "only so much control you have."
- One case: layout drifted across desktop/iPad/phone a few days after being set, and a hero video stopped autoplaying roughly weekly (had to be deleted + re-uploaded) — both flagged as known platform quirks, not user error.
- A legacy gallery-only template with zero ability to add text/headings is a real threshold for switching templates or platforms, not something to keep forcing.

### 11.3 Shopify
- Always auto-places its H1 tag inside the site logo, "for some reason" — a known quirk.
- SEO fields: Online Store → Pages → open a page → scroll to bottom → **"Edit website SEO"** → fill Page Title (focus keyword) + Meta Description.
- H1 should describe the actual product/topic, not just be the brand name alone.
- Automatically messes with H1/H2 hierarchy/ordering — flagged as fixable but involved enough to warrant its own dedicated session.

### 11.4 WordPress + Elementor
- Theme Builder: build a custom blog/archive template, assign it to the blog roll — every new post auto-formats into it.
- Elementor Pro Page Settings: edit meta title/description in-canvas via the Rank Math/Yoast box without leaving the visual editor.
- Clone a page via WP admin → Pages → hover → **Clone** (works even on Elementor Pro pages) instead of Elementor's "save as template" flow — immediately update the clone's Title and URL/slug afterward so it doesn't sit live as a duplicate (e.g., "about-2").
- Container/Min-Height set in **VH units** (100 = full screen, 80 ≈ 80% of viewport); background image settings: no-repeat + display size **cover**.
- Use the **Heading element** (not a text-editor element) to set/lock the semantic tag — a text/paragraph element can't reliably hold a true H-tag.
- Parent/child container nesting for rows/columns: parent sets direction (row/column), children are dragged inside.
- Padding vs. margin: padding = space inside a container; margin = space pushing elements apart. Padding fields have a link/unlink toggle — unlink to set top/bottom (or per-side) independently. Default section padding used repeatedly: **2em** top/bottom (one build used 94px, another 10em bottom / 0 left-right on a hero). Use a container's **Gap** setting (e.g. 25px) to standardize spacing between children instead of manual per-child margin.
- Pasting copy from Google Docs/Word: paste into the **code editor**, not the visual/WYSIWYG editor — the visual editor silently carries over hidden style tags from the source doc and can render wrong.
- CSS ID field (Advanced tab) for the anchor-link/jump-link technique (§2.6).
- Speed: **WP Rocket** for caching, **LiteSpeed** as an alternative, **Imagify** for WebP conversion — see §9.
- Request fast indexing: Google Search Console → Pages report → **All Known Pages** tab (not "Discover/not indexed") → paste the URL → Request Indexing.
- Redirects when changing a ranking URL: a WordPress redirect plugin, 301s from old → new.

### 11.5 Other platforms — quick reference
| Platform | Key note |
|---|---|
| **GoHighLevel** | Return in an H1 field creates 2 H1 tags — fix with padding, not a hard return |
| **Square** | No true H1 field — hover-description field reads as alt text only |
| **Kajabi** | Inflexible blog template; H2 auto-pulled oversized onto blog roll — patch with inline `<span>` or ChatGPT-generated HTML/CSS |
| **Kadence Blocks** (WP) | Has one free blog-post pattern in its design library; unclear/undemoed how to connect it live |
| **Ghost** | Standalone blog platform; described as "structured, simple, nice engaging template" out of the box |
| **SmugMug** | Limited customization but supports raw HTML blocks anywhere (including footer) — the workaround for building real navigation |
| **Showit** | Discussed hidden-page bandwidth (20 hidden pages = fine; "if you had like a hundred," it could matter); platform-switch framework below |
| **Kukui** (automotive-specific) | Limits adding new template rows/sections; ask ChatGPT "I'm using this platform, how do I add in another section" as a workaround |
| **Divi / Elegant Themes** | Same CSS-ID anchor-link concept as Elementor; building without a wireframe first caused mid-build rework in one case |
| **Webflow** | Referenced only in passing — "none of them suck," pick whichever you're comfortable maintaining |
| **WooCommerce / BigCommerce** | Both "work great" but need a developer to set up properly — more setup friction than Shopify/Squarespace |

- **Platform-switch decision framework** (asked whenever a client wonders whether to migrate, e.g. Showit → WordPress): (1) is the current site already ranking? If yes, stay put. (2) Does the owner find the current platform easy to use? If yes, stay put — because a more "powerful" platform's flexibility only helps if it doesn't also cause the owner to abandon consistent updates/blogging. General maxim repeated across calls: **"any platform can rank — Google doesn't care about the platform you're using."** WordPress is popular with agencies because it maximizes *their* flexibility to optimize, not because Google favors it. Don't platform-hop chasing a "gold standard" — migrating means redoing everything and risks a temporary ranking dip; migrate the domain/URL structure as-is if you must move a ranking site, and set up 301 redirects for any URL that changes.

---

## 12. Backlinks (brief — flagged repeatedly as Matt/Denroy's specialty, not Leanne's)

- Easiest starting point for a site with zero backlink strategy: join the local **Chamber of Commerce** and similar business associations for easy, legitimate backlinks.
- Guest-post on other people's websites/blogs with a link back embedded in the post.
- Want **authentic** backlinks — avoid building "a little network of just people backlinking with one another." A prior every-Tuesday reciprocal blog-linking arrangement within one accountability group was explicitly flagged by Matt as something to stop doing.
- A paid service charging ~$40–50 to get a client "published on Forbes and other media outlets" as a backlink play came up once — deferred entirely to Matt as the backlink expert, no verdict given.
- Backlink-building questions are consistently routed to Matt's own Insiders material or a dedicated Denroy technical-SEO session rather than answered live in these design calls.

---

## 13. Ranking & Content Maintenance Rules

- **If a page already ranks, leave its content/URL alone** — just reorganize the layout/formatting if needed; don't rewrite verbiage or swap images just for polish, since editing settled, ranking content carries more downside risk than upside. **If a page isn't ranking (or ranking weakly), you're free to rewrite/redesign from scratch.** This exact framework recurs multiple times as a repeatable decision rule, not a one-off judgment call.
- Ranking-but-flat-traffic diagnosis: don't rewrite the service pages — keep blog posting (targeting easier-to-rank keywords) and internally link those posts back to the service pages to help push them higher. Same fix applies to pages that aren't ranking yet, if they're otherwise "set up correctly": more time + more interlinking, not necessarily a rewrite.
- New sites/redesigns need real time to build traffic even while already ranking page-1 on some terms — upward movement is "on the right track," not a problem to panic-fix.
- Batch editing is safe for on-page elements (titles, meta descriptions, H-tags) across many pages in one sitting. It is **not** safe to publish a large batch of brand-new blog posts all at once — roll those out gradually.
- Once a page starts ranking well, stop touching its title/headline — pre-ranking is the free experimentation window; post-ranking, retitling risks the rank already earned.

---

## 14. Tools & Resources (master reference)

**Design/wireframe:** Figma (industry standard; free tier sufficient for most use; Play-mode prototype preview; Remove Background; Option-drag duplicate; Shift-click multi-select; per-object Export panel JPEG/PNG/SVG/PDF; orientation/fill filters for stock photos; swatch-box technique for palette reference; onscreen measurement squares for exact pixel gaps) · Canva (valid lower-cost alternative; ready-made collage templates; built-in AI upscaler; Background Remover is Pro-only) · Adobe XD (Matt's preferred tool for demos — "actually a little easier to use" than Figma, but flagged as risky long-term since Adobe stopped updating it; no live font preview in its font picker) · Photoshop (AI Remove Background; Save-for-Web PNG+Transparency export; pulling/cleaning a still frame from video) · pencil and paper (a legitimate substitute for any of the above).

**AI:** ChatGPT — generating first-draft page copy from a wireframe/keyword brief, tightening CTA copy, generating alt text/image titles (prompt: *"give me an SEO friendly title in alt text for this image"*), generating custom HTML/CSS snippets for locked-platform bugs (prompt pattern: *"I'm using this platform, how do I add in another section"*), generating headline ideas around a focus keyword (*"give me some ideas — use this focus keyword and write a headline with it"*), generating placeholder demo testimonials (never for production), generating logos (raster output — not vector, so no true SVG export), and as a weak/unreliable icon generator (better used to extend an existing icon's *style* than to generate from scratch). Claude / Claude Design — design rendering from an uploaded Figma file; not used for full site development due to token cost.

**Stock imagery & icons:** Pexels (free, go-to) · Adobe Stock (paid, icons + photography) · Creative Market (paid, icons/logo templates, SVG format) · Shutterstock (flagged as declined in quality) · Flaticon (free icons, but requires attribution backlink) · Image Upscaler, Upscale Media, Canva's upscaler (fixing low-res photos).

**Speed:** Google PageSpeed Insights (the standard diagnostic) · WP Rocket (caching; breaks JS sometimes — toggle+retest) · LiteSpeed (alternative caching/hosting) · Imagify (WordPress WebP plugin) · Free Convert and other free JPEG→WebP web converters (commonly capped ~10/day on free tier) · HTML to Design (Figma plugin — imports a live site's existing design into Figma non-destructively for mockup purposes) · Font Ninja (identifies fonts used on a live site).

**SEO:** Yoast (WordPress SEO plugin; File Editor for robots.txt) · Rank Math (WordPress SEO plugin, Matt's own preference) · Google Search Console (Pages report/All Known Pages/Request Indexing; sitemap management) · Hey Tony Page/Site Audit tool (heading-structure + keyword-density scoring) · Hey Tony headline tool (verifies a focus keyword actually recurs across a page's copy) · Ubersuggest (keyword research, one attendee's tool — deemed "overwhelming" for per-page keyword decisions by that attendee, not otherwise critiqued).

**Color:** Pinterest (palette/vibe search) · color wheel (complementary/analogous reference) · unnamed color-contrast-checking website + Chrome extension version.

**Hosting/platforms:** SiteGround (Leanne's own host) · Wix, Squarespace, Shopify, WordPress+Elementor, GoHighLevel, Kajabi, Kadence Blocks, Ghost, SmugMug, Showit, Kukui, Divi/Elegant Themes, Webflow, WooCommerce, BigCommerce, Square (see §11 for specifics).

---

## 15. Recurring Demo Builds (worked examples used across multiple sessions)

**"Serenity" — Winnipeg Massage Therapy Clinic** (the primary recurring teaching vehicle, built up incrementally across at least five sessions): brand palette teal/green/gold ("really earthy"); target personas — busy professionals, athletes, desk workers, people recovering from injury/surgery; core services — Deep Tissue, Relaxation, Sports Massage; focus keyword "massage therapy in Winnipeg." Across sessions this build produced: full homepage (hero, trust stars, 4-persona icon-box section, services, testimonials, process, FAQ, final CTA — grid 12-col/72px/32px gutter, desktop frame 1440px, H1 Noto Serif ~60-64px, H2 ~40px, body Open Sans 20px), a full About page (hero with brand-color bg + white H1, trust H2, two 2-column trust/founder modules, CTA — section padding 94px, CTA box 1140px wide/16px radius, desktop hero side-padding 255px/mobile ~50px), a Services Overview page and a full Deep Tissue Massage individual service page (icon-cube "who it's for" section, benefits checklist, plain-paragraph "what to expect," local-keyword CTA), and a live Wix rebuild of the homepage hero/header/star-strip/why-choose-us section/4-column grid (first column only, time-boxed) matching the Figma spec 1:1 (Wix accent colors capped at 4 swatches; button theming required manual per-instance overrides).

**"Winnipeg Movers"** (a separate, previously-completed real client site, shown as a finished reference): sans-serif typography (vs. Serenity's serif) for a deliberately "hardworking" vs. "classier" brand feel from the identical underlying wireframe; services shown as icons (not photos) each linking to its own service page; confirmed via the Hey Tony headline tool that "Winnipeg Movers" recurs correctly through the H2 copy; process section: get a quote → plan your move → moving day.

**"Winnipeg Logo Design"** (Leanne's own service page, live SEO rebuild demo): before — Hey Tony Audit score 71, missing H1, keyword-stuffed, zero H2s, disordered H3/H5s, one oversized/no-alt-tag image, vague headline, weak copy, generic stock imagery, a wall-of-text section, over-centered alignment. After — Audit score **71 → 96**; PageSpeed **97**, then **98–100%**. Rebuild used a 3-column icon grid (pen/multi-mark/book icons for "custom logo design"/"brand identity"/"digital assets"), alternating image/text sections, an FAQ accordion (left unstyled to true H2 due to time, a conscious tradeoff), hero CTA "Start your logo design" (teal bg, navy text, 16px radius), example alt text "Winnipeg logo designer Leanne Jones," and image spec 500×375px.

---

## 16. Case Studies — Real Attendee/Client Sites (condensed)

Grouped by the core issue diagnosed, since the same handful of problems recur across nearly every reviewed site.

**Heading/H-tag bugs:** Spoon (chaotic branding site) — duplicate H1 (title + a second in-body H1) both firing; removed the duplicate, bumped title 20px→32px, repositioned "read more." Kelly's Kajabi blog ("How to Heal From Narcissistic Abuse") — heading auto-pulled oversized/mistagged on the blog roll; patched with an inline `<span style="font-size:30px">`. Ariel (photographer, Showit) — one element auto-tagged H1 reclassified to div/span since it wasn't meant to be the page heading. Kai (Muskoka realtor) — developer had styled headings visually but with wrong HTML tags; fixed via Elementor's title-element HTML-tag setting. Catherine/Plum's Laundry (Shopify) — H1 stuck in the rotating promo hero; moved a fixed keyword H1 below the hero instead. Benjamin (dev agency) — H5/H6 used where H3 belonged; converted.

**Contrast/legibility:** Carol (corporate photographer, Squarespace) — white-on-near-white text passed the automated contrast checker but failed the manual grayscale test; a live lawsuit reference (attorney defending a client sued over insufficient contrast) was raised in the same category of call. An unnamed attendee's About section — pure-black-on-white read as "vibrating"; fixed with `#191919` bg + white text; her gold brand accent failed on white but passed on black.

**Busy/cluttered hero or nav:** Aspire Peak Properties (Chantel, property mgmt) — box-shadow "early-2000s" look, Times-New-Roman-style body font, low contrast, three unclear next steps; fixed via HTML-to-Design import (removed shadows, added section-tint backgrounds, solid buttons, Open Sans body, more line-height). "Going Wild" pet brand (Shopify) — scroll-catching fixed-height animation competing with the CTA; vague banner copy ("we love pets") swapped for a concrete offer and frozen from auto-scroll. Personalized Wellness Solutions — gradient/bubble nav effects, ambiguous logo, centered body copy, glow/text-shadow over a busy image, no CTA anywhere; identified "iridology" as the highest-value page and redirected the hero CTA there. Niri (jeweler) — 3-slide rotating hero carousel replaced with one static hero + stacked full sections per theme, since most visitors scroll before slide 2 ever shows; orange accent (read as mismatched against a decades-old, established brand) replaced with a Pinterest-sourced navy/gold pairing.

**Message-mismatch hero:** an electrician/sauna-lighting installer (Vancouver) whose hero photo of a bright sauna interior made first-time visitors think it was a sauna company, not a lighting installer — fixed by re-selecting photography that shows the actual service being performed.

**Missing/weak CTAs:** Garden Fairy Botanicals (Susan, seed business) — zero CTAs anywhere on the site despite getting daily organic orders off unstructured "info dump" copy; recommendation was headline-led chunking of the existing copy (not a rewrite, since it's already ranking/converting), plus adding CTAs. A cleaning-business site ("Cincy Maid") — multiple competing "Book Now" CTAs, unbalanced hero whitespace explicitly tied to trust risk for a cleaning business ("if your website looks a little messy and you're a cleaning business, there's a disconnect"). Fresh Paint Studio — no hero/intro section at all before the class list; added one using "Toronto Art Studio" as the likely keyword, praised for using **real** (non-stock) class photos as a trust signal.

**Page-speed root causes that weren't images:** Leanne's own "Baby Making Genius" GoHighLevel site scored ~88 with images already correctly WebP — the actual bottleneck was a 7-slide testimonial carousel, not image format. A temporary-tattoo e-commerce site — low-contrast CTA plus a video hero measurably slower on mobile; fixed by disabling video on mobile only (kept on desktop) and converting images to WebP.

**Platform-locked or dev-blocked pages:** Pavitra (interior design, legacy Squarespace gallery template) — zero ability to add text/headings; judged as the threshold to switch templates, not force a workaround. Keith (WordPress/Elementor/Rank Math) — didn't know page-cloning existed (was manually rebuilding via "save as template"); one SEO tool falsely reported "no sitemap" while others saw it fine — walked through the WP visibility checkbox + Yoast robots.txt check, root cause not conclusively resolved live. Caroline (Astra Pro/Gutenberg) — wanted to restyle a single word inline; solved via a `<span>` + custom CSS, generated with ChatGPT since she doesn't code.

**Keyword/IA fixes:** Maritzia (comedian, 5 buyer types × 9 cities, plus a book) — homepage "[comedian] in [location]" + per-audience links; book gets its own page; Locations-Served hub + per-city pages, each covering relevant audience types. Fernando/bestbrows.com (Shopify) — no page titles/meta descriptions anywhere; H1 was literally just the brand name; walked through Shopify's SEO fields and a keyword-driven H1 rewrite. Rainbow City/"The Scarf" (drop-shipping) — commercial video hero swapped for a static image + direct product CTA; advised to stop chasing a single homepage keyword and instead push ranking to individual product/collection pages (citing an artist's canvas-print store where every product title repeats "canvas art print" verbatim).

**Multi-location/multi-brand:** Benjamin's dev agency — one combined US+UK page split into separate location pages, plus separate industry-vertical pages; "web development" vs. higher-volume "web design" resolved by adding the second term as a parallel service page rather than replacing, plus a cross-linking blog post explaining the difference. Lux (mechanics-lien filing service) — rewrote a wall-of-text article backlog, gaining **~30% traffic from California** (their target market) but conversion still lagged; root cause was jargon-heavy CTA copy and no bottom-of-page CTA, not the traffic itself.

**Photography/authenticity:** an unnamed member's About page (audited as copy-heavy/bland, "text title, text title") — advised to add ~1 visual element per section and, where literal photos felt over-used, layer a muted mood/texture image instead of forcing more literal shots. Belle (on-site calligraphy) — logo's handwritten-script portion illegible (fixed with more letter-spacing, same style); headline text overlapping a hero photo the client wanted preserved (shifted photo to one side, text to the other); considered an explicit hero-video exception since her service is a live visual performance.

---

## 17. Tradeoffs & Nuance (cross-cutting)

- **Wireframing first vs. building straight into the page builder**: not a hard requirement — real evidence exists both ways (a live attendee who skipped it in Divi had to detour into Photoshop mid-build to resize images; another attendee prefers building/adjusting directly in the live builder and that's "totally okay too"). The consistent finding is that skipping it *can* cost rework, not that it always will.
- **Justified/centered/right-aligned text**: none of these are banned outright — justified text is fine unless it visibly creates "rivers" (font/column-width dependent, harder to manage responsively than in print); centered text is fine for short headlines/blurbs but hurts readability at paragraph length; right-alignment is avoided altogether since it fights left-to-right reading habits.
- **Two competing CTAs**: never solved by removing one — solved by establishing a clear visual hierarchy (one solid/primary, one demoted to outline/secondary), because real businesses often do have two legitimate conversion paths (e.g., call vs. form).
- **Stock vs. AI vs. real photography**: real always wins on trust, but stock and AI are both SEO-neutral with proper alt text — the tradeoff is authenticity/brand-fit, not ranking risk.
- **Video backgrounds**: a genuine cost/benefit call, not a flat ban — video helps most when it actually demonstrates the product/service (or, per one explicit exception, a live-performance skill), but always costs load speed, worst on mobile; the default lean is to skip it when a static image would communicate the same thing.
- **Platform choice**: consistently framed as *not* a real SEO lever ("Google doesn't care about the platform you're using" / "none of them suck... they all do, good, as long as you are comfortable working on it") — but real, concrete platform limitations still get worked around case by case (Squarespace's global H1 lock, Square's missing H1 field, GoHighLevel's return-creates-2-H1s bug, Shopify's logo-H1 quirk, Kajabi's blog-heading bug) rather than treated as launch blockers. The line for "switch platforms" is drawn only when a platform blocks core functionality entirely (e.g., a legacy Squarespace template with zero ability to add text).
- **Redesign scope is entirely conditioned on ranking status**: strong existing rankings → preserve verbiage/keywords/URLs, restructure visually only; weak/no rankings → free rewrite. This exact framework recurs as a repeatable decision rule across multiple, unrelated calls — not a one-off judgment.
- **Automated contrast/accessibility tools are a backstop, not a substitute** for the manual grayscale readability check — at least one live case showed a passing automated score on a design that clearly failed the manual test.
- **Complementary-color contrast only works at an unbalanced ratio** — the same two colors that make a CTA pop at a small percentage cancel each other out at 50/50; similarly, a color's "attention-grabbing" property (yellow) that makes it a great accent makes it a poor dominant/background choice.
- **Length is not the enemy — undifferentiated density is.** Nearly every "wall of text" complaint across every call was resolved with spacing, sectioning, and headline-led chunking, not with cutting copy; several sources explicitly warn against reducing existing SEO copy to "look more minimal."
- **Testing intuition doesn't reliably predict outcomes**: at least one attendee's own A/B test (moving a trust element to the top of a page) produced a worse result with no clear diagnosis — reinforcing the rule of testing one variable at a time and waiting roughly a month before concluding anything.
