#Para organizar uma lista em ordem crescente começando com números pares e terminando com ímpares, você pode usar a função sorted() junto com uma função de chave personalizada. Aqui está um exemplo:

'''
def ordenar_pares_impares(lista):
    #compreensao de lista
    pares = sorted([x for x in lista if x % 2 == 0])
    #sorted = ordenando os elementos filtrados em ordem crescente
    impares = sorted([x for x in lista if x % 2 != 0])
    return pares + impares

# Exemplo de uso:
lista = [3, 6, 8, 1, 4, 5, 7, 2]
resultado = ordenar_pares_impares(lista)
print("Lista ordenada com números pares no início e ímpares no final:", resultado)
'''

#Para organizar uma lista em ordem crescente começando com números pares e terminando com ímpares sem usar bibliotecas, você pode percorrer a lista e mover os números pares para a esquerda e os ímpares para a direita. Aqui está um exemplo de como fazer isso:

def ordenar_pares_impares(lista):
    i = 0
    j = len(lista) - 1

    while i < j:
        #se for par ou impar
        if lista[i] % 2 != 0 and lista[j] % 2 == 0:
            #se lista[i] for impar, trocar valor da posicao com a lista[j]
            lista[i], lista[j] = lista[j], lista[i]
            #'i' começa apontando para o primeiro elemento da lista
            i += 1
            #'j' começa apontando para o ultimo elemento da lista
            j -= 1
        elif lista[i] % 2 == 0:
            i += 1
        elif lista[j] % 2 != 0:
            j -= 1
    
    return lista

# Exemplo de uso:
lista = [3, 6, 8, 1, 4, 5, 7, 2]
resultado = ordenar_pares_impares(lista)
print("Lista ordenada com números pares no início e ímpares no final:", resultado)
