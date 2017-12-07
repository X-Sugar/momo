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


try:
    x=int(input("input a number:"))
except Exception as e:  # Exception 所有错误
    print(e)
    print('xxx')


try:
    x=int(input('a number:'))
except IndexError as e:
    print('IndexError:',e)
except ValueError as e:
    print('ValueError',e)
else:       # 不出错，执行else
    print('else')
finally:        # 不管出不出错，最后都执行
    print('......')

# raise NameError('HiThere')  #抛出异常
