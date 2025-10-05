# Module 4: Scrapy Framework - Tutorial

## Welcome to Module 4! 🕷️

Learn to build production-ready, scalable web scrapers with the Scrapy framework.

## Part 1: Introduction to Scrapy

### What is Scrapy?

Scrapy is a powerful web scraping framework that provides:
- **Built-in crawling**: Follow links automatically
- **Data pipelines**: Process and clean data
- **Middleware**: Customize request/response handling
- **Async processing**: Fast, concurrent requests
- **Export formats**: JSON, CSV, XML, and more

### When to Use Scrapy

Use Scrapy for:
- ✅ Large-scale scraping projects
- ✅ Crawling entire websites
- ✅ Complex data processing pipelines
- ✅ Production deployments
- ✅ Sites with consistent structure

Use requests/BS4 for:
- ✅ Simple one-off scraping
- ✅ Quick prototypes
- ✅ Single-page scraping

## Part 2: Scrapy Architecture

### Core Components

1. **Spiders**: Define how to scrape and what to extract
2. **Items**: Define data structure
3. **Pipelines**: Process extracted data
4. **Middlewares**: Customize requests/responses
5. **Settings**: Configure behavior

### Data Flow

```
1. Spider sends Request
2. Downloader fetches page
3. Spider parses Response
4. Items extracted
5. Pipelines process Items
6. Data exported
```

## Part 3: Creating Your First Scrapy Project

### Step 1: Create Project

```bash
# Create new Scrapy project
scrapy startproject tutorial_project
cd tutorial_project

# Project structure created:
# tutorial_project/
#   scrapy.cfg
#   tutorial_project/
#     __init__.py
#     items.py
#     middlewares.py
#     pipelines.py
#     settings.py
#     spiders/
#       __init__.py
```

### Step 2: Create a Spider

```bash
# Generate spider
scrapy genspider quotes quotes.toscrape.com

# Creates: spiders/quotes.py
```

### Step 3: Basic Spider Structure

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        # Extract data here
        pass
```

## Part 4: Extracting Data with Selectors

### CSS Selectors

```python
def parse(self, response):
    # Extract with CSS
    quotes = response.css('div.quote')
    
    for quote in quotes:
        text = quote.css('span.text::text').get()
        author = quote.css('small.author::text').get()
        tags = quote.css('div.tags a.tag::text').getall()
        
        yield {
            'text': text,
            'author': author,
            'tags': tags
        }
```

### XPath Selectors

```python
def parse(self, response):
    # Extract with XPath
    quotes = response.xpath('//div[@class="quote"]')
    
    for quote in quotes:
        yield {
            'text': quote.xpath('.//span[@class="text"]/text()').get(),
            'author': quote.xpath('.//small[@class="author"]/text()').get(),
            'tags': quote.xpath('.//div[@class="tags"]/a/text()').getall()
        }
```

### Selector Methods

```python
# .get() - returns first match or None
title = response.css('h1::text').get()

# .getall() - returns list of all matches
links = response.css('a::attr(href)').getall()

# .re() - extract using regex
numbers = response.css('span.price::text').re(r'\d+\.\d+')

# .re_first() - first regex match
price = response.css('span.price::text').re_first(r'\d+\.\d+')

# Default values
title = response.css('h1::text').get(default='No Title')
```

## Part 5: Following Links (Pagination)

### Method 1: Manual Link Following

```python
def parse(self, response):
    # Extract data from current page
    for quote in response.css('div.quote'):
        yield {
            'text': quote.css('span.text::text').get(),
            'author': quote.css('small.author::text').get()
        }
    
    # Follow next page link
    next_page = response.css('li.next a::attr(href)').get()
    if next_page:
        yield response.follow(next_page, self.parse)
```

### Method 2: Using response.follow()

```python
def parse(self, response):
    # Extract data
    # ...
    
    # Follow all product links
    for link in response.css('a.product-link'):
        yield response.follow(link, self.parse_product)
    
    # Follow pagination
    yield from response.follow_all(
        css='li.next a', 
        callback=self.parse
    )

def parse_product(self, response):
    yield {
        'name': response.css('h1::text').get(),
        'price': response.css('span.price::text').get()
    }
```

## Part 6: Defining Items

### Create Item Class

```python
# items.py
import scrapy

class ProductItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    url = scrapy.Field()
    scraped_at = scrapy.Field()
```

### Use Items in Spider

```python
from tutorial_project.items import ProductItem

class ProductSpider(scrapy.Spider):
    name = 'products'
    
    def parse(self, response):
        for product in response.css('div.product'):
            item = ProductItem()
            item['name'] = product.css('h3::text').get()
            item['price'] = product.css('span.price::text').get()
            item['url'] = response.url
            
            yield item
```

## Part 7: Item Loaders

Item Loaders simplify data extraction and processing:

```python
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join

class ProductItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(str.strip, lambda x: x.replace('$', '')),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(', ')
    )

# In spider
from scrapy.loader import ItemLoader

def parse_product(self, response):
    loader = ItemLoader(item=ProductItem(), response=response)
    
    loader.add_css('name', 'h1::text')
    loader.add_css('price', 'span.price::text')
    loader.add_css('tags', 'div.tags a::text')
    
    yield loader.load_item()
```

## Part 8: Pipelines

Process items after extraction:

```python
# pipelines.py
from datetime import datetime
from itemadapter import ItemAdapter

class CleanPricePipeline:
    """Clean and convert price to float."""
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        if adapter.get('price'):
            # Remove currency symbols and convert to float
            price_str = adapter['price'].replace('$', '').replace(',', '')
            adapter['price'] = float(price_str)
        
        return item

class AddTimestampPipeline:
    """Add timestamp to items."""
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter['scraped_at'] = datetime.now().isoformat()
        return item

class DuplicatesPipeline:
    """Filter duplicate items."""
    
    def __init__(self):
        self.ids_seen = set()
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        if adapter['id'] in self.ids_seen:
            raise DropItem(f"Duplicate item: {adapter['id']}")
        
        self.ids_seen.add(adapter['id'])
        return item
```

### Enable Pipelines

```python
# settings.py
ITEM_PIPELINES = {
    'tutorial_project.pipelines.CleanPricePipeline': 100,
    'tutorial_project.pipelines.AddTimestampPipeline': 200,
    'tutorial_project.pipelines.DuplicatesPipeline': 300,
}
# Lower numbers = higher priority
```

## Part 9: CrawlSpider

For complex crawling with rules:

```python
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MyWebsiteCrawler(CrawlSpider):
    name = 'website_crawler'
    allowed_domains = ['example.com']
    start_urls = ['https://example.com']
    
    rules = (
        # Follow category pages
        Rule(
            LinkExtractor(allow=r'/category/'),
            callback='parse_category',
            follow=True
        ),
        # Follow product pages
        Rule(
            LinkExtractor(allow=r'/product/\d+'),
            callback='parse_product',
            follow=False
        ),
    )
    
    def parse_category(self, response):
        # Process category page
        yield {
            'category': response.css('h1::text').get()
        }
    
    def parse_product(self, response):
        # Process product page
        yield {
            'name': response.css('h1::text').get(),
            'price': response.css('span.price::text').get()
        }
```

## Part 10: Settings and Configuration

### Important Settings

```python
# settings.py

# Identify your bot
BOT_NAME = 'tutorial_project'
USER_AGENT = 'MyBot (+http://www.example.com/bot)'

# Respect robots.txt
ROBOTSTXT_OBEY = True

# Concurrent requests
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# Download delay (politeness)
DOWNLOAD_DELAY = 2

# Auto-throttle (dynamic delay)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10

# HTTP caching
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 86400  # 24 hours
HTTPCACHE_DIR = 'httpcache'

# Retry settings
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

# Feed export
FEED_EXPORT_ENCODING = 'utf-8'
```

## Part 11: Running Spiders

### Basic Commands

```bash
# Run spider
scrapy crawl quotes

# Export to JSON
scrapy crawl quotes -o output.json

# Export to CSV
scrapy crawl quotes -o output.csv

# Export to JSON Lines
scrapy crawl quotes -o output.jl

# Overwrite file
scrapy crawl quotes -o output.json -t json --overwrite

# Pass arguments
scrapy crawl quotes -a category=technology
```

### Using Arguments in Spider

```python
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    
    def __init__(self, category=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category = category
    
    def start_requests(self):
        url = f'http://example.com/category/{self.category}'
        yield scrapy.Request(url, callback=self.parse)
```

## Part 12: Scrapy Shell

Interactive shell for testing selectors:

```bash
# Open shell
scrapy shell 'http://quotes.toscrape.com'

# In shell:
>>> response.css('div.quote').getall()
>>> response.xpath('//div[@class="quote"]').getall()
>>> view(response)  # Opens in browser
>>> fetch('http://other-url.com')  # Fetch new URL
```

## Part 13: Middleware

### Download Middleware

```python
# middlewares.py
from scrapy import signals

class CustomDownloaderMiddleware:
    def process_request(self, request, spider):
        # Modify request before sending
        request.headers['Custom-Header'] = 'value'
        return None
    
    def process_response(self, request, response, spider):
        # Process response
        return response
    
    def process_exception(self, request, exception, spider):
        # Handle exceptions
        pass
```

### Spider Middleware

```python
class CustomSpiderMiddleware:
    def process_spider_input(self, response, spider):
        # Process response before spider
        return None
    
    def process_spider_output(self, response, result, spider):
        # Process items/requests from spider
        for item in result:
            yield item
```

## Part 14: Complete Example

```python
# spiders/books.py
import scrapy
from tutorial_project.items import BookItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    
    def parse(self, response):
        # Extract books from current page
        for book in response.css('article.product_pod'):
            yield response.follow(
                book.css('h3 a::attr(href)').get(),
                callback=self.parse_book
            )
        
        # Follow pagination
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
    
    def parse_book(self, response):
        item = BookItem()
        
        item['title'] = response.css('h1::text').get()
        item['price'] = response.css('p.price_color::text').get()
        item['availability'] = response.css('p.availability::text').re_first(r'\d+')
        item['rating'] = response.css('p.star-rating::attr(class)').re_first(r'star-rating (\w+)')
        item['description'] = response.css('#product_description + p::text').get()
        item['category'] = response.css('ul.breadcrumb li:nth-child(3) a::text').get()
        item['url'] = response.url
        
        yield item
```

## Part 15: Best Practices

### DO ✅
- Use Item classes for structured data
- Implement pipelines for data processing
- Respect robots.txt and rate limits
- Use scrapy shell for testing
- Enable HTTP caching during development
- Handle errors gracefully
- Log important events

### DON'T ❌
- Hardcode values (use settings)
- Ignore duplicate filtering
- Skip error handling
- Forget to set User-Agent
- Overwhelm servers

## Deployment

### Running in Production

```bash
# Using scrapyd
pip install scrapyd scrapyd-client

# Deploy
scrapyd-deploy

# Schedule spider
curl http://localhost:6800/schedule.json -d project=myproject -d spider=myspider
```

### Cloud Deployment

- **Scrapy Cloud** (Zyte)
- **AWS Lambda + Fargate**
- **Google Cloud Functions**
- **Heroku**

## Exercises

1. Build a spider with pagination
2. Implement custom pipeline
3. Create CrawlSpider with rules
4. Use Item Loaders

## Next Steps

Congratulations! You've mastered Scrapy!

**Next**: Module 5 for best practices and professional deployment!
