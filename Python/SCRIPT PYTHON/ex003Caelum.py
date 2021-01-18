numero = '5'

chute = input('Digite um numero de 0 a 10:\n')

acertou = chute == numero
maior = chute > numero
menor = chute < numero

if (acertou):
     print('Você acertou')
elif(maior):
     print('Você errou! O seu chute foi maior que o número secreto')
elif(menor):
    print('Você errou! O seu chute foi menor que o número secreto')

