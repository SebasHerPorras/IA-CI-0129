from puzzle import obtener_movimientos, mover

def manhattan(estado, objetivo):
    """
    Calcula la heurística de distancia Manhattan entre el estado actual y el objetivo

    """
    pos = {}
    for i in range(3):
        for j in range(3):
            pos[objetivo[i][j]] = (i, j)

    distancia = 0
    for i in range(3):
        for j in range(3):
            if estado[i][j] != 0:  # ignorar el espacio vacío
                oi, oj = pos[estado[i][j]]
                distancia += abs(i - oi) + abs(j - oj)
    return distancia


def ids_modificado(inicial, objetivo):
    """
    IDS modificado (IDA*) con heurística Manhattan.
    Recibe estado inicial y objetivo, devuelve el camino de estados.
    """

    # con manhattan se encuentra la solución óptima en numero mínimo de movimientos
    limite = manhattan(inicial, objetivo)

    # función recursiva de búsqueda
    # estado: estado actual, camino: lista de estados visitados, g: costo actual, limite: límite de f
    def search(estado, camino, g, limite):
        f = g + manhattan(estado, objetivo)
        # si f excede el límite, retornar None y el nuevo límite f para seguir buscando por otro camino en ancho
        # no sigue explorando este camino en profundidad lo que reduce el tiempo de ejecución
        # lo mas costoso por lo general es los ultimos niveles del árbol
        if f > limite:
            return None, f
        if estado == objetivo:
            return camino + [estado], f

        minimo = float("inf")

        # encontrar la posición del espacio vacío (0) 
        f0, c0 = encontrar_cero(estado)

        for fn, cn in obtener_movimientos(f0, c0):
            nuevo_estado = mover(estado, f0, c0, fn, cn)

            # evitar ciclos dentro del mismo camino, asemeja el guardasdo de estados visitados en BFS
            if nuevo_estado in camino:
                continue

            resultado, nuevo_limite = search(nuevo_estado, camino + [estado], g + 1, limite)
            if resultado is not None:
                return resultado, nuevo_limite
            minimo = min(minimo, nuevo_limite)

        return None, minimo

    while True:
        resultado, nuevo_limite = search(inicial, [], 0, limite)
        if resultado is not None:
            return resultado
        if nuevo_limite == float("inf"):
            return None
        limite = nuevo_limite

def encontrar_cero(estado):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j
