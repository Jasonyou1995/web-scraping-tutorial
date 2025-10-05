# Troubleshooting Guide

## Common Issues and Solutions

### 1. Installation Issues

#### Problem: `pip install` fails
**Solution:**
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Try with --user flag
pip install --user requests beautifulsoup4

# Use virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Problem: Selenium WebDriver not found
**Solution:**
```bash
# Install webdriver-manager
pip install webdriver-manager

# Use in code:
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

### 2. Request Errors

#### Problem: `ConnectionError` or `Timeout`
**Solution:**
```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Setup retry strategy
session = requests.Session()
retry = Retry(total=3, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Use session
response = session.get(url, timeout=10)
```

#### Problem: 403 Forbidden or 401 Unauthorized
**Solution:**
```python
# Add proper headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
}
response = requests.get(url, headers=headers)
```

#### Problem: 429 Too Many Requests
**Solution:**
```python
import time
import random

# Add random delays
for url in urls:
    response = requests.get(url)
    delay = random.uniform(2, 5)
    time.sleep(delay)
```

### 3. Parsing Issues

#### Problem: `AttributeError: 'NoneType' object has no attribute`
**Solution:**
```python
# Always check if element exists
element = soup.find('div', class_='my-class')
if element:
    text = element.get_text()
else:
    text = "Not found"

# Or use try-except
try:
    text = soup.find('div', class_='my-class').get_text()
except AttributeError:
    text = "Not found"
```

#### Problem: Cannot find element with BeautifulSoup
**Solutions:**
```python
# 1. Check HTML structure first
print(soup.prettify())

# 2. Try different parsers
soup = BeautifulSoup(html, 'lxml')  # Instead of 'html.parser'

# 3. Check for dynamic content (use Selenium instead)

# 4. Verify selector
# Use browser DevTools to test CSS selectors
```

#### Problem: Encoding issues (weird characters)
**Solution:**
```python
# Specify encoding
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

# Or detect encoding
import chardet
encoding = chardet.detect(response.content)['encoding']
html = response.content.decode(encoding)
```

### 4. Selenium Issues

#### Problem: Element not found or `NoSuchElementException`
**Solutions:**
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Wait for element to appear
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'element-id')))

# Wait for element to be clickable
element = wait.until(EC.element_to_be_clickable((By.ID, 'element-id')))
```

#### Problem: `StaleElementReferenceException`
**Solution:**
```python
# Re-locate element after page changes
def safe_click(driver, by, value):
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            element = driver.find_element(by, value)
            element.click()
            break
        except StaleElementReferenceException:
            if attempt == max_attempts - 1:
                raise
            time.sleep(1)
```

#### Problem: Chrome/Firefox not opening
**Solution:**
```python
# Use headless mode
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
```

### 5. Scrapy Issues

#### Problem: Spider not crawling
**Solution:**
```python
# Check robots.txt setting
# In settings.py
ROBOTSTXT_OBEY = False  # Only if you have permission

# Verify start_urls
class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://example.com']  # Make sure URL is correct
    
    def parse(self, response):
        print(f"Crawled: {response.url}")  # Debug output
```

#### Problem: Data not exporting
**Solution:**
```bash
# Use correct format
scrapy crawl myspider -o output.json
scrapy crawl myspider -o output.csv
scrapy crawl myspider -o output.xml

# Enable item pipeline in settings.py
ITEM_PIPELINES = {
    'myproject.pipelines.MyPipeline': 300,
}
```

### 6. Data Issues

#### Problem: Duplicate data
**Solution:**
```python
# Use set to remove duplicates
unique_items = list(set(items))

# Or in Scrapy, use DuplicatesPipeline
# In pipelines.py
class DuplicatesPipeline:
    def __init__(self):
        self.ids_seen = set()
    
    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem(f"Duplicate: {item['id']}")
        self.ids_seen.add(item['id'])
        return item
```

#### Problem: Missing or incomplete data
**Solution:**
```python
# Use default values
def safe_extract(element, selector, default='N/A'):
    try:
        return element.select_one(selector).get_text().strip()
    except:
        return default

# Or in Scrapy
title = response.css('h1::text').get(default='No title')
```

### 7. Performance Issues

#### Problem: Scraper is too slow
**Solutions:**
```python
# 1. Use concurrent requests in Scrapy
# In settings.py
CONCURRENT_REQUESTS = 16
DOWNLOAD_DELAY = 1

# 2. Use asyncio with aiohttp
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

# 3. Use multiprocessing for CPU-bound tasks
from multiprocessing import Pool

def process_page(url):
    # Your scraping logic
    pass

with Pool(processes=4) as pool:
    results = pool.map(process_page, urls)
```

### 8. JavaScript/AJAX Issues

#### Problem: Content not appearing in requests
**Solution:**
```python
# Use Selenium for JavaScript content
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url)

# Wait for JavaScript to load
import time
time.sleep(3)

# Or use explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'dynamic-content')))
```

### 9. Memory Issues

#### Problem: Memory usage too high
**Solutions:**
```python
# 1. Process data in chunks
def process_in_chunks(data, chunk_size=1000):
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i+chunk_size]
        yield chunk

# 2. Clear browser cache in Selenium
driver.execute_cdp_cmd('Network.clearBrowserCache', {})

# 3. Use generators instead of lists
def scrape_pages(urls):
    for url in urls:
        response = requests.get(url)
        yield parse_page(response)
```

### 10. Debugging Tips

```python
# 1. Print response content
print(response.text[:1000])

# 2. Save HTML for inspection
with open('debug.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

# 3. Use logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug(f"Processing URL: {url}")

# 4. Interactive debugging with pdb
import pdb; pdb.set_trace()

# 5. Selenium screenshot
driver.save_screenshot('debug.png')
```

## Getting Help

1. **Check error messages carefully** - They often tell you exactly what's wrong
2. **Google the error** - Add "python" or library name to your search
3. **Check documentation** - Official docs are your best friend
4. **Use Stack Overflow** - Search existing questions first
5. **Enable verbose logging** - See what's happening under the hood

## Useful Resources

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Scrapy Documentation](https://docs.scrapy.org/)
- [Stack Overflow - web-scraping tag](https://stackoverflow.com/questions/tagged/web-scraping)
