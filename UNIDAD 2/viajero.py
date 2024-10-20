import random
import math

# A) Generar los puntos
puntos = {
    'A': (10, 15),
    'B': (5, 5),
    'C': (12, 10),
    'D': (8, 6),
    'E': (6, 8),
    'F': (15, 5)
}

# B) Calcular la matriz de distancias usando la distancia euclidiana
def calcular_distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def crear_matriz_distancias(puntos):
    nodos = list(puntos.keys())
    matriz = {}
    for i in range(len(nodos)):
        matriz[nodos[i]] = {}
        for j in range(len(nodos)):
            if i != j:
                matriz[nodos[i]][nodos[j]] = calcular_distancia(puntos[nodos[i]], puntos[nodos[j]])
            else:
                matriz[nodos[i]][nodos[j]] = 0
    return matriz

# C) Definir po - punto de inicio
po = 'A'

def generar_solucion_aleatoria(nodos):
    solucion = random.sample(nodos, len(nodos))
    solucion.append(solucion[0])  
    return solucion

def calcular_fo(solucion, matriz_distancias):
    distancia_total = 0
    for i in range(len(solucion) - 1):
        distancia_total += matriz_distancias[solucion[i]][solucion[i + 1]]
    return distancia_total

nodos = list(puntos.keys())
matriz_distancias = crear_matriz_distancias(puntos)

solucion_aleatoria = generar_solucion_aleatoria(nodos)

valor_objetivo = calcular_fo(solucion_aleatoria, matriz_distancias)

print(f'Solución generada: {solucion_aleatoria}')
print(f'Valor objetivo (distancia total): {valor_objetivo:.2f}')
