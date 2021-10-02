"""
POO - Heranca

A ideia de heranca e a de reaproveitar codigo. tambem extender nossas classes

OBS: Com a heranca, a partir de uma classe existente, nos extendemos outra classe
que passa a herdar atributos e metodos de classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Perguntar: Existe alguma entidade generica o suficiente para encapsular os atributos
e metodos comuns a outras entidades?


OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e metodos da classe herdada

Quando uma classe herda de outra classe, a classe herdada e conhecida por:
    [Pessoa]
    - Super Classe:
    - Classe Mae;
    - Classe Pai;
    - Classe Base;
    - Classe Generica;

Quando uma classe herda de outra classe, ela e chamada:
    [Cliente, Funcionario]
    - Sub class;
    - Classe Filha;
    - Classe espefifica;


# Sobrescrita de metodos

Sobrescrita de metodo, ocorre quando reescrevemos um metodo presente na super classe em classes filhas
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # FOrma comumde acessar os dados
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self,nome, sobrenome,cpf) # Forma nao comum de acessar os dados
        self.__matritula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        return f'Funcionario:{self.__matritula} Nome: {self._Pessoa__nome}'

cliente1 = Cliente('Angelina', 'Jolie', '123.123.321.123', 5000)
funcionario1 = Funcionario('Felicy', 'jones', '123.132.333.523', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)