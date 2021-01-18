print('*******************************')
print('**   JOGO DA ADVINHAÇÃO      **')
print('*******************************')

numero_secreto = 42

rodada = 1
tent = input("Em qual nível deseja jogar:\n1 - 20 Tentativas\n2 - 10 Tentativas\n3 - 05 Tentativas\n")

if (tent == '1'):
    total_de_tentativas = 20
elif (tent == '2'):
    total_de_tentativas = 10
elif (tent == '3'):
    total_de_tentativas = 5

for tent in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite um número: '))
    print('Você digitou: {}'.format(chute))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

if (acertou):
    print('Você acertou')


elif (maior):
    print('Você errou! O seu chute foi maior que o número secreto')
elif (menor):
    print('Você errou! O seu chute foi menor que o número secreto')

print('Fim do Jogo')
