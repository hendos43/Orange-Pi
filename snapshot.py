import cv2
import numpy
import matplotlib
import gpiozero
from PIL import Image

import os
dirname = "test"
os.mkdir(dirname)

# create new blank image for compositing edge detection images onto
im = Image.new("RGB", (640, 480), "white")
im.save('result.png')

# open connection to webcam
camera = cv2.VideoCapture(0)

# on button press, collect images
# eventually, until button is pressed again

for i in range(10):
    return_value, image = camera.read()
    edges = cv2.Canny(image, 100, 200)
    edges = cv2.bitwise_not(edges)
    cv2.imwrite(os.path.join(dirname,'opencv'+str(i)+'.png'), edges)
    
# on button press (eventually when button is pressed again)
# multiply all images together and export as one image

image = cv2.imread('opencv1.png')    
result = cv2.imread('result.png')
combined = cv2.multiply(image, result)
cv2.imwrite('result.png', combined)
    
# on button press, capture colour image of orange peel
    
del(camera)
