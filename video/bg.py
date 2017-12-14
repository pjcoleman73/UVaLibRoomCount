# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2

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

while True:
    frame = cap.read() #read a frame
    
    fgmask = fgbg.apply(frame) #Use the substractor
    
    try:        
        cv2.imshow('Frame',frame)
        cv2.imshow('Background Substraction',fgmask)
    except:
        #if there are no more frames to show...
        print('EOF')
        break
    
    #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release() #release video file
cv2.destroyAllWindows() #close all openCV windows
