# -*- coding: utf-8 -*-
import scrapy


class GithubSpiderSpider(scrapy.Spider):
    name = 'github_spider'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']
    url = 'https://github.com/session'

    def parse(self, response):
        token = response.xpath('//input[@name="authenticity_token"]/@value')
        if token:
            token = token.extract_first()
        data = {
                'commit':'Sign+in',
                'login':'a913536021@qq.com',
                'password':'iambleach2',
                'utf8':'✓',
                'authenticity_token':token
                }
        yield scrapy.FormRequest(self.url, formdata=data, callback=self.after_login)
        
    def after_login(self,response):
        with open('github.html','wb') as f:
            f.write(response.body)
