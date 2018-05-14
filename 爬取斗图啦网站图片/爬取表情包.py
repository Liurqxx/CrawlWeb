# _*_coding:utf-8_*_
# Author:liu
import re
import requests
import threading

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}



        page_url = "http://www.doutula.com/article/list/?page=" + str(i)
        # 得到网页源代码
        html = requests.get(page_url, headers=headers)
        html.encoding = "utf-8"
        html = html.text
        # 匹配得到每页的表情数据
        url_title_list = re.findall(r'<a href="(.*?)" class="list-group-item random_list">', html)

        # 开启线程下载每页图片
        t1 = threading.Thread(target=down_img, args=(url_title_list,))
        t1.start()
    t1.join()


if __name__ == '__main__':
    main()
