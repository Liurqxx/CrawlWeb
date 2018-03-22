from baidu_discriminate import baidu_aip_info
from baidu_discriminate import global_discriminate
from baidu_discriminate import global_discriminate_accruacy
from baidu_discriminate import global_discriminate_address
from baidu_discriminate import global_discriminate_rare
from baidu_discriminate import network_written
from baidu_discriminate import idcard_discriminate
from baidu_discriminate import bank_card


def print_menu():
    '''输出菜单'''
    print('==========百度文字识别==========')
    print("1.通用文字识别")
    print("2.通用文字识别(高精度版)")
    print("3.通用文字识别(含位置版)")
    print("4.通用文字识别(含生僻字)")
    print("5.网络文字识别")
    print("6.身份证识别")
    print("7.银行卡识别")
    print("8.退出系统")
    print('==============================')


img_score = 'img.png'
img_url = "http://img1.3lian.com/img013/v2/81/d/90.jpg"


class main(object):
    '''得到aipocr信息'''

    def __init__(self):
        '''初始化aipocr信息'''
        self.baidu_aip_info = baidu_aip_info.get_aipocr()
        self.client = self.baidu_aip_info.get_aipocr_info()

    def run(self):
        while True:
            # 输出菜单
            print_menu()
            input_select = input('请输入你的选项:')
            if input_select == '1':
                # 通用文字识别
                print(global_discriminate.global_getinfo(img_score).get_info())
            elif input_select == '2':
                # 通用文字识别(高精度版)
                print(global_discriminate_accruacy.global_accuracy_info(img_score).get_info())
            elif input_select == '3':
                # 通用文字识别(含位置版)
                print(global_discriminate_address.global_address_info(img_score).get_info())
            elif input_select == '4':
                # 通用文字识别(含生僻字)
                print(global_discriminate_rare.global_rare_info(img_score).get_info())
            elif input_select == '5':
                # 网络文字识别
                print(network_written.network_written_info(img_url).get_info())
            elif input_select == '6':
                # 身份证识别
                print(idcard_discriminate.idcard_getinfo('正面.png', '反面.png').get_info())
            elif input_select == '7':
                # 银行卡识别
                print(bank_card.bank_card_info('img.png').get_info())
            elif input_select == '8':
                print("谢谢使用,再见")
                break
            else:
                print("输入有误")
