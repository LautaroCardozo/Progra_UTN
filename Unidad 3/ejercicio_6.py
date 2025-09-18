enteros = [28,44,404,54,12,331,122]
maximo = None
posicion = None

for i in range(len(enteros)):
    if maximo == None or enteros[i] > maximo:
        maximo = enteros[i]
        posicion = i

print(f"El maximo es {maximo} y se encuentra en la posicion {posicion + 1}")
