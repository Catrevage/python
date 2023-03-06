n = input('Informe o seu nome completo: ').strip()
u = n.upper()
if u.find('SILVA') > -1:
    print('O seu nome tem SILVA')
else:
    print('O seu nome NÃO tem SILVA')