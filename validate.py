def validate_number(numero_entrada :str, tipo: type):
    try:
        tipo(numero_entrada)
        retorno = True
        #return True
    
    except ValueError:
        retorno = False
        #return False
    return retorno


# validate_string