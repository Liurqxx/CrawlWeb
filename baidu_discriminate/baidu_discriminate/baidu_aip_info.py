# _*_ coding:utf-8 _*_
# Author:liu
from aip import AipOcr

'''
    获取aipocr
'''


class get_aipocr(object):
    def __init__(self):
        """ 你的 APPID AK SK """
        #自己注册
        self.APP_ID = '******'
        self.API_KEY = '******'
        self.SECRET_KEY = '******'

    def get_aipocr_info(self):
        return AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
