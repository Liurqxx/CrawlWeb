# _*_coding:utf-8_*_
# Author:liu
import requests
import re
from fake_useragent import UserAgent

'''
    <tr class=.*?>
      <td class=.*?</td>\s+
      <td>(\d+.\d+.\d+.\d+)</td>\s+
      <td>(\d+)</td>\s+
        .*?
      <td class="country">高匿</td>\s+
      <td>(.*?)</td>\s+
      .*?
      <td>(\d+)天</td>\s+
      <td>.*?</td>\s+
    </tr>
'''


class get_proxy_ip(object):

    def __init__(self):
        self.base_url = 'http://www.xicidaili.com/nn/'

        self.headers = {
            'User-Agent': UserAgent().random,
        }

        # 最后的总ip列表
        self.ip_all_list = []

    def get_url_list(self, page_num):
        '''拼接所有的url地址'''
        url_list = []
        for page in range(1, page_num + 1):
            url_list.append(self.base_url + str(page))
        return url_list

    def send_request(self, url):
        '''发送请求数据'''
        html = requests.get(url, headers=self.headers).content.decode()
        return html

    def regex_pattern(self, data):
        '''清洗数据'''

        result_data_list = re.findall(
            r'''<tr class=.*?>\s+<td class=.*?</td>\s+<td>(\d+.\d+.\d+.\d+)</td>\s+<td>(\d+)</td>\s+.*?<td class="country">高匿</td>\s+<td>(.*?)</td>\s+.*?<td>\d+天</td>\s+<td>.*?</td>\s+</tr>''',
            data, re.S)

        return result_data_list

    def format_converse(self, page_data):
        '''对清洗后的数据进行格式转换，方便爬虫使用'''

        for info in page_data:
            dict_data = {}
            # ('111.155.116.237', '8123', 'HTTP')
            # ip  port type
            request_ip, request_port, request_type = info
            # 代理的格式 {'协议':'IP:port'}
            # proxy = {
            #     # 免费 的代理
            #     'https': '101.236.19.165:808'
            # }
            dict_data[str(request_type).lower()] = '{}:{}'.format(request_ip, request_port)

            # 对代理ip进行筛选，去除无效的ip
            try:
                # 测试格式:requests.get(url,proxies={'HTTP/HTTPS','http://ip地址:端口'})
                res = requests.get('http://ip.chinaz.com/', proxies=dict_data, timeout=2)

                # 能用的ip添加到总列表中
                self.ip_all_list.append(dict_data)
            except Exception as e:
                print('去除{}...'.format(dict_data))

        print('总可用数据：===', self.ip_all_list)

    def save_file(self):
        '''保存到文件中'''
        with open('./peoxy_list.txt', 'a') as f:
            f.write(str(self.ip_all_list))

        print('保存成功...')

    def run(self):
        '''运行程序'''
        # 获取所有的url地址
        url_list = self.get_url_list(3)
        for page in url_list:
            # 发送请求
            html_data = self.send_request(page)
            # 清洗数据
            result_data_list = self.regex_pattern(html_data)
            # 数据格式化
            self.format_converse(result_data_list)

            # 保存数据到文件中
            self.save_file()

        # 返回所有的数据
        return self.ip_all_list


if __name__ == '__main__':
    get_proxy_ip().run()
