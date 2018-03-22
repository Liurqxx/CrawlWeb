# _*_ coding:utf-8 _*_
# Author:liu
from baidu_discriminate import baidu_aip_info

'''
    网络文字识别
        用户向服务请求识别一些网络上背景复杂，特殊字体的文字
        注意:既可以识别本地图片,又能识别网络图片,此处演示识别网络图片

'''


class network_written_info(object):
    '''传入图片的url地址'''

    def __init__(self, file_url):
        self.file_url = file_url
        self.baidu_aip_info = baidu_aip_info.get_aipocr()
        self.client = self.baidu_aip_info.get_aipocr_info()

    def get_info(self):
        """ 如果有可选参数 """
        options = {}
        options["detect_direction"] = "true"
        options["detect_language"] = "true"

        """ 带参数调用网络图片文字识别, 图片参数为远程url图片 """
        return self.client.webImageUrl(self.file_url, options)
