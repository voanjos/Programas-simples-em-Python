#Barra de Titulação:
print('\33[34m-=-'*6)
print('\33[34mCalculadora de IMC')
print('\33[34m-=-'*6)

#Peso e Altura:
peso = float(input('\33[32mDigite seu peso: '))
altura = float(input('\33[32mDigite sua altura: '))
imc = peso / (altura**2)

print(   )

#Estruturas Condicionais:
if imc < 18.5:
    print('Seu IMC é de: {:.1f}\nVocê está abaixo do peso!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de: {:.1f}\nParabéns! Você está em seu peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de: {:.1f}\nFique atento! Você está com SOBREPESO.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de: {:.1f}\nInfelizmente seu peso já é considerado obesidade.'.format(imc))
else:
    print('\33[31mSeu IMC é de: {:.1f}\nProcure um médico para lhe avaliar, \n'
          'pois seu peso já é considerado obesidade morbida!'.format(imc))
