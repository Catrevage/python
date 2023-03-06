dados = dict()
dados['nome'] = input('Nome: ').upper().strip()
i = int(input('Ano de nascimento: '))
dados['idade'] = 2022-i
ct = int(input('CPTS (0 se não tiver): '))
if ct != 0:
    dados['ctps'] = ct
    ac = int(input('Ano de contratação: '))
    tc = 2022-ac
    dados['ano_cont'] = ac
    dados['salario'] = float(input('Salário R$: '))
    dados['aposento'] = dados['idade'] + (35-tc)
print('-='*30)
for k, v in dados.items():
    print(f'{k.upper()}: {v}')
