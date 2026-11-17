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
- Before using any third-party figures, data series, tables, charts, maps, images, text or other material, check the exact source/item's rights, copyright notice, dataset licence and reuse conditions globally for the intended use and distribution markets (including commercial use, adaptations, attribution and non-endorsement). Consider where the material was created/published, the rights holder and applicable licence, and where IndustryWire will publish, operate and target readers; do not assume Indian rules alone apply. Record the source, retrieval/publication date, intended use/markets, licence or permission basis, required credit and caveats. “Publicly accessible” does not by itself mean reusable. PIB's policy permits reuse of its own website material with prominent credit and accurate, non-misleading presentation, but excludes third-party material; the Government Open Data License–India applies only to eligible datasets actually made available under that licence and has attribution and other conditions. These are source-specific examples, not global clearance. If cross-border rights or terms are unclear, do not reproduce the material until an appropriately licensed source is found, permission is obtained, or qualified advice resolves the issue. Reporting independently verified facts with attribution is distinct from copying another publisher's wording, table, chart or image.
- The organizational byline profile is editorial-desk.html. It states plainly that the Editorial Desk is not an individual or staffed reporting team. Four unpublished drafts are in drafts/: revised IIP, WPI and ACC tender stories, plus an earlier steel-data draft. They are noindex and must not be treated as published. Re-check every story against the latest sources and obtain human editorial review before use; do not publish the steel draft without a fresh currency check.
- Use article-template.html as a starting layout. It is marked noindex and must not be linked as a published article.
- Editorial demonstrations are listed under sampleArticles in articles.json and have individual noindex pages in sample-articles/. They are examples, not news; do not move them into the published articles array without fact-checking, assigning a real author and completing editorial review.
- Keep articles.json articles[] for published articles only. The newsroom page reads that array and does not surface the sampleArticles array.
- The production build now has an explicit article release gate. Store a reviewed article page under stories/ and add its matching metadata record to articles.json only after editorial approval. Required fields are status ("published"), title, url, file, summary, section, author, authorType (Person or Organization), authorUrl, published (visible publication-date string) and datePublished (ISO 8601 with timezone); dateModified is optional. The build checks the story file, exact visible h1, author page, visible byline/date and metadata. Unlisted files under stories/ are never copied to the public build.
- Story files and article records are emitted only when PUBLIC_INDEXING=true. The current Netlify build keeps this false, so the live preview remains noindex and its article feed and sitemaps stay empty. Do not change this setting until the permanent domain, public facts and launch checks are ready.
- On an indexable production build, the site generates matching NewsArticle structured data, adds the newsroom and article URLs to sitemap.xml, and adds only stories published in the prior 48 hours to news-sitemap.xml. Article dates must be accurate ISO 8601 timestamps with a timezone; visible byline and date must match the article record.
- search.html is a noindex utility page. Keep the empty articles.html archive noindex and out of sitemap.xml until original newsroom reporting exists; then remove noindex and add the archive URL back.
- Give every article a permanent URL, a truthful responsible byline (a real consenting person or the clearly explained Editorial Desk), accurate original publication and update dates, working primary-source links, a self-referencing canonical URL and matching Article/NewsArticle data only when applicable.
- The production build adds reviewed story URLs and the newsroom archive to sitemap.xml; do not manually add draft URLs.
- Keep news-sitemap.xml empty until the independent newsroom publishes eligible news. Do not add client-paid promotional pages. Include only URLs first published in the last two days and remove older entries; follow Google's current news sitemap rules.
- Do not represent concepts, paid client copy or sample text as independently verified reporting.
- Visual standard for IndustryWire data graphics: retain the established deep navy (#102333), blue-teal (#176B87), bright teal (#52B4BD / #72C6C8), and sparing warm-gold accent (#F2BE62), with white and muted-blue text for contrast. Use Manrope for display headings and DM Sans for site body copy; in standalone SVG artwork, use a reliable sans-serif fallback and keep labels legible at mobile thumbnail size. Prefer original, topic-specific vector illustrations (such as a battery for a battery-industry story) and a clear visual sequence that explains what changed, the strongest supported driver or contrast, what remains uncertain, and what readers should watch next. Keep each graphic focused on a few verified facts, with accurate units, geography and time period. Every chart or data graphic must have a visible note directly beneath it naming the source and release/data date, explaining units and comparison basis, and carrying any material caveat (for example provisional data, estimates, or limits on interpretation); include a descriptive alt text and link the citation in the article. Never imply a causal link, forecast, scale, endorsement or reporting access the evidence does not support; do not reuse another publisher's graphic.
- Mark paid outbound links with `rel="sponsored"` in accordance with Google’s link guidance.

RESEARCH CATALOGUE
The listings on research.html are proposed scopes only, not completed reports or findings. Before accepting research work, agree the question, sources, geography, deliverables, timing, capability and commercial terms directly with the client. No subscription or checkout is active.

PRIVACY AND DATA
The site currently has no newsletter collection, active analytics IDs, user accounts, hosted form or payment system. Email enquiries are sent only if a visitor chooses to send the prepared draft from their own mail app. The build supports optional Google Analytics and Microsoft Clarity IDs, but loads those tags only after visitor consent. Set `GA_MEASUREMENT_ID` and/or `CLARITY_PROJECT_ID` in Netlify only after the relevant account setup is complete. Review privacy.html and all provider terms before enabling measurement.

TECHNICAL FILES
- style.css — visual system and responsive layouts
- site.js — navigation, catalogue filtering, search, email draft and share controls
- site-config.js — public contact email
- privacy-consent.js — optional analytics consent controls and tag loading
- robots.txt — crawl access and sitemap locations
- sitemap.xml — current public page URLs; update after final host and domain choice
- news-sitemap.xml — intentionally empty until real news coverage exists
- favicon.svg, social-card.svg and assets/ — IndustryWire visual assets

SEARCH AND NEWS
Search indexing and Google News inclusion are not guaranteed. Before launch on the final host, verify the site in Search Console, submit sitemap.xml, inspect article URLs and validate structured data against Google's current guidance.

PUBLISHER INFORMATION
IndustryWire is currently the publication and service name; legal publishing entity and registered business details have not been established on this website. Do not add unverified claims about company status, staff, audience, credentials, partners, circulation or years of operation. Review commercial terms, privacy practices and legal wording against the actual business and applicable requirements before accepting paid work.
