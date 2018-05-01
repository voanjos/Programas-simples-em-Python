# Acumuladores
soma = 0
cont = 0

# Leitura do número
num = int(input('Digite um Número: '))

# Definição do RANGE
for c in range(1, num, 2):
    if c % 3 == 0:
        soma += c
        cont += 1

# Resposta
print('A soma de todos os \"{}\" números impares encontrados,\n'
      'que são multiplos de 3 foi: {}'.format(cont, soma))
