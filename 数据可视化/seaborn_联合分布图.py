# _*_ coding:utf-8 _*_
# Author:liu
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def main():
    # 设置数据
    df_iris = pd.read_csv(r'info.csv')
    # 绘制箱形图
    sns.jointplot(x=df_iris['Sepal length'], y=df_iris['Sepal width'], kind='hex')

    plt.show()


if __name__ == '__main__':
    main()
