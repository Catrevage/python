from time import sleep

def maior(*a):
    b = str(a)
    print('='*40)
    print('Em', end=' ')
    for i in a:
        print(i, end=', ')
    print(f' Foram ecnotrados {len(a)} valores.\nO maior foi {max(a)}.', flush= True)
    sleep(2)





maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 8)
maior(1, 2)
maior(6)
