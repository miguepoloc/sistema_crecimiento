#!/usr/bin/python
from picamera2 import Picamera2
import time


# Create an instance of Picamera2 class
picam2 = Picamera2()

picam2.start()

# Wait for 5 seconds
time.sleep(5)

picam2.capture_file(f"capture_{time.time()}.jpg")
