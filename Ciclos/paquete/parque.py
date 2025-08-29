def mostrar_atracciones():
    print("============Bienvenido a PythonLand==============")
    carrusel = None
    montania_rusa = None
    casa_del_terror = None
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    cantidad_atracciones = int(input("A cuantas atracciones quiere subir?: "))
    total = 0
    for _ in range(cantidad_atracciones):
        atraccion = input("A que atraccion quiere subir?: ")
        total += calcular_precio(atraccion)
        if atraccion == "carrusel":
            carrusel = puede_subir(edad,atraccion)
        elif atraccion == "montania rusa":
            montania_rusa = puede_subir(edad,atraccion)
        else:
            casa_del_terror = puede_subir(edad,atraccion)
            
    mostrar_resumen(edad,nombre,carrusel,montania_rusa,casa_del_terror,total)

def puede_subir(edad,atraccion):
    retorno = None
    if edad <= 6: 
        if atraccion == "carrusel":
            retorno = True
        
        else:
            retorno = False
    elif edad <= 11:
        if atraccion == "casa del terror":
            retorno = True
        else:
            retorno = False
    else:
        retorno = True
    return retorno

def calcular_precio(atraccion:str):
    retorno = None
    if atraccion == "carrusel":
        retorno = 800
    elif atraccion == "casa del terror":
        retorno = 1200
    else:
        retorno = 1500
    return retorno

def mostrar_resumen(edad,nombre,carrusel,montania_rusa,casa_del_terror,total):    
    print(f"Visitante {nombre}, edad {edad}")
    if carrusel:
        print("Pudo subir al carrusel")
    else:
        print("No pudo subir al carrusel")
    if montania_rusa:
        print("Pudo subir a la montania rusa")
    else:
        print("No pudo subir a la montania rusa")
    if casa_del_terror:
        print("Pudo subir a la casa del terror")
    else:
        print("No pudo subir a la casa del terror")
    print(f"El total es de {total}")
