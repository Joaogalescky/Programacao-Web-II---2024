def sao_anagramas(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    
    contagem_caracteres = [0] * 26  # Criando uma lista para contar a frequência de cada letra do alfabeto
    
    # Contando a frequência de cada letra na primeira palavra
    for letra in palavra1:
        indice = ord(letra) - ord('a')  # Convertendo a letra para um índice na lista (0 a 25)
        contagem_caracteres[indice] += 1
    
    # Subtraindo a frequência de cada letra na segunda palavra
    for letra in palavra2:
        indice = ord(letra) - ord('a')
        contagem_caracteres[indice] -= 1
        
        # Se a contagem for negativa, significa que a segunda palavra tem uma letra que não está na primeira palavra
        if contagem_caracteres[indice] < 0:
            return False
    
    # Se todas as contagens forem zero, as palavras são anagramas
    return all(count == 0 for count in contagem_caracteres)

# Exemplo de uso:
palavra1 = "listen"
palavra2 = "silent"

if sao_anagramas(palavra1, palavra2):
    print(f"'{palavra1}' e '{palavra2}' são anagramas.")
else:
    print(f"'{palavra1}' e '{palavra2}' não são anagramas.")