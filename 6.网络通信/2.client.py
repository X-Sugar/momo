# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/18 0018

"""
# 进行一次通信

import socket

sk=socket.socket()       # 创建socket对象

sk.connect(("127.0.0.1",8888))      # 绑定端口,“127.0.0.1”代表本机地址，8888为设置链接的端口地址

send_data = input("输入发送内容：")
sk.sendall(bytes(send_data,encoding='utf8'))    # str(data,encoding="utf8")用“utf8”进行解码

accept_data = sk.recv(1024)     # conn.recv()接收客户端的内容，接收到的是bytes类型数据
print(str(accept_data,encoding='utf8'))

sk.close()
"""

# -----------------------------------------------------

"""
# 一直通讯

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9008))  # 主动初始化与服务器端的连接

while True:
    send_data = input("输入发送内容:")
    sk.sendall(bytes(send_data, encoding="utf8"))
    if send_data == "byebye":
        break
    accept_data = str(sk.recv(1024), encoding="utf8")
    print("".join(("接收内容：", accept_data)))
sk.close()

"""

# --------------------------------------------------------
"""
import socket

sk = socket.socket()
sk.connect(("127.0.0.1",8888))

while True:
    send_data = input("输入发送内容：")
    sk.sendall(bytes(send_data,encoding="utf8"))
    if send_data == "byebye":
        break
    accept_data = str(sk.recv(1024),encoding='utf8')
    print("".join(("接收内容：",accept_data)))
sk.close()
"""

# --------------------------------------------------------


# 导入 socket、sys 模块
import socket

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口好
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print (msg.decode('utf-8'))