# _*_ coding:utf-8 _*_
# Author:liu

import urllib.request
from bs4 import BeautifulSoup



'''''
目标:获取酒店最低房价和评论总数
'''
url2 = "http://m.ctrip.com/html5/hotel/HotelDetail/435383.html"

html2 = urllib.request.urlopen(url2).read().decode('utf-8')

soup_comment = BeautifulSoup(html2, 'lxml')
# 评论总数
result_comment = soup_comment.find_all(attrs={"class": "hd js_comment_title"})
result_comment = str(result_comment)
soup_comment = BeautifulSoup(result_comment, 'lxml')
commentCounts = soup_comment.find_all('em')[1].string
print("评论总数为:{}".format(commentCounts))


# 提取用户评论数据



for i in range(0, 10):
    result_pf = soup_grades.find_all(attrs={"class": "g-ve"})
    userRating = result_pf[i].string
    print("评分为:{}".format(userRating))

    # userName = result35[i].get_text()
    result_data = soup_grades.find_all(attrs={"class": "tree-ellips-line6"})
    commentText = result_data[i].get_text()
    print("评论内容为:{}".format(commentText))
