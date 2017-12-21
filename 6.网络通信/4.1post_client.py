# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/21 0021

import os

a = os.path.getsize('2.1.server.py')
print(a)

b = os .stat('2.1.server.py').st_size
print(b)