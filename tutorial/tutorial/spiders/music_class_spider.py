
import scrapy

from test_torndb import * 

class QuotesSpider(scrapy.Spider):
    name = "music_class"

    start_urls_dict = {'https://www.8notes.com/piano/':'piano',
                       'https://www.8notes.com/guitar/':'guitar',
                       'https://www.8notes.com/violin/':'violin',
                       'https://www.8notes.com/flute/':'flute',
                       'https://www.8notes.com/saxophone/': 'altosax',
                       'https://www.8notes.com/voice/': 'voice',
                       'https://www.8notes.com/clarinet/': 'clarinet',
                       'https://www.8notes.com/trumpet/': 'trumpet',
                       'https://www.8notes.com/viola/': 'viola',
                       'https://www.8notes.com/trombone/': 'trombone',
                       'https://www.8notes.com/cello/': 'cello'

                                 } 


    start_urls = start_urls_dict.keys()

    start_urls_ = [
        'https://www.8notes.com/piano/', # piano
        'https://www.8notes.com/guitar/', # guitar
        'https://www.8notes.com/violin/', # violin
        'https://www.8notes.com/flute/', # flute
        'https://www.8notes.com/saxophone/', # altosax
        'https://www.8notes.com/voice/', # voice
        'https://www.8notes.com/clarinet/', # clarinet
        'https://www.8notes.com/trumpet/', # trumpet
        'https://www.8notes.com/viola/', # viola
        'https://www.8notes.com/trombone/', # trombone
        'https://www.8notes.com/cello/', # cello
        'https://www.8notes.com/drums/sheet_music/', # drums sheet
        'https://www.8notes.com/percussion/all/', # percussion all
        'https://www.8notes.com/recorder/', # recorder subclass
        'https://www.8notes.com/oboe/', # oboe  
        'https://www.8notes.com/bass_guitar/', # bass guitar
        'https://www.8notes.com/french_horn/', # horn
        'https://www.8notes.com/bassoon/', # bassoon
        'https://www.8notes.com/tuba/', # tuba
        'https://www.8notes.com/double_bass/all/', # double_bass all
        'https://www.8notes.com/organ/sheet_music/', # organ sheet
        'https://www.8notes.com/euphonium/all/', # euphonium  all
        'https://www.8notes.com/banjo/all/', # banjo all
        'https://www.8notes.com/mandolin/all/', # mandolin all
        'https://www.8notes.com/ukulele/', # ukulele
        'https://www.8notes.com/strings/', # strings
        'https://www.8notes.com/wind/', # wind
        'https://www.8notes.com/guitar_groups/', # guitar_group
        'https://www.8notes.com/brass/', # brass
        'https://www.8notes.com/mixed/', # mixed
        'https://www.8notes.com/classroom/', # classroom
        'https://www.8notes.com/keyboards/', # keyboards # special
   
    ]

    def parse(self, response):
        #for key, value in start_urls_dict.items():

        class_ = self.start_urls_dict.get(response.url)

        for item in response.css('a.gs'):
            subclass_lst =  item.css('a.gs::text').extract()
            subclass = ' '.join(subclass_lst).strip()

            subclass_url =  item.css('a.gs').attrib['href']

            data = {'class':class_,
                    'subclass':subclass,
                    'subclass_url':subclass_url,
                    }

            insert_music_class(data) 

            yield {
                #'text': item.extract_first(),
                #'text': item.extract(),
                'subclass': item.css('a.gs::text').extract(),
                #'text': item.css('span.text::text').extract_first(),
                #'author': item.css('small.author::text').extract_first(),
                #'tags': item.css('div.tags a.tag::text').extract(),
            }

