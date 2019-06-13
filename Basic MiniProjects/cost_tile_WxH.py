# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:11:02 2019

@author: Michał
"""
width, height = map(float,input("Enter height and width [m]:   ").split())
cost= float(input("Enter the cost of m2:   "))
print ("{:.{prec}f}".format(width*height*cost,prec=2))