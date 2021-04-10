# -*- coding: utf-8 -*-
# Função que retorna o dobro de um número qualquer
def dobro(num):
    double = num * 2
    return double
# Seus testes
assert 10 == dobro(5), "o dobro de 5 deve ser 10"



# -*- coding: utf-8 -*-
# Função que retorna o valor da área
def area(lado1, lado2):
    A = lado1 * lado2
    return A
# Seu teste
assert 27 == area(3, 9)



# -*- coding: utf-8 -*-
def antecessor(numero):
    predecessor = numero - 1
    return predecessor

def sucessor(numero):
    successor = numero + 1
    return successor
# Testes
assert antecessor(10) == 9
assert sucessor(10) == 11



# -*- coding: utf-8 -*-
def media(valor1, valor2, valor3):
    return (valor1 + valor2 + valor3)/3
# Seu teste
assert 7 == media(6, 7, 8)



# -*- coding: utf-8 -*-
# Função que retorna o número de dias
#
def dias(n_meses):
    return n_meses * 30
# Seu teste
assert 210 == dias(7)






