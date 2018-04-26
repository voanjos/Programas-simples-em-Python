#Definindo ano de nascimento:
nasc = int(input('Ano de nascimento: '))

#Definindo a idade:
idade = 2018 - nasc

#Definindo as condicionantes:
if 2018 - nasc < 18:
    print('\033[34mVocê tem {} anos e ainda faltam {} anos para se alistar'
          .format(idade, 18 - idade))
elif 2018 - nasc == 18:
    print('\033[33mVocê tem {} anos e deve se alistar imediatamente!'
          .format(idade))
elif 2018 - nasc > 18:
    print('\33[31mVocê tem {} e já deveria ter se alistado a {} anos!'
          .format(idade, idade - 18))
