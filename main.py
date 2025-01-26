'''
istrubuidores ECOMODA necesita calcular
el precio de sus rutas logicas
cada ruta tiene clasificacion
-urbnas (cortas,medianas,grandes)
-rurales
1. si la ruta es menor a 10km-->corta
2. si la ruta es mayor a 10km y menor a 25km -->media
3. si la ruta es mator a 25 km se considera larga 
4. las rutas rurales tiene el mismo costo-2500000

requisitos:
Haga un listado DINAMICO de clientes
Haga un listado DINAMICO de rutas(ciudades)
costo corto-50 mil el km
costo medio-70 mil km
costo largo-100 mil el km

HAGA EL SOFTWARE POR CONSOLA UTILIZANDO RAMAS DE GIT

'''

costoUnitarioCorto = 50000  
costoUnitarioMedio = 70000 
costoUnitarioLargo = 100000  

costoViajeRural = 2500000  

listaClientes = []  
listaRutas = []  
opcion = 0


def calcular_costo_ruta(km, rutaRural):
    if rutaRural:
        return costoViajeRural
    elif km < 10:
        return km * costoUnitarioCorto
    elif 10 <= km < 25:
        return km * costoUnitarioMedio
    else:
        return km * costoUnitarioLargo

print("1. Registra cliente")
print("2. Registrar ruta")
print("3. Ver clientes")
print("4. Ver rutas")
print("5. Salir")

while opcion != 5:
    opcion = int(input("Digita una opción: "))
    
    if opcion == 1:
        print("Registrando un cliente")
        cliente = {
            "nombre": input("Digita tu nombre: "),
            "cedula": input("Digita cédula: "),
            "telefono": input("Digita tu teléfono: ")
        }
        listaClientes.append(cliente)
        print(f"Cliente registrado: {cliente}")
        
    elif opcion == 2:
        print("Registrando una ruta")
        cantidad_km = int(input("Digita la cantidad de km: "))
        ciudad = input("Digita la ciudad: ")
        rutaRural = input("¿Es una ruta rural? (sí/no): ").strip().lower() == "sí"
        
        costo_total = calcular_costo_ruta(cantidad_km, rutaRural)
        
        ruta = {
            "ciudad": ciudad,
            "km": cantidad_km,
            "costo_total": costo_total,
            "rural": rutaRural
        }
        
        listaRutas.append(ruta)
        print(f"Ruta registrada: {ruta}")
        
    elif opcion == 3:
        print("Lista de clientes:")
        for cliente in listaClientes:
            print(f"Nombre: {cliente['nombre']}, Cédula: {cliente['cedula']}, Teléfono: {cliente['telefono']}")
    
    elif opcion == 4:
        print("Lista de rutas:")
        for ruta in listaRutas:
            tipo_ruta = "rural" if ruta['rural'] else "urbana"
            print(f"Ciudad: {ruta['ciudad']}, Kilómetros: {ruta['km']}, Tipo: {tipo_ruta}, Costo total: {ruta['costo_total']}")
    
    elif opcion == 5:
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción inválida")