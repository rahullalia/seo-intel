# Blog Post Templates Using Elementor in WordPress — 18.12.2025 (Leanne Jones, Leanne Digital Design)

## Tactics & step-by-step how-to
- Platform choice: use whatever CMS you're already comfortable with (WordPress, Squarespace, Wix) — the design principles below transfer, only the execution UI changes. Don't platform-hop chasing what others use; consistency beats novelty.
- Blog roll (index page) needs an organized layout — a grid/feed, optional sidebar with categories, and/or featured-posts-at-top + roll-below + category filter. Hey Tony's pattern: 2 featured posts at top, category filter, rest of the roll below — "that's really all you need."
- Individual blog post anatomy: hero/header section (title + featured image), then body content. Include title, author, date, featured image. Disable comments sitewide (spam). Show categories for UX/navigation.
- Content layout options for the body: (a) sidebar-left + content-right, (b) single long column, (c) content-left + sidebar-right. Hey Tony's uses sidebar-left/content-right; Leanne's own site does the same.
- Break body copy into shorter paragraphs + bullet points + H2 section breaks — never one dense wall of text.
- Building a custom single-post template in Elementor, step by step:
  1. Theme Builder → Single Post → Add New (or start from a pre-built template) → build from a blank canvas.
  2. Add a Container for the hero/header section; give it a background color if needed so white nav text stays visible.
  3. For a 2-column hero (image + title side by side): add a container, duplicate it, then set the parent container's "direction" so the two columns sit side by side instead of stacking.
  4. Drag in the Title widget (dynamic — pulls the post title automatically) and the Featured Image widget.
  5. Add author/date/read-time via the "Post Info" widget, OR drag a plain Text Editor widget and use Dynamic Tags to pull specific fields (e.g. author name) — the same dynamic-tag approach also works applied to a Heading widget.
  6. Style the H1 size, fix line-height (see Rules), then add top/bottom padding in em units to stop cramped spacing, unlinking the padding control so top/bottom can differ from left/right.
  7. Resize the featured-image column vs. the title column to match the proportions of the reference site.
  8. Below the hero, add a second container for the body: duplicate it → set direction → the narrow column becomes the sidebar, the wider one holds content.
  9. Drag the "Post Content" widget into the content column — this auto-pulls whatever text/images were written in the WordPress back-end editor for that post; no manual linking needed.
  10. Drag the "Table of Contents" widget into the sidebar; set it to anchor only H2 and H3 tags (skip H4–H6); switch the numbered list to bullets, then remove the bullets entirely for a cleaner look if desired.
  11. Sidebar can also hold static (non-dynamic) content — e.g. a Text Editor widget with a bolded "Call me today" + phone number, or business hours — it isn't limited to the table of contents.
  12. Apply a subtle background color to the whole content+sidebar container to visually separate it from the hero, then a separate (e.g. white) background specifically behind the content area; use margin (not padding), unlinked to top-only, to push the body section away from the hero.
  13. Publish → set Display Conditions → Include → "Posts" (all posts) to roll the template out sitewide. If another single-post template is already active, Elementor throws a conflict error — go to the OLD template in Theme Builder, open Display Conditions, remove/X-out its condition, Save and Close; only then does the new template take over. New templates apply retroactively to every existing post, not just future ones.
  14. To revert: go back to Theme Builder → Single Posts → re-enable the old template's display condition (apply to all posts) and disable/delete the new one.
- Two distinct ways to build/edit an individual post: (a) write and edit purely in the WordPress back-end editor (post uses whichever template is assigned, no per-post layout control), or (b) open the post in Elementor for more layout freedom — but Elementor's per-post edit view only lets you touch that post's content container, not the shared template chrome. A separate "Edit single blog post" button from within that view jumps you into editing the TEMPLATE itself (which then affects every post).
- Content-authoring workflow Leanne actually uses: write the post in a Word document → copy/paste into the standard WordPress back-end post editor (where images also get uploaded) → the template's "Post Content" widget then displays that content automatically wherever it's placed.
- Building the blog-roll/archive template (separate from the single-post template): Elementor → "Edit Post Archives." Drag in the "Archive Post" widget to pull the grid of post previews automatically. Adjust column count (tested 5 = "very busy," settled on 4 or 2). Add author name to each preview card via Dynamic Tags → metadata → Author. Style → Content → Title: reduce the default (oversized) font size and reset line-height to match font-size as a starting point, then adjust. Add a background color to each card so previews look grouped/separated instead of blending together. Adjust spacing between posts under layout settings. Fix blurry featured-image thumbnails via the Image Resolution setting.
- Excerpts: toggle the excerpt on/off and set a fixed word-count limit in the archive widget settings. For posts where the auto-excerpt reads awkwardly, write a bespoke excerpt per post using the "Edit excerpt" field inside the WordPress post editor, sized to the right word count.
- Turn on Pagination once the blog has many posts (200-post example given) so the roll doesn't load every single post at once.
- Images: source free stock from Pexels or paid from Adobe Stock; prefer real/original photos over stock when feasible for authenticity.

## Rules / dos & don'ts (keep every threshold, number, specific)
- Featured image aspect ratio: 16:9 as the rule-of-thumb size for WordPress (exact ratio depends on the template). Hey Tony's uses a square featured image; Leanne uses a rectangle — both are valid, just be consistent.
- Body font size: ~16px as a baseline rule of thumb. Don't go bigger than necessary (oversized body text "looks a little bit childish"); don't go below ~10px (too hard on the eyes). Leanne's own site: 18px body. Hey Tony's: 20px body.
- Heading scale (Leanne's own site, general rule of thumb): H1 = 48px, H2 = 36px, H3 = 26px. Hierarchy exists so the H1 always reads as the most important element on the page.
- Separately, in the live demo cloning Hey Tony's actual template: their H1 (title) = 72px, their "key summary" heading = H2 at 48px. Leanne matched her demo H1 to 72px to copy that specific site, not as a universal rule.
- Line-height method: start the line-height value equal to the font-size number (e.g. font-size 72 → start line-height at 72), then adjust down/up visually from there until letters stop touching.
- Padding vs. margin: padding = space inside a container; margin = space that pushes the container away from what's outside it. Use em units for padding/spacing — scales better for mobile ("like the difference between inches and centimeters").
- Specific padding values used in the builds: hero title padding started at 2em top/bottom (too tight) → increased to 6em top/bottom. Second template's hero container: 4em top/bottom. Table-of-contents sidebar block: 2em top, 2em bottom.
- Body copy fonts: keep simple — sans-serif works for "99% of all websites." Named picks: Inter, Open Sans. Headline fonts can be more decorative/interesting since the text is bigger and shorter, so readability cost is low.
- Font choice affects sizing: serif fonts often need to run bigger than sans-serif because there's "more action happening with the letters," so they need more surrounding white space.
- Disable comments on every blog post, on every website — "generally it's just spam."
- Table of Contents: anchor by H2 and H3 only; skip H4/H5/H6 ("we generally don't go that deep for writing our blog posts").
- Images per post: at least 4 images per post as a minimum, adjusted for post length; ideal target is one image per H2 section if budget allows.
- Stock photo sourcing: stick to a small, consistent set of sources (Pexels + Adobe Stock only) so licensing can always be proven if challenged.
- Archive/blog-roll title styling example: font-size 22px with line-height set to 22px as the starting point, then adjusted visually.
- Excerpt word-count example given: 50 words.
- Image resolution for archive thumbnails: pick the smallest resolution setting that doesn't look blurry — Medium was the chosen sweet spot in the demo; Large looked "really crisp" but loads 1000×1000px images (heavier).
- Column counts for a blog-roll grid: 5 columns read as "very busy"; 4 or 2 columns were the adjusted options.
- Pagination threshold example: worth turning on once a blog has around 200 posts, so the roll doesn't load every post at once.
- Squarespace can still rank fine for SEO even if the site doesn't run especially fast, as long as the rest of standard SEO practice is followed.

## Tools, prompts & resources (exact prompt wording if quoted; tool names; settings)
- **Elementor** (Theme Builder) — core tool for the whole demo. Widgets/features used: Container (with direction control for column layout), Title, Featured Image, Post Info (author/date/read-time), Text Editor + Dynamic Tags (alternate way to pull author name or other post metadata), Post Content (pulls the WP back-end post body automatically), Table of Contents (H2/H3 anchor setting, numbered-vs-bullet list style), Author Box (pulls the profile picture from the WordPress Users section), Archive Post (pulls the grid of post previews for the blog-roll/archive template), Display Conditions (assigns a template to "Posts"/all posts; also where conflicting templates get disabled).
- **WordPress back end** — where posts are actually written/pasted and images uploaded; has an "Edit excerpt" field for writing bespoke per-post excerpts; Users section holds each author's profile picture (source for the Author Box widget).
- **Font Ninja** — browser tool Leanne uses to identify fonts on any live website (used live to confirm fonts on Hey Tony's site: body read as Open Sans-adjacent, headline read as "Comba Sans" — likely an imprecise transcription of the actual font name).
- **Pexels** — free stock photo source, used "all the time."
- **Adobe Stock** — paid stock photo source; the only two stock sources Leanne uses.
- **Word** (Microsoft Word) — where Leanne drafts blog posts before copy/pasting into the WordPress back end.
- No AI prompts (ChatGPT, etc.) were used or quoted on this call — it's a pure Elementor UI/design walkthrough.

## Case studies / examples / results (names, niches, numbers)
- **Hey Tony's website** — used throughout as the primary template being reverse-engineered live: 2 featured posts + category filter on the blog roll; sidebar-left/content-right single-post layout; square featured image; body font 20px; H1 = 72px, "key summary" H2 = 48px.
- **Leanne's own site (Leanne Digital Design)** — used as the secondary comparison: rectangle featured image; body font 18px, Open Sans; heading scale H1 48 / H2 36 / H3 26.
- No client case studies, traffic numbers, or ranking results were discussed on this call — it's a live software/design tutorial, not a performance review.
- **Ash** (attendee) — reported creating a template and setting it to apply to all posts, but posts weren't picking it up; Leanne couldn't diagnose remotely and asked Ash to follow up 1:1 after the call.
- **Damian** (attendee) — flagged that title/excerpt text is hard to keep matched/consistent-looking across preview cards on the blog roll; Leanne's fix: write bespoke per-post excerpts at a consistent word count via the "Edit excerpt" field, rather than relying on auto-truncation.
- **Felicia** (attendee) — repeatedly asked how the post content "gets" from Word into the Elementor template; Leanne walked through the full chain (Word → WordPress back-end editor → Post Content widget auto-pulls it) more than once to clarify — a useful signal of where beginners get lost on this workflow.
- A copyright claim was filed against one of Leanne's sites over a stock photo; she was able to close the claim by producing the license because she deliberately limits herself to provable sources (Pexels/Adobe Stock) — cited as the reason for not mixing in random stock sites.

## Notable verbatim quotes (only memorable/strategic ones)
- "I think it can be tempting to be like, ooh, they're using that. So I'm going to jump over to that platform. But really, I think the most important thing is just to be consistent on your own platform and whatever you're comfortable with."
- "The goal for creating the template is to design it once and then you can just copy and paste your content into your text editor and not have to style it every single time. It just, it's a great time saver."
- "So the padding goes within the container and margin pushes things away from the container."
- "If your font size is too big, it makes your website look a little bit childish."
- On ems: "It's flexible so it scales better for mobile devices... it's kind of like the difference between using inches and centimeters."
- On the excerpt word-count setting not updating live: "Sometimes I find this doesn't listen to me until after I hit save. And then I look at it on the front end... it makes me into a liar. That's what it does."
- "Using real pictures is definitely the way to go. It makes you look more authentic and real."
- "You want it to be as small as possible for the image resolution without it looking blurry."
- On table-of-contents SEO value: "I don't know if the table and contents actually improves SEO. It is useful for user experience so that could result in better SEO. But I don't have the exact stats for that."

## Tradeoffs & nuance
- Editing a post via the WordPress back end alone is simpler and respects the shared template, but gives zero per-post layout freedom; editing via Elementor per-post gives layout freedom on that single post's content area, at the cost of it being easy to blur the line between "editing this post" and "editing the shared template" (a separate button, "Edit single blog post," is the only way to jump into changing the template itself — mixing these up would silently change every post's layout).
- Image resolution is a quality-vs-speed tradeoff: Large thumbnails look "really crisp" but weigh in at 1000×1000px per image; Medium was chosen as the balance point where it still "looks pretty good" without the extra load.
- Real/original photography is preferred for authenticity, but cost and availability push most site owners toward stock; Leanne's workaround narrows the tradeoff by limiting herself to just two provable-license sources (Pexels, Adobe Stock) rather than avoiding stock altogether.
- Font size is a balancing act, not a single number: too small strains the eyes, too large reads as childish, and the "right" size also shifts by font choice (serif needs more room than sans-serif) — so the 16px/18px/20px figures given are starting points, not hard rules.
- Table of Contents is promoted for user experience, with Leanne explicitly declining to overclaim an SEO benefit she can't back with data — UX improvement "could" help SEO indirectly, but that's a hypothesis, not a stat.
- Squarespace's typical speed disadvantage doesn't have to block rankings — the tradeoff is absorbed elsewhere (following the rest of standard on-page SEO), not by switching platforms.
- Retroactive template changes are powerful but binary: turning on Display Conditions → "all posts" instantly reskins every historical post at once (not a preview-and-approve flow per post), and a conflicting active template blocks the change entirely until the old one's condition is manually cleared.
