def menu(a):
    t = len(a) * 2
    print('~' * int(t))
    print(f'{a.upper():^{t}}')
    print('~' * int(t))

titulo = input('Informe o título do menu: ')

menu(titulo)