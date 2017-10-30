# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/30 0030

#python解释器交互
import sys

# print(sys.argv) #命令行参数list 第一个元素是程序本身路径
# sys.exit()  #推出程序，正常退出时exit(0)

# print(sys.version)  #获取python解释程序的版本信息

print(sys.platform)
#跨平台执行命令
import os
if sys.platform=='win32':
    os.system('dir')
elif:
    os.system('ls')
