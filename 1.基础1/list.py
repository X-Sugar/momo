# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/9/5 0005

a = ['susu','momo','lili','lucy','Cici']

a.pop()
print(a)

# print(a)

# print(a[1:3])   #切片
# print(a[1:])    #取到最后
# print(a[1:-1])  #取倒数第二个值
# print(a[1:-1:2]) #隔一个取值
# print(a[3::-1]) #反方向打印
# print(a[3::-2]) #反方向隔一个取值
# print(a[-2])
# print(a[-1::-2])
#增加
# a.append('Kiki')    #在最后位置插入
# a.insert(1,'Kiki')  #指定位置插入

#修改
# a[1] = 'Sugar'    #替换单个值
# a[1:3] = ['a','b']    #范围替换值
# print(a)

#删除
# a.pop(1)    #通过索引删除
# a.remove('susu')    #删除列表元素,只能删一个元素
# del a[0]    #删除一个值
# del  a  #直接删除a这个变量
# print(a)

#index
# print(a.index('lucy'))  #根据内容查找位置

# a.reverse()
# print(a)

# b = [2,3,4,6,8,12]
# b.sort()    #升序
# print(b)
# b.reverse() #降序
# print(b)

# print(len(b))