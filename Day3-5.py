# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:30:51 2020

@author: user
"""

while True:
    print('---------------------------------------')
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.離開')
    sel=int(input("請輸入選項"))
    print('------------------')
    
    if sel==1:
        add1=int(input('請輸入數字:'))
        add2=int(input('請輸入數字:'))
        print(add1,'+',add2,'=',add1+add2)
        
    elif sel==2:
        sub1=int(input('請輸入數字:'))
        sub2=int(input('請輸入數字:'))
        print(sub1,'-',sub2,'=',sub1-sub2)
        
    elif sel==3:
        mul1=int(input('請輸入數字:'))
        mul2=int(input('請輸入數字:'))
        print(mul1,'x',mul2,'=',mul1*mul2)
        
        
    elif sel==4:
        div1=int(input('請輸入數字:'))
        div2=int(input('請輸入數字:'))
        print(div1,'/',div2,'=',div1/div2)
    
    elif sel==5:
        print('------系統停止------')
        break
    
    else:
        print('請輸入"1~5"')
        
        
        
        
        
        
        

    