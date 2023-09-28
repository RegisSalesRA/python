"""
A função setattr() em Python é usada para definir o valor de um atributo de um objeto.
 Ela aceita três argumentos: o objeto ao qual você deseja definir o atributo,
 o nome do atributo que você deseja definir e o valor que você deseja atribuir a esse atributo.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Alice", 30)

# Definindo um novo atributo chamado "cidade" com o valor "Nova York"
setattr(pessoa, "cidade", "Nova York")

# Acessando o novo atributo
print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)
print("Cidade:", getattr(pessoa, "cidade"))

# Alterando o valor do atributo "cidade"
setattr(pessoa, "cidade", "Los Angeles")

# Acessando o valor atualizado do atributo "cidade"
print("Cidade (atualizada):", getattr(pessoa, "cidade"))

