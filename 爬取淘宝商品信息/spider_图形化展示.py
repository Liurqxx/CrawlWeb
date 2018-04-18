# _*_ coding:utf-8 _*_
# Author:liu
import requests
import re
import json
import urllib
from pyecharts import Bar
from pyecharts import Pie
from pylab import *

'''
    获取淘宝商品信息
'''





def main():
    # 用于保存所有的商品信息
    DATA = []
    show_info = input("请输入要查询的商品名称：")
    num = int(input("请输入要获取的页数:"))
    # 对商品信息加密
    show_info = urllib.request.quote(show_info)

    # 循环页数
    for page in range(num):
        print('------第%s页:----------' % str(page + 1))
        # 拼装地址
        url = "https://s.taobao.com/search?q={}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180409&ie=utf8&bcoffset={}&ntoffset={}&p4ppushleft=1%2C48&s={}".format(
            show_info, str(6 - (page * 3)), str(6 - (page * 3)), str(page * 44))

        # 发送http请求
        response = requests.get(url)
        # 得到网页源码
        response.encoding = 'utf-8'
        html = response.text
        # 正则匹配出数据
        content = re.findall(r'g_page_config = (.*?)g_srp_loadCss', html, re.S)[0].strip()[:-1]
        # 格式化json
        content = json.loads(content)
        # 获取商品信息列表
        data_list = content['mods']['itemlist']['data']['auctions']
        # 提取数据
        # 标题 标价 购买人数 是否包邮 是否天猫 地区 店名 url
        for item in data_list:
            # 保存每一件商品的信息
            data = {}
            # 对title做初步处理
            title = item['title']
            title = re.sub(r'</?.*?>', "", title, re.S)
            # 提取数据保存到字典中
            temp = {
                'title': title,
                'view_price': item['view_price'],
                'view_sales': item['view_sales'],
                'view_fee': '否' if float(item['view_fee']) else '是',
                'isTmall': '是' if item['shopcard']['isTmall'] else '否',
                'area': item['item_loc'],
                'name': item['nick'],
            }
            # 添加到列表内
            DATA.append(temp)

    # 统计
    # 天猫和淘宝比例
    data1 = {'淘宝': 0, '天猫': 0}
    # 是否包邮
    data2 = {'包邮': 0, '不包邮': 0}
    # 区域分布
    data3 = {}

    for item in DATA:
        if item['view_fee'] == '是':
            data2['包邮'] += 1
        else:
            data2['不包邮'] += 1
        if item['isTmall'] == '否':
            data1['淘宝'] += 1
        else:
            data1['天猫'] += 1
        # 地区
        data3[item['area'].split(' ')[0]] = data3.get(item['area'].split(' ')[0], 0) + 1

    # 包邮信息和是否天猫信息使用饼状图
    bingzhuangtu(data1, '是否天猫')
    bingzhuangtu(data2, '是否包邮')
    # 地区分布使用柱状图
    zhuzhuantu(data3, '地区分布')


if __name__ == '__main__':
    main()
