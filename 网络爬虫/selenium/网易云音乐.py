import time
from selenium import webdriver
from lxml import etree
driver = webdriver.Firefox()
driver.get('http://music.163.com/#/discover/toplist?id=3778678')
driver.implicitly_wait(5)
p = etree.HTML(driver.page_source)
songs = p.xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div[1]/table/tbo\
dy/tr/td[2]/div/div/div/span/a/b/@title')
song_links= p.xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div[1]/tabl\
e/tbody/tr/td[2]/div/div/div/span/a/@href')
try:
    for song, song_link in zip(songs, song_links):
        print(f'{song:<10}{"https://music.163.com/#"+song_link:<}')
except:
    pass
driver.quit()
