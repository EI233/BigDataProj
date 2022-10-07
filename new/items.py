# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewItem(scrapy.Item):
    name = scrapy.Field()
    view = scrapy.Field()
    thumb = scrapy.Field()
    coin = scrapy.Field()
    favor = scrapy.Field()
    forward= scrapy.Field()
