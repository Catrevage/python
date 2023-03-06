n1 = int(input('Informe um número inteiro:' ))
n2 = int(input('Informe outro número inteiro' ))
if n1 == n2:
    print('Os dois números são iguais')
elif n1 > n2:
    print('{} é maior que {}'.format(n1,n2))
else:
    print('{} é maior que {}'.format(n2,n1))