# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 08:10:42 2022

@author: damia
"""

n = int(input('INFORME UM NÚMERO INTEIRO: '))
for t in range(1,11):
    print('{} x {} = {} '.format(t,n,t*n))
    

j = int(input('Digite um número inteiro: '))
print(' {} x 1 = {}\n'.format(j,j*1),'{} x 2 = {}\n'.format(j,j*2),'{} x 3 = {}\n'.format(j,j*3),end=' ')
print('{} x 4 = {}\n'.format(j,j*4),'{} x 5 = {}\n'.format(j,j*5),'{} x 6 = {}\n'.format(j,j*6),end=' ')
print('{} x 7 = {}\n'.format(j,j*7),'{} x 8 = {}\n'.format(j,j*8),'{} x 9 = {}\n'.format(j,j*9),end=' ')
print('{} x 10 = {}\n'.format(j,j*10))    

