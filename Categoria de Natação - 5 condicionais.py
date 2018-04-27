#Importando biblioteca DATETIME
from datetime import date

#Definindo Variáveis:

#Ano de Nascimento
nasc = int(input('Ano de nascimento: '))
#Ano Atual
AnoAtual = date.today().year
#Idade do Nadador
id = AnoAtual - nasc

#Definindo condicionais de categoria:
if id <= 9:
    print('\033[34mO(A) atleta tem {} anos.\n'
          'Disputará a categoria MIRIM.'.format(id))
elif id <= 14:
    print('\033[34mO(A) atleta tem {} anos.\n'
          'Disputará a categoria INFANTIL.'.format(id))
elif id <= 19:
    print('\033[34mO(A) atleta tem {} anos.\n'
          'Disputará a categoria JUNIOR.'.format(id))
elif id <= 25:
    print('\033[34mO(A) atleta tem {} anos.\n'
          'Disputará a categoria SÊNIOR.'.format(id))
else:
    print('\033[34mO(A) atleta tem {} anos.\n'
          'Disputará a categoria MASTER.'.format(id))
