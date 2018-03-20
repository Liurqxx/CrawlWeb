# _*_ coding:utf-8 _*_
# Author:liu
import scrapy
from bqb.items import BqbItem

'''
    抓取表情党网的表情包数据
'''


# 创建类继承scrapy.Spider
class Myspider(scrapy.Spider):
    name = 'bqb'

    def start_requests(self):
        '''访问url地址并得到网页数据'''
        start_urls = ['http://qq.yh31.com/zjbq/2920180.html', 'http://qq.yh31.com/zjbq/2920180_2.html']
        for url in start_urls:
            # 对列表内的url地址进行访问
            # yield:返回并运行，url:告诉我要去的地址，callback:获取到的界面信息在哪个函数进行下一步操作
            yield scrapy.Request(url=url, callback=self.parse)

    # response获取到的数据
    def parse(self, response):
        '''处理得到的网页数据'''
        # 得到图片url地址范围
        img_urls = response.xpath("//div[@id='fontzoom']/p/img")
        a = 0
        for img_url in img_urls:
            # 得到详细的图片url地址
            url = img_url.xpath("@src").extract()
            item = BqbItem()
            item['name'] = a
            item['addr'] = url[0]
            a += 1
            yield item
