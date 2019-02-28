

介绍
======
本文档介绍 music_spider 的使用。

music 数据源：
https://www.8notes.com/

抓取需求：

www.8notes.com 有很多类乐器，每类乐器又会有自己的子类。
每个分类下有很多曲目，每个曲目有自己作者、音乐、乐谱、发布时间。
这里要做的就是把每个曲目有自己作者、音乐、乐谱、发布时间按类抓取下来。



使用 python spacy 进行html 页面分析;
使用 mysql 进行数据存储；
使用 torndb 作为 pyhton 接入 mysql 的驱动；


主要目录：
$ yum install tree
$ tree -L 4
.
|-- README.md             # 项目介绍文档
`-- tutorial
    |-- josn_keep  # .json 文件为执行代码时导出的数据
    |-- requirements.txt  # 运行项目需要的python 模块
    |-- scrapy.cfg  # scrapy 默认生成的配置文件。目前为空，没有做特殊配置。
    `-- tutorial # 运行项目
        |-- __init__.py
        |-- items.py
        |-- middlewares.py
        |-- pipelines.py
        |-- settings.py
        `-- spiders
            |-- base.py  # 一些基本的环境变量
            |-- __init__.py
            |-- mp3      # mp3 的下载保存路径
            |-- music_class_spider.py  # 针对子类的处理
            |-- music_item_spider.py  # 针对曲目的处理
            |-- music_mp3_spider.py  # 针对mp3的处理
            |-- music_pdf_spider.py  # 针对乐谱的处理
            |-- music_subclass_spider.py
            |-- pdf    # 乐谱的下载保存路径
            |-- quotes_content_spider.py
            |-- quotes_spider.py
            |-- sql   # 项目初始化mysql需要的表结构
            |-- test_download.py
            |-- test_torndb.py  # 操作数据库


主要数据表：

music_class: 保存子类信息

music_item：保存完整信息



安装
=======
python： 2.7.14+

$ pip install -r requirements.txt

(NOTE: 通过  pip freeze > requirements.txt 导出项目依赖的 python 模块)


使用
======


进入到相应的session:

$ screen -x jia_scrapy


进入 tutorial 目录：
$ cd tutorial


# 获取子类：
$ scrapy crawl music_class  -o json_keep/music_class.json

# 获取曲目：
$ scrapy crawl music_item -o json_keep/music_item.json


# 获取 mp3
$ scrapy crawl music_mp3  -o json_keep/music_mp3.json

# 获取 pdf
$ scrapy crawl music_pdf -o json_keep/music_pdf.json


