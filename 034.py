s = float(input('Informe o salário do funcionário: '))
if s > 1250:
    print('O salário com aumento é R${:.2f}'.format(s*1.1))
elif s <= 1250:
    print('O salário com aumento é de R${:.2f}'.format(s*1.15))
