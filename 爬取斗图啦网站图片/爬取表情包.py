# _*_coding:utf-8_*_
# Author:liu
import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}


def main():
      url_list = []
    for i in range(1, 10):
        # 　页面url
        page_url = "http://www.doutula.com/article/list/?page=" + str(i)
        # 得到网页源代码
        html = requests.get(page_url, headers=headers)
        html.encoding = "utf-8"
        html = html.text
        # print(html)
        # 匹配得到每页的表情数据
        url_title_list = re.findall(r'<a href="(.*?)" class="list-group-item random_list">', html)
        # 把地址保存到列表内
        url_list.append(url_title_list)
    # 请求每个图片的连接
    for i in url_list:
        for img_data in i:
            img_html_data = requests.get(img_data, headers=headers)
            img_html_data.encoding = "utf-8"
            img_html_data = img_html_data.text
            # 　提取图片地址
            img_url = re.findall(r'<meta property="og:image" content="(.*?)"/>', img_html_data)[0]

            # 截取名字
            # http://img.doutula.com/production/uploads/image//2018/04/20/20180420238483_aIMRwz.gif
            img_name = img_url.split('/')[10]
            # 下载图片
            with open('./img/' + img_name, 'wb') as file:
                img_info = requests.get(img_url, headers=headers).content
                file.write(img_info)
            print('下载成功...')


if __name__ == '__main__':
    main()
