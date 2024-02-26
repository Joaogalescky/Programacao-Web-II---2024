'''
QUESTÃO 1 
Neste trabalho você deve implementar uma calculadora de pilha. Ou seja, para cada elemento da operação aritmética deve-se empilhar. Cada operação aritmética ( +, - , * , / ) é realizada com os dois elementos do topo da pilha, os quais são desempilhados. Além disso, o resultado da operação aritmética é empilhado.

O programa deve conter as seguintes ações:
“+”: efetua a operação de adição com os dois elementos do topo da pilha e empilha o resultado.
“-”: efetua a operação de subtração com os dois elementos do topo da pilha e empilha o resultado.
“*”: efetua a operação de multiplicação com os dois elementos do topo da pilha e empilha o resultado.
“/”: efetua a operação de divisão com os dois elementos do topo da pilha e empilha o resultado.


Além das operações acima o seu programa deverá realizar o tratamento de:

Conversão de texto para número;

Divisão por zero, e;

Pilha vazia.
'''

#importando biblioteca para numeros em extenso
from word2number import w2n

#classe 
class CalculadoraPython:
    #metodo construtor da classe
    #def = definir uma funcao
    #self = nomenclatura para referenciar o objeto atual da classe
    def __init__(self):
        #pilha vazia
        self.pilha = []

    #metodo para adicionar elemento a pilha
    def empilhar(self, num): #push
        #append = adiciona o elemento digito ao final da pilha
        self.pilha.append(num)

    #metodo para remover elemento da pilha e retornar o elemento do topo da pilha
    def desempilhar(self): #pop
        #verifica se a pilha esta vaiza, caso nao, envia um 'erro'
        if self.esta_vazia():
            raise ValueError("Pilha vazia")
        return self.pilha.pop()

    #metodo que verifica se a pilha esta vazia
    def esta_vazia(self):
        #len = retorna o número de itens em um objeto
        #neste caso, retorna o numero de elementos da lista
        return len(self.pilha) == 0
    
    #metodo com uma funcao para converter numero por extenso para numero
    def numero_por_extenso(self, numero_por_extenso):
        return w2n.word_to_num(numero_por_extenso)
    
    #metodo principal
    def calcular(self, expressao):
        #divide a expressao em tokens para avaliar
        tokens = expressao.split()
        #split = metodo para dividir uma string em uma sequencia de sub-strings
        #itera sobre os tokens e executa a operacao apropriada e manipula a pilha de acordo
        for token in tokens:
            try:
                #tentar converter o token para numero
                numero = self.numero_por_extenso(token)
                #se converter, empilhar
                self.empilhar(numero)
            #caso não converta, tratar como operador
            except ValueError:
                if token == '+':
                    #se pilha menor que dois elementos
                    if len(self.pilha) < 2:
                    #alerta de erro
                        raise ValueError("Operação inválida: Pilha contém menos de 2 elementos")
                    #caso nao, executa expressao
                    num2 = self.desempilhar()
                    num1 = self.desempilhar()
                    self.empilhar(num1 + num2)
                elif token == '-':
                    if len(self.pilha) < 2:
                        raise ValueError("Operação inválida: Pilha contém menos de 2 elementos")
                    num2 = self.desempilhar()
                    num1 = self.desempilhar()
                    self.empilhar(num1 - num2)
                elif token == '*':
                    if len(self.pilha) < 2:
                        raise ValueError("Operação inválida: Pilha contém menos de 2 elementos")
                    num2 = self.desempilhar()
                    num1 = self.desempilhar()
                    self.empilhar(num1 * num2)
                elif token == '/':
                    if len(self.pilha) < 2:
                        raise ValueError("Operação inválida: Pilha contém menos de 2 elementos")
                    num2 = self.desempilhar()
                    num1 = self.desempilhar()
                    #alerta de erro
                    if num2 == 0:
                        raise ValueError("Divisão por zero")
                    self.empilhar(num1 / num2)
                #alerta de erro
                else:
                    raise ValueError("Operação inválida: {}".format(token))
            #caso haja algum valor na pilha apos uma operacao
            if len(self.pilha) != 1:
                #alerta de erro
                raise ValueError("Expressão inválida")
            return self.desempilhar()

#instanciando a calculadora
calculadora = CalculadoraPython()

#loop para entrada do usuário
while True:
    expressao = input("Digite uma expressão (ou 'p' para parar): ")
    #tranforma entrada em letra minuscula (lower), caso 'p', finaliza o codigo
    if expressao.lower() == 'p':
        break
    try:
        #caso não 'p', continua o codigo
        resultado = calculadora.calcular(expressao)
        print("Resultado:", resultado)
    #alerta de erro para excecoes
    except ValueError as e:
        print("Erro:", e)
    #apos um erro e a pilha nao estiver vazia, esvaziar
    finally:
        while not calculadora.esta_vazia():
            calculadora.desempilhar()