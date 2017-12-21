# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/19 0019

"""
# 进行 一次通信

import socket

sk = socket.socket()    # 创建socket对象

sk.bind(("127.0.0.1",8888)) # 绑定端口,“127.0.0.1”代表本机地址，8888为设置链接的端口地址

sk.listen(5)    # 设置监听，最多可有5个客户端进行排队

conn,addr = sk.accept()     # 阻塞状态，被动等待客户端的连接
print(conn)     # conn可以理解客户端的socket对象
print(addr)     # addr为客户端的端口地址

accept_data = conn.recv(1024)       # conn.recv()接收客户端的内容，接收到的是bytes类型数据，
acccept_data2 = str(accept_data,encoding='utf8')        # str(data,encoding="utf8")用“utf8”进行解码

print("".join(("接收内容：",acccept_data2,"      客户端口：",str(addr[1]))))

send_data = input("输入发送内容：")

conn.sendall(bytes(send_data,encoding='utf8'))      # 发送内容必须为bytes类型数据，bytes(data, encoding="utf8")用“utf8”格式进行编码
conn.close()
"""
# --------------------------------------------------------

"""
# 一直通讯

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 9008))
sk.listen(5)
while True:
    conn, addr = sk.accept()
    while True:
        accept_data = str(conn.recv(1024),encoding="utf8")
        print("".join(("接收内容：", accept_data, "     客户端口：", str(addr[1]))))
        if accept_data == "byebye":  # 如果接收到“byebye”则跳出循环结束和第一个客户端的通讯，开始与下一个客户端进行通讯
            break
        send_data = input("输入发送内容：")
        conn.sendall(bytes(send_data, encoding="utf8"))
    conn.close()  # 跳出循环时结束通讯
"""

# --------------------------------------------------------


# import socketserver     # 导入socketserver模块
#
# # 创建一个类，继承自socketserver模块下的BaseRequestHandler类
# class Myserver(socketserver.BaseRequestHandler):
#     # 要想实现并发效果必须重写父类中的handler方法，在此方法中实现服务端的逻辑代码（不用再写连接准备，包括bind()、listen()、accept()方法）
#     def handle(self):
#         while 1:
#             conn = self.request
#             addr = self.client_address
#             # 上面两行代码，等于 conn,addr = socket.accept()，只不过在socketserver模块中已经替我们包装好了，还替我们包装了包括bind()、listen()、accept()方法
#             while 1:
#                 accept_data = str(conn.recv(1024),encoding='utf8')
#                 print(accept_data)
#                 if accept_data == 'byebye':
#                     break
#                 send_data = bytes(input(">>>"),encoding='utf8')
#                 conn.sendall(send_data)
#             conn.close()
#
# if __name__ == '__main__':
#     # 传入 端口地址 和 我们新建的继承自socketserver模块下的BaseRequestHandler类  实例化对象
#     server = socketserver.ThreadingTCPServer(("127.0.0.1",8888),Myserver)
#     # 通过调用对象的serve_forever()方法来激活服务端
#     server.serve_forever()

# --------------------------------------------------------

# 导入 socket、sys 模块
import socket

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msg = '欢迎学习python！' + "\r\n"
    # clientsocket.send(msg.encode('utf-8'))
    clientsocket.sendall(bytes(msg,encoding='utf8'))
    clientsocket.close()
