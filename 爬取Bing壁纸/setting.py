# _*_ coding:utf-8 _*_
# Author:liu
import os
import sys

'''
    # 设置壁纸 file:....jpg:图片路径    gsettings set org.gnome.desktop.background picture-uri "file:/home/leon/pic/111.jpg"
    os.system(
        'gsettings set org.gnome.desktop.background picture-uri file:' + img_save_path + cd + '.jpg')

'''
def main():
    fr = 0
    # 判断文件夹是否存在
    if not os.path.exists('./img_source'):
        os.mkdir('./img_source')
        os.system('touch ./img_source/info.txt')
        try:
            with open('./img_source/info.txt', 'w') as file:
                file.write('1')
        except Exception as e:
            print(e)

        finally:
            with open('./img_source/info.txt', 'w') as file:
                file.write('1')

    with open('./img_source/info.txt', 'r') as file:
        fr = file.read()
    with open('./img_source/info.txt', 'r') as file:
        fr = file.read()
    # 设置壁纸
    os.system(
        'gsettings set org.gnome.desktop.background picture-uri file:/home/lrq/传智播客/PycharmProjects/爬取壁纸/img_source/bg' + fr + '.jpg')

    with open('./img_source/info.txt', 'w') as file:
        f = int(fr)
        f += 1
        if f % 9 == 0:
            f = 1
        file.write(str(f))



if __name__ == '__main__':
    main()
