a1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informa a razão da PA: '))
l = [''] * 10
l[0] = a1
for i in range(1, 10):
    l[i] = a1 + (i*r)
print('A sequência é: {}'.format(l))
