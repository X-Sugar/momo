# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/19 0019

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8888))
sk.listen(3)

while True:
    conn,addr=sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
            # recv_data = str(conn.recv(1024),'utf8')
        except Exception:
            break
        print('接收的消息：%s' % str(data,'utf8'))

        send_data = input('输入发送内容：')
        if send_data == 'exit':
            break
        conn.send(bytes(send_data,'utf8'))

    sk.close()