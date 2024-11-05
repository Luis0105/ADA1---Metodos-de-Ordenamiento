# Función para el ordenamiento por el método de selección
def seleccion(lista):
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

numeros = []
cantidad = int(input("¿Cuántos números deseas ingresar? "))

for _ in range(cantidad):
    while True:
        try:
            numero = int(input("Ingrese el número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

print("\nNúmeros ingresados:", numeros)
print("\nProceso de ordenamiento por selección:")
seleccion(numeros)
print("\nNúmeros ordenados:", numeros)
