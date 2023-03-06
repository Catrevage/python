from os import system
while True:
    n = int(input('Informe um número: '))
    system('clear') or None
    if n < 0:
        break
    for i in range(11):
        print(f'{n} x {i} = {n*i}')
    j = input('Pressione qualquer tecla')
print('FIM')