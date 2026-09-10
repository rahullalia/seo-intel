# experts | website-design

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2026-05-11 | WCAG 2.2 sets a 24 by 24 CSS pixel floor for every tap target
- Source: W3C, "Understanding Success Criterion 2.5.8: Target Size (Minimum)", 2026-05-11, https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Quote: "The size of the target for pointer inputs is at least 24 by 24 CSS pixels, except when:"
- Means: A tap-to-call phone number link is a pointer target like any other, so it must clear 24 by 24 CSS pixels unless an exception applies. This is the compliance floor the standard sets, not a measurement of how target size changes call volume.
- Factor: tap-to-call | Evidence: A | Lever: trust | Scope: organic | Stage: build

## 2025-04-03 | Baymard testing found users leave the hero carousel before it finishes rotating
- Source: Baymard Institute, "10 UX Requirements to Follow for a User-Friendly Homepage Carousel Design", 2025-04-03, https://baymard.com/blog/homepage-carousel
- Quote: "During testing, users typically clicked or tapped to another page or scrolled past the carousel long before a full rotation of the slides had been executed."
- Means: Baymard reports 33 percent of top US and European ecommerce desktop sites carry a homepage carousel and 46 percent of desktop and mobile carousels have usability issues, so anything on slide two or later is seen by few visitors. Put the offer and the primary action in the first slide or in a static hero, and repeat carousel content elsewhere on the page. Page shows published 2019-04-30 and updated 2025-04-03.
- Factor: hero-carousel | Evidence: B | Lever: conversion | Scope: organic | Stage: build

## 2024-12-12 | WCAG 2.2 sets the minimum text contrast ratio at 4.5 to 1
- Source: W3C, "Web Content Accessibility Guidelines (WCAG) 2.2", 2024-12-12, https://www.w3.org/TR/WCAG22/
- Quote: "The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except for the following:"
- Means: Success Criterion 1.4.3 Contrast (Minimum) is Level AA and names 4.5:1 for body text, with exceptions for large text, incidental text and logotypes. Soft gray body text on a near white background passes only when the measured ratio clears 4.5:1, so check the pair with a contrast tool rather than by eye. This is the W3C Recommendation text, not a study.
- Factor: text-contrast | Evidence: B | Lever: conversion | Scope: organic | Stage: build
