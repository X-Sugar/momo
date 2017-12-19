# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/19 0019

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8888))
sk.listen(3)

conn,addr=sk.accept()

while True:
    recv_data = str(conn.recv(1024),'utf8')
    print('接收的消息：%s' %recv_data)

    send_data = input('输入发送内容：')
    if recv_data == 'exit':
        break
    conn.send(bytes(send_data,'utf8'))

sk.close()