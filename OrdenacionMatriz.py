# Función de Bubble Sort para ordenar una lista
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila_a_ordenar):
    if 0 <= fila_a_ordenar < len(matriz):
        # Ordenar la fila especificada
        bubble_sort(matriz[fila_a_ordenar])
        print(f"\nFila {fila_a_ordenar + 1} ordenada: {matriz[fila_a_ordenar]}")
    else:
        print("Índice de fila fuera de rango")


# Matriz de ejemplo 3x3
matriz = [
    [3, 1, 2],
    [9, 5, 7],
    [6, 4, 8]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Pedir al usuario el índice de la fila que desea ordenar
try:
    fila_a_ordenar = int(input("\nIntroduce el índice de la fila a ordenar (0-2): "))

    # Ordenar la fila especificada
    ordenar_fila(matriz, fila_a_ordenar)

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
except ValueError:
    print("Por favor, introduce un número válido.")
