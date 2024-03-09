'''
Para identificar a moda de uma lista, você pode usar o módulo collections da biblioteca padrão do Python. Aqui está um exemplo de como fazer isso:
'''

'''
#importando biblioteca
from collections import Counter

#funcao
def Moda(lista):
    #Counter = contar a quantidade de ocorrencias de um determinado elemento em uma lista
    contagem = Counter(lista)
    #most_common = retorna o valor mais comum entre os discretos e nominais na lista
    modaValor = contagem.most_common(1)[0][0]
    return modaValor

lista = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
resultado = Moda(lista)
print("A moda da lista é:", resultado)
'''

'''
Para identificar a moda de uma lista sem usar bibliotecas, você pode percorrer a lista e contar a frequência de cada elemento. Aqui está um exemplo de como fazer isso:
'''

#metodo
def moda(lista):
    contagem = {}
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    
    modaValor = None
    modaFrequencia = 0
    for chave, valor in contagem.items():
        if valor > modaFrequencia:
            modaValor = chave
            modaFrenquencia = valor
    
    return modaValor

lista = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
resultado = moda(lista)
print("A moda da lista é:", resultado)