
import os

import requests

def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)

#url = 'https://www.8notes.com/school/mp32/piano/chopin_prelude_28_4.mp3'

url = 'https://www.8notes.com/school/png/piano/chopin_prelude_28_4001.png'

file_name = url.split('/')[-1]

#response = requests.get(url)

my_pdf_path = '/root/jia_scrapy/tutorial/tutorial/spiders/pdf'
my_mp3_path = '/root/jia_scrapy/tutorial/tutorial/spiders/mp3'

#path = file_path + '/%s' % file_name 

#print '----file---', file_name 

#mkdir(file_path)

#with open(path, 'wb') as f:
#    f.write(response.content)
#
#print 'end'


def download_pdf(url, file_path=None, file_name=None):

    if not file_path:
        file_path = my_pdf_path 
    
    if not file_name:
        file_name = url.split('/')[-1]

    mkdir(file_path)
    
    path = file_path + '/%s' % file_name 
    response = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)

def download_mp3(url, file_path=None, file_name=None):

    if not file_path:
        file_path = my_mp3_path 
    
    if not file_name:
        file_name = url.split('/')[-1]

    mkdir(file_path)
    
    path = file_path + '/%s' % file_name 

    response = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)


