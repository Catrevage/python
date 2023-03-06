from time import sleep
from os import system

cedulas = [100, 50, 20,10, 5, 2, 1]

def conta_cedulas(a,b):
    cont = a
    l = b
    c = []
    for i in range(len(l)):
        div  = cont // l[i]
        c.append(div)
        cont += -div*l[i]
    return(c)
def mostra_quantidade(b,c):
    l = c
    for i in range(len(b)):
        if b[i] != 0:
            print(f'{b[i]} cédula(s) de R${l[i]}')

system('clear') or None
while True:
    while True:
        print('===BANCO LISEU S/A===')
        print('INFORME UMA OPÇÃO')
        print('[1] SAQUE')
        print('[2] SAIR')
        print('=' * 20)
        o = int(input('Opção: '))
        system('clear') or None
        if o == 1 or o == 2:
            system("clear") or None
            break
    if o == 2:
        print('OBRIGADO!')
        break
    elif o == 1:
        while True:
            while True:
                print('===BANCO LISEU S/A===\n')
                print('INFORME O VALOR \n')
                print(f'*Cédulas disponíveis:\nR${cedulas}')
                print('=' * 20)
                v = int(input('VALOR R$:'))
                system('clear') or None
                if v % 2 == 0:
                    break
            break
    print(f'SAQUE DE R${v} AUTORIZADO. CONTANDO CÉDULAS...')
    p = conta_cedulas(v,cedulas)
    mostra_quantidade(p,cedulas)
    sleep(3)
    break
if o != 2:
    print('RETIRE O DINHEIRO!')
    sleep(3)
    print('NÃO ESQUEÇA DE RETIRAR O CARTÃO ;)')
    sleep(3)
    print('=====OBRIGADO!======')
