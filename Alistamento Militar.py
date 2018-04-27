#Importando biblioteca DATETIME para o ano atual
from datetime import date
atual = date.today().year

#Definindo a idade:
nasc = int(input('Digite o ano que você nasceu em 4 digitos: '))
idade = atual - nasc

#Definindo as condicionantes:
#Menor:
if atual - nasc < 18:
    print('\033[34mVocê tem {} anos e ainda faltam {} anos para se alistar.'
          .format(idade, 18 - idade))
#18 anos:
elif atual - nasc == 18:
    print('\033[33mVocê tem {} anos e deve se alistar este ano!'
          .format(idade))
#Maior:
elif atual - nasc > 18:
    print('\33[31mVocê tem {} e já deveria ter se alistado à {} anos atrás!'
          .format(idade, idade - 18))
    print('Seu ano de alistamento foi em: {}'.format(nasc + 18))
