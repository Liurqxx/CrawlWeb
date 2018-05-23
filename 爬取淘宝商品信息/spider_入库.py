# _*_ coding:utf-8 _*_
# Author:liu
import requests
import re
import json
import urllib
from pymysql import *

'''
    获取淘宝商品信息
'''


        # print(content)
        # content = content[:-1]
        # 格式化json
        content = json.loads(content)
        # 获取商品信息列表
        data_list = content['mods']['itemlist']['data']['auctions']
        # 提取数据
        # 标题 标价 购买人数 是否包邮 是否天猫 地区 店名 url
        for item in data_list:
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
                detail_url = str(temp['detail_url'])
                view_sales = re.findall(r'(\d+)', temp['view_sales'])[0]
                # 创建sql语句
                sql = "insert into taobaoinfo(title,price,sales,isfee,istmall,area,name,detailurl) values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    str(title), temp['view_price'], str(view_sales),
                    temp['view_fee'], temp['isTmall'],
                    temp['area'],
                    temp['name'],
                    detail_url)
                # 添加数据
                cs.execute(sql)
            except Exception as e:
                print(e)
        print('------第%s页下载完成----------' % str(page + 1))
        # 提交操作
        conn.commit()

    # 关闭连接
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()
