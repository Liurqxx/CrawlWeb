# _*_ coding:utf-8 _*_
# Author:liu

import urllib.request
from bs4 import BeautifulSoup






for i in range(0, 10):
    result_pf = soup_grades.find_all(attrs={"class": "g-ve"})
    userRating = result_pf[i].string
    print("评分为:{}".format(userRating))

    # userName = result35[i].get_text()
    result_data = soup_grades.find_all(attrs={"class": "tree-ellips-line6"})
    commentText = result_data[i].get_text()
    print("评论内容为:{}".format(commentText))
