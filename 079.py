n = list()
while True:
    try:
        a = int(input('Informe um número inteiro: '))
        if n.count(a) == 0:
            n.append(a)
            b = input('Digite S para sair ou pressione Enter para continuar: ').strip().upper()
            if b == 'S':
                break
        else:
            print('O número digitado ja existe na lista!')
            b = input('Digite S para sair ou pressione Enter para continuar').strip().upper()
            if b == 'S':
                break

    except ValueError:
        print('O valor digitado não é inteiro')
        b = input('Digite S para sair ou pressione Enter para continuar').strip().upper()
        if b == 'S':
            break
print('='*40)
print(f'A lista em ordem crescente é {sorted(n)}')