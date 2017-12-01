# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/30 0030

class Father:   # 父类 基类
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

class Son(Father):  # 子类 派生类     继承父类
    def name6(self):
        print('name6')
    def name2(self):
        print('name22222')
        # super(Son,self).name2()     #执行父类中的name2方法,
        Father.name2(self)  # self需要自己传
    def name1(self):
        print('xxxxx')

a = Son()
a.name1()   # 优先从子类查找
a.name2()