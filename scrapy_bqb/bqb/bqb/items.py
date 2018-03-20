# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BqbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 创建一个字典，key是name
    name = scrapy.Field()
    # key是addr
    addr = scrapy.Field()
