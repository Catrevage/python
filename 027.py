n = input('Informe o seu nome completo: ').strip()
s = n.split()
print("Primeiro nome: {}".format(s[0].upper()))
print('Último nome: {}'.format(s[len(s)-1].upper()))
