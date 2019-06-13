# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:28:32 2019

@author: Michał
"""
import math
cmd, number = input().split()
if cmd=="bin":
    number=int(number)
    positions=math.ceil(number**(1/2))
    result=list()
    for i in range(positions-1,-1,-1):
        if number>=2**i:
            print(i, 2**i)
            result.append(1)
            number=number-(2**i)
        else: result.append(0)
    print(result)
if cmd=="dec":
    result=0
    for i,val in enumerate(number[::-1]):
        if int(val):
            result=result+(2**i)
    print(result)