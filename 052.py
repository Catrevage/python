n = int(input('Informe um número: '))
cont = 0
for i in range(2, 10):
    if n % i == 0:
        cont += 1
if cont == 0 and n != 1:
    print('Este número é primo')
else:
    print('Este número não é primo')
