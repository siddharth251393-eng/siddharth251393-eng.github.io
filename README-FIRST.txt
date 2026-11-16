INDUSTRYWIRE — PROJECT NOTES

PROJECT AND HOSTING
IndustryWire is in an audience-building phase, developing an independent business and industry newsroom. Paid B2B publishing of company announcements and market research report summaries is a long-term possibility, not a service currently open to customers. The code and repository remain on GitHub.

The current live site is https://siddharth251393-eng.github.io/ . Do not publish the commercial-service version to GitHub Pages. GitHub's published Pages limits say Pages is not intended or allowed as free hosting for an online business or a site primarily directed at facilitating commercial transactions: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

The IndustryWire name is provisional pending clearance. Preliminary research found an earlier exact mark associated with press-release distribution and other similar-name uses. Do not buy a matching domain, file a mark or launch under the name until checking the relevant trademark registers and marketplace use in intended countries.

Develop and review the commercial version in this repository first. Hosting choice and any paid hosting/domain purchase are deferred until the site and service model are ready. Before launch, choose a host whose terms permit a commercial site, update canonical URLs, social metadata, structured data, robots.txt, sitemap.xml and privacy wording, then review the production copy. Keep the current live website unchanged until a replacement is approved and ready.

BUSINESS MODEL — AUDIENCE-BUILDING PHASE
- Current focus is original newsroom coverage and reader trust. No paid publishing orders or subscriptions are being accepted now; monetisation is a long-term plan, not the current website call to action.
- Initial proposed service: review and possible clearly labelled publication of client-supplied company announcements and market research report summaries on IndustryWire.
- Intended buyers: company marketing and communications teams, PR agencies and market research publishers.
- Enquiries are reviewed individually. Availability, suitability, deliverable, permissions, fee and timing must be confirmed in writing before work begins.
- There is no active checkout, online payment, user account, content upload, fixed rate card, guaranteed turnaround or external syndication network.
- Do not claim third-party distribution, Google News inclusion, reach, traffic, leads, ranking, customers or testimonials unless independently established and approved for publication.
- Potential later products such as multi-item packages, directory listings, subscriptions or partner distribution are roadmap ideas only until they actually exist.
- If subscriptions are introduced, each subscriber needs a private dashboard showing articles purchased, submitted/uploaded, published and remaining, plus per-article review status. Enforce the purchased quota: a five-article plan must block a sixth submission/publication until renewal or top-up. Allow one customer-requested edit per published article, tied to that article and not transferable or poolable; five published articles provide five separate one-time edits, not five edits for one article. Then lock further customer edits on that article; editorial corrections and required legal changes remain separate. Decide how declined/withdrawn articles affect credits and define the edit scope before implementation. These are future requirements, not current features.
- PUBLISHING-TERMS-DRAFT.md records internal draft rules and a benchmark of Industry Today's public terms/distribution claims. It is not a customer-facing contract and must be adapted for IndustryWire by legal counsel before launch.
- Keep paid client material clearly labelled and separate from independent newsroom coverage. Payment does not buy favourable reporting or guarantee independent editorial coverage.
- Build readership with timely, original newsroom coverage across the chosen sectors and topics. Use trends as a lead signal, then add verified primary-source context or original analysis; do not copy competitors or present paid submissions as independent news.
- There is currently no reporting team. Never invent author identities, credentials, headshots or experience. Credit real writers accurately; use a clearly explained IndustryWire Editorial Desk organization byline for desk-produced work when appropriate. Create named author profiles only for real contributors who consent, and make page bylines match article structured data.
- Disclose sponsorship clearly; never disguise paid material as independent reporting. Qualify paid outbound links with `rel="sponsored"`.

PUBLISHER AND OWNERSHIP
- Kavita is the named publisher and is not the firm’s owner. Do not describe her as owner or assign ownership. The owner and legal publisher/operator structure remain unconfirmed; update public details only from confirmed facts.

CONTACT DETAILS
Change the public contact email in site-config.js. Contact links and the email draft form use that value. Review About, Contact, Corrections and Privacy after any change. The contact form prepares a draft in the visitor's mail app; it does not send or store the form on the site.

PUBLISHING ARTICLES
- Do not publish a newsroom story until facts and sources have been independently checked.
- The organizational byline profile is editorial-desk.html. It states plainly that the Editorial Desk is not an individual or staffed reporting team. Three sourced launch drafts are in drafts/: india-iip-september-2026.html, india-wpi-october-2026.html and india-steel-demand-april-october-2026.html. They are noindex and must not be treated as published. Re-check each against the latest source data and obtain human editorial review before use.
- Use article-template.html as a starting layout. It is marked noindex and must not be linked as a published article.
- Editorial demonstrations are listed under sampleArticles in articles.json and have individual noindex pages in sample-articles/. They are examples, not news; do not move them into the published articles array without fact-checking, assigning a real author and completing editorial review.
- Keep articles.json articles[] for published articles only. The newsroom page reads that array and does not surface the sampleArticles array.
- search.html is a noindex utility page. Keep the empty articles.html archive noindex and out of sitemap.xml until original newsroom reporting exists; then remove noindex and add the archive URL back.
- Give every article a permanent URL, a named responsible author, accurate original publication and update dates, working primary-source links, a self-referencing canonical URL and matching Article/NewsArticle data only when applicable.
- Add published article URLs to sitemap.xml.
- Keep news-sitemap.xml empty until the independent newsroom publishes eligible news. Do not add client-paid promotional pages. Include only URLs first published in the last two days and remove older entries; follow Google's current news sitemap rules.
- Do not represent concepts, paid client copy or sample text as independently verified reporting.
- Mark paid outbound links with `rel="sponsored"` in accordance with Google’s link guidance.

RESEARCH CATALOGUE
The listings on research.html are proposed scopes only, not completed reports or findings. Before accepting research work, agree the question, sources, geography, deliverables, timing, capability and commercial terms directly with the client. No subscription or checkout is active.

PRIVACY AND DATA
The site currently has no newsletter collection, analytics, user accounts, hosted form or payment system. Email enquiries are sent only if a visitor chooses to send the prepared draft from their own mail app. Review privacy.html and all hosting-provider terms before adding a form, analytics, newsletter, payment, file upload or account feature.

TECHNICAL FILES
- style.css — visual system and responsive layouts
- site.js — navigation, catalogue filtering, search, email draft and share controls
- site-config.js — public contact email
- robots.txt — crawl access and sitemap locations
- sitemap.xml — current public page URLs; update after final host and domain choice
- news-sitemap.xml — intentionally empty until real news coverage exists
- favicon.svg, social-card.svg and assets/ — IndustryWire visual assets

SEARCH AND NEWS
Search indexing and Google News inclusion are not guaranteed. Before launch on the final host, verify the site in Search Console, submit sitemap.xml, inspect article URLs and validate structured data against Google's current guidance.

PUBLISHER INFORMATION
IndustryWire is currently the publication and service name; legal publishing entity and registered business details have not been established on this website. Do not add unverified claims about company status, staff, audience, credentials, partners, circulation or years of operation. Review commercial terms, privacy practices and legal wording against the actual business and applicable requirements before accepting paid work.
