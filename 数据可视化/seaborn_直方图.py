# _*_ coding:utf-8 _*_
# Author:liu
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def main():
    # 设置数据
    df_iris = pd.read_csv(r'info.csv')
    # kde:密度线 rug：边际毛毯
    sns.distplot(df_iris['Petal length'], kde=True, rug=True)
    plt.show()


if __name__ == '__main__':
    main()
