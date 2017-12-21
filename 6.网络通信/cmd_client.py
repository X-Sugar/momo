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

    recv_len = int(str(sk.recv(1024),'utf8'))
    print('命令字节大小：%s' % recv_len)

    recv_data = bytes()
    while len(recv_data) != recv_len:
        recv = sk.recv(1024)
        recv_data += recv
    print(str(recv_data,'gbk'))
sk.close()