import numpy as np
import cv2
cap = cv2.VideoCapture(0)
count = 0
import os

name_list = os.listdir("images/")
for name in name_list:
   os.remove("images/" + name)

name_list = os.listdir("detectedImages/")
for name in name_list:
   os.remove("detectedImages/" + name)

while True:
   # Capture frame-by-frame
   ret, frame = cap.read()

   # Our operations on the frame come here
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   name = 'images/'+"frame%d.jpg" % count
   cv2.imwrite(name, frame)

   #cv2.imwrite("frame%d.jpg" % ret, frame)     # save frame as JPEG file
   count +=1

   # Display the resulting frame
   cv2.imshow('frame',gray)
   if cv2.waitKey(10) != -1:
      break

   if(count>=200):
      break