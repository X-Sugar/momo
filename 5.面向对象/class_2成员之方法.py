# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/4 0004

class Foo:
    def bar(self):  # 1.普通方法，保存在类中，由对象来调用，self = 对象
        print('bar')

    @staticmethod   # 2.静态方法  装饰器，保存在类中，由类直接调用
    def sta():
        print('123')

    @staticmethod
    def sta2(a,b):  # 传入参数
        print(a,b)

    @classmethod    # 3.类方法 保存在类中，由类直接调用，cls = 当前类
    def classmd(cls):   # cls是类名
        print('classmd')
        print(cls)

obj=Foo()
obj.bar()

Foo.sta()
Foo.sta2(1,2)

Foo.classmd()

# 应用场景：
# 如果对象中需要保存一些值，执行某些功能时，需要使用对象中的值 --》 普通发方法
# 不需要任何对象的值时，--》静态方法
