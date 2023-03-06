p = float(input('Informe o preço do produto: '))
print("""===Escolha uma opção===
[1] À VISTA DINHEIRO
[2] À VISTA CARTÃO
[3] ATÉ 2X NO CARTÃO
[4] MAIS DE 3X NO CARTÃO""")
o = input('Informe: ').strip()
if o == '1':
    print('O preço do produto com 10% de desconto  é R${:.2f}'.format(p - (p*0.1)))
elif o == '2':
    print('O preço do produto com 5% de desconto é R${:.2f}'.format(p - (p*0.05)))
elif o =='3':
    print('O preço do produto é R${}'.format(p))
elif o =='4':
    print('O preço do produto com 20% de acréscimo é R${:.2f}'.format(p*1.2))

