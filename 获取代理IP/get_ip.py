# _*_ coding:utf-8 _*_
# Author:liu

# encoding=utf8
import socket
import requests
import re
import random
import urllib

list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"

]


class proxy:
    def __init__(self):
        self.proxy_list = []  # 获取到的ip列表
        self.proxy_filter_list = []

    def get_random_header(self):
        headers = {'User-Agent': random.choice(list),
                   'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   'Accept-Encoding': 'gzip'}
        return headers

    def get_proxy(self):
        """
        IP获取
        :return:
        """
        header = {
            "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }

        for i in range(1, 20):
            url = 'http://www.xicidaili.com/nn/' + str(i)
            html = requests.get(url, headers=self.get_random_header()).text
            # print(html)
            ip_list = re.findall(
                r'''<tr.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td class="country">.*?</td>\s+<td>(.*?)</td>.*?</tr>''',
                html, re.S)
            print('获取到的ip列表:', ip_list)

            self.proxy_list.append(ip_list)

    def filter_proxy(self):
        """
        IP筛选
        """
        # socket.setdefaulttimeout(2)
        f = open("./proxy_list", "w")
        url = "http://ip.chinaz.com/"
        proxy_num = 0
        for proxy in self.proxy_list:
            # 获取到元祖数据
            for filter_ip in proxy:
                ip_adress, request_port, request_type = filter_ip
                # print(ip_adress, request_type, request_port)
                # 构造请求地址
                proxy_temp = {"{}".format(request_type.lower()): "{}://{}:{}".format(request_type.lower(), ip_adress,
                                                                                     request_port)}
                print(proxy_temp)
                try:
                    # 测试格式:requests.get(url,proxies={'HTTP/HTTPS','http://ip地址:端口'})
                    res = requests.get(url, proxies=proxy_temp, timeout=2)
                    print('res:', res)
                    write_proxy = ip_adress + "\n"
                    f.write(write_proxy)
                    proxy_num += 1
                except Exception as e:
                    print("代理链接超时，去除此IP：{0}".format(filter_ip))
                    # print(e)
                    continue
        print("总共可使用ip量为{}个".format(proxy_num))

    def get_filter_proxy(self):
        """
        读取该可用ip文件
        :return: 可用ip文件list
        """
        f = open("./proxy_list", "r")
        lins = f.readlines()
        for i in lins:
            p = i.strip("\n")
            self.proxy_filter_list.append(p)
        return self.proxy_filter_list

    def main(self):
        self.get_proxy()
        self.filter_proxy()


if __name__ == "__main__":
    a = proxy()
    a.get_proxy()
    a.filter_proxy()
    # a.get_filter_proxy()
