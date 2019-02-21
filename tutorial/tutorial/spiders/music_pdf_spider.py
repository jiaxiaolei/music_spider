
import re

import scrapy

from base import BASE_URL
from test_torndb import * 
from test_download import *

class QuotesSpider(scrapy.Spider):
    name = "music_pdf"

    data = query_music_item_all()
    print '-----data: ', data 

    start_urls_dict = {}
    for item in data:
        item_url = BASE_URL + item['item_url']
        #class_ = item['class']
        #subclass = item['subclass']
        
        start_urls_dict.update({item_url:item})
        #start_urls_dict.update(dict(subclass_url=item))

    print '-----start_urls_dict: ', start_urls_dict

    start_urls = start_urls_dict.keys()
    print '-----start_urls: ', start_urls
 

    start_urls_ = [
        'https://www.8notes.com/scores/9765.asp',  # piano classical

    ]

    def parse(self, response):

        data = self.start_urls_dict.get(response.url)

        res  = response.xpath('//div[@id="score"]').getall()
        for item in res:
            if 'url' in item:
                p = re.compile(r'[(](.*?)[)]', re.S)
                href = re.findall(p, item)
                if href:
                    href = href[0]
                    print("------pdf href: ", href)

                    d = {'pdf_url':href,
                         'pdf_name':href.split('/')[-1],
                         'id':data['id']
                        }
                    insert_music_pdf(d)

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

