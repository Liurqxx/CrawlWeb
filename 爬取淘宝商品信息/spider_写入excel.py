# _*_ coding:utf-8 _*_
# Author:liu
import requests
import re
import json
import urllib
import xlsxwriter
import os

'''
    获取淘宝商品信息
'''


def write_data():
    # 删除文件
    if os.path.exists('taobaoinfo.xlsx'):
        os.remove('taobaoinfo.xlsx')

    # 创建工作文件
    workbooke = xlsxwriter.Workbook('taobaoinfo.xlsx')
    # 创建工作表
    worksheet = workbooke.add_worksheet()
    # 写标题
    worksheet.write(0, 0, '标题')
    worksheet.write(0, 1, '标价')
    worksheet.write(0, 2, '购买人数')
    worksheet.write(0, 3, '是否包邮')
    worksheet.write(0, 4, '是否天猫')
    worksheet.write(0, 5, '地区')
    worksheet.write(0, 6, '店名')
    worksheet.write(0, 7, '链接')

    return workbooke, worksheet


def main():
    show_info = input("请输入要查询的商品名称：")
    num = int(input("请输入要获取的页数:"))
    show_info = urllib.request.quote(show_info)

    # 创建工作表
    workbooke, worksheet = write_data()



        # 提取数据
        # 标题 标价 购买人数 是否包邮 是否天猫 地区 店名 url
        for index, item in enumerate(data_list):
            try:
                # 提取数据保存到字典中
                temp = {
                    'title': item['title'],
                    'view_price': item['view_price'],
                    'view_sales': item['view_sales'],
                    'view_fee': '否' if float(item['view_fee']) else '是',
                    'isTmall': '是' if item['shopcard']['isTmall'] else '否',
                    'area': item['item_loc'],
                    'name': item['nick'],
                    'detail_url': item['detail_url'],
                }
                title = temp['title']
                title = re.sub(r'</?.*?>', "", title, re.S)
                i = n + index + 1

                # 写入数据
                worksheet.write(i, 0, title)
                worksheet.write(i, 1, temp['view_price'])
                worksheet.write(i, 2, temp['view_sales'])
                worksheet.write(i, 3, temp['view_fee'])
                worksheet.write(i, 4, temp['isTmall'])
                worksheet.write(i, 5, temp['area'])
                worksheet.write(i, 6, temp['name'])
                worksheet.write(i, 7, temp['detail_url'])

            except Exception as e:
                print(e)
        n += len(data_list)
        print('------第%s页下载完成:----------' % str(page + 1))
    workbooke.close()


if __name__ == '__main__':
    main()
