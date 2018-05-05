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
total = 0
mais = 10

# While
while mais != 0:
    total += mais
    while cont <= total:
        print('\33[34m{};'.format(termo))
        termo += razão
        cont += 1
    print('pausa..')
    print()
    mais = int(input('Quantos temor vc quer mostrar a mais? '))

# Total e Conclusão
print('\33[32m ')
print('Progressão finalizada com \"{}\" termos mostrados!'.format(total))
print('FIM ;)')
