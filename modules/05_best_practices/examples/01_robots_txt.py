"""
Example: Respecting robots.txt
Demonstrates how to check and respect robots.txt files
"""

from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
import time


class RespectfulScraper:
    """A scraper that respects robots.txt"""
    
    def __init__(self, user_agent='*'):
        self.user_agent = user_agent
        self.robot_parsers = {}
    
    def can_fetch(self, url):
        """Check if URL can be fetched according to robots.txt"""
        
        # Parse URL to get base
        parsed = urlparse(url)
        base_url = f"{parsed.scheme}://{parsed.netloc}"
        
        # Get or create robot parser for this domain
        if base_url not in self.robot_parsers:
            rp = RobotFileParser()
            robots_url = urljoin(base_url, '/robots.txt')
            rp.set_url(robots_url)
            
            try:
                rp.read()
                self.robot_parsers[base_url] = rp
                print(f"✓ Loaded robots.txt from {robots_url}")
            except Exception as e:
                print(f"⚠ Could not load robots.txt: {e}")
                # If can't load, assume it's OK (be conservative)
                return True
        
        # Check if we can fetch
        can_fetch = self.robot_parsers[base_url].can_fetch(self.user_agent, url)
        
        if can_fetch:
            # Check crawl delay
            crawl_delay = self.robot_parsers[base_url].crawl_delay(self.user_agent)
            if crawl_delay:
                print(f"  Respecting crawl delay: {crawl_delay}s")
                time.sleep(crawl_delay)
        
        return can_fetch
    
    def scrape(self, url):
        """Scrape URL if allowed by robots.txt"""
        
        # Check robots.txt
        if not self.can_fetch(url):
            print(f"✗ Scraping not allowed by robots.txt: {url}")
            return None
        
        print(f"✓ Scraping allowed: {url}")
        
        # Add polite delay
        time.sleep(1)
        
        # Fetch page
        headers = {
            'User-Agent': 'Tutorial Scraper (+https://github.com/Jasonyou1995/web-scraping-tutorial)'
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Parse content
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Error fetching {url}: {e}")
            return None


def main():
    """Example usage"""
    
    scraper = RespectfulScraper(user_agent='MyBot')
    
    # Example URLs to check
    urls = [
        'https://example.com/',
        'https://example.com/page1',
    ]
    
    for url in urls:
        print(f"\nChecking: {url}")
        soup = scraper.scrape(url)
        
        if soup:
            title = soup.find('title')
            if title:
                print(f"  Page title: {title.string}")


if __name__ == "__main__":
    main()
