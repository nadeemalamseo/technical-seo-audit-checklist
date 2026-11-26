# Technical SEO Audit Methodology

This document explains how to use the checklist without turning automated warnings, incomplete datasets, or assumptions into unsupported SEO conclusions.

## 1. Define scope before testing

Record the canonical domain, relevant subdomains, URL patterns, page templates, important business URLs, language/device variants, authentication requirements, exclusions, and audit date. Record crawler configuration: user agent, crawl limits, rendering mode, robots handling, and whether the crawl used a browser, crawler, API, or server logs.

A sample-based audit must disclose the sample. Do not describe a sample as a full-site audit.

## 2. Separate observations, interpretations, and recommendations

Use three distinct statements:

- **Observation:** what the source directly showed (for example, a URL returned HTTP 503 at a recorded time).
- **Interpretation:** what the observation may mean in context (for example, a temporary server issue may affect crawling if it persists).
- **Recommendation:** the action proposed and how it will be verified.

Record affected URLs/templates, timestamp and time zone, source/tool/version, configuration, evidence, expected behavior, impact, confidence, owner, status, and verification. Mark untested items as **Not tested** and conditional items as **Not applicable**; neither is a pass.

## 3. Use evidence in the right order

### First-party Google evidence

Use Search Console for Google-reported search performance and indexing diagnostics. Use URL Inspection for an individual URL's reported indexing state and live test; use the Page indexing report for patterns and trends. Reports have scope and sampling limitations. A URL absent from a report is not automatically a confirmed error, and an indexed URL is not guaranteed to appear for every query.

Search Console query tables can omit anonymized queries and may not show every row. Exported or aggregated totals can therefore differ from visible table rows. Record the report, property, date range, search type, filters, and dimensions used.

### Direct site evidence

Use repeatable HTTP requests, source and rendered DOM inspection, browser testing, server logs, deployment records, and controlled reproduction steps. Record status codes, redirect hops, response headers, timestamps, user agent, and relevant page/template context.

### Third-party tools and estimates

Crawler scores, estimated traffic, keyword volumes, backlink metrics, and vendor-defined health scores are not Google measurements. Use them to discover patterns or prioritize further investigation. Label them as estimates, record the vendor and date, and independently verify material findings before reporting them as defects or causes.

Do not infer a Google ranking cause from a correlation, a single crawl, a tool score, or a change in a third-party metric.

## 4. Interpret crawl and indexing controls correctly

- `robots.txt` controls crawler access; it is not a reliable way to remove a URL from Google's index.
- A crawler blocked by `robots.txt` cannot read a page-level `noindex` directive on that page. If deindexing is the goal, the URL generally needs to remain crawlable so Google can process the directive, or access must be restricted appropriately.
- A sitemap is a discovery and canonical-URL hint. Submission does not guarantee crawling, indexing, or ranking.
- Do not treat every excluded URL, 404, duplicate, or non-indexed page as an error. Determine whether the state is intentional and whether the URL matters.
- Google's minimum technical requirements are not a promise of indexing. Eligibility and actual indexing are separate outcomes.

## 5. Measure Core Web Vitals correctly

The current Core Web Vitals are LCP, INP, and CLS. Use field data (real-user data) where available to assess actual experience. Lab tests are controlled diagnostics useful for debugging; do not present a single lab run as field performance.

At the 75th percentile, the published good thresholds are:

| Metric | Good | Poor |
|---|---:|---:|
| LCP | ≤ 2.5 seconds | > 4.0 seconds |
| INP | ≤ 200 milliseconds | > 500 milliseconds |
| CLS | ≤ 0.1 | > 0.25 |

Record the device category, URL or origin/group scope, date range, sample/coverage limitations, and whether values are field or lab data. Values between the good and poor thresholds are **Needs improvement**. Do not compare unlike scopes or device categories as if they were equivalent.

## 6. Prioritize without inventing a ranking score

Use priority to guide implementation order, not to predict ranking gains.

- **Critical:** verified issue that makes key pages unavailable, unintentionally blocks important crawling/indexing, exposes users to a serious security risk, or causes a broad severe failure. Confirm scope and rule out expected behavior.
- **High:** verified issue affecting important templates or a substantial set of valuable URLs, with a material user or search-processing consequence.
- **Medium:** verified, narrower issue or meaningful improvement with a limited scope or workaround.
- **Low:** minor, low-risk improvement, housekeeping, or issue with limited demonstrated impact.
- **Not rated:** insufficient evidence or applicability is unclear; investigate before assigning severity.

A vendor's severity label is not the priority decision. Consider affected URL count and importance, duration, user impact, evidence confidence, reversibility, dependencies, and implementation risk. Avoid assigning a priority solely because a tool flags an item.

## 7. Verify changes and monitor outcomes

Capture a baseline before changes. Record the exact change, affected templates/URLs, deployment date, and rollback plan where appropriate. Re-test the same conditions after deployment. Distinguish immediate technical verification (for example, a 301 now reaches the intended destination) from later search-engine processing (for example, Google recrawling or selecting a canonical). Do not claim that the latter has happened until first-party evidence supports it.

## 8. Authoritative references

- [Google Search technical requirements](https://developers.google.com/search/docs/essentials/technical)
- [Google robots.txt introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [Block Search indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing)
- [Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Search Console Page indexing report](https://support.google.com/webmasters/answer/7440203)
- [Search Console performance reports](https://support.google.com/webmasters/answer/10268906)
- [Search Console query data limitations](https://support.google.com/webmasters/answer/17011259)
- [Core Web Vitals thresholds and methodology](https://web.dev/articles/defining-core-web-vitals-thresholds)

Recheck these sources when updating this resource; search documentation and product interfaces can change.
