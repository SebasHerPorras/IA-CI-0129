import random

# Estado objetivo
objetivo = [1, 2, 3,
            4, 5, 6,
            7, 8, 0]  # 0 = espacio vacío

# Posiciones vecinas (arriba, abajo, izq, der) según el índice
vecinos = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def generar_puzzle(movimientos=30):
    estado = objetivo[:]
    pos_vacio = 8  # el 0 está al final
    
    for _ in range(movimientos):
        # elige un vecino al azar y mueve el vacío
        nuevo = random.choice(vecinos[pos_vacio])
        estado[pos_vacio], estado[nuevo] = estado[nuevo], estado[pos_vacio]
        pos_vacio = nuevo
    
    return estado

# Generar un tablero aleatorio
tablero = generar_puzzle(40)  # más movimientos = más aleatorio
print("Puzzle generado:")
for i in range(0, 9, 3):
    print(tablero[i:i+3])
