# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/14 0014

import calculate
#
# print(calculate.a)
#
# from calculate import add
# print(add(1,5))

import os
import sys

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))