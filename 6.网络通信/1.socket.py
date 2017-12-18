# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/18 0018

import socket

sk = socket.socket()
# print(sk)

address = ('127.0.0.1',8000)
sk.bind(address)

sk.listen(5)

print('waiting......')

conn = sk.accept()
print (conn)


# sk.sendall(bytes("Hello world",encoding="utf-8"))

#(<socket.socket fd=436, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 11244)>, ('127.0.0.1', 11244))
