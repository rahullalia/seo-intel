# Technical SEO with Elliot Part 2 — 21.05.2026 (Call #039)

Format: live Q&A, raise-hand queue, live screen-share audits/tool demos. Presenter: Elliot (not Denroy this session). Duration 34m22s (~5882 words); call restarted mid-session after Zoom/tech issues, so an earlier segment (sign-language-interpreter/Orange County keyword example) was referenced but not fully replayed.

## Tactics & step-by-step how-to

- **Manual schema markup, step by step:**
  1. Google "schema markup generator" (any generator works — pick by how user-friendly the interface is; Elliot found Google's own older built-in schema tool less user-friendly than third-party generators).
  2. Pick the content category (e.g., Product, Article/Blog).
  3. For a **product**: fill in name (e.g., "black boots"), image URL, brand (e.g., "Nike"), product description (use the target keyword here), price, price currency, lowest value.
  4. For an **article/blog**: fill in type (blog/news/article), URL, headline, image URL, short description (can reuse the meta description or a variant — include the keyword here too).
  5. The tool auto-generates the script/JSON-LD on the right-hand side as you fill fields.
  6. Copy that script.
  7. In WordPress, paste it into the **header** section — for Rank Math, this is a dropdown menu in the blog/page editor. Same placement rule applies to both blog posts and standard web pages: always the header, never elsewhere.
- **Why header placement matters:** the header loads before the rest of the page, so when Google crawls a page it reads the header script first. Same underlying mechanism as installing a custom analytics tracking script.
- **No native header field in your WordPress theme:** use Yoast SEO's header field, or search for a "header extension" plugin to add one.
- **Diagnosing a "page not accessible" flag from an audit tool:** copy the flagged URL, paste it into Google Search Console's URL Inspection search bar (top of GSC), and check the result. Green ticks / indexed status = the page is genuinely fine and the audit tool itself is throwing a false positive — no action needed. If the tool keeps misfiring, flag it up (Elliot said she'd note it for Matt/the dev team to investigate).
- **Defending an established domain against a bigger, name-confusable competitor** (without changing your URL):
  1. Keep the existing domain — don't reset years of accumulated history.
  2. Build backlinks from **local, high-authority sources** — city hall, town chamber of commerce/business center — rather than trying to out-brand a national competitor.
  3. Deepen blog content: pick niche, specific topics and add real depth/richness rather than broad coverage.
  4. Target **long-tail, highly specific keywords** (service + specific qualifying question/scenario) rather than generic head terms, anticipating Google's more AI-driven search direction.
  5. Build hyperlocal content (location pages) as a complementary channel.
- **Validating a location/hyperlocal page before building it:** check keyword search volume for that specific city/county + service term (via GSC or a keyword tool) before committing content. Build only if there's real search demand behind that specific location.
- **Deciding location-page scope:** base the go/no-go decision on actual keyword-volume data, not gut feeling and not blind AI advice — "make the decision not necessarily based on what Claude's saying, but on just what the actual data points are."
- **Internal linking from location pages to service pages:** only link the services genuinely relevant/tailored to that specific area's content (e.g., flat tires and boat/water-damage repair for a lake town) — don't force every service into every location page. It's fine if different location pages link to different subsets of services, as long as there's some crossover/internal linking overall. Prefer working links naturally into body copy over dumping them as a generic "related links" block at the end (acceptable only as a fallback, "if there's really no other alternative").
- **Using AI as an E-A-T self-audit tool:** after editing site content, paste/describe it to Claude or ChatGPT and ask for a grade on each E-A-T category plus specific suggestions to improve it. Endorsed as "a healthy way" to prep content for Google's increasingly AI-driven evaluation.
- **CID link placement:** wrap a CID link (see Tools section) around natural anchor text whenever the business mentions itself — e.g., a phrase combining business name + service + city — on blog posts, service pages, or anywhere it fits naturally on the website.
- **Google Business Profile maintenance routine (used internally at HeyTony, twice/week cadence):**
  1. Post an update roughly twice a week.
  2. Content doesn't need to be promotional — a simple summary of what's on offer that week works (e.g., "Mondays we have functional flow, Tuesdays we have coffee hour before yoga").
  3. Can be AI-drafted; keep it roughly tweet-length.
  4. Include a link at the bottom (book now / learn more).
  5. Also include the business's CID link at the bottom of the post.
  6. Purpose is primarily to signal to Google/Search Console that the profile is actively maintained — customers seeing the post is a secondary benefit.

## Rules / dos & don'ts

- Schema script goes in the page **header**, always — same rule for blog posts and web pages, no exceptions shown.
- If Rank Math is supposedly generating schema but a site-analysis/audit tool still reports "no schema markup," manual JSON-LD paste is a legitimate workaround/supplement — don't assume the plugin alone guarantees the tool will detect it.
- Always cross-reference a "page not accessible" audit-tool warning against GSC's URL Inspection before taking any remedial action. Green ticks in GSC = no real problem, it's a tool-side error.
- Do **not** change an established domain/brand name just because a bigger, better-funded competitor has a similar name and is winning the "did you mean...?" SERP prompt — preserve the accumulated domain authority (7 years of history, since 2019, in this case) instead of resetting to zero.
- Do **not** blanket-build location pages for every possible city/county just because you technically can. Google can read over-broad, unsubstantiated local claims as gaming the system — explicit example: "if you live in Nashville, you can't say you're a local lender to Chattanooga."
- Location-page build threshold (illustrative ratio given): a county with ~500 population where roughly **85%** of that population's search volume is behind the target service+location term = viable to build. No meaningful search volume behind the term = skip it, it's "a waste of space on your site."
- Don't force every service page to link from every location page. Partial coverage (half, or even a quarter, of total services linked per page) is fine as long as links are relevant to that area and there's some overall crossover between pages.
- Avoid a plain "related links" dump at the bottom of a page as the default linking strategy — integrate links throughout the body copy instead; use the bottom-dump only when there's genuinely no better alternative.
- Target GBP posting cadence (HeyTony's own practice, offered as a benchmark): **twice a week**.
- Per Elliot's read of Google's own recent search console update: Google's direction is shifting more AI-focused going forward — prioritize very specific, tightly concentrated long-tail keywords (service + niche modifier + specific city/county) over broad head terms.

## Tools, prompts & resources

- **"Schema markup generator"** — the generic search term Elliot used to find a demo tool live on the call. Any similar generator is fine; choose based on UI friendliness. Elliot noted Google's own older built-in schema tool felt less user-friendly by comparison.
- Schema generator fields demoed — **Product**: name, image URL, brand, description (keyword), price, price currency, lowest value. **Article/Blog**: type, URL, headline, image URL, short description (keyword).
- **Rank Math** (WordPress plugin) — header/script insertion via a dropdown menu in the blog/page editor, used to paste the generated schema script.
- **Yoast SEO** — alternative for adding a header field/section on themes that lack one natively; also does its own automatic schema markup.
- **Google Search Console — URL Inspection tool** (search bar at the top of GSC) — paste any URL to check index/accessibility status; green ticks = page is fine.
- **CID link** — Google's unique identifier link for a Business Profile; described as carrying extra authority/weight because it links directly to the verified profile. Use in anchor text (business + service + city phrasing) and at the bottom of GBP posts.
- **Claude / ChatGPT** — (a) used by an attendee (Chris) to self-grade his own page content for E-A-T and get specific improvement suggestions after edits; (b) used by another attendee (Christopher) to sanity-check a county-expansion strategy for location pages — Claude advised against blanket coverage of every county.
- Upcoming resource: Denroy and Elliot are tag-teaming a combined **Google Analytics + Google Search Console** walkthrough video, expected "by next week at the earliest" from this call's date.

## Case studies / examples / results

- **Varuna** — multi-client WordPress agency work using Rank Math (and Yoast SEO for some clients). Rank Math's own schema markup wasn't showing up in her site-analysis tool, prompting the full manual-schema walkthrough above.
- **Catherine** — HeyTony's own site audit tool flagged "page not accessible" errors on pages she hadn't touched: **9 pages** one week, jumping to **42** on the next crawl. Cross-checked via GSC URL Inspection — all green ticks — confirmed as a tool-side false positive, not a real site issue. Elliot flagged it for escalation to Matt/dev if the pattern continues.
- **Jennifer** — asked about adding a header section when it's not native to her WordPress setup; pointed to Yoast SEO or a "header extension" plugin search.
- **Christopher / Valor Mortgage** — domain "Valor Mortgage" registered since 2019 (~7 years of history); a similarly-named, venture-capital-backed **national chain** ("Valon"/"Valen" per the transcript) started the same year and now out-ranks him on brand searches — Google prompts "did you mean Valon/Valen?" ahead of his own site. He's a one-man show competing against a national player. Already wrote location content for all **11 cities** in his home county; considering expanding across all counties in Tennessee (**94 total**) but Claude advised against blanket coverage, suggesting focus on strong/surrounding counties instead. Also building (in progress, not yet live) a content format: a short video answering a specific question at the top of each blog post, an AI-written article body, an FAQ section at the bottom, and a quick text summary snippet under the video.
- **David Jones** — auto repair shop, Central Texas. Building ~10 location pages for towns within a 25–30 mile radius, each written hyperlocally (local neighborhoods, streets, lakes, parks, region-specific issues like boat/lake damage or Texas-heat-related car problems). Homepage lists 36 total services across separate pages. Asked whether all 10 location pages should link to all 36 services — advised no; link only the subset relevant to that town's actual context, cross-linking internally where it naturally fits rather than forcing full coverage everywhere.
- **Regina** — confirmed CID links can and should be placed across the website; example anchor pattern given: "[business] advertising/SEO agency [city]" wrapping through to the Business Profile.
- **Chris** — routinely asks Claude/ChatGPT to grade his own site content on E-A-T after making changes and to suggest improvements; Elliot endorsed the practice as aligned with where Google is heading.
- **Mario** — Pilates studio Google Business Profile audit (reviewed live via Google Maps). Good review volume and quality already in place. Advised: post more frequently (twice/week benchmark), add a CID link plus a book-now/learn-more link at the bottom of every post. Business opened in **January** (very new), which explains why Google Maps Street View shows no exterior signage yet.

## Notable verbatim quotes

- "You're always going to put the script in the header of the page regardless... when Google goes through and crawls it, it's going to read the script, it's going to read what's in the header first before the rest."
- On the Valor/Valon naming conflict: "I would encourage you to if possible look into backlinks... backlinks locally that are from high authority places like city hall or like a town center, those would be structurally really great for you to move forward with."
- "It would not be great, like you'd be starting from kind of basics again if you were to change your URL. So I wouldn't recommend that, but I would focus on trying to increase your domain authority."
- On over-expanding location pages: "If you live in Nashville, you can't say you're a local lender to Chattanooga."
- On the location-page viability threshold: "If there's a county that maybe has population like 500... if the volume on that is like, let's say it's like 85%... then it would be viable to make that location page."
- "Make the decision not necessarily based on what Claude's saying, but on just what the actual data points are to see if it's actually viable for you and your business."
- On service-linking scope: "You don't have to do all of them. It really is just tailored to that specific area."
- On CID links: "This is the unique identifier that Google gives to your website... it carries a little more authority and a little more weight."
- On AI + E-A-T: "You can never go wrong by even just going through your content to just make sure it E-A-Ts."
- On Google's AI-driven direction: "Keeping it very specific to that area is going to have the best way to keep your business up to date and also keep it relevant for when Google crawls that and starts serving up information."
- On the purpose of GBP posts: "Most often than not this update portion is more so for search console or like Google search as a whole rather than customers actually seeing this... it shows Google that you're continually updating and monitoring your business profile."

## Tradeoffs & nuance

- **Rebrand vs. defend:** even against a much larger, better-funded, name-confusable national competitor, Elliot's call is to never sacrifice years of accumulated domain history — compete via local backlinks and content depth instead of a name/URL reset, accepting a slower, indirect path rather than a clean break.
- **Location-page expansion is data-gated, not ambition-gated:** the identical tactic (a page per county/city) is good practice for one attendee and bad practice ("trying to work the system") for another — the only stated differentiator is verified keyword search volume behind that specific location term. There's no blanket rule ("do all 11" or "do all 94") independent of that check.
- **AI as advisor, not decision-maker:** Claude is used both as a strategy sanity-check (county expansion) and as a self-audit tool (E-A-T grading), but Elliot is explicit the final call should rest on actual keyword/search data, not the AI's suggestion alone.
- **Linking completeness vs. relevance:** trying to cross-link every service to every location page dilutes hyperlocal specificity; partial, contextually relevant linking (even a subset of total services per page) is preferred over exhaustive coverage, so long as some crossover exists site-wide.
- **GBP posting is a Google-facing signal first, marketing second:** framed as worth doing consistently mainly because it demonstrates active profile management to Google/Search Console — real customers reading the posts is a secondary, lesser benefit, not the primary justification.
- **Bottom-of-page "related links" blocks** are acceptable only as a fallback when no natural in-body placement exists — naturally integrated links are the preferred default.
