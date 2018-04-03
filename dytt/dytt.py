# _*_ coding:utf-8 _*_
# Author:liu
import requests
import urllib
import re

'''
    爬取电影天堂的电影
'''

# http://www.ygdy8.net/html/gndy/oumei/list_7_2.html
# 下载页面
# http://www.ygdy8.net/html/gndy/dyzz/20180314/56482.html

# 下载电影
def down_move(move_url):
    # ftp://ygdy8:ygdy8@yg45.dydytt.net:3052/阳光电影www.ygdy8.com.马戏之王.BD.720p.中英双字幕.mkv
    # 获取电影名
    names = move_url.split('阳光电影www.ygdy8.com.')

    urllib.request.urlretrieve(move_url, 'move\\' + names[1])


def main():
	    # 循环产生网址
    for page in range(1, 187):
        # 网址
        url = 'http://www.ygdy8.net/html/gndy/oumei/list_7_' + str(page) + '.html'
        # 得到网页源代码
        html = requests.get(url)
        # 指定编码
        html.encoding = 'gb2312'
        # 提取网页源码中的下一页的网址信息
        # http://www.ygdy8.net
        # /html/gndy/dyzz/20180314/56482.html
        # 得到 电影网址
        dy_data = re.findall('<a href="(.*?)" class="ulink">', html.text)  # 返回的列表
        # 循环拼接电影网址
        for m in dy_data:
            # 拼接网址
            xq_url = 'http://www.ygdy8.net' + m
            # 得到详情页的网页源代码
            html2 = requests.get(xq_url)
            html2.encoding = 'gb2312'
            try:
                # 提取下载链接
                dy_link = re.findall('<a href="(.*?)">.*?</a></td>', html2.text)[0]
                print(dy_link)
            except Exception as e:
                print('没有匹配到数据')
                # 将链接保存到本地
                with open('move\\socare_link.txt', 'a') as f:
                    f.write(dy_link + '\n')


if __name__ == '__main__':
    main()
