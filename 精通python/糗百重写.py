# -*- coding: utf-8 -*-

import urllib.request
import re
from bs4 import BeautifulSoup

def getcontent(url):
    headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #将opener伪装成浏览器
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(data,'lxml')
    info=soup.find_all(name='div',attrs={"class":("content")})
    for i in info:
        info1=i.find(name="span").text
        print(info1)
getcontent("https://www.qiushibaike.com/")


