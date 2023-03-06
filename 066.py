from os import system
l = []
while True:
    n = int(input('Informe um número:'))
    system('clear')
    l.append(n)
    if n == 999:
        break
l.remove(999)
print('='*50)
print(f'Foram digitados {len(l)} números.')
print(f'A soma de todos os números é {sum(l)}.')
print('='*50)