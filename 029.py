v = float(input('Informe a velocidade do veículo: '))
if v > 80:
    print('O veículo foi multado! O valor da multa é R${:.2f}'.format((v-80)*7))
else:
    print("O veículo está dentro do limite de velocidade.")