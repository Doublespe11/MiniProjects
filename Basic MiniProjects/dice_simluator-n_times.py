# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:56:24 2019

@author: Michał
Dice simulator
"""

import random

while True:
    try:
            wall, n = map(int,input("How many walls has a dice and how many dices?\nInput that one by one with space\n").split())
            [print(random.randint(1,wall)) for _ in range(n)]
    except:
            print("Wrong Value")
            
    cmd=input("Press any key to roll again or q to quit the program\n").lower()
    if cmd.startswith("q"):
        break