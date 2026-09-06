# Web Design for SEO — 18.03.2026 (Leanne Jones, Leanne Digital)

## Tactics & step-by-step how-to
- Design process: wireframe/sketch the site in a design tool **before** building in the page builder — not mandatory ("do whatever works best for you"), but it locks image sizes/copy in advance so you're not resizing assets mid-build.
- Standard service-business homepage wireframe, top to bottom:
  1. **Hero**: H1 (business description, simple/clear language) → subhead paragraph → CTA button, all visible with **zero scrolling**, plus a trust signal (reviews/stat/logos) right in the hero.
  2. **About Us** (H2, includes the focus keyword) + audience-identifier icons so the visitor self-identifies ("oh yeah, I'm actually a person working at my desk with back pain — this speaks to me") + its own CTA.
  3. **Services overview** (H2) — brief intro to each service, each linking out to its own dedicated service page.
  4. **Testimonials / past clients** — keeps building trust as the visitor scrolls.
  5. **"Next steps" process section** (e.g., massage therapy: book appointment → assessment → target treatment) to defuse first-time-buyer anxiety.
  6. **FAQ** — same anxiety-reduction purpose, doubles as an SEO play (Google rewards on-page Q&A) and is a low-friction way to add word count without a wall of text.
  7. **Final CTA** — every single page should end with one.
- Divide every page into sections; **one section = one H2 = one topic**, same logic as essay headers/paragraphs.
- Put a CTA in every section, not just once on the page.
- Pick the CTA button color for contrast against its background so it visually pops — doesn't have to be the primary brand color (demoed gold on a teal/gold/green brand).
- Location strategy: pick **one** primary location + the focus keyword for the homepage (e.g. "[keyword] in [City]") — far easier to rank than competing broadly (e.g. targeting all of the US). If you serve many locations, build one "Locations Served" hub page linking out to an individual page per location.
- Multi-audience-segment or multi-city businesses: homepage names location + role, links out to one page per audience segment; for multiple cities, build an overview/hub page + one page per city, and re-cover the relevant audience segments *within* each city page (don't multiply pages endlessly — "I wouldn't make like a bazillion pages").
- Product-based sites: reuse the exact same homepage wireframe, just swap "services" for **product categories**, each linking to product pages.
- Long service lists (e.g. general contractor): don't dump every micro-service on the homepage — list core services prominently/accessibly, push the long tail into a **mega menu**/dropdown, each item linking to its own detail page (e.g. "plumbing" → its own page).
- Cluttered "who we serve" / client-niche lists: treat it as a **layout** problem, not a content problem — repeat a clean card/section design per niche instead of dense paragraphs/columns; can also become its own dedicated page linking to per-niche detail pages.
- Live Elementor build sequence (demoed end-to-end for a "Massage Therapy in Winnipeg" page):
  1. Create the page, title it, set a **Featured Image** (used as the social-share/OG image) with descriptive alt text (e.g. "Winnipeg Massage Therapy Clinic").
  2. In Elementor page settings, turn the default page title **off** if you're building a custom H1 inside the builder.
  3. Add a **Container** → add a background image → set **Min Height** in **VH** units (vertical height) — `100` = full screen, `80` ≈ 80% of viewport.
  4. Background image settings: **no-repeat** + display size **cover**.
  5. Add the H1 using a **Heading element** (not a text-editor element — only the Heading element lets you set/lock the semantic tag); match font/size/line-height to the mockup.
  6. To vertically center hero content: select the parent container → **Layout** → center.
  7. For side-by-side layout, nest containers: the **parent** container sets the direction (row/column), drag child containers into it.
  8. Add the button element; color from the brand/logo palette; check text-color contrast (e.g. white text on a gold button).
  9. Repeat one container block per H2 section; **alternate light/white background colors** between sections to visually divide them.
  10. For grid layouts (e.g. 4 columns): one wrapping container + 4 child containers, set direction on the parent so children line up in a row.
  11. Publish, then run the page audit tool to confirm H1 → H2 → H3 order is correct.
- Padding vs. margin: **padding** = space inside a container; **margin** = space pushing an element away from the container.
- Default section padding: **2 EM** top and bottom (Elementor: Advanced → layout/margin → switch unit to EM → unlink to set top/bottom independently) — consistent top/bottom padding across sections adds visual consistency.
- Use a container's **Gap** setting to standardize spacing between its children (e.g. set to 25px) instead of manual margin on every child — treat it as a reusable spacing preset.
- Cloning in Figma/Adobe XD on Mac: select the object, hold **Option**, drag to clone (or plain copy/paste).
- Fixing wrong heading tags on an existing build: click the heading element → find the **HTML Tag** field/dropdown → set to H1/H2/etc. If the font goes "crazy" when you do this, it's likely inheriting a **global style** tied to that tag — check global settings, and make sure it's a true Heading element (not a text/paragraph element) so size/color can be restyled independent of the semantic tag.
- Mobile design workflow: design desktop first, then adapt to mobile. **Left-align** mobile body text (reads easier than centered). Mobile hero priority order: **H1 read first → paragraph read second → CTA button visible with zero scrolling → photo placed below the text block** (don't force the full desktop hero photo into a mobile background — it won't fit/read well). Keep visible padding on both sides of mobile text blocks so nothing touches the screen edge.
- Image file names: descriptive, **4–5 words max**, no keyword required (e.g. "Woman receiving relaxing massage.jpeg").
- Alt text: include the **focus keyword only when it fits naturally** — don't keyword-stuff. Example given: a massage photo's alt text should include "massage therapy"; a decorative heart icon's alt text should just be descriptive ("heart icon in a teal color"), not keyword-stuffed.
- Can generate SEO-friendly image titles/alt text via ChatGPT by uploading the image and asking (paraphrased): "give me an SEO friendly title in alt text for this image."
- Migrating CMS platforms while already ranking (e.g. Squarespace → WordPress): keep the **same domain and same URL structure** to preserve as much SEO as possible; expect a possible temporary ranking dip that recovers over time.
- Changing a URL that's already ranking / has backlinks pointed at it: set up **301 redirects** (on WordPress, via a redirect plugin) from the old URL to the new one so existing backlinks/rankings carry over.
- WordPress speed tactics independent of any plugin: use properly sized/compressed images, minimize animations/video, avoid unnecessary embedded widgets (e.g. an Instagram feed embed slows load).

## Rules / dos & don'ts
- Only **one H1 per page** — the sole exception is two H1s that contain **identical text** (typical cause: a separate desktop-H1 block and mobile-H1 block); an audit tool may flag two H1s but it's not an actual problem in that case.
- The H1 must be the literal **first heading tag** on the page — never place another heading (or an untagged "hook" line) above it, regardless of what you want to be visually biggest/first. "It's like the title of the book. You don't have a secondary title before the book starts."
- H1 can be styled to **any visual size** — semantic tag and visual size are independent in builders like Elementor ("not all website editors let you do this").
- Section = H2. Go one level deeper (H3) only for subtopics within that section. Don't go deeper than H3 in normal cases ("you probably won't need to go to like H4"); H4 is only for going one layer deeper still (e.g. listing specific professional types under an H3 about "who we help").
- **One focus keyword per page.** Focus keyword = what someone actually types into Google to find you — not a full sentence, not a random string of adjectives.
- Prefer **"[keyword] + [location]"** targeting over broad/national targeting — much easier to rank.
- Don't embed **social media feeds** on the site — the load-speed cost outweighs the vanity benefit (impressive follower count) unless your following is genuinely large.
- No fixed "maximum" number of services for a homepage — the real rule is keep core services easy/accessible and push depth into a mega menu/sub-pages, not a services-count cap.
- **AI-generated images** don't hurt SEO ranking at all — the only real concern is brand fit/clash, which is a design judgment, not an SEO one.
- Photo-source preference ranking: **real photography** first; **stock** and **AI-generated** images are "about the same" after that.
- Don't force the focus keyword into every alt text — only where it fits naturally.
- Don't over-invest in the image **title tag** attribute — alt text and file name carry the real SEO weight.
- Featured/OG image size: **1200 px wide × 628 px tall**.
- Don't change a ranking page's URL casually — it risks the rankings already earned; redirect it if you must change it.
- Don't abandon a platform/site that's already ranking well just to "optimize" — only migrate if the current setup is genuinely not working.

## Tools, prompts & resources
- **Adobe XD** — Leanne's personal go-to for mockups/hero examples ("I find this one really easy to work with"); has a preview/export-selection feature (also cited for Figma).
- **Figma** — called out as the **industry standard**; used for her own reference wireframes during the live build (pixel-based spacing, container "gap" presets, preview/export button).
- **Canva** — mentioned as another workable option "whatever works best for you."
- **WordPress + Elementor** — platform used for the entire live build demo.
- **Yoast** — SEO plugin shown live; flags a red frowny-face icon when a page has no content yet.
- **Hey Tony's page/site audit tool** — used after publishing to confirm H1→H2→H3 structure and check keyword presence across headings; also the tool that can (harmlessly) flag duplicate H1s from responsive desktop/mobile variants.
- **Google Drive resource folder** (linked in chat) contains: an image/asset-sourcing reference doc, homepage wireframe, service-overview-page wireframe, individual-service-page wireframe, a "website design assets" doc (her tool list), a **ChatGPT prompt doc for generating page copy from the wireframe** (prompt text lives in the doc, not read aloud on the call), and an icon-resource doc. No product-page wireframe yet (planned for a future session).
- **Creative Market** — recommended source for **buying** icons (not free ones); buy **SVG** format so the color can be customized in Figma/Adobe XD to match brand.
- Fonts used in the live build: **Noto Serif** (H1, Google Font, 64px / 64 line-height) and **Open Sans** (H3, 20px).
- ChatGPT use #2: image alt text/title generation — upload the image and ask, in effect, "give me an SEO friendly title in alt text for this image."
- E-commerce platform recommendations for someone moving off Square: **Shopify** (top suggestion); **Squarespace** if product count is low; **WooCommerce** and **BigCommerce** also work but need a developer to set up properly ("a little bit tricky to set up by yourself," though WooCommerce "works great" once done).
- WordPress speed plugin recommendation: **WP Rocket** ("a good plugin to use if you want to speed up a WordPress website"); Leanne personally uses **LiteSpeed**.
- Redirects on WordPress: handled via a **redirect plugin** (no specific name given).
- A technical-SEO/redirect question was explicitly routed to **Denroy's** session (scheduled for the next day relative to this call) as the correct venue for developer-level detail.
- SEO title/slug specifics were deferred to existing paid course material ("all of this is in the course") rather than answered live.
- Next sessions teased: a full **website design-critique** session two weeks out (send links via DM in the Hey Tony group), plus a future session covering **product-page wireframes** and Squarespace-specific capabilities.

## Case studies / examples / results
- **Leanne's own agency site** (Leanne Digital, Winnipeg): homepage intentionally does **not** target a single main keyword; her service page targets **"Winnipeg website design"** and repeats "website design" across multiple H2s (confirmed live via the audit tool).
- Live-built demo page: **"Massage Therapy in Winnipeg" / "Winnipeg Massage Therapy Clinic"** — teal/gold/green brand palette pulled straight from the logo; gold used as the CTA accent color.
- **Unnamed photographer(s)** — one question: multi-genre photographer unsure of a homepage focus keyword; recommendation = location + "photographer," with niches (wedding, family, business/headshots) introduced further down the page. A related/possibly-same attendee separately had an **H1 positioned below** a stylized "mushy catchphrase" headline; resolved as a tag-vs-visual-position issue — the styled catchphrase can stay visually first as long as the keyword line is actually tagged H1 in code and appears first in DOM order.
- **Matt** (attendee) — wanted to change a landing-page URL to be more SEO-driven but has existing blog backlinks pointed at the old URL; advised to set up redirects via a WordPress redirect plugin and referred to Denroy's technical-SEO session for the how-to.
- **Kai** — realtor in **Muskoka**, ~7–8 pages, mostly static except a listings page; recommended keyword = **"Muskoka Realtor"** (location + keyword), not a full sentence or a list of adjectives; also had Elementor heading tags set incorrectly by his developer (visually styled but wrong HTML tag) — fixed via the Elementor title-element "HTML tag" setting.
- **Marissa/Maritzia** — stand-up comedian booked by **5 distinct buyer types** (mentioned: corporate/HOA bookers, private hosts, a senior-community activity director, comedy-club bookers) across **9 cities** (farthest one an hour away), plus sells her own book. Structure recommended: homepage = "[comedian] in [location]" + links to per-audience pages; the book gets its **own page** (not a separate site) with a homepage CTA driving to it; a "Locations Served" hub page + one page per city, each covering the relevant audience types.
- **Unnamed attendee** (name mistranscribed) — product-based business; confirmed the homepage wireframe applies to product sites too (swap "services" for "categories"); requested a DM site review.
- **Catherine** — product-based business on **Square**: the platform has no way to place true live text/H1 directly over the hero image, only a hover-to-reveal image description field, which Google reads as **alt text, not H1** ("it won't read that as your H1 tag... which isn't as powerful as having live text on your website"). Recommendation: treat the platform's one available text field as the de facto H1. Considering migrating for better sales features — pointed to Shopify/Squarespace/WooCommerce/BigCommerce.
- **Leo** — general contracting company (kitchen, bathroom, whole-home remodels, ADUs, plus electrical/plumbing/drywall trade work); asked (1) whether AI-generated project images hurt ranking — no, brand-fit is the only real consideration; and (2) the max number of services to list on a homepage — no cap, just organize core-vs-deep via a mega menu.
- **Attendee (name transcribed "Feet")** — new to Hey Tony via Rank Week; does web design for clients plus her own photography site; previously built directly in **Elegant Themes' Divi** ("Elegant Team DV") without wireframing first, which caused mid-build rework (had to jump to Photoshop to resize images) — confirms the wireframe-first workflow prevents that. Also asked about photo-naming SEO (descriptive file names, 4–5 words, keyword optional; alt text keyword only if natural fit), mobile-responsive workflow, and spacing/padding consistency.
- **Carol** — on **Squarespace since 2014**, **200+ blog posts**, recently upgraded to Squarespace's newest version, already ranking highly, but hitting feature limitations vs. WordPress/Elementor. Guidance: keep the current platform since it's working; a migration risks a ranking dip. Noted that Squarespace's **mobile performance score will likely never be high** even with full effort, but performance score is only one ranking element among many.
- **Alandria** — asked (1) about embedding social feeds (don't — load-speed cost) and (2) as a brand-new online health coach whose homepage is currently philosophy-only with no services listed — recommended **keeping** the philosophy content and **adding** a services section rather than replacing it.
- **Neri** — remote bookkeeping business; one page mixing **monthly bookkeeping** and **one-time catch-up/cleanup** services (transcribed "ketchup cleanup"), plus a dense "who we serve" client-industry list reading as cluttered. Diagnosed as a **layout** problem, not content — recommended a services-overview page linking to per-service pages, and a possible dedicated "who we serve" page listing niches with links to per-niche detail pages.
- **Lupita** — building a brand-new site to replace a defunct one; asked where to source customizable icons — pointed to Creative Market (buy SVGs, recolor in Figma/Adobe XD to match brand).
- **Mark** — asked about plugins for quickly changing heading tags (mentioned Yoast and "Rank" [Math] by name; Leanne didn't confirm either has that specific feature, effectively leaving Elementor's native heading-tag interface as the practical answer) and walked through the H2-vs-H3-vs-H4 section model plus the two-identical-H1s exception using Leanne's own live-built page as the example.
- **Attendee (name transcribed "Hi Jones")** — asked WordPress vs. custom-coded (React/Next.js) for SEO/speed; Leanne's own WordPress site "runs pretty fast"; recommended **WP Rocket**, personally uses **LiteSpeed**; noted a custom-coded site has the highest speed ceiling but only if the client can actually use/maintain it after handoff.

## Notable verbatim quotes
- "A major thing that I find people forget to include on their website is including a call to action button right on their homepage, right on their hero image."
- "It's like the title of the book. You don't have a secondary title before the book starts, so you want the title of the book at the start." — on H1 placement.
- "Sometimes developers and designers aren't paying attention to the H tags. They just design it visually correct, but it's not technically correct."
- On Square's hover-description field: "It won't read that as your H1 tag. It'll read that as alt text, which isn't as powerful as having live text on your website."
- "I would keep whatever is working for you right now... If it's not working, then I would change platform."
- "That's only one element of SEO is your performance score."
- On custom-coded vs. WordPress: "A custom coded website will run the fastest because you have the most control over it... but you also want to make sure it loads on the client side... if it's impossible for the client to use, I wouldn't consider that a good option. Even if it's like the fastest website on earth."
- "I wouldn't make like a bazillion pages." — on how far to take location-page proliferation.

## Tradeoffs & nuance
- Wireframing before building is a personal-workflow choice, not a strict requirement ("this isn't necessarily a necessary step, but I find it helps") — yet a live participant's account of skipping it (direct-building in Divi, then having to detour into Photoshop to resize images mid-build) is real evidence for doing it anyway.
- The "one focus keyword per page" rule can be applied selectively at the site level: Leanne's own homepage deliberately skips a primary keyword target and pushes keyword-targeting down to her service pages instead — not every business needs to fight for homepage keyword rank.
- Location-page depth is a judgment call, not a formula: for a 9-city footprint, the guidance capped at a hub page + moderate per-city depth rather than maximal page proliferation ("I wouldn't make like a bazillion pages").
- Custom-coded (React/Next.js) sites have a higher performance ceiling than WordPress, but raw speed isn't the deciding factor — post-handoff client usability/maintainability matters more.
- Mobile performance score is only one ranking signal; a platform (Squarespace) that structurally caps mobile score isn't necessarily worth abandoning if the site is already ranking well and scoring fine elsewhere.
- Migrating platforms is framed as risky even when the destination (WordPress/Elementor) is objectively more flexible — "if your website is currently working, I would hate for you to move and then disrupt your SEO rankings." Migrate only if genuinely broken, not to chase incremental feature gains.
- AI vs. stock vs. real images: no SEO difference between stock and AI, but brand cohesion (a design factor, not an SEO one) still favors real photography first.
- WooCommerce/BigCommerce are viable and "work great" but explicitly carry more setup friction (need a developer) versus Shopify/Squarespace's more turnkey setup — a cost/control tradeoff, not a quality verdict.
- A platform's structural limitation (Square's lack of a true H1 field) doesn't have a real fix — the practical answer is to work within the constraint (use the one available text field as the de facto H1) rather than force a workaround that doesn't exist.
