"""
Scrapy Items
Define the data structures for scraped items.
"""

import scrapy


class ProductItem(scrapy.Item):
    """Product item definition."""
    
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    stock = scrapy.Field()
    url = scrapy.Field()
    scraped_at = scrapy.Field()
