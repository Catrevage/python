from random import randint
a = int(input('Informe quantos jogos deseja fazer: '))
jogos = list()
l = list()
for i in range(a):
    for s in range(6):
        l.append(randint(1, 60))
    jogos.append(l[:])
    l.clear()
print(f'{"RELAÇÃO DE JOGOS":^30}')
print('-='*15, end='\n')
for i in jogos:
    print(f'{sorted(i)}\n')
print('-='*15)