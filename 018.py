from math import radians, sin, cos, tan
a = int(input('Informe o ângulo: '))
b = radians(a)
print('O Seno de {}° é {:.4f}'.format(a,sin(b)))
print('O Cosceno de {}° é {:.4f}'.format(a,cos(b)))
print('A Tangente de {}° é {:.4f}'.format(a,tan(b)))
