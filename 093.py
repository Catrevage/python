dados = dict()
l = list()
c = 0
dados['nome'] = input('Nome: ').upper().strip()
p = int(input('Quantas partidas ele jogou?: '))
for i in range(p):
    l.append(int(input(f'Quantos gols ele fez na partida {i+1}: ')))
dados['gols'] = l[:]
dados['total'] = sum(l)
print('-='*30)
for k, v in dados.items():
    print(f'No campo {k} contém o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {p} partidas.')
for k in dados['gols']:
    c += 1
    print(f'    =>Na partida {c} ele marcou {k} gols.')
print(f'Foi um total de {dados["total"]} gols.')