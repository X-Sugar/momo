# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/30 0030

# 操作系统
import os
#   1.
# print(os.name)  # 断现在正在实用的平台，Windows 返回 ‘nt'; Linux 返回’posix'
#   2.
# print(os.getcwd())  # 得到当前工作的目录。
#   3
# print(os.listdir()) # 显示所有目录下所有的文件和目录名
#   4
# os.remove() # 删除指定文件
# os.remove('xxx','abc') # 重命名
# os.removedirs() # 只能删除空目录
#   5
# os.mkdir('susu') # 生成一个
# os.rmdir('susu')  # 删除空目录
#   6
# os.mkdir()  # 创建目录，只能创建一层
# os.makedirs()   # 递归创建目录
#   7
# print(os.path.isfile('.//os_module.py')) # 判断指定对象是否为文件。是返回True,否则False
#   8
# print(os.path.isdir())  # 判断指定对象是否为目录。是True,否则False。
#   9
# print(os.path.exists()) # 判断指定对象是否存在，是True，否则False
#   10
# print(os.path.split(os.path.abspath(__file__))) # 返回路径的目录和文件名
#   11
# os.system("echo 'hello world'") # 执行shell命令
# 此处运行shell命令时，如果要调用python之前的变量，可以用如下方式：
# var=123
# os.environ['var']=str(var) # 注意此处[]内得是 “字符串”
# os.system('echo $var')
#   12
# os.chdir(r'c://Users')  # 改变目录到指定目录
# print(os.getcwd())
#   13
# print(os.path.getsize())    # 获得文件的大小，如果为目录，返回0
#   14
# print(os.path.abspath())    # 获取绝对路径
#   15
# print(os.path.join(r'c:\Users',r'os_module.py'))   # 连接目录和文件名
#   16
# print(os.path.basename('e:/momo/os_module.py'))  # 返回文件名
#   17
# print(os.path.dirname('e:\\momo\\os_module.py'))    # 返回文件路径
#   18
# import time
# a = os.stat('.\\生成器.py')  # 查看文件状态
# print(a.st_size)  # 文件大小
# print(time.ctime(a.st_ctime))
# print(os.path.getsize('.\\生成器.py'))
#   19
# print(os.sep)   # 路径分隔符，windows\ linux /
# print(os.pathsep) # 用于分割路径的分隔符    ;
#   20
# print(os.environ) # 显示环境变量
# print(os.pardir)