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
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
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


def read_published_articles(indexing_enabled: bool) -> list[dict[str, str]]:
    """Load only explicitly approved articles for an indexable production build."""
    if not indexing_enabled:
        return []

    source = json.loads((ROOT / "articles.json").read_text(encoding="utf-8"))
    if not isinstance(source, dict):
        raise SystemExit("articles.json: the root value must be an object.")
    records = source.get("articles", [])
    if not isinstance(records, list):
        raise SystemExit("articles.json: 'articles' must be a list.")

    published: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict) or record.get("status") != "published":
            continue

        label = f"articles.json articles[{index}]"
        required = (
            "title", "url", "file", "summary", "section", "author",
            "authorType", "authorUrl", "published", "datePublished",
        )
        for key in required:
            if not isinstance(record.get(key), str) or not record[key].strip():
                raise SystemExit(f"{label}: '{key}' is required for a published article.")

        relative = Path(record["file"])
        if relative.is_absolute() or ".." in relative.parts or relative.suffix.lower() != ".html":
            raise SystemExit(f"{label}: 'file' must be a safe relative .html path under stories/.")
        if not relative.parts or relative.parts[0] != "stories":
            raise SystemExit(f"{label}: published story files must be stored under stories/.")
        expected_url = "/" + relative.as_posix()
        if record["url"] != expected_url:
            raise SystemExit(f"{label}: 'url' must match the public path {expected_url!r}.")
        if record["url"] in seen_urls:
            raise SystemExit(f"{label}: duplicate article URL {record['url']!r}.")
        seen_urls.add(record["url"])
        if record["authorType"] not in {"Person", "Organization"}:
            raise SystemExit(f"{label}: 'authorType' must be Person or Organization.")
        if record["authorUrl"].startswith("/") and not record["authorUrl"].startswith("//"):
            author_page = (ROOT / record["authorUrl"].lstrip("/")).resolve()
            if not author_page.is_relative_to(ROOT.resolve()) or not author_page.is_file():
                raise SystemExit(f"{label}: internal 'authorUrl' must point to a local author page.")
        elif not record["authorUrl"].startswith("https://"):
            raise SystemExit(f"{label}: 'authorUrl' must be a site path or HTTPS URL.")

        try:
            published_at = datetime.fromisoformat(record["datePublished"].replace("Z", "+00:00"))
        except ValueError as exc:
            raise SystemExit(f"{label}: 'datePublished' must be an ISO 8601 date/time.") from exc
        if published_at.tzinfo is None:
            raise SystemExit(f"{label}: 'datePublished' must include a timezone.")
        if published_at > datetime.now(timezone.utc) + timedelta(minutes=5):
            raise SystemExit(f"{label}: 'datePublished' cannot be in the future.")
        if record.get("dateModified") and not isinstance(record["dateModified"], str):
            raise SystemExit(f"{label}: 'dateModified' must be a string.")
        if record.get("dateModified"):
            try:
                modified_at = datetime.fromisoformat(record["dateModified"].replace("Z", "+00:00"))
            except ValueError as exc:
                raise SystemExit(f"{label}: 'dateModified' must be an ISO 8601 date/time.") from exc
            if modified_at.tzinfo is None:
                raise SystemExit(f"{label}: 'dateModified' must include a timezone.")
            if modified_at < published_at:
                raise SystemExit(f"{label}: 'dateModified' cannot be earlier than 'datePublished'.")

        page = ROOT / relative
        if not page.resolve().is_relative_to(ROOT.resolve()) or not page.is_file():
            raise SystemExit(f"{label}: story file does not exist: {relative.as_posix()}.")
        body = page.read_text(encoding="utf-8")
        visible_body = re.sub(r"<head\b[^>]*>.*?</head>", " ", body, flags=re.IGNORECASE | re.DOTALL)
        visible_body = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", visible_body, flags=re.IGNORECASE | re.DOTALL)
        heading = re.search(r"<h1\b[^>]*>(.*?)</h1>", visible_body, flags=re.IGNORECASE | re.DOTALL)
        if not heading:
            raise SystemExit(f"{label}: the story page must have one visible h1 headline.")
        visible_headline = html.unescape(re.sub(r"<[^>]+>", " ", heading.group(1)))
        visible_headline = re.sub(r"\s+", " ", visible_headline).strip().casefold()
        if visible_headline != record["title"].strip().casefold():
            raise SystemExit(f"{label}: the visible h1 must exactly match 'title'.")
        visible_text = html.unescape(re.sub(r"<[^>]+>", " ", visible_body))
        visible_text = re.sub(r"\s+", " ", visible_text).casefold()
        for key in ("author", "published"):
            if record[key].casefold() not in visible_text:
                raise SystemExit(f"{label}: '{key}' must match text visible on the story page.")
        date_tokens = {
            published_at.strftime("%Y-%m-%d"),
            published_at.strftime("%d %B %Y").lstrip("0"),
            published_at.strftime("%B %d, %Y"),
            published_at.strftime("%d %b %Y").lstrip("0"),
            published_at.strftime("%b %d, %Y"),
        }
        if not any(token.casefold() in record["published"].casefold() for token in date_tokens):
            raise SystemExit(f"{label}: visible 'published' date must match 'datePublished'.")

        published.append(record)
    return published


def inject_article_metadata(destination: Path, article: dict[str, str], origin: str) -> None:
    """Generate article metadata from the same reviewed record used by the archive."""
    author_url = article["authorUrl"]
    if author_url.startswith("/"):
        author_url = origin + author_url
    schema: dict[str, object] = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": article["title"],
        "description": article["summary"],
        "datePublished": article["datePublished"],
        "author": {
            "@type": article["authorType"],
            "name": article["author"],
            "url": author_url,
        },
        "publisher": {
            "@type": "Organization",
            "name": "The Sector Journal",
            "url": origin + "/",
        },
        "mainEntityOfPage": {"@type": "WebPage", "@id": origin + article["url"]},
    }
    if article.get("dateModified"):
        schema["dateModified"] = article["dateModified"]

    text = destination.read_text(encoding="utf-8")
    text = re.sub(
        r'\s*<meta\s+name=["\']robots["\'][^>]*>',
        "",
        text,
        flags=re.IGNORECASE,
    )
    for name, content in {
        "og:type": "article",
        "og:site_name": "The Sector Journal",
        "og:title": article["title"],
        "og:description": article["summary"],
        "og:url": origin + article["url"],
        "article:published_time": article["datePublished"],
    }.items():
        escaped = html.escape(content, quote=True)
        tag = f'<meta property="{name}" content="{escaped}">'
        text = re.sub(
            rf'\s*<meta\s+property=["\']{re.escape(name)}["\'][^>]*>',
            "",
            text,
            flags=re.IGNORECASE,
        )
        text = text.replace("</head>", tag + "</head>", 1)
    if article.get("dateModified"):
        escaped = html.escape(article["dateModified"], quote=True)
        text = text.replace(
            "</head>",
            f'<meta property="article:modified_time" content="{escaped}"></head>',
            1,
        )
    text = text.replace(
        "</head>",
        '<script type="application/ld+json" data-sector-journal-generated>'
        + json.dumps(schema, ensure_ascii=False, separators=(",", ":"))
        + "</script></head>",
        1,
    )
    destination.write_text(text, encoding="utf-8")


def write_article_sitemaps(articles: list[dict[str, str]], origin: str) -> None:
    """Add approved articles to the regular sitemap and only fresh stories to News."""
    sitemap_path = DIST / "sitemap.xml"
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", namespace)
    known = {node.text for node in root.findall(f"{{{namespace}}}url/{{{namespace}}}loc")}

    urls = (["/articles.html"] if articles else []) + [article["url"] for article in articles]
    for path in urls:
        absolute = origin + path
        if absolute not in known:
            node = ET.SubElement(root, f"{{{namespace}}}url")
            ET.SubElement(node, f"{{{namespace}}}loc").text = absolute
            known.add(absolute)
    tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)

    news_namespace = "http://www.google.com/schemas/sitemap-news/0.9"
    news_root = ET.Element(f"{{{namespace}}}urlset")
    ET.register_namespace("", namespace)
    ET.register_namespace("news", news_namespace)
    now = datetime.now(timezone.utc)
    for article in articles:
        published_at = datetime.fromisoformat(article["datePublished"].replace("Z", "+00:00"))
        if now - published_at.astimezone(timezone.utc) > timedelta(hours=48):
            continue
        item = ET.SubElement(news_root, f"{{{namespace}}}url")
        ET.SubElement(item, f"{{{namespace}}}loc").text = origin + article["url"]
        news = ET.SubElement(item, f"{{{news_namespace}}}news")
        publication = ET.SubElement(news, f"{{{news_namespace}}}publication")
        ET.SubElement(publication, f"{{{news_namespace}}}name").text = "The Sector Journal"
        ET.SubElement(publication, f"{{{news_namespace}}}language").text = "en"
        ET.SubElement(news, f"{{{news_namespace}}}publication_date").text = article["datePublished"]
        ET.SubElement(news, f"{{{news_namespace}}}title").text = article["title"]
    ET.ElementTree(news_root).write(
        DIST / "news-sitemap.xml", encoding="utf-8", xml_declaration=True
    )


def write_rss_feed(articles: list[dict[str, str]], origin: str) -> None:
    """Generate a summary-only RSS feed from explicitly published stories."""
    rss_namespace = "http://www.w3.org/2005/Atom"
    dc_namespace = "http://purl.org/dc/elements/1.1/"
    ET.register_namespace("atom", rss_namespace)
    ET.register_namespace("dc", dc_namespace)
    root = ET.Element("rss", {"version": "2.0"})
    channel = ET.SubElement(root, "channel")
    ET.SubElement(channel, "title").text = "The Sector Journal"
    ET.SubElement(channel, "link").text = origin + "/"
    ET.SubElement(channel, "description").text = (
        "Independent, sourced reporting on business and industry."
    )
    ET.SubElement(channel, "language").text = "en"
    ET.SubElement(
        channel,
        f"{{{rss_namespace}}}link",
        {"href": origin + "/rss.xml", "rel": "self", "type": "application/rss+xml"},
    )
    ET.SubElement(channel, "lastBuildDate").text = format_datetime(
        datetime.now(timezone.utc), usegmt=True
    )

    sorted_articles = sorted(
        articles,
        key=lambda article: datetime.fromisoformat(
            article["datePublished"].replace("Z", "+00:00")
        ),
        reverse=True,
    )
    for article in sorted_articles:
        published_at = datetime.fromisoformat(
            article["datePublished"].replace("Z", "+00:00")
        )
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = article["title"]
        story_url = origin + article["url"]
        ET.SubElement(item, "link").text = story_url
        ET.SubElement(item, "guid", {"isPermaLink": "true"}).text = story_url
        ET.SubElement(item, "description").text = article["summary"]
        ET.SubElement(item, "category").text = article["section"]
        ET.SubElement(item, f"{{{dc_namespace}}}creator").text = article["author"]
        ET.SubElement(item, "pubDate").text = format_datetime(
            published_at.astimezone(timezone.utc), usegmt=True
        )

    ET.ElementTree(root).write(
        DIST / "rss.xml", encoding="utf-8", xml_declaration=True
    )


def main() -> None:
    origin = site_origin()
    publishable = os.environ.get("PUBLIC_INDEXING", "false").strip().lower() == "true"
    verification = os.environ.get("GSC_VERIFICATION", "").strip()
    ga_measurement_id = os.environ.get("GA_MEASUREMENT_ID", "").strip()
    clarity_project_id = os.environ.get("CLARITY_PROJECT_ID", "").strip()
    if ga_measurement_id and not re.fullmatch(r"G-[A-Z0-9]+", ga_measurement_id):
        raise SystemExit("GA_MEASUREMENT_ID must be a Google Analytics G- measurement ID.")
    if clarity_project_id and not re.fullmatch(r"[A-Za-z0-9_-]+", clarity_project_id):
        raise SystemExit("CLARITY_PROJECT_ID contains unsupported characters.")
    published_articles = read_published_articles(publishable)

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    for source in sorted(ROOT.glob("*.html")):
        if source.name in {"article-template.html", "sample-articles.html"}:
            continue
        text = source.read_text(encoding="utf-8")
        text = text.replace(ORIGIN_PLACEHOLDER, origin)

        # The noindex preview deliberately omits story files. Replace the
        # homepage's production feature card so it cannot point to a missing
        # article on the temporary host.
        if source.name == "index.html" and not publishable:
            preview_panel = (
                '<div class="newsroom-panel"><div class="newsroom-mark" aria-hidden="true">SJ</div>'
                '<div><p class="eyebrow">NOINDEX PREVIEW</p>'
                '<h3>Newsroom coverage is being prepared</h3>'
                '<p>The temporary preview does not expose article pages while public indexing is disabled.</p>'
                '<a class="text-link" href="/editorial-policy.html">Read our editorial standards</a></div>'
                '<a class="newsroom-contact" href="/contact.html?type=Editorial%20enquiry">Send an editorial note</a></div>'
            )
            text, replacements = re.subn(
                r'<div class="newsroom-panel">.*?</div>\s*</section>',
                preview_panel + "\n  </section>",
                text,
                count=1,
                flags=re.DOTALL,
            )
            if replacements != 1:
                raise SystemExit("index.html: expected one homepage newsroom panel to update for the noindex preview.")

        # The newsroom archive becomes indexable only once a reviewed article
        # exists and the production build explicitly enables public indexing.
        if source.name == "articles.html" and publishable and published_articles:
            text = re.sub(
                r'\s*<meta\s+name=["\']robots["\'][^>]*>',
                "",
                text,
                count=1,
                flags=re.IGNORECASE,
            )

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

    # A story file is copied only when its metadata is explicitly marked
    # "published" and the build is configured for production indexing.
    for article in published_articles:
        copy_file(article["file"])
        inject_article_metadata(DIST / article["file"], article, origin)

    for relative in (
        "style.css",
        "site.js",
        "site-config.js",
        "privacy-consent.js",
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

    # Only explicitly published records appear in the public feed. Sample
    # explainers and internal draft records never enter the deployed data.
    article_data = {
        "articles": [
            {
                key: article[key]
                for key in ("title", "url", "summary", "section", "author", "published")
            }
            for article in published_articles
        ]
    }
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
                feed_link = (
                    f'<link rel="alternate" type="application/rss+xml" '
                    f'title="The Sector Journal RSS feed" href="{origin}/rss.xml">'
                )
                text = re.sub(
                    r'\s*<link\s+rel=["\']alternate["\'][^>]*type=["\']application/rss\+xml["\'][^>]*>',
                    "",
                    text,
                    flags=re.IGNORECASE,
                )
                text = text.replace("</head>", feed_link + "</head>", 1)
            if not publishable:
                robots_meta = '<meta name="robots" content="noindex,nofollow">'
                if re.search(r'<meta\s+name=["\']robots["\']', text, flags=re.IGNORECASE):
                    text = re.sub(
                        r'<meta\s+name=["\']robots["\'][^>]*>', robots_meta,
                        text, count=1, flags=re.IGNORECASE
                    )
                else:
                    text = text.replace("</head>", f"{robots_meta}</head>", 1)
            if ga_measurement_id or clarity_project_id:
                attrs = []
                if ga_measurement_id:
                    attrs.append(f'data-ga-measurement-id="{html.escape(ga_measurement_id, quote=True)}"')
                if clarity_project_id:
                    attrs.append(f'data-clarity-project-id="{html.escape(clarity_project_id, quote=True)}"')
                consent_script = '<script defer src="/privacy-consent.js" ' + " ".join(attrs) + "></script>"
                text = text.replace("</head>", consent_script + "</head>", 1)
        target.write_text(text, encoding="utf-8")

    if publishable and published_articles:
        write_article_sitemaps(published_articles, origin)

    write_rss_feed(published_articles, origin)

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
