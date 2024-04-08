import pandas as pd

from helpers.convert_string import formatar_valor


"""
Esse script foi criado para pegar somente os cpf de uma cidade
filtrando por cidades_desejadas confira se tem esse campo no excel
e normalmente o e nmmunicipio
pos isso ira gerar um excel com os dados filtrados por cidade 
"""

try:
    caminho_arquivo_original = '../relacao_de_propriedades_ativasa_sem_georreferenciamento_31.10.2023.csv'

    df_original = pd.read_csv(caminho_arquivo_original)
 
    cidades_desejadas = ['FORTALEZA']
 
    df_filtrado = df_original[df_original['nmmunicipio'].isin(cidades_desejadas)]
 
    
    for indice, linha in df_filtrado.iterrows():
        novo_valor_formatado = formatar_valor(linha['cpfcnpj'])
        df_filtrado.at[indice, 'cpfcnpj'] = novo_valor_formatado
    
    
    print(df_filtrado['cpfcnpj'])

    caminho_arquivo_filtrado = 'relacao_de_propriedades_fortaleza.xlsx'
    
    
    with pd.ExcelWriter(caminho_arquivo_filtrado, engine='openpyxl') as writer:
        df_filtrado.to_excel(writer, index=False, sheet_name='Sheet1')

    print("Dados filtrados foram salvos em:", caminho_arquivo_filtrado)
    
except Exception as e:
    print(e)

