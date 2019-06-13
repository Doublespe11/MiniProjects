# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:06:54 2019

@author: Michał
"""

def splitting(board): #<--splitting board on 2D matrix
    for row in range(len(board)):
         board[row]=list(board[row])
    return board

def find_char(matrix,char): #<-- looking for position of jaffar's pawn
    jaffars_pawn = [(index, row.index(char)) for index, row in enumerate(matrix) if char in row]
    return jaffars_pawn #<-- return as tupel in list, in case of many pawns but only one in signle row
    
def attack(jaffar_position,board): #<- main function which ger points when Jaffar's pawn are able to beat Aladdin pawn
    board=splitting(board)
    len_board=len(board)
    y,x = jaffar_position[0]
    points=0
    play=True
    while play: #<-loop until next beat dosen't occur
        
        if ((x+2<len_board or x-2>0) and y-2>0): #<- chceking that attack jaffar's pawn dosen't move to the outside of board
            
            if (board[x-1][y-1] == "X" and not board[x-2][y-2] == "X"): #<- checking if jaffar's pawn can attack up-left direction 
                points+=1 #<- counting points
                x ,y = x - 2, y - 2 #<- move jaffar's pawn
            
            elif (board[x+1][y-1] == "X" and not board[x+2][y-2] == "X"):#<- checking if jaffar's pawn can attack up-right direction
                points+=1
                x ,y = x + 2, y - 2
                
            else: play=False #<- when Jaffar's pawn can't attack next Aladdin's pawn
            
        else: play=False
        
    return points
    
    
def solution(B):
    jaffar_char="O"
    return attack(find_char(splitting(B),jaffar_char),B)