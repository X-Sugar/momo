# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/1 0001

# while True:
#     try:
#         x = int(input("Please enter a number:"))
#         break
#     except (ValueError,RuntimeError, TypeError, NameError):
#         print("Oops! That was no valid number. Try again!")

import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

raise NameError('HiThere')  #抛出异常