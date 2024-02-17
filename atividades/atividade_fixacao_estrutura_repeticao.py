#Matéria: Programação Web II
#Professor: Herbert Rausch Fernandes
#Aluno: João Vitor Campõe Galescky & Gabriel Alburquerque
#Série: 2° TADS

#Questão 1
#Crie um programa que lê três valores e imprime os valores ordenados (do menor para o maior).

'''
# Leitura dos valores
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

# Ordenação dos valores
#min e max são funções que retornam o menor e o maior valor pelos argumentos fornecidos
menor = min(a, b, c)
maior = max(a, b, c)
#subtrai-se o 'menor' valor e o 'maior' pela soma dos três argumentos para encontrar o valor do 'meio'
meio = (a + b + c) - menor - maior

# Saída ordenada
print("Valores ordenados:", menor, meio, maior)
'''

#Questão 2
#Faça um programa que leia 'n' números inteiros digitados pelo usuário e calcula a média desses valores.  O usuário entrará o valor 0 para interromper o procedimento de entrad ade valores. Dessa forma, o valor 0 não deve ser condiserado para o cálculo da média.

'''
soma = 0
contador = 0

while True:
    valor = int(input("Digite um número inteiro (0 para parar): "))
    if valor == 0:
        break
    soma += valor
    contador += 1

if contador == 0:
    print("Nenhum número foi inserido.")
else:
    media = soma / contador
    print("Média dos valores digitados:", media)
'''

#Questão 3
#O 'n-ésimo' termo da sequência de Fibonacci é calculado pela função de recursão: F(n) = F(n-2) + F(n-1)
# Faça um programa que lê um número inteiro 'n' e calcula o 'n-ésimo' termo da sequência de Fibonacci sem utilizar função de recursividade. Considera F(0) = 0 e F(1) = 1.

'''
n = int(input("Digite o valor de n: "))

#O fibonacci começa em 0 e 1 pois são valores fixos
fibonacci = [0, 1]
#O for itera 2 em 2 para começar a sequência e calcular os termos adicionais da sequência, já que 0 e 1 já foram os primeiros termos
for i in range(2, n + 1):
#Para cada próximo termo da sequência de fibonacci, soma-se dois valores anteriores e adiciona-se o resultado à lista
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
print("O", n, "-ésimo termo da sequência de Fibonacci é:", fibonacci[n])
'''

#Questão 4
#Escreva um programa que solicita ao usuário para inserir um número inteiro positivo. O programa dever estão gerar e exibir um lista de todos números pares no intervalo de 1 até o número inserido pelo usuário, utilizando um loop. Em seguinda, o programa deve calcular e exibir a soma de todos os números pares na lista. Lide com casos em que o usuário insere um número negativo ou zero, exibindo uma mensagem apropriada.

'''
numero = int(input("Digite um número inteiro positivo: "))

if numero <= 0:
    print("O número deve ser positivo.")
else:
    #lista_pares é uma compreensão de lista ond epercorre todos os números no intervalo de 1 até 'numero', criando uma lista contendo todos os números pares no intervalo de 1 até 'numero'.
    lista_pares = [i for i in range(1, numero + 1) if i % 2 == 0]
    #sum(lista_pares) é uma função de soma de todos os itens de uma sequência fornecida
    soma_pares = sum(lista_pares)
    print("Lista de números pares:", lista_pares)
    print("Soma dos números pares:", soma_pares)
'''

#Questão 5
#Você recebeu uma lista contendo números inteiros. Sua tarefa é escrever um programa para calcular a soma dos elemetnos únicos na lista.

'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10]  # Exemplo de lista de números inteiros

soma_elementos_unicos = sum(set(lista))
print("A soma dos elementos únicos na lista é:", soma_elementos_unicos)
'''
