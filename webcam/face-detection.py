import numpy as np
import cv2
import os
import shutil
from shutil import copyfile

name_list = os.listdir("detectedImages/")
for name in name_list:
   os.remove("detectedImages/" + name)

image_list = os.listdir("images/")
for image in image_list:
    img = cv2.imread('images/'+image,0)
    upperBody_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
    arrUpperBody = upperBody_cascade.detectMultiScale(img)
    if arrUpperBody != ():
        for (x,y,w,h) in arrUpperBody:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        print('body found')
        shutil.copy('images/'+image, 'detectedImages/')
    '''
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

