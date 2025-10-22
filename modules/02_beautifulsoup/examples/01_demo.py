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
