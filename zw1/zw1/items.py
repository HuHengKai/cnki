# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Zw1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text =scrapy.Field()
    titleName =scrapy.Field()
    authorScholl=scrapy.Field()
    authorName =scrapy.Field()
    jigou =scrapy.Field()
    word =scrapy.Field()
    pass
