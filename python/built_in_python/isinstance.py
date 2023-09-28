"""
A função isinstance() em Python é usada para verificar se um objeto é uma instância de uma classe ou de uma tupla de classes. Ela retorna True se o objeto for uma instância de uma das classes especificadas e False caso contrário.
 A função isinstance() é útil quando você deseja verificar o tipo de um objeto em tempo de execução.
   Aqui está um exemplo de como usar isinstance():
"""

# Definindo uma classe
class Pessoa:
    pass

# Criando uma instância da classe Pessoa
pessoa = Pessoa()

# Verificando se a instância é uma instância da classe Pessoa
resultado = isinstance(pessoa, Pessoa)
print("É uma instância da classe Pessoa?", resultado)  # Saída: True

