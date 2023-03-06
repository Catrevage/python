n = int(input('Informe um número inteiro: '))
m = n/2 + 1
l = [''] * int(m)
cont = 0
for i in range(n+1):
    if i % 2 == 0:
        l[cont] = str(i)
        cont += 1
print(l)
print('De 0 até {} existem {} números pares'.format(n,len(l)))

