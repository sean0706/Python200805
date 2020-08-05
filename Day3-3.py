# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:39:50 2020

@author: AE401
"""

score=[]

'''function avg'''
def sean(h):
    total=0  
    for d in score:
        total=total+d
    return total/n

'''function high'''
def high(h):
    highest=0
    for  c  in score:
        if c>highest:
            highest=c
    return highest

'''main function'''
n=int(input('how many people'))
for e in range(n):
    s=int(input('enter score'))
    score.append(s)
    
q=sean(score)
print('The average is',q)
w=high(score)
print('highest:' ,w)

