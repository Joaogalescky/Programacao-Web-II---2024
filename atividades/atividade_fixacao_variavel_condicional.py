#Matéria: Programação Web II
#Professor: Herbert Rausch Fernandes
#Aluno: João Vitor Campõe Galescky & Gabriel Alburquerque
#Série: 2° TADS

#Questão 1
#Faça um programa que pergunta para o usuário o tamanho (largura e comprimento) dos lados de uma sala. Após a leitura dos valores, seu programa deve calcular e imprimir a área da sala.

'''
print('Coloque o valor da largura: ')
largura = float(input())

print('Coloque o valor do comprimento')
comprimento = float(input())

print('Processando...')
area = largura * comprimento

print('A área será:', area)
'''

#Questão 2
#Em alguns países os clientes podem ser reembolsados ao entregar garrafas para a reciclagem. O valor reembolsado depende do tamanho da garrafa. Se devolverem garrafas de até 1l eles recebem $0.10 por garrafa. Se devolverem garrafas maiores de 1l, o reembolso é de $0.25.
#Faça um programa em que o usuário entra com dois valores: o primeiro é o número de garrafas menores de 1 litro, o segundo é o número de garrafas maiores. Em seguida calcula e imprime o valor que o usuário será reembolsado.

'''
print('Digite a quantidade de garrafas de até 1 litro:')
qgarrf_ate1l = int(input())

print('Digite a quantidade de garrafas maiores que 1 litro:')
qgarrf_maior1l = int(input())

total = (qgarrf_ate1l * 0.10) + (qgarrf_maior1l * 0.25)
print('O total a ser reembolsado será de R$:', total)
'''

#Questão 3
#É comum dizer que 1 ano humano é equivalente a 7 anos para os cachorros. Contudo, esta simples conversão é um pouco falha. Algumas pessoas acreditam que os 2 primeiros anos "humanos" equivalem a 10.5 anos para os cachorros, após isso, 1 ano "humano" equivale a 4 anos para os cachorros. Por exemplo: Um cachorro de 3 anos equivalem a 25 anos "humanos" (2 * 10.5 + 1 * 4 anos). Um cachorro de 5 anos seria o equivalente a (2 * 10.5 + 3 * 4).
#Faça um programa que leia um número inteiro que é a idade de um cachorro e calcule a idade equivalente para o ser humano.

'''
print('Digite a idade do canino:')
idade_canino = int(input())

if(idade_canino <= 2):
    idade_humana = idade_canino * 10.5
    print('A idade do canino para a idade humana é:', idade_humana)
else:
    idade_humana = (2 * 10.5) + ((idade_canino - 2) * 4)
    print('A idade do canino para a idade humana é:', idade_humana)
'''

#Questão 4
#Faça um programa que leia um número inteiro pelo terminal e imprima qual dia da semana corresponde. Considere que o “domingo” é o dia 1, a “segunda-feira” é o dia 2, e assim por diante.

'''
#def é uma palavra-chave para definir uma função (bloco de código reutilizável)
def dia_da_semana(numero):
    dias_semana = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]
    if numero >= 1 and numero <= 7:
    #[numero - 1] é utilizado para converter o número do dia do mês em um índice válido para acessar a lista 'dias_semana'
        return dias_semana[numero - 1]
    else:
        return "Número inválido"
numero = int(input('Digite um valor de 1 a 7 para saber qual dia da semana corresponde:'))
print("O dia correspondente é:", dia_da_semana(numero))
'''
#Ou
'''
numero = int(input('Digite um número de 1 a 30: '))
dias_semana = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sabado"]
if numero >= 1 and numero <= 30:
    # Usamos o operador % para garantir que o número fique no intervalo de 0 a 6
    indice_dia = (numero - 1) % 7
    print ('O dia correspondente é:', dias_semana[indice_dia])
else:
    print('Número inválido')   
'''     

#Questão 5
#Crie um programa simples que simula uma calculadora básica. O usuário deve inserir dois números e uma operação (adição, subtração, multiplicação ou divisão). O programa deve realizar a operação escolhida e exibir o resultado.

def calculadora(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro! Divisão por zero. "
    else:
        return "Operação inválida"
    
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, - , *, /): ")

resultado = calculadora(num1, num2, operacao)
print("O resultado da operação é:", resultado)