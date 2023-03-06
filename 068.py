from random import randint
from os import system
cont = 0
while True:
    p = 0
    while True:
        p = int(input('Escoha 1 para ÍMPAR ou 2 para PAR: '))
        if p == 1 or p ==2:
            break
    system('clear') or None
    n = int(input('Informe um número um de 0 a 10: '))
    if p == 1:
        c = 2
    else:
        c = 1
    nc = randint(0,10)
    r = (n+nc) % 2
    if (p == 1 and r !=0) or (p == 2 and r == 0):
        print(f'O computador jogou {nc}.')
        print('Parabéns, Você ganhou!!!')
        cont += 1
    else:
        print(f'O computador jogou {nc}.')
        print('Você perdeu!')
        print(f'Você ganhou {cont} vezes.')
        break