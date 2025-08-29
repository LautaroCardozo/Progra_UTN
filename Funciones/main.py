from ejercicio_1 import saludar 
from ejercicio_2 import operaciones 
from ejercicio_3 import area_triangulo 
from ejercicio_4 import buscar_mayor 
from ejercicio_5 import es_par 
from ejercicio_6 import convertir_minutos 
from ejercicio_7 import verificar_acceso 
from ejercicio_8 import calcular_edad 

#Ejercicio 1
nombre = input("Ingrese su nombre: ")
saludar(nombre)
#Ejercicio 2
numero_1 = int(input("Ingrese un numero a operar: "))
numero_2 = int(input("Ingrese otro numero a operar: "))
operaciones(numero_1,numero_2)
#Ejercicio 3
base = float(input("Ingrese la base del triagulo: "))
altura = float(input("Ingrese la altura del triagulo: "))
area_triangulo(base,altura)
#Ejercicio 4
numero_1 = int(input("Ingrese un numero a operar: "))
numero_2 = int(input("Ingrese un numero a operar: "))
numero_3 = int(input("Ingrese un numero a operar: "))
print(buscar_mayor(numero_1,numero_2,numero_3))
#Ejercicio 5
numero_1 = int(input("Ingrese un numero: "))
print(es_par(numero_1))
#Ejercicio 6
minutos = int(input("Ingrese los minutos: "))
print(convertir_minutos(minutos))
#Ejercicio 7
edad = int(input("Ingrese su edad: "))
if verificar_acceso(edad):
    print("Acceso otorgado!!!")
else:
    print("Acceso denegado!!!")
#Ejercicio 8
anio_de_nacimiento = int(input("Ingrese el anio en el que nacio: "))
print(calcular_edad(anio_de_nacimiento))