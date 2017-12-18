# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/18 0018

import socket

sk = socket.socket()
print(sk)
sk.bind(("127.0.0.1",8080))
sk.listen(5)

conn,address = sk.accept()
sk.sendall(bytes("Hello world",encoding="utf-8"))