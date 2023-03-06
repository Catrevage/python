from time import sleep
from termcolor import cprint
for a in range(10, 0, -1):
    cprint(a,'red')
    sleep(1)
cprint('Feliz Ano Novo!!!', 'yellow')