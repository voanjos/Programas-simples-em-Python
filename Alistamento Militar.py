#Importando biblioteca DATETIME para o ano atual
from datetime import date
atual = date.today().year

#Definindo o sexo
sexo = int(input('''Masculino ou Feminino
[1] Feminino
[2] Masculino
1 ou 2: '''))

fem = 1
masc = 2

if sexo == fem:
    print('\033[35mMulheres não estão sujeitas ao Alistamento Militar Obrigatorio!'
          '\nMas sinta-se a vontade para servir as forças armadas se desejar!')
elif sexo == masc:
    nasc = int(input('Ano de nascimento: '))

    #Definindo a idade:
    idade = atual - nasc

    #Definindo as condicionantes:
    #Menor:
    if date - nasc < 18:
        print('\033[34mVocê tem {} anos e ainda faltam {} anos para se alistar'
              .format(idade, 18 - idade))
    #18 anos:
    elif date - nasc == 18:
        print('\033[33mVocê tem {} anos e deve se alistar imediatamente!'
              .format(idade))
    #Maior:
    elif date - nasc > 18:
        print('\33[31mVocê tem {} e já deveria ter se alistado a {} anos atrás!'
              .format(idade, idade - 18))
        print('Seu Alistamento foi em: {}!'.format(nasc + 18))
