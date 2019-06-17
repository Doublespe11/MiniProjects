# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:06:54 2019

@author: Michał
"""

attack_position=[]
def splitting(board): #<--splitting board on 2D matrix
    for row in range(len(board)):
         board[row]=list(board[row])
    return board

def find_char(matrix,char): #<-- looking for position of jaffar's pawn
    jaffars_pawn = [(index, row.index(char)) for index, row in enumerate(matrix) if char in row]
    print(jaffars_pawn)
    return jaffars_pawn #<-- return as tupel in list, in case of many pawns but only one in signle row

def attack(jaff_position,board):
    y , x = jaff_position[0]
    if ((x+2<len(board)-1 or x-2 >= 0) and y-2>=0):
        
        if board[y-1][x+1] == "X" and not board[y-2][x+2] == "X":
            position =(y-2,x+2)
            if not (y,x) in attack_position:
                attack_position.append((y,x))
            attack([position],board)
            
              
        if board[y-1][x-1] == "X" and not board[y-2][x-2] == "X":
            position =(y-2,x-2)
            if not (y,x) in attack_position:
                attack_position.append((y,x))
            attack([position],board)
                   
    return len(attack_position)

   
    
def solution(B):
    jaffar_char="O"
    position=find_char(splitting(B),jaffar_char)
    return attack(position,splitting(B))

A =['.X...X.',
   '..X.X..',
   '.X..X..',
   '....X..',
   '...X...',
   '..X.X.X',
   '...O...']
solution(A)
