# _*_ coding:utf-8 _*_
# Author:liu
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pymongo
import requests
import re


    # 判断好友空间是否设置了权限，通过判断是否存在元素ID：QM_OwnerInfo_Icon
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        b = True
    except:
        b = False
    # 如果有权限能够访问到说说页面，那么定位元素和数据，并解析
    if b == True:
        driver.switch_to.frame('app_canvas_frame')
        content = driver.find_elements_by_css_selector('.content')
        stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
        for con, sti in zip(content, stime):
            data = {
                'time': sti.text,
                'shuos': con.text
            }
            print(data)
            sheet_tab.insert_one(data)
        pages = driver.page_source
        soup = BeautifulSoup(pages, 'lxml')

    # 尝试一下获取Cookie，使用get_cookies()
    cookie = driver.get_cookies()
    cookie_dict = []
    for c in cookie:
        ck = "{0}={1};".format(c['name'], c['value'])
        cookie_dict.append(ck)
    i = ''
    for c in cookie_dict:
        i += c
    print('Cookies:', i)

    driver.close()
    driver.quit()


def main():
    to_qq_number = input('请输入对方的qq号码:')
    # url = 'http://user.qzone.qq.com/870469703/311'
    url = 'https://h5.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_module?i_uin={}&i_login_uin=2990599771&mode=4&previewV8=1&style=2&version=8&needDelOpr=true&start=0&count=10&transparence=true&hideExtend=false&showcount=5&MORE_FEEDS_CGI=http%3A%2F%2Fic2.qzone.qq.com%2Fcgi-bin%2Ffeeds%2Ffeeds_html_act_all&refer=2&paramstring=os-mac|100'.format(
        to_qq_number)
    # coookies信息
    cookies = {
        'cookie': 'pgv_pvid=4431548530; pac_uid=0_5a9534d8cc8b8; pgv_pvi=7430702080; ptui_loginuin=2990599771@qq.com; pt2gguin=o2990599771; RK=dAx0MJ3E3W; ptcz=83410556ecde5eea311f3e5ee148c22fe8a782af807dcac16fc70771cac0f85f; _ga=GA1.2.1073515414.1525065235; ptisp=; pgv_si=s3038691328; pgv_info=ssid=s8574927730; Loading=Yes; __Q_w_s_hat_seed=1; __Q_w_s__QZN_TodoMsgCnt=1; zzpaneluin=; zzpanelkey=; uin=o2990599771; skey=@btmlu4tWN; p_uin=o2990599771; pt4_token=1x4Xb1Q4Qj-6B7AhTxbG41uhXJNUgRB74Im6Rz27OFE_; p_skey=2FtCQk5gW4zXp*TgXHnj*QOheoJuWK9JLV8tEEvzi*Q_; rv2=8050F5E0F064DB6006574DC52601240A12C0E22204F792FFAA; property20=993902E31CF830E2311B053C7B36A6950B78F6FB99722B45156DB2067BBF3170FBBF27EE063013CF'}

    data = {
        'i_uin': '870469703',
        'i_login_uin': '2990599771',
        'mode': '4',
        'previewV8': '1',
        'style': '2',
        'version': '8',
        'needDelOpr': 'true',
        'transparence': 'true',
        'hideExtend': 'false',
        'showcount': '5',
        'MORE_FEEDS_CGI': 'http: // ic2.qzone.qq.com / cgi - bin / feeds / feeds_html_act_all',
        'refer': '2',
        'paramstring': 'os - mac | 100',

    }

    '''
        url:https://h5.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_module?i_uin=850792139&i_login_uin=2990599771&mode=4&previewV8=1&style=8&version=8&needDelOpr=true&transparence=true&hideExtend=false&showcount=5&MORE_FEEDS_CGI=http%3A%2F%2Fic2.qzone.qq.com%2Fcgi-bin%2Ffeeds%2Ffeeds_html_act_all&refer=2&paramstring=os-mac|100
    '''
    '''
        i_uin: 目标号码
        i_login_uin: 自己的号码
        mode: 4
        previewV8: 1
        style: 8
        version: 8
        needDelOpr: true
        transparence: true
        hideExtend: false
        showcount: 5
        MORE_FEEDS_CGI: http://ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_act_all
        refer: 2
        paramstring: os-mac|100


        i_uin: 870469703
        i_login_uin: 2990599771
        mode: 4
        previewV8: 1
        style: 2
        version: 8
        needDelOpr: true
        transparence: true
        hideExtend: false
        showcount: 5
        MORE_FEEDS_CGI: http://ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_act_all
        refer: 2
        paramstring: os-mac|100


        uin: 2990599771
        hostuin: 870469703
        scope: 0
        filter: all
        flag: 1
        refresh: 0
        firstGetGroup: 0
        mixnocache: 0
        scene: 0
        begintime: undefined
        icServerTime:
        start: 10
        count: 10
        sidomain: qzonestyle.gtimg.cn
        useutf8: 1
        outputhtmlfeed: 1
        refer: 2
        r: 0.6738102774309018
        g_tk: 920415851
        qzonetoken: 42bb359acdb21caa175ea263f759a78733025e28a984440c0bec215fc57cfb97fe4a2c6ced96136e51
        g_tk: 920415851



        uin: 2990599771
        hostuin: 870469703
        scope: 0
        filter: all
        flag: 1
        refresh: 0
        firstGetGroup: 0
        mixnocache: 0
        scene: 0
        begintime: undefined
        icServerTime:
        start: 20
        count: 10
        sidomain: qzonestyle.gtimg.cn
        useutf8: 1
        outputhtmlfeed: 1
        refer: 2
        r: 0.46931787854609874
        g_tk: 920415851
        qzonetoken: 42bb359acdb21caa175ea263f759a78733025e28a984440c0bec215fc57cfb97fe4a2c6ced96136e51
        g_tk: 920415851


    '''

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
