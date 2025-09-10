from puzzle import generarMatriz
from AnchoPrimero import anchoPrimero
import time

# -----------------------------
# Función para ejecutar y medir algoritmos
#funcion_busqueda es la función que implementa el algoritmo Y nombre_algoritmo es una cadena para identificar el algoritmo
def ejecutar_algoritmo(funcion_busqueda, nombre_algoritmo):
    objetivo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    N = 20
    tiempos = []
    movimientos_totales = []

    for i in range(N):
        inicial = generarMatriz()
        print(f"\nEjecución {i+1} - {nombre_algoritmo}:")
        for fila in inicial:
            print(fila)

        inicio = time.perf_counter()
        solucion = funcion_busqueda(inicial, objetivo)  # llamada al algoritmo
        fin = time.perf_counter()

        tiempo = fin - inicio
        tiempos.append(tiempo)

        if solucion:
            movimientos = len(solucion) - 1
            movimientos_totales.append(movimientos)
            print(f" Solución encontrada en {movimientos} movimientos, tiempo: {tiempo:.6f} s")
        else:
            print(f" No se encontró solución, tiempo: {tiempo:.6f} s")

    if movimientos_totales:
        print("\n--- Resultados promedio ---")
        print(f"Tiempo promedio: {sum(tiempos)/N:.6f} s")
        print(f"Movimientos promedio: {sum(movimientos_totales)/len(movimientos_totales):.2f}")

def menu():
    while True:
        print("\n===== Menú 8-Puzzle =====")
        print("1. Ancho Primero (BFS)")
        print("2. Ancho Primero Greedy (no implementado)")
        print("3. IDS (no implementado)")
        print("4. IDS Modificado (no implementado)")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_algoritmo(anchoPrimero, "Ancho Primero (BFS)")
        elif opcion == "2":
            print("⚠️ Opción aún no implementada.")
            # Aquí luego llamarías: ejecutar_algoritmo(greedy, "Ancho Primero Greedy")
        elif opcion == "3":
            print("⚠️ Opción aún no implementada.")
            # ejecutar_algoritmo(ids, "IDS")
        elif opcion == "4":
            print("⚠️ Opción aún no implementada.")
            # ejecutar_algoritmo(ids_modificado, "IDS Modificado")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
