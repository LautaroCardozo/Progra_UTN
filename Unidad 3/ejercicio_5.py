enteros = [17,28,44,404,54,12,331,122]

busqueda = int(input("Que numero quiere buscar?: "))
posicion = None
se_encontro = False

for i in range(len(enteros)):
    if enteros[i] == busqueda:
        posicion = i
        se_encontro = True

if  se_encontro:
    print(f"El valor {busqueda} se encuentra en la posicion {posicion + 1}")
else:
    print(f"No se encontro el valor {busqueda}")
