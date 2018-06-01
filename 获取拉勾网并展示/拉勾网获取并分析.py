# _*_ coding:utf-8 _*_
# Author:liu
import requests
import re
import time
from utils import map_utils as mp
import random

'''
获取拉勾网招聘信息:
    需求:
        1:获取指定岗位的招聘信息
        2:对公司地区,公司待遇,学历情况,工作经验进行简单分析并可视化展示

    可视化分析:
        公司地区:柱状图,地图
        公司待遇:云图
        公司-学历情况:饼图
        公司工作经验:饼图

    模块:
        request:网络请求
        re:正则匹配数据
        pyecharts:可视化工具

    自定义工具类:map_utils

'''


def get_info(name, page_num):
    '''获取数据并统计'''
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false' # url地址
    # 请求头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }

    # 保存参数的字典
    city_all = {}
    money_all = {}
    education_all = {}
    workyear_all = {}
    good_all = {}

    for page in range(1, page_num + 1):
        if page % 6 == 0:
            time.sleep(60)
        # 请求参数
        my_data = {
            'first': 'true',
            'pn': page,
            'kd': name}
        # 获取网页源码
        html = requests.post(url, headers=headers, data=my_data)
        html.raise_for_status()
        html.encoding = 'utf-8'
        # print(html.json()['content']['positionResult'])
        result_json = html.json()['content']['positionResult']['result']

        for index, result in enumerate(result_json):
            # print(index, '-->', result)
            # print('公司:', result['companyShortName'])
            # print('公司全称:', result['companyFullName'])
            # print('---需要的技能:', result['industryLables'])
            # print('---地区:', result['district'])
            # print('---公司logo:', result['companyLogo'])
            # print('---融资:', result['financeStage'])
            # print('---创建时间:', result['createTime'])
            # print('---类型:', result['jobNature'])
            # print('---公司待遇:', result['companyLabelList'])
            # print('---人数需求:', result['companySize'])
            # print('---学历要求:', result['education'])
            # print('---工作经验:', result['workYear'])
            # print('---城市:', result['city'])
            # print('---工作内容:', result['industryField'])
            # print('---薪资情况:', result['salary'])
            # print('---薪资待遇:', result['positionAdvantage'])
            # print('--' * 100)

            # 统计地区分布
            city_all[result['city']] = city_all.get(result['city'], 0) + 1
            # 统计公司-薪资
            money_all[result['companyFullName']] = result['salary']
            # 统计学历需求
            education_all[result['education']] = education_all.get(result['education'], 0) + 1
            # 统计工作经验情况
            workyear_all[result['workYear']] = workyear_all.get(result['workYear'], 0) + 1
            # 待遇情况
            good_all[result['positionAdvantage']] = random.randint(1, 20)

        print('完成{}页.'.format(page))
    # {'杭州': 5, '深圳': 15, '苏州': 5, '广州': 5, '上海': 5, '北京': 40}
    return city_all, money_all, education_all, workyear_all, good_all


def main():
    # 循环每一页获取数据
    city_all, money_all, education_all, workyear_all, good_all = get_info('Python', 10)

    # 地区柱状图展示
    mp.create_Bar_charts(city_all, '地区分布').render('./地区分布_bar.html')

    # 地区geo展示
    mp.create_geo_charts(city_all, '地区分布').render('./地区分布_geo.html')

    # 学历要求
    mp.create_Pie_charts(education_all, '学历情况').render('./学历情况.html')

    # 工作经验
    mp.create_Pie_charts(workyear_all, '工作经验').render('./工作经验.html')

    # 薪资待遇
    mp.create_clound_charts(good_all, '薪资待遇').render('./薪资待遇.html')

    print('统计完成...')


if __name__ == '__main__':
    main()
