"""

A função getattr() em Python é usada para obter o valor de um atributo de um objeto, dado o nome desse atributo como uma string.
 Ela é útil quando você deseja acessar dinamicamente atributos de objetos. Aqui está um exemplo de como usar getattr():
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Alice", 30)

# Usando getattr() para obter o valor de um atributo
nome = getattr(pessoa, "nome")
idade = getattr(pessoa, "idade")

# Imprimindo os valores dos atributos
print("Nome:", nome)
print("Idade:", idade)