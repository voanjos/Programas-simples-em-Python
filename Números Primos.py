# Variáveis
n = int(input('Digite um número: '))
tot = 0

# RANGE
for c in range(1, n + 1):

# Define os números PRIMOS em amarelo
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\33[m', end='')
    print('{}'.format(c), end=' ')

# Informa se é ou não um número PRIMO
if tot == 2:
    print('\n\33[33mForam {} números divisiveis, este número É PRIMO.'
          .format(tot))
else:
    print('\n\33[31mForam {} números divisiveis, este número NÃO É PRIMO.'
          .format(tot))
