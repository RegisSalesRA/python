def handle_statuscode(status_code,response_data):
    
    if status_code == 200:
        if response_data:
            return response_data

    if status_code == 400:
        print({"error":"Esta passando algo que não deve! error 400"})
        
    elif status_code == 401:
        print("Você não tem autorização pra essa ação.")
        
    elif status_code == 403:
        print("Forbidden não tem permissão pra essa ação.")

    elif status_code == 404:
        print("Página não encontrada. Verifique a URL esta correta.")

    elif status_code == 405:
        print("Você esta tentando fazer uma ação que não pode nos verbos Http.")

    elif status_code == 500:
        print("Erro interno do servidor. Tente novamente mais tarde.")
    
    else:
        print("Erro desconhecido. LASCOU!!.")