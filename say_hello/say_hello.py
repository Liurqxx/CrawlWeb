import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QIcon  # QtWidgets不包含QFont必须调用QtGui
from PyQt5 import QtGui, QtCore
import random


class MessageBox(QtWidgets.QWidget):  # 继承自父类QtWidgets.QWidget
    CloseAllowed = 0

    def __init__(self, parent=None):  # parent = None代表此QWidget属于最上层的窗口,也就是MainWindows.
        QtWidgets.QWidget.__init__(self)  # 因为继承关系，要对父类初始化
        # 通过super初始化父类，__init__()函数无self，若直接QtWidgets.QWidget.__init__(self)，括号里是有self的
        self.setGeometry(300, 300, 800,
                         800)  # setGeometry()方法完成两个功能--设置窗口在屏幕上的位置和设置窗口本身的大小。它的前两个参数是窗口在屏幕上的x和y坐标。后两个参数是窗口本身的宽和高
        # self.resize(1000, 500)  # 设置窗体大小，本行可有可无。
        self.center()  # 自定义一个居中的函数
        self.setFixedSize(self.width(), self.height());  # PyQT禁止调整窗口大小和窗口最大化按钮
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  # PyQT禁止窗口最大化按钮和关闭按钮
        self.setWindowTitle(u'表白神器，你的专属')  # 仅仅设置窗体标题，不设置位置。
        self.setWindowIcon(QIcon(
            'rose.png'))  # 调用QIcon构造函数时，我们需要提供要显示的图标的路径(相对或绝对路径)。同时注意：使用QIcon类型必须导入此模块from PyQt5.QtGui import QIcon
        self.setToolTip(u'哈哈哈')  # 调用setToolTip()方法,该方法接受富文本格式的参数,css之类。
        QtWidgets.QToolTip.setFont(QFont('华文楷体', 10))  # 设置字体以及字体大小
        self.label1 = QtWidgets.QLabel(u'<b>小姐姐，观察你很久了！</b>', self)  # 建立一个标签
        self.label1.move(150, 40)  # 使此标签移动到这个部件(260,40)的位置
        self.label1.setFont(QFont("Timers", 20));  # 设置字体与字体大小
        self.label2 = QtWidgets.QLabel(u'<b>做我女朋友好不好?</b>', self)  # 建立一个标签
        self.label2.move(150, 100)  # 使此标签移动到这个部件(260,100)的位置
        self.label2.setFont(QFont("Timers", 20));  # 设置字体与字体大小

        # Qt中提供的调色板QPalette类就是专门用于管理控件的外观显示。QPalette类相当于对话框或控件的调色板，管理着控件和窗体的所有颜色。
        # 每个窗体和控件都包含一个QPalette对象，在显示时，对其做相应的设置即可
        self.window_pale = QtGui.QPalette()  # 实例化QPalette类
        self.window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("img.jpg")))  # 打开图片
        self.setPalette(self.window_pale)  # 应用背景色
        # setStyleSheet来设置图形界面的外观

        self.buttonOK = QtWidgets.QPushButton(u'同意',
                                              self)  # 因为需要增加按钮，所以我们引入了QPushButton类,该按钮是QPushButton类的一个实例。构造函数的第一个参数是按钮的标签。第二个参数是父窗口小部件。父窗口小部件是示例窗口小部件，它是通过QWidget继承的
        self.buttonOK.setFocusPolicy(QtCore.Qt.NoFocus)  # 按钮无焦点
        # Qt::TabFocus 0x1  接受Tab键焦点
        # Qt::ClickFocus 0x2 接受鼠标单击做焦点
        # Qt::StrongFocus TabFocus | ClickFocus | 0x8 接受Tab键和鼠标单击做焦点
        # Qt::WheelFocus StrongFocus | 0x4  滑轮作为焦点选中事件
        # Qt::NoFocus 0 不接受焦点
        self.buttonOK.move(50, 700)  # move()方法来指定部件的放置坐标，坐标的顶点就是窗口的左上角
        self.buttonOK.clicked.connect(self.showDialogOK)

        self.buttonE = QtWidgets.QPushButton(u'考虑考虑',
                                             self)  # 因为需要增加按钮，所以我们引入了QPushButton类,该按钮是QPushButton类的一个实例。构造函数的第一个参数是按钮的标签。第二个参数是父窗口小部件。父窗口小部件是示例窗口小部件，它是通过QWidget继承的
        self.buttonE.setFocusPolicy(QtCore.Qt.NoFocus)  # 按钮无焦点
        # Qt::TabFocus 0x1  接受Tab键焦点
        # Qt::ClickFocus 0x2 接受鼠标单击做焦点
        # Qt::StrongFocus TabFocus | ClickFocus | 0x8 接受Tab键和鼠标单击做焦点
        # Qt::WheelFocus StrongFocus | 0x4  滑轮作为焦点选中事件
        # Qt::NoFocus 0 不接受焦点
        self.buttonE.move(330, 700)  # move()方法来指定部件的放置坐标，坐标的顶点就是窗口的左上角
        self.buttonE.clicked.connect(self.showDialogEE)

        self.buttonNO = QtWidgets.QPushButton(u'拒绝',
                                              self)  # 因为需要增加按钮，所以我们引入了QPushButton类,该按钮是QPushButton类的一个实例。构造函数的第一个参数是按钮的标签。第二个参数是父窗口小部件。父窗口小部件是示例窗口小部件，它是通过QWidget继承的
        self.buttonNO.setFocusPolicy(QtCore.Qt.NoFocus)  # 按钮无焦点
        # Qt::TabFocus 0x1  接受Tab键焦点
        # Qt::ClickFocus 0x2 接受鼠标单击做焦点
        # Qt::StrongFocus TabFocus | ClickFocus | 0x8 接受Tab键和鼠标单击做焦点
        # Qt::WheelFocus StrongFocus | 0x4  滑轮作为焦点选中事件
        # Qt::NoFocus 0 不接受焦点
        self.buttonNO.move(610, 700)  # move()方法来指定部件的放置坐标，坐标的顶点就是窗口的左上角
        self.buttonNO.clicked.connect(self.showDialogNO)

    def showDialogOK(self):
        QtWidgets.QMessageBox.information(self, "欧耶", "爱你,么么么么么么么哒～～～", QtWidgets.QMessageBox.Ok)
        self.CloseAllowed = 1

    def showDialogEE(self):
        QtWidgets.QMessageBox.information(self, "别纠结了", "你完了，你妈让你嫁给我", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "你爸也是这么说的", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "你奶奶也让你嫁给我", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "你哥哥也同意了，你全家都同意", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "你闺蜜说嫁给我没错", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "你爸说不同意就打你", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "接受现实吧，我会对你好的", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "你都是我的人了", QtWidgets.QMessageBox.Ok)

    def showDialogNO(self):
        self.q = random.randint(0, 650)  # 在0-650内生成随机的X坐标
        self.w = random.randint(150, 650)  # 在150-650内生成随机的Y坐标
        self.buttonNO.move(self.q, self.w)


        # enterEvent事件PyQt自动运行,无需调用

    # def enterEvent(self,event):#重写了鼠标的enterEvent事件，由于继承了窗口类，鼠标一进入主窗口便会出发此函数
    #     self.q=random.randint(0,650)#在0-650内生成随机的X坐标
    #     self.w=random.randint(150,650)#在150-650内生成随机的Y坐标
    #     self.buttonNO.move(self.q,self.w)

    # 当我们关闭一个窗口时，在PyQt中就会触发一个QCloseEvent的事件，正常情况下会直接关闭这个窗口，
    # 但是我们不希望这样的事情发生，所以我们需要重新定义QCloseEvent，函数名称为closeEvent不可变
    def closeEvent(self, event):  # 函数名固定不可变

        if self.CloseAllowed == 1:
            event.accept()  # 关闭窗口
        else:
            QtWidgets.QMessageBox.information(self, "未作回应", "小姐姐,请不要逃避!", QtWidgets.QMessageBox.Ok)
            event.ignore()  # 忽视点击X事件

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()  # 获取屏幕分辨率
        # QtWidgets.QDesktopWidget().screenGeometry()中QDesktopWidget()也有括号
        size = self.geometry()  # 获取窗口尺寸
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)  # 利用move函数窗口居中


app = QtWidgets.QApplication(sys.argv)
window = MessageBox()
window.show()
sys.exit(app.exec_())
