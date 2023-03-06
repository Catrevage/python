n = 0
s = 0
c = 0
while n != 999:
    n = int(input('Informe um número inteiro: '))
    if n != 999:
        s += n
        c += 1
print('Você digitou {} numeros e a soma de todos é {}'. format(c,s))