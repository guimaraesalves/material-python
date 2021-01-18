print('*************************')
print('** JOGO DA ADIVINHAÇÃO **')
print('*************************')

numero_secreto = 42
x = 10
while (x < 10):
     
chute = int(input('Digite o seu número: '))
print('Você digitou {}'.format(chute))

acerto = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

     chute = int(input('Digite o seu número: '))
if (acerto):
     print('VOCÊ ACERTOU!!')
elif (maior):
     print('VOCÊ ERROU PARA CIMA!')
elif (menor):
     print ('VOCÊ ERROU PARA BAIXO!')
     x = x - 1
     

