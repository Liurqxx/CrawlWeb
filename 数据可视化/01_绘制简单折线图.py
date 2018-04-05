# _*_ coding:utf-8 _*_
# Author:liu
import matplotlib.pyplot as plt


def main():
    # 定义Y轴数据
    y_data = [1, 4, 9, 16, 25]
    # 定义X轴数据
    x_data = [1, 2, 3, 4, 5]
    # 设置微软雅黑字体，目的支持中文
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

    # 设置标题,并且给坐标轴添加标签
    plt.title('title', fontsize=24)
    plt.xlabel('x_value', fontsize=14)
    plt.ylabel('y_value', fontsize=14)
    # 设置两个轴刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)

    # 绘制图形
    # linewidth:线宽
    plt.plot(x_data, y_data, linewidth=3)
    plt.show()


if __name__ == '__main__':
    main()
