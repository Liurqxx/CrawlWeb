# _*_ coding:utf-8 _*_
# Author:liu
import requests
import re
import time
import os
import xlsxwriter

'''
    第一页:https://movie.douban.com/subject/4920389/comments?start=0&limit=20&sort=new_score&status=P&percent_type=
    第二页:https://movie.douban.com/subject/4920389/comments?start=20&limit=20&sort=new_score&status=P&percent_type=

'''

# 用于记录写入数据的条数
data_cursor = 1


def main():
    global data_cursor
    try:
        page_num = int(input("请输入页数:"))
        # 创建excel文件
        workbooke, worksheet = write_data()
        for page in range(page_num):
            # 评论url地址
            # url = "https://movie.douban.com/subject/4920389/comments?start=" + str(
            #     page * 20) + "&limit=20&sort=new_score&status=P&percent_type="

            url = "https://movie.douban.com/subject/24773958/comments?start=" + str(
                page * 20) + "&limit=20&sort=new_score&status=P&percent_type="
            # 获取网页源代码
            html = requests.get(url)
            html.encoding = 'utf-8'
            html = html.text
            # 正则匹配得到需要的数据
            result = re.findall(
                r'<a href="javascript:;" class="j a_show_login" onclick="">(.*?)</a>'
                r'.*?<a href="https://www.douban.com/.*?" class="">(.*?)</a>'
                r'.*?<span>(.*?)</span>'
                r'.*?<span class="comment-time " title="(.*?)">.*?</span>'
                r'.*?<p class=""> (.*?)</p>',
                html, re.S)
            # print(result, len(result))
                data_cursor += 1
            print('第{}页完成...'.format(page + 1))
            # 每一页之间间隔1秒
            time.sleep(1)
    except Exception as e:
        print(e)
    finally:
        # 关闭文件对象
        workbooke.close()


if __name__ == '__main__':
    main()
