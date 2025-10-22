---
theme: default
background: https://images.unsplash.com/photo-1542831371-29b0f74f9713
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## HTML Syntax for Web Scraping
  A focused 3-minute introduction to HTML syntax essentials
drawings:
  persist: false
transition: slide-left
title: HTML Syntax for Web Scraping
mdc: true
---

# HTML Syntax Essentials
## For Web Scraping

Learn the core syntax you need to scrape effectively

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space to begin <carbon-arrow-right class="inline"/>
  </span>
</div>

---

# HTML Element Syntax

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

### Basic Structure

```html
<tagname attribute="value">Content</tagname>
```

### Real Examples

```html
<p class="intro">Welcome!</p>

<a href="/page">Link text</a>

<div id="header">Header</div>
```

</div>

<div>

### Key Components

<div class="border border-blue-500 p-4 rounded mb-3">
  <code class="text-blue-400">&lt;p&gt;</code>
  <p class="text-xs mt-2">Opening tag</p>
</div>

<div class="border border-green-500 p-4 rounded mb-3">
  <code class="text-green-400">class="intro"</code>
  <p class="text-xs mt-2">Attribute with value</p>
</div>

<div class="border border-purple-500 p-4 rounded">
  <code class="text-purple-400">&lt;/p&gt;</code>
  <p class="text-xs mt-2">Closing tag</p>
</div>

</div>

</div>

---

# ID vs Class Attributes

<div class="grid grid-cols-2 gap-8">

<div>

### ID: Unique Identifier

```html
<header id="main-header">
  <h1>My Website</h1>
</header>
```

**Python Scraping:**

```python
# Find by ID
header = soup.find(id='main-header')

# CSS selector syntax: #
header = soup.select_one('#main-header')
```

<div class="mt-4 p-3 bg-blue-900 bg-opacity-30 rounded text-sm">
  <strong>Rule:</strong> Use <code>#</code> for IDs<br>
  One ID per page only
</div>

</div>

<div>

### Class: Reusable Label

```html
<div class="product">
  <h3 class="product-title">Laptop</h3>
  <p class="price">$999</p>
</div>
```

**Python Scraping:**

```python
# Find all with class
products = soup.find_all(class_='product')

# CSS selector syntax: .
products = soup.select('.product')
```

<div class="mt-4 p-3 bg-purple-900 bg-opacity-30 rounded text-sm">
  <strong>Rule:</strong> Use <code>.</code> for classes<br>
  Can have many per page
</div>

</div>

</div>

---

# Essential HTML Tags

<div class="grid grid-cols-2 gap-6 text-sm">

<div>

### Structure

```html
<div>    <!-- Container -->
<span>   <!-- Inline -->
<header> <!-- Page header -->
<nav>    <!-- Navigation -->
```

### Text

```html
<h1> to <h6>  <!-- Headings -->
<p>           <!-- Paragraph -->
<strong>      <!-- Bold -->
```

</div>

<div>

### Data

```html
<ul>    <!-- Unordered list -->
<ol>    <!-- Ordered list -->
<li>    <!-- List item -->
<table> <!-- Table -->
<tr>    <!-- Table row -->
<td>    <!-- Table cell -->
```

### Links & Media

```html
<a href="url">    <!-- Link -->
<img src="url">   <!-- Image -->
```

</div>

</div>

---

# CSS Selector Syntax (With VSC Demo)

<div class="grid grid-cols-2 gap-8 mt-4">

<div>

### Basic Selectors

```python
# Tag selector
soup.select('p')

# Class selector
soup.select('.product')

# ID selector
soup.select('#header')

# Attribute selector
soup.select('[data-id="101"]')
```

### Combinators

```python
# Descendant (any level)
soup.select('div p')

# Direct child
soup.select('div > p')
```

</div>

<div>

### Advanced Patterns

```python
# Multiple classes
soup.select('.product.featured')

# Multiple selectors (OR)
soup.select('h1, h2, h3')

# Nth child
soup.select('tr:nth-child(2)')

# Attribute contains
soup.select('[href*="product"]')

# Attribute starts with
soup.select('[href^="https"]')

# Not selector
soup.select('div:not(.excluded)')
```

</div>

</div>

---

# Practical Example: Product Card

<div class="grid grid-cols-2 gap-6">

<div>

### HTML Structure

```html
<div class="product" data-id="101">
  <h3 class="product-title">
    Laptop Pro 15
  </h3>
  <p class="price">$1,299.99</p>
  <p class="stock">In Stock</p>
  <a href="/product/101" 
     class="product-link">
    View Details
  </a>
</div>
```

</div>

<div>

### Python Scraping

```python
from bs4 import BeautifulSoup

# Find the product
product = soup.find('div', class_='product')

# Extract ID from attribute
product_id = product['data-id']

# Extract title
title = product.find('h3', 
    class_='product-title').get_text().strip()

# Extract price
price = product.find('p', 
    class_='price').get_text().strip()

# Extract link URL
link = product.find('a', 
    class_='product-link')['href']
```

</div>

</div>

---

# Table Syntax

<div class="grid grid-cols-2 gap-6">

<div>

### HTML Table (Draw it)

```html
<table id="products">
  <thead>
    <tr>
      <th>Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Laptop</td>
      <td>$1,299</td>
    </tr>
    <tr>
      <td>Mouse</td>
      <td>$29</td>
    </tr>
  </tbody>
</table>
```

</div>

<div>

### Python Scraping

```python
# Find table
table = soup.find('table', id='products')

# Extract headers
headers = [th.get_text().strip() 
           for th in table.find_all('th')]

# Extract rows
rows = []
for tr in table.find('tbody').find_all('tr'):
    row = [td.get_text().strip() 
           for td in tr.find_all('td')]
    rows.append(row)

# Result:
# headers = ['Name', 'Price']
# rows = [
#   ['Laptop', '$1,299'],
#   ['Mouse', '$29']
# ]
```

</div>

</div>

---

# Common Syntax Patterns

<div class="grid grid-cols-2 gap-6 text-sm">

<div>

### Pattern 1: Data Attributes

```html
<div class="item" 
     data-id="101"
     data-price="29.99"
     data-category="electronics">
  Content
</div>
```

```python
item = soup.find('div', class_='item')
item_id = item['data-id']
price = item['data-price']
category = item['data-category']
```

</div>

<div>

### Pattern 2: Nested Elements

```html
<div class="card">
  <h3 class="title">Title</h3>
  <p class="desc">Description</p>
  <a href="/link">More</a>
</div>
```

```python
card = soup.find('div', class_='card')
title = card.find('h3', class_='title')
desc = card.find('p', class_='desc')
link = card.find('a')['href']
```

</div>

</div>

---

# Common Mistakes & Fixes

<div class="grid grid-cols-2 gap-6 text-sm">

<div>

### ❌ Wrong Selector Syntax

```python
# Wrong: Using # for class
soup.select('#product')

# Wrong: Using . for ID
soup.select('.header')
```

### ✅ Correct Syntax

```python
# Right: . for class
soup.select('.product')

# Right: # for ID
soup.select('#header')
```

</div>

<div>

### ❌ No Error Handling

```python
# Crashes if not found
title = soup.find('h1').get_text()
```

### ✅ Safe Extraction

```python
# Safe with check
title_elem = soup.find('h1')
if title_elem:
    title = title_elem.get_text().strip()
else:
    title = "Not found"
```

</div>

</div>

---
layout: center
class: text-center
---

# 🎯 Quick Reference

<div class="grid grid-cols-3 gap-6 mt-12 text-left text-sm">

<div class="p-4 border border-blue-500 rounded">
  <h4 class="text-blue-400 font-bold mb-3">SELECTORS</h4>
  <code class="text-xs">
    .class → class<br>
    #id → ID<br>
    tag → tag name<br>
    [attr] → has attribute<br>
    [attr="val"] → exact match
  </code>
</div>

<div class="p-4 border border-green-500 rounded">
  <h4 class="text-green-400 font-bold mb-3">METHODS</h4>
  <code class="text-xs">
    .find() → first match<br>
    .find_all() → all matches<br>
    .select() → CSS selector<br>
    .get_text() → extract text<br>
    ['attr'] → get attribute
  </code>
</div>

<div class="p-4 border border-purple-500 rounded">
  <h4 class="text-purple-400 font-bold mb-3">TAGS</h4>
  <code class="text-xs">
    &lt;div&gt; container<br>
    &lt;p&gt; paragraph<br>
    &lt;a&gt; link<br>
    &lt;table&gt; table<br>
    &lt;ul&gt;/&lt;li&gt; list
  </code>
</div>

</div>

---
layout: end
class: text-center
---

# Ready to Scrape! 🕷️

You've mastered HTML syntax essentials

<div class="mt-8 text-sm opacity-75">
  HTML Syntax Guide
</div>
