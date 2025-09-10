from puzzle import obtener_movimientos, mover

def encontrar_vacio(estado):
    """
    Encuentra la posición del espacio vacío (0) en el tablero
    """
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j
    return None, None

def DFS_limitado(estado, objetivo, limite, camino=[]):
    """
    Búsqueda en profundidad limitada
    """
    if estado == objetivo:
        return camino + [estado]
    
    if limite <= 0:
        return None
    
    f0, c0 = encontrar_vacio(estado)
    for fn, cn in obtener_movimientos(f0, c0):
        nuevo_estado = mover(estado, f0, c0, fn, cn)
        
        if nuevo_estado not in camino:
            resultado = DFS_limitado(nuevo_estado, objetivo, limite-1, camino + [estado])
            if resultado is not None:
                return resultado
    
    return None

def IDS(inicial, objetivo):
    """
    Iterative Deepening Search - Búsqueda por Profundización Iterativa
    """
    profundidad = 0
    
    while profundidad <= 50:  # Límite máximo para evitar loops infinitos
        resultado = DFS_limitado(inicial, objetivo, profundidad)
        if resultado is not None:
            return resultado
        profundidad += 1
    
    return None

