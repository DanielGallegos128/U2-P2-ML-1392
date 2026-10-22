import numpy as np
# Daniel Gallegos NC 1392
# Ejemplos de Numpy Numerical Python
print("-- Espaciado Linealmente en array -- 1392")
arre = np.linspace(start=0,stop=5,num=5)
print(arre)
print("-- Matriz identidad en 2D array -- 1392")
matriz = np.eye(3)
print(matriz)
print("-- Genera numeros al azar (aleatorios) en 2D array -- 1392")
numale = np.random.random((3,4)) # Genera 12 numeros aleatorios
print(numale)
print("Genera 9 numeros aleatorios entre 0 y 1")
numale = np.random.random((3,3)) # Genera 12 numeros aleatorios
print(numale)
# como generar 9 numeros aleatorios comprendidos entre 1 y 20 
# con numpy en un arreglo de 3x3
print("Generar 9 numeros aleatroios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3,3)
print(arre)