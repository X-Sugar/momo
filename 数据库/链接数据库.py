# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/12/25 0025

# 链接数据库，安装：pip install pymysql
import pymysql
db = pymysql.connect('localhost','root','xia0suba0','mysql')
cursor = db.cursor()
cursor.execute('select user,host from mysql.user')
values = cursor.fetchall()
print(values)