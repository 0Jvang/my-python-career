import requests,bs4,time
from bs4 import BeautifulSoup

def GetHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def FillUnivList(ulist,html):
    soup=BeautifulSoup(html,"lxml")
    for tr in soup.findall("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[3].string])

def PrintUnivList(ulist,num):
    GS="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(GS.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        print(GS.format(ulist[i][0],ulist[i][1],ulist[i][2],chr(12288)))

def main():
    ulist=[]
    url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html=GetHtmlText(url)
    FillUnivList(ulist,html)
    PrintUnivList(ulist,20)
stime=time.time()
main()
print(time.time()-stime)
