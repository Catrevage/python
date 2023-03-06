from random import randint
from time import sleep
from os import system
c = 0
r = 1
t = 0
while c != r:
    r = int(input('Digite um número de 0 a 10: '))
    c =randint(0, 10)
    t += 1
    if r != c:
        print('O computador jogou {}, tente novamente...'.format(c))
        sleep(3)
    system('clear') or None
print('Parabéns!!! Você acertou depois de {} tentaivas'.format(t))
print('=======FIM DO JOGO=======')