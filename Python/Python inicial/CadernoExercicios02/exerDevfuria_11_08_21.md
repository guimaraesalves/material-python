# Exercício de lógica de programação

## Par ou Ímpar
Crie uma função que descubra se um valor é par ou ímpar.

Neste exercício nós utilizarmos o operador módulo %.

A operação módulo encontra o resto da divisão de um número por outro.

Dados dois números a (o dividendo) e b o divisor, a modulo b (a mod b) é o resto da divisão de a por b.

Por exemplo, 7 mod 3 seria 1, enquanto 9 mod 3 seria 0.

> Portanto sua função deve…
- retornar 1 ou mais caso negativo (é ímpar) e
* retornar 0 caso positivo (é par)
	
```py
	# -*- coding: utf-8 -*-

#
# Função que descobre se um número é par ou ímpar
#
def ehPar(numero):
    if numero % 2 == 0:
		return 0
	else:
		return 1

#
# Testes
#
assert ehPar(8)
assert not ehPar(7)
assert ehPar(0)
```

## Valor positivo ou negativo
Crie uma função que descubra se um valor é positivo ou negativo (considere o valor zero como positivo)

```py
# -*- coding: utf-8 -*-

# Função que descobre se um número é positivo ou negativo
#
# retornará 1 caso positivo
# retornará 0 caso negativo
#
def ehPositivo(numero):
    if numero >= 0:
        return 1
    else:
        return 0


#
# Seus testes
#
assert ehPositivo(100) == 1
assert ehPositivo(0) == 1
assert ehPositivo(-100) == 0
```
## Maior que 10
Crie uma função que descubra se um valor é maior ou menor que 10.

```py 
# -*- coding: utf-8 -*-

# Função que descobre se um número é ou não maior que 10
#
# retornará 1 caso seja maior
# retornará 0 caso seja menor
#
def ehMaiorQue10(valorQualquer):
    if valorQualquer > 10:
        return 1
    else:
        return 0
    

#
# Testes
#
assert 1 == ehMaiorQue10(17)
assert 0 == ehMaiorQue10(9)
``` 

## Conversor Celsius/Fahrenheit

Crie duas funções para conversão de temperaturas.

Uma converterá celsius em fahrenheit e a outra fará o inverso.

Saiba que 100c é igual a 212f, veja fórmula:

> 9 * C° = 5 * F - 160
 
```python
# -*- coding: utf-8 -*-

#
# Converte fahrenheit em celsius
#
def toCelsius(fahrenheit):
    celsius = (5*fahrenheit - 160)/9
    return celsius


# Converte celsius em fahrenheit

def toFahrenheit(celsius):
    fahrenheit = (9*celsius + 160)/5
    return fahrenheit

#
# Testes
#
celsius    = 100
fahrenheit = 212

assert celsius == toCelsius(fahrenheit)
assert fahrenheit == toFahrenheit(celsius)
```

## Equação de 2° grau - bhaskara

Utilizando funções, faça um programa que calcule as raízes da equação do 2 grau conforme a fórmula de Bhaskara.

lembrando:
>ax² + bx + c = 0
> 
> delta = (Δ = b2 - 4.a.c)
> 
>x1    = ( (-b + √Δ)/2a)
>
> x2    = ( (-b - √Δ)/2a)


```python
# -*- coding: utf-8 -*-
import math

#
# Retorna o valor de delta
#
def delta(a, b, c):
    return b**2 - (4*a*c)

#
# Retorna o valor da primeira raiz
#
def raiz1(a, b, c):
    return (-b + math.sqrt(delta(a, b, c))) / 2 * a
    

#
# Retorna o valor da segunda raiz
#
def raiz2(a, b, c):
    return (-b - math.sqrt(delta(a, b, c))) / 2 * a

#
# Testes
#
a = 1
b = 0
c = -16

assert 64 == delta(a, b, c)
assert  4 == raiz1(a, b, c)
assert -4 == raiz2(a, b, c)
``` 


