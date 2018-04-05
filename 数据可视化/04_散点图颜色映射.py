# _*_ coding:utf-8 _*_
# Author:liu
import matplotlib.pyplot as plt


def main():
    # x轴列表数据
    x_values = list(range(1, 1001))
    # 列表推导式生成y轴数据
    y_values = [x ** 2 for x in x_values]
    # 设置数据
    # c:定义颜色，可使用rgb，edgecolor=none:去除轮廓,默认是蓝色点黑色轮廓
    # y轴根据高度的变化来映射颜色的变化，数值越大，颜色越深
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
    # 设置每个坐标轴的取值范围
    plt.axis([0, 1100, 0, 1100000])
    # 保存图片, bbox_inches='tight'：设置图片周围无多余的空白区域
    plt.savefig('img.png', bbox_inches='tight')

    # 显示散点图
    plt.show()


if __name__ == '__main__':
    main()
