# Exercício 05 - Ordenação por Inserção
# Implemente o algoritmo de ordenação por inserção (Insertion Sort) e ordene a lista [64, 25, 12, 22, 11].

def insertion_sort(lista):
    for i in range(1, len(lista)):
        # Guarda o valor do elemento atual
        key = lista[i]
        # Inicializa a variável 'j' como o índice do elemento anterior
        j = i - 1
        # Move os elementos da lista que são maiores que 'key' uma posição à frente
        # para abrir espaço para 'key'
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        # Coloca 'key' na posição correta
        lista[j + 1] = key
    return lista


lista = [64, 25, 12, 22, 11]
sortedLista = insertion_sort(lista)
print(sortedLista)

'''
Explicação: O algoritmo de ordenação por inserção constrói a lista ordenada um elemento
por vez, inserindo cada novo elemento na posição correta em relação aos já ordenados.
'''

'''
O algoritmo de ordenação por inserção (Insertion Sort) funciona de forma semelhante ao modo como você organizaria um baralho de cartas na mão. 
Ele constrói a lista ordenada um elemento por vez, sempre inserindo o próximo elemento na posição correta em relação aos elementos já ordenados. 
'''

'''
Comparação e Deslocamento:
j = i - 1
A variável j é inicializada como o índice do elemento imediatamente anterior ao key.
while j >= 0 and key < lista[j]:
O loop while continua enquanto j é um índice válido (não negativo) e key é menor que lista[j]. Se key for menor que lista[j], significa que lista[j] precisa ser movido uma posição à frente.
lista[j + 1] = lista[j]
Move lista[j] uma posição à frente.
j -= 1
Decrementa j para continuar comparando com os elementos anteriores na sublista ordenada.
'''

'''
Funcionamento com um Exemplo:
Vamos ver um exemplo para entender melhor:

Lista Original: [4, 3, 2, 10, 12, 1, 5, 6]

Iteração 1 (i = 1):

key = 3, j = 0
Comparação: 3 < 4, então move 4 para frente.
Lista: [4, 4, 2, 10, 12, 1, 5, 6]
Insere key: [3, 4, 2, 10, 12, 1, 5, 6]
Iteração 2 (i = 2):

key = 2, j = 1
Comparações: 2 < 4, move 4 para frente; 2 < 3, move 3 para frente.
Lista: [3, 3, 4, 10, 12, 1, 5, 6], depois [2, 3, 4, 10, 12, 1, 5, 6]
Iteração 3 (i = 3):

key = 10, j = 2
Comparações: 10 não é menor que 4, então insere key diretamente.
Lista permanece: [2, 3, 4, 10, 12, 1, 5, 6]
Iteração 4 (i = 4):

key = 12, j = 3
Comparações: 12 não é menor que 10, então insere key diretamente.
Lista permanece: [2, 3, 4, 10, 12, 1, 5, 6]
Iteração 5 (i = 5):

key = 1, j = 4
Comparações: 1 < 12, move 12 para frente; 1 < 10, move 10 para frente; 1 < 4, move 4 para frente; 1 < 3, move 3 para frente; 1 < 2, move 2 para frente.
Lista: [2, 2, 3, 4, 10, 12, 5, 6], depois [1, 2, 3, 4, 10, 12, 5, 6]
Iteração 6 (i = 6):

key = 5, j = 5
Comparações: 5 < 12, move 12 para frente; 5 < 10, move 10 para frente.
Lista: [1, 2, 3, 4, 10, 10, 12, 6], depois [1, 2, 3, 4, 5, 10, 12, 6]
Iteração 7 (i = 7):

key = 6, j = 6
Comparações: 6 < 12, move 12 para frente; 6 < 10, move 10 para frente.
Lista: [1, 2, 3, 4, 5, 10, 10, 12], depois [1, 2, 3, 4, 5, 6, 10, 12]
A lista está agora ordenada: [1, 2, 3, 4, 5, 6, 10, 12].

O Insertion Sort é eficiente para listas pequenas ou listas que já estão parcialmente ordenadas, 
mas pode ser ineficiente para listas grandes ou em ordem inversa, com complexidade de tempo de 𝑂(𝑛²) no pior caso.
'''