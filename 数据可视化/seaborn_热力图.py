# _*_ coding:utf-8 _*_
# Author:liu
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def main():
    # 设置数据
    df_iris = pd.read_csv(r'iris.csv')

    corrmat = df_iris[df_iris.columns[:4]].corr()

    sns.heatmap(corrmat, square=True, linewidths=5, annot=True)
    plt.show()


if __name__ == '__main__':
    main()
