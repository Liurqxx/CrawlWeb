# _*_ coding:utf-8 _*_
# Author:liu
import matplotlib.pyplot as plt


def main():
    # x轴列表数据
    x_values = list(range(1, 1001))
    # 列表推导式生成y轴数据
    y_values = [x ** 2 for x in x_values]
    # c:定义颜色，可使用rgb，edgecolor=none:去除轮廓,默认是蓝色点黑色轮廓
    plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
    # 设置每个坐标轴的取值范围
    plt.axis([0, 1100, 0, 1100000])
    # 显示散点图
    plt.show()


if __name__ == '__main__':
    main()
