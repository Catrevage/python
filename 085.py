lista = list()
par = list()
imp = list()
for i in range(7):
    n = int(input(f'Informe o {i+1}º número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
lista.append(imp[:])
lista.append(par[:])
print(f'O valor ímpares são {sorted(lista[0])}')
print(f'Os valores pares são {sorted(lista[1])}')
