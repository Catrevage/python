l = []
time = 'asa', 'csa', 'crb', 'murici', 'cse', 'corinthians alagoano', 'penedense', 'coruripe', 'cruzeiro', 'chapecoense'
print(f'Os cinco preimeiros colocados são: {time[:-4]}')
print(f'Os últimos 4 colocados são: {time[5:]}')
for i in range(len(time)):
    l.append(time[i])
print(f'A lista dos times em ordem alfabética é: {sorted(l)}')
print(f'O time da Chapecoense está em {time.index("chapecoense") + 1}º lugar')