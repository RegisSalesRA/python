# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
     return aluno['nota']


alunos_agrupoados = sorted(alunos, key=ordena)
# alunos_agrupoados = sorted(alunos, key=lambda n: n['nota'])
grupos = groupby(alunos_agrupoados, key=ordena)


for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)