from detection_morpho import model_detection
from capture_image import capture
from matplotlib import pyplot as plt
import csv
import json
import datetime

def image_processing(calibracion_ancho,calibracion_altura):
	#capture image
	try:
		log = []
		log.append({"event": "init_algoritm","date":datetime.datetime.now()})
		print({"event": "init_algoritm","tiempo":datetime.datetime.now()})
		
		imagen_path = capture()
		
		log.append({"event": "image_capture","date":datetime.datetime.now()})
		print({"event": "image_capture","date":datetime.datetime.now()})
		
		path_model = '/home/gideam/Desktop/sistema_crecimiento/src/best.pt'

		dis_min = 10
		resultados_objetos, results = model_detection(imagen_path, calibracion_ancho, calibracion_altura,path_model, distancia_minima=dis_min)
		log.append({"event": "image processing detection","date":datetime.datetime.now()})
		
		print({"event": "image processing detection","date":datetime.datetime.now()})
		return resultados_objetos,log
		
	except Exception as e: 
		log.append({"event": f"failed  image {e}","date":datetime.datetime.now()})
		print({"event": f"failed  image {e}","date":datetime.datetime.now()})
		return [],log

if __name__ == "__main__":

	calibracion_ancho = 1
	calibracion_altura = 1
	
	response, logs = image_processing(calibracion_ancho, calibracion_altura)
	# save info detection
	dir_data = '/home/gideam/Desktop/sistema_crecimiento/registers/detections.txt'
	dir_log = '/home/gideam/Desktop/sistema_crecimiento/registers/log.txt'
	if not response:
		logs.append({"event": "not detection or error","date":datetime.datetime.now()})
	else:
		archivo = open(dir_data,"a")
		for data in response:
			data["date"] = datetime.datetime.now()
			print(data)
			writer = csv.writer(archivo,delimiter=",")
			writer.writerow(data.values())
			
		archivo.close()
		logs.append({"event": f"{len(response)} detection and save","date":datetime.datetime.now()})
		
	archivo_log = open(dir_log,"a")
	for log in logs:
		writer = csv.writer(archivo_log,delimiter=",")
		writer.writerow(log.values())
	archivo_log.close()
			
		
		
		
    
