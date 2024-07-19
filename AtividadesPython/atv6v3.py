# Exercício 06v3 - Verificação de Palíndromo
# Implemente um algoritmo para verificar se uma string é um palíndromo.

# Comparando com a Versão Reversa (Método Alternativo)
def eh_palindrome(palavra):
    return palavra == ''.join(reversed(palavra))

palavra = "radar"
print(f"A palavra é um '{palavra}' palíndromo? {eh_palindrome(palavra)}")

'''
Explicação: A verificação de palíndromo é feita comparando a string original com sua
versão invertida. Se forem iguais, a string é um palíndromo.
'''