# encoding=utf-8
import requests
import os
import datetime
import re
import shutil
import time


def main():
    # 获取当前时间：格式：2018-04-24 20:09:12.222731
    dt = datetime.datetime.now()

    # 获取年月日并拼装
    cd = str(dt.year) + '0' + str(dt.month) + str(dt.day)

    if os.path.exists("Bing"):
        # 删除文件夹
        shutil.rmtree("./Bing")


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
