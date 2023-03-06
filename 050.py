cont_par = 0
for i in range(6):
    n = int(input('Informe um número inteiro: '))
    if n % 2 == 0:
        cont_par += n
print('A soma dos números pares é {}'.format(cont_par))
