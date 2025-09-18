reales = [0] * 6
acumulador = 0

for i in range(len(reales)):
    reales[i] = float(input("Ingrese un numero real: "))

for i in range(len(reales)):
    acumulador += reales[i]

print(acumulador/len(reales))
