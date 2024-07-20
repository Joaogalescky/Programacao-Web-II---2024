# Exercício 01v2 - K-esimo menor elemento da lista
# Implemente uma função para encontrar o k-ésimo menor elemento de uma lista usando o algoritmo Quickselect

def quickselect(lista, k):
    # Se a lista contém apenas um elemento, esse elemento é retornado, pois ele é o único e, portanto, o k-ésimo menor
    if len(lista) == 1:
        return lista[0]

    # O pivô é escolhido como o elemento central da lista. Isso é feito para dividir a lista em três partes: elementos menores, iguais e maiores que o pivô
    pivo = lista[len(lista) // 2] # // operador de divisão inteira
    # elementos menores que o pivô
    esquerda = [x for x in lista if x < pivo] # [nova_lista for elemento in coleção if condição]
    # elementos iguais ao pivô
    meio = [x for x in lista if x == pivo]
    # elementos maiores que o pivô
    direita = [x for x in lista if x > pivo]

    if k < len(esquerda):
        return quickselect(esquerda, k)
    elif k < len(esquerda) + len(meio):
        return meio[0]
    else:
        return quickselect(direita, k - len(esquerda) - len(meio))


lista = [64, 25, 12, 22, 11]
k = int(input("Digite o valor de 'k': "))
k_esimo = quickselect(lista, k-1)
print(k_esimo)

'''
O algoritmo Quickselect é uma variação do Quick Sort que seleciona o k-ésimo
menor elemento dividindo a lista em sublistas e recursivamente procurando na sublista
apropriada.

-- Recursão Baseada na Posição de k --:
Se k for menor que o tamanho da sublista esquerda, isso significa que o k-ésimo menor elemento está na sublista esquerda. 
Portanto, a função é chamada recursivamente com a sublista esquerda e o mesmo k.

Se k for menor que a soma dos tamanhos das sublistas esquerda e meio, isso significa que o k-ésimo menor elemento está na sublista meio (que contém elementos iguais ao pivô). 
Nesse caso, retorna-se o primeiro elemento de meio, pois todos são iguais ao pivô.

Se k for maior ou igual à soma dos tamanhos das sublistas esquerda e meio, isso significa que o k-ésimo menor elemento está na sublista direita. 
Portanto, a função é chamada recursivamente com a sublista direita e um k ajustado (subtraído do tamanho das sublistas esquerda e meio).
--------------------------------------

-- Encontrar o pivô --:
Iteração 1:

x é 64.
Verifica-se a condição 64 == 25 (falso), então 64 não é adicionado à nova lista.
Iteração 2:

x é 25.
Verifica-se a condição 25 == 25 (verdadeiro), então 25 é adicionado à nova lista.
Iteração 3:

x é 12.
Verifica-se a condição 12 == 25 (falso), então 12 não é adicionado à nova lista.
Iteração 4:

x é 22.
Verifica-se a condição 22 == 25 (falso), então 22 não é adicionado à nova lista.
Iteração 5:

x é 11.
Verifica-se a condição 11 == 25 (falso), então 11 não é adicionado à nova lista.

Após todas as iterações, a nova lista meio será:
25
--------------------------------------

'k' significa que queremos encontrar o (input) do menor elemento (one-based index). Como o índice da lista é zero-based, passamos k - 1 (ou seja, 2) para a função quickselect.
'''
