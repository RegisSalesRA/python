"""
A função delattr() em Python é usada para excluir um atributo de um objeto. Você fornece o objeto e o nome do atributo que deseja excluir, 
e a função remove esse atributo do objeto, se ele existir. Aqui está um exemplo de como usar delattr():
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Alice", 30)

# Imprimindo os atributos antes de excluir
print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)

# Usando delattr() para excluir um atributo
delattr(pessoa, "idade")

# Tentando acessar o atributo após a exclusão
# Isso causará um erro AttributeError
print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)
