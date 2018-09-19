import time
from selenium import webdriver

def getInfo():
    driver = webdriver.Firefox()
    driver.get('http://music.163.com/#/discover/toplist?id=3778678', timeout = 120)
    driver.implicitly_wait(5)
    songs = driver.find_element_by_xpath('//div[@class="ttc"]/span/a/b')
    song_links = driver.find_element_by_xpath('//div[@class = "ttc"]/span/a')
    print(songs)
    print(song_links)
    for song, song_link in zip(songs, song_links):
        print(f'{song:<10}{"https://music.163.com/#"+song_link:<}')
    driver.quit()

getInfo()
