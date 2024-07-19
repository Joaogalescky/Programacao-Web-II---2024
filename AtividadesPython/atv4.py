# Exercício 04 - Ordenação por Seleção
# Implemente o algoritmo de ordenação por seleção (Selection Sort) e ordene a lista [64, 25, 12, 22, 11]

def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j
        # trocam = arr[i] assume arr[min_idx] e arr[min_idx] assume arr[i]
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


lista = [64, 25, 12, 22, 11]
sortedArr = selection_sort(lista)
print(sortedArr)

'''
Explicação: O algoritmo de ordenação por seleção encontra o menor elemento da lista e o
coloca na posição inicial, repetindo o processo para os subsequentes até que a lista esteja
ordenada.
'''
