t = int(input('Informe um número: ')), int(input('Informe um número: ')), int(input('Informe um número: ')), int(input('Informe um número: '))
a = t.count(9)
c =[]
b = t.count(3)
print(f'O número 9 apareceu {a} vezes.')
if b != 0:
    print(f'O número 3 está na posição {t.index(3)+1}')
else:
    print('O número 3 não foi digitado nenhuma vez.')
for i in t:
    if i % 2 ==0:
        c.append(str(i))
print(f'Os números pares foram {str(",").join(c)}')
