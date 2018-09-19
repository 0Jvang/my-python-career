import requests,re,time
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding =r.apparent_encoding
        return r.text
    except:
        return ""
     
def parsePage(ilt, html):
    count=0
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            count+=1
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
            print("\r当前进度：{:.%}".format(count/len(plt)),end=" ")
    except:
        print("")
 
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print("")
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count +=1
        print(tplt.format(count, g[0], g[1]))
         
def main():
    goods = '男鞋'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
     
main()
time.sleep(900)
