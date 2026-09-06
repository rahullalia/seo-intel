# Web Design for SEO with Leanne — 18.02.26

## Tactics & step-by-step how-to
- Master homepage structure (the wireframe used for every walkthrough): **Hero (H1 + supporting text + CTA) → Trust signals (5-star reviews) → About/intro section (H2 + 4 pain-point boxes with icons) → Services (H2, with H3 per service + CTA + link to individual service page) → [optional: Why choose us] → Testimonials → Process/how-it-works (numbered steps) → FAQ → Final CTA**. Longer homepage = fewer people reach the bottom, so most important messages go near the top; every page should end in a final CTA telling the visitor what to do next.
- Copy-first workflow: write all copy before opening a design tool — "the purpose of layout and the design process is to help communicate a message," so nailing the message first makes layout decisions obvious.
- Figma setup from scratch: hit **Design** to open a new file → use the **Frame** tool → pick the **Desktop** preset → set frame background to a dark gray (default is hard to see against) → set canvas/page background separately by deselecting the frame and picking a color.
- Grid setup (click the frame, configure layout grid): **12 columns, centered, 72px column width, 32px gutter** — Leanne's standardized website grid, keeps content "grounded" instead of floating.
- Desktop frame width: **1440px** — the size Leanne always starts from.
- If a frame's dimensions get changed by accident: click the frame's label at the top, use the right-hand toolbar to re-enter W/H numerically; hold **Cmd** (Mac) while adjusting so elements don't drag/move accidentally.
- Logo placement: centered or left-aligned are the two standards. Avoid centered-logo-with-nav-below — the nav bar gets too tall and delays visitors reaching real content; instead put the nav off to the side.
- Build the nav bar as a plain box (send to back in layers), colored to sit quietly behind/beside the logo (e.g. soft gray if the logo has a white background).
- Image background removal: select an image with a solid/white background in Figma → **Remove Background** — one-click cutout.
- Hero image sourcing: search **Pexels** for free stock photos matching the niche; pull color inspiration from the logo palette (e.g. teal/gold/green logo → look for photos with those tones) and pick images reflecting the actual service (sanity-check: would an actual customer of this business find the photo accurate — e.g. don't use a couples-massage photo if the business doesn't offer that).
- Fitting a photo into the hero box: Fill → Image → upload from computer → use the crop dropdown to reposition/scale; a **Horizontal** filter/crop option exists to help fit a vertical photo into a horizontal hero box.
- Hero text legibility: add a color overlay (or gradient) in the brand's primary color over the photo, adjust with the opacity slider, so H1/copy stays readable over the image.
- H1 = the page's focus keyword, kept short (trim a long headline down to just the keyword) so it reads clean over the photo; reposition the photo's subject so the headline doesn't cover their face.
- Supporting/body copy under the H1: shorter block; line-height set to start at the same value as the font size, then adjusted visually until it looks right.
- CTA button color: pick a secondary brand color that visually contrasts with the hero's dominant color (e.g. yellow CTA against a green/teal hero) so it pops; make the CTA visually bold — "the quicker someone can click the button, the more likely they are to book."
- Font pass: start with a plain sans-serif to block things out, then swap to a serif (Leanne used **Noto Serif**) once ready to add personality/polish — serif reads "classier," sans-serif reads more "standard/hardworking"; same layout, different vibe purely from the type choice.
- Trust-signal section: build stars from Figma's shape tool (star icon x5), pair with bold text like "Rated 5 stars on Google Reviews" — place either directly inside the hero or as its own strip right below it.
- About/intro section: duplicate the H1 style for an H2, recolor to a brand color, reduce size vs. H1; reuse/duplicate hero body-copy styling but recolor text to soft black/dark gray (never pure black) and center-align.
- Four-segment pain-point layout: one box per customer type (e.g. busy professionals / athletes / desk workers / people recovering from surgery), each bold ~20px text, boxed with a near-white tint of the brand color as background, rounded corners, plus a small icon per box so skimmers grasp the point without reading — "everyone's just skimming websites, mostly." Icons used: running shoe (athletes), computer (desk workers), heart (recovering from surgery).
- Services section: duplicate H2 style on a white background (to visually separate from the prior section); for each service create an H3 (same serif family as H1/H2 but smaller) plus a CTA linking straight to booking/purchase for that service.
- Two layout options for a 4-service section: (a) four equal boxes, each with its own image/icon — clean but can look like "a lot to digest" at once; (b) alternating text-left/image-right blocks that reverse side each section — reads more like a narrative, better for services needing more explanation.
- Recommend building an **individual page per service**: homepage gives a brief description + a "find out more" link to the dedicated page; the dedicated page carries full detail and can be optimized/targeted to that service's own keyword — doubles as an SEO play (more content, more keyword targeting), not just a UX one.
- Testimonials section: Google reviews, pasted personal reviews, and/or embedded video reviews — placed after services to reassure before moving to process/FAQ.
- Process section: explain what happens step-by-step after someone books/inquires (massage example: book appointment → personalized assessment → targeted treatment session; moving-company example: get a quote → plan your move → moving day).
- FAQ section goes after the process section, to mop up remaining objections before the final push.
- Final CTA section closes every homepage (and should exist on every page of the site, not just the homepage) — give the visitor a next action regardless of where they stop scrolling.
- Preview a Figma design at any point with the **Play** button — renders a click-through, browser-like preview before any development happens.
- Export flow: select the box/frame in Figma → **Export** → assets come out built to the actual scale used on the page, which keeps production images from being oversized and helps the live site load faster.
- SEO/copy QA pass: run finished copy through the **"Hey Tony" headline tool** to confirm the focus keyword actually recurs throughout the page copy (checked live for "Winnipeg Movers" — kept surfacing across the H2s).
- To pad thin word count for SEO, add more content via the FAQ section rather than stuffing it elsewhere.
- Once a site is live on WordPress, edit copy directly on WordPress — don't loop back through Figma for small copy tweaks; Figma is for working out the full design before the initial build, not an ongoing content-editing step.
- Copywriting workflow: do keyword research first, then prompt ChatGPT to write the homepage copy using Matt's ("Hey Tony's") copywriting techniques; Leanne's own wireframe/copy template doc is written so you can "copy and paste this into chat and it would help you write out your copy," then edit the output to match your specific business.

## Rules / dos & don'ts
- Grid: **12 columns, centered, 72px column width, 32px gutter** — standardized, don't deviate without reason.
- Desktop frame: **1440px** wide.
- Logo: **max 3 colors** (1 primary + 2 secondary) — keeps printing and color-selection simple; exception: online-only brands (no print constraint) can use more.
- Never use gradients inside a logo — hard to reproduce in print.
- Never use pure black for body text — use a soft black/dark gray; easier on the eyes, reads more "intentional."
- Body copy size: **16–20px** standard range; don't go smaller than **16px** — it gets too small to read comfortably.
- H1: start around **48px**, then push bigger for impact; uppercase is an option for more punch.
- H2: **40px**+ (about-section headline landed a little over 40).
- H3 (individual service headline, nested under an H2 section): **32px**.
- CTA/body button text: standard **20px**.
- Line height starting rule: set it equal to the font size first, then adjust visually — don't guess a number upfront.
- Longer homepage = fewer visitors reach the bottom, so front-load the most important messages near the top of the page.
- Put a CTA in every section, and a final CTA on every single page of the site, not only the homepage.
- Always build individual pages per service rather than cramming full detail onto the homepage — better for SEO (dedicated keyword targeting + more content) and for conversion clarity.
- Icons: prefer buying them (Adobe Stock / Creative Market) over free sources — free icon sites like Flaticon require a visible backlink/attribution, which "looks silly" next to small icons on a real site.
- Don't rely on ChatGPT/AI to generate icons directly — results rarely match what you actually wanted, and iterating to get it right can take as long as sourcing a paid icon; if using AI for icons at all, feed it a reference icon's *style* and ask it to generate in that style rather than prompting from a blank slate.
- Don't overthink stock photo selection — cap the time spent (Leanne explicitly refuses to spend "probably an hour" agonizing over one photo).
- The design software itself doesn't matter (Figma, Canva, Adobe XD, Photoshop all work) — what matters is thinking the layout through before development.
- Match font personality to brand feel deliberately: serif for a "classier"/"bougie" vibe, sans-serif for a more standard/"hardworking" vibe — pick on purpose, not by default.

## Tools, prompts & resources
- **Figma** (free tier is enough) — Leanne's primary wireframing tool, used before any development; has Play-mode preview, frame/grid tools, image fill + Remove Background, per-box asset Export.
- **Pexels** — free stock photography source used for the hero image.
- **ChatGPT** — used to (1) generate the logo itself for the example brand, (2) write homepage copy after keyword research is done, following Matt's copywriting method, and (3) as a fallback icon generator (weak results per the rules above).
- **"Hey Tony" headline tool** — used to verify the focus keyword actually recurs across a page's copy (SEO QA step), demonstrated live on the Winnipeg Movers copy.
- Icon sources ranked by Leanne's actual practice: **Adobe Stock** (paid, login required) and **Creative Market** (paid, "a lot of fun fonts and icons") are her go-tos; **Flaticon** has free icons but requires a backlink credit.
- Leanne's **Google Drive resource folder** (shared live in the call chat, permissions adjusted on the spot) — contains her homepage wireframe template, the massage-business and Winnipeg-Movers mockups, and asset links. She committed to adding her ChatGPT copywriting prompt to the folder and posting a recap + all resources into the Hey Tony Insiders group after the call.
- Leanne's wireframe/copy template Google Doc doubles as a copy-paste-able ChatGPT prompt base — "you could probably just copy and paste this into chat and it would help you write out your copy," then tailor the output to the specific business.
- Font used in the massage-business example: **Noto Serif** (for a classier feel); Winnipeg Movers used a standard sans-serif instead for a more "hardworking" feel.

## Case studies / examples / results
- **Massage therapy business (Winnipeg)** — built live start-to-finish on this call. Logo (ChatGPT-generated): teal primary, plus gold and green secondary tones, no gradients, 3 colors total. Focus keyword: **"massage therapy in Winnipeg."** Four customer segments called out with icon boxes: busy professionals, athletes (running-shoe icon), desk workers (computer icon), people recovering from surgery (heart icon). Process shown: book appointment → personalized assessment → targeted treatment session. Two hero variants built/compared — Leanne judged the second, simpler version (H1 + short description + CTA) stronger than the first, more elaborate one.
- **Winnipeg Movers** (moving company, previously completed client site) — shown as a finished reference example. Focus keyword: **"Winnipeg Movers"**, confirmed recurring through the H2 copy via the Hey Tony headline tool. Section flow: hero + CTA → trust signals → intro (re-hits focus keyword in H2s) → services shown as icons (not photos), each linking straight to its service page → "why choose us" → testimonials → how-it-works (get a quote → plan your move → moving day) → request-a-quote → FAQ → final CTA. Same underlying wireframe as the massage site, but sans-serif type and a different color story gave it a completely different "vibe" for a more "hardworking" brand feel.
- **Karen** (attendee, coaching/program business) — walked through applying the same wireframe to a service business selling an **~$10,000 online program** plus an **8-week intro program**. Advice given: CTA should be "book a call" rather than "buy" for the high-ticket program (not everyone will pay $10K sight-unseen), but the cheaper 8-week intro course could support a more direct purchase path; recommended building an individual page per service/offer, both for clarity and because it "would be great for SEO too... you can add more content and try and target that keyword."
- **Katie** (attendee, joined late) — asked whether the walkthrough/guide would be posted to the Hey Tony Insiders site; Leanne confirmed she'd post a recap and all resources to the group.
- **Unnamed attendee** — described active friction with a hired web developer: she'd spent two hours sourcing, downloading, and correctly sizing stock photos and handed over a full layout/direction, but the developer substituted his own ChatGPT-generated images instead of her stock photos, and the result came back "bland" and didn't match the vision in her head ("it doesn't flow the way it makes sense in my head"). Separately asked where to find **gold line-art icons** for her "five anchors" — breath, water, movement, sleep, diet — Leanne's answer: buy them (Adobe Stock/Creative Market), since AI generation and free-with-attribution sources are both weak fits for a polished custom set.

## Notable verbatim quotes
- "The purpose of layout and the design process is to help communicate a message."
- "The longer it is, the less likely people are going to reach the bottom of it. So you always want your most important messages near the top."
- "Everyone's just skimming websites, mostly." — the reasoning behind pairing every pain-point block with an icon.
- "Sometimes it's hard to like verbalize what you want visually." — attendee describing the gap between her creative brief and what her developer built.
- "I would find an icon that you like the style of and then say, generate an icon in this style of whatever thing you want to be generated... but then that also just takes a long time to do that way." — on the limits of prompting ChatGPT for custom icons.
- "The quicker someone can click on the button, the more likely they are to book a massage appointment with us." — rationale for making the CTA visually bold.

## Tradeoffs & nuance
- Figma-first mockup vs. building straight inside a page builder/CRM (one attendee mentioned preferring GoHighLevel's built-in flow): Leanne's method takes more upfront manual effort but "gets all the kinks and confusion out" before development, making the actual build faster and cleaner overall.
- Serif vs. sans-serif is a deliberate brand-feel choice, not a default — the exact same wireframe/layout produced a "classier"/"bougie" result with serif type (massage business) versus a "hardworking" result with sans-serif (moving company); the structure carries the SEO/UX logic, the type carries the emotional tone.
- Icon sourcing tradeoff: paid icon sites (Adobe Stock, Creative Market) cost money but deliver consistent, professional, on-brand results; free sites (Flaticon) are free but require an attribution backlink that reads as unprofessional next to small site icons; AI-generated icons (ChatGPT) cost nothing and need no license but are unreliable and can burn as much time chasing the right result as just paying for one.
- Two viable layouts for a 4-item services section trade off differently: four equal icon/image boxes is compact and scannable but can read as "a lot to digest" all at once; alternating text/image blocks reads more like a guided narrative but takes more vertical space — Leanne chooses based on how much explanation each service actually needs.
- Whether trust signals (5-star reviews) belong directly inside the hero or in their own strip right below it is treated as a flexible placement choice, not a fixed rule.
- CTA wording/path should flex with price point and decision complexity: a low-cost, simple offer (8-week intro course) can push straight to purchase, while a high-ticket/considered offer ($10K program) should route to "book a call" instead of a direct buy button.
- Figma is positioned as a pre-build planning tool, not a permanent source of truth: once a site is live, small copy edits happen directly on WordPress; looping back into Figma for every tweak is called out explicitly as unnecessary overhead.
