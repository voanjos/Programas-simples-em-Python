from time import sleep

print()
n1 = int(input('\33[1mDigite o primeiro Valor: '))
n2 = int(input('Digite o segundo valor: '))

opção = 0
while opção != 5:
    print('''    \33[m[1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('\33[34mDigite sua opção: '))
    if opção == 1:
        print()
        soma = n1 + n2
        print('\33[33m{} + {} = {}'.format(n1, n2, soma))
    if opção == 2:
        print()
        produto = n1 * n2
        print('\33[33m{} x {} = {}'.format(n1, n2, produto))
    if opção == 3:
        print()
        if n1 > n2:
            print('\33[33m{} é o maior número.'.format(n1))
        if n2 > n1:
            print('\33[33m{} é o maior número.'.format(n2))
        else:
            print('\33[33mOs números são iguais!')
    if opção == 4:
        print()
        print('\33[33mRecarregando menu..')
        sleep(1)
        n1 = int(input('\33[1mDigite o primeiro Valor: '))
        n2 = int(input('Digite o segundo valor: '))
    if opção == 5:
        print()
        print('\33[33mFinalizando..')
        sleep(1.5)
print('\33[1mObrigado, volte sempre!')
