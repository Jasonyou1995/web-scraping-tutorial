"""
Example 1: Simple HTTP Request
This script demonstrates how to make a basic HTTP GET request
and examine the response.
"""

import requests

def simple_request():
    """Make a simple GET request to a website."""
    
    # URL to fetch
    url = "https://example.com"
    
    print(f"Fetching: {url}")
    
    # Make the request
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        print("✓ Request successful!")
        print(f"Status Code: {response.status_code}")
        print(f"Content Type: {response.headers.get('Content-Type')}")
        print(f"Content Length: {len(response.content)} bytes")
        print("\nFirst 500 characters of response:")
        print(response.text[:500])
    else:
        print(f"✗ Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    simple_request()
