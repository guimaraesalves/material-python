def ehPar(numero):
    if numero % 2 == 0:
        return print('é par.')
    else:
        return print('é impar')

#
# Testes
#
ehPar(0)


def ehPositivo(n):
    if n >= 0:
        return print('Positivo')
    else:
        return print('Negativo')

ehPositivo(-7)

def ehmaiorQ10(valor):
    if valor > 10:
        return print('Valor maior que 10.')
    else:
        return print('Valor menor que 10.')

ehmaiorQ10(8)

def toCelsius(f):
    Celsius = (5*f - 160)/9
    return print(f'{f} Fahrenheit é {Celsius} °C.')


def toFahrenheit(c):
    Fahrenheit = (9*c + 160)/5
    return print(f'{c} °C em Fahrenheit é {Fahrenheit}.')

toCelsius(212)
toFahrenheit(30)



# Equação do 2° grau - Bhaskara
from math import sqrt

a = float(1)
b = float(0)
c = float(-16)


def delta(a, b, c):
    return (b**2 - 4 * a * c)


def x1(a, b, c):
    x = (-b + sqrt(delta(a, b, c))) / 2 * a

    return print('x1 = ', x)


def x2(a, b, c):
    y = (-b - sqrt(delta(a, b, c))) / 2 * a
    return print('x2 = ', y)



print(delta(a, b, c))

x1(a, b, c)
x2(a, b, c)



# LISTA DE EXERCÍCIOS NÍVEL 3

