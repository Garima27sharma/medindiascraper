# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MedindiaItem(scrapy.Item):
    # define the fields for your item here like:
    drug_name = scrapy.Field()
    drug_form = scrapy.Field()
    generic_name = scrapy.Field()
    price = scrapy.Field()
    dosage = scrapy.Field()
    conditions = scrapy.Field()
    side_Effects = scrapy.Field()
    indications = scrapy.Field()
    how_To_Take = scrapy.Field()
    contraindications = scrapy.Field()
    warning = scrapy.Field()
    other_Precautions = scrapy.Field()
    storage = scrapy.Field()
    pass