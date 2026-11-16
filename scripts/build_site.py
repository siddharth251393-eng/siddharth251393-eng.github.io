#!/usr/bin/env python3
"""Build a clean static deployment for a Netlify preview or production site.

Internal planning files, reusable article templates, and unpublished drafts are
intentionally excluded. The site origin is rewritten at build time so metadata,
structured data, robots.txt, and sitemaps all use the deployed host.
"""

from __future__ import annotations

import html
import json
import os
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
ORIGIN_PLACEHOLDER = "https://siddharth251393-eng.github.io"


def site_origin() -> str:
    context = os.environ.get("CONTEXT", "").strip().lower()
    # Netlify deploy previews get their own canonical host; production builds
    # use the stable site URL (or an explicitly configured custom domain).
    value = os.environ.get("SITE_ORIGIN", "").strip()
    if not value:
        value = (
            os.environ.get("DEPLOY_PRIME_URL", "")
            if context in {"deploy-preview", "branch-deploy"}
            else os.environ.get("URL", "") or os.environ.get("DEPLOY_PRIME_URL", "")
        ).strip()
    value = value.rstrip("/")
    if not re.fullmatch(r"https://[A-Za-z0-9.-]+(?::\d+)?", value):
        raise SystemExit(
            "Set SITE_ORIGIN to the deployed HTTPS origin, or run this build in Netlify."
        )
    return value


def copy_file(relative: str) -> None:
    source = ROOT / relative
    if not source.exists():
        raise SystemExit(f"Required site file is missing: {relative}")
    destination = DIST / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def main() -> None:
    origin = site_origin()
    publishable = os.environ.get("PUBLIC_INDEXING", "false").strip().lower() == "true"
    verification = os.environ.get("GSC_VERIFICATION", "").strip()

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    for source in sorted(ROOT.glob("*.html")):
        if source.name in {"article-template.html", "sample-articles.html"}:
            continue
        text = source.read_text(encoding="utf-8")
        text = text.replace(ORIGIN_PLACEHOLDER, origin)

        # Never carry a Search Console token from the old host into a new one.
        text = re.sub(
            r'\s*<meta\s+name=["\']google-site-verification["\']\s+content=["\'][^"\']*["\']\s*/?>',
            "",
            text,
            flags=re.IGNORECASE,
        )
        if source.name == "index.html" and verification:
            token = html.escape(verification, quote=True)
            text = text.replace(
                "</head>",
                f'<meta name="google-site-verification" content="{token}"></head>',
                1,
            )

        # Give every published HTML file a self-referencing canonical, even
        # on pages that were previously missing one.
        # Error documents should not be advertised as canonical content.
        if source.name == "404.html":
            text = re.sub(
                r'\s*<link\s+rel=["\']canonical["\'][^>]*>',
                "",
                text,
                flags=re.IGNORECASE,
            )
        else:
            page_path = "/" if source.name == "index.html" else f"/{source.name}"
            canonical = f'<link rel="canonical" href="{origin}{page_path}">'
            text = re.sub(
                r'\s*<link\s+rel=["\']canonical["\'][^>]*>',
                "",
                text,
                flags=re.IGNORECASE,
            )
            text = text.replace("</head>", f"{canonical}</head>", 1)

        # Preview builds, including all their pages, must not be indexed.
        # Production indexing remains an explicit opt-in after clearance.
        if not publishable:
            robots_meta = '<meta name="robots" content="noindex,nofollow">'
            if re.search(r'<meta\s+name=["\']robots["\']', text, flags=re.IGNORECASE):
                text = re.sub(
                    r'<meta\s+name=["\']robots["\'][^>]*>',
                    robots_meta,
                    text,
                    count=1,
                    flags=re.IGNORECASE,
                )
            else:
                text = text.replace("</head>", f"{robots_meta}</head>", 1)
        (DIST / source.name).write_text(text, encoding="utf-8")

    for relative in (
        "style.css",
        "site.js",
        "site-config.js",
        "favicon.svg",
        "social-card.svg",
        "robots.txt",
        "sitemap.xml",
        "news-sitemap.xml",
    ):
        copy_file(relative)

    for directory in ("assets",):
        source_dir = ROOT / directory
        if source_dir.exists():
            shutil.copytree(source_dir, DIST / directory)

    # Only real, reviewed articles may appear in the public deployment data.
    # The source repository's sample explainers are deliberately omitted
    # from the deployed site and its story feed.
    article_data = json.loads((ROOT / "articles.json").read_text(encoding="utf-8"))
    article_data["articles"] = []
    article_data.pop("sampleArticles", None)
    (DIST / "articles.json").write_text(
        json.dumps(article_data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Rewrite every public text asset (including sample article metadata,
    # JSON, robots, and both sitemaps) to the actual deployment origin.
    for target in DIST.rglob("*"):
        if not target.is_file() or target.suffix.lower() not in {
            ".html", ".xml", ".txt", ".json", ".webmanifest", ".svg"
        }:
            continue
        text = target.read_text(encoding="utf-8")
        text = text.replace(ORIGIN_PLACEHOLDER, origin)
        if target.suffix.lower() == ".html":
            rel_path = target.relative_to(DIST).as_posix()
            page_path = "/" if rel_path == "index.html" else f"/{rel_path}"
            text = re.sub(
                r'\s*<link\s+rel=["\']canonical["\'][^>]*>',
                "",
                text,
                flags=re.IGNORECASE,
            )
            if rel_path != "404.html":
                canonical = f'<link rel="canonical" href="{origin}{page_path}">'
                text = text.replace("</head>", f"{canonical}</head>", 1)
            if not publishable:
                robots_meta = '<meta name="robots" content="noindex,nofollow">'
                if re.search(r'<meta\s+name=["\']robots["\']', text, flags=re.IGNORECASE):
                    text = re.sub(
                        r'<meta\s+name=["\']robots["\'][^>]*>', robots_meta,
                        text, count=1, flags=re.IGNORECASE
                    )
                else:
                    text = text.replace("</head>", f"{robots_meta}</head>", 1)
        target.write_text(text, encoding="utf-8")

    if not publishable:
        # A noindex preview should not advertise sitemap URLs as indexable.
        (DIST / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>\n',
            encoding="utf-8",
        )
        robots_path = DIST / "robots.txt"
        robots_path.write_text(
            "\n".join(
                line for line in robots_path.read_text(encoding="utf-8").splitlines()
                if not line.lower().startswith("sitemap:")
            ) + "\n",
            encoding="utf-8",
        )

    print(f"Built {len(list(DIST.rglob('*')))} deployment entries for {origin}")
    print(f"Public indexing enabled: {publishable}")


if __name__ == "__main__":
    main()
