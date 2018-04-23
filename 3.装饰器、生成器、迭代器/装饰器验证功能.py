#coding:utf8
# _author: Administrator
# Date: 2018/4/23 0023
user_list=[
    {'name':'susu','password':'123'},
    {'name':'momo','password':'123'},
    {'name':'sb','password':'123'},
]
current_dic={'username':None,'login':False}


def auth_func(func):
    def wrapper(*args,**kwargs):
        if current_dic['username'] and current_dic['login']:
            res = func(*args,**kwargs)
            return res
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        for user_dic in user_list:
            if username == user_dic['name'] and password == user_dic['password']:
                current_dic['username'] = username
                current_dic['login'] = True
                res = func(*args,**kwargs)
                return res
        else:
            print('用户名或者密码错误！')

    return wrapper

@auth_func
def index():
    print('欢迎来到苏苏的迷人水果店')

@auth_func
def home(name):
    print('欢迎回家%s' % name)

@auth_func
def shopping_car(name):
    print('%s的购物车里面有[%s、%s、%s]' % (name,'苹果','菠萝','香蕉'))

print('before-->',current_dic)
index()
print('after-->',current_dic)
home('sb')
shopping_car('susu')