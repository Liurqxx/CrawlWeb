# _*_ coding:utf-8 _*_
# Author:liu
import simpleguitk as simplegui
import random

'''
    实现基本逻辑：
        1）设置图像
        2）定义一个图像块的类
        3）定义一个方法开始拼接图版
        4）重置游戏
        5）绘制游戏界面各元素
        6）定义鼠标的点击事件
        7）创建框架
        8）注册鼠标事件
        9）初始化游戏
        10）启动框架
        
'''

# 载入图像
baymax = simplegui.load_image(
    'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1522330165521&di=3f4c40d53f7da062bff2a8ba56f68b2a&imgtype=0&src=http%3A%2F%2Fimg01.taopic.com%2F160625%2F235106-1606250Q05845.jpg')

# 设置画布的宽高
WIDTH = 600
HEIGHT = WIDTH + 100
# 定义图片的边长，每个图像块就是200
IMAGE_SIZE = WIDTH / 3

# 定义图像坐标列表
all_coordinates = [[IMAGE_SIZE * 0.5, IMAGE_SIZE * 0.5], [IMAGE_SIZE * 1.5, IMAGE_SIZE * 0.5],
                   [IMAGE_SIZE * 2.5, IMAGE_SIZE * 0.5], [IMAGE_SIZE * 0.5, IMAGE_SIZE * 1.5],
                   [IMAGE_SIZE * 1.5, IMAGE_SIZE * 1.5], [IMAGE_SIZE * 2.5, IMAGE_SIZE * 1.5],
                   [IMAGE_SIZE * 0.5, IMAGE_SIZE * 2.5], [IMAGE_SIZE * 1.5, IMAGE_SIZE * 2.5], None]
# 棋盘的行列
ROWS = 3
COLS = 3
# 定义步数
steps = 0
# 保存所有的图像块的列表
board = [[None, None, None], [None, None, None], [None, None, None]]


# 定义一个图像框的类
class Square(object):
    # 初始化参数 coordinate:坐标值
    def __init__(self, coordinate):
        self.center = coordinate

    # 绘制图像块方法
    # canvas：
    # board_pos：
    def draw(self, canvas, board_pos):
        canvas.draw_image(baymax, self.center, [IMAGE_SIZE, IMAGE_SIZE],
                          [(board_pos[1] + 0.5) * IMAGE_SIZE, (board_pos[0] + 0.5) * IMAGE_SIZE],
                          [IMAGE_SIZE, IMAGE_SIZE])


# 开始拼接图版
def init_board():
    # 打乱图像块的坐标
    random.shuffle(all_coordinates)
    # 填充并且拼接图版
    for i in range(ROWS):
        for j in range(COLS):
            idx = i * ROWS + j
            square_center = all_coordinates[idx]

            if square_center is None:
                board[i][j] = None
            else:
                board[i][j] = Square(square_center)


# 重置游戏
def play_game():
    global steps
    steps = 0
    init_board()


# 绘制游戏界面各个元素
def draw(canvas):
    canvas.draw_image(baymax, [WIDTH / 2, WIDTH / 2], [WIDTH, WIDTH], [50, WIDTH + 50], [98, 98])
    # 画步数
    canvas.draw_text('步数：' + str(steps), [400, 680], 22, 'White')
    # 绘制游戏界面各个元素
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is not None:
                board[i][j].draw(canvas, [i, j])


# 鼠标点击事件
def mouseclick(pos):
    global steps
    # 将点击的位置换算成拼接板上的坐标
    r = int(pos[1] // IMAGE_SIZE)
    c = int(pos[0] // IMAGE_SIZE)
    if r < 3 and c < 3:
        # 点击到一个空白的位置
        if board[r][c] is None:
            return
        else:
            # 依次检查当前的图像块的周围是否有空位置，如果有就移动当前的图像块
            current_square = board[r][c]
            if r - 1 >= 0 and board[r - 1][c] is None:  # 判断上面
                board[r][c] = None
                board[r - 1][c] = current_square
                steps += 1
            elif c + 1 <= 2 and board[r][c + 1] is None:  # 判断右面
                board[r][c] = None
                board[r][c + 1] = current_square
                steps += 1
            elif r + 1 <= 2 and board[r + 1][c] is None:  # 判断下面
                board[r][c] = None
                board[r + 1][c] = current_square
                steps += 1
            elif c - 1 >= 0 and board[r][c - 1] is None:  # 判断左面
                board[r][c] = None
                board[r][c - 1] = current_square
                steps += 1


if __name__ == '__main__':
    # 创建框架
    frame = simplegui.create_frame('拼图', WIDTH, HEIGHT)
    frame.set_canvas_background('Black')
    frame.set_draw_handler(draw)
    frame.add_button('重新开始', play_game, 60)
    # 注册鼠标事件
    frame.set_mouseclick_handler(mouseclick)
    # 初始化游戏
    play_game()
    # 开始游戏
    frame.start()
