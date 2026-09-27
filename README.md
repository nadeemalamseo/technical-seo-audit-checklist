# Technical SEO Audit Checklist

A practical technical SEO audit checklist for reviewing crawlability, indexability, canonicalization, redirects, XML sitemaps, status codes, site architecture, performance, rendering, and technical validation.

## Overview

A technical SEO audit helps identify issues that can affect how a website is crawled, processed, indexed, and maintained by search engines.

This checklist provides a structured way to review the technical foundations of a website before making broader SEO decisions.

It is designed for:

- Website owners
- SEO professionals
- Digital marketers
- WordPress site owners
- Developers
- Agencies
- Technical SEO teams

## Use the Audit Worksheet

The repository includes a practical worksheet for recording checks, findings, evidence, recommendations, and verification results.

[Open the Technical SEO Audit Worksheet](checklist.md)

## What This Audit Covers

### 1. Website Accessibility

- Confirm the preferred HTTPS version is accessible
- Confirm the canonical domain is clear
- Check HTTP and HTTPS behavior
- Review `www` and non-`www` versions where applicable
- Check important URLs for successful responses
- Identify unexpected access restrictions
- Review server response behavior
- Check whether important pages can be accessed without unnecessary barriers

### 2. Crawlability

- Review `robots.txt`
- Confirm important sections are not unintentionally blocked
- Check blocked resources where they affect page rendering
- Review crawl directives
- Identify unnecessary crawlable URL patterns
- Check parameter-driven URLs where applicable
- Review faceted navigation where applicable
- Identify crawl traps
- Review excessive URL variations
- Check internal links to important pages
- Identify orphan pages

### 3. Indexability

- Identify important indexable pages
- Check `noindex` directives
- Review canonical tags
- Check HTTP status codes
- Identify accidentally indexed low-value URLs
- Identify important pages that are not indexed
- Review duplicate or near-duplicate URLs
- Check pagination where applicable
- Review indexing behavior after major site changes
- Compare intended indexability with actual search-engine indexing

### 4. Canonicalization

- Check canonical tags on important pages
- Confirm canonical URLs are valid
- Confirm canonical URLs use the preferred protocol
- Check canonical URLs against the preferred domain
- Identify self-referencing canonical inconsistencies
- Identify conflicting canonical signals
- Check canonical targets for redirects
- Check canonical targets for errors
- Review duplicate URL variations
- Confirm canonicalization reflects the actual preferred page

### 5. HTTP Status Codes

Review important URLs for appropriate HTTP responses.

Check for:

- `200` successful pages
- `301` permanent redirects
- `302` temporary redirects where appropriate
- `404` missing pages
- `410` intentionally removed content where appropriate
- `5xx` server errors
- Unexpected redirect responses
- Redirect chains
- Redirect loops
- Soft 404 behavior

Document important errors and determine whether each requires correction, redirection, removal, or monitoring.

### 6. Redirects

- Identify unnecessary redirects
- Check redirect chains
- Check redirect loops
- Review redirects after URL changes
- Confirm important redirects reach the intended destination
- Avoid unnecessary multi-step redirects
- Review internal links pointing to redirected URLs
- Check redirects after domain or protocol migrations
- Document significant redirect changes

### 7. XML Sitemaps

- Confirm the XML sitemap is accessible
- Confirm the sitemap URL is correctly referenced where appropriate
- Check sitemap response status
- Review included URLs
- Remove URLs that should not be submitted
- Check for broken URLs
- Check for redirected URLs
- Check canonical consistency
- Review sitemap segmentation for large websites where appropriate
- Confirm important indexable URLs are represented
- Monitor sitemap processing and errors

### 8. Site Architecture

- Review the hierarchy of important pages
- Identify cornerstone pages
- Review navigation structure
- Check important pages for sufficient internal links
- Identify orphan pages
- Review excessive URL depth where relevant
- Check category and subcategory relationships
- Review breadcrumb implementation
- Ensure architecture supports user navigation
- Ensure related pages are logically connected

### 9. Internal Linking

- Identify important pages
- Review links from relevant supporting pages
- Use descriptive anchor text
- Avoid excessive exact-match anchor usage
- Check for broken internal links
- Check for links pointing to redirected URLs
- Review orphan pages
- Review important pages with very few internal links
- Link related content where it genuinely helps users
- Review internal links after URL changes

### 10. Mobile & Responsive Experience

- Check important pages on mobile devices
- Review responsive layouts
- Check navigation usability
- Check content visibility
- Check interactive elements
- Review viewport configuration
- Check for horizontal scrolling
- Review mobile page performance
- Confirm important content is accessible on mobile

### 11. Performance

Review performance using appropriate real-user and laboratory data where available.

Check:

- Core Web Vitals
- Largest Contentful Paint
- Interaction to Next Paint
- Cumulative Layout Shift
- Server response time
- Image optimization
- Resource loading
- JavaScript execution
- CSS delivery
- Font loading
- Caching
- Compression
- Unnecessary third-party resources

Performance findings should be prioritized according to user impact and actual evidence.

### 12. JavaScript & Rendering

- Identify important content dependent on JavaScript
- Check whether important content is available to crawlers
- Review client-side rendering behavior
- Check links generated by JavaScript
- Review dynamically loaded content
- Check important metadata
- Review structured data implementation
- Test important templates after JavaScript changes
- Investigate rendering-dependent indexing problems

### 13. Duplicate Content

- Identify duplicate URLs
- Review URL parameters
- Check protocol variations
- Check domain variations
- Review trailing-slash variations where relevant
- Check duplicate category or archive pages
- Review printer or alternative versions where applicable
- Check pagination and filtering URLs
- Use canonicalization or other appropriate controls where necessary

### 14. Images & Media

- Check important images for accessibility
- Review useful image `alt` text
- Check image file sizes
- Review image dimensions
- Check responsive image delivery
- Review lazy loading
- Check broken image resources
- Review image URLs and redirects
- Ensure important visual information is not unnecessarily inaccessible

### 15. Structured Data

- Identify applicable structured data
- Confirm markup reflects visible page content
- Use appropriate Schema.org types
- Check required properties where applicable
- Review recommended properties where useful
- Validate structured data
- Check for invalid or misleading markup
- Review structured data after template changes
- Document significant implementation changes

### 16. Metadata

Review important pages for:

- Page titles
- Meta descriptions
- Canonical URLs
- Robots directives
- Language information where applicable
- Open Graph metadata
- Social sharing metadata
- Duplicate metadata
- Missing metadata
- Metadata inconsistencies

Metadata should support accurate representation of the page rather than rely on keyword repetition alone.

### 17. International & Multilingual SEO

Where applicable:

- Review language targeting
- Review country targeting
- Check `hreflang` implementation
- Check reciprocal `hreflang` references
- Validate language-region codes
- Review canonical relationships
- Check alternate URL accessibility
- Identify conflicting international signals

Only audit international elements when the website actually uses them.

### 18. Security & HTTPS

- Confirm HTTPS is enabled
- Check for HTTP-to-HTTPS redirects
- Review mixed-content issues
- Check certificate validity
- Review security-related browser warnings
- Check important resources over HTTPS
- Review unexpected insecure references

### 19. Error Monitoring

Establish a process for monitoring:

- Server errors
- Crawl errors
- Broken links
- Redirect problems
- Indexing issues
- Sitemap errors
- Template problems
- Deployment-related issues
- Unexpected URL changes

Document significant incidents and their resolutions.

---

## Technical SEO Audit Workflow

A practical audit can follow this sequence:

```text
1. DEFINE THE AUDIT SCOPE
          ↓
2. CRAWL & ACCESSIBILITY
          ↓
3. INDEXABILITY
          ↓
4. CANONICALIZATION
          ↓
5. STATUS CODES & REDIRECTS
          ↓
6. XML SITEMAPS
          ↓
7. SITE ARCHITECTURE
          ↓
8. INTERNAL LINKING
          ↓
9. MOBILE & PERFORMANCE
          ↓
10. RENDERING & JAVASCRIPT
          ↓
11. STRUCTURED DATA
          ↓
12. VALIDATE & DOCUMENT
          ↓
13. PRIORITIZE ACTIONS
          ↓
14. RECRAWL & VERIFY
```

The exact order may change depending on the website, audit objective, and severity of identified problems.

## Audit Prioritization

Not every technical issue deserves the same level of attention.

For each finding, document:

| Field | Description |
|---|---|
| Issue | What was identified |
| Location | URL, template, directory, or system affected |
| Evidence | Data supporting the finding |
| Impact | Potential consequence |
| Recommendation | Suggested corrective action |
| Priority | Relative implementation priority |
| Owner | Person or team responsible |
| Status | Open, in progress, resolved, or monitoring |
| Verification | How the correction will be tested |

Prioritize issues according to their actual effect on accessibility, crawling, indexing, usability, performance, and site maintenance.

## Evidence Sources

Useful audit evidence may include:

- Website crawls
- Server logs
- HTTP response testing
- Google Search Console
- Analytics data
- XML sitemaps
- `robots.txt`
- Browser testing
- Page-source inspection
- Rendering tests
- Structured-data validation
- Core Web Vitals data
- Real-user performance data
- Internal linking analysis

Use multiple evidence sources when a finding could have more than one explanation.

## Before Making Changes

Before implementing significant technical changes:

1. Record the current state.
2. Document the affected URLs or templates.
3. Identify dependencies.
4. Create a rollback plan where appropriate.
5. Make the smallest practical change.
6. Validate the result.
7. Monitor the affected area after deployment.

## Verification After Fixes

After implementing a correction:

- Recheck the affected URL or template
- Confirm the intended HTTP status
- Confirm canonical behavior
- Confirm robots directives
- Recheck internal links
- Recheck sitemap inclusion where applicable
- Validate structured data where applicable
- Review rendering
- Re-crawl affected sections
- Monitor search-engine processing over time

Do not assume that implementing a fix immediately changes search-engine processing or indexing.

## Common Technical SEO Audit Mistakes

Avoid:

- Treating every crawl warning as a critical problem
- Blocking important resources without understanding the consequences
- Changing canonicals without checking page relationships
- Redirecting large numbers of URLs without documenting the mapping
- Removing indexed pages without evaluating their purpose
- Making technical changes without a baseline
- Relying on a single SEO tool as the only source of evidence
- Assuming correlation proves causation
- Implementing structured data that does not match visible content
- Making large technical changes without verification
- Prioritizing issues solely because an automated tool assigns a high score

## Audit Documentation

Keep a record of:

- Audit date
- Website scope
- Tools and data sources
- Crawl configuration
- Important findings
- Recommended actions
- Implemented changes
- Verification results
- Follow-up dates

Good documentation makes future audits easier to reproduce and compare.

## Maintenance

Technical SEO is not a one-time task.

Review important technical areas after:

- Website migrations
- Domain changes
- Template changes
- CMS changes
- Major plugin changes
- Navigation changes
- URL restructuring
- Large content releases
- Performance changes
- Significant development deployments

Schedule recurring technical reviews according to the website's size, complexity, and rate of change.

## Related Resource

For a broader implementation framework covering AI search, content optimization, structured data, entity optimization, internal linking, authority, and measurement:

[AI SEO Implementation Checklist](https://github.com/nadeemalamseo/ai-seo-implementation-checklist)

Market Latch publishes practical resources covering SEO, AI search, WordPress, content strategy, and digital marketing.

[Visit Market Latch](https://marketlatch.com/)

## Disclaimer

This checklist provides general educational information for technical SEO auditing.

Search engines, browsers, CMS platforms, and web technologies can change over time. A technical issue does not automatically mean that a website will lose rankings or traffic, and resolving an issue does not guarantee improved search performance.

Always validate findings against the actual website, available evidence, current authoritative documentation, and the site's specific technical environment.

## Author

Created by **Nadeem Alam**, Digital Marketing & SEO Specialist.

[GitHub profile](https://github.com/nadeemalamseo)
