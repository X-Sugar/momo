# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/19 0019

# 一直通信
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen(3)

while True:
    conn,addr=sk.accept()
    while True:
        try:
            recv_data = str(conn.recv(1024), 'utf8')
        except Exception:
            break
        if not recv_data:
            conn.close()
            conn,addr = sk.accept()
            print('新的请求，地址：%s' % str(addr))
            continue
        print('接受数据：%s 地址：%s' % (recv_data, addr))

        send_data = input('请输入发送内容：')
        conn.send(bytes(send_data,'utf8'))
        if send_data == 'exit':
            break

sk.close()
