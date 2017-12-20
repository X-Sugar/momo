# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/20 0020

import socket,subprocess

sk = socket.socket()
sk.bind(('127.0.0.1',8888))
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
        print('接受的命令：%s 地址：%s' % (recv_data, addr))

        obj = subprocess.Popen(recv_data,shell=True,stdout=subprocess.PIPE)
        send_data = obj.stdout.read()
        # send_data = input('请输入发送内容：')
        conn.send(send_data)

sk.close()
