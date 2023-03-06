from os import system
from statistics import mean
from math import trunc
nome = []
idade = []
sexo = []
nh =[]
im = []
ih = []
cont = 0
for i in range(4):
    print('Informe os dados da {}ª pessoa'.format(i+1))
    n = input('Informe o nome: ').upper().strip()
    nome.append(n)
    idade.append(int(input('Informe a idade:')))
    s = input('Informe o sexo M ou F: ').upper().strip()
    if s != 'M' and s != 'F':
        while s != 'M' and s != 'F':
            s = input('Informe o sexo M ou F: ').upper().strip()
    sexo.append(s)
    system('clear') or None
    if s == 'M':
        ih.append(idade[i])
        nh.append(nome[i])
    elif s == 'F':
        im.append(idade[i])
        if idade[i] < 20:
            cont += 1
mih = max(ih)
c = ih.index(mih)
system('clear') or None
print('=' * 40)
print('A média da idade do grupo é {} anos'.format(trunc(mean(idade))))
print('O homem mais velho é {} com {} anos'.format(nh[c], max(ih)))
print('{} mulheres tem menos de 20 anos'.format(cont))
print('=' * 40)
