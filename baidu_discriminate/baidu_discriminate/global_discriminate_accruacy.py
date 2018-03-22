# _*_ coding:utf-8 _*_
# Author:liu
from baidu_discriminate import baidu_aip_info

'''
    通用文字识别-高精度
        用户向服务请求识别某张图中的所有文字，相对于通用文字识别该产品精度更高，但是识别耗时会稍长
'''


class global_accuracy_info(object):
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

        """ 调用通用文字识别（高精度版） """
        self.client.basicAccurate(image);

        """ 如果有可选参数 """
        options = {}
        options["detect_direction"] = "true"
        options["probability"] = "true"

        """ 带参数调用通用文字识别（高精度版） """
        return self.client.basicAccurate(image, options)
