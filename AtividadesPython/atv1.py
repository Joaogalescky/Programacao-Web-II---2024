# Exercício 01 - K-esimo menor elemento da lista
# Pegar o k-esimo menor número de uma lista

lista = [2, 48, 15, 6, 7, 5, 7, 8, 9, 32, 12, 15]
print(f"Lista: {lista}")
lista.sort()
print(f"Lista organizada {lista}")

maxPos = len(lista)
numero = int(
    input(f"Digite a posição de um número da lista, entre 0 e {maxPos}: "))
menor = 0

if numero < 1 or numero > maxPos:
    print("Posição inválida, tente novamente!")
else:
    if numero == 1:
        menor = lista[0]
        print(f"O {numero}º menor número da lista é: {menor}")
    else:
        menor = lista[numero - 1]
        print(f"O {numero}º menor número da lista é: {menor}")
