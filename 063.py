n = int(input('Informe uma número inteiro: '))
cont = 0
s = []
c = 0
while cont != n:
    if cont == 0:
        s.append(0)
        cont = 1
        s.append(cont)
    else:
        c = s[cont-1] + s[cont]
        s.append(c)
        cont += 1
print(s)
