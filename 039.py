import datetime
i = str(input('Informe a sua data de nascimento(DDMMAAA):'))
ref1 = datetime.date(year=2004, month=1, day=1)
ref2 = datetime.date(year=2004, month=1, day=31)
n = datetime.datetime.strptime(i, '%d%m%Y')
idade_alist = (datetime.date.today() - ref1).days
idade_user = (datetime.date.today() - n.date()).days

def calc_mes(a):
    if 1 <= a.month <= 5:
        m = datetime.date.today().month - a.month
        return(m)
    elif 6 <= n.month <= 12:
        m = (12 - a.month) + datetime.date.today().month
        return(m)

def calc_dia(a):
        d = (30 - a.day) + datetime.date.today().day
        return(d)

ano = idade_user // 365
mes = calc_mes(n)
dia = calc_dia(n)
print('Sua idade é  {} anos, {} meses e {} dias.'.format(ano,mes,dia))
if ref1.year == n.year:
    print('O Sr está em idade de alistamento, por favor apresente-se')
elif (idade_user // 365) > (idade_alist // 365):
    print('O Sr passou da idade de alistamento.')
elif (idade_user // 365) < (idade_alist // 365):
    print("""O Sr ainda não está na idade do alistamento,\n
    ainda falta {} anos, {} meses e {} dias.""".format((idade_alist // 365) - ano, abs((idade_alist % 12) - n.month), abs((idade_alist % 30) - n.day)))