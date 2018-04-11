# _*_ coding:utf-8 _*_
# Author:liu
import requests
import re
import urllib
import base64
import os
import threading

'''
    爬取电影天堂的电影连接并下载
'''

# http://www.ygdy8.net/html/gndy/oumei/list_7_2.html
# 下载页面
# http://www.ygdy8.net/html/gndy/dyzz/20180314/56482.html


'''
    Headers:
            Accept:image/webp,image/apng,image/*,*/*;q=0.8
            Accept-Encoding:gzip, deflate
            Accept-Language:zh-CN,zh;q=0.9
            Connection:keep-alive
            Cookie:u=Y4VsWhRogA0BAAAA8MJK
            Host:log.he2d.com
            Referer:http://www.37cs.com/html/click/8040_2134.html
            User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36
'''


def down_move(url):
    # 启动迅雷下载
    # 传入两个参数：path和下载连接
    os.system("D:\程序\Program\Thunder.exe -StartType:DesktopIcon \"%s\"" % url)


def main():
    num = int(input("请输入页数:"))
    # 循环产生网址
    for page in range(1, num):
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
                # print(dy_link)
                # 拼接下载连接
                dy_link = 'AA' + dy_link + 'ZZ'
                dy_link = dy_link.encode()
                QutoUrl = urllib.request.quote(dy_link)
                downurl = "thunder://" + (base64.b64encode(QutoUrl.encode())).decode()
                print(downurl)
                # 开启线程调用迅雷下载资源
                down_thread = threading.Thread(target=down_move, args=(downurl,))
                # 开启线程
                down_thread.start()

            except Exception as e:
                print('数据有误', e)
                # ftp: // ygdy8: ygdy8 @ yg45.dydytt.net:3065 / 阳光电影www.ygdy8.com.华盛顿邮报.BD.720p.中英双字幕.mkv
    print('添加下载任务完成')


if __name__ == '__main__':
    main()
