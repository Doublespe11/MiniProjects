# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:46:32 2019

@author: Michał
"""

import math

try:
    e_digits=int(input("Enter number of digits in e number:"))
    assert e_digits>=0
except:
    print("WRONG VALUE")
print("{:.{prec}f}".format(math.e, prec=e_digits))
    