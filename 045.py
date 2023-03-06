from random import randint
from time import sleep
u = input(' Escolha PEDRA, PAPEL OU TESOURA: ').upper()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
v = u.strip()
list = ['PEDRA', 'PAPEL', 'TESOURA']
if  list.count(v) == 0:
    print('Opção não encontrada')
sort = randint(0, 2)
print('O computador escolheu {} '.format(list[sort]))
print('-=' * 12)
if v == list[sort]:
    print('EMPATE')
elif v == 'PEDRA' and sort == 1:
    print('Papel embrulha pedra, você perdu!')
elif v == 'PAPEL' and sort == 2:
    print('Você perdeu!')
elif v =='TESOURA' and sort == 0:
    print('Você perdeu!')
else:
    print('Você ganhou')
print('-=' * 12)