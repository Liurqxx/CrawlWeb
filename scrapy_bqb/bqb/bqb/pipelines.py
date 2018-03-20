# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests


class BqbPipeline(object):
    '''处理网页的数据'''

    def process_item(self, item, spider):
        '''通过图片url地址下载表情包'''
        url = 'http://qq.yh31.com' + item['addr']
        response = requests.get(url)
        response.encoding = 'utf-8'
        # 保存表情包
        with open('C:\\Users\\29905\Desktop\\scrapy_bqb\\bqb\data\\%d.gif' % item['name'], 'wb') as ft:
            # 写入二进制数据
            ft.write(response.content)
