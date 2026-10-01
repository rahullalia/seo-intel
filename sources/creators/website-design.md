# creators | website-design

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2026-09-27 | Removing the navigation bar doubled conversions on Yuppiechef's registry page
- Source: Edward Sturm, "How to Double Your Conversions by Doing Less (10 Before-and-After Examples)", 2026-09-27, https://edwardsturm.com/articles/conversion-rate-optimisation-strategy-simplify-landing-pages/
- Source: VWO, "A/B Testing Case Study: Removing Navigation Menu Increased Conversions By 100%", 2011-12-15, https://vwo.com/blog/a-b-testing-case-study-navigation-menu/
- Quote: "The conversion rate jumped from 3 to 6% with an effective 100% increase in conversions."
- Means: Sturm's 2026 roundup relays a test VWO published on 2011-12-15, on an online kitchen tools store's wedding registry page. A second test, Career Point's nursing enquiry page at 3.12 percent to 13.64 percent with 95.2 percent confidence, published by Unbounce on 2013-11-12, removed the primary navigation and moved the form above the fold in the same variation, so it does not isolate the navigation. Drop the navigation on a page whose only job is one action, and read both numbers as pre-mobile-era tests.
- Factor: landing-page-nav-removal | Evidence: C | Lever: conversion | Scope: organic | Stage: build

## 2026-09-27 | Cutting a contact form from eleven fields to four raised submissions 160 percent
- Source: Edward Sturm, "How to Double Your Conversions by Doing Less (10 Before-and-After Examples)", 2026-09-27, https://edwardsturm.com/articles/conversion-rate-optimisation-strategy-simplify-landing-pages/
- Source: Imaginary Landscape, Brian Moloney, "Fewer fields in a contact form sharply increases conversions", 2008-06, https://www.imagescape.com/media/filer_public/06/94/0694c7f4-8914-4598-8871-b857fbc12737/form_case_study.pdf
- Quote: "The test compared an 11-field Contact Us form with a 4-field Contact Us form. The more abbreviated form resulted in a 160% increase in submitted forms."
- Means: Sturm prints 12 fields and the case study he links says 11, and QA read that PDF at HTTP 200 on 2026-10-01 rather than the 404 the research run recorded. Imaginary Landscape counted thank-you page views in Google Analytics over two months for each form, its own 11-question form in late 2007 against the 4-question form that replaced it in April 2008, so cut a contact form to the fields you will use and read the number as one 2008 test on one site.
- Factor: form-field-count | Evidence: C | Lever: conversion | Scope: organic | Stage: build

## 2026-09-27 | Sturm's Highrise signup figure does not match the number the original test published
- Source: Edward Sturm, "How to Double Your Conversions by Doing Less (10 Before-and-After Examples)", 2026-09-27, https://edwardsturm.com/articles/conversion-rate-optimisation-strategy-simplify-landing-pages/
- Source: Signal v. Noise, Jamis Buck and Noah Lorang, "Behind the scenes: A/B testing part 3: Finale", 2011, https://signalvnoise.com/posts/2991-behind-the-scenes-ab-testing-part-3-final
- Quote: "Highrise CRM replaced their busy homepage with a simple page built around one happy customer."
- Means: Sturm prints a 102.5 percent rise in paid signups. The 37signals post he links reports "a 47% percent increase in paid signups" for the Person Page against the Long Form design in its own text, and 102.5 percent appears there only inside images and a reader comment dated 25 Aug 11. The claim is not verifiable at the primary as Sturm states it, so the row keeps grade D.
- Factor: single-primary-cta | Evidence: D | Lever: conversion | Scope: organic | Stage: build

## 2026-07 | An auto-rotating hero carousel costs load time and hides its own H1
- Source: HeyTony master playbook, Part III 3.4 and Part IV Conversion elements, 2026-07 (skills/skills/heyTony/reference/part-3-onpage-and-money-pages.md), local file
- Quote: "A carousel that freezes on hover hid a page's own H1 from most visitors; every load still fetches every slide's image."
- Means: Replace a rotating hero with one static image and persistent descriptive text, so the H1 is always rendered and only one image loads.
- Factor: hero-carousel | Evidence: D | Lever: conversion | Scope: organic | Stage: build

## 2026-07 | One primary call to action per page, secondary actions receding
- Source: HeyTony master playbook, Part III 3.4, 2026-07 (skills/skills/heyTony/reference/part-3-onpage-and-money-pages.md), local file
- Quote: "If people have too many choices, they sometimes just choose not to make any choice."
- Means: One solid high-contrast CTA per page; a second action gets an outline or neutral treatment so it does not compete.
- Factor: single-primary-cta | Evidence: D | Lever: conversion | Scope: organic | Stage: build

## 2026-07 | A phone number must be visible and tappable, not an icon
- Source: HeyTony master playbook, Part IV Mobile and responsive design, 2026-07 (skills/skills/heyTony/reference/part-4-technical-and-internal-linking.md), local file
- Quote: "One profile's icon-only floating button (no visible clickable number) tanked call conversions."
- Means: Put a labelled clickable number near the bottom of the mobile screen where a thumb reaches it, and check every page renders it.
- Factor: tap-to-call | Evidence: D | Lever: conversion | Scope: local organic | Stage: both

## 2026-07 | Real team photos build more trust than stock or AI images
- Source: HeyTony master playbook, Part IV Trust signals, 2026-07 (skills/skills/heyTony/reference/part-4-technical-and-internal-linking.md), local file
- Quote: "Real photos of the actual team build more trust than stock or AI. Screenshots read as more authentic than over-polished imagery."
- Means: Use real photography on any page meant to show a real team, and prefer a plain screenshot over polished stock.
- Factor: real-team-photos | Evidence: D | Lever: trust | Scope: organic | Stage: build

## 2026-07 | A review carousel plugin adds markup and gets scrolled past
- Source: HeyTony master playbook, Part V 3 Reviews and Reputation, 2026-07 (skills/skills/heyTony/reference/part-5-offpage-and-ai-search.md), local file
- Quote: "one added ~1,000 words of markup per page (hurting load time) and users scroll past carousels rather than clicking through"
- Means: Hand-paste two or three real reviews as plain text on each money page instead of running a carousel widget.
- Factor: review-carousel-plugin | Evidence: D | Lever: conversion | Scope: organic | Stage: both

## 2026-07-16 | Accessibility and SEO share the same fixes
- Source: HeyTony email, 2026-07-16 (insiders/page-types/heytony-email-tips.md), local file
- Quote: "Good SEO is build on the exact same foundations as accessibility."
- Means: Real headings, live text, alt text and contrast serve a screen reader and Google's crawler with one fix, so they are not separate work.
- Factor: accessibility-baseline | Evidence: D | Lever: trust | Scope: organic | Stage: both

## 2026-07-08 | Body text never below sixteen pixels
- Source: HeyTony Insiders, call 008, 2026-07 (insiders/page-types/00-rules-for-every-page.md, citing transcripts/008_web-design-for-seo-08-07-2026.txt), local file
- Quote: "Body text never smaller than 16 pixels, roughly 1.8 line height; headings step down clearly in size."
- Means: The working range is 16 to 20 pixels. Font size is the one value allowed to shrink on mobile; spacing and margins stay generous.
- Factor: body-font-size | Evidence: D | Lever: conversion | Scope: organic | Stage: build

## 2026-05-13 | Pure black text on pure white reads as vibrating
- Source: HeyTony Insiders, call 045, 2026-05 (insiders/page-types/00-rules-for-every-page.md, citing transcripts/045_web-design-for-seo-13-05-2026.txt), local file
- Quote: "Never pure black on pure white; it reads as 'vibrating.' Use a soft dark gray on near-white instead."
- Means: Set body text to a soft dark gray on a near-white ground rather than #000 on #fff.
- Factor: text-contrast | Evidence: D | Lever: conversion | Scope: organic | Stage: build

## 2026-04-15 | Whitespace is the empty space around elements, and too little is a negative
- Source: HeyTony Insiders, call 055, 2026-04 (insiders/page-types/00-rules-for-every-page.md, citing transcripts/055_web-design-for-seo-with-leanne-15-04-2026.txt), local file
- Quote: "White space doesn't mean just white, it just means the empty space around objects and assets."
- Means: Give each section consistent top and bottom padding and alternate the layout rhythm so each section reads as one idea.
- Factor: whitespace-section-rhythm | Evidence: D | Lever: conversion | Scope: organic | Stage: build
