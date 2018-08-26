import numpy as np
import cv2
import pandas as pd

#cap = cv2.VideoCapture('video/FootBall.mp4')
cap = cv2.VideoCapture('video/people.avi')
fgbg = cv2.createBackgroundSubtractorMOG2()

kernel = np.ones((5, 5), np.uint8)
count = 0
while (1):
    ret, frame = cap.read()
    height, width, channels = frame.shape

    fgmask = fgbg.apply(frame)
    fgmask[fgmask < 200] = 0

    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

    fgmask2 = fgmask.copy()
    #fgmask2 = cv2.cvtColor(fgmask, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(fgmask2, 127, 255, 0)
    image, contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #print(len(contours))

    arrayCentour = []
    for i in range(0, len(contours)):
        cnt = contours[i]
        # mask = np.zeros(im2.shape,np.uint8)
        # cv2.drawContours(mask,[cnt],0,255,-1)
        x, y, w, h = cv2.boundingRect(cnt)

        if(w*h > 0.01*height*width):
            if(w >120):
                w = int(w/2)
                print(x, y, w, h)
                arrayCentour.append((x+w, y, w, h))
                cv2.rectangle(frame, (x+w, y), (x+w + w, y + h), (0, 255, 0), 2)


            print(x,y,w,h)
            arrayCentour.append((x, y, w, h))
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #cv2.imshow('Features', fgmask)
            #cv2.imwrite(str(i) + '.png', fgmask)

    cv2.imshow('frame', frame)
    cv2.imshow('fgmask', fgmask2)
    pd.DataFrame(arrayCentour).to_csv('frame/arrayCentour'+str(count)+'.csv',header=False,index=False)
    count = count + 1
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.imwrite(str(0) + '.png', fgmask)
cap.release()
cv2.destroyAllWindows()