# Cabeçalho
print()
print('\33[1m='*25)
print('   10 TERMOS DE UMA PA')
print('='*25)
print()

# Variáveis
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1

# While
while cont <= 10:
    print('\33[34m{};'.format(termo))
    termo += razão
    cont += 1
print('FIM.')


# RANGE
#print()
#for c in range(primeiro, décimo,  razão):
#    print()
#    print('{}'.format(c), end=' ')
#print('Acabou!')
