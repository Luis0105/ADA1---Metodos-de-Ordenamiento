# Función para el ordenamiento por el método de burbuja
def burbuja_nombres(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:  # Ordenar alfabéticamente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            print(f"{i+1}° Pasada, posición {j+1}: {lista}")

nombres = []
cantidad = int(input("¿Cuántos nombres deseas ingresar? "))
print(f"Ingrese {cantidad} nombres cualesquiera: ")

for _ in range(cantidad):
    nombre = input("Nombre: ")
    nombres.append(nombre)

print("\nNombres ingresados:", nombres)
print("\nProceso de ordenamiento por burbuja:")
burbuja_nombres(nombres)
print("\nNombres ordenados:", nombres)
print()