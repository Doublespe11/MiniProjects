# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:16:34 2019

@author: Michał
"""

def solution(A, B):
    cards_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7 , "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14} #<- create a dict with cards and values 
    alec_wins = 0  # <- set alec results on 0
    for alec, bob in zip (A,B): #<-looping over two lists parallel
        if cards_values[alec] > cards_values[bob]: #<-checking who win the turn
            alec_wins+=1 #<- increment alec points
    return alec_wins 
    
    