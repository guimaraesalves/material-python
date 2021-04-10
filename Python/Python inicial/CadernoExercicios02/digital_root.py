# raiz digital é a soma recursiva de todos os dígitos de um número.

'''Dado n, pegue a soma dos dígitos de n. Se esse valor tiver mais de um dígito,
continue reduzindo dessa forma até que um número de um dígito seja produzido.
A entrada será um número inteiro não negativo.'''

# 1º - separar o n em algarismos individuais e somá-los.
# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


num = int(input())
def digital_root(num):
    root = num % 9
    if root != 0 or num == 0:
        return root
    return 9







