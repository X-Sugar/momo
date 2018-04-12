# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/9/6 0006

a = (1,) # 单个元素加个逗号
print(a)

b = (2,3,4,5,6)
print(b[3])         # 切片方式拿出值

# 获取指定元素在元组中出现的次数
print(b.count(2))

# 获取索引位置
print(b.index(5))