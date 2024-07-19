# Exercício 07 - Ordenação Rápida
# Implemente o algoritmo de ordenação rápida (Quick Sort) e ordene a lista [64, 25, 12, 22, 11]

# Ordenar Recursivamente: Aplica o QuickSort recursivamente às sublistas esquerda e direita.
def quick_sort(lista):
    # Se a lista contém apenas um elemento, esse elemento é retornado
    if len(lista) <= 1:
        return lista
    # Escolher um Pivô: Seleciona um elemento da lista para ser o pivô.
    pivo = lista[len(lista) // 2]
    # Particionar a Lista: Divide a lista em duas sublistas
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    # Combinar: Junta as sublistas ordenadas e o pivô para formar a lista ordenada final.
    return quick_sort(esquerda) + meio + quick_sort(direita)


lista = [64, 25, 12, 22, 11]
sorted_lista = quick_sort(lista)
print(sorted_lista)

'''
O algoritmo de ordenação rápida divide a lista em três partes
(menores que o pivô, igual ao pivô e maiores que o pivô) e recursivamente ordena as sublistas.
'''
