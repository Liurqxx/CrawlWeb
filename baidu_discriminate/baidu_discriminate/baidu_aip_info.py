# _*_ coding:utf-8 _*_
# Author:liu
from aip import AipOcr

'''
    获取aipocr
'''


class get_aipocr(object):
    def __init__(self):
        """ 你的 APPID AK SK """
        self.APP_ID = '10823272'
        self.API_KEY = 'aFCDfvS6SfknFkQUuXCr8tQ9'
        self.SECRET_KEY = 'K6vjemA4Qw3wp6X23KvF1qCbdWSkK7kn'

    def get_aipocr_info(self):
        return AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
