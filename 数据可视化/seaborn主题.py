# _*_ coding:utf-8 _*_
# Author:liu
import matplotlib.pyplot as plt
import seaborn as sns

'''
    set_style():用来设置主题
        五个预设好的主题：darkgrid,whitegrid,dark,white,ticks,默认darkgrid

'''


def main():
    # 设置主题
    sns.set_style('whitegrid')
    # 设置数据
    plt.plot(range(10))
    plt.show()


if __name__ == '__main__':
    main()
