# _*_ coding:utf-8 _*_
# Author:liu

import urllib.request
from bs4 import BeautifulSoup

'''''
目标:获取酒店名称和酒店星级
'''
url1 = 'http://hotels.ctrip.com/hotel/435383.html'

html1 = urllib.request.urlopen(url1).read().decode('utf-8')

# 1.获取酒店名称信息
soup_name = BeautifulSoup(html1, 'lxml')

hotelName = soup_name.h2.string
print("酒店名称为:{}".format(hotelName))

# 2.获取酒店星级信息
result_star = soup_name.find_all(attrs={"class": "grade"})

# print(result1)
result_star = str(result_star)

soup_star = BeautifulSoup(result_star, 'lxml')

result_star = soup_star.find_all('span')
hotelStar = result_star[0]['title']
print("酒店星级为:{}".format(hotelStar))

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

'''''
目标:获取酒店卫生评分、环境评分、服务评分、设施评分、用户推荐比、用户评分、评价内容
'''

url3 = 'http://m.ctrip.com/html5/hotel/HotelDetail/dianping/435383.html'

html3 = urllib.request.urlopen(url3).read().decode('utf-8')

soup_grades = BeautifulSoup(html3, 'lxml')

# 获取酒店各项评分数据
result_grades = soup_grades.find_all(attrs={"class": "ve-txt"})
result_grades = str(result_grades)
soup32 = BeautifulSoup(result_grades, 'lxml')

result33 = soup32.find_all('em')
userRecommendRate = result33[0].string
hRating = result33[1].string
eRating = result33[2].string
sRating = result33[3].string
iRating = result33[4].string

print("用户推荐为:{}".format(userRecommendRate))
print("卫生评分为:{}分".format(hRating))
print("环境评分为:{}分".format(eRating))
print("服务评分为:{}分".format(sRating))
print("设施评分为:{}分".format(iRating))

# 提取用户评论数据



for i in range(0, 10):
    result_pf = soup_grades.find_all(attrs={"class": "g-ve"})
    userRating = result_pf[i].string
    print("评分为:{}".format(userRating))

    # userName = result35[i].get_text()
    result_data = soup_grades.find_all(attrs={"class": "tree-ellips-line6"})
    commentText = result_data[i].get_text()
    print("评论内容为:{}".format(commentText))
