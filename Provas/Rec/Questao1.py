# Aluno: João Vitor Campõe Galescky
# Questão 1 - corrigida
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
        # O valor de i + 1 determina quantos * serão impressos na linha atual. 
        # Por exemplo, na primeira iteração, i é 0 e i + 1 é 1, então apenas um * será impresso; 
        # Na segunda iteração, i é 1 e i + 1 é 2, então dois * serão impressos, e assim por diante.
    print()
