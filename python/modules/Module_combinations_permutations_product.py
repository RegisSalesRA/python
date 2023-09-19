# Combinations, Permutations e Product - Itertools

# COmbinação - ORdem nao importa - iteravel + tamanho do grupo  (Nao se repete a combinacao)
# Permutacao - ordem importa ( Se repete as combinacoes )
# Produto - Ordem importa e repete valores unicos

from itertools import combinations , permutations , product


def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()


pessoas = [ 
    "Joao", "Joana", "Luiz", "Leticia"
]

camisetas = [
    ["Preta", "Branca"],
    ["p", "m", "g"],
    ["masculino", "feminino", 'unisex'],
    ["algodao", "polister"],
]

mulheres_album = [
    ["africana", "ruiva", "loira", "latina", "asiatica"],
    ["America do sul", "Europa", "Asia", "Oceania", "America do norte"],
    ["Fantasia outro genero", "Fantasia com mesmo genero"],
    ["Anã","Não Anã"]
]

#print_iter(combinations(pessoas,2))
#print_iter(permutations(pessoas,2))

print_iter(product(*mulheres_album))
