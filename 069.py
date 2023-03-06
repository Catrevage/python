from os import system
nome = []
idade = []
sexo = []
while True:
    n = input('Informe o nome: ').upper().strip()
    nome.append(n)
    i = int(input('Informe a idade: '))
    idade.append(i)
    while True:
        s = input('Informe o sexo(M/F): ').upper().strip()
        if s == 'M' or s == 'F':
            sexo.append(s)
            break
    system('clear') or None
    while True:
        o = input('Deseja continuar cadastrando?S/N:').strip().upper()
        if o == 'N' or o == 'S':
            break
    if o == 'N':
        system('clear') or None
        break
    system('clear')or None
am18 = 0
for i in range(len(idade)):
    if idade[i] > 18:
        am18 += 1
bh = 0
for i in range(len(sexo)):
    if sexo[i] == 'M':
        bh +=1
cm20 = 0
for i in range(len(sexo)):
    if sexo[i] == 'F' and idade[i] < 20:
        cm20 +=1

system('clear') or None
print('==========LISTA DIGITADA================')
print('NOME -   IDADE   -   SEXO  ')
for i in range(len(nome)):
    print(f'{nome[i]}   |   {idade[i]}  |   {sexo[i]}')
print('=========================================')
print(end='')
print('===========ESTATÍSTICAS=================')
print(f'{am18} PESSOAS POSSUEM MAIS DE 18 ANOS.')
print(f'FORAM CADASTRADOS {bh} HOMEN(S).')
print(f'{cm20} MULHER(S) TEM MENOS DE 20 ANOS')
print('*******FIM DO PROGRAMA***********')
