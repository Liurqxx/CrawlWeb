# _*_coding:utf-8 _*_
# Author:liu
import requests
from bs4 import BeautifulSoup
import os

Hostreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://www.mzitu.com'
}
# 报文头信息
Picreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://i.meizitu.net'
}


def get_page_name(url):
    '''获取图片最大页数和名称'''
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    span = soup.findAll('span')
    title = soup.find('h2', class_='main-title')
    return span[10].text, title.text


def get_html(url):
    '''获取页面的html代码'''
    req = requests.get(url, headers=Hostreferer)
    html = req.text
    return html


def get_img_url(url, name):
    '''获取所有的图片名'''
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    img_url = soup.find('img', alt=name)
    return img_url['src']


def save_img(img_url, count, name):
    '''保存图片'''
    req = requests.get(img_url, headers=Picreferer)
    with open(name + '/' + str(count) + '.jpg', 'wb') as f:
        f.write(req.content)


def main():
    '''程序主入口'''
    #url地址
    old_url = 'http://www.mzitu.com/123114'
    #得到包名和页数
    page, name = get_page_name(old_url)
    #创建文件夹
    os.mkdir(name)
    #遍历，保存每一张图片
    for i in range(1, int(page) + 1):
        url = old_url + '/' + str(i)
        img_url = get_img_url(url, name)
        save_img(img_url, i, name)
        print('保存第' + str(i) + '张图片成功')


if __name__ == "__main__":
    main()
