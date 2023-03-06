import random
from time import sleep
from os import system
numeros = list(range(1,11))


def limpatela():
    system('clear') or None

def sorteia(a):
    b = list()
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        m = random.choice(a)
        b.append(m)
        print(f'{m}', end=' ', flush= True)
        sleep(1)
    print('PRONTO!')
    return b

def soma_par(a):
    soma = 0
    print('Somando os valores pares ', end='')
    for i in a:        
        if i % 2 == 0:
            print(i, end=", ")
            soma += i
    print(f' temos {soma}.')

c = sorteia(numeros)
soma_par(c)