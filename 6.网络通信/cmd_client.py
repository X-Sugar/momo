# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/20 0020

import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8888))

while True:
    send_data = input('输入发送内容：')
    if send_data == 'exit':
        break
    sk.send(bytes(send_data, 'utf8'))

    recv_data = str(sk.recv(1024),'gbk')
    print('接收的消息：%s' % recv_data)

sk.close()