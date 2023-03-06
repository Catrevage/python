import math
o = float(input('Digite o valor do cateto oposto:'))
a = float(input('Digite o valor do cateto adjacente: '))
h = a**2 + o**2
print('O valor da hipotenusa é {:.2f}'.format(math.sqrt(h)))