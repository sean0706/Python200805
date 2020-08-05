# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:16:53 2020

@author: user
"""

d={}


print('歡迎進入系統')

while True:
    print('1.建立詞彙')
    print('2..列出所有詞彙')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗學習')
    print('6.離開系統')
    print('--------------')
    sel=int(input('請輸入選項'))
    
    if sel==1:
        while True:
            E=str(input('輸入英文單字(按0回選單):'))
            C=str(input('輸入中文解釋(按0回選單):'))
            d[E]=C
            if E=='0':
                break
        
    if sel==2:
        for k,v in d.items():
            print(k,v)
            
    if sel==3:
        while True:
            EC=str(input('輸入字彙(按0跳出):'))
            if EC=='0':
                break
            if EC in d:
                print(d[EC])
            else:
                print('不在字典中')
        
        