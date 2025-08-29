def verificar_acceso(edad:int)->bool:
    retorno = None
    if edad >= 18:
        retorno = True
    else:
        retorno = False
    return retorno

