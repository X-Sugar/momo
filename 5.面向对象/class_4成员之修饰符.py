# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/5 0005

# 成员修饰符
# 共有成员
# 私有成员 __字段名
#          无法直接访问，只能间接访问
"""
class Foo:
    def __init__(self,name,age):
        self.name = name
        # self.age = age
        self.__age = age    #私有字段,外部无法直接访问

    def show(self):
        return self.__age

obj = Foo('susu',18)
print(obj.name)
# print(obj.age)

print(obj.show())

"""

# -----------------------------------------------
"""
class Foo:
    __v = '数据连接'

    def __init__(self):
        pass

    def show(self):
        return Foo.__v

    @staticmethod
    def stat():
        return Foo.__v

obj=Foo()
print(obj.show())

print(Foo.stat())

"""

# --------------------------------------------------
"""
class Foo:
    def f1(self):
        return 数据连接

    def __f2(self):
        return 456

    def f3(self):
        return self.__f2()
obj = Foo()
print(obj.f1())

print(obj.f3())

"""

# --------------------------------------------------

class F:
    def __init__(self):
        self.ge = 'boy'
        self.__ge = 'girl'

    @property       # 子类不能继承，只能定义共有的
    def gen(self):
        return self.__ge

class S(F):
    def __init__(self,name):
        self.name = name
        self.__age = 18
        F.__init__(self)
        # super(S,self).__init__()

    def show(self):
        print(self.name)
        print(self.__age)
        print(self.ge)
        print(self.gen)

obj = S('susu')
obj.show()