# _*_ coding:utf-8 _*_
# Author:liu

import os
import PIL
import numpy
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation

'''
    准备工具；
        1）adb驱动
        2）安卓手机
        3）打开手机调试模式
        4）usb线连接手机电脑
        5）pycharm IDE

    实现原理：
        1）获取手机的实时截图
        2）点击起始位置和落地位置
        3）计算两个点的距离(利用勾股定理)
        4）计算按压时间
        5）发送按压指令
        6）重新刷新手机截图
'''
# 设置锁，判断是否需要刷新
need_update = True


def get_screen_image():
    '''获取手机截图返回对应的二维数组'''
    # 获取屏幕截图保存到sdcard根目录下，文件名：screen.png
    os.system('adb shell screencap -p /sdcard/screen.png')
    # 把截图拿到当前文件夹下
    os.system('adb pull /sdcard/screen.png')
    # 打开图片,操作图片 PIL.Image.open('screen.png')
    # 返回二维数组信息 numpy.array
    return numpy.array(PIL.Image.open('screen.png'))


def jump_to_next(point1, point2):
    '''跳的函数'''
    # point1:起始坐标  point2：终点坐标
    # 得到起始点对应的x坐标和y坐标
    x1, y1 = point1
    # 得到终点对应的x坐标和y坐标
    x2, y2 = point2
    # 使用勾股定理计算两点之间的位置
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    # 开始跳 swipe按压
    # 四个参数：第一个：按下去的横坐标，第二个：按下去的纵坐标
    #           第三个：抬起来的横坐标 第四个：抬起来的纵坐标
    # 一个像素点按压时间1.35毫秒
    os.system('adb shell input swipe 320 410 320 410 {}'.format(int(distance * 1.35)))


def on_click(event, coor=[]):
    '''绑定的鼠标单击事件'''
    global need_update
    # event：点击的坐标位置
    # 添加起始位置和终点位置的xy坐标
    coor.append((event.xdata, event.ydata))  # [(x,y),(x,y)]
    # 两次点击坐标都添加了，可以执行了
    if len(coor) == 2:
        # 开始跳,传入坐标参数同时清空列表内数据
        jump_to_next(coor.pop(), coor.pop())
    need_update = True


def update_screen(frame):
    '''更新重画图片'''
    global need_update

    if need_update:
        time.sleep(1)
        # 重画图片
        axes_image.set_array(get_screen_image())
        need_update = False
    return axes_image,


# 创建一个空白的图片对象
figure = plt.figure()
# 把获取的图片画在坐标轴上
axes_image = plt.imshow(get_screen_image(), animated=True)
# 执行鼠标点击回调函数  注：传递on_click对象
figure.canvas.mpl_connect('button_press_event', on_click)
# 循环刷新图片 interval刷新的时间
ani = FuncAnimation(figure, update_screen, interval=50, blit=True)
# 展示图片
plt.show()
