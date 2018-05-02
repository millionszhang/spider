import urllib
from bs4 import BeautifulSoup
import re
import csv
import requests
'''
url = "https://search.51job.com/list/020000,000000,0000,00,9,99,%25E5%25AE%259E%25E4%25B9%25A0%25E7%2594%259F,2,1.html?"
data = urllib.request.urlopen(url).read().decode('gbk')
urlpat = '<div class="el".*?</span>'
urllist = re.compile(urlpat,re.S).findall(data)
list = []
for x in urllist:
    info={}
    soup=BeautifulSoup(x,'lxml')
    info1 = soup.find('a')

    if  info1 is None:
        pass
    else:
        info2 = info1.get('href')
        if "show_job_detail" in info2:
            pass
        else:
            list.append(info2)
for y in list:
   html = urllib.request.urlopen(y).read().decode('gbk')
   contentpat = '<div class="in".*?<div class="e"'
   content = re.compile(contentpat,re.S).findall(html)
   for z in content:
       soup = BeautifulSoup(z,'lxml')
       '''
out = open('51job.csv','a',newline='',encoding='utf-8')
filenames = ['职位','位置','公司名称','信息','待遇','职位信息','联系方式','公司信息','','']
csv_write = csv.writer(out,dialect = 'excel')
csv_write.writerow(filenames)
url = "https://jobs.51job.com/shanghai-mhq/101559864.html?s=01&t=0"
html = urllib.request.urlopen(url).read().decode('gbk')
#print(html)
contentpat = '<div class="tHeader tHjob">.*?<div class="tCompany_sidebar">'
cont=re.compile(contentpat,re.S).findall(html)
for i in cont:
    soup = BeautifulSoup(i,'lxml')
    info = soup.find('h1').get('title')
    info1 = soup.find('span').text
    info2 = soup.find('strong').text
    info3 = soup.find('a').get('title')
    info4 = soup.find('a').get('href')
    info5 = soup.find('p',class_='msg ltype').text
    info6 = soup.find('p',class_='t2').text
    info7 = soup.find('div',class_='bmsg job_msg inbox').text
    info8 = soup.find('span',class_='label').text
    info9 = soup.find('div',class_='tmsg inbox').text
    stu1 = (info,info1,info2,info3,info4,info5,info6,info7,info8,info9)
    print(info,info1,info2,info3,info4,info5,info6,info7,info8,info9)
    csv_write.writerow(stu1)