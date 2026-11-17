# IndustryWire

**Business & Industry News** — an independent industry newsroom in development, with an India and Asia perspective. Paid publishing is a long-term plan, not an active offer.

Live site: <https://siddharth251393-eng.github.io/>

The code remains in GitHub. The existing GitHub Pages site is unchanged; the separate public Netlify preview is connected to this repository at https://dashing-frangipane-55897f.netlify.app/ and intentionally remains noindex. Netlify's connected production branch is `industrywire-netlify-preview`. GitHub's [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) say Pages is not intended or allowed as free hosting for an online business or a site primarily directed at facilitating commercial transactions. No custom domain or paid hosting has been purchased. The latest changes in the local checkout are uncommitted and are not on the public preview. Read [README-FIRST.txt](README-FIRST.txt) before editing or publishing content.

The current phase is audience-building: original independent newsroom coverage and reader trust come first. Paid publishing and subscriptions are long-term plans, not services currently open to customers. The site has no checkout, payment, upload, fixed pricing, promised turnaround or external syndication network. Any future paid client publishing must remain separate from independent newsroom coverage. See [BUSINESS-MODEL.md](BUSINESS-MODEL.md) for the working offer, delivery flow and launch gates.

Google Analytics 4 and Microsoft Clarity IDs are configured in Netlify, and both tags load only after a visitor opts in through the consent panel. The Netlify preview remains noindex. Do not enable public indexing before the final domain and launch checks are complete.

## Pages

- Homepage and five sector pages
- Research concept catalogue with search and category filters
- Future publishing model page (not currently available)
- Newsroom archive, currently empty until verified reporting is ready
- About, Contact, Editorial Policy, Corrections, Privacy and Terms
- Search page and reusable noindex article layout
- Ten source-linked editorial demonstrations, marked as samples and excluded from the newsroom feed and sitemap
- Four source-linked, unpublished story drafts in `drafts/` (IIP, WPI and ACC tender drafts recently revised; WPI now has three original graphics; the older steel-data draft still needs a currency check), plus publisher and Editorial Desk profiles
- A guarded article release workflow: reviewed story pages live under `stories/`; the production build validates the visible headline, byline and date, generates NewsArticle data, and updates both sitemaps. The current Netlify preview has public indexing disabled, so it remains noindex and does not expose story files or article data.
- An RSS 2.0 feed at `/rss.xml` is generated at build time from explicitly published stories only. It contains linked summaries, never draft or sample articles, and is empty on noindex builds. Page headers advertise the feed to compatible readers.
- Custom `404.html`, site audit and pre-purchase hosting/domain handoff

## Local preview

The latest local build succeeded with `PUBLIC_INDEXING=false`; it generated 33 deployment entries for the noindex Netlify origin. Unpublished drafts remain excluded from the public build. Recent source, article and graphic changes are still uncommitted and have not been deployed. Serve this folder with any static HTTP server to inspect the source locally.

## Production hosting

GitHub remains the source-code repository. The current local copy still uses `https://siddharth251393-eng.github.io/` in its canonicals and sitemaps. When the name is cleared and a production host/domain is chosen, update those references and verify the final domain before launch. See [BUYING-STAGE.md](BUYING-STAGE.md) and [SITE-AUDIT-REPORT.md](SITE-AUDIT-REPORT.md).
