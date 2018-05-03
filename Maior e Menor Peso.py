# Variáveis
maior = 0
menor = 0

# Range
for c in range(1, 6):
    peso = float(input('Digite o {}º peso: '.format(c)))

    # Condições
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

# Resultado
print('\33[1m')
print('O maior peso foi: {}kg'.format(maior))
print('O menor peso foi: {}kg'.format(menor))
