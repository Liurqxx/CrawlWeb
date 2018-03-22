# _*_ coding:utf-8 _*_
# Author:liu
from baidu_discriminate import baidu_aip_info

'''
    通用文字识别
'''


class global_getinfo(object):
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

        # 调用通用文字识别, 图片参数为本地图片
        self.client.basicGeneral(image);

        # 如果有可选参数
        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "true"

        # 带参数调用通用文字识别, 图片参数为本地图片
        return self.client.basicGeneral(image, options)
