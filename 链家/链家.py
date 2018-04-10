# -*- coding: utf-8 -*-
import urllib.request
import re
import csv
from bs4 import BeautifulSoup

ss=['http://sh.lianjia.com/ditiezufang/li143685036/d1l1l2', 'http://sh.lianjia.com/ditiezufang/li143685036/d2l1l2',]
out = open('lianjia1.csv', 'a', newline='', encoding='utf-8')
filednames = ['小区', '标题', '链接', '价格','户型','面积']
csv_write = csv.writer(out, dialect='excel')
csv_write.writerow(filednames)
for url in ss:
    data=urllib.request.urlopen(url).read().decode('utf-8')
    contentpat='<div class="info-panel">.*?</li>'
    contentlist=re.compile(contentpat,re.S).findall(str(data))

    for x in contentlist:
        info={}
        soup =BeautifulSoup(x,'lxml')
        info1 = soup.find('a').get('title')
        info3 = soup.select('.price')[0].text
        info2 ="http://sh.lianjia.com"+soup.find('a').get('href')
        t3=soup.find('div',class_='where')#提取div标签a标签的内容下的内容
        t4=t3.find_all('span')[0].text#提取span的内容
        t5=t3.find_all('span')[1].text
        t6=t3.find_all('span')[2].text

        stu1=(t4,info1,info2,info3,t5,t6)
        csv_write.writerow(stu1)
