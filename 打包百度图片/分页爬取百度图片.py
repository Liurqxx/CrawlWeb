# _*_coding:utf-8_*_
# Author:liu
import requests
import gevent
import os
import shutil
from gevent import monkey

'''


原理：
    每次pn+30，返回一条新的json数据,数据包含图片的url和downloadurl

'''
# 打补丁
monkey.patch_all()


class Down(object):
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
                'ipn': 'rj',
                'ct': 201326592,
                'is': '',
                'fp': 'result',
                'queryWord': self.info,
                'cl': 2,
                'lm': -1,
                'ie': 'utf-8',
                'oe': 'utf-8',
                'adpicid': '',
                'st': -1,
                'z': '',
                'ic': 0,
                'word': self.info,
                's': '',
                'se': '',
                'tab': '',
                'width': '',
                'height': '',
                'face': 0,
                'istype': 2,
                'qc': '',
                'nc': 1,
                'fr': '',
                'pn': one_page,
                'rn': 30,
                'gsm': '1e',
                '1488942260214': ''

            }
            # 把每一页数据添加到列表中
            page_list.append(requests.get(self.url, params=json_data).json().get('data'))
        # 返回数据列表
        return page_list

    def down_img(self, img_url):
        '''下载图片'''
        # 截取出文件名
        img_info = img_url.split('/')[5]
        img_name = img_info.split('&')[0]
        # 保存图片
        with open('baidu_img/' + img_name + '.jpg', 'wb') as file:
            img_data = requests.get(img_url).content
            file.write(img_data)

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

	#接收用户输入的参数
	user_info = input('请输入关键词内容:')
    # 创建实例对象并初始化参数
    down = Down(user_info, 2)
    # 开启下载任务
    down.start()
    print('下载成功')
