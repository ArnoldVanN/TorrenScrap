# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class TorrentItem(scrapy.Item):
    title = Field() 
    url = Field()
    size = Field()
    sizeType = Field()
    seed = Field()
    leech = Field()
    pass
