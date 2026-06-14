import cv2
from picamzero import Camera
import math
import numpy as np
import time
import serial

def average_chunk(chunk):
    if (chunk.shape[0] * chunk.shape[1] == 0):
        return [0, 0, 0]
    average_rgb = [0, 0, 0]
    n = 0
    for row in range(chunk.shape[0]):

        for col in range(chunk.shape[1]):
            n += 1
            # (a - avg)/n + avg
            average_rgb[0] = (chunk[row][col][0] - average_rgb[0]) / n + average_rgb[0]
            average_rgb[1] = (chunk[row][col][1] - average_rgb[1]) / n + average_rgb[1]
            average_rgb[2] = (chunk[row][col][2] - average_rgb[2]) / n + average_rgb[2]
        
    
    
    return average_rgb


# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# try:
#     while True:
#         ser.write(b"icecream")
#         print("Sent data")
#         time.sleep(1)
# except:
#     ser.close()
#     print("clsoe the serial")


start = time.perf_counter()
cam = Camera()
image = cv2.imread("Photos/IMG_0833.jpeg")

image = cv2.resize(image, (25, 25))

cv2.imwrite("Photos/resized.jpeg", image)

is_sidewalk_array = []
for row in image:
    row_pixels = []
    for pixel in row:
        if pixel[2] > 127:
            row_pixels.append(True)
        else:
            row_pixels.append(False)
    is_sidewalk_array.append(row_pixels)

picture = []
for row in is_sidewalk_array:
    row_pixels = []
    for pixel in row:
        if pixel:
            row_pixels.append([255,255,255])
        else:
            row_pixels.append([0,0,0])
        
    picture.append(row_pixels)

cv2.imwrite("Photos/blackwhite.jpg", np.array(picture))