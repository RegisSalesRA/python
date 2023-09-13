"""
POO - Metodos

- Metodos (funcoes) -> Representam os comportamentos do objeto. Ou seja, as acoes
que este objeto pode realizar no seu sistema

Em python , dividimos os metodos, em 2 grupos, Metodos de instancia
E metodos de Classe

# Metodos de instancia

# O metodo dunder init __init__ e um metodo especial chamado de construtor e sua funcao
e construir o objeto a partir da classe

OBS: Todo elemento em python que inicia e finaliza com duplo underline e chamado de dunder (Double Underline)

OBS: Os metodos  dunder em python sao chamados de metodos magicos
"""


class Lampada:

    def __index__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:
    contador = 4999

    def __index__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    produto_id = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.produto_id + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.produto_id = self.__id

    def desconto(self, porcentagem):
        """REtorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    def __index__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha


p1 = Produto('Playstation4', 'Video Game', 100)
print(p1.desconto(10))
