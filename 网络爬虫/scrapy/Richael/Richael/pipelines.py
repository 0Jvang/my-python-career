# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql, settings
from pymysql import connections

class RichaelPipeline(object):
	def process_item(self, item, spider):

		host = settings.MYSQL_HOST
		user = settings.MYSQL_USER
		passwd = settings.MYSQL_PASSWORD
		db = settings.MYSQL_DB
		charset = settings.CHARSET
		port = settings.MYSQL_PORT

		con = pymysql.connect(host=host, user=user, passwd=passwd, db=db, charset=charset, port=port)
		cue = con.cursor()
		print("mysql connect succes")#测试语句，这在程序执行时非常有效的理解程序是否执行到这一步

		try:
			cue.execute("insert into SongsOfRichael (rank,name,link) values(%s,%s,%s)",[item['rank'],item['name'],item['link']])
			print("insert success")#测试语句
		except Exception as e:
			print('Insert error:',e)
			con.rollback()
		else:
			con.commit()
		con.close()
		return item	

class ImagePipeline(object):
	"""docstring for ImagePipeline"""
	pass