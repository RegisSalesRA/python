"""
Recebendo dados do usuario

input() -> Todo dado recebido via input e di tipo string

Em python ,string e tudo que estiver entre:
- aspas simples;
- aspas duplas;
- aspas simples triplas;
- aspas duplas triplas;

Exemplo:

- aspas simples; 'Angel'
- aspas duplas;  "Angel"
- aspas simples triplas; '''Angel'''
"""
# - aspas duplas triplas; """Angel"""

#   Entrada de dados
print("Qual o seu nome? ")
nome = input() # Input -> Entrada

# Exemplo de print 'antigo' 2.x
#print('Seja bem-vindo(a) %s' % (nome))

#exemplo de print 'moderno' 3.x
#print('Seja bem-vindo {0}'.format(nome))

#exemplo de print 'moderno' 3.7
print(f'Seja bem-vindo! {nome}')

print("Qual a sua idade? %s" % nome)
idade = input()

# Processamento

# Saida de dados
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome,idade))

# exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos'.format(nome,idade))

# exemplo de print 'moderno' 3.7
print(f'A {nome} tem {idade} anos')


"""
    int(idade) => cast
    Cast e a conversao de um tipo de dado para outro
"""
print(f'A {nome} nasceu em {2018 - int(idade)}')