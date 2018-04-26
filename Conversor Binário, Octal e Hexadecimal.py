#Definição do numeral a ser convertido
num = int(input('Digite um número inteiro: '))

#Definição da base para conversão
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

#Condicionais
if opção == 1:
    print('{} convertido em BINÁRIO: {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido em OCTAL: {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido em HEXADECIMAL: {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mOPÇÃO INVALIDA!')
    print('Você deve escolher entre as opções [1, 2 e 3]')
