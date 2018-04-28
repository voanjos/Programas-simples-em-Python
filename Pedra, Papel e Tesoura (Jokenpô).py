#Importanto bibliotecas:
from random import randint
from time import sleep

#Definindo variáveis:
itens = ('Pedra', 'PAPEL', 'TESOURA')
computador = randint(1, 3)
##print('COMPUTADOR: {}'.format(itens[computador]))

#Escolhas do Jogador e Computador:
print('''Suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')

#Caso o jogador escolha um número fora das opções:
jogador = (int(input('Qual é a sua jogada? ')))
##print('VOCÊ: {}'.format(itens[jogador]))
if jogador != 1 and jogador != 2 and jogador != 3:
    print('''\33[31mJogada Inválida!
Você deve escolher: 
    1 para PEDRA
        2 para PAPEL 
            3 para TESOURA''')
else:
#Cenário em que o computador escolhe ##PEDRA##
    if computador == 1:
        if jogador == 1: #Pedra
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[33mDeu Empate!')
        elif jogador == 2: #Papel
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[32Você VENCEU!!')
        elif jogador == 3: #Tesoura
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[31mVocê Perdeu.')

#Cenário em que o computador escolhe ##PAPEL##
    elif computador == 2:
        if jogador == 1:  # Pedra
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[31mVocê Perdeu.')
        elif jogador == 2:  # Papel
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[33mDeu Empate!')
        elif jogador == 3:  # Tesoura
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[32Você VENCEU!!')

#Cenário em que o computador escolhe ##TESOURA##
    elif computador == 3:
        if jogador == 1:  # Pedra
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[32Você VENCEU!!')
        elif jogador == 2:  # Papel
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[31mVocê Perdeu.')
        elif jogador == 3:  # Tesoura
            print()
            print('VOCÊ: {}'.format(itens[jogador]))
            print('COMPUTADOR: {}'.format(itens[computador]))
            print()
            print('\33[33mDeu Empate!')
