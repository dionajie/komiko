# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class KomikoItem(Item):
    image_urls = Field()
    chapter = Field()
    image_titles = Field()
    images = Field()
