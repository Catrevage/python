n = input('Informe o seu nome completo:')
print('Seu nome em maiúsculo é: {}'.format(n.upper()))
print('Seu nome em minúsculo é: {}'.format(n.lower()))
s = n.count(' ')
q = len(n)
print('O Nome possui {} letras'.format(q-s))
l = n.split()
p = l[0]
print('O primeiro nome tem {} letras'.format(len(p)))