from os import system
s = ''
while s!="M" and s!="F":
    s = input('Informe o sexo M ou F: ').upper().strip()
    system('clear') or None
print('fim')
