
import scrapy

from base import BASE_URL
from test_torndb import * 
from test_download import *

class QuotesSpider(scrapy.Spider):
    name = "music_mp3"
    start_urls = [
        'https://www.8notes.com/scores/9765.asp?ftype=mp3',  # piano classical

    ]

    def parse(self, response):

        href = response.css('a.transp_alphabet').attrib['href']
        print("------mp3 href: ", href)
        item = dict(mp3_url=href)
        insert_music_item(item)

        download_mp3(BASE_URL+href)

        return

        #for item in response.css('div.listboxmain'):
        #    for i in item.css('a.listboxrow'):
        #        
        #        
        #        href =  i.css('a.listboxrow').attrib['href']

        #        span =  i.css('span::text').extract()
        #        if len(span) != 3:
        #            continue
        #         
        #        yield {
        #            'artname': i.css('span::text').extract_first(),
        #            'href': href,
        #            'title': i.css('span::text').extract()[1],
        #            'date': i.css('span::text').extract()[2] ,
        #        }

