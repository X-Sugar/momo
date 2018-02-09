#coding:utf8
# _author: Administrator
# Date: 2018/2/7 0007

'''实现动态模块导入'''

# 普通方法
# mudule = 'src.user_info'
# func_name = 'add'
#
# import importlib
# m = importlib.import_module(mudule)
# func = getattr(m,func_name)
# func()

# --------------------------------------------

# 标准方法
import importlib


def dynamic_import(module):
    return importlib.import_module(module)

if __name__ == '__main__':
    module = dynamic_import('src.user_info')
    # func = getattr(module,'add')
    # func()
    module.add()
