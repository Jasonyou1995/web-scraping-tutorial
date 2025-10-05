"""
Scrapy Settings
Configure your Scrapy project settings here.
"""

BOT_NAME = 'tutorial_scrapy'

SPIDER_MODULES = ['tutorial_scrapy.spiders']
NEWSPIDER_MODULE = 'tutorial_scrapy.spiders'

# Crawl responsibly by identifying yourself
USER_AGENT = 'tutorial_scrapy (+https://github.com/Jasonyou1995/web-scraping-tutorial)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests
CONCURRENT_REQUESTS = 16

# Configure a delay for requests
DOWNLOAD_DELAY = 2

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Configure item pipelines
ITEM_PIPELINES = {
   'tutorial_scrapy.pipelines.CleanDataPipeline': 300,
}

# Enable and configure HTTP caching (disabled by default)
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'

# Set settings whose default value is deprecated
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'
