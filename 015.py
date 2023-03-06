# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 09:53:49 2022

@author: damia
"""

k =float(input('Informe a quantidade de Km rodados: '))
d = int(input('Informe a quantidade de dias de locação: '))
print("O valor do aluguel é: R${:.2f}".format((k * 0.15) + (d * 60)))
