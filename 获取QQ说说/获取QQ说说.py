# _*_ coding:utf-8 _*_
# Author:liu
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pymongo
import requests
import re


def main():
    to_qq_number = input('请输入对方的qq号码:')
    #拼接url地址
    url = 'https://h5.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_module?i_uin={}&i_login_uin=2990599771&mode=4&previewV8=1&style=2&version=8&needDelOpr=true&start=0&count=10&transparence=true&hideExtend=false&showcount=5&MORE_FEEDS_CGI=http%3A%2F%2Fic2.qzone.qq.com%2Fcgi-bin%2Ffeeds%2Ffeeds_html_act_all&refer=2&paramstring=os-mac|100'.format(
        to_qq_number)
    # cookies信息,使用谷歌浏览器抓包工具得到
    cookies = {
        'cookie': '你的cookies信息'}

    html = requests.get(url=url, cookies=cookies)
    html.encoding = 'utf-8'
    html = html.text
    # print(html.text)


    # 获取好友的备注
    qq_user_name = re.findall(r'<div class="f-nick">.*?href="(.*?)".*?>(.*?)<.*?</div>', html, re.S)
    qq_url, qq_name = qq_user_name[0]
    print('qq空间地址:', qq_url, '好友昵称:', qq_name)
    # 每一页日期列表
    qq_info_date = re.findall(r'<div class="info-detail">.*?>(.*?)</span>', html, re.S)
    print(qq_info_date)

    # 每一页说说内容列表
    qq_user_info = re.findall(r'<div class="f-info">(.*?)</div>', html, re.S)
    print(qq_user_info)
    # 设备型号列表
    iphone_style = re.findall(r'来自.*?<a .*?class=" phone-style state">(.*?)</a>', html)
    print(iphone_style)

    # 浏览次数列表
    wath_number = re.findall(r'<a .*?class="state qz_feed_plugin".*?>(.*?)</a>', html)
    print(wath_number)

    # 获取点赞好友列表
    good_user_list = re.findall(r'<div class="user-list">(.*?)</div>', html)
    # print(good_user_list)
    for user in good_user_list:
        # 得到每一条说说的点赞列表
        one_info_list = re.findall(r'<a href="(.*?)".*?>(.*?)</a>', user)
        for good_info in one_info_list:
            friend_url, friend_name = good_info
            print('点赞好友空间地址:', friend_url, '点赞好友昵称:', friend_name)
        print('==' * 50)


if __name__ == '__main__':
    # get_shuoshuo('870469703')
    main()
