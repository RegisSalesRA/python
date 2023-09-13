"""
List Comprehension Map

"""


produtos = [
    {'nome': 'p1' , 'preco':20 },
    {'nome': 'p2' , 'preco':10 },
    {'nome': 'p3' , 'preco':30 },
]


novos_produtos = [produto for produto in produtos]

print(novos_produtos)


# Desempacotar

novos_produtos = [{**produto} for produto in produtos]

print(novos_produtos)

# Desempacotar e interando nos valores

novos_produtos = [ {**produto, 'preco':produto['preco'] * 1.05 } for produto in produtos]

print(novos_produtos)


# Desempacotar e interando nos valores com ternario

novos_produtos = [ {**produto, 'preco':produto['preco'] * 1.05 }
                   if produto['preco'] > 20 else {**produto}
                   for produto in produtos ]

print(novos_produtos, sep='\n')


#OBS: Repare que ele confere os valores e executa alteracao de acordo com o ternario no caso se for maior que 20
#  ele altera o valor do preco se nao so retorna o produto normal

