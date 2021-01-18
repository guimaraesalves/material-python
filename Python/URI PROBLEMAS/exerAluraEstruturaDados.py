lista1 = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
lista2 = []
lista3 = []

print(lista1)

print('O número de elementos da lista é: {}'.format(len(lista1)))
print('O maior numero da lista é {}.'.format(max(lista1)))
print('O menor numero da lista é {}.'.format(min(lista1)))

for valor in lista1:
    if valor % 2 == 0:
        lista2.append(valor)

print('O numeros pares são:\n {}'.format(lista2))

print('O numero de vezes que o numero {} aparece na lista é {} vezes'.format(lista1[0], lista1.count(lista1[0])))


print('A média da soma dos elementos da lista é {:.2f}'.format(sum(lista1) / len(lista1)))

for n in lista1:
    if n < 0:
        lista3.append(n)
print('A quantidade de números negativos é {} e eles são: {}'.format(len(lista3), lista3))
print('A soma dos numeros negativos são: {}'.format(sum(lista3)))










