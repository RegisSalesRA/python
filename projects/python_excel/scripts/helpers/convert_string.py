def formatar_valor(valor):
  
    cumprimento_original = len(str(valor))

    if cumprimento_original == 14:
        valor_str = str(valor)
    else:
        valor_str = str(int(valor))

    tamanho = len(valor_str)
    
    if tamanho == 14:
        return f"{valor_str[:2]}.{valor_str[2:5]}.{valor_str[5:8]}/{valor_str[8:12]}-{valor_str[12:]}"
    
    if tamanho == 13:
        return f"0{valor_str[:1]}.{valor_str[1:4]}.{valor_str[4:7]}/{valor_str[7:11]}-{valor_str[11:]}"
    
    elif tamanho == 11:
        return f"{valor_str[:3]}.{valor_str[3:6]}.{valor_str[6:9]}-{valor_str[9:]}"

    elif tamanho == 10:
        return f"0{valor_str[:2]}.{valor_str[2:5]}.{valor_str[5:8]}-{valor_str[8:]}"

    elif tamanho == 9:
        return f"00{valor_str[:1]}.{valor_str[1:4]}.{valor_str[4:7]}-{valor_str[7:]}"

    elif tamanho == 8:
        return f"000.{valor_str[:3]}.{valor_str[2:5]}-{valor_str[6:]}"

    elif tamanho == 7:
        return f"000.0{valor_str[:2]}.{valor_str[2:5]}-{valor_str[5:]}"
        
    else:
        return valor_str
    
