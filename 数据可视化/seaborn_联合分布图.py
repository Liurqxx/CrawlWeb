# _*_ coding:utf-8 _*_
# Author:liu
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def main():
    # 设置数据
    df_iris = pd.read_csv(r'iris.csv')
    # 绘制箱形图
    sns.jointplot(x=df_iris['petal_length'], y=df_iris['sepal_length'], kind='hex')

    plt.show()


if __name__ == '__main__':
    main()
