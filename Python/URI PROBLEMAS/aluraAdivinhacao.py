print('*****************************************')
print('** *  **  JOGO DA ADVINHAÇÃO   **    * **')
print('*****************************************')

print('Tente adivinhar um número entre 0 a 100!')
print('')
print('Você começa com 1000 pontos!')
print('')

numero_secreto = 42
total_de_tentativas = 3
pt = 1000

tent = input("Em qual nível deseja jogar:\n1 - 20 Tentativas\n2 - 10 Tentativas\n3 - 05 Tentativas\n").strip()

if (tent == '1'):
    total_de_tentativas = 20
elif (tent == '2'):
    total_de_tentativas = 10
elif (tent == '3'):
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    print('')
    chute = int(input('Digite um número: '))
    print('')
    print('Você digitou: {}'.format(chute))


    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('Você acertou!!!')
        break
        print('')

    elif (maior):
        print('Você errou! O seu chute foi maior que o número secreto')
        print('')
        pt = abs(pt - 100)
    elif (menor):
        print('Você errou! O seu chute foi menor que o número secreto')
        print('')
        pt = abs(pt - 100)

    rodada = rodada + 1

print('Sua pontuação final foi de {}'.format(pt))
print('')

print('Fim do Jogo')
