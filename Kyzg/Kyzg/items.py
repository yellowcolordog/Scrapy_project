# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KyzgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 项目名称, 报酬, 开发限时, 已竞标人数,
    # 发布时间, 页面加载地址/project/detail.html?id=13540374 id经过简单加密
    name = scrapy.Field()
    price = scrapy.Field()
    lim_time = scrapy.Field()
    renshu = scrapy.Field()
    pub_time = scrapy.Field()
    link = scrapy.Field()
