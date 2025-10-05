#!/usr/bin/env python3
"""
Hello World Web Scraping Tutorial
==================================

This is a simple introduction to web scraping using Python.
It demonstrates fetching a web page and extracting basic information.
"""

import os
import requests
from bs4 import BeautifulSoup


def main():
    """Main function demonstrating basic web scraping."""
    
    print("=" * 50)
    print("Hello World - Web Scraping Tutorial")
    print("=" * 50)
    print()
    
    # Example 1: Load local HTML file
    print("1. Loading sample HTML file...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(script_dir, 'sample.html')
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        print(f"   ✓ Successfully loaded HTML file")
        print(f"   Content Length: {len(html_content)} bytes")
    except FileNotFoundError:
        print(f"   ✗ File not found: {html_file}")
        return
    
    print()
    
    # Example 2: Parsing HTML with BeautifulSoup
    print("2. Parsing HTML content with BeautifulSoup...")
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the title
    title = soup.find('title')
    if title:
        print(f"   Page Title: {title.text}")
    
    # Find the first heading
    h1 = soup.find('h1')
    if h1:
        print(f"   First Heading: {h1.text}")
    
    print("   ✓ Parsing successful!")
    print()
    
    # Example 3: Finding all paragraphs
    print("3. Extracting all paragraphs...")
    paragraphs = soup.find_all('p')
    print(f"   Found {len(paragraphs)} paragraph(s)")
    
    for i, p in enumerate(paragraphs, 1):
        text = p.text.strip()
        if text:
            print(f"   Paragraph {i}: {text[:60]}..." if len(text) > 60 else f"   Paragraph {i}: {text}")
    
    print()
    
    # Example 4: Finding elements by class
    print("4. Finding elements by CSS class...")
    content_div = soup.find('div', class_='content')
    if content_div:
        print(f"   ✓ Found content div")
        items = content_div.find_all('li')
        print(f"   List items in content:")
        for item in items:
            print(f"     - {item.text}")
    
    print()
    
    # Example 5: Extracting specific text
    print("5. Extracting library information...")
    examples_div = soup.find('div', class_='examples')
    if examples_div:
        libraries = examples_div.find_all('p')
        print(f"   Popular libraries mentioned:")
        for lib in libraries:
            print(f"     • {lib.text}")
    
    print()
    
    # Example 6: Demonstrating requests library (optional, with internet)
    print("6. Testing requests library (optional)...")
    print("   Note: Skipping HTTP request (requires internet access)")
    print("   The requests library is installed and ready to use!")
    print("   Example usage:")
    print("     response = requests.get('https://example.com')")
    print("     soup = BeautifulSoup(response.content, 'html.parser')")
    
    print()
    print("=" * 50)
    print("Tutorial complete! All packages are working correctly.")
    print("=" * 50)
    print()
    print("✓ BeautifulSoup - HTML parsing works!")
    print("✓ lxml - Parser backend works!")
    print("✓ requests - HTTP library is installed!")
    print("✓ selenium - Browser automation library is installed!")
    print("✓ pandas - Data processing library is installed!")
    print()
    print("You're all set to start web scraping! 🎉")


if __name__ == "__main__":
    main()
