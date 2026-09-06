# Cross-page elements

*Part of the HeyTony page-type research (`page-types/`). The rules every page inherits are in `00-rules-for-every-page.md`; the citation key, sources, and file map are in `README.md`.*

## Header and navigation

- The nav is "the number one example of internal linking," HeyTony's own menu (Work, Services, Contact, Blog) each linking to that section; nav and footer links "send a strong signal to Google (and your visitors) about which pages are the most important," since they appear on every page. [course: internal-linking] [book ch. 9]
- Keep top-nav to roughly 7-8 items max; push non-essentials (store, careers, policies) to the footer or an About dropdown; contact must be in the nav; never hide the blog, "'Can we link to the blog but hide it so people can't find it?' If that's you, don't." [playbook IV] [call 058] [book ch. 27]

Crawl depth:
- A page in the nav is one click from the homepage; keep everything you want ranked within 3 clicks total; dropdown items don't add an extra click by themselves, "it's when you leave that page" that counts, but a hidden hamburger menu does. [course: crawl-depth] [call 022] [call 073] [call 097]
- Recovering an old ranking can be as simple as "put that page in your navigation menu." [call 071]

Design rules:
- Keep the header small, about one-sixth of the page, not half. [call 070] [playbook IV]
- The logo sits left or centered beside the nav, never shown twice, and never becomes the page's H1. [call 083] [playbook IV]
- Fit the nav on one line, nest overflow under an existing item rather than let it wrap. [call 070] [call 066]
- Design for mobile reality: 50-60% of traffic is mobile, and deep dropdowns don't work there, "I put everything on a page" instead. [call 073] [call 070]
- Menu labels should read as clear categories, not vague branding, "Nutrition" doesn't say what it is. [call 066]

Don'ts and live examples:
- Don't hide the nav behind a hamburger button on desktop, "it should just be shown"; don't let theme code inject stray heading tags into the header, creating duplicate H1s; don't add unfinished pages to the menu before they have content. [call 061] [call 070] [call 069] [call 032]
- Elliot's HTML pages used a differently colored menu per page, "this site looks like a different site." [call 010]

## Mega menus and drop-downs

- Purpose: keep core items visible, push the long tail (services or locations) into a dropdown or mega menu, each item still linking to its own page. [call 067] [playbook IV]
- Simplicity beats depth regardless of catalog size: "there's like five buttons. That's it... the more things that you have in your navigation menu, the less impact it has." [call 048]
- Locations pattern: a "Locations" dropdown lists cities, hovering one can reveal that city's service pages; Google can read content inside collapsed dropdown or detail elements. [call 068] [call 072]
- Test it like a real user: "ask somebody to go through it with you... like a mom or a grandparent... can you find this page." Don'ts: no three-level arrow-nested menus a first-time visitor can't follow, and no mega menu so dense it's unusable on mobile, "I want to see one drop down. You could have 10 on here." [call 048] [call 103]

## Footer

- Carries secondary-but-important pages (FAQs, policies, support pages, location-specific content), plus NAP (name, address, phone) and a link to the Google Business Profile via its CID link, "Google looks for that to determine if it's a local business." [book ch. 9] [call 052] [playbook V]
- Social profile links instead of an auto-updating embedded feed; location pages that don't fit the main nav can live in the footer. [call 042] [call 082]
- Mirror the top nav in the footer whenever the header nav isn't sticky, so the footer is never a dead end. [call 059] [playbook IV]
- Footer titles above menu columns must be H4 or smaller, or plain text, never H1/H2/H3. [call 125] [playbook IV]
- Footer links carry less crawl/authority weight than header or in-content links; footer text, like nav and sidebar text, doesn't count toward word count. [call 084] [course: low-word-count-how-to-fix]
- "Website design by / powered by" footer credit links work as an early-stage backlink tactic but are "not a long term solution"; if one client footer is responsible for more than about 100 backlinks (one real case ran 288,000-406,000, flagged as spam with only the homepage still indexed), remove your link, a sitewide footer credit reads as spam. [call 013] [call 095] [book ch. 16]
- A dark footer reads as a stable "end of the website" cue; use a static, linked map image, not a slow embedded interactive one; don't put an H1 in the footer, and don't reciprocal-link footer credits into an "incest hub." [call 028] [call 098] [call 040] [call 066] [call 004]

## Sidebars

- Common contents: a table of contents anchoring only H2/H3, a static CTA (phone, hours, shop link), a custom callout graphic. [call 030] [call 111] [call 008]
- A sticky sidebar table of contents (left quarter column) works well on long posts and beats one placed mid-post. [call 080] [call 054]
- In-content contextual links carry more weight than a sidebar "related posts" block, don't rely on a sidebar as your internal-linking strategy; sidebar text, like footer and nav text, is excluded from word-count measurement. [playbook III] [playbook IV] [call 124]
- The book is blunt about it: "Blog sidebar. Not very effective. People have developed banner blindness." [book ch. 46]
- Don't: rotating carousel content in a sidebar can render as H4 tags via the theme, breaking heading order. [call 086]

## Pop-ups and email capture

Placement, ranked, per the book's numbered list: blog sidebar (weak, "banner blindness"); in-content between paragraphs (works well if related to the post); a navigation menu tab (e.g., "New Owner Checklist"); exit-intent (most effective, appears bottom-left or bottom-right without blocking content, fires only when a visitor is about to leave). [book ch. 46]

- Timing beats offer: fire on exit intent or after a delay (about 30 seconds), never on page load, "unless I know who this is... I'm not signing up for anything"; a pop-up form is also a legitimate alternative to jump-links on a funnel page. [call 081] [call 124] [call 016]
- A pop-up's own heading tag creates a duplicate H1 even if it never opens, "if a person can see it all the time, Google can see it all the time"; restyle it down to plain paragraph text instead of removing it. [call 013] [call 096] [playbook III]
- Hidden pop-up text and review-widget copy inflate word-count tools invisibly, one plugin added roughly 2,000 identical hidden words per page. [call 095] [playbook II] [playbook III]
- Don't fire a newsletter pop-up immediately, it reads as aggressive; don't rely on a generic "Subscribe to Newsletter" widget, "that doesn't work anymore." [call 061] [book ch. 46]

## Chat widgets

- The sources say almost nothing about chat widgets specifically, most guidance folds them into general floating-UI rules; the closest concrete example is an accessibility widget "on the side of the screen" (accessiBe and similar). [playbook IV] [call 002]
- A floating mobile icon needs a text label ("call"), an icon alone isn't self-explanatory; a "let's chat" widget stacked with call/email links added to CTA confusion on a page with no clear primary action, treat it as one more competing CTA to prune. [call 054] [call 100]
- A slow-loading "checking your browser" interstitial "is going to be a bad signal to Google... because it's so slow," the same caution applies to any heavy chat-widget script. [call 001]

## Sticky bars and announcement/cookie bars

- Sticky bars carry an offer (a coupon percentage, a free-shipping threshold) and should stay static, not animated. [call 060]
- Book's rule, numeric: "Do NOT have both top and bottom sticky banners at once." [book ch. 46]
- Anchor a mobile phone-number bar at the bottom of the screen, not top-left, and make sure it's clickable. [call 054]
- A cookie or announcement bar, or a pop-up, adds hidden words that word-count tools, and Google, still count; cookie-consent/GDPR-style plugins can silently break page JavaScript, an "Accept all cookies" button did nothing on one site. [call 125] [call 064] [call 072]
- Don't let a cookie or announcement bar re-show on every visit or take over the screen on mobile, one owner's cookie consent pop-up was "too big... on the phone too"; don't stack a separate phone-number bar above the main header, "it almost looks broken"; don't let sticky bottom bars annoy visitors off the page, "God, these bars at the bottom piss me off so much. Get out of my way." [call 019] [call 049] [call 100] [call 066]

## Breadcrumbs

- Definition: "those little navigation trails you often see at the top of a page, just under the main menu... kind of like a GPS for your website." Example: "Products > Dog > Collars > Small Collars." SEO effect: "they also create a logical internal link structure that signals hierarchy and relevance to search engines." [book ch. 9]
- Rule: breadcrumbs must not carry heading tags, strip any H-tag to plain text. [playbook IV]
- Don't let breadcrumbs disappear on scroll: "you're hiding text on the page immediately. Google doesn't like that." [call 109]
- Live example: a custom post type kept its slug inside child URLs, functioning as "part of like the breadcrumb." [call 014]

## Search

- The sources say almost nothing about an on-site search feature; the one concrete mention is design-level, not structural: an invisible search icon on a low-contrast header bar was called out as "useless unless it's the right color." [call 103]
