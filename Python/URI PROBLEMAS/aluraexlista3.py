#Faça um programa que leia 4 notas, mostre as notas e a média na tela.

lista = []
media = 0
print ('informe as suas 4 notas: ')
for i in range(4):
    lista.append(float(input('Nota  ' + str(i + 1) + ':\n')))
    media += lista[i]
media = media/4
print ('Suas notas: {}'.format(lista))
print ('Sua média é: {:.2f}'.format(media))
