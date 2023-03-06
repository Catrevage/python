from os import system
from time import sleep
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
op = 0
m = []
while op != 5:
    print("""Escolha uma operação!
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR""")
    op = int(input('Escolha:'))
    if op == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
        sleep(5)
    elif op == 2:
        print('{} - {} = {}'.format(n1,n2,n1-n2))
        sleep(5)
    elif op == 3:
        m.append(n1)
        m.append(n2)
        print('O maior é {}'.format(max(m)))
        sleep(5)
    elif op ==4:
        system('clear')
        n1 = float(input('Informe o primeiro número: '))
        n2 = float(input('Informe o segundo número: '))
    system('clear')
print('FIM')