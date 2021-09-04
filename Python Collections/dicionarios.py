"""
Dicionarios

OBS: Em algumas linguagens de programacao , os dicionarios Python sao conhecidos
por mapas

Dicionarios sao colecoes do tipo chave/valor.

Dicionarios sao representados por chave {}

print(type({}))

OBS: Sobre dicionarios
    - Chave e valor sao separados por ":"  Ex: 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Criacao de dicionarios

# Forma 1 (Mais comum)

paises = {'br':'Brasil','eua':'Estados undiso','py':'Paraguay'}

# print(paises)
# print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil',eua='Estados undiso',py='Paraguay')
print(paises)
print(type(paises))

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
#print(paises['br'])
#print(paises['ru'])

# OBS: Caso tentamo fazer uma acesso utilizando uma chave que nao existe teremos o erro key error

# Forma 2 - Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))


# Acessando elementos

pais = paises.get('py', 'nao encontrado')

# caso o get nao encontre o objeto com a chave sera gerado o valor None e nao sera gerado um valor keyError

if pais:
    print(f'Encontrei o pais {pais} ')
else:
    print('Nao encontrei o pais')


# Podemos definir um valor padrao para caso nao encontremos o objeto com a chave informada
pais = paises.get('ru', 'nao encontrado')

print(f'Encontrei o pais {pais}')


# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int,float,string,boolean), inclusive lista, tupla dicionario,como chaves
# De dicionarios

# Tuplas por exemplos sao bastante interessantes de serem utilizadas como chave de dicionarios, pois as mesmas
# sao imutaveis.
localidades = {
    (35.6515, 32.3213): 'Escritorio em tokio',
    (50.6515, 42.3213): 'Escritorio em nova york',
    (78.6515, 12.3213): 'Escritorio em Sao paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 Mais comum

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mar':500}
receita.update(novo_dado) # receita.update({'mai':500})
print(receita)

print(sum(receita.values()))

# Atualizando dados de um dicionario

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai':600})

print(receita)

# CONCLUSAO 1: A forma de adicionar novos elementos  ou atualizar dados em um dicionario e a mesma.
# CONCLUSAO 2: Em um dicionarios, Nao podemos ter chaves repetidas.


# REmover dados de um dicionario

receita = {'jan':100,'fev':120,'mar':300}

print(receita)
# Forma 1 Mais comum
ret = receita.pop('mar')
print(ret)
print(receita)

# OBS 1: Aqui precisamos sempre informar a chave e caso nao encontre o elemento um KEyError e retornado!

# Forma 2

del receita['fev']

print(receita)
# Se a chave nao existir sera gerado um KEyError

# Adicionando o valor novamente
receita['fev']=500
print(receita)

#OBS nesse caso  o valor recebido nao e retornado!!

"""

# Imagine que voce tem um comercio eletronico
# onde temos um carrinho de compras onde adicionamos produtos
"""
Carrinho de compras:
    produto 1:
        -nome;
        -quandidade;
        -preco
    produto 2:
        -nome:
        -quantidade:
        -preco:

# - poderiamos utilizar uma Lista para isso? Sim


carrinho = []
produto1 = ['playstation 4', 1, 2303.00]
produto2 = ['god of war 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual  e o indice de cada informacao no produto .

# 2 - Poderiamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2399.00)
produto2 = ('God of war 4', 1, 2399.00)

carrinho = (produto1, produto2)
print(carrinho)

# Teriamos que saber qual  e o indice de cada informacao no produto .

carrinho = []

produto1 = {'nome': 'PLaystation', 'quantidade': 1, 'preco': 2303.00}
produto2 = {'nome': 'God of war 4', 'quantidade': 1, 'preco': 150}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# Podemos ter a certeza sobre cada informacao.


# Metodos de dicionarios.

d = dict(a=1,b=2,c=3)
print(d)
print(type(d))

# Limpar o dicionario (Zerar dados)

d.clear()
print(d)


# COpiando um dicionario para outro

# FOrma 1

# Deep Copy
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)


# Forma 2 # Shallow copy

novo = d
print(novo)
novo['d'] = 4

print(d)
print(novo)
"""


# Forma nao usual de criacao de dicionarios

outro = {}.fromkeys('a','b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome','pontos','email','profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O Metodo fromkeys recebendo dois parametros: um interavel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste','valor')
print(veja)

veja = {}.fromkeys(range(1,11),'novo')

print(veja)