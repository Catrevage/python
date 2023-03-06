m = []
l = list()
#s_par = s_3col = 0
for i in range(3):
    for c in range(3):
        l.append(int(input('Informe um número da posição [{}, {}]:'.format(i,c))))
    m.append(l[:])
    l.clear()
print('=-='*6)
for i in m:
    print('[ {} ] [ {} ] [ {} ]'.format(i[0],i[1],i[2]))