n = int(input('Infrme um número: '))
c = 0
r = n
f = 0
while r != 0:
    if c == 0:
        f += (n * n-1)
        c += 1
        r = n-c
    else:
        c += 1
        f += f * r
        r = abs(n-c)
print(f)



