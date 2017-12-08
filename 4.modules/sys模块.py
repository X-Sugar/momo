# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/30 0030

#python解释器交互
import sys

#   1.
# print(sys.argv) #命令行参数list 第一个元素是程序本身路径
# print('The name of this program is: %s' % (sys.argv))
#   2.
# sys.exit()  #退出程序，正常退出时exit(0)
#   3.
# print(sys.version)  #获取python解释程序的版本信息
#   4.
# print(sys.platform)
# 跨平台执行命令
import os
if sys.platform=='win32':
    os.system('dir')
else:
    os.system('ls')


#   5.
# print(sys.path)   #path是一个目录列表，供Python从中查找第三方扩展模块
#   6
# print(sys.builtin_module_names) # 返回一个列表，包含内建模块的名字
