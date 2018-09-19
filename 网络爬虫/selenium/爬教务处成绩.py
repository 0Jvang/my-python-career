import requests, time
from selenium import webdriver
from lxml import etree

def getInfo():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get('http://jwxt.swpu.edu.cn/')
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[3]/tbody/tr/t\
d[2]/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input').clear()
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[3]/tbody/tr/t\
d[2]/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input').send_keys('201531010311')
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[3]/tbody/tr/t\
d[2]/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').clear()
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[3]/tbody/tr/t\
d[2]/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').send_keys('635423')
    #showVcode()
    vcode = input('请输入验证码：')
    
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[3]/tbody/tr/t\
##d[2]/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(vcode)
    driver.find_element_by_xpath('//*[@id="btnSure"]').click() 
    
    try:
        driver.get(current_url)
        driver.find_element_by_xpath('//*[@id="moduleTab"]/tbody/tr/td[7]/a').click()
        driver.find_element_by_xpath('//*[@id="project"]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/a').click()
        p = etree.HTML(driver.get(current_page))
        names = p.xpath('//*[@id="user"]/thead/tr/td[3]/text')
        grades = p.xpath('//*[@id="user"]/thead/tr/td[10]/text')
        for name, grade in zip(names, grades):
            print(f'{name:<10}{grade}')
    except:
        getInfo()


def showVcode():
    driver.get(current_page)
    img = driver.find_element_by_xpath('//*[@id="vchart"]')
    print(type(img))
    print(img)
##    with open('验证码.jpg', 'wb') as f:
##        f.write(content)
##    im = Image.open('验证码.jpg')
##    im.show()
getInfo()
