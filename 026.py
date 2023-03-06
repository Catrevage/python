f = input('Digite uma frase: ').strip()
u = f.upper()
if u.find('A') > -1:
    print('Nesta frase a letra A aparece {} vezes'.format(u.count('A')))
    print('A letra A aparece na posição {} na primeira vez'.format(u.find('A')+1))
    print('A letra A aparece na posição {} na última vez'.format(u.rfind('A')+1))
else:
    print('Na sentença digitada não existe a letra A')
