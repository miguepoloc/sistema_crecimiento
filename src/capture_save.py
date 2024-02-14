#!/usr/bin/python
from picamera2 import Picamera2
import time

# Create an instance of Picamera2 class
picam2 = Picamera2()

# Set the resolution to the maximum possible value
picam2.resolution = (2592, 1944)

picam2.start()

# Wait for 5 seconds
time.sleep(5)

picam2.capture_file(f"capture_{time.time()}.jpg")
