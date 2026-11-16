INDUSTRYWIRE — SITE NOTES

PROJECT
IndustryWire is a static, zero-cost business and industry publication concept hosted on GitHub Pages. The site uses the existing IndustryWire identity, HTML, CSS and JavaScript. No build system, paid service, analytics, newsletter backend, database or payment processor is required.

LIVE SITE
https://siddharth251393-eng.github.io/

EDITING CONTACT DETAILS
Change the public contact email in site-config.js. Contact links and the email draft form use that value. Review the About, Contact, Corrections and Privacy pages after any change.

PUBLISHING ARTICLES
- Do not publish a story until its facts and sources have been independently checked.
- Use article-template.html as a starting layout. It is marked noindex and must not be linked as an article.
- Editorial demonstrations are listed under sampleArticles in articles.json and have individual noindex pages in sample-articles/. They are examples, not news; do not move them into the published articles array without fact-checking, assigning a real author and completing editorial review.
- Keep articles.json articles[] for published articles only. The newsroom page reads that array and does not surface the sampleArticles array.
- Give every article a permanent URL, a named responsible author, accurate original publication and update dates, working primary-source links, a self-referencing canonical URL and matching Article/NewsArticle data only when applicable.
- Add published article URLs to sitemap.xml.
- Keep news-sitemap.xml empty until real news is published. Then include only news URLs first published in the last two days and remove older entries; follow Google’s current news sitemap rules.
- Do not represent concepts, press releases or sample text as independently verified reporting.

RESEARCH CATALOGUE
The listings on research.html are proposed scopes only, not completed reports or findings. Before accepting paid work, agree the question, sources, geographic coverage, deliverables, timing and commercial terms directly with the client. There is no checkout or subscription system.

CONTACT AND DATA
The contact form prepares an email draft in the visitor’s own mail app. It does not send or store the form. The site has no newsletter collection, analytics or account system. Update privacy.html if those practices change.

SEARCH AND ACCESSIBILITY
Search, category filters, mobile navigation, article-share controls and the contact draft are implemented in site.js. Keep keyboard access, clear labels and responsive behavior when changing the pages.

TECHNICAL FILES
- style.css — visual system and responsive layouts
- site.js — navigation, catalogue filtering, search, email draft and share controls
- site-config.js — public contact email
- robots.txt — crawl access and sitemap locations
- sitemap.xml — current public page URLs
- news-sitemap.xml — intentionally empty until real news coverage exists
- favicon.svg and social-card.svg — IndustryWire brand assets

GOOGLE SEARCH AND NEWS
Google may crawl public pages, but indexing, visibility and Google News inclusion are not guaranteed. Verify the site in Search Console, submit sitemap.xml, inspect article URLs and validate structured data after publishing. Google News sitemap guidance: https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap

EDITORIAL AND PUBLISHER DETAILS
IndustryWire is currently the publication name; legal publishing entity details have not been established on this site. Do not add unverified claims about company status, staff, audience, circulation, credentials or years of operation. Review legal and privacy wording against the actual business and applicable requirements before relying on it as formal advice.
