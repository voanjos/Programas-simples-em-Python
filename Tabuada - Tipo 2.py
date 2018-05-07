# O programa faz a tabuada de qualquer número inteiro, quantas
# vezes o usuário quiser, até digitar o número 0 (ZERO), que aciona o comando BREAK.

while True:
    print()
    n = int(input('\33[1mDigite para a sua tabuada: '))
    if n == 0:
        break
    for c in range(1, 10):
        print(f'\33[36m{n} x {c} = {n*c:.0f}')
print('\33[34mFIM ;)')
