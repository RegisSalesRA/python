import pandas as pd
from helpers.convert_string import formatar_valor

try:
    # Caminho do arquivo CSV e XLSX
    caminho_arquivo_csv = '../RelaçcaodepropriedadesdeBlocovariosmunicipios02ativassemGeorreferenciamento-06.04.2024.csv'
    caminho_arquivo_xlsx = '../RelaçcaodepropriedadesdeBlocovariosmunicipios02ativassemGeorreferenciamento-06.04.2024.xlsx'

    # Ler o DataFrame do arquivo CSV
    df = pd.read_csv(caminho_arquivo_csv)

    # Aplicar a formatação na coluna 'cpfcnpj'
    df['cpfcnpj'] = df['cpfcnpj'].apply(formatar_valor)

    # Salvar o DataFrame em um arquivo XLSX
    df.to_excel(caminho_arquivo_xlsx, index=False)

    print(f'Dados foram convertidos para XLSX e salvos em {caminho_arquivo_xlsx}')

except Exception as e:
    print(e)
