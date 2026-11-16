# IndustryWire site audit and launch status

**Audit date:** 16 November 2026
**Scope:** Public GitHub Pages site, local working copy, navigation, mobile-related layout rules, crawl files, metadata, structured data, business/publisher information and first editorial workflow.
**Live site:** https://siddharth251393-eng.github.io/
**Repository:** https://github.com/siddharth251393-eng/siddharth251393-eng.github.io

## Summary

### Follow-up audit and Netlify preview launch — 16 November 2026

- Rechecked the live GitHub Pages site: homepage, `robots.txt`, both sitemaps, and all 14 regular sitemap URLs responded with HTTP 200. The live news sitemap has zero article entries, appropriately, and `/publishing.html` still returns 404 because this newer page is only in the local working copy.
- Built and deployed the Netlify preview at https://dashing-frangipane-55897f.netlify.app/ using Netlify Drop. The 18 content pages now use self-canonicals on that exact origin and `noindex,nofollow`; the 404 page has `noindex` but no canonical. Because this is a noindex preview, its regular sitemap is empty and `robots.txt` does not advertise a sitemap. A separate production-style build produced 16 self-canonical, indexable sitemap URLs and an empty news sitemap. All internal file and fragment links resolve; all JSON-LD and XML parse; no GitHub-host origin remains in either build.
- The Netlify output excludes the unpublished `drafts/` directory, sample-article pages, sample story records, and reusable article template. The public story feed remains empty. No fabricated news, author credentials, company identity, audience figures, or paid-service availability is included in the preview.
- Updated `privacy.html` to describe host-processed technical request data and link to the applicable GitHub Pages and Netlify privacy notices. The site still has no analytics, ad pixels, newsletter backend, account system, or server-side contact form.
- Verified the public Netlify deploy after making the project public with the owner's approval. All 16 main page routes returned HTTP 200, had self-canonicals on the assigned Netlify origin, and carried `noindex,nofollow`. Both XML sitemaps returned HTTP 200 and parsed; both contain no entries in the preview. `robots.txt` allows crawling so search engines can see the noindex directive.
- Verified the URL-prefix property `https://dashing-frangipane-55897f.netlify.app/` in Google Search Console with an HTML meta tag. The property is new and its reports are still processing. No sitemap was submitted and no indexing request was made because this is a noindex preview.
- Tested the mobile navigation on the narrow browser viewport: the menu opens and exposes the expected navigation links. A full device-size and text-zoom accessibility sweep remains outstanding.
- Connected the Netlify project to the IndustryWire GitHub repository and deployed commit `79b6b7f` from the dedicated `industrywire-netlify-preview` production branch. Netlify confirms the repository link, build command (`python3 scripts/build_site.py`), publish folder (`dist`), active build status, and production branch. GitHub `main` and the existing GitHub Pages site remain unchanged.

The public GitHub Pages site remains unchanged. The Netlify preview is a separate, public, noindex deployment.

The live homepage, sitemap URLs and same-site links checked responded successfully. The live site uses consistent self-referencing canonicals on the sampled pages, exposes `robots.txt`, and has an intentionally empty news sitemap because it has no original newsroom articles yet. Its homepage and sampled information pages contain Organization and BreadcrumbList structured data. No published article exists to validate as `NewsArticle`.

The local working copy now presents IndustryWire as an audience-building newsroom, keeps paid publishing closed, explains its future publishing model, and includes Kavita’s publisher profile, a transparent organizational byline profile and three sourced, unpublished launch article drafts. Ten enquiry links in the working copy had spaces in their query strings; these have been encoded. A local audit of 34 HTML pages found no missing internal files or fragment targets, malformed JSON-LD, or sitemap entries pointing to missing/noindex pages. A branded `404.html` is also prepared but excluded from the sitemap.

**The Netlify preview is live and Git-connected; GitHub Pages is unchanged.** The production Netlify site now deploys from the public `industrywire-netlify-preview` branch. Commit `79b6b7f` built successfully in about 15 seconds. Future pushes to that production branch will trigger Netlify builds; branch deploys are limited to that production branch. The existing `main` branch was not changed. No custom domain was purchased; the preview uses a free `netlify.app` address. GitHub Pages' current published limits say the free service is not intended for use to run an online business or a site primarily facilitating commercial transactions or commercial SaaS. IndustryWire's stated longer-term purpose is a paid publishing business. No custom domain was purchased; the Netlify preview uses a free `netlify.app` address.

## Findings and recommended corrections

| Priority | Finding | Recommended correction / status | Files or accounts |
|---|---|---|---|
| **P2 — Netlify route aliases** | Clean paths such as `/about` and file paths such as `/about.html` both return HTTP 200. Canonicals consistently select the `.html` URL, but the alternate clean path remains a duplicate response. The preview is noindex, so this does not currently expose duplicate pages to search. | Before enabling indexing, choose one URL style and redirect the alternate form to it. Keep internal links, sitemap entries, and canonicals consistent. | `netlify.toml`; `scripts/build_site.py`; HTML canonical/link templates |
| **P1 — Before naming/launch** | “IndustryWire” is not legally cleared. Earlier preliminary research found an exact/similar name concern in a related publishing/distribution area. This is not a complete international clearance search. | Treat the name as provisional. Search national and regional registers plus marketplace use in intended countries and related classes; obtain qualified trademark advice before filing, domain purchase or commercial launch. A database search alone is not legal clearance. | `README-FIRST.txt`; `BUSINESS-MODEL.md`; brand assets/metadata in all HTML files, `favicon.svg`, `social-card.svg` if a replacement name is needed |
| **P1 — Before publication** | No genuine newsroom article is published. The live newsroom/archive therefore has no article record to demonstrate original reporting or byline practices. | Publish only after human editing and independent source verification. The new IIP explainer is an unpublished draft, noindex and not in the sitemap. Re-check it against current data before use; do not pass it off as a fresh update if superseded. | `drafts/india-iip-september-2026.html`; `articles.json`; `articles.html`; `sitemap.xml`; `news-sitemap.xml` |
| **P1 — Before public launch** | India is the planned operating country; Kavita is the named publisher, not the owner. The owner and legal entity/registration details are not confirmed on the site. No formal reporting team is claimed. | Use “IndustryWire” as the publication title and keep Kavita identified as publisher, not owner. Identify the owner and legal entity only when confirmed; do not conflate ownership, publisher and company/operator roles. Ask India-qualified counsel to confirm applicable digital-news requirements. MIB’s published Rule 18 information format separates title and entity name and requests contact/grievance information; check the current process and applicability. Do not invent company or staff claims. | `about.html`; `contact.html`; `privacy.html`; `terms.html`; `site-config.js`; future legal publisher/grievance details |
| **P1 — Before accepting money/data** | There is no checkout, account system, customer dashboard, upload workflow or distribution network. Future privacy, credit and customer-edit terms remain unimplemented. | Keep paid orders closed. Before launch, implement the per-customer quota and per-article one-edit rules, define declined/withdrawn-credit treatment, security/retention, refunds and privacy; test the actual payment and publishing flow. | `BUSINESS-MODEL.md`; `PUBLISHING-TERMS-DRAFT.md`; `publishing.html`; `privacy.html`; future dashboard/backend |
| **P2 — Before first article is indexed** | The live site has Organization and BreadcrumbList JSON-LD, but no article exists and therefore no Article/NewsArticle markup is demonstrated. Article structured data is helpful but is not a Google News inclusion requirement. | On each real story, match visible headline/byline/date with Article or NewsArticle JSON-LD, a self-canonical URL and a working author/profile URL. Add only after facts and images/rights are checked. Never add placeholder/fabricated author identities. | `article-template.html`; future article HTML; `editorial-desk.html`; `articles.json` |
| **P2 — Search/News monitoring** | The Netlify preview property is verified in Search Console, but its reports are processing. The preview remains noindex and both sitemaps are empty. | Before final launch, add/verify the confirmed custom-domain property, remove noindex, build production sitemaps from real pages and eligible original stories, then submit the regular sitemap. Keep the news sitemap empty until eligible news is published; then include only the newest two days. Search/News visibility is not guaranteed. | `news-sitemap.xml`; `sitemap.xml`; `robots.txt`; `scripts/build_site.py`; Google Search Console |
| **P2 — Responsive QA** | Responsive CSS includes a collapsed mobile menu at 800px, a single-column layout at 520px, 44px minimum interactive controls and reduced-motion handling. The Netlify homepage and opened mobile menu were visually reviewed in a narrow browser viewport; a full range of device widths and text zoom was not checked. | Complete the remaining screen-width, keyboard, contrast and text-zoom checks before a custom-domain launch. | `style.css`; `site.js`; all page templates |
| **P3 — Local link correction completed** | Ten research enquiry links in the local working copy contained unescaped spaces in the `topic` query parameter. | Encoded spaces as `%20`. The local internal-link audit now reports no missing files/fragments. | `research.html` |

## Live-site checks

- Homepage, `robots.txt`, `sitemap.xml` and `news-sitemap.xml`: HTTP 200.
- 14 URLs listed in the live sitemap: all returned HTTP 200 during this check.
- Same-site URLs discovered from the live sitemap pages: 28 unique URLs checked; no broken same-site responses found.
- Sampled live page canonical URLs are self-referencing and point to the current `github.io` origin.
- Sampled live pages expose Organization and BreadcrumbList JSON-LD. There is no live Article/NewsArticle page to inspect.
- `robots.txt` allows crawling and points to both sitemaps.
- The news sitemap contains no news entries; appropriate until eligible original newsroom content exists.
- The current GitHub Pages homepage's visible title is “IndustryWire | Business & Industry Intelligence”; the new newsroom-first version is live on the separate Netlify preview.
- The local `publishing.html` is present but not on the live site (live URL returned 404 on 16 November). The local navigation should only be deployed together with that page.

## Working-copy changes made in this task

- Added `editorial-desk.html`, an accurate profile for a desk byline, and `publisher.html` naming Kavita as publisher without inventing credentials or assigning her story authorship. The desk profile says the byline does not represent a staffed team.
- Added three source-linked, noindex drafts: `drafts/india-iip-september-2026.html`, `drafts/india-wpi-october-2026.html` and `drafts/india-steel-demand-april-october-2026.html`. They are not listed as published stories and need latest-data checks and a human editor's review before release.
- Updated `article-template.html` to link author/byline information and call for original context.
- Linked the transparent byline explanation from `about.html`.
- Added the byline page to `sitemap.xml`; kept all unpublished drafts and `404.html` out of the sitemap and news sitemap.
- Fixed the ten malformed query links in `research.html`.
- Documented the workflow in `README-FIRST.txt`.
- Confirmed that the local sitemap parses and local JSON-LD parses across the audited pages.

## Five-step completion status

1. **Newsroom workflow:** Prepared locally. Transparent Editorial Desk profile; no invented individual authors. Human verification remains required for each story.
2. **Original launch content:** One sourced explainer draft prepared, explicitly unpublished/noindex. It requires fact-check and human editorial approval.
3. **Site and SEO review:** Live and local checks completed as described above. Mobile CSS reviewed; visual device QA remains outstanding.
4. **Launch details:** IndustryWire remains the preferred working name and the user-provided editorial contact is configured. Brand clearance, owner identity and legal publisher/entity structure remain unresolved; Kavita is the named publisher, not owner.
5. **Publish and measure:** The noindex preview is deployed on Netlify at https://dashing-frangipane-55897f.netlify.app/ and verified as a URL-prefix property in Search Console. The project is Git-connected to the IndustryWire repository and successfully deployed from `industrywire-netlify-preview` (commit `79b6b7f`); `main` and GitHub Pages remain unchanged. No custom domain was bought or production indexing enabled. Keep this preview noindex until the publication name, legal owner/operator and launch domain are confirmed.

## Primary references

- [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
- [Google Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article)
- [Google News sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap)
- [Google Article structured data guidance](https://developers.google.com/search/docs/appearance/structured-data/article)
- [Netlify privacy statement](https://www.netlify.com/privacy/)
- [Google helpful, reliable, people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [USPTO: comprehensive trademark clearance search](https://www.uspto.gov/trademarks/search/comprehensive-clearance-search-similar-trademarks)
- [WIPO Global Brand Database](https://www.wipo.int/en/web/global-brand-database/index)
- [India MIB digital media rules and guidance](https://mib.gov.in/en/ministry/our-wings/digital-media)
- [MIB digital-news publisher information format](https://mib.gov.in/sites/default/files/2025-06/furnishing-of-informaiton-30.05.2025_0.pdf)
