from collections import deque
import heapq
import copy
from puzzle import obtener_movimientos, mover

def distancia_manhattan(estado, objetivo):
    distancia = 0
    for i in range(3):
        for j in range(3):
            if estado[i][j] != 0:  # No contar el espacio vacío
                valor = estado[i][j]
                # Encontrar posición objetivo
                for oi in range(3):
                    for oj in range(3):
                        if objetivo[oi][oj] == valor:
                            distancia += abs(i - oi) + abs(j - oj)
                            break
    return distancia

def encontrar_vacio(estado):
    """
    Encuentra la posición del espacio vacío (0) en el tablero
    """
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j
    return None, None

def anchoPrimeroGreedy(inicial, objetivo):
    # Heap: (heurística, contador, estado, camino)
    heap = [(distancia_manhattan(inicial, objetivo), 0, inicial, [])]
    visitados = set()
    contador = 0
    
    while heap:
        _, _, estado_actual, camino = heapq.heappop(heap)
        
        # Verificar si llegamos al objetivo
        if estado_actual == objetivo:
            return camino + [estado_actual]
        
        # Convertir a hash para visitados
        estado_hash = tuple(tuple(fila) for fila in estado_actual)
        if estado_hash in visitados:
            continue
        visitados.add(estado_hash)
        
        # Generar sucesores
        f0, c0 = encontrar_vacio(estado_actual)
        for fn, cn in obtener_movimientos(f0, c0):
            nuevo_estado = mover(estado_actual, f0, c0, fn, cn)
            heuristica = distancia_manhattan(nuevo_estado, objetivo)
            contador += 1
            heapq.heappush(heap, (heuristica, contador, nuevo_estado, camino + [estado_actual]))
    
    return None