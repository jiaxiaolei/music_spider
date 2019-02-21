
import scrapy

from base import BASE_URL
from test_torndb import * 
from test_download import *

class QuotesSpider(scrapy.Spider):
    name = "music_mp3"

    data = query_music_item_all()
    print '-----data: ', data 

    start_urls_dict = {}
    for item in data:
        item_url = BASE_URL + item['item_url'] + "?ftype=mp3"
        print '-----mp3_url: ', item_url 
        #class_ = item['class']
        #subclass = item['subclass']
        
        start_urls_dict.update({item_url:item})
        #start_urls_dict.update(dict(subclass_url=item))

    print '-----start_urls_dict: ', start_urls_dict

    start_urls = start_urls_dict.keys()
    print '-----start_urls: ', start_urls
 

    # TODO
    start_urls_ = [
        'https://www.8notes.com/scores/9765.asp?ftype=mp3',  # piano classical

    ]

    def parse(self, response):

        data = self.start_urls_dict.get(response.url)

        href = response.css('a.transp_alphabet').attrib['href']
        print("------mp3 href: ", href)

        d = {'mp3_url':href,
             'mp3_name':href.split('/')[-1],
             'id':data['id']}


        insert_music_mp3(d)

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

