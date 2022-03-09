# %%
#import dependencies
#requirements: 
# pip install scrapy
import re
import os
from typing import Counter
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.url import url_query_cleaner

# %%
#clean urls
def process_links(links):
    for link in links:
        link.url = url_query_cleaner(link.url)
        yield link

# %%
class KingstonCrawler(CrawlSpider):
    name = 'kingston'
    allowed_domains = ['www.cityofkingston.ca']
    start_urls = ['https://www.cityofkingston.ca/']
    rules = (
        Rule(
            LinkExtractor(
                deny=[
                    re.escape('https://www.cityofkingston.com/offsite'),
                    re.escape('https://www.cityofkingston.com/whitelist-offsite'),
                ],
            ),
            process_links=process_links,
            callback='parse',
            follow=True,
        ),
    )
    def parse(self, response):
        yield {
            'url': response.url,
            'status': response.status,
            'lang': response.headers.getlist('Content-Language'),
            'updated': response.headers.getlist('Last-Modified'),
            'text': str(response.body)
        }