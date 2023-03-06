from random import randint
n = int(input('Estou pensando em um número entre 0 a 5, Qual é?: '))
s = randint(0, 5)
if n==s:
    print('PARABÉNS você acertou miseravi!')
else:
    print("ERRRRRRRROU!!!! O número é {}".format(s))