
from bs4 import BeautifulSoup

# Sample HTML document
html = """
<html>
<body>
    <div class="container">
        <h1 id="main-title">Products</h1>
        <div class="product featured" data-id="1">
            <h2>Product A</h2>
            <p class="price">$100</p>
        </div>
        <div class="product" data-id="2">
            <h2>Product B</h2>
            <p class="price">$200</p>
        </div>
    </div>
</body>
</html>
"""

# Parse the HTML document
soup = BeautifulSoup(html, 'html.parser')

# print(soup)

# Select all the h2 tags
h2_tags = soup.find_all('h2')
print("All h2 tags:")
for tag in h2_tags:
    print(f" - {tag.get_text()}")

# Find all elements with class 'product'
products = soup.find_all(class_='product')
print(f"\nFound {len(products)} products.")
for product in products:
    print(f" - {product.find('h2').get_text()}")

# Select element with id 'main-title'
title = soup.find(id='main-title')
print(f'\nMain title: {title.get_text()}')

# Select by attributes, Find elements with data-id="1"
featured = soup.find_all(attrs={"data-id": "1"})
print(f'\nFeatured product: {featured[0].find("h2").get_text()}')

# Find all price paragraphs within product divs
prices = soup.select('div.product p.price')
print("\nProduct Prices:")
for price in prices:
    print(f" - {price.get_text()}")



# """
# Example: CSS Selectors with BeautifulSoup
# Demonstrates various CSS selector techniques
# """

# from bs4 import BeautifulSoup

# # Sample HTML
# html = """
# <html>
# <body>
#     <div class="container">
#         <h1 id="main-title">Products</h1>
#         <div class="product featured" data-id="1">
#             <h2>Product A</h2>
#             <p class="price">$100</p>
#         </div>
#         <div class="product" data-id="2">
#             <h2>Product B</h2>
#             <p class="price">$200</p>
#         </div>
#     </div>
# </body>
# </html>
# """

# soup = BeautifulSoup(html, 'html.parser')

# print("CSS Selector Examples")
# print("=" * 50)

# # Select by tag
# # Find all h2 tags
# print("\n1. Select by tag:")
# h2_tags = soup.select('h2')
# for tag in h2_tags:
#     print(f"   {tag.get_text()}")

# # Select by class
# # Find all elements with class 'product'
# print("\n2. Select by class:")
# products = soup.select('.product')
# print(f"   Found {len(products)} products")

# # Select by ID
# # Select element with id 'main-title'
# print("\n3. Select by ID:")
# title = soup.select_one('#main-title')
# print(f"   {title.get_text()}")

# # Select by attribute
# # Find element with data-id="1"
# print("\n4. Select by attribute:")
# featured = soup.select('[data-id="1"]')
# print(f"   Featured product: {featured[0].find('h2').get_text()}")

# # Descendant selector
# # Find all price paragraphs within product divs
# print("\n5. Descendant selector (div p):")
# prices = soup.select('div.product p.price')
# for price in prices:
#     print(f"   {price.get_text()}")

# # ------
# # You can play more with CSS selectors below
# # ------


# # Direct child selector
# print("\n6. Direct child selector (div > h2):")
# headings = soup.select('div.product > h2')
# for heading in headings:
#     print(f"   {heading.get_text()}")

# # Multiple selectors
# print("\n7. Multiple selectors (h1, h2):")
# all_headings = soup.select('h1, h2')
# for heading in all_headings:
#     print(f"   {heading.name}: {heading.get_text()}")

# # Complex selector
# print("\n8. Complex selector:")
# featured_price = soup.select_one('div.product.featured p.price') # Select the price of the featured product
# if featured_price:
#     print(f"   Featured product price: {featured_price.get_text()}")
