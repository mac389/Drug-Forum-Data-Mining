# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ErowidItem(Item):
    Title = Field(serializer=str)
    Author = Field(serializer=str)
    Text = Field(serializer=str)
    Substance = Field(serializer=str)
    # name = scrapy.Field()
