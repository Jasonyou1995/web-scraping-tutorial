"""
URL and Data Validators
Functions to validate URLs and scraped data.
"""

import re
from urllib.parse import urlparse
from typing import Optional

def is_valid_url(url: str) -> bool:
    """
    Check if a URL is valid.
    
    Args:
        url: URL string to validate
    
    Returns:
        True if valid, False otherwise
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

def is_valid_email(email: str) -> bool:
    """
    Check if an email address is valid.
    
    Args:
        email: Email string to validate
    
    Returns:
        True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def sanitize_filename(filename: str) -> str:
    """
    Remove invalid characters from filename.
    
    Args:
        filename: Original filename
    
    Returns:
        Sanitized filename
    """
    # Remove invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Replace spaces with underscores
    filename = filename.replace(' ', '_')
    # Limit length
    return filename[:255]

def extract_domain(url: str) -> Optional[str]:
    """
    Extract domain from URL.
    
    Args:
        url: Full URL
    
    Returns:
        Domain name or None if invalid
    """
    try:
        parsed = urlparse(url)
        return parsed.netloc
    except Exception:
        return None
