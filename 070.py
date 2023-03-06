from os import system
produto = []
preco = []
while True:
    p = input('Informe o nome do produto: ').upper().strip()
    produto.append(p)
    v = float(input('Indorme o preço: '))
    system('clear') or None
    preco.append(v)
    while True:
        o = input('Deseja continuar cadastrando S/N?: ').upper().strip()
        if o == 'S' or o == "N":
            break
    if o == 'N':
        break
    system('clear') or None
system('clear') or None
print('='*40)
a = sum(preco)
print(f'O TOTAL DOS PRODUTOS É: R${a:.2f}')
b = 0
for i in range(len(preco)):
    if preco[i] > 1000:
        b +=1
print(f'{b} PRODUTOS CUSTAM MAIS DE R$1000.00')
c = min(preco)
d = preco.index(c)
print(f'O PRODUTO MAIS BARATO FOI {produto[d]}.')
print('='*40)
print('FIM')