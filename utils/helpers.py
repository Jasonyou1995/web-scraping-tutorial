"""
Utility Helper Functions for Web Scraping
Common functions used across different scraping projects.
"""

import time
import random
from functools import wraps
from typing import Optional, Dict

def rate_limit(min_delay: float = 1.0, max_delay: float = 3.0):
    """
    Decorator to add rate limiting to functions.
    
    Args:
        min_delay: Minimum delay in seconds
        max_delay: Maximum delay in seconds
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = random.uniform(min_delay, max_delay)
            time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def get_headers(custom_headers: Optional[Dict] = None) -> Dict:
    """
    Generate common HTTP headers for requests.
    
    Args:
        custom_headers: Optional custom headers to merge
    
    Returns:
        Dictionary of HTTP headers
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    if custom_headers:
        headers.update(custom_headers)
    
    return headers

def clean_text(text: str) -> str:
    """
    Clean extracted text by removing extra whitespace.
    
    Args:
        text: Raw text string
    
    Returns:
        Cleaned text string
    """
    if not text:
        return ""
    
    # Replace multiple spaces/newlines with single space
    lines = [line.strip() for line in text.splitlines()]
    return ' '.join(filter(None, lines))

def safe_find(soup, *args, **kwargs):
    """
    Safely find an element, returning None if not found.
    
    Args:
        soup: BeautifulSoup object
        *args, **kwargs: Arguments to pass to find()
    
    Returns:
        Element if found, None otherwise
    """
    try:
        return soup.find(*args, **kwargs)
    except Exception:
        return None

def safe_get_text(element, default: str = "") -> str:
    """
    Safely extract text from an element.
    
    Args:
        element: BeautifulSoup element
        default: Default value if element is None
    
    Returns:
        Extracted text or default value
    """
    if element:
        return clean_text(element.get_text())
    return default

def save_to_file(data: str, filename: str, mode: str = 'w'):
    """
    Save data to a file.
    
    Args:
        data: Data to save
        filename: Output filename
        mode: File mode ('w' for write, 'a' for append)
    """
    with open(filename, mode, encoding='utf-8') as f:
        f.write(data)
    print(f"✓ Data saved to {filename}")
