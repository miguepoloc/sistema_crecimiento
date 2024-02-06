from funcion import modelo
from capture_image import capture
from matplotlib import pyplot as plt

image = capture()
#image = '/home/gideam/Desktop/sistema_crecimiento/src/prueba.JPG'
# Llamada a la función con tus listas de coordenadas y parámetros de calibración
imagen_path = image
calibracion_ancho = 1  # ejemplo de calibración para ancho
calibracion_altura = 1 # ejemplo de calibración para altura
dis_min = 10
resultados_objetos, results = modelo(imagen_path, calibracion_ancho, calibracion_altura, distancia_minima=dis_min)

# Imprimir los resultados para cada objeto
print("Resultados por objeto:")
print(resultados_objetos)



