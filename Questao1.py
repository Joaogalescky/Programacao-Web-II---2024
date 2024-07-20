# Aluno: João Vitor Campõe Galescky
# Questão 1
'''
Escreva um programa que, dado um número inteiro N, desenhe um triângulo de asteriscos de altura N.
Exemplo de Entrada:
N = 5
Exemplo de Saída:
*
**
***
****
*****
'''

N = int(input("Digite um número inteiro para a altura do triângulo: "))

for i in range(N): # altura
    for j in range(i + 1): # comprimento
        print("*", end = " ") # juntar com o outro print, após o 1
    print()
