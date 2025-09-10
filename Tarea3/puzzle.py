import random
import copy
from collections import deque

# -----------------------------
# Generar tablero aleatorio y validarlo
# -----------------------------
def generarMatriz():
    """
    Genera un tablero 3x3 aleatorio resoluble
    """
    while True:
        numeros = list(range(9))
        random.shuffle(numeros)
        matriz = [numeros[i:i+3] for i in range(0, 9, 3)]
        if es_resoluble(matriz):
            return matriz

# -----------------------------
# Verificar si el tablero es resoluble
# -----------------------------
def es_resoluble(tablero):
    plano = sum(tablero, [])
    inversions = 0
    for i in range(len(plano)):
        for j in range(i+1, len(plano)):
            if plano[i] != 0 and plano[j] != 0 and plano[i] > plano[j]:
                inversions += 1
    return inversions % 2 == 0

# -----------------------------
# Movimientos válidos
# -----------------------------
def obtener_movimientos(fila, col):
    movimientos = []
    if fila > 0: movimientos.append((fila-1, col))  # arriba
    if fila < 2: movimientos.append((fila+1, col))  # abajo
    if col > 0: movimientos.append((fila, col-1))  # izquierda
    if col < 2: movimientos.append((fila, col+1))  # derecha
    return movimientos

# -----------------------------
# Mover ficha
# -----------------------------
def mover(matriz, f0, c0, fn, cn):
    nueva = copy.deepcopy(matriz)
    nueva[f0][c0], nueva[fn][cn] = nueva[fn][cn], nueva[f0][c0]
    return nueva
