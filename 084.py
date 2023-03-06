from statistics import mean
dados = list()
cad_usuario = list()
gordo = list()
magro = list()
peso = list()
while True:
    print('CADASTRO')
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    cad_usuario.append(dados[:])
    dados.clear()
    o = input('Deseja continuar cadastrando? S/N').upper().strip()
    if o == 'N':
        break
for i in cad_usuario:
    peso.append(i[1])
for i in cad_usuario:
    if i[1] >= mean(peso):
        gordo.append(i)
    else:
        magro.append(i)
print(f'Foram cadastradas {len(cad_usuario)} pessoas.')
print(f'A média de peso é {mean(peso):.2f}')
print('-='*15)
print(f"{'=MENOS PESADOS=':^25}")
print(f"{'NOME':<20}{'PESO(Kg)':<10}")
for i in magro:
    print(f'{i[0].upper():<20}{i[1]:<10}')
print('-='*15)
print(f"{'=MAIS PESADOS=':^25}")
print(f"{'NOME':<20}{'PESO(Kg)':<10}")
for i in gordo:
    print(f'{i[0].upper():<20}{i[1]:<10}')
    