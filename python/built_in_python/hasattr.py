"""
A função hasattr() em Python é usada para verificar se um objeto possui um determinado atributo ou método.
 Ela retorna True se o atributo ou método existe no objeto e False caso contrário. Aqui está um exemplo de como usar hasattr()
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Alice", 30)

# Verificando se o objeto possui um atributo chamado "nome"
tem_nome = hasattr(pessoa, "nome")

# Verificando se o objeto possui um método chamado "saudacao"
tem_metodo_saudacao = hasattr(pessoa, "saudacao")

# Verificando se o objeto possui um atributo chamado "endereco" (que não existe)
tem_endereco = hasattr(pessoa, "endereco")

# Imprimindo os resultados
print("Tem atributo 'nome'?", tem_nome)  # Saída: True
print("Tem método 'saudacao'?", tem_metodo_saudacao)  # Saída: True
print("Tem atributo 'endereco'?", tem_endereco)  # Saída: False


