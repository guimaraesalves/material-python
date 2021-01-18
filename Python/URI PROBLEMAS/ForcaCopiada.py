palavra = input('Digite uma palavra secreta:').upper().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = []
erros = 0
while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else ' _ '
    print(senha)
    if senha == palavra:
        print('Você acertou!')
        break
    tentativa = input('\nDigite uma letra:').upper().strip()
    if tentativa in digitadas:
        print('Você já tentou esta letra!')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')
    print('|==:==\n| : ')
    print('|  O ' if erros >= 1 else '|')
    linha2 = ' '
    if erros == 2:
        linha2 = ' /|\ '
    elif erros == 3:
        linha2 = ' | '
    elif erros >= 4:
        linha2 = ' | '
    print('|%s' % linha2)
    linha3 = ' I '
    if erros == 5:
        linha3 += " / \ "
    print("|%s" % linha3)
    print('|\n==========')
    if erros == 6:
        print('Enforcado!')
        break

