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
    # 创建实例对象并初始化参数
    demo = Demo('Python', 2)
    # 开启下载任务
    demo.start()
    print('下载成功')
