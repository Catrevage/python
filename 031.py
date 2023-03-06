k = float(input('Informe a distância da viagem em KM: '))
if k <= 200:
    print('O valor da passagem é R${:.2f}'.format(k*0.5))
else:
    print('O valor da passagem é R${:.2f}'.format(k*0.45))