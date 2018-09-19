# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
	name = 'douban_spider'
	# allowed_domains = ['movies.com']
	#扔进调度器
	start_urls = ['https://movie.douban.com/top250']

	def parse(self, response):
		movie_list = response.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li')
		db = DoubanItem()
		def patt(s):
			return i.xpath(s).extract()
		for i in movie_list:
			db['rank'] 		  = patt('.//em/text()')
			db['name'] 		  = patt('./div/div[2]/div[1]/a/span[1]/text()')
			info = patt('./div/div[2]/div[2]/p[1]/text()')
			info = '\n'.join([i for i in map(lambda x:x.replace('\xa0', '').strip(), info)])
			db['info'] 		  = info
			db['star'] 		  = patt('./div/div[2]/div[2]/div/span[2]/text()')
			db['evaluate']    = patt('./div/div[2]/div[2]/div/span[4]/text()')
			db['description'] = patt('./div/div[2]/div[2]/p[2]/span/text()')
			#将数据发送给piplines
			yield db
		next_page = response.xpath('/html/body/div[3]/div[1]/div/div[1]/div[2]/span[3]/a/@href').extract()[0]
		if next_page:
			#将请求发送给调度器
			yield scrapy.Request('https://movie.douban.com/top250' + next_page, callback = self.parse)