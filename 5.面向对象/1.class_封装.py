# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/30 0030

# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板
# 根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
# 面向对象三大特性之一：封装
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
# lisa = Student('Lisa',99)
# print(lisa.name,lisa.get_grade())

# bart = Student('Bart',55)
# print(bart.name,bart.get_grade())

# ------------------------------------------------------
'''
class Bar(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def foo(self):
        print('456')
z = Bar('alex',84)
print('我的名字是%s,年龄是%s' %(z.name,z.age))
'''
-----------------------------------------------------
class Person:
    def __init__(self,name,age):
        """
        构造方法，构造方法特性，类名()自动执行构造方法
        :param name: 
        :param age: 
        """
        self.n=name
        self.a=age
    def show(self):
        print('%s-%s' % (self.n,self.a))

susu = Person('Susu',18)
susu.show()
momo = Person('Momo',20)
momo.show()