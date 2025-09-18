enteros = [17,28,44,404,54,12,331,122]

contador = 0

for i in range(len(enteros)):
    if enteros[i] > 100:
        contador += 1

print(contador)