n = list()
for i in range(5):
    c = 0
    a = int(input('Informe um número: '))
    if i == 0 or a > n[-1]:
        n.append(a)
    else:
        for i in range(len(n)):
            if a < n[c]:
                n.insert(c, a)
                break
            c += 1
print(f'A lista em ordem é {n}')
