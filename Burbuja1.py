# Función para el ordenamiento por el método de burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                # Intercambiar los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            print(f"{i+1}° Pasada, posición {j+1}: {lista}")

numeros = []
cantidad = int(input("¿Cuántos números deseas ingresar? "))
print(f"Ingrese {cantidad} números:")

for _ in range(cantidad):
    while True:
        try:
            numero = int(input("Ingrese el número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

print("\nNúmeros ingresados:", numeros)
print("\nProceso de ordenamiento paso por paso por el método burbuja:")
burbuja(numeros)
print("\nNúmeros ordenados:", numeros)
print()