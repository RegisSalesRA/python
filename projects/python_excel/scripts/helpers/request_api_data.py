import requests
from helpers.status_code import handle_statuscode
import time
import os
import dotenv

dotenv.load_dotenv()

SECRET_URL = os.getenv("URL")
SECRET_TOKEN = os.getenv("TOKEN")


def get_data_request_from_api(cpf_cnpj):
    url = f"{SECRET_URL}{cpf_cnpj}"
    token = SECRET_TOKEN
    headers = {
        'Authorization': f'Bearer {token}'
    }

    try:
    
        response = requests.get(url, headers=headers, timeout=20, )
        response.raise_for_status()
        response_data = response.json()
        return handle_statuscode(response.status_code,response_data)
    
    except requests.exceptions.Timeout as e:
        print(f'Erro de tempo limite na solicitação para {url}: {e}')
        return
    
    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação para {cpf_cnpj}: {e}')
    
    return None