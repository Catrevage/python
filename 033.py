n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
l = [n1, n2, n3]
r = sorted(l)
print('O menor número digitado foi {}'.format(r[0]))
print('O maior número digitado foi {}'.format(r[2])
