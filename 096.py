def area(a, b):
    return(print(f' A área do terro {a}m x {b}m é {a*b}m².'))


print('='*30)
print(f'{"ÁREA DE TERRENOS":^30}')
print('='*30)

c = float(input('Informe o compimento: '))
l = float(input('Informe a largura: '))

area(c, l)
