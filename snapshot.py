import cv2
import numpy
import matplotlib
import gpiozero
from PIL import Image

im = Image.new("RGB", (640, 480), "white")
im.save('result.png')

camera = cv2.VideoCapture(0)
for i in range(10):
    return_value, image = camera.read()
    edges = cv2.Canny(image, 100, 200)
    edges = cv2.bitwise_not(edges)
    cv2.imwrite('opencv'+str(i)+'.png', edges)
    
image = cv2.imread('opencv1.png')    
result = cv2.imread('result.png')
combined = cv2.multiply(image, result)
cv2.imwrite('result.png', combined)
    

    
    
del(camera)
