# Exercício 02 - Elemento que mais se repete
# Lista para procurar o número que mais se repete
lista = [1, 5, 6, 7, 8, 5, 6, 5, 6, 12, 15, 98, 1, 2]
listaContadora = []  # lista para guardar a quantidade de vezes que aparece um número
maior = 0  # contador

for i in range(len(lista)):  # percorre a lista
    listaContadora.append(0)
    # percorre a lista inteira, comparando com o valor selecionado do for de cima
    for j in range(len(lista)):
        if lista[i] == lista[j]:
            # armazena na listaContadora a quantidade de vezes que aparece o número
            listaContadora[i] += 1

listaContadora.sort()  # .sort() vai ordenar de forma crescente
maior = listaContadora[-1] - 1  # guarda a posição do número que mais aparece

print(f"lista original: {lista}")
print(f"lista contadora: {listaContadora}")
print(f"O número que mais se repete é: {lista[maior]}")
