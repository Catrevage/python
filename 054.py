from os import system
ano = 0
cont = 0
for i in range(7):
    print('Informe o ano de nascimento da {}ª pessoa'.format(i+1))
    ano = int(input('Ano: '))
    system('clear') or None
    if ano <= 2001:
        cont += 1
print('='*25)
print('{} pessoas tem maior idade.'.format(cont))
print('='*25)
