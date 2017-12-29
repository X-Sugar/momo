# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/27 0027

# Event对象存在于 threading 模块中。
# Event 实例管理着 一个内部标志，
# 通过 set() 方法来将该标志设置成 True，
# 使用 clear() 方法将该标志重置成 False
# wait() 方法会使当前线程阻塞直到标志被设置成 True，
# wait()可以选择给他一个参数，代表时间，代表阻塞多长时间，若不设置就是阻塞直到标志被设置为True
# isSet()方法  ：能判断标志位是否被设置为True

import threading,time


class Mon(threading.Thread):
    def run(self):
        Dinner.clear()  # 标志设置为False
        print('Cooking dinner')
        time.sleep(3)
        Dinner.set()    # 标志设置为True
        print(self.name,":dinner is OK!")

class Son(threading.Thread):
    def run(self):
        while True:
            if Dinner.isSet():  # 判断标志位是否被设置为True
                break
            else:
                print('dinner isnot ready!')
                Dinner.wait(1)
        print(self.name,':Eating Dinner')

def main():
    mon = Mon()
    son = Son()
    mon.name = 'Mon'
    son.name = 'Son'
    mon.start()
    son.start()

if __name__ == '__main__':
    Dinner = threading.Event()
    main()