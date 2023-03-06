from os import system
n = list()
system('clear') or None
for i in range(5):
    system('clear') or None
    while True:
        try:
            print('====LISTA DE NḾEROS INTEIROS====')
            n.append(int(input(f'Informe um número inteiro para a posição {i}: ')))
            system('clear') or None
            break
        except ValueError:
            print('O valor digitado não é inteiro')
system('clear') or None
plus = n[:]
minor = n[:]
def maior(a):
    m = max(a)
    r = list()
    for i in a:
        if i == m:
            r.append(str(a.index(m)))
            a[a.index(m)] = ''
    return r
def menor(a):
    m = min(a)
    r = list()
    for i in a:
        if i == m:
            r.append(str(a.index(m)))
            a[a.index(m)] = ''
    return r
print('='*40)
print(f'A sequência digitada foi {n}')
print(f'O maior valor foi {max(n)}; na posição {str("... ").join(maior(plus))}...')
print(f'O menor valor foi {min(n)}; na posição {str("... ").join(menor(minor))}...')
