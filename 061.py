from time import sleep
from os import system
a1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informa a razão da PA: '))
l = ['']
l[0] = a1
cont = 0
while cont != 9:
    cont +=1
    c = a1 + (r*cont)
    l.append(c)
print('A sequência é: {}'.format(l))
o =''
while o != 'N':
    o = input('Deseja acrescentar mais algum termo? S/N').upper().strip()
    if o == 'S':
        n = int(input('Informe a quantidade de termonos: '))
        c = 0
        for i in range(n):
            cont += 1
            c = a1 + (r*cont)
            l.append(c)
        system('clear')
        print(l)
        sleep(5)
    else:
        print('FIM')


