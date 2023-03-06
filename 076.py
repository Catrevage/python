

t = ('Feijão Carioquinha', 5.95), ('Arroz', 3.90), ('Macarrão D. Benta', 4.80), ('Café', 7.99)
print('-'*35)
print(f"LISTAGEM DE PRODUTOS")
print('{}'.format('-'*35))
for i in t:
    produto, preço = i
    print('{:<25} R${:<4}'.format(produto, preço))