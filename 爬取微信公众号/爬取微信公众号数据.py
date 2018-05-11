# _*_ coding:utf-8 _*_
# Author:liu

import time
import requests
import re
import random

# 微信公众号账号
user = "2990599771@qq.com"
# 公众号密码
password = "154439LRQ"


# 爬取微信公众号文章，并存在本地文本中
def get_content(query):
    # query为要爬取的公众号名称

    # 打开搜索的微信公众号文章列表页
    appmsg_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)
    # 获取文章总数
    max_num = appmsg_response.json().get('app_msg_cnt')
    print('文章总数:', max_num)
    # 每页至少有5条，获取文章总的页数，爬取时需要分页爬
    num = int(int(max_num) / 5)
    # 起始页begin参数，往后每页加5
    begin = 0
    while num + 1 > 0:
        query_id_data = {
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'action': 'list_ex',
            'begin': '{}'.format(str(begin)),
            'count': '5',
            'query': '',
            'fakeid': fakeid,
            'type': '9'
        }
        print('正在翻页：--------------', begin)

        # 获取每一页文章的标题和链接地址，并写入本地文本中
        query_fakeid_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)
        fakeid_list = query_fakeid_response.json().get('app_msg_list')
        for item in fakeid_list:
            content_link = item.get('link')
            content_title = item.get('title')
            fileName = query + '.txt'
            with open(fileName, 'a', encoding='utf-8') as fh:
                fh.write(content_title + ":\n" + content_link + "\n")
        num -= 1
        begin = int(begin)
        begin += 5
        time.sleep(2)


def main():
    try:
        weiname = input('请输入对方的公众号名称:')
        gzlist = [weiname]
        # 登录之后，通过微信公众号后台提供的微信公众号文章接口爬取文章
        for query in gzlist:
            # 爬取微信公众号文章，并存在本地文本中
            print("开始爬取公众号：" + query)
            get_content(query)
            print("爬取完成")
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
