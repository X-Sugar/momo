# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/9/21 0021

# susu = [1,2,3,4,54,6,67,32,2]
#
# a = set(susu)
# a.add('Susu')
#
# a.update('aa','bb',[99,'momo'],'28')
# print(a)
#
# a.remove('Susu')
# print(a)
#

# a.pop()
# print(a)

# a = set([1,2,3,4,5])
# b = set([4,5,6,7,8])
#
# print(a & b)    #合集
# print(a | b)    #并集
# print(a - b)    #差集
# print(b - a)    #差集
# print(a ^ b)    #对称差集
#
# print(a.issuperset(a))  #父集
# print(b.issubset(a))    #子集

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

a=[x for x in basket if x != 'pear']
print(a)





