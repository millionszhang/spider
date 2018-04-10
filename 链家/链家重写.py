# --*-- conding: utf-8 --*--
#2018-3-28   对链家爬虫的重写  对代码的优化

import urllib
import re
from bs4 import BeautifulSoup

def  get_url(url):
    page=int(input(print("请输入页数")))
    urllist=[]
    for i in range(1,page):
        aurl = url+"d"+str(1)+"1112"
        urllist.append(aurl)
    return(urllist)

def get_content(urllist):
    for url in urllist:
        data = urllib.request.urlopen(url).read().decode('utf-8')
        contentpat = '<div class="info-panel">.*?</li>'
        contentlist = re.compile(contentpat, re.S).findall(str(data))
        for x in contentlist:
            info = {}
            soup = BeautifulSoup(x, 'lxml')
            info1 = soup.select('.fang-subway-ex')[0].text
            info3 = soup.select('.price')[0].text
            info4 = soup.select('.price-pre')[0].text
            info5 = soup.select('.where')[0].text
            info6 = soup.find('h2')
            t3 = re.compile('/.*?.html').findall(str(info6))
            info7 = soup.find('h2').text
            print(t3, info1, info3, info4, info7, info5, )

if __name__=='__main__':
    url='https://sh.lianjia.com/ditiezufang/li143685065/'




