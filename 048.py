n = int(input('Informe um número inteiro: '))
cont = 0
for i in range(1,n+1):
    if i % 2 != 0:
        if i % 3 == 0:
            cont += i
print('A soma dos do números impares múltiplos de 3 \n entre 1 e {} é {}'.format(n,cont))