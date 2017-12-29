# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/27 0027

# 这个方法用于判断线程是否运行。
# 1.当线程未调用 start()来开启时，isAlive()会返回False
# 2.但线程已经执行后并结束时，isAlive()也会返回False

import threading
import time


class mythread(threading.Thread):
    def run(self):
        time.sleep(2)


if __name__ == '__main__':
    ta = mythread()  # 实例化线程
    print(ta.isAlive())  # 打印False，因为未执行 start()来使ta线程运行
    ta.start()
    print(ta.isAlive())  # 打印Ture，因为ta线程运行了
    time.sleep(3)
    print(ta.isAlive())  # 打印False，因为ta线程已经结束了