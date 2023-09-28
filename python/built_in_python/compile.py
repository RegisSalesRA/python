"""
A função compile() em Python é usada para compilar uma string contendo código Python em um objeto de código ou bytecode Python.
O objeto de código pode ser executado posteriormente usando a função exec(), eval() ou eval() embutida. Aqui está um exemplo de como usar compile()
"""


# Define uma string contendo código Python
codigo_python = """
def saudacao(nome):
    return f"Olá, {nome}!"

mensagem = saudacao("Alice")
print(mensagem)
"""

# Compila a string de código Python em um objeto de código
codigo_compilado = compile(codigo_python, "<string>", "exec")

# Executa o código compilado
exec(codigo_compilado)
