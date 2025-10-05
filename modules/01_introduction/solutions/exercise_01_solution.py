"""
Exercise 1: Solution

Extract all product titles from the sample HTML page
"""

from bs4 import BeautifulSoup

# Read the HTML file
with open('../../../data/sample_pages/sample_products.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all product title elements
titles = soup.find_all('h3', class_='product-title')

# Extract and print the titles
print("Product Titles:")
print("-" * 40)
for title in titles:
    print(f"- {title.get_text().strip()}")

# BONUS: Save titles to a file
with open('../../../data/outputs/product_titles.txt', 'w', encoding='utf-8') as f:
    for title in titles:
        f.write(title.get_text().strip() + '\n')

print("\n✓ Titles saved to product_titles.txt")
