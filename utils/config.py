"""
Configuration Settings
Centralized configuration for web scraping projects.
"""

import os
from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = DATA_DIR / 'outputs'
SAMPLE_PAGES_DIR = DATA_DIR / 'sample_pages'

# Create directories if they don't exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
SAMPLE_PAGES_DIR.mkdir(parents=True, exist_ok=True)

# Request settings
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 2

# Rate limiting
MIN_REQUEST_DELAY = 1.0
MAX_REQUEST_DELAY = 3.0

# Headers
DEFAULT_USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/91.0.4472.124 Safari/537.36'
)

# Selenium settings
SELENIUM_IMPLICIT_WAIT = 10
SELENIUM_PAGE_LOAD_TIMEOUT = 30
HEADLESS_MODE = True

# Scrapy settings
SCRAPY_USER_AGENT = 'Tutorial Scraper (+https://github.com/Jasonyou1995/web-scraping-tutorial)'
SCRAPY_ROBOTSTXT_OBEY = True
SCRAPY_CONCURRENT_REQUESTS = 16
SCRAPY_DOWNLOAD_DELAY = 2

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
