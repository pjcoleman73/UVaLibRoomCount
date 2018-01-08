# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())


#cap = cv2.VideoCapture('peopleCounter.avi') #Open video file
#cap = cv2.VideoCapture(0) #Open video file
cap = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True) #Create the background substractor

kernelOp = np.ones((3,3),np.uint8)
kernelCl = np.ones((11,11),np.uint8)

while True:
    frame = cap.read() #read a frame
    
    fgmask = fgbg.apply(frame) #Use the substractor
    
    try:        
        ret,imBin= cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
        mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
        mask = cv2.morphologyEx(mask , cv2.MORPH_CLOSE, kernelCl)

#        thresh1 = cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
#        opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
#        cv2.imshow('Background Substraction',opening)

        #cv2.imshow('Frame',frame)
        #cv2.imshow('Background Substraction',fgmask)

    except:
        #if there are no more frames to show...
        print('EOF')
        break
    
    _, contours0, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours0:
        cv2.drawContours(frame, cnt, -1, (0,255,0), 3, 8)

    cv2.imshow('Frame',frame)
    #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release() #release video file
cv2.destroyAllWindows() #close all openCV windows
