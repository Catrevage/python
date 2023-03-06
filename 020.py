import random
a =input('Informe o nome do aluno 1: ')
b = input('Informe o nome do aluno 2: ')
c = input('Informe o nome do aluno 3: ')
d = input('Informe o nome do aluno 4: ')
s = random.sample([a,b,c,d],k=4)
print('A ordem de apresentação é {}'.format(s))