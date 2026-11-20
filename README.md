# Ecletra portfolio

Static Ecletra portfolio, hosted with GitHub Pages at https://forthewynne.uk.

Edit `dist/index.html` and `dist/style.css`. Push to `main` to deploy through GitHub Actions. No build or dependencies are required.

## Cloudflare DNS

Use DNS-only (grey cloud) records during GitHub Pages setup and certificate issuance:

| Type | Name | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | k33k0.github.io |

Replace conflicting web records only; preserve email records and unrelated subdomains. Remove obsolete apex AAAA records if they point elsewhere. Set the repository's Pages custom domain to `forthewynne.uk`, and enable Enforce HTTPS once GitHub has issued its certificate.

GitHub reference: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## Content and assets

The ribbon is extracted from the supplied brand guide. The phone illustration is explicitly labelled as an illustrative product preview. Upcoming products are not presented as released.

Copyright © 2026 Ecletra. All rights reserved. No open-source licence is granted.

The Inter font (`dist/assets/fonts/inter-latin.woff2`) is self-hosted and licensed under the SIL Open Font License 1.1 (https://github.com/rsms/inter). `dist/404.html`, `robots.txt` and `sitemap.xml` are served by GitHub Pages; update `lastmod` in the sitemap when content changes.
