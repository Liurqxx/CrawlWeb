# _*_coding:utf-8_*_
# Author:liu

import requests

import json
import time

from selenium import webdriver
from bs4 import BeautifulSoup


class get_data(object):

    def __init__(self):
        self.base_url = 'https://www.douyu.com/directory/all'
        self.web_driver = webdriver.Chrome()
        self.count = 0

    def parttern_rex(self, data):
        '''清洗数据'''
        # 转换类型
        soup = BeautifulSoup(data, 'lxml')

        # 解析数据
        room_list = soup.select('#live-list-contentbox .ellipsis')
        nick_list = soup.select('#live-list-contentbox .dy-name')
        hot_list = soup.select('#live-list-contentbox .dy-num')

        # 要求数据一一对应，所以需要使用zip进行处理
        for room_name, nick_name, hot in zip(room_list, nick_list, hot_list):
            print(room_name.get_text().strip() + "==", nick_name.get_text().strip() + "==", hot.get_text().strip())
            self.count += 1

    def save_file(self):
        '''保存数据'''
        pass

    def run(self):
        '''运行'''
        self.web_driver.get(self.base_url)
        time.sleep(3)

        # 获取网页源代码
        response_data = self.web_driver.page_source
        # 解析数据
        self.parttern_rex(response_data)

        while 1:

            # 判断是否已经是最后一个页面了
            if response_data.find('shark-pager-disable-next') != -1:
                '''已经是最后一页了'''
                break

            # 获取下一页标签，点击
            next_element = self.web_driver.find_element_by_class_name('shark-pager-next')
            # 点击
            next_element.click()

            # 获取下一页的网页源代码
            response_data = self.web_driver.page_source
            # 解析数据
            self.parttern_rex(response_data)
            print('==' * 100)

        print('总数量：', self.count)


if __name__ == '__main__':
    get_data().run()
