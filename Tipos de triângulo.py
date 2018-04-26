#Barra de Titulação:
print('\33[33m-=- '*6)
print('Descubra o Triângulo.')

#Definindo os Lados:
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

#Condicional do tiângulo:
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\33[36mEssas medidas formam um triângulo,')
    if l1 == l2 == l3:
        print('mais precisamente um triângulo Equilátero.')
    elif l1 == l2 or l1 == l3 or l2 == l3 or l3 == l2:
        print('mais precisamente um triângulo Isóseles.')
    elif l1 != l2 != l3:
        print('mais precisamente um triângulo Escaleno.')
else:
    print('\33[31mEssas medidas justas NÃO formam um triângulo.')
