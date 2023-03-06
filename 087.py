m = []
l = list()
s_par = s_3col = 0
for i in range(3):
    for c in range(3):
        l.append(int(input('Informe um número da posição [{}, {}]:'.format(i,c))))
    m.append(l[:])
    l.clear()
print('=-='*6)
for i in m:
    print('[ {} ] [ {} ] [ {} ]'.format(i[0],i[1],i[2]))
for i in m:
    for c in range(3):
        if i[c] % 2 == 0:
            s_par += i[c]
        if c == 2:
            s_3col += i[c]
print(f'A soma de todos o valores pares é {s_par}.')
print(f'A soma dos valores da terceira coluna é {s_3col}.')
print(f'O maior valor da segunda linha é {max(m[1])}.')



