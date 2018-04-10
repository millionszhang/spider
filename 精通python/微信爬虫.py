# -*- coding: utf-8 -*-
#2018-3-16  对微信公众号的爬取

import re
import urllib.request
import time
import urllib.error

#模拟成浏览器
headers = ("User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
#将opener伪装成安全局
urllib.request.install_opener(opener)
#设置一个列表listurl存储文章网址列表
listurl=[]
#自定义函数，功能为使用代理服务器
def use_proxy(proxy_addr,url):
    # 建立异常处理机制
    try:
        import urllin.request
        proxy= urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPBasicAuthHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    # 若为url异常延迟10秒执行
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
        # 若为Except异常，延迟1秒执行
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)
#获取所有文章链接
def getlisturl(key,pagestart,pagend,proxy):
    try:
        page = pagestart
        #编码关键词key
        keycode=urllib.request.quote(key)
        #编码&page
        pagecode=urllib.request.quote("&page")
        #循环爬取各页的url链接，每次循环构建一次
        url="http://weixin.sogou.com/weixin?type2&query="+keycode+pagecode+str(page)
        #用代理服务器爬取，解决ip被封杀问题
        data1=use_proxy(proxy,url)
        #获取文章链接的正则表达式
        listurlpat='<div class="txt-box">.*?(http//.*?)"'
        #获取每页的所有文章链接并添加到列表listurl中
        listurl.apend(re.compile(listurlpat,re.S).findall(data1))
        print("共获取到"+str(len(listurl))+"页")#便于调试
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #若为UrlError，延时10秒执行
        time.sleep(10)
    except Exception as e:
        print("ecception:"+str(e))
        #若为Exception异常，延时1秒执行
        time.sleep(1)
        #通过文章链接获取相对应的内容
def getcontent(listurl,proxy):
    i=0
    #设置本地文件中的开始html编码
    html1='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content="text/html; charset=utf-8"  />
    <title>微信文章页面</title>
    </head>
    <body>'''
    fh=open('1.html',"wb")
    fh.write(html1.encode("utf-8"))
    fh.close()
    #再次以追加写入的方式打开文件，以写入对应文章内容
    fh=open('1.html',"ab")
    #此时listurl为二维列表，形如listurl[][],第一维存储的信息跟第几页相关，第二维存储的跟该页第几个文章链接相关
    for i in range(0,len(listurl)):
        for j in range(0,len(listurl[i])):
            try:
                url= listurl[i][j]
                #处理成真实url
                url=url.replace("amp;","")
                #使用代理去爬取对应网址的内容
                data=use_proxy(proxy,url)
                #文章标题正则表达式
                titlepat="<title>(.*?)<title>"
                #文章内容正则表达式
                contentpat='id="js_content">(.*?)id="js_sg_bar"'
                #通过对应正则表达找到标题并赋给列表title
                title=re.compile(titlepat).findall(data)
                #通过对应正则表达式找到内容并赋给列表content
                content=re.compile(contentpat,re.S).findall(data)
                #初始化标题与内容
                thistitle="此次没有获取到"
                thiscontent="此次没有获取到"
                #如果标题列表不为空，说明找到标题，取列表第零个元素，即此次标题赋给变量thistitle
                if(title!=[]):
                    thistitle-title[0]
                if(content!=[]):
                    thiscontent=content[0]
                #将标题与内容汇总赋给变量dataall
                dataall="<p>标题为:"+thistitle+"</p><p>内容为:"+thiscontent+"</p><br>"
                #将该篇文章的标题与内容的总信息写入对应文件
                fh.write(dataall.encode("utf-8"))
                print("第"+str(i)+"个网页第"+str(j)+"次处理")#便于调试
            except urllib.error.URLError as e:
                if hasattr(e,"code"):
                    print(e.code)
                if hasattr(e,"content"):
                    print(e.reason)
                #若为urlerror异常，延迟10秒执行
                time.sleep(10)
            except Exception as e:
                print("exception:"+str(e))
                #若为exception异常，延迟1秒执行
                time.sleep(1)
                fh.close()
                #设置并写入本地文件的HTML后面结束部分代码
                html2='''</body>
        </html>'''
                fh=open('1.html',"ab")
                fh.write(html2.encode("utf-8"))
                fh.close()
                #设置关键词
            key="物联网"
            #设置代理服务器，该代理服务器有可能失效，读者需要换成新的有效的代理服务器
            proxy="119.6.136.122:80"
            #可以为getlisturl与getcontent设置不同的代理服务器，此处没有启用该项设置
            proxy2=""
            #起始页
            pagestart=1
            #爬取到哪页
            pageend=2
            listurl=getlisturl(key,pagestart,pageend,proxy)
            getcontent(listurl,proxy)
