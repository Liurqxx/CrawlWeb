# _*_coding:utf-8_*_
# Author:liu
import requests
import json
import matplotlib.pyplot as plt
from pyecharts import Bar
# from pyecharts import WordCloud
from wordcloud import WordCloud

'''
评论地址:
http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token=34814d54e40b194cff84c0569bbbb200

请求头：
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36

# post请求参数
'params':'xL8LMVOqYZZkjIdEt3kWzTpNoVxGBZiOy23JzoDe+YwD4k/mkv6i9DmHUIRSmctYlmlAJzMtCpCYZxrL0OrEPVpY3V0iLQvNqGjMZxc0JiiYLUOFmt7bm6Uc7FQe6l6j87eS934h9XJsGZtjQ2kjfj0hWJzWBzwdP9l1wu366gjC29E9l4Hhc6UgLRiRGx6vazgIjen7QW2xSKmz7OJDR2a0TSxdtK9fYL0PAxo4UZY='
'encSecKey':'cde658dde9306dee77aa07ae3797bfaa2e12ac3dead3a8a60d69c3df509cda2d136cf5ddc9105175f9d1b5f9de17ca715dd1b9bbccb3628003dfa6acb28c0aaf98d0d9b9f134692111975000365446283a4af6326d83f836c93a244222bb96dddafe82ce6053967b422d7abe77429baddefc434c279b475e7ff967a984564671'

'''


# 制作点赞数据图表
def makePlot(nickname_list, likedCount_list):
    # 制成图表(柱状图)
    bar = Bar('点赞图表', width=1000, height=700)
    bar.add('点赞数', nickname_list, likedCount_list, is_stack=True, mark_line=['min', 'max'], mark_point=['average'])
    bar.render(path='./点赞图表分析.html')


# 制成词云图显示
def makeCloud(content_list):
    # 制成词云图显示

    content_list = "".join(content_list)
    wordcloud = WordCloud(font_path=r'/usr/share/fonts/truetype/arphic/uming.ttc', width=1500, height=1000,
                          max_font_size=300, min_font_size=20).generate(
        content_list)
    # 保存文件
    wordcloud.to_file('./评论.png')


def main():
    # 评论地址
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token=34814d54e40b194cff84c0569bbbb200"

    # 请求头
    headers = {
        'Host': 'music.163.com',
        'Origin': 'http://music.163.com',
        'Referer': 'http://music.163.com / song?id = 551816010',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'

    }

    # post请求数据
    user_data = {
        'params': 'xL8LMVOqYZZkjIdEt3kWzTpNoVxGBZiOy23JzoDe+YwD4k/mkv6i9DmHUIRSmctYlmlAJzMtCpCYZxrL0OrEPVpY3V0iLQvNqGjMZxc0JiiYLUOFmt7bm6Uc7FQe6l6j87eS934h9XJsGZtjQ2kjfj0hWJzWBzwdP9l1wu366gjC29E9l4Hhc6UgLRiRGx6vazgIjen7QW2xSKmz7OJDR2a0TSxdtK9fYL0PAxo4UZY=',
        'encSecKey': 'cde658dde9306dee77aa07ae3797bfaa2e12ac3dead3a8a60d69c3df509cda2d136cf5ddc9105175f9d1b5f9de17ca715dd1b9bbccb3628003dfa6acb28c0aaf98d0d9b9f134692111975000365446283a4af6326d83f836c93a244222bb96dddafe82ce6053967b422d7abe77429baddefc434c279b475e7ff967a984564671'

    }

    # 获取网页数 url:评论地址 headers:请求头信息 data：请求参数
    response = requests.post(url, headers=headers, data=user_data)

    # 解析数据
    data = json.loads(response.text)
    # 提取数据
    result_data = []
    for info in data['hotComments']:
        # 把信息保存到字典中
        item = {
            'nickname': info['user']['nickname'],
            'content': info['content'],
            'likedCount': info['likedCount']
        }
        # 把保存信息的字典添加到列表中
        result_data.append(item)

    # 得到对应的数据列表
    # 名称列表
    nickname_list = [data['nickname'] for data in result_data]
    # 评论内容列表
    content_list = [data['content'] for data in result_data]
    # 点赞数量
    likedCount_list = [data['likedCount'] for data in result_data]

    # 制作点赞图表
    makePlot(nickname_list, likedCount_list)
    # 制作图云显示
    makeCloud(content_list)


if __name__ == '__main__':
    main()
