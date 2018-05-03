# Acumuladores
soma = 0
cont = 0

# Definição do RANGE
for c in range(1, 7):
    num = int(input('Escolha o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1

# Resultado
print()
print('\33[34mForam \"{}\" valores pares e a soma deles foi: {}'.format(cont, soma))
