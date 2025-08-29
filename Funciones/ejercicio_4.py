def buscar_mayor(a,b,c)->None:
    ordenados = None
    if a >= b and a >= c:
        if b >= c:
            ordenados = a,b,c
        else:
            ordenados = a,c,b
    elif b >= a and b >= c:
        if a >= c:
            ordenados = b,a,c
        else:
            ordenados = b,c,a
    else:
        if a >= b:
            ordenados = c,a,b
        else:
            ordenados = c,b,a
    return ordenados