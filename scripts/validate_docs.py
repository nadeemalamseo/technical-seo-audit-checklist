#!/usr/bin/env python3
"""Dependency-free documentation checks for the technical SEO checklist repository."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(path):
    file_path = ROOT / path
    if not file_path.is_file():
        errors.append(f"Missing required file: {path}")
        return ""
    return file_path.read_text(encoding="utf-8")

readme = read("README.md")
worksheet = read("checklist.md")
methodology = read("methodology.md")
landing = read("index.html")
index_md = read("index.md")

expected_sections = [
    "Website Accessibility", "Crawlability", "Indexability", "Canonicalization",
    "HTTP Status Codes", "Redirects", "XML Sitemaps", "Site Architecture",
    "Internal Linking", "Mobile & Responsive Experience", "Performance",
    "JavaScript & Rendering", "Duplicate Content", "Images & Media",
    "Structured Data", "Metadata", "International & Multilingual SEO",
    "Security & HTTPS", "Error Monitoring",
]

for number, heading in enumerate(expected_sections, start=1):
    pattern = rf"^## {number}\. {re.escape(heading)}$"
    if not re.search(pattern, worksheet, flags=re.MULTILINE):
        errors.append(f"Worksheet section missing or misnumbered: {number}. {heading}")
    if f"### {number}. {heading}" not in readme:
        errors.append(f"README coverage missing: {number}. {heading}")

for required in [
    "Not tested", "third-party estimates", "Search Console",
    "observation date", "verification", "Audit Finding Register",
]:
    if required.lower() not in worksheet.lower():
        errors.append(f"Worksheet evidence rule missing: {required}")

for required in [
    "First-party Google evidence", "Third-party tools and estimates",
    "robots.txt", "noindex", "75th percentile", "Needs improvement",
    "Critical", "Not rated",
]:
    if required.lower() not in methodology.lower():
        errors.append(f"Methodology topic missing: {required}")

latest_zip = "https://github.com/nadeemalamseo/technical-seo-audit-checklist/archive/refs/heads/main.zip"
if latest_zip not in readme or latest_zip not in landing or latest_zip not in index_md:
    errors.append("Latest main-branch ZIP must be linked from README, HTML landing page, and index.md")

if "archive/refs/tags/v0.1.0.zip" in readme or "archive/refs/tags/v0.1.0.zip" in landing:
    errors.append("A historical v0.1.0 ZIP is presented as a current download")

for token in [
    '<link rel="canonical" href="https://nadeemalamseo.github.io/technical-seo-audit-checklist/">',
    '<meta property="og:title"',
    '<meta name="twitter:card"',
    "<title>Technical SEO Audit Checklist | MarketLatch</title>",
]:
    if token not in landing:
        errors.append(f"Landing page metadata missing: {token}")

if "methodology.md" not in readme or "methodology.md" not in index_md or "methodology.md" not in landing:
    errors.append("Audit methodology must be linked from all project entry points")

if errors:
    print("Documentation validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Documentation validation passed: {len(expected_sections)} audit sections, evidence methodology, download links, and landing-page metadata.")
