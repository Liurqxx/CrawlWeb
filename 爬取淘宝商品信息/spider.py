# _*_ coding:utf-8 _*_
# Author:liu
import requests
import re
import json
import urllib

'''
    获取淘宝商品信息
'''

'''
https://s.taobao.com/search?q=%E8%A1%A3%E6%9C%8D%E7%94%B7&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180409&ie=utf8&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s=0
https://s.taobao.com/search?q=%E8%A1%A3%E6%9C%8D%E7%94%B7&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180409&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
https://s.taobao.com/search?q=%E8%A1%A3%E6%9C%8D%E7%94%B7&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180409&ie=utf8&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88
https://s.taobao.com/search?q=%E8%A1%A3%E6%9C%8D%E7%94%B7&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180409&ie=utf8&bcoffset=-3&ntoffset=-3&p4ppushleft=1%2C48&s=132
https://s.taobao.com/search?q=%E8%A1%A3%E6%9C%8D%E7%94%B7&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180409&ie=utf8&bcoffset=-6&ntoffset=-6&p4ppushleft=1%2C48&s=176

https://s.taobao.com/search?q=%E8%A1%A3%E6%9C%8D%E7%94%B7&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180409&ie=utf8&bcoffset=-9&ntoffset=-3&p4ppushleft=1%2C48&s=88

bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s=0
bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
bcoffset和ntoffset 6-3->>
s:0+44



_ksTS:1523284693414_238
callback:jsonp239
ajax:true
m:customized
stats_click:search_radio_all:1
q:衣服男
ntoffset:6
p4ppushleft:1,48
s:36
imgfile:
initiative_id:staobaoz_20180409
bcoffset:-1
js:1
ie:utf8
rn:59f4f7e48f2f86d861c50a211d378a7e

'''

DATA = []


def main():
    show_info = input("请输入要查询的商品名称：")
    num = int(input("请输入要获取的页数:"))
    show_info = urllib.request.quote(show_info)
    # 循环页数
    for page in range(num):
        print('------第%s页:----------' % str(page + 1))
        # 拼装地址
        url = "https://s.taobao.com/search?q={}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180409&ie=utf8&bcoffset={}&ntoffset={}&p4ppushleft=1%2C48&s={}".format(
            show_info, str(6 - (page * 3)), str(6 - (page * 3)), str(page * 44))

        # 发送http请求
        response = requests.get(url)
        # 得到网页源码
        response.encoding = 'utf-8'
        html = response.text
        # print(html)
        # 正则匹配出数据
        content = re.findall(r'g_page_config = (.*?)g_srp_loadCss', html, re.S)[0].strip()[:-1]
        # content = content[:-1]
        # 格式化json
        content = json.loads(content)
        # 获取商品信息列表
        data_list = content['mods']['itemlist']['data']['auctions']
        # 提取数据
        # 标题 标价 购买人数 是否包邮 是否天猫 地区 店名 url
        for item in data_list:
            # print(item)
            temp = {
                'title': item['title'],
                'view_price': item['view_price'],
                'view_sales': item['view_sales'],
                'view_fee': '否' if float(item['view_fee']) else '是',
                'isTmall': '是' if item['shopcard']['isTmall'] else '否',
                'area': item['item_loc'],
                'name': item['nick'],
                'detail_url': item['detail_url'],
            }
            print(temp)


if __name__ == '__main__':
    main()
