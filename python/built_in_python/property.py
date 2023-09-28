"""
property() em Python é uma função que permite criar atributos de propriedade em classes, 
o que fornece controle sobre o acesso, modificação e deleção de atributos de objeto.
 Ela é frequentemente usada junto com os decoradores @property, @atributo.setter, e @atributo.deleter para criar atributos de propriedade,
   também conhecidos como "getter" (para leitura), "setter" (para escrita) e "deleter" (para exclusão) de atributos.

Aqui está um exemplo simples de como usar property() e decoradores para criar um atributo de propriedade em uma classe:
"""


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo privado
        self._idade = idade  # Atributo privado
    
    @property
    def nome(self):
        """Getter para o atributo de nome."""
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        """Setter para o atributo de nome."""
        if isinstance(novo_nome, str):
            self._nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string.")
    
    @property
    def idade(self):
        """Getter para o atributo de idade."""
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        """Setter para o atributo de idade."""
        if isinstance(nova_idade, int) and nova_idade >= 0:
            self._idade = nova_idade
        else:
            raise ValueError("A idade deve ser um número inteiro não negativo.")
    
    @idade.deleter
    def idade(self):
        """Deleter para o atributo de idade."""
        print("Excluindo a idade.")
        del self._idade

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Alice", 30)

# Usando o getter
print("Nome:", pessoa.nome)  # Saída: Nome: Alice
print("Idade:", pessoa.idade)  # Saída: Idade: 30

# Usando o setter
pessoa.nome = "Bob"
pessoa.idade = 25

# Usando o


