# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:46:34 2019

@author: Michał
GUESS the number
"""

import random
while True:
    
    print("You have 5 chances to guess the random number")
    x=random.randint(1,101)
    count=1
    while count<=5:
        a=int(input())
        if a==x:
            print("you WIN",count)
            break
        else:
            if a>x:
                print("too high")
            else:
                print("too low")
            count+=1
    print("you loose!")
    cmd=input("Press any key to play again or q to quit the program\n").lower()
    if cmd.startswith("q"):
        break      