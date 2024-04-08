import pandas as pd
from pyproj import Proj
import time
import re
from helpers.request_api_data import get_data_request_from_api


"""
Apos rodar o getscript pegue o arquivo gerado e coloque aqui para gerar o excel
baseado no arquivo que tenha os cpfs
normalmente deixo com o nome de dados.txt
"""


nome_arquivo = "relacao_de_propriedades_bloco_varios_municipios_2_api_values.xlsx"
myProf = Proj('+proj=utm +zone=24 +south +ellps=WGS84', preserve_units=False)
pattern = r"[-+]?\d*\.\d+"

def decimal_degrees_to_dms(dd, is_longitude=False):
    negative = dd < 0
    dd = abs(dd)
    minutes, seconds = divmod(dd*3600, 60)
    degrees, minutes = divmod(minutes, 60)
    direction = "S" if negative else "N"
    if is_longitude:
        direction = "W" if negative else "E"
    return f"{int(degrees)}°{int(minutes)}'{seconds:.1f}\"{direction}"

try:

    df = pd.read_excel(nome_arquivo)


    print("O maravilhoso arquivo existe!")

except FileNotFoundError:

    df = pd.DataFrame()
    print("O Arquivo de Excel nao existe meu fi,vou ter que criar né?")

data_nested = []

try:
    with open('../dados.txt', 'r') as file:
        for linha in file:
            print('waiting')
            time.sleep(1)
            cpf_cnpj = linha.strip()
            response_data = get_data_request_from_api(cpf_cnpj)
            if response_data is not None:
                data_nested.append(response_data)
            print('continue')


except FileNotFoundError:
    print('Arquivo "dados.txt" não encontrado.')


finally:
    if 'file' in locals() and not file.closed:
        file.close()

flattened_data = [item for sublist in data_nested for item in sublist]

unique_data = []

for item in flattened_data:
    if item not in unique_data:
        matches = re.findall(pattern, item['centroide'])
        longitudeGD, latitudeGD = myProf(matches[0], matches[1], inverse=True)
        latitudeDms = decimal_degrees_to_dms(latitudeGD)
        longitudeDms = decimal_degrees_to_dms(longitudeGD,is_longitude=True)
        googleMapCode = latitudeDms + " " + longitudeDms
        item['Latitude_gd'] = latitudeGD
        item['Longitude_gd'] = longitudeGD
        item['LatLong_GoogleMaps'] = googleMapCode
        item.pop('multipolygon', None)
        unique_data.append(item)

df_new = pd.DataFrame(unique_data)

df = pd.concat([df, df_new])

df.to_excel(nome_arquivo, index=False)

