# Technical SEO Audit Checklist

A practical worksheet for reviewing the technical foundations of a website.

Use the checklist to record findings, evidence, recommendations, and verification results. Treat each item as a prompt to investigate; do not mark a site as defective without recording supporting evidence.

## Audit setup and evidence rules

- [ ] Audit scope is defined (domain, subdomains, URL patterns, templates, device types, and exclusions)
- [ ] Audit date, time zone, and comparison period are recorded
- [ ] Data sources and tool versions are recorded
- [ ] Crawl configuration is recorded (user agent, crawl limits, rendering mode, robots handling, and authentication)
- [ ] A representative URL sample and any sampling limitations are documented
- [ ] First-party data is distinguished from third-party estimates
- [ ] Findings are separated from hypotheses and recommendations
- [ ] Applicable / not applicable / not tested states are distinguished

**Evidence rule:** For every issue, record the affected URL(s) or template, observation date, source, exact evidence, expected behavior, potential impact, confidence, owner, status, and a reproducible verification method. If evidence is unavailable, mark the item **Not tested** rather than **Pass** or **Fail**.

**Source distinction:** Search Console and other first-party diagnostics describe their own reported data; third-party crawlers and vendor scores are estimates or observations from their own systems. Do not present third-party scores as Google metrics or as proof of a ranking cause. See [Audit Methodology](methodology.md).

---

## 1. Website Accessibility

- [ ] HTTPS version is accessible
- [ ] Preferred canonical domain is clearly defined
- [ ] HTTP and HTTPS versions behave as intended
- [ ] `www` and non-`www` versions behave as intended
- [ ] Important URLs return expected responses
- [ ] Important pages are accessible without unnecessary barriers
- [ ] No unexpected access restrictions are affecting important pages
- [ ] Server response behavior has been reviewed

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

**Affected URL(s) / Template:**

**Data Source / Observation Date:**

**Priority / Confidence / Owner / Status:**

**Verification Method / Result:**

---

## 2. Crawlability

- [ ] `robots.txt` is accessible
- [ ] Important pages are not unintentionally blocked
- [ ] Important resources are accessible where required for rendering
- [ ] Crawl directives have been reviewed
- [ ] URLs that must be processed for a `noindex` directive are not blocked from crawling
- [ ] Unnecessary crawlable URL patterns have been identified
- [ ] Parameter-driven URLs have been reviewed where applicable
- [ ] Faceted navigation has been reviewed where applicable
- [ ] Potential crawl traps have been investigated
- [ ] Excessive URL variations have been reviewed
- [ ] Important pages have internal links
- [ ] Orphan pages have been identified

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 3. Indexability

- [ ] Important pages are intended to be indexable
- [ ] `noindex` directives have been reviewed
- [ ] Canonical tags have been reviewed
- [ ] HTTP status codes have been reviewed
- [ ] Important pages that are not indexed have been investigated
- [ ] Unwanted indexed URLs have been identified
- [ ] Duplicate URLs have been reviewed
- [ ] Pagination has been reviewed where applicable
- [ ] Indexing behavior has been reviewed after major site changes
- [ ] Intended indexability has been compared with observed indexing

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 4. Canonicalization

- [ ] Important pages contain appropriate canonical signals
- [ ] Canonical URLs are valid
- [ ] Canonical URLs use the preferred protocol
- [ ] Canonical URLs use the preferred domain
- [ ] Canonical targets do not unnecessarily redirect
- [ ] Canonical targets do not return errors
- [ ] Conflicting canonical signals have been investigated
- [ ] Duplicate URL variations have been reviewed
- [ ] Canonicalization reflects the intended preferred page

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 5. HTTP Status Codes

- [ ] Important `200` responses have been reviewed
- [ ] `301` redirects are used appropriately
- [ ] `302` redirects are used appropriately
- [ ] `404` responses have been reviewed
- [ ] `410` responses are used intentionally where appropriate
- [ ] `5xx` errors have been investigated
- [ ] Redirect chains have been identified
- [ ] Redirect loops have been identified
- [ ] Soft 404 behavior has been investigated

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 6. Redirects

- [ ] Unnecessary redirects have been identified
- [ ] Redirect chains have been identified
- [ ] Redirect loops have been identified
- [ ] Redirects after URL changes have been reviewed
- [ ] Important redirects reach the intended destination
- [ ] Internal links do not unnecessarily point to redirected URLs
- [ ] Redirects after migrations have been reviewed
- [ ] Significant redirect changes are documented

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 7. XML Sitemaps

- [ ] XML sitemap is accessible
- [ ] Sitemap URL is correctly referenced where appropriate
- [ ] Sitemap returns an expected response
- [ ] Included URLs have been reviewed
- [ ] URLs that should not be submitted have been excluded
- [ ] Broken URLs have been removed or corrected
- [ ] Redirected URLs have been reviewed
- [ ] Canonical consistency has been checked
- [ ] Important canonical URLs intended for indexing are represented
- [ ] Sitemap entries are not assumed to guarantee crawling, indexing, or ranking
- [ ] Sitemap processing and errors are monitored

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 8. Site Architecture

- [ ] Important page hierarchy has been reviewed
- [ ] Cornerstone pages have been identified
- [ ] Navigation structure has been reviewed
- [ ] Important pages have sufficient internal links
- [ ] Orphan pages have been identified
- [ ] URL depth has been reviewed where relevant
- [ ] Category and subcategory relationships are logical
- [ ] Breadcrumb implementation has been reviewed
- [ ] Architecture supports user navigation
- [ ] Related pages are logically connected

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 9. Internal Linking

- [ ] Important pages have been identified
- [ ] Relevant supporting pages link to important pages
- [ ] Anchor text describes the destination accurately
- [ ] Excessive exact-match anchors are avoided
- [ ] Broken internal links have been identified
- [ ] Links to redirected URLs have been identified
- [ ] Orphan pages have been reviewed
- [ ] Important pages with few internal links have been identified
- [ ] Related content is connected where useful
- [ ] Internal links have been reviewed after URL changes

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 10. Mobile & Responsive Experience

- [ ] Important pages have been tested on mobile
- [ ] Responsive layouts work correctly
- [ ] Navigation is usable on mobile
- [ ] Important content is visible
- [ ] Interactive elements are usable
- [ ] Viewport configuration is appropriate
- [ ] Horizontal scrolling is not unintentionally required
- [ ] Mobile performance has been reviewed
- [ ] Important content remains accessible on mobile

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 11. Performance

- [ ] Core Web Vitals have been reviewed using field data where available
- [ ] Field-data coverage, device category, URL/group scope, and reporting period are recorded
- [ ] Lab diagnostics are labelled separately from real-user field data
- [ ] LCP, INP, and CLS are assessed at the 75th percentile when the dataset supports it
- [ ] Largest Contentful Paint has been reviewed
- [ ] Interaction to Next Paint has been reviewed
- [ ] Cumulative Layout Shift has been reviewed
- [ ] Server response time has been reviewed
- [ ] Images have been reviewed for optimization
- [ ] Resource loading has been reviewed
- [ ] JavaScript execution has been reviewed
- [ ] CSS delivery has been reviewed
- [ ] Font loading has been reviewed
- [ ] Caching has been reviewed
- [ ] Compression has been reviewed
- [ ] Unnecessary third-party resources have been reviewed

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 12. JavaScript & Rendering

- [ ] Important content is accessible without unnecessary rendering barriers
- [ ] Client-side rendering behavior has been reviewed
- [ ] JavaScript-generated links have been reviewed
- [ ] Dynamically loaded content has been reviewed
- [ ] Important metadata is available as intended
- [ ] Structured data implementation has been reviewed
- [ ] Important templates have been tested after JavaScript changes
- [ ] Rendering-dependent indexing problems have been investigated

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 13. Duplicate Content

- [ ] Duplicate URLs have been identified
- [ ] URL parameters have been reviewed
- [ ] Protocol variations have been reviewed
- [ ] Domain variations have been reviewed
- [ ] Trailing-slash variations have been reviewed where relevant
- [ ] Duplicate archive or category URLs have been reviewed
- [ ] Alternative page versions have been reviewed
- [ ] Pagination and filtering URLs have been reviewed
- [ ] Appropriate controls have been considered for duplicate URLs

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 14. Images & Media

- [ ] Important images have been reviewed for accessibility
- [ ] Useful image `alt` text is present where appropriate
- [ ] Image file sizes have been reviewed
- [ ] Image dimensions have been reviewed
- [ ] Responsive image delivery has been reviewed
- [ ] Lazy loading has been reviewed
- [ ] Broken image resources have been identified
- [ ] Image URLs and redirects have been reviewed
- [ ] Important visual information is accessible where necessary

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 15. Structured Data

- [ ] Applicable structured data has been identified
- [ ] Structured data reflects visible page content
- [ ] Appropriate Schema.org types are used
- [ ] Required properties have been reviewed where applicable
- [ ] Recommended properties have been reviewed where useful
- [ ] Structured data has been validated
- [ ] Invalid markup has been investigated
- [ ] Misleading markup has been avoided
- [ ] Structured data has been reviewed after template changes

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 16. Metadata

- [ ] Important page titles have been reviewed
- [ ] Meta descriptions have been reviewed
- [ ] Canonical URLs have been reviewed
- [ ] Robots directives have been reviewed
- [ ] Language information has been reviewed where applicable
- [ ] Open Graph metadata has been reviewed
- [ ] Social sharing metadata has been reviewed
- [ ] Duplicate metadata has been identified
- [ ] Missing metadata has been identified
- [ ] Metadata inconsistencies have been reviewed

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 17. International & Multilingual SEO

Complete this section only when applicable.

- [ ] Language targeting has been reviewed
- [ ] Country targeting has been reviewed
- [ ] `hreflang` implementation has been reviewed
- [ ] Reciprocal `hreflang` references have been checked
- [ ] Language-region codes have been validated
- [ ] Canonical relationships have been reviewed
- [ ] Alternate URLs are accessible
- [ ] Conflicting international signals have been investigated

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 18. Security & HTTPS

- [ ] HTTPS is enabled
- [ ] HTTP-to-HTTPS redirects work as intended
- [ ] Mixed-content issues have been reviewed
- [ ] Certificate validity has been checked
- [ ] Security-related browser warnings have been investigated
- [ ] Important resources use HTTPS
- [ ] Unexpected insecure references have been reviewed

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

## 19. Error Monitoring

- [ ] Server errors are monitored
- [ ] Crawl errors are monitored
- [ ] Broken links are monitored
- [ ] Redirect problems are monitored
- [ ] Indexing issues are monitored
- [ ] Sitemap errors are monitored
- [ ] Template problems are monitored
- [ ] Deployment-related issues are monitored
- [ ] Unexpected URL changes are monitored
- [ ] Significant incidents and resolutions are documented

**Notes / Findings:**

**Evidence:**

**Recommended Action:**

---

# Audit Finding Register

Use one row per distinct issue (not one row per checklist tick). Keep the raw evidence or a durable link to it with the audit record.

| ID | Affected URL / Template | Finding | Evidence & Source | Impact | Priority | Confidence | Owner | Status | Verification |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Priority should reflect real scope and impact, not the number of tool warnings. Confidence describes the strength of the evidence, not how certain the auditor feels.

# Audit Summary

## Critical Findings

Record issues that require immediate investigation or action.

1. 
2. 
3. 

## High-Priority Findings

1. 
2. 
3. 

## Medium-Priority Findings

1. 
2. 
3. 

## Low-Priority Findings

1. 
2. 
3. 

---

# Verification Log

| Date | Change | Affected Area | Verification Method | Result |
|---|---|---|---|---|
| | | | | |

---

# Audit Information

| Field | Details |
|---|---|
| Website | |
| Audit Date | |
| Auditor | |
| Audit Scope | |
| Crawl Tool | |
| Other Data Sources | |
| Previous Audit Date | |
| Next Review | |

---

## Disclaimer

This checklist provides general educational information for technical SEO auditing.

Search engines, browsers, CMS platforms, and web technologies can change over time. Findings should be evaluated against the actual website, available evidence, current authoritative documentation, and the site's specific technical environment.

Completing this checklist does not guarantee rankings, indexing, traffic, or other search-performance outcomes.

## Author

Created by **Nadeem Alam**, Digital Marketing & SEO Specialist.

[GitHub profile](https://github.com/nadeemalamseo)
