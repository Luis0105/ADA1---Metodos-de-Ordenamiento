# Función para el ordenamiento por el método de selección
def seleccion_nombres(lista):
    n = len(lista)
    for i in range(n):
        # Suponemos que el primer elemento no ordenado es el más pequeño
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        # Intercambiar el elemento encontrado con el primero no ordenado
        lista[i], lista[min_index] = lista[min_index], lista[i]
        print(f"{i + 1}° Pasada: {lista}")

nombres = []
cantidad = int(input("¿Cuántos nombres deseas ingresar? "))
print(f"Ingrese {cantidad} nombres cualesquiera: ")

for _ in range(cantidad):
    nombre = input("Ingrese el nombre: ")
    nombres.append(nombre)

print("\nNombres ingresados:", nombres)
print("\nProceso de ordenamiento paso por paso por el método de Selección:")
seleccion_nombres(nombres)
print("\nNombres ordenados:", nombres)
print()