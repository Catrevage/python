from math import trunc
from os import system
l_dic= list()
dic = {}
f = m = c = 0
while True:
    system('clear') or None
    dic['nome'] = input('Nome: ').upper().strip()
    dic['sexo'] = input('Sexo(M/F):').upper().strip()
    dic['idade'] = int(input('Idade: '))
    l_dic.append(dic.copy())
    o = input('Continuar cadastrando?(S/N): ').upper().strip()
    if o == 'N':
        system('clear') or None
        break

print('-='*25)

print(f'Foram cadastradas {len(l_dic)} pessoas.')

for i in l_dic:
    c += i['idade']

media_idades = trunc(c/len(l_dic))

print('-='*25)

print(f'A média de idades é {media_idades} anos.')

print('-='*25)

print('As mulheres cadastradas foram:')
for i in l_dic:
    if i['sexo'] == 'F':
        print(i['nome'])

print('-='*25)

print('Todos que estão acima da média de didades são:')
for i in l_dic:
    if i['idade'] > media_idades:
        print(i['nome'])
