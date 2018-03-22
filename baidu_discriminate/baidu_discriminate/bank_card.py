# _*_ coding:utf-8 _*_
# Author:liu

from baidu_discriminate import baidu_aip_info

'''
    银行卡识别   识别银行卡并返回卡号和发卡行
'''


class bank_card_info(object):
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

        """ 调用银行卡识别 """
        return self.client.bankcard(image);
