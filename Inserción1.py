# Función para ordenar una lista usando el método de inserción directa
def insercion_derecha(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Mover los elementos de lista[0..i-1] que son mayores que clave a una posición adelante de su posición actual
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
        print(f"Inserción {i}: {lista}")

numeros = []
cantidad = int(input("¿Cuántos números deseas ingresar? "))
print(f"Ingrese {cantidad} números cualesquiera:")

for _ in range(cantidad):
    while True:
        try:
            numero = int(input("Número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

print("\nNúmeros ingresados:", numeros)
print("\nProceso de ordenamiento por inserción directa:")
insercion_derecha(numeros)
print("\nNúmeros ordenados:", numeros)
print()