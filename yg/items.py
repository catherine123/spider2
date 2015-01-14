# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    fprice = scrapy.Field()
    mkprice = scrapy.Field()
    name = scrapy.Field()
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    category3 = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    
