# -*- coding=utf-8 -*-
# _author: Administrator
# Date: 2017/9/14 0014

menu = {
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'XX银行':{},
                'CCTV':{},
            },
            '望京':{
                '陌陌':{},
                '奔驰':{},
                '360':{},
            },
            '三里屯':{
                '优衣库':{},
                '大使馆':{},
            },
        },
        '昌平':{
            '沙盒':{},
            '天书元':{},
            '西山居':{},
        },
        '海淀':{
            '谷歌':{},
            '网易': {},
            'Sohu': {},
        },
    },
    '上海':{},
    '山东':{},
}
back_menu = menu
fu_menu = []
while True:
    for key in menu:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:continue    #如果为空继续输入
    if choice in menu:
        # back_menu = menu        #在改变之前赋值，为父层
        fu_menu.append(menu)
        menu = menu[choice]     #改变menu值，变为子层
    elif choice == "b":
        # menu = back_menu        #把子层改为父层
        if fu_menu:
            menu = fu_menu.pop()    #删除最后一个值
    else:
        print("无此项")
