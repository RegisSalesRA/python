"""
classmethod() é um decorador em Python que é usado para definir um método de classe.
 Um método de classe é um método que está associado à classe em vez de uma instância específica dessa classe.
   Isso significa que ele pode ser chamado na classe em si,
 sem a necessidade de criar uma instância da classe. Vou mostrar um exemplo de como usar classmethod():
"""


class MinhaClasse:
    atributo_de_classe = "Sou um atributo de classe"

    def __init__(self, valor):
        self.valor = valor

    @classmethod
    def metodo_de_classe(cls, x):
        print(f"Chamado método de classe com {x}")
        print(f"Atributo de classe: {cls.atributo_de_classe}")

# Criando uma instância da classe
objeto = MinhaClasse("Objeto 1")

# Chamando o método de classe usando a instância
objeto.metodo_de_classe(42)

# Chamando o método de classe diretamente na classe
MinhaClasse.metodo_de_classe(100)
