# Module 3: Selenium for Dynamic Content - Tutorial

## Welcome to Module 3! 🚗

Learn to scrape JavaScript-heavy websites using Selenium WebDriver for browser automation.

## Part 1: Understanding Dynamic Content

### Static vs Dynamic Websites

**Static websites:**
- HTML is complete in initial response
- Can scrape with requests + BeautifulSoup
- Example: `curl URL` shows all content

**Dynamic websites:**
- Content loaded with JavaScript
- Requires browser to render
- Example: Infinite scroll, AJAX content

### When to Use Selenium

Use Selenium when:
- ✅ Content loads with JavaScript
- ✅ Need to interact with page (clicks, forms)
- ✅ Handle authentication flows
- ✅ Infinite scroll or pagination
- ✅ Wait for AJAX requests

Use requests + BS4 when:
- ✅ Content in initial HTML
- ✅ Simple, fast scraping needed
- ✅ No interaction required

## Part 2: Setting Up Selenium

### Installation

```bash
# Install Selenium
pip install selenium

# Install WebDriver Manager (handles driver downloads)
pip install webdriver-manager
```

### Basic Setup

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatic driver management
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to URL
driver.get('https://example.com')

# Always close when done
driver.quit()
```

### Browser Options

```python
from selenium.webdriver.chrome.options import Options

options = Options()

# Headless mode (no GUI)
options.add_argument('--headless')

# Window size
options.add_argument('--window-size=1920,1080')

# Disable images (faster)
prefs = {'profile.managed_default_content_settings.images': 2}
options.add_experimental_option('prefs', prefs)

# Use options
driver = webdriver.Chrome(service=service, options=options)
```

## Part 3: Finding Elements

### Locator Strategies

```python
from selenium.webdriver.common.by import By

# By ID
element = driver.find_element(By.ID, 'element-id')

# By Class Name
elements = driver.find_elements(By.CLASS_NAME, 'my-class')

# By Tag Name
links = driver.find_elements(By.TAG_NAME, 'a')

# By CSS Selector
element = driver.find_element(By.CSS_SELECTOR, 'div.class > p')

# By XPath
element = driver.find_element(By.XPATH, '//div[@class="my-class"]')

# By Link Text
link = driver.find_element(By.LINK_TEXT, 'Click Here')

# By Partial Link Text
link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Click')

# By Name
input_field = driver.find_element(By.NAME, 'username')
```

### find_element vs find_elements

```python
# find_element - returns first match or raises exception
element = driver.find_element(By.CLASS_NAME, 'product')

# find_elements - returns list (empty if none found)
elements = driver.find_elements(By.CLASS_NAME, 'product')

if elements:
    for elem in elements:
        print(elem.text)
```

## Part 4: Waiting Strategies

**Never use `time.sleep()` alone!** Use Selenium waits instead.

### Implicit Wait

Sets a default wait time for finding elements:

```python
# Wait up to 10 seconds for elements to appear
driver.implicitly_wait(10)

# Now all find operations will wait
element = driver.find_element(By.ID, 'dynamic-content')
```

### Explicit Wait (Recommended)

Wait for specific conditions:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Create wait object
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

# Wait for element to be present
element = wait.until(
    EC.presence_of_element_located((By.ID, 'element-id'))
)

# Wait for element to be clickable
button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit'))
)

# Wait for element to be visible
element = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'product'))
)
```

### Common Expected Conditions

```python
# Element exists in DOM
EC.presence_of_element_located((By.ID, 'id'))

# Element is visible
EC.visibility_of_element_located((By.ID, 'id'))

# Element is clickable
EC.element_to_be_clickable((By.ID, 'id'))

# Text present in element
EC.text_to_be_present_in_element((By.ID, 'id'), 'text')

# Element is selected (checkbox/radio)
EC.element_to_be_selected((By.ID, 'id'))

# Alert is present
EC.alert_is_present()

# Title contains text
EC.title_contains('text')

# Number of windows
EC.number_of_windows_to_be(2)
```

## Part 5: Interacting with Elements

### Clicking Elements

```python
# Click button
button = driver.find_element(By.ID, 'submit-btn')
button.click()

# Click with wait
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.ID, 'submit-btn')))
button.click()
```

### Typing Text

```python
from selenium.webdriver.common.keys import Keys

# Type in input field
search_box = driver.find_element(By.NAME, 'search')
search_box.send_keys('web scraping')

# Clear and type
search_box.clear()
search_box.send_keys('new search')

# Press Enter
search_box.send_keys(Keys.RETURN)

# Type with modifiers
search_box.send_keys(Keys.CONTROL, 'a')  # Ctrl+A
```

### Dropdowns

```python
from selenium.webdriver.support.select import Select

# Select dropdown
dropdown = Select(driver.find_element(By.ID, 'country'))

# Select by visible text
dropdown.select_by_visible_text('United States')

# Select by value
dropdown.select_by_value('us')

# Select by index
dropdown.select_by_index(0)

# Get selected option
selected = dropdown.first_selected_option
print(selected.text)
```

### Checkboxes and Radio Buttons

```python
# Check if selected
checkbox = driver.find_element(By.ID, 'terms')
if not checkbox.is_selected():
    checkbox.click()

# Radio button
radio = driver.find_element(By.ID, 'option1')
radio.click()
```

## Part 6: Handling Forms

### Complete Form Example

```python
def fill_login_form(driver, username, password):
    """Fill and submit login form."""
    
    # Wait for form to load
    wait = WebDriverWait(driver, 10)
    
    # Find and fill username
    username_field = wait.until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    username_field.send_keys(username)
    
    # Fill password
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(password)
    
    # Submit (either click button or press Enter)
    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_btn.click()
    
    # Or: password_field.send_keys(Keys.RETURN)
    
    # Wait for redirect
    wait.until(EC.url_contains('/dashboard'))

# Usage
driver.get('https://example.com/login')
fill_login_form(driver, 'myuser', 'mypass')
```

## Part 7: JavaScript Execution

Execute JavaScript directly:

```python
# Scroll to bottom
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# Scroll to element
element = driver.find_element(By.ID, 'section')
driver.execute_script('arguments[0].scrollIntoView();', element)

# Click with JavaScript (bypass click interception)
button = driver.find_element(By.ID, 'btn')
driver.execute_script('arguments[0].click();', button)

# Get value from JavaScript
title = driver.execute_script('return document.title;')

# Modify page
driver.execute_script('arguments[0].style.border="3px solid red";', element)
```

## Part 8: Handling Multiple Windows/Tabs

```python
# Get current window handle
main_window = driver.current_window_handle

# Click link that opens new tab
link = driver.find_element(By.LINK_TEXT, 'Open in New Tab')
link.click()

# Wait for new window
wait = WebDriverWait(driver, 10)
wait.until(EC.number_of_windows_to_be(2))

# Switch to new window
for window in driver.window_handles:
    if window != main_window:
        driver.switch_to.window(window)
        break

# Do something in new window
print(driver.title)

# Close current window
driver.close()

# Switch back to main window
driver.switch_to.window(main_window)
```

## Part 9: Handling Infinite Scroll

```python
def scrape_infinite_scroll(driver, url, scroll_pause_time=2):
    """Scrape content from infinite scroll page."""
    
    driver.get(url)
    
    # Get initial scroll height
    last_height = driver.execute_script('return document.body.scrollHeight')
    
    all_items = []
    
    while True:
        # Scroll down
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        
        # Wait for content to load
        time.sleep(scroll_pause_time)
        
        # Extract items
        items = driver.find_elements(By.CLASS_NAME, 'item')
        for item in items:
            all_items.append(item.text)
        
        # Calculate new scroll height
        new_height = driver.execute_script('return document.body.scrollHeight')
        
        # Break if no more content
        if new_height == last_height:
            break
        
        last_height = new_height
    
    return all_items
```

## Part 10: Taking Screenshots

```python
# Full page screenshot
driver.save_screenshot('page.png')

# Element screenshot
element = driver.find_element(By.ID, 'content')
element.screenshot('element.png')

# For debugging
try:
    element = driver.find_element(By.ID, 'problematic-element')
    element.click()
except Exception as e:
    driver.save_screenshot('error.png')
    raise
```

## Part 11: Practical Examples

### Example 1: Scraping Dynamic Product Listings

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_products(url):
    """Scrape products from dynamic website."""
    
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Wait for products to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product')))
    
    # Scroll to load all products
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)
    
    # Extract products
    products = []
    product_elements = driver.find_elements(By.CLASS_NAME, 'product')
    
    for elem in product_elements:
        product = {
            'name': elem.find_element(By.CLASS_NAME, 'name').text,
            'price': elem.find_element(By.CLASS_NAME, 'price').text,
            'rating': elem.find_element(By.CLASS_NAME, 'rating').get_attribute('data-rating')
        }
        products.append(product)
    
    driver.quit()
    return products
```

### Example 2: Handling Login and Session

```python
def scrape_after_login(url, username, password):
    """Scrape content after logging in."""
    
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Go to login page
        driver.get(url + '/login')
        
        # Fill login form
        username_input = wait.until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys(username)
        
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)
        
        # Submit
        submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_btn.click()
        
        # Wait for dashboard
        wait.until(EC.url_contains('/dashboard'))
        
        # Now scrape protected content
        driver.get(url + '/protected/data')
        
        # Extract data
        data = driver.find_element(By.ID, 'data-container').text
        
        return data
        
    finally:
        driver.quit()
```

## Part 12: Best Practices

### DO ✅
- Use explicit waits instead of `time.sleep()`
- Always close drivers with `driver.quit()`
- Use headless mode for production
- Handle exceptions properly
- Take screenshots for debugging

### DON'T ❌
- Mix implicit and explicit waits
- Forget to close browser
- Use overly long timeouts
- Ignore stale element exceptions

## Debugging Tips

```python
# Print current URL
print(driver.current_url)

# Print page source
print(driver.page_source)

# Check element visibility
element = driver.find_element(By.ID, 'elem')
print(f"Displayed: {element.is_displayed()}")
print(f"Enabled: {element.is_enabled()}")

# Get element attributes
print(element.get_attribute('class'))
print(element.get_attribute('href'))
```

## Exercise: Build a Dynamic Scraper

Create a scraper that:
1. Logs into a website
2. Navigates to a data page
3. Scrolls to load all content
4. Extracts and saves data

## Next Steps

Excellent work! You can now handle dynamic content and browser automation.

**Next**: Move to Module 4 to learn Scrapy for production-scale scraping!
