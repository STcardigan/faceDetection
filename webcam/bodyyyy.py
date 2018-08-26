import numpy as np
import sys
import cv2

body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
img = cv2.imread('body/body4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = body_cascade .detectMultiScale(gray, 1.1, 8)

for (x,y,w,h) in faces:
   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
   roi_gray = gray[y:y+h, x:x+w]
   roi_color = img[y:y+h, x:x+w]