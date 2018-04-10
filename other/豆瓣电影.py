#--*-- conding:utf-8 --*--
import urllib.request
import re
import requests
import csv
import time
from bs4 import BeautifulSoup

def get_urllist():
    url='https://read.douban.com/topic/1577/?start=90&limit=30'
    data=urllib.request.urlopen(url).read().decode('utf-8')
    pat='<div class="border-wrap">.*?</div>'
    contlist= re.compile(pat).findall(str(data))
    urllist=[]
    for cont in contlist:
        soup=BeautifulSoup(cont,'lxml')
        info=soup.find('a')
        info2='https://read.douban.com'+info.get('href')
        urllist.append(info2)
    print(urllist)
    return (urllist)
def get_content(urllist):
    for url in urllist:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        t1 = soup.find('div', class_='article-profile-bd').find('h1').text
        t2 = soup.find('a', class_='author-item').text
        t3 = soup.find('span', class_='score').text
        stu1 = (t1, t2, t3,)
        out = open('豆瓣书单.csv', 'a', newline='', encoding='utf-8')
        csv_write = csv.writer(out, dialect='excel')
        csv_write.writerow(stu1)
url=get_content(get_urllist())



