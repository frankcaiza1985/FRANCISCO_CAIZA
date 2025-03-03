def buscar_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Si no se encuentra el valor


# Ejemplo de uso:
if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    valor = 5
    resultado = buscar_matriz(matriz, valor)
    if resultado:
        print(f"El valor {valor} se encuentra en la posición: {resultado}")
    else:
        print(f"El valor {valor} no se encontró en la matriz.")
