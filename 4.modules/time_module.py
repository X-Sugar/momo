# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/10/27 0027

import time

# print(help(time))

# print(time.time())  #1509023231.7808106 时间戳
# time.sleep(3)
# print(time.clock()) #计算cpu执行的时间
# print(time.gmtime())  #UTC时间,世界标准时间
# print(time.localtime()) #本地时间
# a = time.localtime()
# print(a.tm_year)

# print(help(time.strftime))
# print(time.strftime('%Y-%m-%d %H:%M:%S'))   # 字符串时间 2018-04-25 22:22:48
#
print(time.strptime('2017-10-26 21:34:51','%Y-%m-%d %H:%M:%S'))  # time.struct_time(tm_year=2017, tm_mon=10, tm_mday=26, tm_hour=21, tm_min=34, tm_sec=51, tm_wday=3, tm_yday=299, tm_isdst=-1)
# a=time.strptime ('2017-10-26 21:34:51','%Y-%m-%d %H:%M:%S')
# print(a.tm_year)
# print(a.tm_mon)
# #
# print(time.ctime()) #默认值是当前时间，固定格式
# print(time.ctime(1509023231.7808106))   #时间戳转换成时间
#
# print(time.mktime(time.localtime()))    #转换成时间戳.
#
# import datetime
# print(datetime.datetime.now())  #2017-10-26 22:00:24.462707


# from datetime import date
#
# now = date.today()
# print(now)
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
#
# import reprlib
#
# ret = reprlib.repr(set('supercalifragilisticexpialidocious'))
# print(ret)
#
# import pprint
#
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
#
# pprint.pprint(t,width=30)
#
# import logging
#
# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()
