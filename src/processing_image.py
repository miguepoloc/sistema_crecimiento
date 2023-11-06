"""
This file is in charge of processing the image and returning a data structure with the information of the image
"""

import numpy as np
from ultralytics import YOLO


class Morfologydetection:
    """
    A class for performing morphology detection.

    Args:
        route (str): The image route.
        raspberry_id (str): The Raspberry Pi ID.

    Attributes:
        router_image (str): The image route provided during initialization.
        model (str): The relative path to the model file used for morphology detection.
    """

    def __init__(self, **args):
        """
        Initializes the Morfologydetection class.

        Args:
            route (str): The image route.
            raspberry_id (str): The Raspberry Pi ID.
        """
        self.router_image = args['route']
        # relative path for the model(change for rspberry)
        self.model = YOLO('../model/best.pt')
        self.calibrationx = 1
        self.calibrationy = 2

    def predict_image(self):
        """
        Predicts the image.

        Returns:
            dict: The dictionary with the image information.
        """
        results = self.model(self.router_image, imgsz=1024)

        for result in results:
            print(result.masks)
            if result.masks:
                response = self.extrac_morphology(result.masks)
        return response

    def extrac_morphology(self, maks):
        response = {}
        for id, recorrido in enumerate(maks.xy):
            arr = np.array(recorrido)
            max_column_1 = np.max(arr[:, 0])
            max_column_2 = np.max(arr[:, 1])
            min_column_1 = np.min(arr[:, 0])
            min_column_2 = np.min(arr[:, 1])
            print(max_column_1, max_column_2, min_column_1, min_column_2)
            dif_y = max_column_1 - min_column_1
            dif_x = max_column_2 - min_column_2
            alto = dif_y * self.calibrationy
            ancho = dif_x * self.calibrationx
            print(alto, ancho)
            response[f"data_{id}"] = {'alto': alto, 'ancho': ancho}

        return response
