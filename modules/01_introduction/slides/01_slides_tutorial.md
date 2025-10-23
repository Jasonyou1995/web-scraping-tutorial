---
theme: default
title: Web Scraping Basics
transition: slide-left
---

# Web Scraping Basics

Introduction to extracting data from the web

---
layout: center
---

# The Request-Response Cycle

<v-clicks>

- Browser sends **HTTP request** to server
- Server processes the request
- Server sends back **HTTP response** with HTML
- Browser renders the HTML

</v-clicks>

<div v-click class="mt-8 text-center opacity-75">
Web scraping mimics this process programmatically
</div>

---

# Your First HTTP Request

```python {all|1|4|7|10-11|all}
import requests

# URL to scrape
url = "https://example.com"

# Make the request
response = requests.get(url)

# Check status
print(f"Status Code: {response.status_code}")
print(f"Content Length: {len(response.content)} bytes")
```

<div class="mt-8">
<v-clicks>

- **200**: Success ✅
- **404**: Page not found ❌
- **403**: Forbidden ❌

</v-clicks>
</div>

---

# Parsing HTML with BeautifulSoup

```python {all|2|8-9|11-12|14|all}
import requests
from bs4 import BeautifulSoup

# Get the page
url = "https://example.com"
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Get page title (there are many ways to find this)
title = soup.find(’title_tag’, class_=’title_class_name’).get_text()

print(f"Page Title: {title}")
```

---

# HTML Structure

```html
<div class="product">
    <h2>Product Name</h2>
    <p class="price">$19.99</p>
    <a href="/product/123">View Details</a>
</div>
```

<div class="mt-8">

- **Tag**: `<div>`, `<h2>`, `<p>`, `<a>`
- **Attribute**: `class="product"`, `href="/product/123"`
- **Content**: "Product Name", "$19.99"

</div>

---

# Finding Elements

## Method 1: `find()` - First Match

```python
# Find first <h1> tag
heading = soup.find('h1')
print(heading.get_text())

# Find first element with specific class
element = soup.find('div', class_='product')
print(element.get_text())
```

---

# Finding Elements

## Method 2: `find_all()` - All Matches

```python
# Find all <p> tags
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.get_text())

# Find all links
links = soup.find_all('a', href=True)
for link in links:
    print(link['href'])
```

---

# Finding Elements

## Method 3: CSS Selectors

```python
# Select by class
products = soup.select('.product')

# Select by ID
header = soup.select_one('#header')

# Complex selectors
prices = soup.select('div.product > p.price')
```

---

# Extracting Data

<div class="grid grid-cols-2 gap-8">
<div>

### Getting Text

```python
element = soup.find('h1')
text = element.get_text()

# Remove whitespace
text = element.get_text().strip()
```

</div>
<div>

### Getting Attributes

```python
link = soup.find('a')
url = link.get('href')
# or
url = link['href']

div = soup.find('div')
class_name = div.get('class')
```

</div>
</div>

---

# Practical Example: Product Scraper

```python {all|1-2|5-6|9|12|15-22|all}
import requests
from bs4 import BeautifulSoup

# Use local file for practice
with open('data/sample_pages/sample_products.html', 'r') as f:
    html_content = f.read()

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all products
products = soup.find_all('div', class_='product')

print(f"Found {len(products)} products:\n")

for product in products:
    # Extract data
    title = product.find('h3', class_='product-title').get_text()
    price = product.find('p', class_='price').get_text()
    
    print(f"Product: {title}")
    print(f"Price: {price}")
```

---

# Saving Data to CSV

```python {all|1|4-8|11-13|all}
import csv

# Prepare data
data = [
    ['Product', 'Price', 'Rating'],
    ['Laptop Pro 15', '$1,299.99', '4.5'],
    ['Wireless Mouse', '$29.99', '5.0']
]

# Save to CSV
with open('products.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

---

# Error Handling

```python {all|5|7|12|14-15,17|all}
import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.find('h1')
        if title:
            print(f"Title: {title.get_text()}")
            
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
```

---
layout: two-cols
---

# Best Practices

## DO ✅

- Start with simple websites
- Add delays: `time.sleep(1)`
- Use try-except handling
- Test on local HTML first
- Read terms of service

::right::

## DON'T ❌

- Make rapid requests
- Scrape private data
- Ignore error messages
- Assume structure stays same

---
layout: center
---

# You Now Know How To:

<v-clicks>

- ✅ Make HTTP requests
- ✅ Parse HTML with BeautifulSoup
- ✅ Find and extract elements
- ✅ Save data to files
- ✅ Handle errors properly

</v-clicks>

<div v-click class="mt-12 text-center text-2xl">
Happy Scraping! 🕷️
</div>
