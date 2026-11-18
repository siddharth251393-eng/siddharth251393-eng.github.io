# The Sector Journal

**Business & Industry News** — an independent industry newsroom in development, with an India and Asia perspective. Paid publishing is a long-term plan, not an active offer.

Live site: <https://siddharth251393-eng.github.io/>

The existing GitHub repository is retained as the source-code location; its repository slug and the connected Netlify branch name are technical identifiers, not the publication brand. The public preview is hosted at https://dashing-frangipane-55897f.netlify.app/ from `industrywire-netlify-preview`. The GitHub Pages copy is a separate older deployment. No custom domain or paid hosting has been purchased. Read [README-FIRST.txt](README-FIRST.txt) before editing or publishing content.

The current phase is audience-building: original independent newsroom coverage and reader trust come first. Paid publishing and subscriptions are long-term plans, not services currently open to customers. The site has no checkout, payment, upload, fixed pricing, promised turnaround or external syndication network. Any future paid client publishing must remain separate from independent newsroom coverage. See [BUSINESS-MODEL.md](BUSINESS-MODEL.md) for the working offer, delivery flow and launch gates.

Google Analytics 4 and Microsoft Clarity IDs are configured in Netlify, and both tags load only after a visitor opts in through the consent panel. The Netlify site uses its free `netlify.app` address while the custom domain decision is pending. Check the deployed robots and canonical settings before any domain migration.

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

Unpublished drafts remain excluded from the public build. Local source changes are published to Netlify when the connected branch successfully builds. Serve this folder with any static HTTP server to inspect source changes locally.

## Production hosting

GitHub remains the source-code repository. The current local copy still uses `https://siddharth251393-eng.github.io/` in its canonicals and sitemaps. When the name is cleared and a production host/domain is chosen, update those references and verify the final domain before launch. See [BUYING-STAGE.md](BUYING-STAGE.md) and [SITE-AUDIT-REPORT.md](SITE-AUDIT-REPORT.md).
