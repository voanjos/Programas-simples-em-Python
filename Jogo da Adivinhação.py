# Cabeçalho
print('\33[35mOi, sou seu computador..')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinha qual foi? ')

# Biblioteca
from random import randint

# Variáveis
computador = randint(1, 10)
acertou = False
palpite = 0

# While
while not acertou:
    print()
    jogador = int(input('\33[34mQual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('+ Mais.. Tente mais uma vez.')
        elif jogador > computador:
            print('- Menos.. Tente mais uma vez.')

# Condicional para o Final
if palpite <= 3:
    print('\33[1m')
    print('Parabéns! Você acertou na {} tentativa!'.format(palpite))
else:
    print('\33[1m')
    print('Você acertou na {} tentativa'.format(palpite))
