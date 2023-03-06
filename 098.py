from time import sleep

def contador(i,f, p):
    topo = f    
    if i > f:
        if p == 0:
            p = -1
        f = f - abs(p)
        if p > 0:
            p = p * -1        
    else:
        if p == 0:
            p = 1
        if p < 0:
            p = p * -1        
        f +=1    
    print(f'Contagem de {i} até {topo} de {abs(p)} em {abs(p)}')
    print('='*30)            
    for c in range(i, f, p):
        print(c, end=' ', flush= True)
        sleep(1)
    print('FIM!')


def mostralinha(a):
    t = len(a) * 2
    print('=' * int(t))
    print(f'{a.upper():^{t}}')
    print('=' * int(t))

m = 'contador'

contador(1, 10, 1)
contador(10, 0, 2)

mostralinha(m)

inicio = int(input('Informe o valor inicial: '))
final = int(input('Informe o valor final: '))
passo = int(input('Informe o valor do passo: '))
contador(inicio,final, passo)
