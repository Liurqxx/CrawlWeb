# _*_ coding: utf-8 _*_
import socket

# 目标地址IP/URL及端口
target_host = "127.0.0.1"
target_port = 9999


class send_info(object):
    '''发送数据类'''

    def __init__(self):
        # 创建一个socket对象
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接主机
        self.client.connect((target_host, target_port))

    # 发送数据
    def send_to(self, sendinfo=None):
        # 发送数据
        self.client.send(sendinfo)













