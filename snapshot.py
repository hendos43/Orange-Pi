import time
import cv2
import numpy
import matplotlib
import gpiozero
from PIL import Image

import keyboard

import os, sys
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
dirname = "test-" + timestr
os.mkdir(dirname)
subfolder = dirname + "/result"
os.mkdir(subfolder)


images = []


# create new blank image for compositing edge detection images onto
im = Image.new("RGB", (640, 480), "white")
im.save(subfolder + '/result.png')

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

def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            # print("OK")
            images.append(img)
            path_to_base = os.path.join(folder, "result")
            base = cv2.imread(os.path.join(path_to_base, "result.png"))
            combined = cv2.multiply(img, base)
            cv2.imwrite(os.path.join(path_to_base, "result.png"), combined)
        else:
            print("don't fucking work m8")
    return images



load_images_from_folder(dirname)

print(len(images))

# for i in images:
    # image = cv2.imread(subfolder + 'opencv1.png')    
    # result = cv2.imread('result.png')
    # combined = cv2.multiply(image, result)
    # cv2.imwrite('result.png', combined)
    
# on button press, capture colour image of orange peel
    
del(camera)
