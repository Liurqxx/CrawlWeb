# _*_coding:utf-8_*_
# Author:liu
import re
import requests

# 请求头信息
headers = {

    'user - agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 64.0.3282.119Safari / 537.36'
}

 re.findall(
        r'<span class="date">(.*?)</span><span class="title"><a target="_blank" href="(.*?)">(<font color=.*?>)?(.*?)</a></span></li>',
        html, re.S)

    # 输出结果
    for i in news_url:
        print(i[0], i[1], i[3])


# 获取win10之家信息
def get_win10_info():
    url = "https://win10.ithome.com/"
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    html = html.text

    # print(html)
    # 匹配结果
    news_url = re.findall(
        r'<span class="date">(.*?)</span><span class="title"><a target="_blank" href="(.*?)">(<font color=.*?>)?(.*?)</a></span></li>',
        html, re.S)

    # 输出结果
    for i in news_url:
        print(i[0], i[1], i[3])



def get_home_info():
    url = "https://www.ithome.com/"
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    html = html.text

    # print(html)
    # 匹配结果
    news_url = re.findall(
        r'<span class="date">(.*?)</span><span class="title"><a target="_blank" href="(.*?)">(<font color=.*?>)?(.*?)</a></span></li>',
        html, re.S)

    # 输出结果
    for i in news_url:
        print(i[0], i[1], i[3])


def main():
	# 数码之家信息
    # get_digi_info()
    print('--' * 100)
    # get_ithome_info()
    print('--' * 100)
    # get_win10_info()
    get_home_info()


if __name__ == '__main__':
    main()
