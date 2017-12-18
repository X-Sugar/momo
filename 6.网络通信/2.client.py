# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/18 0018

import socket

sk=socket.socket()

address=('127.0.0.1',8000)

sk.connect(address)
print(sk)

#<socket.socket fd=380, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 11244), raddr=('127.0.0.1', 8000)>
