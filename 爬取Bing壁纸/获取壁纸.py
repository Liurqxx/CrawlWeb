import requests
import os
import datetime
import re
import shutil


def main():
    # 获取当前时间：格式：2018-04-24 20:09:12.222731
    dt = datetime.datetime.now()

    # 获取年月日并拼装
    cd = str(dt.year) + '0' + str(dt.month) + str(dt.day)

    if os.path.exists("Bing"):
        # 删除文件夹
        shutil.rmtree("./Bing")

    # 创建文件夹
    os.makedirs('./Bing', exist_ok=True)

    # 请求头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }

    # url地址
    url = 'http://bingwallpaper.com/'
    # 获取文件保存的路径信息
    img_save_path = os.getcwd() + "/Bing/"

    # 获取网页源代码
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    html = html.text
    # 提取图片地址
    img_url = re.findall(r'''class='cursor_zoom'><img src='(.*?)' alt=''', html, re.S)[0]

    # 下载图片
    img_data = requests.get(img_url).content

    # 保存图片
    with open(img_save_path + cd + '.jpg', "wb") as file:
        file.write(img_data)
        # 设置壁纸 file:....jpg:图片路径    gsettings set org.gnome.desktop.background picture-uri "file:/home/leon/pic/111.jpg"
        os.system(
            'gsettings set org.gnome.desktop.background picture-uri file:' + img_save_path + cd + '.jpg')


if __name__ == '__main__':
    main()
