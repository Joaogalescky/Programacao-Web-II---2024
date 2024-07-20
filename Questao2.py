# Aluno: João Vitor Campõe Galescky

# Questão 2
'''
Dada uma matriz de inteiros N×M, escreva um programa que verifique quais números são primos e retorne a uma nova matriz onde os números primos são substituídos por 1 e os não primos por 0.
Exemplo de Entrada:
matriz = [
    [2, 4, 6],
    [7, 8, 9]
]
Exemplo de Saída:
resultado = [
    [1, 0, 0],
    [1, 0, 0]
]
'''

import math

def eh_primo(n):
    if n <= 1:
    	return False
    if n == 2:
    	return True
    if n % 2 == 0:
    	return False
    for i in range(3, int(math.sqrt(n)) + 1,2):
    	if n % i == 0:
   	    return False
    return True

matriz = [[2, 4, 6], [7, 8, 9]]
l1 = len(matriz)
c1= len(matriz[0])
print(f"Matriz:\n {matriz}\n")

matrizSubs = []
for _ in range(l1):
    matrizSubs.append([0] * c1)
print(f"Matriz vazia:\n {matrizSubs}\n")

for i in range(l1):
    for j in range(c1):
        primo = math.sqrt(matriz[i][j])
        if eh_primo(matriz[i][j]):
            matrizSubs[i][j] = 1
        else:
            matrizSubs[i][j] = 0
print(f"Matriz de resposta:\n {matrizSubs}")

