n = input('Informe um número de 0 a 9999: ')
if len(n)==1:
    print('Unidade: {}'.format(n[0]))
if len(n)==2:
    print('Dezena: {}'.format(n[0]))
    print('Unidade: {} '.format(n[1]))
if len(n)==3:
    print('Centena: {}'.format(n[0]))
    print('Dezena: {}'.format(n[1]))
    print('Unidade: {} '.format(n[2]))
if len(n) == 4:
    print('Milhar: {}'.format(n[0]))
    print('Centena: {}'.format(n[1]))
    print('Dezena: {}'.format(n[2]))
    print('Unidade: {} '.format(n[3]))
