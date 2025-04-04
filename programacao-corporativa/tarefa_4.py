# -*- coding: utf-8 -*-
"""tarefa_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/181fDqZPY3JHAoj-vHzBxyPOW9EwzF0c-

Atividade 1
"""

# Função
def imprimir_menor(a, b):
    if a < b:
        print(f"O menor valor é: {a}")
    elif b < a:
        print(f"O menor valor é: {b}")
    else:
        print("Os valores são iguais")

# Entrada
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Saída
imprimir_menor(valor1, valor2)

"""Atividade 2"""

# Função
def verificar_positivo_negativo(n):
    if n > 0:
        print(f"{n} é positivo.")
    elif n < 0:
        print(f"{n} é negativo.")
    else:
        print("O número é zero.")

# Entrada
numero = float(input("Digite um número: "))

# Saída
verificar_positivo_negativo(numero)

"""Atividade 3"""

# Função
def verifica_soma_limite():
    # Entrada
    a = float(input("Digite o primeiro número (a): "))
    b = float(input("Digite o segundo número (b): "))
    limite = float(input("Digite o valor limite: "))

    # Cálculo
    if (a + b) > limite:
        print(f"A soma de {a} + {b} = {a+b} é MAIOR que {limite} (True)")
        return True
    else:
        print(f"A soma de {a} + {b} = {a+b} é MENOR ou IGUAL a {limite} (False)")
        return False

# Saída
verifica_soma_limite()

"""Atividade 4"""

# Função
def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)

# Entrada
n = int(input("Digite um número inteiro: "))

# Saída
fizzbuzz(n)

"""Atividade 5"""

# Função
def numero_na_lista(lista, numero):
    return numero in lista

# Entrada
entrada_lista = input("Digite os números da lista separados por espaço: ")
numeros = [int(num) for num in entrada_lista.split()]
alvo = int(input("Digite o número a ser verificado: "))

# Saída
resultado = numero_na_lista(numeros, alvo)
print(f"O número {alvo} está na lista? {resultado}")

"""Atividade 6"""

# Função
def soma_inteiros_positivos(n):
    return sum(range(1, n + 1))

# Entrada
n = int(input("Digite um número inteiro positivo: "))

# Saída
if n > 0:
    resultado = soma_inteiros_positivos(n)
    print(f"A soma de todos os inteiros positivos até {n} é: {resultado}")
else:
    print("Por favor, digite um número inteiro positivo.")