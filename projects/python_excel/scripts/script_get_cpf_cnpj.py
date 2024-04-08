import pandas as pd
import math
from helpers.convert_string import formatar_valor

try:

    # Para obter o cpf e o cnpj de uma planilha rode esse script
    df = pd.read_excel('../RelaçcaodepropriedadesdeBlocovariosmunicipios02ativassemGeorreferenciamento-06.04.2024.xlsx')

    coluna = df["cpfcnpj"]
    print(coluna)

#    valores = [valor for valor in coluna if not math.isnan(valor)]
    valores = [valor for valor in coluna]

    with open('../dados.txt', 'w') as file:
        for valor in valores:
            file.write(str(valor) + '\n')

except Exception as e:
    print(e)
