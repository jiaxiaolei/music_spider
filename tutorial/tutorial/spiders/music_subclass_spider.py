
import scrapy

from test_torndb import * 

from base import BASE_URL

class QuotesSpider(scrapy.Spider):
    name = "music_subclass"

    data = query_music_class_all()
    print '-----data: ', data 

    start_urls_dict = {}
    for item in data:
        subclass_url = BASE_URL + item['subclass_url']
        #class_ = item['class']
        #subclass = item['subclass']
        
        start_urls_dict.update({subclass_url:item})
        #start_urls_dict.update(dict(subclass_url=item))

    print '-----start_urls_dict: ', start_urls_dict

    start_urls = start_urls_dict.keys()
    print '-----start_urls: ', start_urls
    
    start_urls_ = [
        'https://www.8notes.com/piano/classical/sheet_music/', # piano classical

    ]

    def parse(self, response):

        data = self.start_urls_dict.get(response.url)
 
        for item in response.css('div.listboxmain'):
            for i in item.css('a.listboxrow'):
                
                
                href =  i.css('a.listboxrow').attrib['href']

                span =  i.css('span::text').extract()
                if len(span) != 3:
                    continue

                artname = i.css('span::text').extract_first()
                title =  i.css('span::text').extract()[1]
                date =  i.css('span::text').extract()[2]
     
                item = {'class':data['class'],
                           'subclass':data['subclass'],
                            'subclass_url':data['subclass_url'],
                            'item_url':href,
                            'artname':artname,
                            'title':title,
                            'date':date}

                insert_music_subclass(item)
                 
                yield {
                    'artname': i.css('span::text').extract_first(),
                    'href': href,
                    'title': i.css('span::text').extract()[1],
                    'date': i.css('span::text').extract()[2] ,
                }

