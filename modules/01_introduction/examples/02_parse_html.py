"""
Example 2: Parse HTML with BeautifulSoup
This script demonstrates how to parse HTML content and extract information.
"""

import requests
from bs4 import BeautifulSoup

def parse_html():
    """Parse HTML and extract basic information."""
    
    # Fetch a simple webpage
    url = "https://example.com"
    response = requests.get(url)
    
    # Create BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract title
    title = soup.title.string if soup.title else "No title found"
    print(f"Page Title: {title}")
    
    # Extract all headings
    print("\nHeadings found:")
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        print(f"  {heading.name}: {heading.get_text().strip()}")
    
    # Extract all paragraphs
    print("\nParagraphs:")
    paragraphs = soup.find_all('p')
    for i, p in enumerate(paragraphs, 1):
        print(f"  {i}. {p.get_text().strip()[:100]}...")

if __name__ == "__main__":
    parse_html()
