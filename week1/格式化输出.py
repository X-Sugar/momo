# coding=utf-8
name = input("Input your name:")
age = int(input("Input your age:"))
job = input("Input your job:")
salary = input("Input your salary:")

if salary.isdigit():    #长的像不像数字，比如200d、200
    salary = int(salary)    #转成数字格式，重新赋值
else:
    exit("Must input digit!")  #退出程序并打印提示

msg = '''
--------------info of sugar--------------
Name: %s
Age:%d
Job:%s
Salary:%f
------------------end---------------------
''' % (name,age,job,salary)
print(msg)