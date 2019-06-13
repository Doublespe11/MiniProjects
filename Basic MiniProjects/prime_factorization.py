# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:33:22 2019

@author: Michał
"""

prime_numbers = [2,3,5,7,11,13,17,19,23,29,31]
number= int(input("Enter the number:    "))
primes_factors=list()
temp=0
for prime_number in prime_numbers:
    while number%prime_number==0:
        number=number/prime_number
        primes_factors.append(prime_number)
        temp=prime_number
    if temp**2<prime_number and temp!=0:
        break
if number!=1:
    primes_factors.append(int(number))
print (primes_factors)