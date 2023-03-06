l = list()
while True:
    try:
        l.append(int(input('Informe um múmero')))
        s = input('Deseja continuar digitando S/N: ').upper().strip()
        if s == 'N':
            break
    except ValueError:
        print('Informe apenas números inteiros.')
i = []
p = []
for c in l:
    if c % 2 == 0:
        p.append(c)
    else:
        i.append(c)
print(f'A lista digitado é {l}')
print(f'Os números pares são {p}')
print(f'Os números ímpares são {i}')
