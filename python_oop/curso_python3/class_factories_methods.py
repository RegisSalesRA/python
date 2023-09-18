"""
# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
"""


"""
Pra ter acesso a propria classe sem ter self sem ter que uma instancia da classe
criar o metodo na propria classe acesso a propria classe no primeiro parametro e usar do segundo em diante
"""

class Pessoa:
    ano = 2023

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("Ola")
    
    @classmethod
    def criar_com_50_anos(cls,name):
        return cls(name, 50)

    @classmethod
    def criar_sem_nome(cls,idade):
        return cls('Anonima', idade)
    
    
p1 = Pessoa('Joao', 34)
p2 = Pessoa.criar_com_50_anos("Helena")
p3 = Pessoa("Anonima",23)
p4 = Pessoa.criar_sem_nome(23)
print(p2.nome, p2.idade)
print(p4.nome, p4.idade)