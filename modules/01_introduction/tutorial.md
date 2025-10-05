# Module 1: Introduction to Web Scraping - Tutorial

## Welcome! 👋

This tutorial will guide you through the fundamentals of web scraping. By the end, you'll be able to fetch web pages and extract data from them.

## Part 1: Understanding How the Web Works

### The Request-Response Cycle

When you visit a website:
1. Your browser sends an **HTTP request** to a server
2. The server processes the request
3. The server sends back an **HTTP response** with HTML content
4. Your browser renders the HTML

Web scraping mimics this process programmatically!

## Part 2: Your First HTTP Request

### Step 1: Install Required Libraries

```bash
pip install requests beautifulsoup4
```

### Step 2: Make a Simple Request

Create a file `first_scraper.py`:

```python
import requests

# URL to scrape
url = "https://example.com"

# Make the request
response = requests.get(url)

# Check status
print(f"Status Code: {response.status_code}")
print(f"Content Length: {len(response.content)} bytes")
```

Run it:
```bash
python first_scraper.py
```

### Understanding Status Codes

- **200**: Success! ✅
- **404**: Page not found ❌
- **403**: Forbidden - access denied ❌
- **500**: Server error ❌

## Part 3: Parsing HTML with BeautifulSoup

### Step 3: Create a BeautifulSoup Object

```python
import requests
from bs4 import BeautifulSoup

# Get the page
url = "https://example.com"
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Get page title
title = soup.title.string
print(f"Page Title: {title}")
```

### Understanding HTML Structure

HTML is made of **elements** (tags):

```html
<div class="product">
    <h2>Product Name</h2>
    <p class="price">$19.99</p>
    <a href="/product/123">View Details</a>
</div>
```

- **Tag**: `<div>`, `<h2>`, `<p>`, `<a>`
- **Attribute**: `class="product"`, `href="/product/123"`
- **Content**: "Product Name", "$19.99"

## Part 4: Finding Elements

### Method 1: `find()` - Get First Match

```python
# Find first <h1> tag
heading = soup.find('h1')
print(heading.get_text())

# Find first element with specific class
element = soup.find('div', class_='product')
print(element.get_text())
```

### Method 2: `find_all()` - Get All Matches

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

### Method 3: CSS Selectors

```python
# Select by class
products = soup.select('.product')

# Select by ID
header = soup.select_one('#header')

# Complex selectors
prices = soup.select('div.product > p.price')
```

## Part 5: Extracting Data

### Getting Text Content

```python
# Get text from element
element = soup.find('h1')
text = element.get_text()

# Remove extra whitespace
text = element.get_text().strip()
```

### Getting Attributes

```python
# Get href from link
link = soup.find('a')
url = link.get('href')
# or
url = link['href']

# Get class attribute
div = soup.find('div')
class_name = div.get('class')
```

## Part 6: Practical Example - Scraping a Product Page

Let's scrape our sample product page:

```python
import requests
from bs4 import BeautifulSoup

# Use local file for practice
with open('data/sample_pages/sample_products.html', 'r') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Extract all products
products = soup.find_all('div', class_='product')

print(f"Found {len(products)} products:\n")

for product in products:
    # Extract title
    title = product.find('h3', class_='product-title').get_text()
    
    # Extract price
    price = product.find('p', class_='price').get_text()
    
    # Extract stock status
    stock = product.find('p', class_='stock').get_text()
    
    print(f"Product: {title}")
    print(f"Price: {price}")
    print(f"Status: {stock}")
    print("-" * 40)
```

## Part 7: Extracting Table Data

Tables are common on websites. Here's how to extract them:

```python
# Find the table
table = soup.find('table', id='comparison')

# Get headers
headers = []
for th in table.find_all('th'):
    headers.append(th.get_text().strip())

print(f"Headers: {headers}")

# Get rows
rows = []
for tr in table.find_all('tr')[1:]:  # Skip header row
    cells = []
    for td in tr.find_all('td'):
        cells.append(td.get_text().strip())
    rows.append(cells)

print(f"\nData rows: {len(rows)}")
for row in rows:
    print(row)
```

## Part 8: Saving Data to CSV

```python
import csv

# Assuming we have our scraped data in a list
data = [
    ['Product', 'Price', 'Rating'],
    ['Laptop Pro 15', '$1,299.99', '4.5'],
    ['Wireless Mouse', '$29.99', '5.0'],
    ['Mechanical Keyboard', '$89.99', '4.0']
]

# Save to CSV
with open('data/outputs/products.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("✓ Data saved to products.csv")
```

## Part 9: Error Handling

Always handle potential errors:

```python
import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    try:
        # Make request with timeout
        response = requests.get(url, timeout=10)
        
        # Check if successful
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract data
        title = soup.find('h1')
        if title:
            print(f"Title: {title.get_text()}")
        else:
            print("Title not found")
            
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Use the function
scrape_page("https://example.com")
```

## Part 10: Best Practices for Beginners

### DO ✅
- Start with simple websites
- Add delays between requests: `time.sleep(1)`
- Use try-except for error handling
- Test on local HTML files first
- Read the website's terms of service

### DON'T ❌
- Make too many rapid requests
- Scrape personal/private data
- Ignore error messages
- Assume page structure never changes

## Practice Exercises

### Exercise 1: Basic Scraping
1. Open `data/sample_pages/sample_products.html` in your browser
2. Write a script to extract all product names
3. Save them to a text file

### Exercise 2: Price Extraction
1. Extract all prices from the sample page
2. Convert them to float (remove '$' and ',')
3. Calculate the average price

### Exercise 3: Link Extraction
1. Extract all links from the page
2. Print links with their text
3. Save to a CSV file

## Complete Example: Product Scraper

Here's a complete example pulling it all together:

```python
import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_products(html_file):
    """Scrape products from HTML file."""
    
    # Read HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all products
    products = soup.find_all('div', class_='product')
    
    # Extract data
    product_list = []
    for product in products:
        title = product.find('h3', class_='product-title').get_text().strip()
        price = product.find('p', class_='price').get_text().strip()
        rating = product.find('p', class_='rating').get_text().strip()
        stock = product.find('p', class_='stock').get_text().strip()
        
        product_list.append({
            'title': title,
            'price': price,
            'rating': rating,
            'stock': stock
        })
    
    return product_list

def save_to_csv(products, filename):
    """Save products to CSV file."""
    
    keys = products[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(products)
    
    print(f"✓ Saved {len(products)} products to {filename}")

# Main execution
if __name__ == "__main__":
    html_file = 'data/sample_pages/sample_products.html'
    output_file = 'data/outputs/scraped_products.csv'
    
    print("Starting scraper...")
    products = scrape_products(html_file)
    
    print(f"Found {len(products)} products")
    for product in products:
        print(f"- {product['title']}: {product['price']}")
    
    save_to_csv(products, output_file)
    print("Done!")
```

## Next Steps

Congratulations! 🎉 You've completed Module 1!

You now know how to:
- Make HTTP requests
- Parse HTML with BeautifulSoup
- Find and extract elements
- Save data to files

**Next**: Move to Module 2 to learn advanced BeautifulSoup techniques!

## Troubleshooting

### Common Issues

**Problem**: `ModuleNotFoundError: No module named 'requests'`
- **Solution**: `pip install requests`

**Problem**: Element returns `None`
- **Solution**: Check if element exists, verify selector

**Problem**: Getting weird characters
- **Solution**: Add `encoding='utf-8'` when opening files

### Need Help?

- Check `resources/troubleshooting.md`
- Review `resources/references.md`
- Look at solution files in `solutions/` directory

Happy Scraping! 🕷️
