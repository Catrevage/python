from os import system
o = 0
while o != 4:
    n = int(input('Digite um número inteiro: '))
    z = str(n)
    print("""Escolha uma opção:')
    1- Binário
    2- Octal
    3- Hexadecimal
    4 - Para sair """)
    o = int(input('Opção:'))
    if len(z) > 18:
        print('Número não suportado!!!')
        o = 4
    if o == 1:
        i = 0
        q = 1
        c = [''] * 100
        while q != 0:
            if i == 0:
                v = n % 2
                c[i] = str(v)
                q = n // 2
                i = 1
            else:
                v = q % 2
                c[i] = str(v)
                i += 1
                q = q // 2
        s = ''
        for i in range(len(c)):
            s += str(c[i])
        print(s[::-1].strip())
    if o == 2:
        i = 0
        q = 1
        c = [''] * 100
        while q != 0:
            if i == 0:
                v = n % 8
                c[i] = str(v)
                i = 1
                q = n // 8
            else:
                v = q % 8
                c[i] = str(v)
                i += 1
                q = q // 8
        s = ''
        for i in range(len(c)):
            s += str(c[i])
        print(s[::-1].strip())
    if o == 3:
        h = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        if 0 <= n < 16:
            print(h[n])
        else:
            i = 0
            q = 1
            c = [0] * 16
            while q != 0:
                if i == 0:
                    v = n % 16
                    c[i] = v
                    i = 1
                    q = n // 16
                else:
                    v = q % 16
                    c[i] = v
                    i += 1
                    q = q // 16
            s = ''
            y = len(z) - 1
            w = len(z) - 2
            if len(z) == 2:
                for i in range(len(z)):
                    s += h[c[i]]
            if len(z) == 3:
                for i in range(len(z)):
                    s += h[c[i]]
            if len(z) == 4:
                for i in range(y):
                    s += h[c[i]]
            if len(z) == 5:
                for i in range(y):
                    s += h[c[i]]
            if len(z) == 6:
                for i in range(y):
                    s += h[c[i]]
            if len(z) >= 7:
                for i in range(w):
                    s += h[c[i]]
            print(s[::-1].strip())
    h = input('{}Pressione qualquer tecla para continuar!!!!{}'.format('='*30, '='*30))
    system('clear') or None