f = str(input('Digite uma frase: ')).strip()
us = f.upper().replace(' ','')
c = ''
for i in range(len(us), 0, -1):
    c += us[i-1]
cont = 0
for i in range(len(us)):
    if c[i] == us[i]:
        cont += 1
if cont == len(us):
    print('A frase é um palídromo')
else:
    print('A frase não é um palídromo')
