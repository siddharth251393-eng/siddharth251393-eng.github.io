# IndustryWire: launch and domain handoff

**Status:** The static newsroom foundation and a public Netlify preview are prepared. The Netlify project is connected to GitHub and the preview is deliberately noindex. No custom domain or paid hosting has been purchased. The latest article, graphics, accessibility and editorial-note changes are local and uncommitted; they are not visible on the public preview yet.

## What is ready

- Mobile-responsive static newsroom website with the current IndustryWire branding and editorial/publisher information pages.
- GitHub remains the source-code repository. Netlify builds the connected `industrywire-netlify-preview` branch at [the public preview](https://dashing-frangipane-55897f.netlify.app/).
- `netlify.toml` and `scripts/build_site.py` support a noindex preview and a separate production build with canonicals, structured data, robots and sitemaps derived from the configured site origin.
- Article release gate for reviewed story pages and metadata; drafts and sample articles are excluded from the public feed and sitemaps.
- The working copy has four unpublished drafts. Three were recently revised; the WPI story has a set of three original SVG graphics. All require final human editorial review before publication. The older steel-data draft needs a fresh currency check.
- Kavita is identified as publisher, not owner. The owner/legal entity details are still unconfirmed and must not be invented.
- The Netlify preview URL-prefix property was verified in Google Search Console. Because the preview is noindex, no indexing request or sitemap submission was made for it.
- Local privacy/measurement wiring is prepared: Google Analytics 4 and Microsoft Clarity load only when configured with their public project IDs and accepted by a visitor. The contact metric is only `contact_draft_opened`; it does not mean an email was sent or received. The consent and privacy changes are not yet on the live preview.
- The GA4 property and web stream were created, but its `G-...` measurement ID has not yet been added to Netlify. Clarity setup is still incomplete and its project ID is not available. No visitor tracking is active on the current preview.
- The initial owner dashboard can combine GA4 traffic with Clarity heatmaps/recordings after both are installed and Clarity is linked to the GA4 property. Search Console remains a separate search-performance view; the contact inbox remains the source of truth for actual enquiries. There is no form-submission database or customer dashboard.

## What is not finished

1. **Final local review and preview update.** Review the latest local changes and responsive article/graphic presentation. They have not been committed or pushed, so the public preview still reflects the last deployed commit.
   - Finish Clarity project creation and retrieve its project ID; retrieve the GA4 web-stream measurement ID. These IDs are not passwords, but they should be configured in Netlify environment variables rather than committed to source.
   - Add the IDs in Netlify, deploy the preview, verify the consent choices and confirm opted-in data appears in each service. Verify a draft-open event only; never treat it as a delivered enquiry.
   - Link the GA4 web stream to Clarity from Clarity Settings → Setup → Google Analytics integration. Add saved links/bookmarks for Search Console and the inbox to the owner’s operating dashboard. A consolidated reporting dashboard can be considered after traffic data exists.
2. **Domain choice and availability.** Check the exact spelling and extension, registration and renewal cost, and whether the name is suitable for the intended markets before purchase. No domain has been bought. Any trademark/name clearance is separate from checking technical domain availability.
3. **Editorial readiness.** Recheck article facts, dates and source-use rights at publication time; obtain human editorial approval; ensure the byline and publication date are real and accurate. Drafts stay out of the site feed and sitemap until approved.
4. **Production-domain setup.** After selecting a domain, add it to the host, choose one preferred HTTPS host, update canonicals, social metadata, structured-data URLs and sitemaps, verify the final domain in Search Console and submit the regular sitemap. Remove noindex only when the site and launch information are ready. Google visibility or Google News inclusion cannot be guaranteed.
5. **Publisher/legal launch facts.** Confirm the actual operator, owner and contact/grievance details before presenting them as facts. Kavita remains the publisher and is not the owner. Ask India-qualified counsel about applicable launch requirements when the business structure and publication plan are settled.

## Scope boundary: future customer dashboard

The current product is a static newsroom site. It does not have customer accounts, article upload, checkout, payment, subscription quotas, edit-credit enforcement or a private dashboard. A real five-article quota and one-edit-per-published-article rule need a secure backend with authentication and persistent data; static GitHub Pages/Netlify files alone cannot enforce those rules. Keep paid orders closed until that separate product and its privacy, security and terms are designed.

## Hosting and budget

The temporary Netlify preview is public but noindex. The repository is still the source of code, and GitHub Pages remains unchanged. No monthly hosting fee or domain purchase has been made in this work. Recheck Netlify's current free-tier limits and terms before relying on it for a commercial launch; the domain will have its own registration and renewal cost.
