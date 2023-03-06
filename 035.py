r1 = float(input('Informe o comprimento do seguimento 1:'))
r2 = float(input('Informe o comprimento do seguimento 2:'))
r3 = float(input('Informe o comprimento do seguimento 3:'))
l = [r1,r2,r3]
t = sorted(l)
if t[0]+t[1] > t[2]:
    print('Os seguimentos de reta podem formar um triângulo')
else:
    print('Os seguimentos não formam um triângulo')
