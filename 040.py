n1 = float(input('informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A a média do aluno foi {}'.format(m))
if m < 5.0:
    print('REPROVADO')
elif 5 <= m <= 6.9:
    print('RECUPERAÇÃO')
elif m >=7.0:
    print('APROVADO')