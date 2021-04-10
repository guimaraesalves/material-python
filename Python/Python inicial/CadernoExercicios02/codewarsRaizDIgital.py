 #raiz digital é a soma recursiva de todos os dígitos de um número.

'''Dado n, pegue a soma dos dígitos de n. Se esse valor tiver mais de um dígito, 
continue reduzindo dessa forma até que um número de um dígito seja produzido. 
A entrada será um número inteiro não negativo.'''

# EXEMPLO
'''
16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


'''
# 1º - separar o n em algarismos individuais:
'''n = int(input('Digite um numero: '))
soma = 0
nString = str(n) # Transformando em str para poder usar a posição.Ex: "b[1] = 2"
for i in range(len(nString)):
    soma += int(nString[i])
    print(nString[2])
print(soma)
'''
n = int(input('Digite um numero: '))
x = 0
y = 0
s = 0
s1 = 0
ns = str(n)
for i in range(len(ns)):
    x = ns[0]
    y = ns[1]
    s = x + y
    x




