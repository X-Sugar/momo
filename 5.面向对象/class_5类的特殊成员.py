# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/5 0005


# 特殊成员：
# __init__   类()自动执行
# __call__  对象() 类()()自动执行
# __int__   int(对象)
# __str__   str()
# __del__   析构方法，对象被销毁()时，自动执行。（不常用）
# __dict__  讲对象中封装的所有内容通过字典形式返回

# ----------------------------------------------------------
# call

"""
class F:
    def __init__(self):
        print('123')

    def __call__(self, *args, **kwargs):
        print('call')

# obj= F()
# obj()

F()()

"""

# ------------------------------------------------------------
# __int__ __str__

"""

class Foo:
    def __init__(self):
        pass

    def __int__(self):
        return 1    #只能返回数字

    def __str__(self):
        return 'susu'

obj = Foo()

print(obj,type(obj))

# int,对象，自动执行对象的__int__方法，并将返回值赋值给int对象
r = int(obj)
print(r)

i = str(obj)
print(i)

"""

# ------------------------------------------------------------
# str

"""
class Foo:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def __str__(self):
        return '%s %s' % (self.name,self.age)

obj = Foo('susu',18)
print(obj)  # print(str(obj.name),str(obj.age))

"""

# -------------------------------------------------------
# 俩对象相加 __add__

"""
class Foo:

    def __init__(self,n,a):
        self.name = n
        self.age = a

    def __add__(self, other):

        # self = obj1('susu',19)
        # self = obj2('momo',20)

        # return 123    #返回什么输出什么
        # return 'susuuuuu'
        # return Foo('cici',20)   # <__main__.Foo object at 0x0000000001E88668> <class '__main__.Foo'>
        # return Foo(obj1.name,other.age)
        return self.age + other.age
obj1 = Foo('susu',19)
obj2 = Foo('momo',20)

# 两个对象相加时，自动执行第一个对象的__add__方法，并且将第二个对象参数传递进入
sums = obj1 + obj2
print(sums,type(sums))
"""

# -------------------------------------------------------
# __dict__  讲对象中封装的所有内容通过字典形式返回

"""

class Foo:
    '''
    当前类是干嘛的
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.gender = 'boy'

obj = Foo('susu',19)

d = obj.__dict__
print(d)

ret = Foo.__dict__
print(ret)

"""

# -------------------------------------------------------
"""
class Foo:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        return item+10

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)
        # self.age = key

li = Foo('susu',18)
r = li[9]   # 9 = item
print(r)

li[100] = 'susu' # 100 = key  susu = value

del li[999]
"""


"""
class Foo:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        if type(item) ==  slice:
            print('调用这希望内部做切片处理')
        else:
            print('调用这希望内部做索引处理')
    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)

li = Foo('susu',18)
li[123]
li[1:4:2]

"""

# ----------------------------------------------------
# __iter__

# """
class Foo:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __iter__(self):
        # return iter([11,22,33])
        return iter([self.name,self.age])   # 返回什么循环什么
li = Foo('susu',18)
# 如果类中有__iter__方法，对象 -》 可  迭代对象
# 对象.__iter__()的返回值：迭代器
# for循环，迭代器，next
# for循环，可迭代对象，对象.__iter()，迭代器，next
# 1.执行li对象的F类中的__iter__方法，并获取其返回值
# 2.循环上一部中返回的对象
for i in li:
    print(i)
# """