
import scrapy

from test_torndb import * 

class QuotesSpider(scrapy.Spider):
    name = "music_list"
    start_urls = [
        'https://www.8notes.com/piano/classical/sheet_music/', # piano classical

    ]

    def parse(self, response):
        for item in response.css('div.listboxmain'):
            for i in item.css('a.listboxrow'):
                
                
                href =  i.css('a.listboxrow').attrib['href']

                span =  i.css('span::text').extract()
                if len(span) != 3:
                    continue

                artname = i.css('span::text').extract_first()
                title =  i.css('span::text').extract()[1]
                date =  i.css('span::text').extract()[2]
     
                item = dict(item_url=href,
                            artname=artname,
                            title=title,
                            date=date,)
                insert_music_list(item)
                 
                yield {
                    'artname': i.css('span::text').extract_first(),
                    'href': href,
                    'title': i.css('span::text').extract()[1],
                    'date': i.css('span::text').extract()[2] ,
                }

