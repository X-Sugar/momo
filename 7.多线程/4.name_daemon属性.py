# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/27 0027

# name属性表示线程的线程名 默认是 Thread-x  x是序号，由1开始，第一个创建的线程名字就是 Thread-1

# import threading,time
#
# class mythread(threading.Thread):
#     def run(self):
#         pass
#
# if __name__ == '__main__':
#     ta = mythread()  # 实例化线程
#     ta.name = 'thread-ta'
#     tb = mythread()
#     tb.start()
#     ta.start()
#
#     print(ta.name)  # 打印 thread-ta
#     print(tb.name)  # 打印 Thread-2

# daemon属性用来设置线程是否随主线程退出而退出
# 当 daemon = False 时，线程不会随主线程退出而退出（默认时，就是 daemon = False）
# 当 daemon = True 时，当主线程结束，其他子线程就会被强制结束

import threading,time

class mythread(threading.Thread):
    def run(self):
        time.sleep(2)
        print('my thread over')

def main():
    ta = mythread()
    ta.daemon = True
    ta.start()
    print('main thread over')

if __name__ == '__main__':
    main()
