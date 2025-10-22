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
