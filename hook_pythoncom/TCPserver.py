# -*- coding: utf-8 -*-
import socket
import threading

'''服务器端'''

# 监听的IP及端口
bind_ip = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)


def handle_client(client_socket):
    request = client_socket.recv(1024)

    print "[*] Received:%s" % request

    client_socket.send("ok!")

    client_socket.close()


while True:
    client, addr = server.accept()

    print "[*] Accept connection from:%s:%d" % (addr[0], addr[1])

    client_handler = threading.Thread(target=handle_client, args=(client,))

    client_handler.start()















