#Importanto bibliotecas:
from random import randint
from time import sleep

#Definindo variáveis:
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

#Escolhas do Jogador e Computador:
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

#Caso o jogador escolha um número fora das opções:
jogador = (int(input('Qual é a sua jogada? ')))

if jogador != 0 and jogador != 1 and jogador != 2:
    print('''\33[31mJogada Inválida!
Você deve escolher: 
    0 para PEDRA
        1 para PAPEL 
            2 para TESOURA''')

else:
#Cenário em que o computador escolhe ##PEDRA##
    if computador == 0:
        if jogador == 0: #Pedra
            print()
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PÔ!!')
            sleep(1)
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[33mDeu Empate!')
        elif jogador == 1: #Papel
            print()
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PÔ!!')
            sleep(1)
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[32mVocê VENCEU!!')
        elif jogador == 2: #Tesoura
            print()
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PÔ!!')
            sleep(1)
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[31mVocê Perdeu.')

#Cenário em que o computador escolhe ##PAPEL##
    elif computador == 1:
        if jogador == 0:  # Pedra
            print()
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PÔ!!')
            sleep(1)
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[31mVocê Perdeu.')
        elif jogador == 1:  # Papel
            print()
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PÔ!!')
            sleep(1)
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[33mDeu Empate!')
        elif jogador == 2:  # Tesoura
            print()
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PÔ!!')
            sleep(1)
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[32mVocê VENCEU!!')

#Cenário em que o computador escolhe ##TESOURA##
    elif computador == 2:
        if jogador == 0:  # Pedra
            print()
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PÔ!!')
            sleep(1)
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[32mVocê VENCEU!!')
        elif jogador == 1:  # Papel
            print()
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PÔ!!')
            sleep(1)
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[31mVocê Perdeu.')
        elif jogador == 2:  # Tesoura
            print()
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PÔ!!')
            sleep(1)
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[33mDeu Empate!')