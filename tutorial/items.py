# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


class TutorialItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class TutorialItem(Item):
    url = Field()
    name = Field()
    pass
