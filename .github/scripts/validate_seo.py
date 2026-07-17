#!/usr/bin/env python3
"""Validate the small static SEO surface without third-party dependencies."""

from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
ORIGIN = "https://oakcoderx.github.io"
BASE_PATH = "/nomtiq"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.in_title = False
        self.h1_count = 0
        self.meta: dict[str, str] = {}
        self.links: list[str] = []
        self.json_ld: list[str] = []
        self.in_json_ld = False
        self.json_chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "meta":
            key = values.get("name") or values.get("property")
            if key:
                self.meta[key] = values.get("content", "")
        elif tag == "link" and values.get("rel") == "canonical":
            self.meta["canonical"] = values.get("href", "")
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"])
        elif tag == "script" and values.get("type") == "application/ld+json":
            self.in_json_ld = True
            self.json_chunks = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.in_json_ld:
            self.json_ld.append("".join(self.json_chunks))
            self.in_json_ld = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self.in_json_ld:
            self.json_chunks.append(data)


def public_url(page: Path) -> str:
    relative = page.relative_to(DOCS)
    if relative == Path("index.html"):
        route = "/"
    else:
        route = "/" + relative.parent.as_posix().strip("/") + "/"
    return f"{ORIGIN}{BASE_PATH}{route}"


def local_target(page: Path, href: str) -> Path | None:
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc or href.startswith("#"):
        return None
    clean = parsed.path
    if not clean:
        return None
    target = (page.parent / clean).resolve()
    if clean.endswith("/"):
        target /= "index.html"
    return target


def main() -> int:
    errors: list[str] = []
    pages = sorted(DOCS.glob("**/index.html"))
    expected_urls = {public_url(page) for page in pages}
    titles: dict[str, Path] = {}
    descriptions: dict[str, Path] = {}

    for page in pages:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        title = parser.title.strip()
        description = parser.meta.get("description", "").strip()
        canonical = parser.meta.get("canonical", "")
        expected = public_url(page)

        if not title or len(title) > 65:
            errors.append(f"{page}: title missing or longer than 65 characters")
        if title in titles:
            errors.append(f"{page}: duplicate title also used by {titles[title]}")
        titles[title] = page
        min_description_length = 40 if any(ord(char) > 127 for char in description) else 70
        if not description or not min_description_length <= len(description) <= 180:
            errors.append(
                f"{page}: meta description should be {min_description_length}-180 characters"
            )
        if description in descriptions:
            errors.append(f"{page}: duplicate description also used by {descriptions[description]}")
        descriptions[description] = page
        if parser.h1_count != 1:
            errors.append(f"{page}: expected exactly one h1, found {parser.h1_count}")
        if canonical != expected:
            errors.append(f"{page}: canonical {canonical!r} does not match {expected!r}")
        if parser.meta.get("og:url") != expected:
            errors.append(f"{page}: og:url does not match canonical")
        if not parser.json_ld:
            errors.append(f"{page}: missing JSON-LD")
        for payload in parser.json_ld:
            try:
                json.loads(payload)
            except json.JSONDecodeError as exc:
                errors.append(f"{page}: invalid JSON-LD: {exc}")
        for href in parser.links:
            target = local_target(page, href)
            if target is not None and not target.exists():
                errors.append(f"{page}: broken local link {href!r}")

    sitemap = ET.parse(DOCS / "sitemap.xml")
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = {node.text for node in sitemap.findall("s:url/s:loc", namespace)}
    if sitemap_urls != expected_urls:
        errors.append(
            "sitemap URLs differ from indexable HTML pages: "
            f"missing={sorted(expected_urls - sitemap_urls)}, extra={sorted(sitemap_urls - expected_urls)}"
        )

    if errors:
        print("SEO validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"SEO validation passed for {len(pages)} pages and {len(sitemap_urls)} sitemap URLs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
