n = input('informa a cidade onde você mora: ')
u = n.upper().strip()
l = u.split()
if 'SANTO' in l:
    print('O nome da sua cidade começa com a palavra santo')
else:
    print('O nome da sua cidade NÃO começa com a palavra santo')
