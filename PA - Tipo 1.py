# Cabeçalho
print()
print('\33[1m='*25)
print('   10 TERMOS DE UMA PA')
print('='*25)
print()

# Variáveis
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10) * razão

# RANGE
print()
for c in range(primeiro, décimo,  razão):
    print('{}'.format(c), end=' -> ')
print('Acabou!')
