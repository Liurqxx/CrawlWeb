# _*_ coding:utf-8 _*_
# Author:liu
import requests
import re
from pymysql import *

'''
    爬取电影天堂的电影并写入数据库
'''



def main():
    # 创建Connection链接,链接数据库
    conn = connect(host='localhost', port=3306, database='movielink', user='root', password='000000', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    num = int(input("请输入页数:"))
    # 循环产生网址
    for page in range(1, num):
        # 下载页面url
        url = 'http://www.ygdy8.net/html/gndy/oumei/list_7_' + str(page) + '.html'
        # 得到网页源代码
        html = requests.get(url)
        # 指定编码
        html.encoding = 'gb2312'
        # 得到 电影网址
        dy_data = re.findall('<a href="(.*?)" class="ulink">', html.text)  # 返回的列表
        # 循环拼接电影网址
        for m in dy_data:
            # 拼接网址
            xq_url = 'http://www.ygdy8.net' + m
            # 得到详情页的网页源代码
            html2 = requests.get(xq_url)
            # 指定编码格式
            html2.encoding = 'gb2312'
            try:
                # 提取下载链接
                dy_link = re.findall('<a href="(.*?)">.*?</a></td>', html2.text)[0]
                # 创建sql语句
                sql = "insert into moveinfo(moveurl) values ('{}')".format(str(dy_link))
                cs.execute(sql)
                # print(dy_link)
            except Exception as e:
                print('数据有误', e)
    # 提交
    conn.commit()
    print('下载成功')


if __name__ == '__main__':
    main()
