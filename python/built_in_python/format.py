"""
A função format() em Python é usada para formatar uma string substituindo marcadores de posição por valores específicos.
 Você pode especificar os marcadores de posição na string usando chaves {} e, em seguida, fornecer os valores que deseja inserir nas posições correspondentes. 
Aqui estão alguns exemplos de como usar format()
"""


nome = "Alice"
idade = 30
mensagem = "Olá, meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem)

# Olá, meu nome é Alice e eu tenho 30 anos.


nome = "Bob"
idade = 25
mensagem = "Olá, meu nome é {0} e eu tenho {1} anos.".format(nome, idade)
print(mensagem)


nome = "Charlie"
idade = 35
mensagem = "Olá, meu nome é {nome} e eu tenho {idade} anos.".format(nome=nome, idade=idade)
print(mensagem)

