# Testimonials and reviews pages

*Part of the HeyTony page-type research (`page-types/`). The rules every page inherits are in `00-rules-for-every-page.md`; the citation key, sources, and file map are in `README.md`.*

## What it is for and what it targets

- Reviews build trust and conversion, and feed local map-pack ranking: review velocity, roughly one a week, can outpace a competitor sitting on a bigger lifetime total [call 052; playbook V 3, VI 3.4].
- A dedicated reviews page is optional, not the main event: "I like to include testimonials where it's relevant... on the homepage... on specific service pages... you can have a page just for reviews if you want, but I also like to sprinkle reviews all over the website" [call 016].
- Matt's own reviews page doesn't rank for "hey tony reviews" (the results are dominated by social posts, Trustpilot, Reddit, Google reviews, and BBB), yet he still keeps the page on the main site [call 001].
- Reviews shape AI picks too: ChatGPT favored the highest-rated Boston towing companies over the most-reviewed ones, and a 2.2-star company still ranked in Google Maps with no website [call 109].

## What goes on it, top to bottom (the structure)

- Reviews belong on every money page, not funneled onto one reviews page: 2 to 3 real reviews per page, pasted as plain text [call 021; playbook III 3.4, V 3].
- On the homepage, testimonials sit as their own section, after the services/products overview and before FAQs [call 028; course: word count].
- Heading should name the service or city, e.g. "Kind words our customers say in Fort Myers," or "Reviews of the Yellowstone Day tour"; the quote itself must never carry a heading tag, plain paragraph text only [calls 070, 097, 014].
- A "featured in" line with press or media logos can follow a press release, without linking the logos out [call 012].

## Layout and design

- Hero social proof: five gold star icons plus "rated five stars on Google," linked to the real Google review URL, kept as the one prominent placement rather than competing with the main quote/call CTA [calls 036, 060].
- Trust badges directly under the hero: the 5-star rating plus chamber or association logos, with Yelp, Trustpilot, or BIA badges on service pages [calls 055, 061].
- A testimonial section doesn't need photos if it already has visual interest (the Google logo and stars); icons work when clients don't want their photo shown [call 100].
- Show one testimonial section, not two: keep it once and higher, or give it a button through to more [calls 049, 060].

## Visuals

- Four formats: a live Google reviews widget, copy-pasted text, video testimonials, and screenshots, which "feel really real... especially now with a lot of things being vibe coded" [call 016].
- Screenshots build human trust, but Google likely isn't reading text baked into an image; embed or paste the actual text if you want it picked up by search or AI [call 077].
- Never a review carousel or a live plugin: one carousel added roughly 1,000 words of markup per page, a Google Reviews plugin inflated pages by 3,000 to 4,000 duplicated words, and a widget pulling 80 to 90 reviews inflated a service page to 6,500 words; visitors want "maybe three reviews," then a link to see more [calls 021, 032, 074].
- Upload the actual photos you took for a client alongside their testimonial into the Google Business Profile review itself [call 011].

## Length, keyword density, and on-page SEO

- Pasted review text counts toward a page's word count and SEO; a live review widget adds no extra trust signal beyond whatever text is actually visible [playbook IV Conversion elements].
- Keep product reviews on the page even if they skew keyword density, "that's social proof... that'll help you sell more" [call 116].
- The same review text repeated verbatim on every page reads as duplicate content; rotate which 2 to 3 reviews appear where, and keep location-specific testimonials on the matching location page only [calls 021, 032, 096].
- Adding testimonials to an already-ranking page doesn't move its ranking either way; review schema needs a third-party generator, Yoast's default markup doesn't add it [calls 035, 072].

## CTAs and conversion

- Always link a testimonial back to its real source, Google, Yelp, or wherever it actually lives: "that tells Google, that tells people that okay, this is legit... I can go into ChatGPT, generate an image, generate a review, and slap it on my website with a fake name" [call 103].
- Pair the visible reviews with a "read more reviews" button pointing at the full profile, rather than dumping every review onto the page [calls 021, 086].
- Reviews placed right under the hero "add some impact for reducing friction" toward buying [call 100].

## Links, indexing, and where it sits in the site

- Every displayed review links to its real source; connect the website to the actual Google profile rather than just quoting it [call 086].
- The reviews micro-site tactic, explicitly gray-hat, "not white hat SEO": register a separate root domain like yourbusinessnamereviews.com, fill it with real review text rather than screenshots, and link to it once from an already-indexed blog post on the main site, never the reverse. Build it cheap with Claude Code from dumped review screenshots, "shouldn't take more than a couple hours," hosted on Railway or Netlify; grab the domain early, and never connect or verify it in Search Console [calls 001, 032; playbook V 7.6, VI 1.6].
- Never host a press release itself on your own site, that's linking to something that's linking back to you, promote its reviews via social posts instead [call 031].

## Don'ts

- Don't review-gate with an NPS or 1-to-5 screener before sending the real Google review link, "Google wants you to send everybody a link to your Google business profile" [call 003].
- Don't incentivize a review, let a customer name staff in it, ask only happy customers, solicit one while someone is still at your business, or ask for a specific review or product mention, Google's own policy bans all five [email 2026-04-16].
- Don't run review trains or reciprocal review swaps, they read as gaming the system and get removed [call 071].
- Don't repeat the same testimonial section twice on one page, or repeat identical review text across many pages [calls 049, 096].
- Don't fake a review with an AI-generated name and image [call 103].

## From the calls: live examples

- Marisa's reviews micro-site (marisabrusilloreviews.com) lists every review, including non-Google ones, as plain text on a deliberately generic page with no menu and no branding, built to read like an independent third party wrote it [call 021].
- A client's page audit turned up 3,000 to 4,000 extra words purely from a duplicated Google Reviews plugin; removing the section and comparing word count against competitors, 500 versus 3,000, was the fix [call 032].
- A press release opened with "a five-star average across 111 Google reviews," hyperlinking "111 Google reviews" straight to the GBP CID link [call 031].

## Where the sources are thin or disagree

- The reviews micro-site tactic is explicitly unresolved: a working, low-cost bet with no seen downside in one framing, unproven and disputed by other SEOs in another, "it is to manipulate the search results, which they don't want you to do" [call 001; playbook V 7.6, VI 1.6].
- "Featured in" press logos get two different treatments: "you could say featured in and then post the logos, but I wouldn't link to them" in one call [call 012], while a competitor's featured-in logos were themselves linked out as external links in another [call 034].
- The official solicitation rules flatly ban incentivizing a review, yet a QR code offering "10% off next time" for leaving one appears approvingly in the same source material, a real gray area rather than a resolved rule [email 2026-04-16; call 071].
