import pandas as pd

"""
esse codigo e responsavel por juntar e mergear os dois excel
com os dados encontrados tudo mergeado por cpfcnpj
"""

try:

    excel_1 = pd.read_excel('../relacao_de_propriedades_bloco_varios_municipios_2_api_values.xlsx')
    excel_2 = pd.read_excel('../RelaçcaodepropriedadesdeBlocovariosmunicipios02ativassemGeorreferenciamento-06.04.2024.xlsx')

    merged_data = excel_1.merge(excel_2, on='cpfcnpj', how='outer')
    merged_data.to_excel('arquivo_excel_combinado_varios_municipios_2_ativa.xlsx', index=False)


except Exception as e:
    print(e)