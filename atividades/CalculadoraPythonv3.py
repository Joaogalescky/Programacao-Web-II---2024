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

'''
----- DICIONARIO ------
self = nomenclatura para referenciar o objeto atual da classe
def = definir uma funcao
append = adiciona o elemento digito ao final da pilha
len = retorna o número de itens em um objeto
split = metodo para dividir uma string em uma sequencia de sub-strings
-----------------------
'''

#importando biblioteca para numeros em extenso
from word2number import w2n

#classe 
class CalculadoraPython:
    #metodo construtor da classe

    def __init__(self):
        #pilha vazia
        self.pilha = []

    #metodo para adicionar elemento a pilha
    def empilhar(self, num):

        self.pilha.append(num)

    #metodo para remover elemento da pilha e retornar o elemento do topo da pilha
    def desempilhar(self):
        #verifica se a pilha esta vaiza, caso nao, envia um 'erro'
        if self.esta_vazia():
            raise ValueError("Pilha vazia")
        return self.pilha.pop()

    #metodo que verifica se a pilha esta vazia
    def esta_vazia(self):
        #neste caso, retorna o numero de elementos da lista
        return len(self.pilha) == 0
    #metodo com uma funcao para converter numero por extenso para numero
    def numero_por_extenso(self, numero_por_extenso):
        return w2n.word_to_num(numero_por_extenso)
    
    #metodo principal
    def calcular(self, expressao):
        operacoes = {
            '+': self.adicao,
            '-': self.subtracao,
            '*': self.multiplicacao,
            '/': self.divisao
        }

        #divide a expressao em tokens para avaliar
        tokens = expressao.split()
        #itera sobre os tokens e executa a operacao apropriada e manipula a pilha de acordo        
        for token in tokens:
        #tentar converter o token para numero            
            try:
                #se converter, empilhar
                numero = self.numero_por_extenso(token)
                self.empilhar(numero)
            #caso não converta, tratar como operador
            except ValueError:
                if token in operacoes:
                    operacoes[token]()
                else:
                    raise ValueError("Operação inválida: {}".format(token))
        
        if len(self.pilha) != 1:
            raise ValueError("Expressão inválida")
        return self.desempilhar()
    
    def adicao(self):
        #se pilha menor que dois elementos
        if len(self.pilha) < 2:
            #levanta um alerta de erro
            raise ValueError("Operação inválida: Pilha contém menos de 2 elementos")
        #caso nao, executa expressao
        n2 = self.desempilhar()
        n1 = self.desempilhar()
        self.empilhar(n1 + n2)
    
    def subtracao(self):
        if len(self.pilha) < 2:
            raise ValueError("Operação inválida: Pilha contém menos de 2 elementos")
        n2 = self.desempilhar()
        n1 = self.desempilhar()
        self.empilhar(n1 - n2)

    def multiplicacao(self):
        if len(self.pilha) < 2:
            raise ValueError("Operação inválida: Pilha contém menos de 2 elementos")
        n2 = self.desempilhar()
        n1 = self.desempilhar()
        self.empilhar(n1 * n2)

    def divisao(self):
        if len(self.pilha) < 2:
            raise ValueError("Operação inválida: Pilha contém menos de 2 elementos")
        n2 = self.desempilhar()
        n1 = self.desempilhar()
        if n2 == 0:
            raise ValueError("Divisão por zero")
        self.empilhar(n2 / n1)

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