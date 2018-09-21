# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoctorItem(scrapy.Item):
    # 医院名称
    hospitalname = scrapy.Field()
    # 科室链接
    deptlink = scrapy.Field()
    # 大科室
    bigdept = scrapy.Field()
    # 小科室
    smalldept = scrapy.Field()
    # 姓名
    name = scrapy.Field()
    # 职称
    title = scrapy.Field()
    # 简介
    introduction = scrapy.Field()