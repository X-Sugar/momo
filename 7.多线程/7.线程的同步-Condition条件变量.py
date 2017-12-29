# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/27 0027

import threading
import time


class Server(threading.Thread):
    def run(self):
        global x
        while True:
            con.acquire()   # 上锁
            while x > 0:
                con.wait()  # 当前线程阻塞直到标志被设置成 True
            x += 1
            time.sleep(1)
            print(self.name, ':I make %d cake!' % (x))
            con.notifyAll() # 等待线程醒来
            con.release()   # 解锁


class Client(threading.Thread):
    def run(self):
        global x
        con.acquire()   # 上锁
        while x == 0:
            con.wait()  # 当前线程阻塞直到标志被设置成 True
        x -= 1
        print(self.name, 'I bought a cake! the rest is %d cake' % (x))
        con.notifyAll()
        con.release()   # 解锁


def main():
    ser = Server()
    ser.name = 'Cake Server'
    client = []
    for i in range(3):
        client.append(Client())
    ser.start()
    for c in client:
        c.start()


if __name__ == '__main__':
    x = 0
    con = threading.Condition()
    main()