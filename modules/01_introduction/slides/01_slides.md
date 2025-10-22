---
theme: default
background: https://images.unsplash.com/photo-1542831371-29b0f74f9713
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## HTML Fundamentals for Web Scraping
  A comprehensive introduction to HTML for absolute beginners
drawings:
  persist: false
transition: slide-left
title: HTML Fundamentals for Web Scraping
mdc: true
---

# HTML Fundamentals
## For Web Scraping Beginners

Understanding the building blocks of web pages

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: two-cols
---

# What is HTML?

HTML = **H**yper**T**ext **M**arkup **L**anguage

- The backbone of every webpage
- A markup language, not programming
- Describes the structure and content
- Made of **elements** (tags)

::right::

<div class="mt-8">

```html {monaco}
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello World!</h1>
    <p>This is HTML!</p>
  </body>
</html>
```

<div class="mt-4 text-sm opacity-75">
Every webpage you scrape has this structure
</div>

</div>

---
layout: center
class: text-center
---

# Why Learn HTML for Web Scraping?

<div class="grid grid-cols-2 gap-8 mt-12">

<div>
  <h3 class="text-blue-400">🎯 Target Elements</h3>
  <p class="text-sm mt-2">Find exactly what you need</p>
</div>

<div>
  <h3 class="text-green-400">🔍 Understand Structure</h3>
  <p class="text-sm mt-2">Navigate the page hierarchy</p>
</div>

<div>
  <h3 class="text-purple-400">📦 Extract Data</h3>
  <p class="text-sm mt-2">Pull text, links, images</p>
</div>

<div>
  <h3 class="text-red-400">🛠️ Build Better Scrapers</h3>
  <p class="text-sm mt-2">Write robust, maintainable code</p>
</div>

</div>

---

# HTML Anatomy: The Basics

<div class="mt-8">

```html {monaco} {1-3|4|5|6|all}
<!-- This is a complete HTML element -->
<tagname attribute="value">Content Here</tagname>

<p class="intro">Welcome to web scraping!</p>

<a href="https://example.com">Click here</a>
```

</div>

<div class="grid grid-cols-3 gap-4 mt-8">

<div class="border border-blue-500 p-4 rounded">
  <h4 class="text-blue-400 font-bold">Opening Tag</h4>
  <code>&lt;p&gt;</code>
  <p class="text-xs mt-2">Marks the start</p>
</div>

<div class="border border-green-500 p-4 rounded">
  <h4 class="text-green-400 font-bold">Content</h4>
  <code>Welcome...</code>
  <p class="text-xs mt-2">The actual text</p>
</div>

<div class="border border-red-500 p-4 rounded">
  <h4 class="text-red-400 font-bold">Closing Tag</h4>
  <code>&lt;/p&gt;</code>
  <p class="text-xs mt-2">Marks the end</p>
</div>

</div>

---

# HTML Attributes: Adding Information

Attributes provide extra information about elements

<div class="mt-8">

```html {monaco} {1|3|5|7|all}
<div id="header">Unique identifier</div>

<p class="warning highlight">Can have multiple classes</p>

<a href="/products">Link destination</a>

<img src="photo.jpg" alt="Description">

<div data-id="101" data-price="29.99">Custom attributes</div>
```

</div>

<div class="mt-6 p-4 bg-blue-900 bg-opacity-30 rounded">
  <h4 class="text-yellow-300">💡 For Web Scraping:</h4>
  <p class="text-sm mt-2">Attributes help you target specific elements. Class and ID are your best friends!</p>
</div>

---

# The ID Attribute: Unique Identifier

<div class="grid grid-cols-2 gap-8">

<div>

## What is an ID?

- **Unique** identifier for ONE element
- Used for specific targeting
- Denoted with `id="name"`
- Only ONE per page

```html {monaco}
<header id="main-header">
  <h1>My Website</h1>
</header>

<div id="sidebar">
  Navigation content
</div>

<footer id="page-footer">
  Copyright 2024
</footer>
```

</div>

<div>

## How to Target IDs

In Python (BeautifulSoup):

```python {monaco}
# Find by ID
header = soup.find(id='main-header')

# Or using CSS selector
header = soup.select_one('#main-header')

# Extract text
title = header.get_text()
```

<div class="mt-4 p-3 bg-green-900 bg-opacity-30 rounded text-sm">
  <strong>Rule:</strong> Use <code>#</code> for ID in CSS selectors
  <br>
  <code>#main-header</code> → targets the element with id="main-header"
</div>

</div>

</div>

---

# The Class Attribute: Reusable Styles

<div class="grid grid-cols-2 gap-8">

<div>

## What is a Class?

- **Reusable** identifier for multiple elements
- Used for grouping similar items
- Denoted with `class="name"`
- Can have multiple classes

```html {monaco}
<div class="product">
  <h3 class="product-title">Laptop</h3>
  <p class="price highlight">$999</p>
</div>

<div class="product">
  <h3 class="product-title">Mouse</h3>
  <p class="price">$29</p>
</div>

<div class="product featured">
  <h3 class="product-title">Keyboard</h3>
  <p class="price highlight">$89</p>
</div>
```

</div>

<div>

## How to Target Classes

In Python (BeautifulSoup):

```python {monaco}
# Find all elements with class
products = soup.find_all(class_='product')

# Or using CSS selector
products = soup.select('.product')

# Multiple classes
highlights = soup.select('.price.highlight')

# Loop through results
for product in products:
    title = product.find(class_='product-title')
    print(title.get_text())
```

<div class="mt-4 p-3 bg-purple-900 bg-opacity-30 rounded text-sm">
  <strong>Rule:</strong> Use <code>.</code> for class in CSS selectors
  <br>
  <code>.product</code> → targets all elements with class="product"
</div>

</div>

</div>

---

# Common HTML Tags for Web Scraping

<div class="grid grid-cols-2 gap-6 text-sm">

<div>

### Structure Tags

```html {monaco}
<div>    <!-- Generic container -->
<span>   <!-- Inline container -->
<header> <!-- Page header -->
<footer> <!-- Page footer -->
<nav>    <!-- Navigation -->
<main>   <!-- Main content -->
<section><!-- Section of content -->
<article><!-- Independent content -->
```

### Text Tags

```html {monaco}
<h1> to <h6>  <!-- Headings -->
<p>           <!-- Paragraph -->
<strong>      <!-- Important text -->
<em>          <!-- Emphasized text -->
<br>          <!-- Line break -->
```

</div>

<div>

### Data Tags

```html {monaco}
<ul>  <!-- Unordered list -->
<ol>  <!-- Ordered list -->
<li>  <!-- List item -->
<table> <!-- Table -->
<tr>  <!-- Table row -->
<td>  <!-- Table cell -->
<th>  <!-- Table header -->
```

### Link & Media Tags

```html {monaco}
<a href="url">    <!-- Link -->
<img src="url">   <!-- Image -->
<video>           <!-- Video -->
<iframe>          <!-- Embedded content -->
```

</div>

</div>

---

# HTML Hierarchy: Parent, Child, Sibling

Understanding relationships between elements

<div class="grid grid-cols-2 gap-8 mt-4">

<div>

```html {monaco}
<div class="container">          <!-- Parent -->
  
  <h2>Title</h2>                 <!-- Child 1 -->
  
  <p class="intro">              <!-- Child 2 -->
    Welcome to <strong>HTML</strong>  <!-- Grandchild -->
  </p>
  
  <ul class="items">             <!-- Child 3 -->
    <li>Item 1</li>              <!-- Grandchild -->
    <li>Item 2</li>              <!-- Grandchild -->
    <li>Item 3</li>              <!-- Grandchild -->
  </ul>
  
</div>
```

</div>

<div class="text-sm">

### Relationships

- **Parent**: Container element
  - `.container` is parent of `h2`, `p`, `ul`
  
- **Child**: Direct descendant
  - `h2`, `p`, `ul` are children of `.container`
  
- **Sibling**: Same level
  - `h2`, `p`, `ul` are siblings
  
- **Descendant**: Any nested element
  - `strong` and all `li` are descendants

### Why It Matters

```python {monaco}
# Find child elements
container = soup.find(class_='container')
title = container.find('h2')

# Find all descendants
all_li = container.find_all('li')

# Navigate siblings
first_p = soup.find('p')
next_element = first_p.find_next_sibling()
```

</div>

</div>

---

# Real Example: Product Card Structure

Let's dissect a real e-commerce product element

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

```html {monaco}
<div class="product" data-id="101">
  <h3 class="product-title">
    Laptop Pro 15
  </h3>
  
  <p class="price">
    $1,299.99
  </p>
  
  <p class="rating">
    ★★★★☆ (4.5/5) - 234 reviews
  </p>
  
  <p class="description">
    High-performance laptop 
    with 16GB RAM and 512GB SSD
  </p>
  
  <p class="stock">
    In Stock
  </p>
  
  <a href="/product/101" 
     class="product-link">
    View Details
  </a>
</div>
```

</div>

<div class="text-sm">

### Element Breakdown

<div class="space-y-3">

<div class="p-2 bg-blue-900 bg-opacity-20 rounded">
  <code>&lt;div class="product"&gt;</code>
  <p class="text-xs mt-1">Container for entire product</p>
</div>

<div class="p-2 bg-green-900 bg-opacity-20 rounded">
  <code>data-id="101"</code>
  <p class="text-xs mt-1">Custom attribute storing product ID</p>
</div>

<div class="p-2 bg-purple-900 bg-opacity-20 rounded">
  <code>&lt;h3 class="product-title"&gt;</code>
  <p class="text-xs mt-1">Product name (heading level 3)</p>
</div>

<div class="p-2 bg-red-900 bg-opacity-20 rounded">
  <code>&lt;p class="price"&gt;</code>
  <p class="text-xs mt-1">Price information (paragraph)</p>
</div>

<div class="p-2 bg-yellow-900 bg-opacity-20 rounded">
  <code>&lt;a href="/product/101"&gt;</code>
  <p class="text-xs mt-1">Link to product details page</p>
</div>

</div>

</div>

</div>

---

# Scraping the Product Card

Now let's extract data from that product element!

<div class="grid grid-cols-2 gap-6">

<div>

### The HTML

```html {monaco}
<div class="product" data-id="101">
  <h3 class="product-title">
    Laptop Pro 15
  </h3>
  <p class="price">$1,299.99</p>
  <p class="rating">
    ★★★★☆ (4.5/5) - 234 reviews
  </p>
  <p class="description">
    High-performance laptop
  </p>
  <p class="stock">In Stock</p>
  <a href="/product/101" 
     class="product-link">
    View Details
  </a>
</div>
```

</div>

<div>

### The Python Code

```python {monaco}
from bs4 import BeautifulSoup

# Find the product
product = soup.find('div', class_='product')

# Extract product ID from attribute
product_id = product['data-id']
# Result: "101"

# Extract title
title = product.find('h3', class_='product-title')
title_text = title.get_text().strip()
# Result: "Laptop Pro 15"

# Extract price
price = product.find('p', class_='price')
price_text = price.get_text().strip()
# Result: "$1,299.99"

# Extract link URL
link = product.find('a', class_='product-link')
url = link['href']
# Result: "/product/101"

# Extract stock status
stock = product.find('p', class_='stock')
status = stock.get_text().strip()
# Result: "In Stock"
```

</div>

</div>

---

# Tables: Structured Data Gold Mine

Tables are perfect for scraping structured data

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### HTML Table Structure

```html {monaco}
<table id="comparison">
  <thead>
    <tr>
      <th>Product Name</th>
      <th>Price</th>
      <th>Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Laptop Pro 15</td>
      <td>$1,299.99</td>
      <td>4.5</td>
    </tr>
    <tr>
      <td>Wireless Mouse</td>
      <td>$29.99</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>Keyboard</td>
      <td>$89.99</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
```

</div>

<div>

### Table Element Breakdown

<div class="space-y-2 text-sm">

<div class="p-2 bg-blue-900 bg-opacity-20 rounded">
  <code>&lt;table&gt;</code>
  <p class="text-xs mt-1">The container for entire table</p>
</div>

<div class="p-2 bg-green-900 bg-opacity-20 rounded">
  <code>&lt;thead&gt;</code>
  <p class="text-xs mt-1">Table header section</p>
</div>

<div class="p-2 bg-purple-900 bg-opacity-20 rounded">
  <code>&lt;tbody&gt;</code>
  <p class="text-xs mt-1">Table body with data rows</p>
</div>

<div class="p-2 bg-red-900 bg-opacity-20 rounded">
  <code>&lt;tr&gt;</code>
  <p class="text-xs mt-1">Table row</p>
</div>

<div class="p-2 bg-yellow-900 bg-opacity-20 rounded">
  <code>&lt;th&gt;</code>
  <p class="text-xs mt-1">Table header cell (column name)</p>
</div>

<div class="p-2 bg-orange-900 bg-opacity-20 rounded">
  <code>&lt;td&gt;</code>
  <p class="text-xs mt-1">Table data cell (actual data)</p>
</div>

</div>

</div>

</div>

---

# Scraping Tables: Extracting Structured Data

<div class="grid grid-cols-2 gap-6">

<div>

### The HTML Table

```html {monaco}
<table id="comparison">
  <thead>
    <tr>
      <th>Product Name</th>
      <th>Price</th>
      <th>Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Laptop Pro 15</td>
      <td>$1,299.99</td>
      <td>4.5</td>
    </tr>
    <tr>
      <td>Wireless Mouse</td>
      <td>$29.99</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
```

</div>

<div>

### The Python Code

```python {monaco}
# Find the table
table = soup.find('table', id='comparison')

# Extract headers
headers = []
for th in table.find_all('th'):
    headers.append(th.get_text().strip())
# Result: ['Product Name', 'Price', 'Rating']

# Extract all data rows
rows = []
for tr in table.find('tbody').find_all('tr'):
    row = []
    for td in tr.find_all('td'):
        row.append(td.get_text().strip())
    rows.append(row)

# Result:
# [
#   ['Laptop Pro 15', '$1,299.99', '4.5'],
#   ['Wireless Mouse', '$29.99', '5.0']
# ]

# Create dictionary for each row
products = []
for row in rows:
    product = {
        headers[0]: row[0],
        headers[1]: row[1],
        headers[2]: row[2]
    }
    products.append(product)
```

</div>

</div>

---

# Lists: Ordered and Unordered

Lists are common for navigation, features, and collections

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### Unordered List (Bullets)

```html {monaco}
<ul class="features">
  <li>16GB RAM</li>
  <li>512GB SSD</li>
  <li>15-inch display</li>
  <li>Backlit keyboard</li>
</ul>
```

### Ordered List (Numbers)

```html {monaco}
<ol class="instructions">
  <li>Open the package</li>
  <li>Connect the power cable</li>
  <li>Press the power button</li>
  <li>Follow setup wizard</li>
</ol>
```

### Nested Lists

```html {monaco}
<ul class="categories">
  <li>Electronics
    <ul>
      <li>Laptops</li>
      <li>Phones</li>
    </ul>
  </li>
  <li>Accessories</li>
</ul>
```

</div>

<div>

### Scraping Lists

```python {monaco}
# Find unordered list
features_list = soup.find('ul', class_='features')

# Extract all list items
features = []
for li in features_list.find_all('li'):
    features.append(li.get_text().strip())

# Result: 
# ['16GB RAM', '512GB SSD', 
#  '15-inch display', 'Backlit keyboard']


# Find ordered list
instructions = soup.find('ol', class_='instructions')
steps = [li.get_text().strip() 
         for li in instructions.find_all('li')]

# Result:
# ['Open the package', 
#  'Connect the power cable',
#  'Press the power button',
#  'Follow setup wizard']


# Nested lists - only direct children
categories = soup.find('ul', class_='categories')
main_items = categories.find_all('li', recursive=False)

# Get nested items
electronics = main_items[0]
sub_items = electronics.find('ul').find_all('li')
```

</div>

</div>

---

# Links: The Web's Connective Tissue

Links (`<a>` tags) are essential for navigation and scraping multiple pages

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### Basic Links

```html {monaco}
<!-- Simple link -->
<a href="/products">Products</a>

<!-- Link with class -->
<a href="/product/101" class="product-link">
  View Details
</a>

<!-- External link -->
<a href="https://example.com" 
   target="_blank">
  Visit Example
</a>

<!-- Email link -->
<a href="mailto:info@example.com">
  Contact Us
</a>

<!-- Link with multiple attributes -->
<a href="/product/101" 
   class="btn btn-primary"
   data-id="101"
   data-category="electronics">
  Buy Now
</a>
```

</div>

<div>

### Extracting Links

```python {monaco}
# Find all links
links = soup.find_all('a')

for link in links:
    # Get URL
    url = link.get('href')
    # Get link text
    text = link.get_text().strip()
    print(f"{text}: {url}")


# Find links with specific class
product_links = soup.find_all('a', class_='product-link')

for link in product_links:
    url = link['href']  # Alternative syntax
    print(url)


# Find links containing text
external_links = soup.find_all('a', href=True)
for link in external_links:
    href = link['href']
    if href.startswith('http'):
        print(f"External: {href}")


# Extract data attributes
buy_buttons = soup.find_all('a', 
                           class_='btn')
for button in buy_buttons:
    product_id = button.get('data-id')
    category = button.get('data-category')
    print(f"ID: {product_id}, Cat: {category}")
```

</div>

</div>

---

# CSS Selectors: The Power Tool

CSS selectors provide precise targeting of elements

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### Basic Selectors

```python {monaco}
# Tag selector
soup.select('p')  # All <p> tags

# Class selector
soup.select('.product')  # class="product"

# ID selector
soup.select('#header')  # id="header"

# Multiple classes
soup.select('.product.featured')

# Attribute selector
soup.select('[data-id]')  # Has attribute
soup.select('[data-id="101"]')  # Exact match
```

### Combinators

```python {monaco}
# Descendant (any level)
soup.select('div p')  # <p> inside <div>

# Direct child
soup.select('div > p')  # Direct child only

# Adjacent sibling
soup.select('h2 + p')  # <p> right after <h2>

# General sibling
soup.select('h2 ~ p')  # All <p> after <h2>
```

</div>

<div>

### Advanced Selectors

```python {monaco}
# Multiple selectors (OR)
soup.select('h1, h2, h3')  # Any heading

# Nested classes
soup.select('.product .price')

# Class + attribute
soup.select('.product[data-id="101"]')

# Nth child
soup.select('tr:nth-child(2)')  # 2nd row
soup.select('li:first-child')   # First item
soup.select('li:last-child')    # Last item

# Contains attribute value
soup.select('[href*="product"]')  # Contains
soup.select('[href^="https"]')    # Starts with
soup.select('[href$=".pdf"]')     # Ends with

# Not selector
soup.select('div:not(.excluded)')
```

### Real-World Example

```python {monaco}
# All product prices in stock items
prices = soup.select(
    '.product:not(.out-of-stock) .price'
)

# All external links
external = soup.select('a[href^="http"]')

# Product titles in featured section
titles = soup.select(
    '#featured .product .product-title'
)
```

</div>

</div>

---

# Putting It All Together: Complete Example

Let's scrape a complete page from our sample HTML

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

### Sample HTML Structure

```html {monaco}
<body>
  <header id="main-header">
    <h1>Sample E-Commerce Site</h1>
    <nav>
      <a href="/">Home</a>
      <a href="/products">Products</a>
    </nav>
  </header>
  
  <main>
    <h2>Featured Products</h2>
    
    <div class="product" data-id="101">
      <h3 class="product-title">Laptop Pro 15</h3>
      <p class="price">$1,299.99</p>
      <p class="rating">★★★★☆ (4.5/5)</p>
      <p class="stock">In Stock</p>
      <a href="/product/101">View Details</a>
    </div>
    
    <div class="product" data-id="102">
      <h3 class="product-title">Wireless Mouse</h3>
      <p class="price">$29.99</p>
      <p class="rating">★★★★★ (5/5)</p>
      <p class="stock">In Stock</p>
      <a href="/product/102">View Details</a>
    </div>
  </main>
</body>
```

</div>

<div class="text-sm">

### Complete Scraping Script

```python {monaco}
from bs4 import BeautifulSoup

# Load HTML (in practice, use requests.get())
with open('sample_products.html') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Extract site title
site_title = soup.select_one('#main-header h1')
print(f"Site: {site_title.get_text()}")

# Extract all navigation links
nav_links = soup.select('nav a')
print("\nNavigation:")
for link in nav_links:
    text = link.get_text()
    url = link['href']
    print(f"  {text} → {url}")

# Extract all products
products = soup.select('.product')
print(f"\nFound {len(products)} products:\n")

for product in products:
    # Extract each field
    product_id = product['data-id']
    title = product.select_one('.product-title').get_text()
    price = product.select_one('.price').get_text()
    rating = product.select_one('.rating').get_text()
    stock = product.select_one('.stock').get_text()
    link = product.select_one('a')['href']
    
    # Display results
    print(f"ID: {product_id}")
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print(f"Stock: {stock}")
    print(f"URL: {link}")
    print("-" * 40)
```

</div>

</div>

---

# Common HTML Patterns in Web Scraping

Recognizing these patterns will help you scrape faster

<div class="grid grid-cols-2 gap-6 mt-4 text-sm">

<div>

### Pattern 1: Card Layout

```html {monaco}
<div class="card">
  <img src="image.jpg" class="card-image">
  <h3 class="card-title">Title</h3>
  <p class="card-description">Description</p>
  <a href="/details" class="card-link">More</a>
</div>
```

**Target**: `.card`  
**Extract**: title, description, link, image

### Pattern 2: Data List

```html {monaco}
<ul class="specs">
  <li><strong>Brand:</strong> Apple</li>
  <li><strong>Model:</strong> Pro 15</li>
  <li><strong>RAM:</strong> 16GB</li>
</ul>
```

**Target**: `.specs li`  
**Extract**: split on `:` to get key-value pairs

### Pattern 3: Pagination

```html {monaco}
<div class="pagination">
  <a href="?page=1">1</a>
  <a href="?page=2" class="active">2</a>
  <a href="?page=3">3</a>
  <a href="?page=4">Next</a>
</div>
```

**Target**: `.pagination a[href]`  
**Extract**: page URLs for crawling

</div>

<div>

### Pattern 4: Metadata

```html {monaco}
<div class="item" 
     data-id="101"
     data-price="1299.99"
     data-category="electronics"
     data-rating="4.5">
  Content...
</div>
```

**Target**: `.item`  
**Extract**: all `data-*` attributes

### Pattern 5: Nested Comments

```html {monaco}
<div class="comment">
  <p class="author">John</p>
  <p class="text">Great product!</p>
  <div class="replies">
    <div class="comment">
      <p class="author">Jane</p>
      <p class="text">I agree!</p>
    </div>
  </div>
</div>
```

**Target**: `.comment` (recursive=False for top-level)  
**Extract**: author, text, nested replies

### Pattern 6: Hidden Data

```html {monaco}
<script type="application/json">
{
  "products": [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Mouse"}
  ]
}
</script>
```

**Target**: `script[type="application/json"]`  
**Extract**: JSON data, parse with `json.loads()`

</div>

</div>

---

# HTML Attributes Quick Reference

Essential attributes for web scraping

<div class="grid grid-cols-3 gap-4 mt-8 text-xs">

<div class="border border-blue-500 p-3 rounded">
<h4 class="text-blue-400 font-bold mb-2">IDENTIFICATION</h4>

```html
id="unique-name"
class="reusable-name"
data-id="101"
data-custom="value"
```

**Use**: Target specific elements
</div>

<div class="border border-green-500 p-3 rounded">
<h4 class="text-green-400 font-bold mb-2">LINKS & MEDIA</h4>

```html
href="/url"
src="image.jpg"
alt="description"
title="tooltip"
```

**Use**: Extract URLs and paths
</div>

<div class="border border-purple-500 p-3 rounded">
<h4 class="text-purple-400 font-bold mb-2">CONTENT</h4>

```html
value="input-value"
content="meta-content"
placeholder="hint"
aria-label="accessibility"
```

**Use**: Extract values and labels
</div>

<div class="border border-red-500 p-3 rounded">
<h4 class="text-red-400 font-bold mb-2">STATE</h4>

```html
disabled
checked
selected
hidden
```

**Use**: Check element state
</div>

<div class="border border-yellow-500 p-3 rounded">
<h4 class="text-yellow-400 font-bold mb-2">STYLE & DISPLAY</h4>

```html
style="color: red"
width="100"
height="200"
colspan="2"
```

**Use**: Extract dimensions, styles
</div>

<div class="border border-orange-500 p-3 rounded">
<h4 class="text-orange-400 font-bold mb-2">METADATA</h4>

```html
name="field-name"
type="text"
rel="nofollow"
target="_blank"
```

**Use**: Understand element purpose
</div>

</div>

---

# Debugging HTML: Browser DevTools

Learn to inspect HTML like a pro

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

### How to Inspect Elements

1. **Right-click** on any element
2. Select **"Inspect"** or **"Inspect Element"**
3. DevTools opens showing HTML structure
4. Hover over code to highlight elements

### What to Look For

<div class="space-y-2 text-sm mt-4">

✅ **Element tag name**  
`<div>`, `<p>`, `<span>`, etc.

✅ **Class names**  
`class="product featured"`

✅ **ID attributes**  
`id="main-header"`

✅ **Data attributes**  
`data-id="101"`, `data-price="29.99"`

✅ **Nested structure**  
Parent → Child relationships

✅ **Dynamic content**  
JavaScript-generated elements

</div>

</div>

<div>

### Pro Tips

<div class="space-y-3 text-sm">

<div class="p-3 bg-blue-900 bg-opacity-20 rounded">
<strong>💡 Copy Selectors</strong>
<br>
Right-click element → Copy → Copy selector
<br>
Gets exact CSS selector!
</div>

<div class="p-3 bg-green-900 bg-opacity-20 rounded">
<strong>💡 Search HTML</strong>
<br>
Press Ctrl+F (Cmd+F) in DevTools
<br>
Search for text, classes, or tags
</div>

<div class="p-3 bg-purple-900 bg-opacity-20 rounded">
<strong>💡 Network Tab</strong>
<br>
See what data the page loads
<br>
Find API calls and JSON responses
</div>

<div class="p-3 bg-red-900 bg-opacity-20 rounded">
<strong>💡 Console Testing</strong>
<br>
Test selectors in browser:
<br>
<code>document.querySelectorAll('.product')</code>
</div>

</div>

</div>

</div>

---

# Common Pitfalls & Solutions

Avoid these beginner mistakes

<div class="grid grid-cols-2 gap-6 mt-4 text-sm">

<div>

### ❌ Problem: Element Not Found

```python
# This returns None - crashes!
title = soup.find('h1').get_text()
```

### ✅ Solution: Check Existence

```python
title_element = soup.find('h1')
if title_element:
    title = title_element.get_text()
else:
    title = "Not found"

# Or use try-except
try:
    title = soup.find('h1').get_text()
except AttributeError:
    title = "Not found"
```

### ❌ Problem: Wrong Selector

```python
# Looking for class, but used ID syntax
products = soup.select('#product')  # Wrong!
```

### ✅ Solution: Use Correct Syntax

```python
# For class, use dot
products = soup.select('.product')  # Right!

# For ID, use hash
header = soup.select('#main-header')  # Right!
```

</div>

<div>

### ❌ Problem: Getting List Instead of String

```python
# Classes return a list!
product = soup.find('div')
print(product['class'])  
# Result: ['product', 'featured']
```

### ✅ Solution: Handle Lists

```python
classes = product['class']
# Join into string
class_string = ' '.join(classes)
# Result: "product featured"

# Or check if class exists
if 'featured' in product.get('class', []):
    print("This is featured!")
```

### ❌ Problem: Extra Whitespace

```python
text = element.get_text()
# Result: "\n    Laptop Pro 15    \n"
```

### ✅ Solution: Strip Whitespace

```python
text = element.get_text().strip()
# Result: "Laptop Pro 15"

# Or remove all whitespace
text = ' '.join(element.get_text().split())
```

</div>

</div>

---

# Practice Exercise: Your Turn! 🎯

Apply what you've learned

<div class="mt-8">

### Exercise: Scrape This HTML

```html {monaco}
<div class="store">
  <h1>Tech Store</h1>
  
  <div class="product" data-id="1" data-price="999">
    <h2 class="name">Laptop</h2>
    <p class="description">Fast and lightweight</p>
    <span class="badge featured">Featured</span>
    <a href="/products/1" class="buy-btn">Buy Now</a>
  </div>
  
  <div class="product" data-id="2" data-price="49">
    <h2 class="name">Mouse</h2>
    <p class="description">Wireless gaming mouse</p>
    <a href="/products/2" class="buy-btn">Buy Now</a>
  </div>
</div>
```

### Your Task

Write Python code to extract:

1. Store name
2. All product names
3. Product with id="1" → name, price, description, featured status
4. All "Buy Now" links
5. Count of total products

</div>

---

# Exercise Solution

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

### The Code

```python {monaco}
from bs4 import BeautifulSoup

html = """
<div class="store">
  <h1>Tech Store</h1>
  <div class="product" data-id="1" data-price="999">
    <h2 class="name">Laptop</h2>
    <p class="description">Fast and lightweight</p>
    <span class="badge featured">Featured</span>
    <a href="/products/1" class="buy-btn">Buy Now</a>
  </div>
  <div class="product" data-id="2" data-price="49">
    <h2 class="name">Mouse</h2>
    <p class="description">Wireless gaming mouse</p>
    <a href="/products/2" class="buy-btn">Buy Now</a>
  </div>
</div>
"""

soup = BeautifulSoup(html, 'html.parser')

# 1. Store name
store_name = soup.select_one('.store h1').get_text()
print(f"Store: {store_name}")

# 2. All product names
names = soup.select('.product .name')
print("\nAll Products:")
for name in names:
    print(f"  - {name.get_text()}")
```

</div>

<div>

```python {monaco}
# 3. Product with id="1" details
product_1 = soup.select_one('.product[data-id="1"]')
name = product_1.select_one('.name').get_text()
price = product_1['data-price']
desc = product_1.select_one('.description').get_text()
is_featured = product_1.select_one('.badge.featured')

print(f"\nProduct 1:")
print(f"  Name: {name}")
print(f"  Price: ${price}")
print(f"  Description: {desc}")
print(f"  Featured: {is_featured is not None}")

# 4. All "Buy Now" links
buy_links = soup.select('a.buy-btn')
print("\nBuy Links:")
for link in buy_links:
    text = link.get_text()
    url = link['href']
    print(f"  {text} → {url}")

# 5. Count of products
product_count = len(soup.select('.product'))
print(f"\nTotal Products: {product_count}")
```

### Output

```
Store: Tech Store

All Products:
  - Laptop
  - Mouse

Product 1:
  Name: Laptop
  Price: $999
  Description: Fast and lightweight
  Featured: True

Buy Links:
  Buy Now → /products/1
  Buy Now → /products/2

Total Products: 2
```

</div>

</div>

---
layout: center
class: text-center
---

# 🎉 Congratulations!

You now understand HTML fundamentals for web scraping!

<div class="mt-12 space-y-4">

### You've Learned:

✅ HTML structure and syntax  
✅ Tags, attributes, classes, and IDs  
✅ Common elements (divs, lists, tables, links)  
✅ CSS selectors for precise targeting  
✅ How to scrape real-world HTML  
✅ Debugging with browser DevTools

</div>

<div class="mt-12">
  <span class="text-2xl">Ready to build your first scraper! 🕷️</span>
</div>

---
layout: center
class: text-center
---

# Next Steps

<div class="grid grid-cols-2 gap-8 mt-12 text-left">

<div class="p-6 border border-blue-500 rounded">
  <h3 class="text-blue-400 text-xl mb-4">📚 Practice</h3>
  <ul class="text-sm space-y-2">
    <li>✓ Complete exercises in <code>exercises/</code></li>
    <li>✓ Run example scripts</li>
    <li>✓ Inspect real websites</li>
    <li>✓ Experiment with selectors</li>
  </ul>
</div>

<div class="p-6 border border-green-500 rounded">
  <h3 class="text-green-400 text-xl mb-4">🚀 Continue Learning</h3>
  <ul class="text-sm space-y-2">
    <li>✓ Module 2: Advanced BeautifulSoup</li>
    <li>✓ Module 3: Selenium for dynamic sites</li>
    <li>✓ Module 4: Scrapy framework</li>
    <li>✓ Module 5: Best practices & ethics</li>
  </ul>
</div>

</div>

<div class="mt-12">
  <p class="text-sm opacity-75">
    Questions? Check <code>resources/troubleshooting.md</code>
  </p>
</div>

---
layout: end
class: text-center
---

# Thank You! 🙏

Happy Scraping!

<div class="mt-8 text-sm opacity-75">
  Web Scraping Tutorial - Module 01
  <br>
  HTML Fundamentals for Beginners
</div>

