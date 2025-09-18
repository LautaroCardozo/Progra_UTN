enteros_1 = [1,2,3,4,5]
enteros_2 = [1,2,3,6,5]
igualdad = True

for i in range(len(enteros_1)):
    if enteros_1[i] != enteros_2[i]:
        igualdad = False

if igualdad:
    print("Las listas son iguales")
else:
    print("Las listas son distintas")
