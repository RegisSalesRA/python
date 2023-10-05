# Dada uma lista de palavras, crie uma nova lista que contenha apenas as palavras que começam com a letra "A"


nomes = ["Alice", "Bob", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel", "Helena", "Isabela", "João"]


lambda_achar_começa_com_a = lambda lista : [value for value in lista if "a" in value]

print(lambda_achar_começa_com_a(nomes))