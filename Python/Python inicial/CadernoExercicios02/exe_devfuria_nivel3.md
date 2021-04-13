# Lista de Exercícios nível 3
## Exercícios para treinar laços de repetição.

# Número primo
Exercício de lógica de programação para descobrir se um número é primo.

Faça um programa para identificar se um número é primo.

Lembre-se que número primo, é um número natural, maior que 1, apenas divisível por si próprio e pela unidade.


> Comentários:
>
>Os problemas (e as soluções) envolvendo os números primos são fascinantes e não é objetivo deste artigo esgotar o assunto, muito pelo contrário, o objetivo é simplesmente ser a porta de entrada, o primeiro degrau.
>
>Outro ponto a comentar é a questão dos testes, você verá que é difícil determinar o quanto de testes seriam suficientes para garantir o correto funcionamento do algoritmo.

 ```python
# -*- coding: utf-8 -*-

#
# Função que descobre se o número é ou não primo.
#
def ehPrimo(num):
    s = 0
    for i in range(num):
        if num % i == 0:
            s = s + 1
        if s > 2:
            return print("Não é primo")
        else:
            return print('É primo')

#
# Testes
#

assert ehPrimo(2)
assert ehPrimo(3)
assert ehPrimo(5)
assert ehPrimo(7)
assert ehPrimo(11)
assert ehPrimo(13)

assert not ehPrimo(4)
assert not ehPrimo(6)
assert not ehPrimo(8)
assert not ehPrimo(9)
assert not ehPrimo(10)
assert not ehPrimo(12)
```
>Agora se quisermos partir para uma solução um pouco mais pythonica, que tal…
```python
def ehPrimo(num):
    if num < 2:
        return False
    else:
        for n in range(2, num):
            if num % n == 0:
               return False
        return True
``` 

# Algoritmo para somar vetor

Exercício de lógica de programação onde criaremos uma função para somar um vetor.

```python
# -*- coding: utf-8 -*-

#
# Seu código
#
def somarLista(lista):
    soma = 0
    for n in lista:
        soma += n
    return soma

#
# Seu teste
#
lista = [10, 20, 30, 0]
assert 60 == somarLista(lista)
```
# MDC máximo divisor comum

Faça um programa para calcular o MDC (máximo divisor comum) entre dois números.

Aconselho a utilizar o método de divisões sucessivas, pois você verá que a forma como costumamos resolver problemas matemáticos na mão nem sempre é o melhor caminho quando estamos codificando.

```python
# -*- coding: utf-8 -*-

#
# Função que calcula o MDC entre dois números
#
def mdc(num1, num2):
    pass

#
# Testes
#
assert 3 == mdc(24, 9)
assert 10 == mdc(30, 20)
```