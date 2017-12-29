# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/25 0025

import socket

ip_port = ('127.0.0.1',8091)
sk = socket.socket()
sk.connect(ip_port)
print('Client startting...')

while True:
    send_data = input('输入发送内容：')
    if send_data == 'exit':
        break
    sk.send(bytes(send_data, 'utf8'))

    recv_data = str(sk.recv(1024),'utf8')
    print('接收的消息：%s' % recv_data)

sk.close()