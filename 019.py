import random
a =input('Informe o nome do aluno 1: ')
b = input('Informe o nome do aluno 2: ')
c = input('Informe o nome do aluno 3: ')
d = input('Informe o nome do aluno 4: ')
s = random.choice([a,b,c,d])
print('O aluno sorteado para apagar o quadro foi {}'.format(s.upper()))
