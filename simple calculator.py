# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:07:45 2024

@author: ADMIN
"""
#1/6/25
#simple calculator
def cal(a,b,opr):
    def sum():
        s=a+b
        return s
    def diff():
        d=a-b
        return d
    def prod():
        p=a*b
        print(p)
    def div():
        q=a/b
        print(q)
    if opr=='+':
        s=sum()
        print(s)
    if opr=='-':
        d=diff()
        print(d)
    if opr=='*':
        p=prod()
        print(p)
    if opr=='/':
        d=div()
        print(d)
#main
e=int(input('enter value1:'))
f=int(input('enter value2:'))
g=(input('enter value3:'))
d=cal(e,f,g)
print(d)


