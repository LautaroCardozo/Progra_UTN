def buscar_primera_aparicion(array:list,numero:int):
    posicion = -1
    for i in range(len(array)):
        if array[i] == numero:
            posicion = i+1 
    
    return posicion


abc = [121,342,377]
print(buscar_primera_aparicion(abc , 121))
