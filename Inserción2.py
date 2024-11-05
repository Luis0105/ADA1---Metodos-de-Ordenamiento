# Función para ordenar una lista de nombres usando el método de inserción directa
def insercion_derecha(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Mover los elementos que son mayores que la clave a una posición adelante
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
        print(f"Inserción {i}: {lista}")

nombres = []
cantidad = int(input("¿Cuántos nombres deseas ingresar? "))
print(f"Ingrese {cantidad} nombres cualesquiera:")

for _ in range(cantidad):
    nombre = input("Nombre: ")
    nombres.append(nombre)
    
print("\nNombres ingresados:", nombres)
print("\nProceso de ordenamiento por inserción directa:")
insercion_derecha(nombres)
print("\nNombres ordenados:", nombres)
print()