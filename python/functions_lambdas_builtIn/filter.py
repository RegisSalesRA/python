
# filter

# filter() Serve para filtrar dados de uma determinada colecao

# Biblioteca para trabalhar com dados estatisticos
import statistics

# Dados coletados de algum sensor
dados = [1.2,2.7,0.8,4.1,4.3, -0.1]

# Calculando a media dos dados utilizando a funcao mean()
media = statistics.mean(dados)


# OBS: Assim como a funcao map a filter recebe dois parametros
# Sendo funcao e um interavel

res = filter(lambda x: x > media, dados)
print(list(res))

# Assim como a funcao map(), apos serem utilizados os dados de filter() eles sao excluidos da memoria

paises = ['','Argentina','','Brasil','','Chile','', 'Colombia','','Equador','','','Franca']

# res = filter(lambda pais: len(pais) > 0, paises)

# print(list(res))



# A diferenca entre map e filter E na map recebe dois parametros uma funcao e um interavel e retorna um objeto
# Mapeando uma funcao para cada elemento do interavel
# O filter tambem