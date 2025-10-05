# Legal and Ethical Scraping Checklist

Use this checklist before starting any web scraping project to ensure you're acting legally and ethically.

## Pre-Scraping Checks

### Legal Compliance

- [ ] **Read Terms of Service (ToS)**
  - Check if scraping is explicitly prohibited
  - Look for data usage restrictions
  - Note any API availability

- [ ] **Check robots.txt**
  - Visit `website.com/robots.txt`
  - Verify allowed/disallowed paths
  - Respect crawl-delay directives

- [ ] **Review Copyright**
  - Understand data ownership
  - Check for copyright notices
  - Plan appropriate attribution

- [ ] **Personal Data Compliance**
  - GDPR compliance (if EU data)
  - CCPA compliance (if California data)
  - Only collect publicly available data
  - Don't scrape PII without consent

- [ ] **Check Local Laws**
  - Research jurisdiction-specific regulations
  - Understand computer fraud laws (e.g., CFAA in US)
  - Consult legal counsel if uncertain

### Technical Preparation

- [ ] **API Availability**
  - Check if official API exists
  - Compare API vs scraping benefits
  - Prefer API when available

- [ ] **Rate Limiting Plan**
  - Implement delays between requests
  - Use exponential backoff for errors
  - Monitor request frequency

- [ ] **Error Handling**
  - Handle HTTP errors gracefully
  - Implement retry logic
  - Log errors properly

## During Scraping

### Respectful Practices

- [ ] **Identify Your Bot**
  - Use descriptive User-Agent
  - Include contact information
  - Be transparent about purpose

- [ ] **Respect Server Resources**
  - Limit concurrent requests
  - Scrape during off-peak hours
  - Cache responses during development

- [ ] **Monitor Impact**
  - Watch for 429 (Too Many Requests) errors
  - Adjust rate if necessary
  - Stop if causing issues

### Data Handling

- [ ] **Minimize Data Collection**
  - Only collect necessary data
  - Avoid redundant requests
  - Clean up temporary data

- [ ] **Secure Storage**
  - Encrypt sensitive data
  - Use secure connections (HTTPS)
  - Follow data retention policies

## Post-Scraping

### Data Usage

- [ ] **Respect Copyright**
  - Don't republish copyrighted content
  - Provide proper attribution
  - Use data within legal bounds

- [ ] **Privacy Protection**
  - Anonymize personal data
  - Don't share sensitive information
  - Comply with privacy laws

- [ ] **Maintenance**
  - Monitor for website changes
  - Update scrapers when needed
  - Document your scraping process

## Red Flags - STOP if:

❌ **Website explicitly prohibits scraping in ToS**
❌ **robots.txt disallows your target pages**
❌ **You're bypassing authentication/paywalls**
❌ **You're collecting personal/sensitive data**
❌ **Scraping could harm the website**
❌ **Data will be used for illegal purposes**

## Example User-Agent

```python
USER_AGENT = 'MyScraperBot/1.0 (+https://mywebsite.com/bot; contact@email.com)'
```

## Example robots.txt Check

```python
from urllib.robotparser import RobotFileParser

def can_scrape(url):
    rp = RobotFileParser()
    rp.set_url(f"{url}/robots.txt")
    rp.read()
    return rp.can_fetch("*", url)
```

## Resources

- [robots.txt documentation](https://www.robotstxt.org/)
- [GDPR overview](https://gdpr.eu/)
- [CCPA information](https://oag.ca.gov/privacy/ccpa)

## Notes

Remember: **Just because you can scrape, doesn't mean you should.**

Always prioritize:
1. Legal compliance
2. Ethical considerations
3. Respect for website owners
4. Privacy protection

When in doubt, contact the website owner or seek legal advice.
