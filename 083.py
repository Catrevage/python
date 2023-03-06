e = input('Digite uma expressão matémática: ')
def valida_expressao(a):
    v = False
    pos = 0
    for i in a:
        if a.count('(') == 0 and a.count(')') == 0:
            v = True
        elif i == '(':
            for c in range(a.index('('), len(a)):
                if a[c] == ')' and a.count('(') == a.count(')'):
                    v = True
                    pos = a.index(')')
                    break
                else:
                    v = False
            if v is True:
                for d in range(pos, len(a)):
                    if a[d] == '(':
                        for c in range(a.index('('), len(a)):
                            if a[c] == ')':
                                v = True
                                break
                            else:
                                v = False
                    else:
                        v = True
    if v is True:
        return('válida')
    else:
        return('inválida')
print(f'A expressão é {valida_expressao(e)}!')
