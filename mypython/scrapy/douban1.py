from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import threading
import time
import os

#获取豆瓣大图，从一个影视所有图片进入https://movie.douban.com/subject/1830528/all_photos，


def get_html(web_url):  # 爬虫获取网页没啥好说的
    header = {
        "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
    html = requests.get(url=web_url, headers=header).text#不加text返回的是response，加了返回的是字符串
    soup = BeautifulSoup(html,"html.parser")
    data = soup.find('ul',{'class':'pic-col5'}).find_all('li',{'class':''}) # 还是有一点要说，就是返回的信息最好只有你需要的那部分，所以这里进行了筛选
    return data

def get_son_html(web_url):  # 爬虫获取网页没啥好说的
    #print(1111111111)
    #print(web_url)
    header = {
        "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
    html = requests.get(url=web_url, headers=header).text
    soup = BeautifulSoup(html,"html.parser")
    data = soup.find('div',{'class':'photo-show'}).find_all('a',{'class':'mainphoto'})
    #print(data)
    return data

def fmt():
    reg = r'href="(.+?)"'
    return re.compile(reg)

def fmt1():
    reg = r'src="(.+?\.jpg)" width'
    return re.compile(reg)

def saveImg(href,n):
    #print(str(get_son_html(href)))
    imglist = re.findall(fmt1(),str(get_son_html(href)))
    print(imglist)
    for img in imglist:
        urllib.request.urlretrieve(img, '%s.jpg' %n)
    return 0

def showHref(hreflist):
    x = 0
    print(hreflist)
    for href in hreflist:
        #print(href)
        saveImg(href,x)
        #urllib.request.urlretrieve(img, '%s.jpg' %x)
        time.sleep(5)
        x += 1


hreflist = re.findall(fmt(),str(get_html('https://movie.douban.com/subject/1830528/all_photos')))
x = 0
showHref(hreflist)