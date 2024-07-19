# Exercício 03
# Pegar uma lista e colocar os pares antes dos impares, ou vice-versa

lista = [2, 5, 7, 9, 1, 6, 4, 12, 15, 17, 19, 18, 25, 24, 32, 84, 97]
listaPar = []
listaImpar = []

for numero in lista:
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)

listaParesOrdenada = listaPar + listaImpar
listaImparesOrdenada = listaImpar + listaPar
print(f"lista normal: {lista}\nlista com pares na frente: {
      listaParesOrdenada}\nlista com impares na frente: {listaImparesOrdenada}")
