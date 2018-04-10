# --*-- conding: utf-8 --*--
#2018-3-21 对网易音乐的代码重写 和对方法的理解
import xlwt
import requests
from bs4 import BeautifulSoup
import re

#定义这个方法是用requests 库来打开网页
def get_url(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('woring......')

def singer_url(url):
    html = get_url(url)
    soup = BeautifulSoup(html,'html.parser')
    cont = soup.find_all('div',attrs={'class':'u-cover u-cover-5'})
    singers=[]
    for cont1 in cont:
        cont2 = 'http://music.163.com'+cont1.find('a').get('href')
        singers.append(cont2)

def song_info(singers):
    for singer in singers:
        try:
            songs=get_url(singer)
            soup = BeautifulSoup(songs,'html.parser')

            info = soup.find_all('texarea',attrs={'style:display:none'})[0]
            songs_url_and_name = soup.find_all('ul',atters={'class':'f-hide'})[0]
            datas=[]
            data1 = re.findall(r'"album".*?"name":"(.*?)".*?', str(info.text))
            data2 = re.findall(r'.*?<li><a href="(/song\?id=\d+)">(.*?)</a></li>.*?', str(songs_url_and_name))

            for i in range(len(data2)):
                datas.append([data2[i][1], data1[i], 'http://music.163.com/#' + str(data2[i][0])])

            save_excel(singer,datas)
        except:
            continue


def save_excel(singer, datas):
    fpath = 'C:\\Users\\Administrator\\Desktop\\python\\图片'
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)
    sheet1.col(0).width = (25 * 256)
    sheet1.col(1).width = (30 * 256)
    sheet1.col(2).width = (40 * 256)
    # xlwt中列宽的值表示方法：默认字体0的1/256为衡量单位。
    # xlwt创建时使用的默认宽度为2960，既11个字符0的宽度
    # 所以我们在设置列宽时可以用如下方法：
    # width = 256 * 20    256为衡量单位，20表示20个字符宽度

    heads = ['歌曲名称', '专辑', '歌曲链接']
    count = 0

    print('正在存入文件......')
    for head in heads:
        sheet1.write(0, count, head)
        count += 1

    i = 1
    for data in datas:
        j = 0
        for k in data:
            sheet1.write(i, j, k)
            j += 1
        i += 1

    book.save(fpath + str(singer[1]) + '.xls')  # 括号里写存入的地址
    print('OK！')


def main():
    url = 'http://music.163.com/discover/artist/cat?id=1001'  # 华语男歌手页面
    singer_url(url)


main()