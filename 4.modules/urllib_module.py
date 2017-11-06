# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/11/3 0003

from urllib import request

response =request.urlopen(r'http://www.baidu.com')
page = response.read()