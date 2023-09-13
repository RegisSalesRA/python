"""

List Comprehension Filter

"""


produtos = [
    {'nome': 'p1' , 'preco':20 },
    {'nome': 'p2' , 'preco':10 },
    {'nome': 'p3' , 'preco':30 },
]


novos_produtos = [produto for produto in produtos if produto["preco"] < 20]

print(novos_produtos, sep=" ")


#OBS tudo na esquerda é map e na direita é filtro

novos_produtos = [ {**produto, 'preco':produto['preco'] * 1.05 }
                   if produto['preco'] > 20 else {**produto}
                   for produto in produtos if produto["preco"] <= 20]

print(novos_produtos, sep=" ")