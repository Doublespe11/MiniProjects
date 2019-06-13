# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:19:58 2019

@author: Michał
"""

n=int(input("How many :  "))
x=0
y=1

for _ in range(n):
    print(x)
    x,y = y, x+y
