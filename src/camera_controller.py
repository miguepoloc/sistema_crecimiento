"""
Code for controlling a camera and capturing and saving images.

Created by: Miguel Angel Polo Castañeda and Alexander Esteban Espinosa Valdez
Date: 2023-11-05
Last modified by: Miguel Angel Polo Castañeda
Date: 2023-11-05

Universidad del Magdalena (2023)
Electronics Engineering
Proyecto Sistemas Inteligentes
"""

import time
from datetime import datetime

from picamera2 import Picamera2


class CameraController:
    """
    Controls a camera and captures and saves images using the picamera2 library.
    """

    def __init__(self):
        """
        Initializes the CameraController class.

        Initializes the camera, route, and raspberry_id fields.
        """
        self.picam2 = Picamera2()
        self.route = "/home/gideam/Desktop/sistema_crecimiento/images/"
        self.raspberry_id = "rpi1"

    def capture_and_save_image(self):
        """
        Captures an image using the camera and saves it to a specified route with a unique filename.
        """
        # Generate a configuration for capturing a high-resolution still image
        config = self.picam2.create_still_configuration()

        # Apply the configuration to the camera system
        self.picam2.configure(config)

        # Start the camera system
        self.picam2.start()

        # Wait for 2 seconds to allow the camera to adjust to lighting conditions
        time.sleep(2)

        # Capture the image
        time_save = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        total_route = self.route + self.raspberry_id + "_" + time_save + ".jpg"
        self.picam2.capture_file(total_route)

        return total_route
