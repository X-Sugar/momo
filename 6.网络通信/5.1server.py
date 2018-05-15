# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/25 0025

# 并发聊天

import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('Server startting...')
        while True:
            conn = self.request
            addr = self.client_address
            print(addr)
            while True:
                client_data = str(conn.recv(1024),'utf8')
                print(client_data)
                print('waitting...')

                server_response=input('Please input str:')
                conn.sendall(bytes(server_response,'utf8'))
            conn.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8091),MyServer)
    server.serve_forever()