# Module 5: Best Practices & Ethics - Tutorial

## Welcome to Module 5! ⚖️

Learn professional web scraping practices, legal considerations, and how to build ethical, maintainable scrapers.

## Part 1: Legal and Ethical Foundations

### Understanding the Legal Landscape

**Key Principle**: Just because you CAN scrape doesn't mean you SHOULD.

#### Important Legal Concepts

1. **Terms of Service (ToS)**
   - Binding contract between you and website
   - Often prohibits automated access
   - Violation can lead to account termination or legal action

2. **robots.txt**
   - Not legally binding but shows intent
   - Industry standard for crawler behavior
   - Respecting it shows good faith

3. **Copyright Law**
   - Scraped content may be copyrighted
   - Fair use has limits
   - Don't republish without permission

4. **Privacy Laws**
   - **GDPR** (Europe): Strict personal data protection
   - **CCPA** (California): Consumer privacy rights
   - Scraping personal data requires consent

5. **Computer Fraud Laws**
   - **CFAA** (US): Unauthorized access is illegal
   - "Exceeding authorized access" is debated
   - Recent cases favor scraping public data

### Notable Legal Cases

**HiQ Labs v. LinkedIn (2022)**
- LinkedIn tried to block HiQ from scraping public profiles
- Court sided with HiQ for public data
- BUT: Private/protected data is different

**Takeaways:**
- Public data scraping is generally OK
- Respect technical barriers (login walls, CAPTCHAs)
- Don't cause harm to the website
- Follow robots.txt when possible

## Part 2: robots.txt Deep Dive

### Understanding robots.txt

Located at `https://example.com/robots.txt`

```
User-agent: *
Disallow: /admin/
Disallow: /private/
Crawl-delay: 2

User-agent: Googlebot
Disallow: /temp/

Sitemap: https://example.com/sitemap.xml
```

### Parsing robots.txt

```python
from urllib.robotparser import RobotFileParser

def check_robots_txt(url, user_agent='*'):
    """Check if URL can be scraped according to robots.txt."""
    
    from urllib.parse import urlparse
    
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    robots_url = f"{base_url}/robots.txt"
    
    rp = RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    
    # Check if allowed
    can_fetch = rp.can_fetch(user_agent, url)
    
    # Get crawl delay
    crawl_delay = rp.crawl_delay(user_agent)
    
    return {
        'can_fetch': can_fetch,
        'crawl_delay': crawl_delay,
        'robots_url': robots_url
    }

# Usage
result = check_robots_txt('https://example.com/page', 'MyBot')
print(f"Can fetch: {result['can_fetch']}")
print(f"Crawl delay: {result['crawl_delay']} seconds")
```

### Respecting Crawl-Delay

```python
import time
from urllib.robotparser import RobotFileParser

class PoliteScraperrobotsparser import RobotFileParser

class PoliteScraper:
    def __init__(self, user_agent='MyBot'):
        self.user_agent = user_agent
        self.robot_parsers = {}
        self.last_request_time = {}
    
    def can_fetch(self, url):
        """Check robots.txt and enforce crawl delay."""
        from urllib.parse import urlparse
        
        parsed = urlparse(url)
        domain = parsed.netloc
        
        # Load robots.txt if not cached
        if domain not in self.robot_parsers:
            rp = RobotFileParser()
            rp.set_url(f"{parsed.scheme}://{domain}/robots.txt")
            rp.read()
            self.robot_parsers[domain] = rp
        
        # Check if allowed
        if not self.robot_parsers[domain].can_fetch(self.user_agent, url):
            return False
        
        # Enforce crawl delay
        crawl_delay = self.robot_parsers[domain].crawl_delay(self.user_agent)
        if crawl_delay:
            if domain in self.last_request_time:
                elapsed = time.time() - self.last_request_time[domain]
                if elapsed < crawl_delay:
                    time.sleep(crawl_delay - elapsed)
        
        self.last_request_time[domain] = time.time()
        return True
```

## Part 3: Rate Limiting Strategies

### Simple Rate Limiting

```python
import time
import random

# Fixed delay
time.sleep(2)

# Random delay (more natural)
delay = random.uniform(1, 3)
time.sleep(delay)

# Exponential backoff for errors
def exponential_backoff(attempt, base_delay=1, max_delay=60):
    delay = min(base_delay * (2 ** attempt), max_delay)
    time.sleep(delay)

# Usage
for attempt in range(5):
    try:
        response = requests.get(url)
        response.raise_for_status()
        break
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:  # Too many requests
            exponential_backoff(attempt)
```

### Token Bucket Algorithm

```python
import time
from collections import deque

class RateLimiter:
    """Token bucket rate limiter."""
    
    def __init__(self, rate, capacity):
        """
        Args:
            rate: Tokens per second
            capacity: Maximum tokens
        """
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_update = time.time()
    
    def acquire(self):
        """Wait until a token is available."""
        while True:
            now = time.time()
            elapsed = now - self.last_update
            
            # Add tokens based on elapsed time
            self.tokens = min(
                self.capacity,
                self.tokens + elapsed * self.rate
            )
            self.last_update = now
            
            if self.tokens >= 1:
                self.tokens -= 1
                return
            
            # Wait for next token
            sleep_time = (1 - self.tokens) / self.rate
            time.sleep(sleep_time)

# Usage: 10 requests per minute
limiter = RateLimiter(rate=10/60, capacity=10)

for url in urls:
    limiter.acquire()
    response = requests.get(url)
```

## Part 4: Error Handling and Resilience

### Comprehensive Error Handling

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_session():
    """Create session with retry logic."""
    
    session = requests.Session()
    
    # Retry strategy
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST"]
    )
    
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    return session

def safe_request(url, session=None, timeout=30):
    """Make request with comprehensive error handling."""
    
    if session is None:
        session = create_session()
    
    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()
        return response
        
    except requests.exceptions.Timeout:
        logger.error(f"Timeout error for {url}")
        
    except requests.exceptions.TooManyRedirects:
        logger.error(f"Too many redirects for {url}")
        
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error {e.response.status_code} for {url}")
        
    except requests.exceptions.ConnectionError:
        logger.error(f"Connection error for {url}")
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error for {url}: {e}")
    
    return None
```

### Handling Specific HTTP Errors

```python
def handle_http_response(response):
    """Handle different HTTP status codes."""
    
    if response.status_code == 200:
        return response
    
    elif response.status_code == 404:
        logger.warning(f"Page not found: {response.url}")
        return None
    
    elif response.status_code == 403:
        logger.error(f"Access forbidden: {response.url}")
        # Maybe you need better headers or authentication
        return None
    
    elif response.status_code == 429:
        # Rate limited
        retry_after = response.headers.get('Retry-After')
        if retry_after:
            logger.info(f"Rate limited. Retry after {retry_after}s")
            time.sleep(int(retry_after))
        else:
            time.sleep(60)  # Wait 1 minute
        return 'retry'
    
    elif response.status_code >= 500:
        # Server error - retry
        logger.error(f"Server error {response.status_code}")
        return 'retry'
    
    else:
        logger.warning(f"Unexpected status {response.status_code}")
        return None
```

## Part 5: User-Agent Best Practices

### Good User-Agent

```python
# Identify your bot clearly
USER_AGENT = 'MyScraperBot/1.0 (+https://mywebsite.com/bot-info; contact@email.com)'

# Include purpose and contact
USER_AGENT = 'ResearchBot/2.0 (University Study; research@university.edu)'

# For development/testing
USER_AGENT = 'Mozilla/5.0 (compatible; DevBot/0.1; +http://localhost/info)'
```

### User-Agent Rotation (Use Carefully!)

```python
from fake_useragent import UserAgent

# Only if absolutely necessary
ua = UserAgent()

headers = {
    'User-Agent': ua.random
}

# Better: Use a consistent, descriptive User-Agent
headers = {
    'User-Agent': 'MyBot/1.0 (+https://mysite.com)'
}
```

## Part 6: Logging and Monitoring

### Proper Logging

```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file='scraper.log'):
    """Configure logging for scraper."""
    
    # Create logger
    logger = logging.getLogger('scraper')
    logger.setLevel(logging.DEBUG)
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Usage
logger = setup_logging()

logger.info(f"Starting scrape of {url}")
logger.debug(f"Response status: {response.status_code}")
logger.warning(f"Missing data for {item_id}")
logger.error(f"Failed to parse {url}: {error}")
```

### Monitoring Scraper Health

```python
class ScraperMetrics:
    """Track scraper metrics."""
    
    def __init__(self):
        self.requests_made = 0
        self.requests_failed = 0
        self.items_scraped = 0
        self.start_time = time.time()
    
    def record_request(self, success=True):
        self.requests_made += 1
        if not success:
            self.requests_failed += 1
    
    def record_item(self):
        self.items_scraped += 1
    
    def get_stats(self):
        elapsed = time.time() - self.start_time
        success_rate = (
            (self.requests_made - self.requests_failed) / 
            self.requests_made * 100
            if self.requests_made > 0 else 0
        )
        
        return {
            'requests': self.requests_made,
            'failed': self.requests_failed,
            'success_rate': f"{success_rate:.2f}%",
            'items': self.items_scraped,
            'duration': f"{elapsed:.2f}s",
            'items_per_second': self.items_scraped / elapsed if elapsed > 0 else 0
        }

# Usage
metrics = ScraperMetrics()

for url in urls:
    response = requests.get(url)
    metrics.record_request(response.status_code == 200)
    
    if response.status_code == 200:
        items = parse_page(response)
        metrics.record_item()

print(metrics.get_stats())
```

## Part 7: Configuration Management

### Using Environment Variables

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration from environment
CONFIG = {
    'api_key': os.getenv('API_KEY'),
    'db_url': os.getenv('DATABASE_URL'),
    'max_workers': int(os.getenv('MAX_WORKERS', 4)),
    'rate_limit': float(os.getenv('RATE_LIMIT', 1.0)),
    'user_agent': os.getenv('USER_AGENT', 'DefaultBot/1.0')
}

# .env file:
# API_KEY=your_key_here
# DATABASE_URL=postgresql://localhost/scraper
# MAX_WORKERS=8
# RATE_LIMIT=2.0
```

### Configuration Class

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class ScraperConfig:
    """Scraper configuration."""
    
    base_url: str
    user_agent: str = 'MyBot/1.0'
    rate_limit: float = 1.0
    timeout: int = 30
    max_retries: int = 3
    respect_robots_txt: bool = True
    cache_enabled: bool = False
    output_format: str = 'json'
    
    @classmethod
    def from_env(cls):
        """Load config from environment."""
        return cls(
            base_url=os.getenv('BASE_URL'),
            user_agent=os.getenv('USER_AGENT', 'MyBot/1.0'),
            rate_limit=float(os.getenv('RATE_LIMIT', 1.0)),
            # ... etc
        )
```

## Part 8: Data Validation

### Validating Scraped Data

```python
from typing import Optional
from pydantic import BaseModel, validator, HttpUrl

class Product(BaseModel):
    """Product data model with validation."""
    
    name: str
    price: float
    url: HttpUrl
    rating: Optional[float] = None
    
    @validator('price')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Price must be positive')
        return v
    
    @validator('rating')
    def rating_in_range(cls, v):
        if v is not None and not (0 <= v <= 5):
            raise ValueError('Rating must be between 0 and 5')
        return v

# Usage
try:
    product = Product(
        name="Laptop",
        price=999.99,
        url="https://example.com/laptop",
        rating=4.5
    )
except ValueError as e:
    logger.error(f"Invalid product data: {e}")
```

## Part 9: Testing Your Scraper

### Unit Testing

```python
import unittest
from unittest.mock import Mock, patch

class TestScraper(unittest.TestCase):
    
    def test_parse_price(self):
        """Test price parsing."""
        self.assertEqual(parse_price("$99.99"), 99.99)
        self.assertEqual(parse_price("€50,00"), 50.00)
    
    @patch('requests.get')
    def test_fetch_page(self, mock_get):
        """Test page fetching with mock."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>Test</body></html>"
        mock_get.return_value = mock_response
        
        response = fetch_page('http://example.com')
        self.assertEqual(response.status_code, 200)
    
    def test_robots_txt_parsing(self):
        """Test robots.txt compliance."""
        can_fetch = check_robots_txt('https://example.com/page')
        self.assertTrue(can_fetch)

if __name__ == '__main__':
    unittest.main()
```

## Part 10: Deployment Checklist

### Pre-Deployment

- [ ] Test on sample data
- [ ] Verify robots.txt compliance
- [ ] Implement rate limiting
- [ ] Add error handling
- [ ] Set up logging
- [ ] Configure monitoring
- [ ] Review legal compliance
- [ ] Document code
- [ ] Create deployment guide

### Production Settings

```python
PRODUCTION_CONFIG = {
    'respect_robots_txt': True,
    'rate_limit': 2.0,  # 2 seconds between requests
    'timeout': 30,
    'max_retries': 3,
    'cache_enabled': False,
    'log_level': 'INFO',
    'alert_on_errors': True,
    'max_concurrent_requests': 4
}
```

## Part 11: Ethical Scraping Principles

### The Golden Rules

1. **Respect**: Respect website owners and their resources
2. **Transparency**: Identify your bot clearly
3. **Politeness**: Don't overwhelm servers
4. **Privacy**: Don't scrape personal data without consent
5. **Legality**: Follow laws and terms of service
6. **Attribution**: Credit data sources appropriately

### Ethical Decision Framework

Ask yourself:
1. Is this data publicly available?
2. Does scraping violate ToS?
3. Could this harm the website?
4. Am I respecting privacy?
5. Would I want my site scraped this way?
6. Is there an official API I should use instead?

If ANY answer raises concerns, reconsider your approach.

## Congratulations! 🎉

You've completed the Web Scraping Tutorial!

### You Now Know:
- Legal and ethical considerations
- How to respect robots.txt
- Rate limiting strategies
- Error handling best practices
- Logging and monitoring
- Configuration management
- Data validation
- Testing strategies
- Deployment practices

### Next Steps:
- Build real-world projects
- Contribute to open source
- Stay updated on legal developments
- Join scraping communities
- Always scrape responsibly!

**Happy (and Ethical) Scraping!** 🕷️⚖️
