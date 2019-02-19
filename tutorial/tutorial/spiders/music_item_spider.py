import scrapy

class QuotesSpider(scrapy.Spider):
    name = "music_item"
    start_urls = [
        'https://www.8notes.com/scores/7063.asp', # piano classical

    ]

    def parse(self, response):
        for item in response.css('div.listboxmain'):
            for i in item.css('a.listboxrow'):
                
                
                href =  i.css('a.listboxrow').attrib['href']

                span =  i.css('span::text').extract()
                if len(span) != 3:
                    continue
                 
                yield {
                    'artname': i.css('span::text').extract_first(),
                    'href': href,
                    'title': i.css('span::text').extract()[1],
                    'date': i.css('span::text').extract()[2] ,
                }

