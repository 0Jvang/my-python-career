# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RichaelItem(scrapy.Item):
    # define the fields for your item here like:
    images_url = scrapy.Field()

class ImageItem(scrapy.Item):
    """docstring for ImageItem"""
    images_url = scrapy.Field()
    images = scrapy.Field()
		