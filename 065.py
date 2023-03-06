from statistics import mean
from os import system
o = ''
l = []
while o != 'N':
    n = int(input('Degite um número: '))
    l.append(n)
    o = input('Continuar digitando? S/N:').upper().strip()
    system('clear')
print('A média é {}'.format(mean(l)))
print('O maior número foi {}'.format(max(l)))
print('O menor número foi {}'.format(min(l)))