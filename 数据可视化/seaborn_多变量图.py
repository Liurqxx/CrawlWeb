# _*_ coding:utf-8 _*_
# Author:liu
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def main():
    # 设置数据
    df_iris = pd.read_csv(r'iris.csv')
    # 使用默认配色
    sns.set(style='ticks')
    # 绘制多变量图 hue:选择分类别
    sns.pairplot(df_iris, hue='petal_length')
    plt.show()


if __name__ == '__main__':
    main()
