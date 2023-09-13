# Tipo string

# Em python , um dado e considero string sempre que estiver entre aspas

# ex: 'uma string' , '234', '1', 'True', '5,22'

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's bar"
print(nome)
print(type(nome))

#Caractere de escape quebra de linha
nome = 'Angel\nJolie'
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma uma lista de strings

# [0 , 1 ]
# ['geek','university']

print(nome.split()[0])
print(nome.split()[1])

# EXEMPLO 1:
# [0,1,2,3,4,5,6]
# ['g','e','r','q','g','t','s','q']
nome = 'Geek University'
print(nome[0:5]) # Slice de string
print(nome[5:15]) # Slice de string

# Exemplo 2
# [0,1,2,3,4,5,6]
# ['g','e','r','q','g','t','s','q']
nome = 'Geek University'

# [::1] -> Comece do primeiro elemento ,va ate o ultimo elemento e inverta

print(nome[::-1]) # Pythonico - inversao da string
# Substitua G por P na string nome
print(nome.replace('G','P'))

text = 'Socorram me subino onibus em marrocos'
print(text)

print(text[::-1])

nome = 'ana vic' # Palimedro
print(nome)

print(nome[::-1])

