import cv2
from picamzero import Camera
import math
import numpy as np
import time
import serial

def get_sidewalk(image):
    image = cv2.resize(image, (25, 25))
    is_sidewalk_array = []
    for row in image:
        row_pixels = []
        for pixel in row:
            if pixel[2] > 127:
                row_pixels.append(True)
            else:
                row_pixels.append(False)
        is_sidewalk_array.append(row_pixels)

    return is_sidewalk_array

def get_direction(sidewalk_array):
    threshold = 10 # adjust as needed
    grass_count_left = 0
    for row in range(int(len(sidewalk_array)/2 + 1), len(sidewalk_array)):
        for col in range(int(len(sidewalk_array[0])/2 + 1)):
            if not sidewalk_array[row][col]:
                grass_count_left += 1 # count grass pixels in the lower left quadrant
    grass_count_right = 0
    for row in range(int(len(sidewalk_array)/2 + 1), len(sidewalk_array)):
        for col in range(int(len(sidewalk_array[0])/2 + 1), len(sidewalk_array[0])):
            if not sidewalk_array[row][col]:
                grass_count_right += 1 # count grass pixels in the lower right quadrant
    if grass_count_left > threshold and grass_count_right > threshold:
        print("Both sides have grass")
        return "straight"
    elif grass_count_left > threshold:
        print("Left side has grass")
        return "right"
    elif grass_count_right > threshold:
        print("Right side has grass")
        return "left"
    else:
        return "straight"
    
print(get_direction(get_sidewalk(cv2.imread("/home/james/Downloads/IMG_5118.jpeg"))))



