f = float(input('Informe o valor do imóvel: '))
s = float(input('Informe o valor do seu salário: '))
p = int(input('Informe em quantos anos deseja pagar: '))
vp = f/(p*12)
if vp <= s*0.3:
    print('O empréstimo foi aprovado! O valor da parcela é R$:{:.2f}'.format(vp))
else:
    print('O empréstimo não foi aprovado')
