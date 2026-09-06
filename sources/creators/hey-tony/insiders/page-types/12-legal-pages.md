# Legal pages

*Part of the HeyTony page-type research (`page-types/`). The rules every page inherits are in `00-rules-for-every-page.md`; the citation key, sources, and file map are in `README.md`.*

Covers privacy policy, terms and conditions, cookie policy, disclaimers, accessibility statements, and refund/return policies.

## What legal pages are for

- Terms and conditions plus a privacy policy in the footer "shows that you're a legitimate business... and that you care about people's privacy"; running Meta ads without one means "your ads won't get shown to as many people." [call 013]
- Google wants to see the pages exist ("here's the data we're going to collect... that legitimizes the business"); their absence "can hurt, definitely hurt your SEO." [call 043]
- Accessibility doubles as an SEO lever: proper heading hierarchy and alt text serve screen readers and search engines together, "the more accessible your site, the better it is for SEO." [call 002] [call 024]

## Index or noindex

- Noindexing is normal here: legal terms and service agreements "are just legal documents... there's really no sales value in it. It's for existing customers." [call 054]
- A privacy policy showing "not indexed" in Search Console is nothing to worry about; what matters is the homepage, money pages, and blog posts. [calls 058, 059]
- Live example: Jennifer had already noindexed her privacy policy and accessibility statement; missing meta descriptions there are "really non issues." [call 078]
- Robots.txt can keep pages like these out of the index, but "Just leave it alone" unless you know what you're doing. [book ch. 24]

## What goes on the page

- Use real text, not an iframe: Katie's privacy, terms, and cookie pages pulled from a third-party lawyer site and read as low word count; "copy the text from the third party and paste that text onto your website." [call 043]
- Draft with ChatGPT or Claude ("I need a privacy policy... tell me what I should include"), then confirm it's actually compliant, Matt is not a lawyer. [call 013] [call 043]
- Refund and shipping pages get compared directly against competitors by Google Merchant Center. [call 081]
- Aim the accessibility statement at a real WCAG level (A, AA, AAA). [call 002]
- Accessibility widgets are a paid shortcut: accessiBe runs roughly $300-400 a year, a comparable widget about $300 a year, cheaper or free WordPress options exist. [call 002]
- Contrast is testable: pure black (#000) and #191919 both pass on white, failures start in mid-tone grays, gold text fails on white but passes on black; text too small, or a page that can't zoom, excludes older and visually impaired users. [call 045] [call 002]

## Placement in the footer

- "Policies" belong in the footer, not the main nav. [call 058] [book ch. 9]
- Move non-essentials, including policies, into the footer or an About dropdown, keeping roughly 7-8 top-nav items max. [playbook IV]
- A footer holding only cookies, privacy policy, and contact is too thin for local SEO; legal pages are one part of the footer, not the whole footer. [call 081]

## Don'ts

- Don't iframe legal text, paste real text onto your own page instead. [call 043]
- Don't just pay ADA demand letters ($100,000-150,000): "unless you are a place of public accommodation that has 15 employees or more, most of those lawsuits don't apply to you"; Canada's threshold sits around 50-plus employees. [call 002]
- Don't let cookie-consent or privacy-center topics bleed into unrelated content, delete those headings when outlining from a competitor. [course: creating-a-blog-outline]

## Live examples

- Katie: privacy, terms, and cookie policy as iframes, fixed by pasting real text in. [call 043]
- Jennifer: privacy policy and accessibility statement both noindexed on purpose. [call 078]
- David, a legally blind Insider, runs an accessibility button on his own site and confirmed the community platform's contrast and screen-reader order were sound. [call 024] [calls 013, 017]
- HeyTony's own site audit flagged "button background and foreground colors do not have a sufficient contrast ratio" and "button name not accessible." [call 107]

## What Matt does not cover

- The curriculum, playbook, and book have nothing on writing privacy, terms, cookie, or disclaimer pages themselves, only placement, indexing, and adjacent nav/footer rules. [course: creating-a-blog-outline] [playbook III] [playbook IV] [book ch. 9] [book ch. 24]
- Not legal advice: Matt flags repeatedly that he is not a lawyer, and sends real legal disputes, like trademark misuse in a competitor's ad, straight to a lawyer. [call 043] [call 020]
- Site ownership is a site-level rule, not a legal-page rule: "If you paid for a website, you should own that website," hosted on your own server. [book ch. 25]

