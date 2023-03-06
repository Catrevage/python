l = list()
while True:
    try:
        l.append(int(input('Informe um múmero')))
        s = input('Deseja continuar digitando S/N: ').upper().strip()
        if s == 'N':
            break
    except ValueError:
        print('Informe apenas números inteiros.')
print(f'Foram digitados {len(l)} números.')
print(f'A lista em ordem decrescente é {l[::-1]}')
if l.count(5) > 0:
    print(f'O valor 5 está na lista e foi digitado {l.count(5)} vezes')