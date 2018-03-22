# _*_ coding:utf-8 _*_
# Author:liu
from baidu_discriminate import  baidu_aip_info

'''
    身份证识别
        用户向服务请求识别身份证，身份证识别包括正面和背面
'''


class idcard_getinfo(object):
    def __init__(self, side_front=None, side_back=None):
        # 传入正反两面
        self.side_front = side_front
        self.side_back = side_back
        self.baidu_aip_info = baidu_aip_info.get_aipocr()
        self.client = self.baidu_aip_info.get_aipocr_info()

    # 读取图片信息
    def get_file_content(self, side):
        with open(side, 'rb') as fp:
            return fp.read()

    def get_info(self):
        # 创建一个列表保存数据
        idcard_list = []
        if self.side_front:
            # 读取正面信息
            image_front = self.get_file_content(self.side_front)
            idCardSide = "front"
            """ 如果有可选参数 """
            options = {}
            options["detect_direction"] = "true"
            options["detect_risk"] = "false"
            """ 带参数调用身份证识别 """
            idcard_list.append(self.client.idcard(image_front, idCardSide, options))
        if self.side_back:
            # 读取反面信息
            image_back = self.get_file_content(self.side_front)
            idCardSide = "back"
            """ 如果有可选参数 """
            options = {}
            options["detect_direction"] = "true"
            options["detect_risk"] = "false"

            """ 带参数调用身份证识别 """
            idcard_list.append(self.client.idcard(image_back, idCardSide, options))
        return idcard_list
