# Contadores
idadeSoma = 0
idadeMédia = 0
idhmaisvelho = 0
nomemaisvelho = ''
mulheres20 = 0

#Range
for p in range(1, 5):
    print('-=-=-= {}ª PESSOA =-=-=-'.format(p))
    nome = str(input('NOME: ')).strip().title()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    print()
    idadeSoma += idade

    # Condicionais
    if p == 1 and sexo in 'Mm':
        idhmaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > idhmaisvelho:
        idhmaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres20 += 1

idadeMédia = idadeSoma / 4

# Resultado
print('\033[1mA média de idade do grupo é de {:.0f} anos;'.format(idadeMédia))
print('O homem mais velho tem {} anos e se chama {};'.format(idhmaisvelho, nomemaisvelho))
print('{} mulher(es) tem menos de 20 anos.'.format(mulheres20))
