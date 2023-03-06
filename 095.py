from os import system
dados = dict()
l = list()
l2 = list()
c = 0
while True:
    system('clear') or None
    dados['nome'] = input('Nome: ').upper().strip()
    p = int(input('Quantas partidas ele jogou?: '))
    for i in range(p):
        l.append(int(input(f'Quantos gols ele fez na partida {i+1}: ')))
    dados['gols'] = l[:]
    dados['total'] = sum(l)
    l2.append(dados.copy())
    l.clear()
    o = input('Continuar?[S/N]: ').upper().strip()
    if o == 'N':
        system('clear') or None
        break

print('-='*30)
print(f'{"Cod":<5}{"NOME":<20}{"GOLS":<20}{"TOTAL":<3}')
for i, c in enumerate(l2):
    print(f'{i:<5}{c["nome"]:<20}{str(c["gols"]):<20}{c["total"]:<3}')
print('-='*30)
a = 0
while True:
    a = int(input('Mostrar dados de qual jogador?: '))
    if a == 999:
        print('FIM')
        break
    if a > (len(l2)-1):
        print(f'Jogador {a} não encontrado!')
    else:
        print(f'Dados do jogador {l2[a]["nome"]}:')
        for i, v in enumerate(l2[a]['gols']):
            print(f'Na partida {i+1} ele marcou {v} gols.')

