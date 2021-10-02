"""
Levantando os proprios erros com raise
raise -> Lanca excecoes
OBS: o raise nao e uma funcao e uma palavra reservada, assim como def ou qualquer outra python.
Para simlificar, pense no raise como sendo util para que possamos criar nossas proprias  excecoes e mensagens
de erro.
A forma geral de utilizacao e:
raise TipoDoerro('Mensagem de erro')
# Exemplo real
def colore(texto,cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} sera impresso na cor{cor}')
colore(2,2)
# Exemplo Real
def colore(texto,cor):
    cores = ('verde','amarelo','azul','branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre:{cores}')
    print(f'O texto {texto} sera impresso na cor {cor}')
colore('Geek University','cinza')
OBS: o Raise assim como return finaliza a funcao ! ou seja depois dele nada e executado
"""

# Exemplo Real

def colore(texto,cor):
    cores = ('verde','amarelo','azul','branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre:{cores}')
    print(f'O texto {texto} sera impresso na cor {cor}')

colore('Geek University','cinza')