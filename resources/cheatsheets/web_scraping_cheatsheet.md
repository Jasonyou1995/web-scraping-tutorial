# Web Scraping Cheat Sheet

## Quick Reference for Common Tasks

### 1. Making HTTP Requests

```python
import requests

# Basic GET request
response = requests.get('https://example.com')

# With headers
headers = {'User-Agent': 'My Scraper 1.0'}
response = requests.get('https://example.com', headers=headers)

# With timeout
response = requests.get('https://example.com', timeout=10)

# POST request
data = {'key': 'value'}
response = requests.post('https://example.com/api', data=data)
```

### 2. BeautifulSoup Basics

```python
from bs4 import BeautifulSoup

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find elements
element = soup.find('div', class_='my-class')
elements = soup.find_all('a', href=True)

# CSS selectors
element = soup.select_one('.my-class')
elements = soup.select('div.class > p')

# Extract data
text = element.get_text()
attribute = element.get('href')
```

### 3. Common CSS Selectors

```python
# By tag
soup.select('p')

# By class
soup.select('.class-name')
soup.select('div.class-name')

# By ID
soup.select('#element-id')

# By attribute
soup.select('[data-id="123"]')

# Combinators
soup.select('div > p')        # Direct child
soup.select('div p')          # Descendant
soup.select('div + p')        # Adjacent sibling
soup.select('div ~ p')        # General sibling

# Multiple selectors
soup.select('h1, h2, h3')
```

### 4. Selenium WebDriver

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
driver = webdriver.Chrome()
driver.get('https://example.com')

# Find elements
element = driver.find_element(By.ID, 'element-id')
elements = driver.find_elements(By.CLASS_NAME, 'class-name')

# Wait for element
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'element-id')))

# Interact
element.click()
element.send_keys('text')

# Cleanup
driver.quit()
```

### 5. XPath Selectors

```python
# Basic XPath
driver.find_element(By.XPATH, '//div[@class="my-class"]')

# Common patterns
'//tag'                          # All tags
'//tag[@attr="value"]'          # Tag with attribute
'//tag[text()="exact text"]'    # Tag with exact text
'//tag[contains(text(), "partial")]'  # Tag containing text
'//tag[@attr]/following-sibling::tag' # Following sibling
'//tag/parent::*'               # Parent element
```

### 6. Scrapy Quick Commands

```bash
# Create project
scrapy startproject myproject

# Generate spider
scrapy genspider myspider example.com

# Run spider
scrapy crawl myspider

# Export data
scrapy crawl myspider -o output.json
scrapy crawl myspider -o output.csv

# Shell for testing
scrapy shell 'https://example.com'
```

### 7. Error Handling

```python
import requests
from requests.exceptions import RequestException

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except RequestException as e:
    print(f"Error: {e}")
```

### 8. Rate Limiting

```python
import time

# Simple delay
time.sleep(2)

# Random delay
import random
delay = random.uniform(1, 3)
time.sleep(delay)
```

### 9. Saving Data

```python
import csv
import json

# Save to CSV
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Header1', 'Header2'])
    writer.writerow(['Value1', 'Value2'])

# Save to JSON
data = {'key': 'value'}
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)

# Pandas
import pandas as pd
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
```

### 10. Common Locators

| Method | Selenium | BeautifulSoup |
|--------|----------|---------------|
| ID | `By.ID, 'id'` | `id='id'` |
| Class | `By.CLASS_NAME, 'class'` | `class_='class'` |
| Tag | `By.TAG_NAME, 'tag'` | `'tag'` |
| CSS | `By.CSS_SELECTOR, 'selector'` | `.select('selector')` |
| XPath | `By.XPATH, 'xpath'` | N/A |

### 11. HTTP Status Codes

- **200**: OK - Success
- **301/302**: Redirect
- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **429**: Too Many Requests
- **500**: Internal Server Error
- **503**: Service Unavailable

### 12. User-Agent Examples

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
```

### 13. robots.txt Checking

```python
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://example.com/robots.txt')
rp.read()
can_fetch = rp.can_fetch('*', 'https://example.com/page')
```

## Quick Tips

✅ **DO:**
- Add delays between requests
- Use proper User-Agent
- Handle errors gracefully
- Respect robots.txt
- Cache during development

❌ **DON'T:**
- Hammer servers with rapid requests
- Ignore error codes
- Scrape private/sensitive data
- Bypass authentication maliciously
