"""
super() em Python é uma função que é usada em classes para acessar e chamar métodos e atributos das classes pai ou superclasses.
 Ela é frequentemente usada quando uma classe derivada (subclasse) quer estender ou substituir o comportamento de uma classe base (superclasse).

A função super() é geralmente usada no contexto de um método em uma subclasse,
 como o método __init__() de uma subclasse que precisa chamar o __init__() da classe base, além de executar o próprio código adicional da subclasse.
"""

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # Chama o construtor da classe base
        self.raca = raca

    def fazer_som(self):
        return "Au au!"

# Criando uma instância da subclasse Cachorro
cachorro = Cachorro("Buddy", "Golden Retriever")

# Acessando atributos da superclasse usando super()
print("Nome do cachorro:", cachorro.nome)
print("Raça do cachorro:", cachorro.raca)

# Chamando o método da superclasse usando super()
som = cachorro.fazer_som()
print("Som do cachorro:", som)
