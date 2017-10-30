# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/30 0030

import os

# print(os.getcwd())  #显示当前路径

# os.chdir(r'c:\Users')
# print(os.getcwd())

# print(os.curdir)
# print(os.pardir)

# os.chdir()
# os.makedirs('abc\\susu') #生成多层文件夹 在当前目录生成abc/susu目录
# os.removedirs('abc\\susu')  #只能删除空目录

# os.mkdir('susu') #生成一个
# os.rmdir('susu')  #删除空目录

# print(os.listdir(r'C:\Users'))

# os.remove('xx') #删除文件,不可以删除文件夹

# os.remove('xxx','abc') #重命名

# import time
# a = os.stat('.\\生成器.py')
# print(a.st_size)
# print(time.ctime(a.st_ctime))

# print(os.sep) #路径分隔符，windows\\ linux /

# print(os.pathsep) #用于分割路径的分隔符

# print(os.system('dir'))

# print(os.environ) #显示环境变量

# print(os.path.abspath('./os模块.py')) #获取绝对路径

# print(os.path.split('E:\momo\week3\os模块.py'))   #('E:\\momo\\week3', 'os模块.py')

# print(os.path.dirname('os模块.py')) #返回文件路径

# print(os.path.dirname(__file__))

# print(os.path.exists('.//生成器.py')) #判断文件是否存在，返回True
# print(os.path.isdir(r'c://')) #判断对象是否为目录，返回 True False

# os.system("cd /usr/local") #执行shell命令     重要！！！

#此处运行shell命令时，如果要调用python之前的变量，可以用如下方式：
# var=123
# os.environ['var']=str(var) //注意此处[]内得是 “字符串”
# os.system('echo $var')

# print(os.path.getsize(r'.//时间模块.py')) #获取文件大小，如果为目录，返回0

