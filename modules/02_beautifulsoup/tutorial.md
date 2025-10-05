# Module 2: Advanced BeautifulSoup4 - Tutorial

## Welcome to Module 2! 🎯

Now that you understand the basics, let's dive into advanced BeautifulSoup techniques for efficient web scraping.

## Part 1: CSS Selectors Mastery

CSS selectors provide a powerful way to find elements precisely.

### Basic CSS Selectors Review

```python
from bs4 import BeautifulSoup

html = """
<div class="container">
    <h1 id="title">My Page</h1>
    <p class="intro">Introduction text</p>
    <p class="content">Main content</p>
</div>
"""

soup = BeautifulSoup(html, 'html.parser')

# Select by tag
p_tags = soup.select('p')

# Select by class
intro = soup.select_one('.intro')

# Select by ID
title = soup.select_one('#title')
```

### Advanced Selectors

#### 1. Attribute Selectors

```python
# Element with specific attribute
links = soup.select('a[href]')

# Element with specific attribute value
external = soup.select('a[target="_blank"]')

# Attribute contains value
products = soup.select('[data-category*="electronics"]')

# Attribute starts with
images = soup.select('img[src^="https://"]')

# Attribute ends with
pdfs = soup.select('a[href$=".pdf"]')
```

#### 2. Combinators

```python
# Descendant (space) - any level deep
items = soup.select('div.container p')

# Direct child (>) - immediate child only
direct_children = soup.select('ul > li')

# Adjacent sibling (+) - immediately after
next_sibling = soup.select('h2 + p')

# General sibling (~) - any following sibling
all_siblings = soup.select('h2 ~ p')
```

#### 3. Pseudo-classes

```python
# First/Last child
first_item = soup.select('li:first-child')
last_item = soup.select('li:last-child')

# Nth child
third_item = soup.select('li:nth-child(3)')
even_items = soup.select('li:nth-child(even)')
odd_items = soup.select('li:nth-child(odd)')

# Not selector
not_featured = soup.select('div.product:not(.featured)')
```

## Part 2: Tree Navigation

BeautifulSoup allows you to navigate the parse tree in multiple ways.

### Parent, Children, and Siblings

```python
# Get parent
element = soup.find('p', class_='price')
parent = element.parent
print(f"Parent tag: {parent.name}")

# Get all parents
for parent in element.parents:
    print(f"Ancestor: {parent.name}")

# Get children
div = soup.find('div', class_='product')
for child in div.children:
    if child.name:  # Skip text nodes
        print(f"Child: {child.name}")

# Get all descendants
for descendant in div.descendants:
    if descendant.name:
        print(f"Descendant: {descendant.name}")

# Get siblings
element = soup.find('h2')
next_sib = element.next_sibling
prev_sib = element.previous_sibling

# Get all next siblings
for sibling in element.next_siblings:
    if sibling.name:
        print(f"Next sibling: {sibling.name}")
```

### String Navigation

```python
# Get next/previous elements (including text)
element = soup.find('h2')
next_elem = element.next_element
prev_elem = element.previous_element

# Get all next elements
for elem in element.next_elements:
    if isinstance(elem, str):
        print(f"Text: {elem.strip()}")
```

## Part 3: find() vs find_all() vs select()

Understanding when to use each method:

```python
# find() - returns first match or None
first_link = soup.find('a')

# find_all() - returns list of all matches
all_links = soup.find_all('a')

# select_one() - returns first match or None (CSS)
first_product = soup.select_one('.product')

# select() - returns list of all matches (CSS)
all_products = soup.select('.product')

# Tip: select() is often more readable for complex selections
# find_all() is faster for simple tag/class searches
```

## Part 4: Working with Tables

Tables are common in web data. Here's how to extract them efficiently:

```python
def extract_table(table):
    """Extract table data into a list of dictionaries."""
    
    # Get headers
    headers = []
    for th in table.find_all('th'):
        headers.append(th.get_text().strip())
    
    # Get rows
    rows = []
    for tr in table.find_all('tr')[1:]:  # Skip header row
        row_data = {}
        cells = tr.find_all('td')
        
        for i, cell in enumerate(cells):
            if i < len(headers):
                row_data[headers[i]] = cell.get_text().strip()
        
        if row_data:  # Only add non-empty rows
            rows.append(row_data)
    
    return rows

# Usage
table = soup.find('table', id='data-table')
data = extract_table(table)

for row in data:
    print(row)
```

### Converting Table to Pandas DataFrame

```python
import pandas as pd

def table_to_dataframe(table):
    """Convert HTML table to pandas DataFrame."""
    
    # Extract data
    data = extract_table(table)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    return df

# Usage
df = table_to_dataframe(table)
print(df)
df.to_csv('table_data.csv', index=False)
```

## Part 5: Handling Nested Structures

Extract data from complex, nested HTML:

```python
# Example: Product listings with nested info
def extract_product_details(product_div):
    """Extract all details from a product element."""
    
    details = {}
    
    # Title
    title_elem = product_div.select_one('h3.product-title')
    details['title'] = title_elem.get_text().strip() if title_elem else None
    
    # Price (might be in nested spans)
    price_elem = product_div.select_one('.price .amount')
    if not price_elem:
        price_elem = product_div.select_one('.price')
    details['price'] = price_elem.get_text().strip() if price_elem else None
    
    # Nested attributes
    specs = {}
    spec_list = product_div.select('.specs li')
    for spec in spec_list:
        key = spec.select_one('.spec-name')
        value = spec.select_one('.spec-value')
        if key and value:
            specs[key.get_text().strip()] = value.get_text().strip()
    
    details['specifications'] = specs
    
    return details

# Usage
products = soup.select('div.product')
for product in products:
    details = extract_product_details(product)
    print(details)
```

## Part 6: Text Extraction and Cleaning

### Getting Clean Text

```python
# Basic text extraction
text = element.get_text()

# Remove extra whitespace
clean_text = ' '.join(element.get_text().split())

# Get text with custom separator
text_with_pipes = element.get_text(separator='|')

# Strip specific characters
text = element.get_text().strip('$€£')

# Get only direct text (no descendants)
direct_text = element.find(text=True, recursive=False)
```

### Using Regular Expressions

```python
import re

# Find elements with text matching pattern
prices = soup.find_all(string=re.compile(r'\$\d+'))

# Find elements by attribute pattern
products = soup.find_all('div', {'data-id': re.compile(r'prod-\d+')})

# Extract using regex
price_text = "$123.45"
price_value = re.search(r'\d+\.?\d*', price_text).group()
```

## Part 7: Different Parsers

BeautifulSoup supports multiple parsers, each with pros and cons:

```python
# html.parser (built-in, no dependencies)
soup = BeautifulSoup(html, 'html.parser')

# lxml (fastest, needs installation)
soup = BeautifulSoup(html, 'lxml')

# html5lib (most forgiving, slowest)
soup = BeautifulSoup(html, 'html5lib')

# XML parser (for XML documents)
soup = BeautifulSoup(xml_content, 'xml')
```

**When to use each:**
- `html.parser`: Default choice, no extra dependencies
- `lxml`: When speed matters and HTML is well-formed
- `html5lib`: When dealing with malformed HTML
- `xml`: For XML documents (RSS feeds, sitemaps)

## Part 8: Handling Encoding Issues

```python
# Detect encoding
import chardet

raw_data = response.content
detected = chardet.detect(raw_data)
encoding = detected['encoding']

# Use detected encoding
html = raw_data.decode(encoding)
soup = BeautifulSoup(html, 'html.parser')

# Or let BeautifulSoup handle it
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

# Handle encoding errors
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8', exclude_encodings=['ascii'])
```

## Part 9: Practical Examples

### Example 1: Scraping a Complex Product Page

```python
def scrape_product_page(url):
    """Scrape detailed product information."""
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    product = {}
    
    # Basic info
    product['title'] = soup.select_one('h1.product-name').get_text().strip()
    product['price'] = soup.select_one('.price-current').get_text().strip()
    
    # Nested rating info
    rating_elem = soup.select_one('.rating-stars')
    if rating_elem:
        product['rating'] = rating_elem.get('data-rating')
        product['reviews'] = rating_elem.get('data-review-count')
    
    # Specifications table
    specs = {}
    spec_rows = soup.select('table.specs tr')
    for row in spec_rows:
        key = row.select_one('th').get_text().strip()
        value = row.select_one('td').get_text().strip()
        specs[key] = value
    product['specifications'] = specs
    
    # Images (multiple)
    images = []
    for img in soup.select('.product-images img'):
        images.append(img.get('src'))
    product['images'] = images
    
    return product
```

### Example 2: Extracting Article Content

```python
def extract_article(url):
    """Extract article content from news site."""
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    article = {}
    
    # Title
    article['title'] = soup.select_one('h1.article-title').get_text().strip()
    
    # Author and date
    byline = soup.select_one('.article-byline')
    article['author'] = byline.select_one('.author').get_text().strip()
    article['date'] = byline.select_one('.date').get_text().strip()
    
    # Content (combine all paragraphs)
    content_div = soup.select_one('div.article-content')
    paragraphs = content_div.select('p')
    article['content'] = '\n\n'.join([p.get_text().strip() for p in paragraphs])
    
    # Tags
    tags = [tag.get_text().strip() for tag in soup.select('.article-tags a')]
    article['tags'] = tags
    
    return article
```

## Part 10: Performance Tips

### Tip 1: Limit Your Search Scope

```python
# Instead of searching entire document
prices = soup.find_all('span', class_='price')

# Search within a specific container
container = soup.find('div', class_='products')
prices = container.find_all('span', class_='price')
```

### Tip 2: Use Appropriate Methods

```python
# Faster for simple searches
links = soup.find_all('a')

# Better for complex CSS selections
specific_links = soup.select('div.container > ul > li > a.external')
```

### Tip 3: Compile Regular Expressions

```python
import re

# Compile once, use many times
price_pattern = re.compile(r'\$\d+\.?\d*')

prices = soup.find_all(string=price_pattern)
```

## Practice Exercises

### Exercise 1: Advanced Selectors
Extract all product prices from a nested structure using CSS selectors.

### Exercise 2: Table Extraction
Convert a complex HTML table to a CSV file.

### Exercise 3: Article Scraper
Build a scraper that extracts articles with nested metadata.

## Next Steps

Great job! You've mastered advanced BeautifulSoup techniques. 

**Next**: Move to Module 3 to learn Selenium for dynamic content!

## Quick Reference

```python
# CSS Selectors
.select('.class')           # By class
.select('#id')             # By ID
.select('tag')             # By tag
.select('[attr]')          # Has attribute
.select('[attr="val"]')    # Attribute equals
.select('parent > child')  # Direct child
.select('ancestor desc')   # Descendant

# Navigation
.parent                    # Parent element
.children                  # Direct children
.descendants              # All descendants
.next_sibling             # Next sibling
.previous_sibling         # Previous sibling

# Text
.get_text()               # Extract text
.string                   # Direct text only
.stripped_strings         # Iterator of stripped text
```
