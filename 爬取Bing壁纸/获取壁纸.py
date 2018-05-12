# encoding=utf-8
import requests
import os
import datetime
import re
import shutil
import time


def main():


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
    print('完成时间', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


if __name__ == '__main__':
    main()
