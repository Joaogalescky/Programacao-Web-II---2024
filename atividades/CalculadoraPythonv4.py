from word2number import w2n

#classe
class CalculadoraPython:
    #metodo construtor da classe
    def __init__(self):
        self.pilha = []

    #metodo de empilhar
    def empilhar(self, num):
        self.pilha.append(num)

    #metodo de desempilhar
    def desempilhar(self):
        if not self.pilha:
            raise ValueError('Pilha vazia')
        return self.pilha.pop()
    
    #metodo para converter string para numero
    def numero_por_extenso(self, numero_por_extenso):
        return w2n.word_to_num(numero_por_extenso)
    
    #metodo principal
    def calcular(self, expressao):
        tokens = expressao.split()
        for token in tokens:
            try:
                numero = self.numero_por_extenso(token)
                self.empilhar(numero)
            except ValueError:
                if token in ['+', '-', '*', '/']:
                    if len(self.pilha) < 2:
                        raise ValueError('Operação inválida: Pilha contém menos de 2 elementos')
                    n2 = self.desempilhar()
                    n1 = self.desempilhar()
                    if token == '+':
                        resultado = n1 + n2
                    elif token == '-':
                        resultado = n1 - n2
                    elif token == '*':
                        resultado = n1 * n2
                    else:
                        if n2 == 0:
                            raise ValueError('Divisão por zero')
                        resultado = n1 / n2
                    self.empilhar(resultado)
                else:
                    raise ValueError('Operação inválida: {}'.format(token))
            if len(self.pilha) != 1:
                raise ValueError('Expressao inválida')
            return self.desempilhar()