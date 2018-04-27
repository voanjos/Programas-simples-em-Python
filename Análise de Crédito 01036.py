# Definindo variáveis
emp = float(input('Valor do empréstimo: R$ '))
sal = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prest = emp / anos / 12

#Corpo da resposta
print('Para financiar uma casa de R$ {:.2f} em {} anos, '
      'a prestação será de R${:.2f}'.format(emp, anos, prest))

#Aceitabilidade do emprestimo
if prest > (sal*30/100):
    print('Empréstimo \033[31mnegado.')
else:
    print('Emprestimo \033[32mACEITO!')