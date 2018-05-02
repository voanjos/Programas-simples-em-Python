# Importanto bilhioteca
from datetime import date
atual = date.today().year

# Contadores
tmaior = 0
tmenor = 0
cont = 0

# Range
for p in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu (AAAA): '.format(p)))
    if atual - nasc >= 18:
        print('Está pessoa é MAIOR.')
        tmaior += 1
    else:
        print('Está pessoa é MENOR.')
        tmenor += 1

# Resultado
print()
print('''\33[1mMaior de Idade: {}
Menor de idade: {}'''.format(tmaior, tmenor))