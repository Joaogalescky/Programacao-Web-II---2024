# Exercício 06v2 - Verificação de Palíndromo
# Implemente um algoritmo para verificar se uma string é um palíndromo.

# Usando um Loop para Comparação de Extremos
def eh_palindrome(palavra):
    tamanho = len(palavra)
    for i in range(tamanho // 2): # Tamanho // 2 calcula o ponto médio da palavra.
        if palavra[i] != palavra[tamanho - i - 1]:
            return False
    return True


palavra = "radar"
print(f"A palavra é um '{palavra}' palíndromo? {eh_palindrome(palavra)}")

'''
Explicação: A verificação de palíndromo é feita comparando a string original com sua
versão invertida. Se forem iguais, a string é um palíndromo.
'''