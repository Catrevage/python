from os import system
t = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    n = int(input('Informe um número de 0 a 20: '))
    system('clear') or None
    if n >= 0 and n <= 20:
        break
for i in range(len(t)):
    if i == n:
        s = t[i]
        print(s.upper())
