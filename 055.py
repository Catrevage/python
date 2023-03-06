from os import system
peso = ['']*5
p = 0
for i in range(5):
    p = float(input('Informe o seu peso: '))
    peso[i] = p
    system('clear') or None
print('O maior peso foi {}Kg'.format(max(peso)))
print('O menor peso foi {}Kg'.format(min(peso)))