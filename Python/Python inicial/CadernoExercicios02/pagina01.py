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


# Lista de Exercícios Nível 1

# Funções para as quatros operações matemáticas
# -*- coding: utf-8 -*-

# as funções são tão pequenas e tão concisas
# que nem precisam de comentários

def somar(num, add):
    return num + add

def subtrair(num, sub):
    return num - sub

def multiplicar(num, mult):
    return num * mult

def dividir(num, divisor):
    return num / divisor

#
# Testes
#
assert 12 == somar(10, 2)
assert 8 == subtrair(10, 2)
assert 20 == multiplicar(10, 2)
assert 5 == dividir(10, 2)


 # -*- coding: utf-8 -*-

#
# Retorna o custo final da fabricação de um carro
#
def custoFinal(n):
    custoFabrica = 10000.00
    perceDistribuidor = (0.28 * 10000)
    percImpostos = (0.45 * 10000)
    return custoFabrica + perceDistribuidor + percImpostos

#
# Teste
#
assert 17300 == custoFinal(10000), "'custoFinal' deve ser igual a 17300"



'''
Faça um programa para calcular o juros simples segundo a fórmula abaixo.

J = C.i.n
Onde:
J = juros,
C = capital,
i = taxa de empréstimo
n = períodos

Vamos imaginar o seguinte cenário: um empréstimo de R$ 16000.00 sobre a taxa de 4% durante 4 meses.

'''

def juros_simples(c, i, n):
    j = c * i * n
    return j


assert 2560 == juros_simples(16000, 0.04, 4), "juros de ser igual a 2560"

'''
Faça um algoritmo que calcule o reajuste de um salário, utilize os seguintes dados:
salário = 1000.00
reajuste = 15%

'''

def reajustar_salario(sal, reaj):
    return sal * reaj

assert  150 == reajustar_salario(1000, 0.15), 'reajustar_salario de retornar 150'

# Lista de Exercícios Nível 2

