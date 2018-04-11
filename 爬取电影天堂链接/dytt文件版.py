# _*_ coding:utf-8 _*_
# Author:liu
import requests
import re

'''
    爬取电影天堂的电影
'''


def main():
    with open('move/info.txt', 'w') as file:
        # 循环产生网址
        for page in range(1, 3):
            # 网址
            url = 'http://www.ygdy8.net/html/gndy/oumei/list_7_' + str(page) + '.html'
            # 得到网页源代码
            html = requests.get(url)
            # 指定编码
            html.encoding = 'gb2312'
            # 提取网页源码中的下一页的网址信息
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
                    file.write(dy_link + '\r\n')
                    print(dy_link)
                except Exception as e:
                    print('没有匹配到数据', e)

    print('下载成功')


if __name__ == '__main__':
    main()
