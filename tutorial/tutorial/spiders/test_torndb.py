# *_* coding=utf8 *_*

import sys
reload(sys)
sys.setdefaultencoding('utf8')


import torndb

host = "172.28.39.183:3306"
db_name = "music_spider"

db = torndb.Connection(host, db_name, user="root", password="root")
#for item in db.query("SELECT * FROM music"):
#    print item
#    print item.id
#    #print utf8(item['title'])


#sql_cmd = 'INSERT INTO music(class,subclass,title,artname,pdf_url) values("paino","66","66","66","66")'
#db.execute(sql_cmd)
#db.execute('insert into music values("66","66","66", ""66")')


"""Functions
"""

def insert_subclass():
    pass

def insert_music_item(item):
    """
    item = {"artname":"",
            "title":"",
            "date":""}
    """

    sql_cmd = 'INSERT INTO music(class,subclass,title,artname,pdf_url, mp3_url)  values("paino","66","66","66","66", "%s")' % item['mp3_url']

    print "sql_cmd", sql_cmd
    db.execute(sql_cmd)


def insert_music_pdf(item):
    """
    """
   
    sql_cmd = 'INSERT INTO music(class,subclass,title,artname,pdf_url, mp3_url)  values("paino","66","66","66","%s","66")' % item['pdf_url']

    print "sql_cmd", sql_cmd
    db.execute(sql_cmd)


def insert_music_list(item):
 
    sql_cmd = 'INSERT INTO music(artname, title, date, item_url)  values("%s","%s", "%s", "%s")' % (item['artname'], item['title'], item['date'], item['item_url'])

    print "sql_cmd", sql_cmd
    db.execute(sql_cmd)

# okay
def insert_music_class(item):
 
    sql_cmd = 'INSERT INTO music_class(class, subclass, subclass_url)  values("%s","%s", "%s")' % (item['class'], item['subclass'], item['subclass_url'] )

    print "sql_cmd", sql_cmd
    db.execute(sql_cmd)

def insert_music_subclass(item):
    print '---item: ', item
 
    sql_cmd = 'INSERT INTO music_item(class, subclass, subclass_url, artname, title, date, item_url)  values("%s","%s", "%s", "%s", "%s", "%s", "%s")' % (item['class'], item['subclass'], item['subclass_url'], item['artname'], item['title'], item['date'], item['item_url'] )

    print "sql_cmd", sql_cmd

    db.execute(sql_cmd)



"""Query
"""
def query_music_class_all():
    res = db.query('SELECT * FROM music_class ')
    return res 


def query_music_by_id(id=1):
    res = db.query('SELECT * FROM music WHERE id = %s', id)
    print '----res:', res


