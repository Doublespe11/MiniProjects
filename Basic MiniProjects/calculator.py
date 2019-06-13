# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:50:27 2019

@author: Michał
"""
while True:   
    evaluation = input()
    if evaluation.startswith("q"):
        break
    if "^" in evaluation:
        evaluation=evaluation.replace("^","**")
    print(eval(evaluation))