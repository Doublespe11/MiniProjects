# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:06:28 2019

@author: Michał
"""
from collections import defaultdict
import datetime

def check_interesting(clock): #<- checking that this time is interesting 
    amount_of_numbers = defaultdict(int) #<-create default dictionary to count how many chars are in clock string
    for i in clock: #<-loop to add the values of chars
        amount_of_numbers[i]+=1 
    if len(amount_of_numbers)<=3:#<- checking that the amount of chars is less or equal 3 (3 because one of these char is ":", and this dosen't count)
        return True
    else: return False
    

def solution(S, T):
    hours_start, minutes_start, seconds_start = map(int,S.split(":")) 
    start = hours_start*3600 + minutes_start*60 + seconds_start #<- splitting and get total seconds of start time
    hours_end, minutes_end, seconds_end = map(int,T.split(":"))
    end = hours_end*3600 + minutes_end*60 + seconds_end #<- splitting and get total seconds of end time
    count=0
    while start<=end:  #<- looping over next seconds between start and end time
        if check_interesting(str(datetime.timedelta(seconds=start))): #<-using of check_interesting function as a argument use the datetime method which converts seconds into time type and then recast to the string
            count+=1 #<-counts how many interesting numbers is in this range
        start+=1 #<- increment time
    return count
