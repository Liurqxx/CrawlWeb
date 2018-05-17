# _*_coding:utf-8_*_
# Author:liu
import requests
import gevent
import os
import shutil
from gevent import monkey

'''


原理：
    每次pn+30，返回一条新的json数据

'''
# 打补丁
monkey.patch_all()


class Demo(object):
    # 初始化数据 搜索的关键字 页数
    def __init__(self, info, page):
        self.info = info
        self.page = page
        self.url = 'https://image.baidu.com/search/acjson'

    def get_page(self):
        '''获取每页图片信息'''
        page_list = []
        # 得到每一页数据
        for one_page in range(30, 30 * (self.page) + 30, 30):
            # 封装json数据
            json_data = {
                'tn': 'resultjson_com',

    def start(self):
        # 获取数据列表
        page_list = self.get_page()
        # 创建图片保存文件夹
        if os.path.exists('baidu_img'):
            shutil.rmtree('baidu_img')
        os.mkdir('baidu_img')

        # 遍历列表，开启协程下载
        for page_info in page_list:
            for img_info in page_info:
                if img_info:
                    img_url = img_info['thumbURL']
                    # 开启协程
                    g1 = gevent.spawn(self.down_img, img_url)
        # 等待下载任务结束后才结束
        gevent.joinall([g1])


if __name__ == '__main__':
    # 创建实例对象并初始化参数
    demo = Demo('Python', 2)
    # 开启下载任务
    demo.start()
    print('下载成功')
