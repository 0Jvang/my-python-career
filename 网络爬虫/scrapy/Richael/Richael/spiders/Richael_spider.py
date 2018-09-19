# -*- coding: utf-8 -*-
import json
import scrapy
from Richael.items import RichaelItem

class RichaelSpiderSpider(scrapy.Spider):
    name = 'Richael_spider'
    # allowed_domains = ['baidu.com']
    start_urls = [f'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%88%98%E7%91%9E%E7%90%A6&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E5%88%98%E7%91%9E%E7%90%A6&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn={i}&rn=30&1536458726282=' for i in range(30,301,30)]

    def parse(self, response):
        # response.encoding = 'utf-8'
        # j = response.json()
        data = RichaelItem()
        j = json.loads(response.text)
        for i in range(30):
            img = j['data'][i]['thumbURL']
            data['images_url'] = [img]
            yield data

    # def parse_img(self, response):
    #     filename = response.url.split('/')[-1]
    #     with open(f'G:/proc/网络爬虫/scrapy/Richael/Richael/spiders/imgs/{filename}', 'wb') as f:
    #         f.write(response.body)

