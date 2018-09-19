# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Test1Spider(CrawlSpider):
    name = 'Test1'
    allowed_domains = ['test.com']
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=538&workExperience=-1&education=-1&compa\
        nyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%\
        22:%22538%22,%22kw%22:%22python%22,%22kt%22:%223%22%7D']

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        r = response.json()
        print(r)
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
