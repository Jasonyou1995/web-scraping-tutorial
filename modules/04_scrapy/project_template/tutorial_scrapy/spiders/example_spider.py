"""
Example Spider
A basic Scrapy spider to demonstrate structure.
"""

import scrapy
from tutorial_scrapy.items import ProductItem


class ExampleSpider(scrapy.Spider):
    """Example spider for scraping quotes."""
    
    name = 'example'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        """Parse the main page and extract quotes."""
        
        # Extract quotes
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        
        # Follow pagination
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
