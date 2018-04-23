def login():
    print('这是登陆功能！')


def select():
    print('这是查询功能！')


def update():
    print('这是更新功能！')


def delete():
    print('这是删除功能！')


def exit():
    print('这是退出功能！')


if __name__ == '__main__':
    msg='''
        1.登陆
        2.查询
        3.更新
        4.删除
        5.退出
    '''
    msg_dic={
        '1':login,
        '2':select,
        '3':update,
        '4':delete,
        '5':exit
    }

    while True:
        print(msg)
        choice = input('请输入你的选项：').strip()
        if not choice:continue
        if choice == '5':break
        if choice in msg_dic:
            res=msg_dic[choice]
            res()
        else:
            print('error')
