numeros = [0] * 10
acumulador = 0

for i in range(len(numeros)):
    numeros[i] = int(input("Ingrese un numero entero: "))

for i in range(len(numeros)):
    acumulador += numeros[i]

print(acumulador)

