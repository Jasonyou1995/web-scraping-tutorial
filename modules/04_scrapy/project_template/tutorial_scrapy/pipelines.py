"""
Scrapy Pipelines
Process scraped items here.
"""

from datetime import datetime
from itemadapter import ItemAdapter


class CleanDataPipeline:
    """Clean and validate scraped data."""
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        # Clean price - remove $ and convert to float
        if adapter.get('price'):
            price_str = adapter['price'].replace('$', '').replace(',', '')
            try:
                adapter['price'] = float(price_str)
            except ValueError:
                adapter['price'] = 0.0
        
        # Add timestamp
        adapter['scraped_at'] = datetime.now().isoformat()
        
        return item
