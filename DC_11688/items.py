# -*- coding: utf-8 -*-
import scrapy


class Dc11688Item(scrapy.Item):
    title = scrapy.Field()
    abstract = scrapy.Field()
    topic_id = scrapy.Field()
    tag = scrapy.Field()
