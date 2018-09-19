import requests
from lxml import etree

r = requests.get('http://www.kugou.com/yy/rank/home/1-8888.html?from=rank')
ranks = etree.HTML(r.text).xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/ul/li/@data-index')
songs = etree.HTML(r.text).xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/ul/li/@title')
sites = etree.HTML(r.text).xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/ul/li/a/@href')
gs = '{0}\t{1:{3}<20}\t{2}'
print(gs.format('排名', '歌名', '网址', chr(12288)))
for rank, song, site in zip(ranks, songs, sites):
	print(gs.format(eval(rank)+1, song, site, chr(12288)))
