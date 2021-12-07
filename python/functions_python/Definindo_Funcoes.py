"""
Definindo Funcoes

- Funcoes sao pequenos trechos de codigos que realizam tarefas especificas
- Pode ou nao receber entradas de dados e retornar uma saida de dados;
- Muito uteis para executar procedimentos simulares ou repetidas vezes

OBS: se voce escrever uma funcao que realiza varias tarefas dentro dela:
e bom fazer uma verificacao para que a funcao seja simplificada

Ja utilizamos varias funcoes desde que iniciamos este curso:
- print()
- max()
- min()
- len()
e varias outras
"""

# Exemplo de utilizacao  de funcoes

cores = ['verde','amarelo','azul','branco']

# Utilizando a funcao integrada (Built-in) do python print()
print(cores)

curso = 'programacao em python essencial'

print(curso)

cores.append('roxo')
print(cores)

# curso.append('Mais Dados...') # Attribute Error
# print(curso)

cores.clear()
print(cores)


# print(help(print()))

# DRY - dont repeat yourself - Nao repita voce mesmo / Nao repita seu codigo

# Mas entao, como definir funcoes?

"""
Em python , a forma geral de definir uma funcao 1

def nome_da_funcao(parametro_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> Sempre , com letras minusculas , e se for nome composto, separado por virgula (snake case):
parametros_de_entrada -> Opcionais,onde tendo mais de um , cada um separado por virgula,podendo ser opcionais ou nao
bloco_da_funcao -> tambem chamado de corpo da funcao ou implementacao, e onde processamento de funcao acontece
neste bloco, pode ter  ou nao retorno de funcao.

OBS: veja que para definir uma funcao , utlizamos a palavra reservada 'def' informando ao python que
estamos definindo uma funcao . tambem abrimos o bloco de codigo com o ja conhecido dois pontos : que e
utilizado em python para definir blocos.
"""

# Definindo a primeira funcao

def diz_oi():
    print('oi!')

"""
OBS: 

1 - veja que, dentro das nossas funcoes podemos utlizar outras funcoes
2 - veja que nossa funcao so executa uma tarefa, ou seja a unica coisa que ela faz e dizer oi;
3 - veja que esta funcao nao recebe nenhum parametro de entrada;
4 - veja que esta funcao nao retorna nada;
"""

# utilizando funcoes

# Chamada de execucao
diz_oi()

"""
ATENCAO:

Nunca esqueca de utlizar o paranteses ao executar uma funcao

Exemplo:

# Errado
diz_oi

# Certo
diz_oi()

# Errado
diz_oi ()
"""

def cantar_parabens():
    print('PArabens para voce')
    print('nesta data para voce')
    print('querida para voce')
    print('muitos anos  para voce')

for n in range(5):
    cantar_parabens()

# Em python,podemos inclusive criar variaveis do tipo de uma funcao e executar esta funcao atraves da variavel

canta = cantar_parabens()
canta()