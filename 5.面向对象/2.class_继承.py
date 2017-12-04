# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/30 0030
'''
class Father:   # 父类（基类）
    def name1(self):
        print('name1')
    def name2(self):
        print('name2')
    def name3(self):
        print('name3')
    def name4(self):
        print('name4')
    def name5(self):
        print('name5')

class Son(Father):  # 子类（派生类）     继承父类
    def name6(self):
        print('name6')
    def name2(self):
        print('name22222')
        # super(Son,self).name2()     # 方法一：执行父类中的name2方法,
        Father.name2(self)  # 方法二：self需要自己传
    def name1(self):
        print('xxxxx')  #重写父类方法

a = Son()
a.name1()   # 优先从子类查找
a.name2()
'''
# ------------------------------------------------------
# 多继承
# 1.左侧优先
# 2.一条道走道黑
# 3.同一个根时，根最后执行
'''
class F0:
    def a(self):
        print('F0.a')
class F_1(F0):
    def a1(self):
        print('F_1.a')
class F1(F_1):
    def a1(self):
        print('F1.a')
class F2:
    def a(self):
        print('F2.a')
class S(F1,F2):
    pass
obj=S()
obj.a()
'''
# -----------------------------------------------
'''
class BaseRequest:
    pass

class RequestHandler(BaseRequest):
    def server_forever(self):
        print('RequestHandle.server_forever')
        self.process_request()  #返回重新从Minx查找

    def process_request(self):
        print('RequestHandler.process_request')

class Minx:
    def process_request(self):
        print('Minx.process_request')

class Son(Minx,RequestHandler):
    pass

obj=Son()
obj.server_forever()
'''
# ------------------------------------------------4
import socketserver

obj = socketserver.ThreadingTCPServer()
obj.serve_forever()