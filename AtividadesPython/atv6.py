# Exercício 06 - Verificação de Palíndromo
# Implemente um algoritmo para verificar se uma string é um palíndromo.

def eh_palindrome(palavra):
    return palavra == palavra[::-1]  # [start:stop:step]
# : - significa que está selecionando toda a sequência
# : - permite especificar um passo para o slicing ([start:stop:step])
# -1 - é o passo, indica que a sequência deve ser percorrida de trás para frente


palavra = "radar"
print(f"A palavra é um '{palavra}' palíndromo? {eh_palindrome(palavra)}")

'''
Explicação: A verificação de palíndromo é feita comparando a string original com sua
versão invertida. Se forem iguais, a string é um palíndromo.
'''
