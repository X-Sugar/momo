# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/14 0014

# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# obj = Foo()     # obj对象，obj也成为Foo类的实例 （实例化）

# 单例，用于使用同一份实例（对象）

class Foo:

    __v = None
    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v

obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)
obj3 = Foo.get_instance()
print(obj3)