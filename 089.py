from os import system
from time import sleep
cad_aluno = list()
l = list()
while True:
    print('-='*15)
    print("NOTAS DOS ALUNOS")
    print('=' * 30)
    print("""[1] - CADASTRAR NOTA/ALUNO
[2] - BOLETIM GERAL
[3] - CONSULTA INDIVIDUAL
[4] - SAIR""")
    print('=' * 30)
    o = input('Escolha uma opção: ').strip()
    system('clear') or None
    if o == '1':
        l.append(input('Aluno: ').upper().strip())
        l.append(float(input('Nota AV1: ')))
        l.append(float(input('Nota AV2: ')))
        cad_aluno.append(l[:])
        l.clear()
        system('clear') or None
    elif o == '2':
        print(f'{"BOLETIM GERAL":^35}')
        print(f'{"MAT":<5}{"NOME":<20}{"MÉDIA":<10}')
        for i, ind in enumerate(cad_aluno):
            print(f'{i:<5}{ind[0]:<20}{(ind[1]+ind[2])/2:<10}')
        a = input('Pressione enter...')
        system('clear') or None
    elif o == '3':
        c = int(input('Informe matrícula do aluno do aluno: '))
        print(f'{"NOME":<20}{"AV1":<10}{"AV2":<10}')
        for i, m in enumerate(cad_aluno):
            if i == c:
                print(f'{m[0]:<20}{m[1]:<10}{m[2]:<0}')
        a = input('Pressione Enter...')
    elif o == '4':
        print('Obrigado!')
        break
