# _*_ coding:utf-8 _*_
# Author:liu
import matplotlib.pyplot as plt


def main():
    # 绘制散点图
    # 参数：x轴，y轴,s:点的大小，
    # 绘制一个点
    plt.scatter(2, 4, s=200)

    # 设置标题,并且给坐标轴添加标签
    plt.title('title', fontsize=24)
    plt.xlabel('x_value', fontsize=10)
    plt.ylabel('y_value', fontsize=10)
    # 设置两个轴刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)

    plt.show()


def many():
    # 设置元素
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]

    # 绘制一系列点
    plt.scatter(x_values, y_values, s=100)

    # 设置标题,并且给坐标轴添加标签
    plt.title('title', fontsize=24)
    plt.xlabel('x_value', fontsize=10)
    plt.ylabel('y_value', fontsize=10)

    # 设置两个轴刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)

    # 显示散点图
    plt.show()


if __name__ == '__main__':
    main()
    many()
