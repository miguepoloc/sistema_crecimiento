"""
This module is used to capture an image from the camera and save it in the specified route.
"""

from camera_controller import CameraController


def capture() -> str:
    """
    This function demonstrates the usage of the CameraController class to capture and save an image
    using a Raspberry Pi camera.

    Returns:
        str: The route (file path) of the saved image.
    """
    # Create a CameraController object
    camera_controller = CameraController()

    # Change the route and raspberry_id fields
    camera_controller.raspberry_id = "rpi_1"

    # Capture and save an image
    route = camera_controller.capture_and_save_image()

    print("Image saved in: " + route)

    return route


if __name__ == "__main__":
    capture()
