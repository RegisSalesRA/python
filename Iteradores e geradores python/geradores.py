"""
Geradores

- Geradores (Generators) sao Iteraveis (Iteadores):

OBS: O contrario nao e veradeiro nem todo iterador e um generator

Outras informacoes:
- Generators podem ser criados com funcoes geradoras;
- Funcoes geradoras utilizam a palavra
- Generators podem ser criados com expressoes Geradoras;

Diferencas entre Funcoes e generator function( Funcoes Geradoras)

......................................................................
/ funcoes                      /  Generator Functions
/ utilizam return              /  utilizam yield
/ retorna uma vez              /  podem utilizar yield multiplas vezes
/ quando executada,retorna um valor / quanto executada,retorna um generator
```````````````````````````````````````````````````````````````````````
"""

# Exemplo Generator Function ( Funcao Geradora )

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

#OBS: Uma Generator Function nao e um Generator , Ela gera um generator, ok?

gen = conta_ate(5)

print(type(gen))