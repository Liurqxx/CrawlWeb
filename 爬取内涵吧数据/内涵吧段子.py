# _*_coding:utf-8_*_
# Author:liu
import re
import requests

from fake_useragent import UserAgent


class get_data(object):

    def __init__(self):
        self.base_url = 'https://www.neihan8.com/article/'
        self.headers = {
            'User-Agent': UserAgent().random,
        }

        # 1.第一层解析数据
        # <div class="desc">(.*?)</div>
        self.first_pattern = re.compile('<div class="desc">(.*?)</div>', re.S)

        # 2.第二层解析
        # 1.标签          <(.*?)>
        # 2.字符实体       &(.*?);
        # 3,空白          \s

        self.second_pattern = re.compile('<(.*?)>|&(.*?);|\s')

    def get_max_num(self):
        # 获取总页数

        html = requests.get(self.base_url, headers=self.headers).content.decode()
        # print(html)

        # 创建正则对象 <span>21861条记录 2 / 1094 页</span>
        patter = re.compile('<span>.*条记录 .* / (.*) 页</span>')

        # 匹配数据,得到最大页数
        max_num = patter.findall(html)[0]
        print('最大页数：', max_num)
        return max_num

    def get_url_list(self):
        # 获取所有页面的url
        # 获取最大页数
        max_pages = self.get_max_num()

        url_lists = []
        # 拼接每个页面的url
        for i in range(1, int(max_pages)):
            url_lists.append(self.base_url + 'index_{}.html'.format(i))

        return url_lists

    def send_request(self, url):
        # 获取每页数据
        response_data = requests.get(url, headers=self.headers).content.decode()

        return response_data

    def analysis_data(self, data):
        # 清洗每页数据,第一次清洗
        result_list = self.first_pattern.findall(data)
        return result_list

    def save_file(self, data, page):
        '''
        :param data: 保存的数据
        :param page: 对应的页数
        :return:
        '''
        # 拼接页标题
        title_data = '---------------------------------------第{}页---------------------------------------\r\n\r\n'.format(
            page)
        print(title_data, '写入成功')
        with open('./NeihanBa.txt', 'a') as f:
            # 写入标题
            f.write(title_data)
            # 对每页数据进行初次清洗
            analysis_result = self.analysis_data(data)
            # 对每页数据进一步清洗
            for content in analysis_result:
                # 过滤每一条段子中的多余内容
                new_content = self.second_pattern.sub('', content) + '\r\n\r\n'
                # 写入文件中
                f.write(new_content)

    def run(self):

        # 遍历得到的url列表，对每个url进行请求获取数据
        url_list = self.get_url_list()
        for index, url in enumerate(url_list):
            # 获取每页数据
            response_data = self.send_request(url)

            # 对数据进行保存
            self.save_file(response_data, index + 1)


if __name__ == '__main__':
    get_data().run()
