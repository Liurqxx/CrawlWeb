import requests
import subprocess
import random
import os

from urllib import request
from io import BytesIO
from PIL import Image
from aip import AipOcr

'''
    该程序适用于分辨率1920 x 1080
'''

#点击屏幕的参数
config = {
    '点击参数':{
        'title':(80,500,1000,880),
        'answers':(80,960,1000,1720),
        'point':[
            # (170,815,440,890),
            # (635,815,930,890),
            # (170,950,440,1000),
            # (635,950,930,1000),
            (190, 890, 880, 980),
            (190, 1060, 880, 1170),
            (190, 1230, 880, 1330),
            (190, 1400, 880, 1500),
        ]
    }
}

def get_screenshot():
    """获取手机图片"""
    #执行该命令获取手机的图片
    process = subprocess.Popen("adb shell screencap -p",shell=True,stdout=subprocess.PIPE)
    screenshot = process.stdout.read()
    #格式化
    screenshot = screenshot.replace(b"\r\r\n",b"\n")
    #将图片信息保存到图片中
    # with open('test.png','wb') as f:
    #     f.write(screenshot)
    #将图片信息写入到内存中
    img_fb = BytesIO()
    img_fb.write(screenshot)
    #处理图片
    img = Image.open(img_fb)
    #切出题目
    # title_img = img.crop((20,650,1060,790))
    title_img = img.crop((100, 690, 960, 860))
    #切出答案
    # answers_img = img.crop((20,795,1060,1055))
    answers_img = img.crop((100, 860, 960, 1560))
    #拼接
    # new_img = Image.new('RGBA',(1040,400))
    # new_img.paste(title_img,(0,0,1040,140))
    # new_img.paste(answers_img,(0,140,1040,400))
    new_img = Image.new('RGBA',(860,870))
    new_img.paste(title_img,(0,0,860,170))
    new_img.paste(answers_img,(0,170,860,870))

    #内存对象
    new_img_fb = BytesIO()
    new_img.save(new_img_fb,'png')

    # # 将图片信息保存到图片中
    # with open('test2.png','wb') as f:
    #     f.write(new_img_fb.getvalue())
    return new_img_fb

def get_word_by_img(img):
    """文字提取,调用百度文字识别接口"""
    App_ID='使用自己的APP_ID'
    API_Key='使用自己的API_Key'
    SECRET_Key='使用自己的SECRET_key'
    client = AipOcr(App_ID,API_Key,SECRET_Key)
    res = client.basicGeneral(img)
    return res


def baidu(question, answers):
    """搜索最有帮助的答案"""
    url = 'https://www.baidu.com/s'
    #User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36
    # headers ={'User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;", "Accept-Encoding": "gzip",
               "Accept-Language": "zh-CN,zh;q=0.8", "Referer": "http://www.example.com/",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}

    data = {
        'wd':question
    }
    #获取网页搜索的结果信息
    res = requests.get(url,params=data,headers=headers)
    res.encoding = 'utf-8'
    html = res.text
    #分析数据
    for i in range(len(answers)):
        answers[i] = (html.count(answers[i]),answers[i],i)
    #对结果进行排序
    answers.sort(reverse=True)
    return answers

def click(point):
    """点击屏幕"""
    cmd = "adb shell input swipe %s %s %s %s %s"%(
        point[0],
        point[1],
        point[0]+random.randint(0,3),
        point[1]+random.randint(0,3),
        200
    )
    os.system(cmd)


def main():
    """主函数入口"""
    print("准备答题...")
    while True:
        #hold 回车之后往下执行
        input("请输入回车进行答题:")
        # get_screenshot()
        #获取手机截图
        img = get_screenshot()
        # 文字提取
        info = get_word_by_img(img.getvalue())
        print(info)
        #获取对应的答案信息
        if info['words_result_num'] <5:
            continue
        answers = [x['words'] for x in info['words_result'][-4:]]
        question = ''.join([x['words'] for x in info['words_result'][:-4]])
        res = baidu(question,answers)
        print(res)
        click(config['点击参数']['point'][res[0][2]])

if __name__=="__main__":
    main()

