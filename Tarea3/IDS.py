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

def DFS_limitado(estado, objetivo, limite, camino, visitados):
    if estado == objetivo:
        return camino[:]
    
    if limite <= 0:
        return None

    f0, c0 = encontrar_vacio(estado)
    for fn, cn in obtener_movimientos(f0, c0):
        nuevo_estado = mover(estado, f0, c0, fn, cn)
        t_nuevo = tuple(sum(nuevo_estado, []))  # estado como tupla

        if t_nuevo not in visitados:
            visitados.add(t_nuevo)
            camino.append(nuevo_estado)
            resultado = DFS_limitado(nuevo_estado, objetivo, limite-1, camino, visitados)
            if resultado is not None:
                return resultado
            camino.pop()
            visitados.remove(t_nuevo)

    return None

def IDS(inicial, objetivo):
    for profundidad in range(51):  # límite de seguridad
        visitados = {tuple(sum(inicial, []))}
        camino = [inicial]
        resultado = DFS_limitado(inicial, objetivo, profundidad, camino, visitados)
        if resultado is not None:
            return resultado
    return None


