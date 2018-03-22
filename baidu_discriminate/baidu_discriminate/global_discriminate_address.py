# _*_ coding:utf-8 _*_
# Author:liu
from baidu_discriminate import baidu_aip_info

'''
    通用文字识别-含位置信息
'''


class global_address_info(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.baidu_aip_info = baidu_aip_info.get_aipocr()
        self.client = self.baidu_aip_info.get_aipocr_info()

    # 读取图片信息
    def get_file_content(self):
        with open(self.filepath, 'rb') as fp:
            return fp.read()

    def get_info(self):
        # 读取图片
        image = self.get_file_content()

        """ 如果有可选参数 """
        options = {}
        options["recognize_granularity"] = "big"
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["vertexes_location"] = "true"
        options["probability"] = "true"

        """ 带参数调用通用文字识别（含位置信息版）, 图片参数为本地图片 """
        return self.client.general(image, options)
