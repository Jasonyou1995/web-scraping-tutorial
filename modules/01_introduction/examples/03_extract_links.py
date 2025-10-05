"""
Example 3: Extract Links from a Page
This script demonstrates how to find and extract all links from a webpage.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_links(url):
    """Extract all links from a webpage."""
    
    print(f"Extracting links from: {url}\n")
    
    # Fetch the page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all <a> tags
    links = soup.find_all('a', href=True)
    
    print(f"Found {len(links)} links:\n")
    
    for i, link in enumerate(links, 1):
        href = link['href']
        text = link.get_text().strip() or "[No text]"
        
        # Convert relative URLs to absolute
        absolute_url = urljoin(url, href)
        
        print(f"{i}. Text: {text}")
        print(f"   URL: {absolute_url}")
        print()

def categorize_links(url):
    """Categorize links as internal or external."""
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    base_domain = urlparse(url).netloc
    internal_links = []
    external_links = []
    
    for link in soup.find_all('a', href=True):
        absolute_url = urljoin(url, link['href'])
        link_domain = urlparse(absolute_url).netloc
        
        if link_domain == base_domain:
            internal_links.append(absolute_url)
        elif link_domain:  # Not empty (not a fragment or javascript:)
            external_links.append(absolute_url)
    
    print(f"\nInternal Links ({len(internal_links)}):")
    for link in internal_links[:5]:  # Show first 5
        print(f"  - {link}")
    
    print(f"\nExternal Links ({len(external_links)}):")
    for link in external_links[:5]:  # Show first 5
        print(f"  - {link}")

if __name__ == "__main__":
    url = "https://example.com"
    extract_links(url)
    categorize_links(url)
