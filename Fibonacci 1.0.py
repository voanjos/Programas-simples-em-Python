# O programa lê um número (N inteiro) qualquer e mostra
# na tela os (N primeiros) elementos de uma Sequência de Fibonacci.

# Cabeçalho
print()
print('\33[1m='*26)
print('  Sequência de Fibonacci')
print('='*26)
print()

# Input
n = int(input('Quantos termos vc quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{}; '.format(t1))
print('{}; '.format(t2))

# While
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('{}; '. format(t3))
    t1 = t2
    t2 = t3
    cont += 1
print('FIM.')
