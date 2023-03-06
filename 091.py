from random import randint
from time import sleep
from operator import itemgetter
dict = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
for k, v in dict.items():
    print(f'O {k} tirou {v}.')
ord = list()
ord  = sorted(dict.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ord):
    print(f'Em {i+1}º lugar, {v[0]} tirou {v[1]}')