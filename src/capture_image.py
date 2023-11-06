"""
This module is used to capture an image from the camera and save it in the specified route.
"""

# from camera_controller import CameraController
from processing_image import Morfologydetection


def capture() -> str:
    """
    This function demonstrates the usage of the CameraController class to capture and save an image
    using a Raspberry Pi camera.

    Returns:
        str: The route (file path) of the saved image.
    """
    # # Create a CameraController object
    # camera_controller = CameraController()

    # # Change the route and raspberry_id fields
    # camera_controller.raspberry_id = "rpi_1"

    # # Capture and save an image
    # route = camera_controller.capture_and_save_image()
    # Path Alex relative
    route = '../images/DSC_0088_JPG_jpg.rf.83725eb52fa35e5cc76786636486974f.jpg'
    detection = Morfologydetection(route=route)
    detection.predict_image()
    print("Image saved in: " + route)

    return route


if __name__ == "__main__":
    capture()
