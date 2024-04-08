import pandas as pd
from helpers.convert_string import formatar_valor

"""
Esse script foi criado para pegar somente os cpf de uma cidade
filtrando por cidades_desejadas confira se tem esse campo no excel
e normalmente o e nmmunicipio
pos isso ira gerar um excel com os dados filtrados por cidade
"""

try:
# Caminho do arquivo Excel
    caminho_arquivo_excel = '../Relacao_de_propriedades_de_Porteiras_ativas_sem_Georreferenciamento_11.03.2024.csv'

# Ler o DataFrame do arquivo Excel
    df = pd.read_excel(caminho_arquivo_excel)

# Aplicar a formatação na coluna 'cpfcnpj'
    df['cpfcnpj'] = df['cpfcnpj'].apply(formatar_valor)

# Escrever o DataFrame formatado de volta no arquivo Excel
    df.to_excel(caminho_arquivo_excel, index=False)

    print(f'Dados foram atualizados e salvos em {caminho_arquivo_excel}')


except Exception as e:
    print(e)
