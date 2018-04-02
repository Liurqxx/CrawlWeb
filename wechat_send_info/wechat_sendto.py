# _*_ coding:utf-8 _*_
# Author:liu
from wxpy import *
import requests
from wechat_sender import Sender
from threading import Timer

# 用于登录微信
bot = Bot()
# 好友列表
#friends_list = bot.friends()

# 组列表
#group_list = bot.groups()


def get_news():
    '''获取金山词霸每日一句'''
    url = "http://open.iciba.com/dsapi/"
    html = requests.get(url)
    # 得到每日一句英文
    contents = html.json()['content']
    # 得到每日一句中文
    translation = html.json()['translation']
    return contents, translation


def main():
    '''给指定好友发消息'''
    try:
        # 要发送的朋友的微信名称（不是备注也不是账号）
        my_friend = bot.friends().search(u'******')[0]

        # 发送数据
        my_friend.send(get_news()[0])
        my_friend.send(get_news()[1][5:])
        my_friend.send(u'来自爸爸的心灵鸡汤！')

        # 定时发送，每86400秒(一天)发送一次
        #t = Timer(86400, main)
        #t.start()
    except Exception as e:
        print(e)
        print('发送失败')


if __name__ == '__main__':
    main()
