# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:24:13 2019

@author: Michał
"""

import math
while True:
    
    try:
        pi_digits=int(input("Please Enter number the digit of PI:   "))
    except:
        print("WRONG VALUE")
        continue
    
    print("{:.{prec}f}".format(math.pi, prec=pi_digits))
        
        