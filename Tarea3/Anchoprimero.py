from collections import deque
from puzzle import obtener_movimientos, mover

def anchoPrimero(inicial, objetivo):
    """
    Búsqueda en anchura (BFS) usando deque
    """
    queue = deque([(inicial, [])]) # cola de estados y caminos
    visitados = set()
    resultado = None


    while queue:
        # se saca el primer estado y camino de la cola
        estado, camino = queue.popleft()

        if estado == objetivo:
            return  camino + [estado]

        estado_hash = tuple(tuple(fila) for fila in estado)
        if estado_hash in visitados:
            continue
        # marcar estado como visitado
        visitados.add(estado_hash)

        f0, c0 = encontrar_cero(estado)

        for fn, cn in obtener_movimientos(f0, c0):
            nuevo_estado = mover(estado, f0, c0, fn, cn)
            queue.append((nuevo_estado, camino + [estado]))

    return resultado

def encontrar_cero(estado):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j
    return None