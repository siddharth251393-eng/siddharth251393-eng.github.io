# IndustryWire: pre-purchase handoff

**Website code is prepared locally. No domain or hosting has been purchased, and no new public deployment has been made.** Keep the GitHub repository as the source of the site code.

## What is ready

- Newsroom-first, mobile-responsive static site, IndustryWire identity and future publishing page.
- About, contact, corrections, editorial policy, privacy and site terms pages.
- Kavita publisher profile, transparent organization byline, article template, sample-analysis separation, and three source-linked launch drafts in `drafts/`.
- Search metadata, self-canonicals for the current GitHub Pages origin, regular sitemap, robots file and empty news sitemap.
- Netlify deployment configuration (`netlify.toml`) and a build script that rewrites canonicals, structured-data URLs, robots and sitemap origins for the deploy host. Preview builds default to `noindex`; unpublished `drafts/` are excluded.
- Local internal-link, fragment, canonical/sitemap and JSON-LD checks.
- Custom `404.html` recovery page.

## Do these before buying a domain

1. **Clear the name in India and any other target markets.** IndustryWire is still provisional. The official India public-search page currently requires CAPTCHA and an OTP login, so no registry result, owner or status could be verified in this review. Independent public-web checks surfaced an exact-name industry-news blog and a US listing for INDUSTRYWIRE in class 35 described as in use for communications/media/news/press services. These are risk indicators, not a legal conclusion or proof of Indian rights. Search IndustryWire, Industry Wire, phonetic/similar spellings and relevant services (classes 35 and 41 are starting points to discuss with a professional); review status, owner and services in the registry. Have an India trademark professional assess the results, then clear each intended foreign market before buying a matching domain. Do not send or share an OTP.
2. **Confirm the legal publisher/operator.** India is the planned operating country. Kavita is the named publisher, not the owner. “IndustryWire” is the publication title/brand. The owner, legal person/entity structure and registered details remain unconfirmed and must be treated as separate information. The current contact email is the only confirmed public contact. Do not invent a company name or registration details.
3. **Approve and date the launch coverage.** Re-check the three drafts against the latest official data, have the responsible human publisher/editing contact review them, and use the actual first-publication time. These drafts remain noindex and outside the archive/sitemaps until that is done.
4. **Choose the final domain spelling and extension.** Check availability and renewal pricing only after the name is cleared. Record the regular renewal price and avoid buying extra email, privacy, or hosting bundles unless needed.
5. **Confirm India digital-news compliance.** Because the project is intended to publish news from India, ask an India-qualified media/technology lawyer what current digital-news publisher requirements apply before public launch. The Ministry of Information and Broadcasting’s published Rule 18 information format distinguishes the publication title from the entity name and asks for entity/contact and grievance details. Its notice says information furnishing is not the same as prior registration; confirm the current process and scope for this publication rather than assuming exemption or a registration requirement.

## Hosting option researched for a zero monthly budget

GitHub remains the code repository. GitHub Pages is not the recommended production host for this planned commercial publication: GitHub's published limits say its free Pages service is not intended for running an online business or a site primarily facilitating commercial transactions.

Netlify currently advertises a Free plan at $0/month, supports commercial projects, permits custom domains with SSL, and provides 300 monthly usage credits. The plan has a hard limit; if usage reaches it, sites pause until the next billing cycle. The plan may change, and its agreement reserves provider discretion over Free-tier projects, so re-check the current terms when launching. A custom domain itself still has an annual registration/renewal cost. Start on a temporary `netlify.app` address for a no-cost smoke review before buying a domain. The deployment configuration is prepared, but no Netlify account has been connected and no deployment has been made.

Sources: [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits); [Netlify Free plan and commercial projects](https://www.netlify.com/blog/introducing-netlify-free-plan/); [Netlify current pricing and limits](https://www.netlify.com/pricing/); [Netlify domain setup](https://docs.netlify.com/domains-https/custom-domains/); [MIB digital media rules and guidance](https://mib.gov.in/en/ministry/our-wings/digital-media); [MIB digital-news publisher information format](https://mib.gov.in/sites/default/files/2025-06/furnishing-of-informaiton-30.05.2025_0.pdf).

## After the name and domain are settled

- Create a Netlify account and connect it to this GitHub repository. Keep all code commits in GitHub; Netlify will use `netlify.toml` to build a clean `dist/` preview from the static source.
- Deploy first to the temporary preview address and inspect pages, responsive layout, contact links, `404.html`, sitemaps and robots file.
- Add the cleared custom domain, update canonical/OG/structured-data URLs and sitemap/robots references throughout the HTML/XML, then enforce one HTTPS host and one preferred `www` or apex version.
- After the final domain is chosen, add a Search Console property, verify ownership using its provided DNS record or HTML meta token, submit `sitemap.xml`, inspect key URLs, and track indexing and queries. No Search Console property for a final domain is verified yet. Add current news entries to `news-sitemap.xml` only when eligible, original articles go live.
- Keep paid publishing, customer accounts, uploads and payments closed until the future service workflow, privacy/security controls and reviewed terms are implemented.

**Purchase point:** after steps 1–5 above. At that point, the likely cost is the domain registration only; Netlify hosting may remain $0/month if the site stays within Free-plan limits. Do not buy until the brand check is satisfactory.
