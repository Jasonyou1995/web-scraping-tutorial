"""
Example: Basic Selenium Usage
Demonstrates how to set up and use Selenium WebDriver
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def basic_selenium_example():
    """Basic Selenium setup and usage."""
    
    # Setup Chrome driver with automatic driver management
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Navigate to a website
        print("Opening example.com...")
        driver.get("https://example.com")
        
        # Get page title
        print(f"Page title: {driver.title}")
        
        # Find element by tag name
        heading = driver.find_element(By.TAG_NAME, "h1")
        print(f"Main heading: {heading.text}")
        
        # Find all links
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"\nFound {len(links)} links:")
        for link in links:
            print(f"- {link.text}: {link.get_attribute('href')}")
        
        # Wait for element (example)
        wait = WebDriverWait(driver, 10)
        body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print(f"\nPage loaded successfully!")
        
        # Get page source
        page_source = driver.page_source
        print(f"Page source length: {len(page_source)} characters")
        
    finally:
        # Always close the browser
        print("\nClosing browser...")
        driver.quit()

if __name__ == "__main__":
    basic_selenium_example()
