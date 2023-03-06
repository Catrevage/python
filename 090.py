aluno = dict()
aluno['nome'] = input('Nome: ').upper().strip()
aluno['med'] = float(input('Média: '))
print(f'O nome é igual a {aluno["nome"]}')
print(f'A média de {aluno["nome"]} é {aluno["med"]}.')
if aluno['med'] >= 6:
    print(f'A situação de {aluno["nome"]} é Aprovado!')
else:
    print(f'A situação de {aluno["nome"]} é Reprovado!')