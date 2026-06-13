import cv2
from picamzero import Camera
import math
import numpy as np

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

cam = Camera()
cam.take_photo("skibidi.jpg")

image = cv2.imread("picture.jpeg")
image = cv2.resize(image, None, fx=0.05, fy=0.05)

num_rows = 10
num_cols = 10

row_size = math.ceil(image.shape[0] / num_rows)
col_size = math.ceil(image.shape[1] / num_cols)

squished = []
for row in range(num_rows):
    chunk_row = []
    for col in range(num_cols):

        y_start = row * col_size
        y_end = (row + 1) * col_size
        x_start = col * col_size
        x_end = (col + 1) * col_size
        
        chunk = image[y_start:y_end, x_start:x_end]
        chunk = average_chunk(chunk)
        chunk_row.append(chunk)

    squished.append(chunk_row)



cv2.imwrite("compressed.jpg", np.array(squished))
        