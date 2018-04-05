# _*_ coding:utf-8 _*_
# Author:liu
import matplotlib.pyplot as plt
from random import choice

'''
    根据用户输入的点数量随机生成散点图
'''


# 创建RandomWalk类
class RandomWalk(object):
    '''生成随机数据'''

    def __init__(self, num_points=5000):
        '''初始化随机漫步的属性'''
        self.num_points = num_points
        # 所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    # 生成漫步包含的点，并且决定每次漫步的方向
    def fill_walk(self):
        '''计算随机漫步包含的所有点'''

        # 不断的漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及前进的距离
            # 选择前进的方向。1->左 -1->右
            x_direction = choice([1, -1])
            # 随机选择一个前进的距离
            x_distance = choice([0, 1, 2, 3, 4])
            # 前进的步长
            x_step = x_direction * x_distance

            # y轴选择前进的方向和距离
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


if __name__ == '__main__':
    # 绘制随机漫步
    # 生成随机漫步数据，参数可有可无，默认为5000
    random_walk = RandomWalk()
    random_walk.fill_walk()

    # 设置绘图窗口的大小和尺寸
    plt.figure(figsize=(10, 6))

    # 每个点不同的颜色映射
    # point_number：所有数据的列表
    point_number = list(range(random_walk.num_points))

    # 绘制随机漫步
    plt.scatter(random_walk.x_values, random_walk.y_values, c=point_number, cmap=plt.cm.Blues, s=15)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c='red', edgecolors='none', s=50)

    # 设置x和y轴不可见
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
