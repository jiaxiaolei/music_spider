
import re

import scrapy

from base import BASE_URL
from test_torndb import * 
from test_download import *

class QuotesSpider(scrapy.Spider):
    name = "music_pdf"
    start_urls = [
        'https://www.8notes.com/scores/9765.asp',  # piano classical

    ]

    def parse(self, response):
        res  = response.xpath('//div[@id="score"]').getall()
        for item in res:
            if 'url' in item:
                p = re.compile(r'[(](.*?)[)]', re.S)
                href = re.findall(p, item)
                if href:
                    href = href[0]
                    print("------pdf href: ", href)

                    item = dict(pdf_url=href)
                    insert_music_pdf(item)

                    download_pdf(BASE_URL+href)

                else:
                    continue

    def parse2(self, response):

        res  = response.css('div.riffbox')
        for item in res:
            href = item.css('div::attr(style)').getall()
            #href = response.css('div::attr(backgroud)').getall()
            #href = response.css('div').xpath('@style').getall()
            #href = response.css('div.riffbox').extract()
            #href = response.css('div.score::text').extract()
            #href = response.css('div.score').attrib['style']
            print("------pdf href: ", href)

