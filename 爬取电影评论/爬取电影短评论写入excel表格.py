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


# 创建工作文件
def write_data():
    # 删除文件
    if os.path.exists('./复仇者联盟3评论信息.xlsx'):
        os.remove('./复仇者联盟3评论信息.xlsx')

    # 创建工作文件
    workbooke = xlsxwriter.Workbook('复仇者联盟3评论信息.xlsx')
    # 创建工作表
    worksheet = workbooke.add_worksheet()
    # 写标题
    worksheet.write(0, 0, '是否有用')
    worksheet.write(0, 1, '是否看过')
    worksheet.write(0, 2, '作者')
    worksheet.write(0, 3, '时间')
    worksheet.write(0, 4, '内容')

    return workbooke, worksheet


def main():
    global data_cursor
    try:

    except Exception as e:
        print(e)
    finally:
        # 关闭文件对象
        workbooke.close()


if __name__ == '__main__':
    main()
