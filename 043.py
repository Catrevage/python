p = float(input('Informe o seu peso: '))
a = float(input('Informe a sua altura em metros: '))
imc = p/(a**2)
print('O seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 < imc < 25.0:
    print('Você está com o peso ideal')
elif 25.0 < imc < 30.0:
    print('Você está com sobrepeso')
elif 30.0 < imc < 40.0:
    print('Você está com obesidade')
elif imc > 40.0:
    print('Você é obeso mórbido')