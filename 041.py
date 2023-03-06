from datetime import date
a = int(input('informe o ano de nascimento do atleta: '))
i = date.today().year - a
print('{} anos'.format(i))
if 1 <= i <= 9:
    print('CATEGORIA MIRIM')
elif 9 < i <= 14:
    print('CATEGORIA INFANTIL')
elif 14 < i <= 19:
    print('CATEGORIA JUNIOR')
elif 19 < i <= 20:
    print('CATEGORIA SENIOR')
elif i > 20:
    print('CATEGORIA MASTER')